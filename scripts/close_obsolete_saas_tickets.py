#!/usr/bin/env python3
"""Close stale SAAS tickets as Obsolete.

KEYS holds two batches: tickets assigned to me with no activity since before
2025 (already closed on 2026-11-11, skipped on rerun), and unassigned tickets
with no activity since before 2026.

The SAAS workflow is linear (Draft -> Open -> In Implementation ->
Implementation Done -> In Review -> Done), so each ticket is walked forward
one transition at a time until "To done" is available. That final transition
sets Resolution = Obsolete and adds a short cleanup comment. "Back to ..."
transitions are never used. Sub-tasks are processed first and Epics last so
parents never close before their children.

Credentials: Jira Cloud email + API token (basic auth). The token is read from
$JIRA_API_TOKEN, or prompted for (hidden input) when unset. Create one at
https://id.atlassian.com/manage-profile/security/api-tokens

Usage:
    python scripts/close_obsolete_saas_tickets.py                  # dry run (default)
    python scripts/close_obsolete_saas_tickets.py --apply          # close all tickets
    python scripts/close_obsolete_saas_tickets.py --apply --only SAAS-1214   # one ticket
    python scripts/close_obsolete_saas_tickets.py --apply --only SAAS-1697 SAAS-1760 \\
        --comment "Closed as Obsolete during backlog cleanup."    # any keys, custom comment

--only accepts any ticket key, including ones not in KEYS; listed keys keep
the given order, so pass sub-tasks before their parents.
"""

from __future__ import annotations

import argparse
import base64
import getpass
import json
import os
import sys
import urllib.error
import urllib.request

SITE = "https://exasol.atlassian.net"
EMAIL = "edis.shabi@exasol.com"
RESOLUTION = "Obsolete"
COMMENT = "Closed as Obsolete during backlog cleanup: no activity since before 2026."

# Forward transitions in preference order; the first one available is taken.
FORWARD: list[str] = [
    "To done",
    "To Review",
    "Implementation Done",
    "Start Implementation",
    "open",
]
MAX_STEPS = 6

# Open SAAS tickets assigned to me, last updated before 2025-01-01 (snapshot 2026-11-11).
# Order: Sub-tasks, then Tasks/Bugs/Improvements, then Epics.
KEYS: list[str] = [
    "SAAS-1123",  # In Implementation Done · Sub-task · Monitoring of backups on management node
    "SAAS-1239",  # In Implementation Done · Sub-task · Add region based downtime
    "SAAS-1105",  # In Implementation · Sub-task · Adapt temporary solution to get log files from S3 instead of
    "SAAS-571",  # In Implementation · Sub-task · Add cloud monitoring section
    "SAAS-1243",  # Draft · Sub-task · Optimize lambda function for large number of dbs
    "SAAS-1173",  # Draft · Sub-task · Design decisions and create the rest of the tickets
    "SAAS-1171",  # Draft · Sub-task · Automate installation of telegraf agent
    "SAAS-1172",  # Draft · Sub-task · Evaluate installation of agent on host machine
    "SAAS-1170",  # Draft · Sub-task · Integrate agent installation to c4
    "SAAS-1169",  # Draft · Sub-task · Evaluation of new monitoring stack
    "SAAS-1082",  # Draft · Sub-task · Improve error handling for the plugin
    "SAAS-953",  # Draft · Sub-task · Monitoring of backups
    "SAAS-919",  # Draft · Sub-task · Handle update (maintenance) window in monitoring
    "SAAS-808",  # Draft · Sub-task · Automatic cleanup of empty dashboards
    "SAAS-1043",  # Draft · Sub-task · Move other deployments to deployment instance
    "SAAS-1042",  # Draft · Sub-task · Create a technical user for deployments
    "SAAS-1268",  # Draft · Sub-task · DR scenario - Management database is corrupted for any reaso
    "SAAS-1216",  # Draft · Sub-task · Education
    "SAAS-1215",  # Draft · Sub-task · Slack discussions & support
    "SAAS-1175",  # Draft · Sub-task · Automatic monitoring for non-trial accounts
    "SAAS-1214",  # Draft · Sub-task · Meetings Edis
    "SAAS-1012",  # Draft · Sub-task · Fetch saas working copy & developer tools
    "SAAS-1217",  # Draft · Sub-task · Release
    "SAAS-860",  # Open · Sub-task · Monitoring of usage import
    "SAAS-1680",  # In Review · Task · Access to engineering AWS accounts
    "SAAS-1537",  # In Review · Task · find out on which aws account of Exasol a certain database i
    "SAAS-1519",  # In Review · Task · Athena access for usage analysis in prod-saas-customers
    "SAAS-1491",  # In Review · Task · Delete expired SaaS trial accounts
    "SAAS-1302",  # In Review · Improvement · Check and reduce number of actions if it is possible
    "SAAS-1446",  # In Implementation · Task · Move repository aws_cleanup into saas-infra
    "SAAS-1355",  # In Implementation · Task · Security updates of SaaS environments
    "SAAS-1702",  # Draft · Task · Please check instance tagging for SaaS account acc_gVe9NjHiQ
    "SAAS-1700",  # Draft · Task · Create technical User to connect Grafana
    "SAAS-1685",  # Draft · Task · Add additional 20.000 credits to Adidas Neptune PoC account
    "SAAS-1677",  # Draft · Bug · Request access to AWS
    "SAAS-1667",  # Draft · Bug · Access to Amazon Q & Quicksight
    "SAAS-1653",  # Draft · Task · Assist Eldar Valibayov with AWS DB
    "SAAS-1551",  # Draft · Task · Centralize the management of AWS instance profiles and roles
    "SAAS-1515",  # Draft · Task · Implement essential security measures to maximize the isolat
    "SAAS-1511",  # Draft · Task · Resize test master node
    "SAAS-1241",  # Draft · Task · Daily Backup Creation in case no daily backup was created
    "SAAS-1312",  # Draft · Bug · Check leftover script
    "SAAS-1417",  # Draft · Task · Implement monitoring of backups
    "SAAS-1418",  # Draft · Task · Implement lambda function to do security updates on SaaS
    "SAAS-1464",  # Draft · Task · Migrate saas-plugin to lambda function
    "SAAS-945",  # Draft · Task · Improvements on deployments
    "SAAS-1311",  # Draft · Bug · More usage than expected
    "SAAS-1420",  # Draft · Task · check archived pages in IPS confluence
    "SAAS-1308",  # Draft · Task · Migrate PIn Dev Thomas to CT as an experiment
    "SAAS-743",  # Draft · Task · Automate account creation
    "SAAS-1157",  # Draft · Task · Monitor and reduce number of hosts on Datadog
    "SAAS-1156",  # Draft · Bug · Infra monitors don't include Access Node
    "SAAS-1249",  # Draft · Task · Create a run command document to update bucketfs in old data
    "SAAS-1684",  # Open · Task · Check access to SaaS accounts for the support team.
    "SAAS-1590",  # Open · Task · access for release porcess
    "SAAS-1573",  # Open · Task · Privileges to deploy and use Protegrity REST Container for A
    "SAAS-1513",  # Open · Task · create a lambda user in master node with least privileges
    "SAAS-1494",  # Open · Task · Enable AWS users to switch role to  aws-exa-pin-ci1
    "SAAS-1475",  # Open · Task · Insufficient permissions to run "cdk bootstrap" in exa-aws-p
    "SAAS-1470",  # Open · Task · Access permissions for Cost Management are outdated
    "SAAS-1056",  # Open · Task · Create a statistics dashboard from state monitors
    "SAAS-442",  # In Implementation · Epic · Datadog Plugin for SaaS
    "SAAS-1512",  # Draft · Epic · Replace admin auth-token with a user account that has the le
    "SAAS-1307",  # Draft · Epic · Migrate old department accounts to CT
    "SAAS-1267",  # Draft · Epic · SaaS Disaster Recovery Tests
    "SAAS-1158",  # Open · Epic · Internal Monitoring Stack for SaaS
    # Unassigned open SAAS tickets, last updated before 2026-01-01 (snapshot 2026-11-11).
    # Same order: Sub-tasks, then Tasks/Bugs/Improvements, then Epics.
    "SAAS-264",  # Draft · Sub-task · Implement REST API for User Management
    "SAAS-263",  # Draft · Sub-task · Implement RPC API for User Management
    "SAAS-1753",  # Open · Task · AWS access to upload to  s3 buckets - x-u, x-pkg, x-p.
    "SAAS-1751",  # Open · Task · Requesting AWS scheduler permissions
    "SAAS-1710",  # Open · Bug · Unsubscribing to Databricks on AWS Marketplace
    "SAAS-1705",  # Open · Bug · exa-aws-se-test account - enable hourly granularity on cost 
    "SAAS-1586",  # Draft · Task · test to see who this gets assigned to
    "SAAS-1583",  # Draft · Task · please remove certain people from the email distribution lis
    "SAAS-1570",  # Draft · Task · Access Request for Viorel Bosneac and Mihail Alexandris - Sa
    "SAAS-1554",  # Draft · Task · Since my email changed, I don't have access to my existing a
    "SAAS-1553",  # Draft · Task · Antivirus creates significant load on my windows
    "SAAS-1542",  # Draft · Task · Dirk Beerbohm - AWS account setup issue
    "SAAS-1540",  # Open · Task · Who is responsible for 166629205485 account
    "SAAS-1534",  # Open · Task · Access to AWS billing and cost information
    "SAAS-1530",  # Open · Task · Additional permissions in AWS Account exa-aws-pin-dev
    "SAAS-1501",  # Open · Task · Auto assign SaaS tickets to Edis Shabi
    "SAAS-1498",  # In Review · Task · Please add following roles for user PieterjanSpoelders  on p
    "SAAS-1487",  # Draft · Task · Delete expired SaaS trial accounts
    "SAAS-670",  # Draft · Task · Implement 'is my IP whitelisted'
    "SAAS-626",  # Draft · Task · Testing
    "SAAS-597",  # Draft · Task · SaaS API Monitoring
    "SAAS-575",  # Draft · Task · Update DB-Schema
    "SAAS-534",  # Draft · New Feature · Multi-Region Support
    "SAAS-509",  # Draft · Task · Prevent deletion of last user
    "SAAS-479",  # Draft · Bug · c4_play_init has a wrong state
    "SAAS-477",  # Draft · Bug · The number of route entries is too high
    "SAAS-476",  # Draft · Bug · Burst balance of root disks is 0 after some usage
    "SAAS-462",  # Draft · Task · Implement metering REST-API
    "SAAS-436",  # Draft · Improvement · Move UUIDs to Hashtypes
    "SAAS-418",  # Draft · Task · Move Okta implementation to saas engine
    "SAAS-373",  # Draft · Bug · ClusterID is the same for additional clusters
    "SAAS-275",  # Draft · Task · Okta IAM POC - Backend
    "SAAS-273",  # Draft · Task · Switch to Pre-Built Images
    "SAAS-272",  # Draft · Task · Software Repository
    "SAAS-271",  # Draft · Task · Release Management Process Concept
    "SAAS-266",  # Draft · Task · Digital River Integration Check - Backend
    "SAAS-212",  # Draft · Improvement · DHCP option set
    "SAAS-69",  # Draft · Story · Delete & Suspend Account
    "SAAS-66",  # Draft · Story · Configure Organization Settings
    "SAAS-63",  # Draft · Story · Create 'Add Nodes (Advanced Options) on database' wizard
    "SAAS-54",  # Draft · Story · Create Getting Started dialog
    "SAAS-43",  # Draft · Task · Configure Payment Method Frontend
    "SAAS-41",  # Draft · Task · Extensions/Plugin System Frontend
    "SAAS-40",  # Draft · Task · Extensions/Plugin System UX
    "SAAS-15",  # Draft · Task · Implement 'Getting Started' items
    "SAAS-11",  # Draft · Story · Configure Payment Method/Information
    "SAAS-1496",  # Draft · Epic · Address items from the Amazon FTR
    "SAAS-431",  # Draft · Epic · Release-Management Process
    "SAAS-261",  # Draft · Epic · User & Access Management
    "SAAS-157",  # Draft · Epic · Cross cutting
    "SAAS-153",  # Draft · Epic · Usability & Testing
    "SAAS-145",  # Open · Epic · Authentication for SaaS
    "SAAS-140",  # Open · Epic · WebSQL via Websocket
    "SAAS-70",  # Draft · Epic · Security Settings for the Account
    "SAAS-55",  # Open · Epic · Manage Databases & Clusters
    "SAAS-49",  # Draft · Epic · Organization and Billing
    "SAAS-39",  # Draft · Epic · Extensions & Plug-ins
    "SAAS-19",  # Draft · Epic · Help and Assistance
    "SAAS-9",  # Open · Epic · Sign-Up
]


class Jira:
    def __init__(self, email: str, token: str) -> None:
        raw = f"{email}:{token}".encode()
        self.auth = "Basic " + base64.b64encode(raw).decode()

    def call(self, method: str, path: str, body: dict | None = None) -> dict:
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(
            f"{SITE}/rest/api/3{path}",
            data=data,
            method=method,
            headers={
                "Authorization": self.auth,
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                text = resp.read().decode()
                return json.loads(text) if text else {}
        except urllib.error.HTTPError as e:
            raise RuntimeError(f"{method} {path} -> {e.code}: {e.read().decode()[:500]}") from e

    def status(self, key: str) -> tuple[str, str, str | None]:
        f = self.call("GET", f"/issue/{key}?fields=status,resolution")["fields"]
        res = f["resolution"]["name"] if f.get("resolution") else None
        return f["status"]["name"], f["status"]["statusCategory"]["key"], res

    def transitions(self, key: str) -> dict[str, str]:
        data = self.call("GET", f"/issue/{key}/transitions")
        return {t["name"]: t["id"] for t in data["transitions"]}

    def transition(self, key: str, tid: str, comment: str | None) -> None:
        """Run a transition; a non-None comment marks the final close step."""
        body: dict = {"transition": {"id": tid}}
        if comment is not None:
            body["fields"] = {"resolution": {"name": RESOLUTION}}
            body["update"] = {"comment": [{"add": {"body": {
                "type": "doc",
                "version": 1,
                "content": [{"type": "paragraph", "content": [{"type": "text", "text": comment}]}],
            }}}]}
        self.call("POST", f"/issue/{key}/transitions", body)


def pick_forward(available: dict[str, str]) -> str | None:
    return next((name for name in FORWARD if name in available), None)


def close(jira: Jira, key: str, apply: bool, comment: str) -> bool:
    status, category, _ = jira.status(key)
    if category == "done":
        print(f"{key}: already {status}, skipping")
        return True
    if not apply:
        nxt = pick_forward(jira.transitions(key))
        print(f"{key}: [dry-run] {status} -> next '{nxt}' ... -> Done ({RESOLUTION})")
        return nxt is not None

    path = [status]
    for _ in range(MAX_STEPS):
        available = jira.transitions(key)
        name = pick_forward(available)
        if name is None:
            print(f"{key}: STOPPED at {path[-1]}; available: {', '.join(available) or 'none'}")
            return False
        jira.transition(key, available[name], comment if name == "To done" else None)
        status, category, res = jira.status(key)
        path.append(status)
        if category == "done":
            print(f"{key}: {' -> '.join(path)} (resolution: {res})")
            return True
    print(f"{key}: STOPPED after {MAX_STEPS} steps at {path[-1]}")
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--apply", action="store_true", help="perform the transitions (default: dry run)")
    parser.add_argument("--only", nargs="+", metavar="KEY", help="close these keys instead of KEYS (any ticket)")
    parser.add_argument("--comment", default=COMMENT, help="comment added on the final close step")
    parser.add_argument("--email", default=EMAIL)
    args = parser.parse_args()

    # dict.fromkeys de-duplicates while keeping the order given on the command line.
    keys = list(dict.fromkeys(k.upper() for k in args.only)) if args.only else KEYS
    outside = [k for k in keys if k not in KEYS]
    if outside:
        print(f"Not in the stale list (closing anyway): {' '.join(outside)}")

    token = os.environ.get("JIRA_API_TOKEN") or getpass.getpass("Jira API token: ")
    jira = Jira(args.email, token)

    failed: list[str] = []
    for key in keys:
        try:
            if not close(jira, key, args.apply, args.comment):
                failed.append(key)
        except RuntimeError as e:
            print(f"{key}: ERROR {e}")
            failed.append(key)
            if "-> 401" in str(e) or "-> 403" in str(e):
                print("Auth/permission error; aborting.", file=sys.stderr)
                return 1

    mode = "closed" if args.apply else "checked"
    print(f"\n{len(keys) - len(failed)}/{len(keys)} {mode}.")
    if failed:
        print("Needs attention: " + " ".join(failed))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
