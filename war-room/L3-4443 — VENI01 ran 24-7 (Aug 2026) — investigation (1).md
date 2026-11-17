---
account: acc_JLkQkqwHTuaFW9sqf-r-xQ
investigated: 2026-09-08
region: eu-west-1
status: in-review
tags:
- saas
- l3
- veni
- auto-stop
- investigation
ticket: L3-4443
---
# L3-4443 — VENI01 ran 24/7 (Aug 2026)

Investigation evidence collected 2026-09-08, with billing data, five Teams screenshots, cost-and-usage breakdown screenshots for VENI01 and VENI02, and invoice screenshots 901/936 supplied 2026-09-10. Related: [[SAAS-1834 — VENI restore additional cost (June–July 2026)]]

Editorial cleanup: 2026-09-10. The supplied `SAAS.CLUSTER_USAGE_INTERVALS` / `SAAS.PRICES` data covers VENI01 and VENI02 through 2026-09-10 07:06:13 UTC; other infrastructure and ticket observations remain dated 09-08 unless stated otherwise. Recorded observations are distinguished from inferred causes; unresolved evidence gaps are collected under [[#Missing information]].

**Disputed-run compute: $10,360.99** for VENI01's 2026-08-05 → 09-04 continuous run. The supplied data resolves the two billing legs and their price; it does not determine the approved credit. See [[#Compute billing evidence supplied 2026-09-10]].

**Tickets:** [L3-4443](https://exasol.atlassian.net/browse/L3-4443) (the complaint, In Review, Aleksandr Lipatev) · [L3-4267](https://exasol.atlassian.net/browse/L3-4267) (the restore, Resolved) · [L3-4264](https://exasol.atlassian.net/browse/L3-4264) (the offboarding that caused it, Resolved) · [SPOT-32540](https://exasol.atlassian.net/browse/SPOT-32540) (**the follow-up raised from this investigation** — alert when auto-stop cannot connect, Draft) · [SAAS-1833](https://exasol.atlassian.net/browse/SAAS-1833) (credits for restore consumption, Done) · [SPOT-31028](https://exasol.atlassian.net/browse/SPOT-31028) (v8 storage-metadata corruption, hypothesis only)

**Account** `acc_JLkQkqwHTuaFW9sqf-r-xQ`, eu-west-1, org `org_5ILMCr19rONe4Lxr`.

**Self-healing follow-up (2026-09-11):** [SPOT-32614](https://exasol.atlassian.net/browse/SPOT-32614) — automatically reconcile SaaS technical users when authentication or required permissions fail, replacing the manual technical-user post-migration steps. Linked to L3-4443 and the separate alerting story SPOT-32540. Scope and ownership are on the agenda for [[20260908 1-1 Edis#Action Items]]; this is planned work, not evidence of a deployed repair.

Added to [E6: SaaS: Engineering Phase](https://exasol.atlassian.net/wiki/spaces/SPOTSUP/pages/2677964868/E6+SaaS+Engineering+Phase), row 17, as **[Unplanned]** with the red background used for unplanned work.

**Repair evidence refreshed from L3-4443 (2026-09-11):** [comment 485359](https://exasol.atlassian.net/browse/L3-4443?focusedCommentId=485359) records the 09-08 manual `ALTER USER` credential synchronization for all three technical users on `Migration`, using `/kpcgenarvghd/<username>` SSM values. [Comment 485400](https://exasol.atlassian.net/browse/L3-4443?focusedCommentId=485400) verifies that idle measurements resumed and auto-stop stopped `Migration` at 16:58:03 UTC after its **120-minute** threshold. **VENI01 was not repaired.** This supersedes the earlier statements below that Migration's repair and post-repair idle check were unverified; it does not establish an automatic fix.

**Implementation requirement:** [SPOT-32614](https://exasol.atlassian.net/browse/SPOT-32614) must tolerate existing technical users and update their credentials in place, not skip them or drop/recreate them. Use the expected deployment secrets and grants from the [Recreate SaaS Users procedure](https://github.com/exasol/internal-knowledgebase/blob/main/SaaS/db-migration-to-saas.md#recreate-saas-users). The current [`db_system_init.py`](https://github.com/exasol/saas-terraform/blob/main/modules/ops-dispatcher/src/db_system_init.py) already has `_create_or_alter_user`; the follow-up should reuse that behavior for automatic repair. The separately missing select1 schedule was manually created in [comment 485374](https://exasol.atlassian.net/browse/L3-4443?focusedCommentId=485374); user synchronization alone does not recreate schedules.

**Chargebee customer:** [acc_JLkQkqwHTuaFW9sqf-r-xQ](https://exasol.chargebee.com/d/customers/acc_JLkQkqwHTuaFW9sqf-r-xQ) — customer-page link supplied by Mihai on 2026-09-10; the URL uses the same identifier as the SaaS account UUID. The page has not been independently retrieved.

**Primary source document:** the customer-facing RCA, [`RCA No SaaS Databases in Account - Case 96293.pdf`](<RCA No SaaS Databases in Account - Case 96293.pdf>) — local copy of [attachment `128736`](https://exasol.atlassian.net/rest/api/3/attachment/content/128736) on [L3-4267](https://exasol.atlassian.net/browse/L3-4267). See [[#The customer-facing RCA — L3-4267 attachment 128736]] below for what it says and where it is wrong.

---

## Timeline

Times are **UTC** unless marked CEST. saasdb rows are UTC; Jira/Slack/RCA are +0200. Events are ordered by their UTC-equivalent start time; date-only records have no known time within that day. **Teams display times are treated as CEST for placement**, matching the embedded 09:45 Jira comment to the existing 09:45:55 CEST record. The screenshots do not show their time zone, so these rows retain the displayed time and are marked **CEST (inferred)**. Terminal timestamps are preserved separately without assuming their time zone. Rows sourced from the RCA are marked; its `2026-07-30` date error is discussed below.

| when                                                            | what                                                                                                                                                                                                                                                                                                                                                     | source                                                                                                                                                                                                                                                     |
| --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **06-02 16:01 CEST**                                            | Salesforce offboarding case **00095779** created by Commercial Delivery — 24 days before the Jira ticket. Only source: the RCA timeline                                                                                                                                                                                                                  | RCA p.2                                                                                                                                                                                                                                                    |
| 06-24 11:17:38–11:17:43                                         | **The direct select1 schedule-creation fix is merged under SPOT-31207.** PR #1160 adds `CreateSelect1Sensor` after `CreateBackupSensor` in `database_create`. Its production deployment enters **WAITING**; test and staging subsequently succeed, but the production job runs no steps.                                                                 | [PR #1160](https://github.com/exasol/saas-terraform/pull/1160); [production job](https://github.com/exasol/saas-terraform/actions/runs/28094670177/job/83181034075)                                                                                        |
| 06-25                                                           | Deployment workflow changes: pushes to `main` deploy only to **test** and a limited set of **master** modules. Published `rc*` releases target staging; published `v*` releases target production. A later green main-branch run therefore does not establish production deployment of the select1 fix.                                                  | [PR #1162](https://github.com/exasol/saas-terraform/pull/1162); [release routing](https://github.com/exasol/saas-terraform/blob/4909b1b981783c6585e1d563878541e865b43d89/.github/workflows/deploy_release.yml)                                             |
| 06-26 13:05 CEST                                                | Gerardo: "go ahead and decommission this system"                                                                                                                                                                                                                                                                                                         | [L3-4264 c465004](https://exasol.atlassian.net/browse/L3-4264?focusedCommentId=465004)                                                                                                                                                                     |
| 06-26 12:25:57                                                  | A production deployment succeeds, but it is **Datadog agent deploy**: it updates `DATADOG_VERSION` on the updater Lambda. It does **not** run Terraform or update the database-create Step Function, even though its checkout contains the select1 fix.                                                                                                  | [Datadog deployment job](https://github.com/exasol/saas-terraform/actions/runs/28237875751/job/83657030266); [workflow](https://github.com/exasol/saas-terraform/blob/c3c366ec2a216194f6be5245a6b95f2531392dca/.github/workflows/datadog-agent-deploy.yml) |
| 06-27 09:26 CEST                                                | Bogdan: "keep their account and just remove the databases"                                                                                                                                                                                                                                                                                               | [L3-4264 c465194](https://exasol.atlassian.net/browse/L3-4264?focusedCommentId=465194)                                                                                                                                                                     |
| 06-29 07:34→11:27                                               | `EXA_DB` `S11uTYyGRDeIuR4wivF-3Q` (`yduqkiablvll`, 4 TB) and `EXA_DB_BACKUP` `yy3HwVzcTAmz-wLA-aSPfw` (`ajzgtxsafcyp`) deleted; EXA_DB flapped `todelete`/`deleting` ~4 h                                                                                                                                                                                | `SAAS.DATABASES`; [L3-4264 c465410](https://exasol.atlassian.net/browse/L3-4264?focusedCommentId=465410)                                                                                                                                                   |
| 06-30 08:48 CEST                                                | Salesforce case **00096293** opened Blocker — customer reports the cluster and DB gone, "can't resolve hostname". [L3-4267](https://exasol.atlassian.net/browse/L3-4267) created 08:55 CEST                                                                                                                                                              | RCA p.2; [L3-4267](https://exasol.atlassian.net/browse/L3-4267) description                                                                                                                                                                                |
| 06-30 09:32 CEST                                                | Edis: "VENI is offboarded, see L3-4264"                                                                                                                                                                                                                                                                                                                  | [L3-4267 c465702](https://exasol.atlassian.net/browse/L3-4267?focusedCommentId=465702)                                                                                                                                                                     |
| 06-30 09:56:19 / 09:57:50                                       | **Customer user** `marius.gundersen@venienergy.com` creates VENI01 + VENI02 at XS (also Database01, Database02 at 09:55)                                                                                                                                                                                                                                 | `SAAS.CLUSTERS` actor field                                                                                                                                                                                                                                |
| 06-30 12:24 CEST                                                | Valdrin posts both hostnames openly: VENI01 `cdoiwhqmybfjzldaookf26tzo4`, VENI02 `rq2n5jhonjbhdn42cuwgsr5gs4`                                                                                                                                                                                                                                            | [L3-4267 c465750](https://exasol.atlassian.net/browse/L3-4267?focusedCommentId=465750)                                                                                                                                                                     |
| **06-30 10:45:52**                                              | **auto-stop fires correctly on VENI01** (actor `auto-stop`) while still an empty XS DB                                                                                                                                                                                                                                                                   | `SAAS.CLUSTERS`                                                                                                                                                                                                                                            |
| 06-30 11:35:46 / 13:51:29                                       | root puts VENI01, then VENI02, into `maintenance`                                                                                                                                                                                                                                                                                                        | `SAAS.CLUSTERS`                                                                                                                                                                                                                                            |
| 06-30 13:40 CEST                                                | Edis: "backup procedure started for VENI01" — restore of the old EXA_DB into VENI01                                                                                                                                                                                                                                                                      | [L3-4267 c465787](https://exasol.atlassian.net/browse/L3-4267?focusedCommentId=465787)                                                                                                                                                                     |
| 06-30 15:31 CEST                                                | Edis verdict: restore only partially worked, fear of crash on next snapshot → "Use migration as we did for Adena. Migrate VENI01 to VENI02"                                                                                                                                                                                                              | [L3-4267 c465820](https://exasol.atlassian.net/browse/L3-4267?focusedCommentId=465820)                                                                                                                                                                     |
| 06-30 15:38 CEST                                                | Huddle — Gerardo "call?", Slackbot "A huddle started". The investigation attributes the Adena-style migration agreement to this call; no written decision record is cited                                                                                                                                                                                | slack                                                                                                                                                                                                                                                      |
| 06-30 14:34 (16:34 CEST)                                        | Edis's first backup attempt out of VENI01 **fails**: `Remote volume error: Protocol "s3" not supported or disabled in libcurl` (db-2025.1.11 / cos-8.60.19). Valdrin: "s3 bucket not supported"                                                                                                                                                          | [slack](https://teamexasol.slack.com/archives/C0BE3UKT56J)                                                                                                                                                                                                 |
| 06-30 20:51 CEST                                                | Clone VENI01→VENI02 via S3 `veni-backup` + IAM `veni-backup-svc`; restore reports success but VENI02 (db-2025.1.11) logs `PersistentStorageError: Block does not exist 52809728, 1`. VENI02 abandoned                                                                                                                                                    | [L3-4267 c465871](https://exasol.atlassian.net/browse/L3-4267?focusedCommentId=465871)                                                                                                                                                                     |
| 07-01 09:02 CEST (inferred)                                     | Teams meeting starts. Invitation notices name Gerardo Abihaggle and four others, Juergen Albertsen, Tomohiro Kobayashi, and Marcel Kempken; invitations do not establish attendance.                                                                                                                                                                     | [Screenshot 1](<L3-4443 - Teams 20260701 - 01.png>)                                                                                                                                                                                                        |
| 07-01 09:21 CEST (inferred)                                     | A message shares [L3-4267 comment 465750](https://exasol.atlassian.net/browse/L3-4267?focusedCommentId=465750), the earlier connection-hostname comment. The sender's name is not visible.                                                                                                                                                               | [Screenshot 1](<L3-4443 - Teams 20260701 - 01.png>)                                                                                                                                                                                                        |
| **07-01 07:45:55** (09:45:55 CEST)                              | **Mihai Dinca records the plan: "we create VENI03 and use examigration from VENI01 → VENI03"** — per Mihai, minutes of a call, not his own decision; decision-maker not recorded                                                                                                                                                                         | [L3-4267 c466075](https://exasol.atlassian.net/browse/L3-4267?focusedCommentId=466075)                                                                                                                                                                     |
| 07-01 09:46 CEST (inferred)                                     | A screenshot of Mihai's 09:45 Jira comment is shared: **"Decision: we create VENI03 and use examigration from VENI01 → VENI03"**. This is the same plan recorded in [c466075](https://exasol.atlassian.net/browse/L3-4267?focusedCommentId=466075), now also evidenced in the meeting chat.                                                              | [Screenshot 1](<L3-4443 - Teams 20260701 - 01.png>)                                                                                                                                                                                                        |
| 07-01 09:53 CEST (inferred)                                     | Marcel supplies `confd_client db_start db_name: DB1 maintenance: true`.                                                                                                                                                                                                                                                                                  | [Screenshot 1](<L3-4443 - Teams 20260701 - 01.png>)                                                                                                                                                                                                        |
| 07-01 09:54 CEST (inferred)                                     | Edis posts a `root@n10` attempt using **VENI01's cluster UUID**: `confd_client db_start db_name: ENyLHgzASpysYHOUXXp5dw maintenance: true`. Result: **`UsageError: db_start: Database is already running`**. Marcel replies, "stop it first". This attempt did not start the DB.                                                                         | [Screenshot 1](<L3-4443 - Teams 20260701 - 01.png>)                                                                                                                                                                                                        |
| 07-01 09:55 CEST (inferred; terminal 09:55:22, zone not shown)  | Edis posts **"Try to start system in maintenance mode"** followed by **"System started successfully in partition 4886."** The continuation documents a successful maintenance-mode start. The output itself does not repeat the DB UUID; the preceding command identifies VENI01.                                                                        | [Screenshot 2](<L3-4443 - Teams 20260701 - 02.png>)                                                                                                                                                                                                        |
| 07-01 09:55 CEST (inferred)                                     | Marcel: **"please change the port"**, **"anyone can now access the database without a proper password"**. He lists: "1. stop db again / 2. change port / 3. start maintenance mode". This records a warning and instructions, not proof of external access or completed mitigation.                                                                      | [Screenshot 2](<L3-4443 - Teams 20260701 - 02.png>)                                                                                                                                                                                                        |
| 07-01 09:56–09:57 CEST (inferred)                               | Edis asks "change port ?" and "8563 ? how to do it?"; Marcel specifies "database port" and supplies `confd_client db_configure db_name: exa_db port: 18563`. No execution result for that command is shown.                                                                                                                                              | [Screenshot 2](<L3-4443 - Teams 20260701 - 02.png>)                                                                                                                                                                                                        |
| 07-01 09:58 CEST (inferred)                                     | Fardin Sabzi: **"I have a meeting with customer, need to drop off"**. This is a customer-contact lead, not a record of what was communicated.                                                                                                                                                                                                            | [Screenshot 2](<L3-4443 - Teams 20260701 - 02.png>)                                                                                                                                                                                                        |
| 07-01 09:59 CEST (inferred)                                     | Edis posts a clipped parameter line showing `/opt/exasol/cos-8.60.19/bin/dwa_wrapper` and `-dbName ENyLHgzASpysYHOUXXp5dw`. Remaining flags are outside the visible area. A nearby specification image lists **2 vCPUs, 16 GiB memory, 8 GiB per vCPU**, without a visible instance-type label.                                                          | [Screenshot 3](<L3-4443 - Teams 20260701 - 03.png>)                                                                                                                                                                                                        |
| 07-01 10:14–10:15 CEST (inferred)                               | A message asks, **"Is there a place documenting the procedure for backup creation, verification and restore?"** The sender's name is not visible. Edis replies, "ok give me 10mins and I'll be back"; no procedure link or substantive answer is shown in these extracts.                                                                                | [Screenshot 3](<L3-4443 - Teams 20260701 - 03.png>)                                                                                                                                                                                                        |
| 07-01 08:49:25–08:54:37                                         | The latest successful main-branch deploy before `Migration` is created runs **test / deploy** and **master / deploy** only. There is no production job in this run.                                                                                                                                                                                      | [Deployment run](https://github.com/exasol/saas-terraform/actions/runs/28505369322)                                                                                                                                                                        |
| 07-01 11:00 CEST (inferred)                                     | Edis shares [the AWS access portal](https://exasol-ct.awsapps.com/start).                                                                                                                                                                                                                                                                                | [Screenshot 3](<L3-4443 - Teams 20260701 - 03.png>)                                                                                                                                                                                                        |
| 07-01 11:06 CEST (inferred)                                     | Edis posts **`24TAKI_mQOahKMm2FiGlpw`**, VENI01's database UUID.                                                                                                                                                                                                                                                                                         | [Screenshot 3](<L3-4443 - Teams 20260701 - 03.png>)                                                                                                                                                                                                        |
| 07-01 11:12 CEST                                                | Slack DM created (Gerardo, Marcel, Edis, Valdrin, Bogdan, Mihai) — after the decision                                                                                                                                                                                                                                                                    | [`C0BE3UKT56J`](https://teamexasol.slack.com/archives/C0BE3UKT56J)                                                                                                                                                                                         |
| 07-01 11:21 CEST (inferred)                                     | Marcel shares an **`r5d.4xlarge`** specification link. Its visible Vantage preview describes **16 vCPUs and 128 GiB memory**. This shows sizing discussion, but does not state the chosen cluster topology or why VENI01 was left at Medium.                                                                                                             | [Screenshot 3](<L3-4443 - Teams 20260701 - 03.png>)                                                                                                                                                                                                        |
| 07-01 10:18:56                                                  | root creates the third DB — actual name `Migration`, `jLoRP5ZSSF-NQuh898tzvw` / `kpcgenarvghd`, at Large                                                                                                                                                                                                                                                 | `SAAS.CLUSTERS`                                                                                                                                                                                                                                            |
| **07-01 10:23:13**                                              | **root scales VENI01 XS → M. Not scaled back after migration; customer returns it to XS on 09-04**                                                                                                                                                                                                                                                       | `SAAS.CLUSTERS`                                                                                                                                                                                                                                            |
| 07-01 12:29 CEST (inferred)                                     | Marcel: **"scaling worked this time"**. The message does not name the database; it cannot alone identify which recorded resize succeeded.                                                                                                                                                                                                                | [Screenshot 4](<L3-4443 - Teams 20260701 - 04.png>)                                                                                                                                                                                                        |
| 07-01 12:31 CEST (inferred)                                     | Edis posts **`jLoRP5ZSSF-NQuh898tzvw`**, the `Migration` database UUID.                                                                                                                                                                                                                                                                                  | [Screenshot 4](<L3-4443 - Teams 20260701 - 04.png>)                                                                                                                                                                                                        |
| 07-01 12:42 CEST (inferred)                                     | Marcel posts `172.16.122.0/24` and `172.16.131.0/24`. Their intended network use and any applied change are not stated.                                                                                                                                                                                                                                  | [Screenshot 4](<L3-4443 - Teams 20260701 - 04.png>)                                                                                                                                                                                                        |
| 07-01 13:12 CEST                                                | Gerardo: "connection string for the **final database** for Veni?"                                                                                                                                                                                                                                                                                        | [slack](https://teamexasol.slack.com/archives/C0BE3UKT56J/p1782904328702049)                                                                                                                                                                               |
| 07-01 13:20 CEST                                                | Edis: `vgd2ki3glrb57h5jby5yvplieq` — "**It's not available to the customer yet.** Once the migration is complete, we still need to perform some additional configuration before the customer can see the database in the UI"                                                                                                                             | [slack](https://teamexasol.slack.com/archives/C0BE3UKT56J/p1782904848957079)                                                                                                                                                                               |
| 07-01 14:37 CEST (inferred)                                     | Teams records the meeting ending after **5h 34m 58s**.                                                                                                                                                                                                                                                                                                   | [Screenshot 4](<L3-4443 - Teams 20260701 - 04.png>)                                                                                                                                                                                                        |
| 07-01 14:38–15:06 CEST (inferred)                               | Edis asks Marcel "how is going ?"; Marcel replies "I'm checking now". Teams records another meeting starting at **15:06**.                                                                                                                                                                                                                               | [Screenshot 4](<L3-4443 - Teams 20260701 - 04.png>)                                                                                                                                                                                                        |
| 07-01 15:06 CEST (inferred)                                     | Swen Elges: "curious also..." and **"we have a customer call at 15:30h... waiting for your update"**, addressed to Marcel.                                                                                                                                                                                                                               | [Screenshot 4](<L3-4443 - Teams 20260701 - 04.png>)                                                                                                                                                                                                        |
| 07-01 15:12 CEST (inferred)                                     | Marcel: **"Migration is done"**, followed by **"let me start the new database is normal mode"**. The first reports migration completion; the second states an intention to start the new database in normal mode, not the result of that start.                                                                                                          | [Screenshot 5](<L3-4443 - Teams 20260701 - 05.png>)                                                                                                                                                                                                        |
| 07-01 15:13–15:15 CEST (inferred)                               | Swen: "uu... can it be... so fast?" and "we are in the call... if you wanna join". Marcel says he cannot join because of his internet connection and confirms "yes, it can be so fast".                                                                                                                                                                  | [Screenshot 5](<L3-4443 - Teams 20260701 - 05.png>)                                                                                                                                                                                                        |
| 07-01 15:38 CEST (inferred)                                     | Gerardo posts **`petter.skjolden+exasol@venienergy.com`**. The address is a contact lead; the screenshot does not show an email being sent or its contents.                                                                                                                                                                                              | [Screenshot 5](<L3-4443 - Teams 20260701 - 05.png>)                                                                                                                                                                                                        |
| 07-01 13:54:27                                                  | root scales `Migration` Large → Small; `running` at 14:07:06 — **no later stop recorded through 09-08**                                                                                                                                                                                                                                                  | `SAAS.CLUSTERS`                                                                                                                                                                                                                                            |
| 07-01 16:36 CEST (inferred; invitation earlier, time not shown) | Vahid Zangeneh is invited; the invitation time is not shown. Teams records the second meeting ending at **16:36**, duration **1h 30m 36s**.                                                                                                                                                                                                              | [Screenshot 5](<L3-4443 - Teams 20260701 - 05.png>)                                                                                                                                                                                                        |
| 07-01 17:24 CEST                                                | Edis: "Ensure Stefan stops the database after checking logs… we don't want to waste customer credits"                                                                                                                                                                                                                                                    | [L3-4267 c466302](https://exasol.atlassian.net/browse/L3-4267?focusedCommentId=466302)                                                                                                                                                                     |
| 07-01 17:18 (19:18 CEST)                                        | Marcel Kempken: *"Hi, is **the old cluster** stopped? If not can someone do it?"* — VENI01 is called the *old* cluster once `Migration` is live. The request precedes the recorded stop; a causal link is inferred                                                                                                                                       | [slack](https://teamexasol.slack.com/archives/C0BE3UKT56J)                                                                                                                                                                                                 |
| **07-01 18:14:02**                                              | **root parks VENI01 in `stopped`** — an ordinary customer state, not `maintenance`                                                                                                                                                                                                                                                                       | `SAAS.CLUSTERS`                                                                                                                                                                                                                                            |
| 07-03                                                           | RCA issued (`Root Cause Analysis`, dated 03.07.2026); attached to L3-4267 on 07-07 10:56                                                                                                                                                                                                                                                                 | RCA p.1                                                                                                                                                                                                                                                    |
| **07-03 09:28 CEST**                                            | **Confirmation to the customer: the database is running normally and the data loading is complete.** Closing event of the recovery as far as the RCA is concerned                                                                                                                                                                                        | RCA p.2                                                                                                                                                                                                                                                    |
| 07-14 08:30:34                                                  | L3-4267 auto-resolved `Success` by Automation for Jira when the Salesforce case closed — no human closed it, last human action 07-01 16:08                                                                                                                                                                                                               | L3-4267 changelog                                                                                                                                                                                                                                          |
| 07-24 11:17:42                                                  | The production deployment queued for the 24 June select1 fix ends in **failure**, with no runner and no executed steps. GitHub's annotation states: **"The deployment was rejected or didn't satisfy other protection rules."** It did not apply the fix to production.                                                                                  | [Production job](https://github.com/exasol/saas-terraform/actions/runs/28094670177/job/83181034075)                                                                                                                                                        |
| 08-05 11:51:19                                                  | `marius.dyrseth@venienergy.com` starts VENI01 — at M                                                                                                                                                                                                                                                                                                     | `SAAS.CLUSTERS` + `SAAS.USERS` (auth0 id 1379)                                                                                                                                                                                                             |
| 08-05 11:54:18 → 09-04 11:25:06                                 | **719.51 h continuous at M**, zero transitions                                                                                                                                                                                                                                                                                                           | `SAAS.CLUSTERS`                                                                                                                                                                                                                                            |
| 09-04 11:25–11:47                                               | Customer stops, restarts, scales to XS (`r6id` in the supplied billing rows), stops                                                                                                                                                                                                                                                                      | `SAAS.CLUSTERS`; `SAAS.CLUSTER_USAGE_INTERVALS`                                                                                                                                                                                                            |
| 09-07 09:58 CEST                                                | [L3-4443](https://exasol.atlassian.net/browse/L3-4443) raised                                                                                                                                                                                                                                                                                            | —                                                                                                                                                                                                                                                          |
| 09-10 (evidence supplied)                                       | Mihai supplies a **Cost and usage breakdown** screenshot grouped by `saas:DBUUID`. VENI01 shows **$3,219.74** total: July **$635.80**, August **$2,209.58**, September **$374.36**. The screenshot marks September with an asterisk; the cost basis and cutoff are not visible.                                                                          | [Cost breakdown screenshot](<L3-4443 - VENI01 cost breakdown - 20260910.png>)                                                                                                                                                                              |
| 09-10 (evidence supplied)                                       | Mihai supplies a second **Cost and usage breakdown** screenshot, identifying VENI02 `VK8805V4RbSicxSIYihpFg`: **$684.80** total, comprising June **$7.36**, July **$338.48**, and August **$338.96**. July/August costs are present in this view despite zero billed maintenance compute in `SAAS.CLUSTER_USAGE_INTERVALS`; the cost basis is not shown. | [VENI02 cost breakdown screenshot](<L3-4443 - VENI02 cost breakdown - 20260910.png>)                                                                                                                                                                       |
| 09-10 (review observation)                                      | Mihai identifies a process issue: many decisions are made during voice calls without being captured in a written record. This leaves gaps in reconstructing the recovery decisions, customer instructions, and ownership of follow-up actions.                                                                                                           | Mihai's investigation review; [[#Process issue - undocumented call decisions]]                                                                                                                                                                             |

---

**Teams sources:** five screenshots supplied by Mihai on 2026-09-10, preserved beside this note and linked directly from the integrated timeline rows. The first identifies the Teams meeting chat as **Escalation | saas | Veni | 96293**. The year is visible in the embedded Jira comment and terminal log. The screenshots provide extracts of the meeting chat, not the full call record.
**Recorded maintenance-start output** (screenshot 2; terminal time zone not shown):

```text
[2026-07-01 09:55:22] (UID 0) Try to start system in maintenance mode.
[2026-07-01 09:55:22] System started successfully in partition 4886.
```

**Conclusion:** the escalation discussion is evidenced in Teams, including the VENI01→VENI03 plan, direct support operation of VENI01, a reported successful resize, and Marcel's migration-completion report. The maintenance start and later intention to start the **new** database in normal mode are different events; neither establishes that VENI01 was left in maintenance mode during its August run.

**Still missing from these extracts:** execution/verification of the requested port change, the result of the new database's normal-mode start, the decision-maker behind the migration plan, and the contents of the customer calls or follow-up messages. Fardin and Swen are additional customer-communication leads alongside Gerardo and Brian. The screenshots contain no instruction telling the customer VENI01 was surplus and no evidence about the 7 September support-start discrepancy.

---

## Current state of the account

`SAAS.DATABASES` + `SAAS.CLUSTERS`, self-joined on `MAX(LAST_MODIFIED_AT)` (both are append-only history tables; neither has `DELETED_AT`).

The table records the 09-08 investigation. Supplied billing rows extend VENI01's `stopped` interval and VENI02's `maintenance` interval through 09-10 07:06:13 UTC; they do not refresh `Migration`, Database01, or Database02.

| name       | db_uuid                  | platform_ref   | cluster                  | cluster state                                       |
| ---------- | ------------------------ | -------------- | ------------------------ | --------------------------------------------------- |
| Database01 | `B9oDsxzTTAGnVRQ01TGW_w` | `grshshwurusr` | `1mmKy_LiR6ufOMZBn9upvg` | stopped 06-30 12:17                                 |
| Database02 | `1z-1o9HMRvyztrVIEbWkTg` | `sxxwqzotfasd` | `BpoAehP4TSKaX-8i8Kx-2g` | stopped 06-30 12:18                                 |
| VENI01     | `24TAKI_mQOahKMm2FiGlpw` | `exydhmequbki` | `ENyLHgzASpysYHOUXXp5dw` | stopped 09-04 11:47:34                              |
| VENI02     | `VK8805V4RbSicxSIYihpFg` | `eqszsrcyktrm` | `jDTepO5qQnG3mhUsaUemlw` | **`maintenance` since 06-30 13:51:29, set by root** |
| Migration  | `jLoRP5ZSSF-NQuh898tzvw` | `kpcgenarvghd` | `qYelI2ZcQ9-fqQ47ir1oJA` | **`running` since 07-01 14:07:06 — 69 days**        |

There is **no DB named VENI03**; the third DB is `Migration`.

Hostname→cluster mapping verified by decode (base64url-decode the 22-char cluster UUID, base32-encode lowercase):

| cluster | host |
|---|---|
| `ENyLHgzASpysYHOUXXp5dw` (VENI01) | `cdoiwhqmybfjzldaookf26tzo4` |
| `jDTepO5qQnG3mhUsaUemlw` (VENI02) | `rq2n5jhonjbhdn42cuwgsr5gs4` |
| `qYelI2ZcQ9-fqQ47ir1oJA` (Migration) | `vgd2ki3glrb57h5jby5yvplieq` |

Sizes from `SAAS.CLUSTER_SIZES`: 1/17 XSmall, 2/18 Small, 3/19 Medium, 4/20 Large, 5 XLarge, 6 2XLarge, 7 3XLarge (two id families).

---

## Answers to the customer's three questions

### 1. What started the cluster and what kept it active

`marius.dyrseth@venienergy.com` (auth0 `…66337333eced2db6df0ad8fc`, `SAAS.USERS` id 1379) started it 08-05 11:51:19.

The sampled auto-stop logs show connection failures before the idle query could run. They do not establish whether VENI01 was idle. The recorded `Migration` last-day session-view results contain no August login rows; they are not a direct check of VENI01's audit retention. **Billed usage** survives and provides a traffic comparison, not a session or workload history:

Internet egress, GB, deduped from `SAAS.USAGE_ATTRIBUTION`:

| database | Jul | Aug | Sep (to 08) |
|---|---|---|---|
| `Migration` `jLoRP5ZSSF-NQuh898tzvw` | **4,112.67** | **3,758.80** | 958.41 |
| VENI01 `24TAKI_mQOahKMm2FiGlpw` | 0.45 | **14.13** | 9.72 |

VENI01's **14.13 GB** of August egress is about 0.5 GB/day and 0.4 % of `Migration`'s **3,758.80 GB** in that month. This supports much lower traffic on VENI01, but does not identify users, query activity, or whether the auto-stop idle condition was met. It cannot prove that no workload ran. September's **9.72 GB** remains recorded. The earlier account that Edis started VENI01 on 09-07 for a `sys` password check conflicts with the supplied billing view's continuous `stopped` interval from 09-04 through 09-10. Attribution of September traffic to that check is unresolved.

### 2. Why auto-stop did not trigger — answered

The auto-shutdown Lambda could not open a session in the sampled runs. `/aws/lambda/prod-auto-shutdown-StopDatabases` (prod mgmt acct, eu-central-1), scheduled every 15 minutes, logged:

```text
Connection to database failed: Account uuid: acc_JLkQkqwHTuaFW9sqf-r-xQ,
  24TAKI_mQOahKMm2FiGlpw=>ENyLHgzASpysYHOUXXp5dw, Error:      <- VENI01
  jLoRP5ZSSF-NQuh898tzvw=>qYelI2ZcQ9-fqQ47ir1oJA, Error:      <- Migration
```

Identical failures are recorded at 08-05 12:00, 08-20 12:00, and 09-03 12:00. These samples support a recurring failure across the window, but do not by themselves prove every run failed. On the database side, `SYS.EXA_DBA_USERS` on `Migration` reports `EXA_MONITORING_USER` `PASSWORD_STATE` = `VALID` with **86,593** failed login attempts.

Mechanism in `saas-terraform/modules/auto-shutdown-idle-databases/src/auto_shutdown.py`: `check_database()` opens as `exa_monitoring_user` (password from SSM `/<platform_reference>/exa_monitoring_user`) *before* it can run the idle query; the connect raises, the broad `except Exception` swallows it, returns `None`, no stop is issued, nothing alerts. That blind spot is what [SPOT-32540](https://exasol.atlassian.net/browse/SPOT-32540) is meant to close.

**Leading cause: credentials inherited during recovery no longer match the new deployment's configuration.** VENI01 was the restore target for the deleted EXA_DB, and `Migration` was built from VENI01 by examigration. The inherited service-user creation dates and authentication failures support this explanation. The SSM parameters exist for both deployments (as plain `String`, not `SecureString`), but no direct authentication test with the monitoring credential is recorded. Edis also reported a failing `sys` password on VENI01 ([L3-4443 c484844](https://exasol.atlassian.net/browse/L3-4443?focusedCommentId=484844)); `sys` still works on `Migration`. The precise credential mismatch and recovery step that caused it remain to be verified.

Auto-stop worked on VENI01 at 06-30 10:45:52, before the restore. This supports a recovery-related regression, but the first failed run after recovery is not recorded here.

### 3. Why the environments were not removed — partly answered

Four recovery databases remain alongside the delivered `Migration` database. VENI02 is in `maintenance`, which is not a customer-operable state. VENI01 was released into `stopped`, making it customer-startable. No comment in the three reviewed L3 tickets records a decision to remove the recovery databases.

The supplied billing rows show **no compute charge for VENI02's maintenance intervals** from 06-30 13:51:29.305 through 09-10. Its total compute amount is **$3.79**, all from its initial creating/running/stopping intervals. This does not establish zero storage or traffic charges.

The separate cost-view screenshot records **$338.48 in July and $338.96 in August** against VENI02, during that maintenance period. Zero maintenance compute billing therefore must not be described as zero cost in all sources. See [[#VENI02 cost and usage breakdown screenshot — March–August 2026]].

---

## Compute billing evidence supplied 2026-09-10

**Source:** `SAAS.CLUSTER_USAGE_INTERVALS` joined to `SAAS.PRICES`, supplied by Mihai on 2026-09-10. The query and all **50 rows (41 VENI01, 9 VENI02)** are retained under [[#Billing query and complete interval rows]]. Open intervals end at the query's `CURRENT_TIMESTAMP`, shown as **2026-09-10 07:06:13 UTC**.

### The disputed continuous run

| VENI01 row | Service window (UTC, 2026) | Wall hours | vCPU rate | Billing vCPU-hours | USD per vCPU-hour | Compute USD |
|---|---|---|---|---|---|---|
| 27 | 08-05 11:54:18.861 → 08-31 10:33:23.000 | 622.6511 | 32 | 19,924.8368 | 0.45 | 8,966.18 |
| 28 | 08-31 10:33:23.000 → 09-04 11:25:06.564 | 96.8621 | 32 | 3,099.5872 | 0.45 | 1,394.81 |
| **Total** | **One continuous M / r5d running interval** | **719.5132** | **32** | **23,024.4240** | **0.45** | **10,360.99** |

Rows 27 and 28 split at a **Chargebee subscription service-window boundary**, not a cluster state change. The supplied explanation identifies a subscription event at **08-31 10:33:23**. The earlier boundary at **07-31 10:33:24** likewise splits VENI01's stopped rows 23/24 and VENI02's maintenance rows 7/8. A repeated status in this view therefore need not represent a new cluster operation.

**Price is per vCPU-hour, not per wall-clock hour.** `vcpu_rate` is `num_nodes × vcpu`: Medium has 32, XS has 8. Medium / r5d therefore costs **32 × $0.45 = $14.40 per billable wall-clock hour**. The disputed amount is **23,024.4240 × $0.45 = $10,360.9908**, rounded to **$10,360.99**.

### Totals and billing behavior

| Scope | Compute USD | Interpretation |
|---|---|---|
| VENI01, all 41 supplied rows | **10,484.88** | Total rounded once after summing interval charges |
| VENI01, disputed running rows 27/28 | **10,360.99** | Continuous 08-05 → 09-04 run, excluding startup/shutdown and later operations |
| VENI01, June–July recovery rows 1–22 | **121.36** | Agrees with the earlier recovery-period compute amount |
| VENI01, other August–September billable intervals | **2.53** | Startup, shutdown, and the later 09-04 restart/resize; total rounded once |
| VENI02, all 9 supplied rows | **3.79** | Initial creating/running/stopping only; maintenance compute is zero |

The supplied per-row USD values sum to **$10,484.90** for VENI01, while rounding the aggregate once gives **$10,484.88**. The **$0.02** difference is rounding, not another charge. The four-decimal vCPU-hour display also explains small differences from earlier rounded recovery totals: VENI01 rows 1–22 sum to 269.6782 here versus 269.6783 previously; VENI02 sums to 8.4174 versus 8.4175. The USD totals remain $121.36 and $3.79.

The view assigns zero `billing_vcpu_hours` to `stopped`, `maintenance`, `error`, and the `tocreate` / `tostop` / `tostart` / `toscale` statuses. A row can carry a price and still have zero charge. `creating`, `starting`, `stopping`, and `scaling` are billable and 15-minute-capped; the 0.2500 h creating rows show the cap, not the actual transition duration.

VENI01 changes from **M / r5d, $0.45 per vCPU-hour** to **XS / r6id, $0.495 per vCPU-hour** at the 09-04 resize. Both size and family matter to the price. Rows VENI01/41 and VENI02/9 remain open; their wall hours grow as `CURRENT_TIMESTAMP` advances, but their stopped/maintenance compute charge stays zero.

**Credit conclusion:** the continuous-run compute amount is now established from the supplied billing source. Invoice screenshots 901/936 below establish paid totals for the June–July and July–August periods, but not per-database attribution or existing credit notes. Approval, invoice/credit reconciliation, and the amount considered avoidable under the intended idle policy remain open. Storage, traffic, and `Migration` costs are outside this query.

**September activity discrepancy:** VENI01 row 41 is continuously `stopped` from 09-04 11:47:34.529 through the supplied 09-10 cutoff. It contains no 09-07 start. This conflicts with the earlier support-start account; it does not invalidate the recorded password-check report or prove that no host-level support activity occurred.

### Paid invoice screenshots — June–August 2026

**Source:** two invoice-detail screenshots and their Chargebee links supplied by Mihai on 2026-09-10 as VENI investigation evidence: **[invoice 901](https://exasol.chargebee.com/d/invoices/901)** and **[invoice 936](https://exasol.chargebee.com/d/invoices/936)**. Neither screenshot displays the customer name, account UUID, or a per-database breakdown; the VENI association comes from the supplied context, not a visible account identifier. The linked pages have not been independently retrieved; values below are transcribed from the screenshots.

| Invoice field | 901 | 936 |
|---|---|---|
| Billing period, as displayed | Jun 30 – Jul 31, 2026 | Jul 31 – Aug 31, 2026 |
| Invoiced on (Europe/Berlin) | 06-Aug-2026 14:17 | 02-Sep-2026 12:33 |
| Payment status | Paid on 06-Aug-2026 14:18 | Paid; screenshot says "8 days ago" |
| Storage (GB-Month) | $307.67 | $97.15 |
| Internet traffic (GB) | $366.39 | $340.12 |
| Compute eu-west-1 r5d (vCPU hours) | $5,372.93 | $14,323.61 |
| **Invoice total (USD)** | **$6,046.99** | **$14,760.88** |
| Amount paid, as displayed | ($6,046.99) | ($14,760.88) |
| Amount due | $0.00 | $0.00 |

Each invoice's three line amounts sum exactly to its total. Both show Enterprise prices beginning **$0.02500… per GB-month**, **$0.09000… per GB**, and **$0.45000… per vCPU-hour**. Quantities and unit-price fields are truncated in the screenshots; do not reconstruct exact billed quantities from those fields. The displayed compute price is consistent with the **$0.45/vCPU-hour** used in the supplied interval query.

**Relation to VENI01:** invoice 936's displayed period corresponds by date to the first disputed billing leg, **$8,966.18** for 08-05 → 08-31. That is part of the investigation's **$10,360.99** disputed-run amount, not a replacement for invoice 936's **$14,323.61** compute total. The screenshot does not identify which databases contributed to that total. Exact service-window timestamps and usage-to-invoice linkage still need confirmation before treating the leg as reconciled to invoice 936.

The second disputed leg, **$1,394.81** for 08-31 → 09-04, falls outside invoice 936's displayed service period. Its 2 September issue date does not extend that period. No invoice covering that later service window has been supplied here. Invoice 901 covers the earlier recovery period, not VENI01's August start; it likewise does not isolate recovery charges or establish which credits have already been applied.

**Payment is not credit approval:** the screenshots establish paid status and zero outstanding balance at capture. They do not show credit-note/refund history, a VENI01-specific charge, or an approved refund.

![Invoice 901 for the June 30 to July 31 billing period](<L3-4443 - Invoice 901 - 20260806.png>)

![Invoice 936 for the July 31 to August 31 billing period](<L3-4443 - Invoice 936 - 20260902.png>)

### Cost and usage breakdown screenshot — July–September 2026

**Source:** screenshot supplied by Mihai on 2026-09-10, titled **"Cost and usage breakdown (2)"**, grouped by **`saas:DBUUID`**. The row identifies **VENI01 `24TAKI_mQOahKMm2FiGlpw`**. Values below retain the screenshot's dollar notation.

| Displayed period | VENI01 cost |
|---|---|
| July 2026 | **$635.80** |
| August 2026 | **$2,209.58** |
| September 2026* | **$374.36** |
| **Total** | **$3,219.74** |

The displayed **Total costs** row and the VENI01 row contain the same amounts; they are not two charges to add together. The three monthly amounts sum to **$3,219.74**. The September asterisk is present in the source, but its meaning and the period's cutoff are not shown.

**Comparison limit:** this is a separate cost-view observation, not a replacement for the **$10,360.99** continuous-run compute amount derived from `SAAS.CLUSTER_USAGE_INTERVALS` and `SAAS.PRICES`. The screenshot alone does not identify the cost basis, included services, or filters. Those distinctions and the period boundaries must be established before treating the two totals as comparable or calculating a difference for credit.

![VENI01 cost and usage breakdown for July, August, and September 2026](<L3-4443 - VENI01 cost breakdown - 20260910.png>)

### VENI02 cost and usage breakdown screenshot — March–August 2026

**Source:** second **"Cost and usage breakdown (2)"** screenshot supplied by Mihai on 2026-09-10. The row identifies **VENI02 `VK8805V4RbSicxSIYihpFg`**. The displayed columns cover March through August 2026; September is not shown.

| Displayed period | Total costs row | VENI02 row |
|---|---|---|
| March 2026 | $0.00 | - |
| April 2026 | $0.00 | - |
| May 2026 | $0.00 | - |
| June 2026 | **$7.36** | **$7.36** |
| July 2026 | **$338.48** | **$338.48** |
| August 2026 | **$338.96** | **$338.96** |
| **Total** | **$684.80** | **$684.80** |

The dashes in the VENI02 row are preserved as displayed, rather than replaced with zero. The monthly amounts **$7.36 + $338.48 + $338.96 = $684.80** reconcile to the displayed total. The total row and database row represent the same amounts, not additive charges.

**Maintenance-period cost:** July and August together account for **$677.44** in this view. `SAAS.CLUSTER_USAGE_INTERVALS` records VENI02 in maintenance throughout both months with **zero billed compute**. Both observations remain valid: the screenshot records costs against the database, while the billing view records no compute charge for maintenance. The screenshot does not identify which services incurred those costs or whether they are customer charges, so **$684.80 is not a replacement for the $3.79 compute total or an established credit amount**.

![VENI02 cost and usage breakdown for March through August 2026](<L3-4443 - VENI02 cost breakdown - 20260910.png>)

---

## The intent question

**VENI01 was an intermediate recovery database, but it remained customer-operable after the handover.** See [[#Evidence of the intended handover]] for the supporting records.

`Migration` is documented as the final/handover DB ([slack, 07-01 13:12–13:20 CEST](https://teamexasol.slack.com/archives/C0BE3UKT56J/p1782904848957079)). The available records do not identify VENI01 as internal-only. From the customer's perspective:

- a customer user created it;
- its connection string was posted openly on 06-30;
- it held their restored data and was the examigration **source**;
- it stayed visible and startable in their UI.

The monitoring-login failure does not establish that VENI01 was internal-only: the same failure is present on `Migration`, the DB that was handed over.

Edis's own caution, [L3-4443 c484791](https://exasol.atlassian.net/browse/L3-4443?focusedCommentId=484791): *"'Created at Exasol's request' aligns with support asking VENI to create it, but every create/start/stop/scale action on this cluster was issued by a VENI account user."*

The quoted "every" is broader than the transition evidence: the timeline also records `root` maintenance, scale, and stop actions during recovery. A VENI-attributed action identifies the executing account, not who requested the action.

**Conclusion:** VENI01 was an intermediate recovery database, left customer-operable at 4× its original size, with no instruction in the reviewed records identifying it as surplus.

The RCA's timeline names VENI01 as where the restore was attempted and the ExaMigration target as what was delivered. This documents the intended handover, but does not characterise VENI01 as temporary or surplus. See [[#What the RCA is evidence of]] for the communication evidence.

---

## Customer actions and responsibility

The **719.51 h** run followed a customer-attributed start while auto-stop was unable to perform the idle check in the sampled runs. Responsibility depends on both the platform failure and the circumstances of that start.

**The delivered database was already running.** `Migration` was handed over 2026-07-01 and remained running through 2026-09-08. The 2026-08-05 start brought up a second database containing the recovery source data. The two databases' contents were not compared at the time of that start.

**The start is attributed to a VENI user.** `tostart` at 2026-08-05 11:51:19 is attributed to `marius.dyrseth@venienergy.com` (`SAAS.USERS` id 1379, active). This does not distinguish a UI action from API automation, an accidental start, or an action requested by Exasol.

**Traffic was low relative to `Migration`.** VENI01 had 14.13 GB of August internet egress (~0.5 GB/day), compared with `Migration`'s 3,758.80 GB. User activity and idle periods cannot be reconstructed from these monthly totals.

**Why VENI01 was at Medium — inferred from timing.** No reviewed message gives a reason, but the resize pairs with the migration:

| 07-01 UTC | actor | what |
|---|---|---|
| 10:18:56 | root | creates the target `Migration` at **Large** |
| 10:23:13 | root | scales the source VENI01 **XS → M** |
| ~11:20 | — | EXAmigration running (Marcel, 13:21 CEST: *"let EXAmigration run a little bit"*) |
| 13:54:27 | root | scales `Migration` **Large → Small** — target sized back down |
| 18:14:02 | root | VENI01 **stopped**, still at M — source never sized back |

The target was created at Large and the source was scaled up about four minutes later, immediately before migration; afterwards only the target was sized back down. This supports migration capacity as the reason for Medium, but no written rationale is recorded. Bogdan's only message in the reviewed window is *"Didn't we just removed VENI's databases a few days back as the customer was offboarded?"* (07-01 15:38 CEST) — nothing about sizing or backup duration. The recorded backup problem was a protocol error, not a slow transfer: `Protocol "s3" not supported or disabled in libcurl` on 06-30 16:34 CEST.

**The UI displays the cluster size.** VENI01 remained at Medium after recovery, and a customer user scaled it to XS on 09-04. The August start's UI/API path and the initiating user's awareness of the size are not recorded.

**Customer management actions continued in September.** On 09-04 `marius.gundersen@venienergy.com` stopped VENI01, restarted it, scaled it to XS, and stopped it again inside 22 minutes. These actions establish access to the controls, not what the customer understood about the database's intended role.

**The complaint distinguishes usage from creation.** *"None of our team has used this cluster"* could refer to query workload rather than the start operation. *"VENI01 was one of the environments created at Exasol's request"* is compatible with a customer user executing the creation. The transition actors alone cannot confirm or refute that request.

**The no-usage claim remains unresolved.** Non-zero billed egress establishes traffic, but not customer queries or who generated it. Edis's proposed current-session check cannot reconstruct expired history. Separate audit retention, archived logs, or customer-side records would be needed to establish August workload.

**Responsibility assessment.** Exasol left VENI01 startable at Medium, four times its original size, with no surplus-use instruction in the reviewed records and a failing auto-stop check. A VENI-attributed start then preceded roughly 30 days without a stop. Both facts matter to a credit decision. The purpose of the start, any Exasol instruction, and whether a working 30-minute idle check would have stopped it are still unknown.

### Did anyone at Exasol tell them to start VENI01?

**No instruction to start VENI01 was found in the sources below.** Direct correspondence from the account team and the Salesforce case were not accessible to this investigation:

| source | result |
|---|---|
| Slack search across accessible channels and DMs | The exact `VENI01` search returned a gap between 2026-07-01 12:24 and 2026-09-07, with no August matches. |
| Mihai's mailbox (Inbox / Archive / Sent / Deleted) | No VENI messages found between `CoE Veni` on 07-08 and the 09-08 investigation. Last operational threads are Fardin Sabzi's `Escalation \| saas \| Veni \| 96293` on 06-30 and 07-01. |
| [L3-4267](https://exasol.atlassian.net/browse/L3-4267) | no comment after 07-02. |
| Jira, any project | The search reported no intervening VENI ticket between 06-30 and 09-07. Exact query and date-boundary semantics were not retained. |
| [SAAS-1833](https://exasol.atlassian.net/browse/SAAS-1833) | the credit thread ran 07-29 → 08-06 (Gerardo, Edis, Brian Cunningham, Mihai). Brian relays customer questions about the restore costs. **No one asks the customer to start anything.** |

**The start overlapped the credit discussion.** The cost conversation ran 07-29 → 08-06; the start occurred 08-05 11:51. Brian Cunningham's and Gerardo Abihaggle's direct customer email and the Salesforce case are needed to determine whether anyone requested it. Those sources were not accessible to this investigation.

**Questions for the customer and account team:**

- What was the 2026-08-05 start for? A test, a data check during the credit discussion, a mistaken click, an automation?
- Did anyone at Exasol — support, SDM or AE — ask them to start or verify VENI01 in that window?
- Who requested the 06-30 creation, and is there a message or call record supporting *"created at Exasol's request"*?
- Did the customer understand `Migration` to be the delivered environment and the rest to be surplus? The RCA does not state that the others were surplus; other correspondence has not been reviewed.

---

## Corrections needed before anything goes to the customer

- **"Logs show there was activity"** ([L3-4443 c484791](https://exasol.atlassian.net/browse/L3-4443?focusedCommentId=484791)) does not hold. The Lambda logs show a failed connection — it never got far enough to observe a session.
- **`Migration` ran continuously from 2026-07-01 14:07 through the 2026-09-08 check** — approximately 69 days — with recurring auto-stop connection failures. The customer wrote that it "runs in parallel and is separately accounted for"; this does not establish whether they knew auto-stop was failing or intended 24/7 operation. Refresh the state and billed amount before quoting a cost.
- **The customer-facing RCA has a wrong date.** Its timeline row `2026-07-30 21:29 | Restore issue identified` should read `06-30`. The correction should be reconciled with any new customer reply.

---

## Process issue - undocumented call decisions

**Reported by Mihai on 2026-09-10:** many decisions are made during voice calls without being captured or documented.

The VENI investigation illustrates the gap. [L3-4267 c466075](https://exasol.atlassian.net/browse/L3-4267?focusedCommentId=466075) records the migration plan from a call but does not identify the decision-maker. The supplied Teams extracts refer to customer calls without recording their outcomes. Cleanup ownership, sizing rationale, and the instructions given to the customer remain unresolved; see [[#Missing information]].

Some plans and actions were written down, so the evidence does not establish that every call decision was undocumented or that no other records exist. The process issue is the lack of a reliable written decision record, not merely the absence of another query export or a more precise source link.

**Proposed follow-up, not yet agreed:** record call decisions in the incident ticket or linked meeting note, including the decision, rationale, decision-maker, action owner, and any agreed deadline. Distinguish proposed actions from completed and verified actions, and record what was communicated to the customer.

---

## Missing information

These gaps remain after incorporating the billing data supplied on 09-10. No additional live production queries were run for this update.

| Missing information                                    | Why it matters / evidence needed                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Reason and request path for the 08-05 start            | Ask the initiating user and review UI/API records, automation, and account-team correspondence. A customer-attributed actor does not establish motive or exclude an Exasol request.                                                                                                                                                                                                      |
| Customer instructions and RCA delivery | Review Brian/Gerardo's outbound correspondence and Salesforce case 00096293. The Teams timeline adds Fardin's customer meeting and Swen's planned 15:30 call as leads. The RCA supports intended handover, but no reviewed record tells the customer not to use VENI01; call contents, direct delivery evidence, and other communications remain absent. |
| Cleanup and sizing decisions                           | Identify who owned retiring VENI01, VENI02, Database01, and Database02, why VENI01 stayed startable at Medium, and whether `Migration` should run 24/7. No cleanup decision or explicit Medium-sizing rationale is recorded.                                                                                                                                                             |
| Recovery decision-maker | The supplied Teams screenshots identify **Escalation \| saas \| Veni \| 96293** and show the VENI01→VENI03 plan being shared during the meeting. Mihai's comment records the plan, not who decided it. The decision-maker and any additional call decisions remain unrecorded in the supplied extracts. |
| Maintenance-mode and normal-mode follow-through | Teams records a successful maintenance-mode start and Marcel's request to stop, change the port, and restart. Execution and verification of the port change are not shown. At 15:12 he reports migration complete and proposes starting the new DB in normal mode; these extracts do not show that start's result or the final configuration. |
| Monitoring-credential cause, onset, and repair         | A direct monitoring-user authentication result, first post-recovery failed run, and successful idle-check result after repair are missing. Do not include credentials in the evidence. The `sys` probe does not test the monitoring account.                                                                                                                                             |
| Actual August workload and idle periods                | Egress totals do not identify SQL, users, or idle eligibility. Check VENI01's separate audit retention, archived DB logs, and customer-side records. Restarting cannot recreate expired session history.                                                                                                                                                                                 |
| Session-query reconciliation                           | The aggregate snapshot lists **2,028** rows; daily counts **1 + 1,063 + 992 = 2,056**. Capture times and matching query filters are missing. The live-check heading says **14:09 CEST**, while a result includes `MAX(LOGIN_TIME)` **15:19** on the same date; query timing/time-zone details need reconciliation. Preserve both observations rather than treating them as one snapshot. |
| Other consumers' health                                | Inspect `select1` and snapshot-policy logs, schedules, and successful runs. The cumulative **86,593** failures have no documented start/reset time or caller breakdown. Reconcile any sensor failure with the recorded August availability of **100% / 0 downtimes**.                                                                                                                    |
| Final credit decision | The supplied billing view resolves the disputed-run compute amount to **$10,360.99**. Invoice 936 shows **$14,323.61** compute / **$14,760.88** paid total for Jul 31–Aug 31; invoice 901 shows **$5,372.93** compute / **$6,046.99** paid total for Jun 30–Jul 31. Neither isolates VENI01. Confirm account/subscription linkage, exact service-window boundaries, per-database invoice attribution, the later invoice covering the **$1,394.81** Aug 31–Sep 4 leg, existing credit notes/refunds, approval, and what portion would have been avoided under the intended idle policy. `Migration`, storage, and traffic are outside the supplied interval query. |
| Select1 fix deployment at `Migration` creation | CI records show no production Terraform deployment of the direct-creation fix between its 24 June merge and `Migration`'s creation on 1 July at 10:18:56 UTC. The historical Step Function definition and any deployment outside CI remain unverified. See [[#Existing select1 creation fix and deployment evidence]]. |
| Cost-view comparison basis | The screenshots show **VENI01 $3,219.74** for July–September and **VENI02 $684.80** for March–August, including **$677.44** during July/August maintenance. Cost basis and included services/filters are not visible; VENI01's September cutoff and asterisk meaning are also unspecified. Identify the cost components before comparing these figures with customer compute billing or using them for credit. |
| September support activity | Reconcile the earlier reported 09-07 start for Edis's password check with VENI01's continuously `stopped` billing interval from 09-04 through 09-10. Identify whether the report concerned a cluster start, host-level access, or another database before attributing September egress. |
| Current operational and ticket status | The supplied view extends VENI01's stopped and VENI02's maintenance intervals through 09-10 07:06:13 UTC. Repairs, other cluster states, cleanup ownership, and SPOT-32540 scope/assignee are not refreshed. A Draft alert ticket does not establish a deployed fix. |

---

## Open

- Repairing the `exa_monitoring_user` and `sys` logins on VENI01 — Edis's `additional_sys_passwd_hashes` attempt failed ([c484857](https://exasol.atlassian.net/browse/L3-4443?focusedCommentId=484857)), routed to the interface team ([c484856](https://exasol.atlassian.net/browse/L3-4443?focusedCommentId=484856)). `Migration` was manually repaired and its auto-stop recovery verified on 09-08 ([c485400](https://exasol.atlassian.net/browse/L3-4443?focusedCommentId=485400)).
- Credit approval and reconciliation: the **719.5132 h** continuous run totals **$10,360.99** compute across the two billing legs. The earlier rounded vCPU-hour figures (19,924.84 and 3,099.59) are resolved to **19,924.8368 + 3,099.5872** in the supplied data. See [[#Compute billing evidence supplied 2026-09-10]] and [[SAAS-1834 — VENI restore additional cost (June–July 2026)]] for the recovery-period context.
- Cleanup decision for VENI01, VENI02, Database01, Database02 — and whether `Migration` should keep running 24/7 at all. Raised on 2026-08-06 in [[SAAS-1834 — VENI restore additional cost (June–July 2026)]] as open question #1 and still unanswered.
- Whether the availability sensor (`select1`) and the volume-snapshot policy are also failing on these databases — they share `monitoring_db_user`. Inferred from the failure rate, **not verified**.
- **Confirm customer instructions with Gerardo Abihaggle (SDM) and Brian Cunningham.** The RCA claims "regular status updates" but does not identify VENI01 as temporary. Their correspondence, the Salesforce case, and any relevant call records are needed; other senders or verbal instructions cannot be excluded.
- Scope of [SPOT-32540](https://exasol.atlassian.net/browse/SPOT-32540): alert on auto-stop specifically, or on any service account that cannot authenticate to a customer DB.
- [SPOT-32614](https://exasol.atlassian.net/browse/SPOT-32614): implement automatic technical-user synchronization and verify recovery with the actual consumer credentials. Covers platform-managed technical users, not automatic `sys` credential repair or unrelated post-migration configuration.
- The earlier Slack search for `escalation-veni-96293` returned only `#escalation-veni-00078563` (2024) and archived private `#veni-exa_db_restore`. The supplied screenshots now identify a **Teams** meeting chat, **Escalation | saas | Veni | 96293**; see the 1 July entries in [[#Timeline]]. Any further call decisions, customer instructions, and execution results remain outside the supplied extracts.

---

## Method notes

- `SAAS.DATABASES` and `SAAS.CLUSTERS` are append-only history tables — one row per state transition. Any current-state query must self-join on `MAX(LAST_MODIFIED_AT) GROUP BY UUID`; a plain `SELECT` returns every transition and overruns the MCP result limit. Neither table has a `DELETED_AT` column.
- `DATABASES.STATUS = 'running'` means the DB record is not deleted. It does **not** mean a cluster is up — cluster state lives in `SAAS.CLUSTERS`.
- Queried via saas-debug MCP against prod mgmt node `i-0af4f9152b7b8ad1c`; CloudWatch via profile `prod-admin`, eu-central-1. DB **cluster** nodes are in `prodc` — use profile `prodc-admin` and target **n11**, not n10: n10 refuses 8563 and carries no `saas:ClusterUUID` tag.
- A cluster's connection hostname is its UUID re-encoded: base64url-decode the 22-char cluster UUID to 16 bytes, then base32-encode lowercase. That is how a hostname in a ticket is tied back to a cluster.
- `cos_exaplus_query` connects as `sys` with the `dwad_client` password and takes no user argument, so it cannot test another account's credentials. The failed-login counter in `SYS.EXA_DBA_USERS` provides authentication-failure evidence, but does not identify the supplied password, caller, or failure time.
- RCA text was extracted with `pypdf` using `extraction_mode="layout"` to preserve the timeline's column and row structure.

---

## Cross-references found in the vault (added 2026-09-08)

### The offboarding itself was an error

[[Mid-Year Review 2026 — Evidence]], "VENI offboarding":

> **Per Mihai (2026-08-02): the offboarding request was a mistake rooted in a misunderstanding of the billing model; a correction of error was later done by Katharina.** The mistake/correction is not recorded on the ticket itself — Mihai's account; ask him for the Katharina correction reference if challenged.

The reviewed comments on [L3-4264](https://exasol.atlassian.net/browse/L3-4264) and [L3-4267](https://exasol.atlassian.net/browse/L3-4267) do not record the billing-model misunderstanding. This explanation is attributed to Mihai; the related CoE ticket is documented below.

### The `Migration` exposure was already found on 2026-08-06 — a month before the customer complained

[[SAAS-1834 — VENI restore additional cost (June–July 2026)]], observation 3, verbatim:

> **⚠️ The `Migration` database has been running continuously since 01 July and is still up.**
> - Cluster `qYelI2ZcQ9-fqQ47ir1oJA` (Cluster01), `status=running`, last modified 2026-07-01 14:07:06 by stepfunction. Final transition is `running → (none)`, **h=868.48** and counting.
> - Size **S** (r5d.xlarge, 4 nodes × 4 vCPU = 16 vCPU), i.e. **384 vCPU-h/day = $172.80/day**.
> - **Every interval is `by=root`** — created and scaled by us, not by the customer.
> - 868.48 h × 16 vCPU × $0.45 ≈ **$6,250 to date**. It is on VENI's account and July onward is CT-billed, so **the customer is being charged for it.**

Open question #1 in that note was "Is the `Migration` DB still needed? … Decision needed from Edis/Gerardo." It was raised 2026-08-06; no decision is recorded here, and the cluster was still `running` on 2026-09-08. The investigation's rough compute estimate was **$12,000**, using $172.80/day and ~69.9 days since 07-01 14:07, before storage (205–233 GB-Mo/day) and traffic (76–171 GB/day). The elapsed-time estimate needs an exact cutoff and reconciliation with the approximately 69-day live-check interval before being used for billing or credit.

The billing-query behavior recorded in that note explains why open intervals must be included:

> An open-ended `running` interval (`to_ts` = now) is deliberately **not** capped by the billing query, so a cluster left running bills indefinitely. That is how the Migration DB was found — and how it would be missed if you only looked at closed intervals.

### VENI01's June–July cost was almost entirely root-initiated

Same note, per-DB breakdown for 2026-06-19 → 07-06 (subscription `AzypycTwFCmon11f6`):

| Database | vCPU-h | USD |
|---|---|---|
| EXA_DB `S11uTYyGRDeIuR4wivF-3Q` (deleted 06-29) | 2,176.3749 | 1,077.31 |
| **Migration** `jLoRP5ZSSF-NQuh898tzvw` | 1,901.8402 | **855.83** |
| VENI01 `24TAKI_mQOahKMm2FiGlpw` | 269.6783 | 121.36 |
| Database01 | 18.6337 | 9.22 |
| Database02 | 18.6458 | 9.23 |
| VENI02 | 8.4175 | 3.79 |
| EXA_DB_BACKUP | 0.1144 | 0.06 |

Initiators over that window: `Migration` root $855.83; **VENI01 root $111.88 of its $121.36**. Most recovery-period VENI01 compute was therefore attributed to `root`, unlike the August run's customer-attributed start. A credit assessment should distinguish these periods.

Also relevant to a credit note: VENI is explicitly named in the decomposition note's rule #9 as a case where `deleted_leak` over-attributes for auto-stopping DBs. Do not quote invoice 887's `deleted_leak` of $1,317.62.

### This exact complaint from this exact customer, six months earlier — and it resolved the other way

[[VENI Energy]] lists start/stop reliability as their standing pain, including [L3-3973](https://exasol.atlassian.net/browse/L3-3973) "Clusters not shut down automatically & REST API for shutting down DB did not work" (16.03.2026) and [L3-3954](https://exasol.atlassian.net/browse/L3-3954) "Large cluster being turned on probably after midnight" (09.03.2026, billing impact), plus [L3-3306](https://exasol.atlassian.net/browse/L3-3306) "Database in maintenance mode for weeks" — the precedent for the item-3 complaint.

On L3-3973 the finding was the **opposite** of L3-4443 ([c441929](https://exasol.atlassian.net/browse/L3-3973?focusedCommentId=441929), Mihai, 16.03.2026): auto-stop *was* firing (`tostop` by `root` at 23:30 nightly) and `petter.skjolden@venienergy.com` was restarting the cluster at 23:10 every single night, with `dataops+consumption@venienergy.com` starting it again at 08:00 on weekdays. Juergen's follow-up ([c442029](https://exasol.atlassian.net/browse/L3-3973?focusedCommentId=442029)): *"Could we find out if they have a script that triggers the restart? An e-mail address like `dataops+consumption@venienergy.com` sounds a bit as if drives some automation."*

**The recorded mechanisms differ:**

- L3-3973: dozens of customer `tostart` events, one per night. L3-4443: **exactly one** `tostart` in 30 days.
- L3-3973: `tostop` rows present throughout — auto-stop ran. L3-4443: no `tostop` during the 719.51 h run, and the sampled 15-minute Lambda runs show connection failures.

The March finding of repeated customer restarts does not explain VENI01's single-start, continuous-running interval.

Note also the actor naming changed between the two: in March auto-stop wrote `tostop` as `root`; on VENI01 in June it wrote `auto-stop`. Consistent with the identity census recorded in the SAAS-1834 note (`root`, `saasengine`, `stepfunction`, `scheduled-action`, `auto-stop`).

### Internal downtime record

The July SLI blip for VENI is written up on Confluence `08-07-2026` (SAAS space, page 2897805321), quoted in [[CBR SaaS availability slide - Andy's process (2026-08-18)]]: *"The VENI (acc_JLkQkqwHTuaFW9sqf-r-xQ) issue occurred when migrating backup data to a new database after deleting the original."* VENI's July availability 99.63% / 9 downtimes / 23 min; August 100% / 0.

---

## Evidence of the intended handover

**VENI01 and VENI02 were intermediate recovery databases; the third DB was the intended deliverable.** Four independent artefacts support this:

1. [c465820](https://exasol.atlassian.net/browse/L3-4267?focusedCommentId=465820) — VENI01 is "Restore, which I worked on"; the plan is to migrate VENI01 *into* VENI02.
2. [c465871](https://exasol.atlassian.net/browse/L3-4267?focusedCommentId=465871) — VENI01 is the backup **source**, VENI02 the restore **target**; VENI02 ends "not yet trustworthy / not ready to go live" and is stopped ([c465872](https://exasol.atlassian.net/browse/L3-4267?focusedCommentId=465872)). Its latest recorded platform state remains `maintenance` as of 09-08.
3. [c466075](https://exasol.atlassian.net/browse/L3-4267?focusedCommentId=466075) — a **third** DB is created precisely because neither of the first two could be delivered; VENI01 is demoted to examigration source.
4. Slack 07-01 13:12–13:20 CEST — Gerardo asks for "the **final** database", Edis answers with the third DB and notes it is "not available to the customer yet".

**Cleanup and customer instructions are not established.** The transition history shows VENI01 remained usable, and the reviewed communication contains no instruction that it was surplus:

- VENI02 got the `maintenance` lock. **VENI01 did not** — it was released to `stopped` at 07-01 18:14:02, an ordinary customer state.
- [c466271](https://exasol.atlassian.net/browse/L3-4267?focusedCommentId=466271) (Edis, 07-01 16:07 CEST) "DB is scaled down to Size: S / Status is up and running" is the **Migration** DB, not VENI01 — 16:07 CEST = 14:07 UTC, matching `qYelI2ZcQ9-fqQ47ir1oJA` `running` at 14:07:06 UTC at size id 2 (Small). The delivery DB was scaled down that afternoon, while **VENI01 was left at Medium**.
- VENI01's connection string was posted as a customer-facing endpoint on 06-30 ([c465750](https://exasol.atlassian.net/browse/L3-4267?focusedCommentId=465750)); no retraction is recorded.
- It stayed visible and startable in the UI. The 08-05 start is recorded, but whether it used the UI or API is unknown.

**Conclusion:** VENI01 was an intermediate recovery step rather than the intended handover database. After migration it was not removed, locked, or resized back. The reviewed records do not show that the customer was told it was surplus; separate correspondence remains an evidence gap.

### Carsten's position — no written decision found

No written statement of Carsten's position was found in the following sources:

- **Jira:** no comment by Carsten Tzschoppe on [L3-4267](https://exasol.atlassian.net/browse/L3-4267) (18 comments), [L3-4264](https://exasol.atlassian.net/browse/L3-4264) (11) or [L3-4443](https://exasol.atlassian.net/browse/L3-4443) (8) — full comment lists retrieved. `text ~ "VENI01"` across all of Jira returns only L3-4267 and L3-4443.
- **Slack:** the search returned zero messages from `carsten.tzschoppe@exasol.com` containing "veni". In the reviewed 2026-06-28 → 07-06 window, it returned five messages from him, three in `#release-exasol-2025-1-12` about unrelated flaky tests. This is limited to searchable content.

The trail ends in group DM [`C06HJ21RDL5`](https://teamexasol.slack.com/archives/C06HJ21RDL5) (Carsten, Edis, Mihai, Iaroslav Babanin, Sun Nam), 2026-06-30:

> **Edis 14:18:51** — "Hi guys, I need help to restore backup"
> **Edis 14:19:23** — "it's a customer DB"
> **Edis 14:23:07** — "looks like @Carsten Tzschoppe is not available, I need help to do a restore"
> **Carsten 14:27:39** — "What is the problem that you have?"
> **Edis 14:27:44** — "call ?"
> **Carsten 14:28:00** — "where to join?"

The conversation moves to a call at 14:28; no written outcome is cited. Mihai states that [c466075](https://exasol.atlassian.net/browse/L3-4267?focusedCommentId=466075) was **not his decision**, but a record of a call. The decision-maker is not named. Carsten or other participants would need to confirm the decision and rationale.

The supplied 1 July Teams screenshots show that the same Jira plan was shared during the escalation meeting at displayed time 09:46. They add the subsequent operational discussion, but contain no visible statement by Carsten and do not identify who made the migration decision.

### The Correction of Error exists as a ticket

[SPOT-31532](https://exasol.atlassian.net/browse/SPOT-31532) "CoE VENI actions - 06/26", label `CoE`, Katharina Halasz, **In Progress** since 08.07.2026, no comments. Four subtasks, **all still Draft**:

| | |
|---|---|
| [SPOT-31543](https://exasol.atlassian.net/browse/SPOT-31543) | Hand over SaaS offboarding process to CD |
| [SPOT-31544](https://exasol.atlassian.net/browse/SPOT-31544) | Remove blockers from SaaS offboarding process |
| [SPOT-31545](https://exasol.atlassian.net/browse/SPOT-31545) | Define and agree on new Process for PAYG / consumption based |
| [SPOT-31546](https://exasol.atlassian.net/browse/SPOT-31546) | Define a long term sustainable process for on- and offboarding SaaS customers with low effort |

This is the "correction of error … done by Katharina" referenced in [[Mid-Year Review 2026 — Evidence]]. The listed actions address offboarding processes, not cleanup of the recovery databases. Their Draft status does not establish completed remediation; ownership of the remaining databases is unresolved.

### L3-3973's cluster was not VENI01 — it was a worker on the deleted production DB

[c441929](https://exasol.atlassian.net/browse/L3-3973?focusedCommentId=441929) concerns cluster `zfuyjJbqRnCsR_6cVmmEVA`, named `DEV-LARGE-WORKER`. Resolved against `SAAS.CLUSTERS`:

| field | value |
|---|---|
| cluster uuid | `zfuyjJbqRnCsR_6cVmmEVA` |
| db_uuid | **`S11uTYyGRDeIuR4wivF-3Q`** — i.e. `EXA_DB`, the old production DB deleted on 2026-06-29 |
| main_cluster | **FALSE** — a worker cluster |
| names over time | `Cluster04-` → `Cluster04-LARGE-WORKER` / `LARGE-WORKER` (10.03.2025) → `DEV-LARGE-WORKER` (11.03.2025 → 15.04.2026) |

VENI01 is a different database created three months later (`24TAKI_mQOahKMm2FiGlpw`, cluster `ENyLHgzASpysYHOUXXp5dw`, MainCluster, 2026-06-30). No overlap.

So the March precedent is on the **pre-deletion estate**, on a **worker** cluster, and the nightly restart loop belonged to that workload. It bears on how the customer operates their databases in general — and on how this same complaint was answered before — but it says nothing about VENI01, and none of its actors (`petter.skjolden@`, `dataops+consumption@`) appear in VENI01's history, where the only two account users are `marius.gundersen@` (create, and the 09-04 actions) and `marius.dyrseth@` (the single 08-05 start).

---

## Tracking of post-migration steps

### Documented handoffs and follow-up in other L3s

**Historical comparison, verified 2026-09-11:** post-restore coordination with SaaS was documented multiple times, including explicit requests and completion reports. The missing VENI record should not be read as evidence that no procedure or handoff practice existed.

| Case | Recorded request / coordination | Follow-through and limitations |
|---|---|---|
| [L3-3926 — SaaS backup restore](https://exasol.atlassian.net/browse/L3-3926), March 2026 | On [03-03, Mihai told Support that SaaS needed to be notified when the restore finished](https://exasol.atlassian.net/browse/L3-3926?focusedCommentId=439317), because follow-up steps were required, and linked the migration procedure. | On [03-05, Mihai reported that the post-backup-restore steps had been applied](https://exasol.atlassian.net/browse/L3-3926?focusedCommentId=439864), then asked Support to have the customer reconnect. |
| [L3-3947 — Adena cluster recreation](https://exasol.atlassian.net/browse/L3-3947), March 2026 | The ticket's plan includes post-restore tasks. On [03-06, Mihai asked Edis for an update on those operations](https://exasol.atlassian.net/browse/L3-3947?focusedCommentId=440170). | On [03-09, Edis confirmed fixing the SSM parameters but said he lacked information from Support about other completed steps](https://exasol.atlassian.net/browse/L3-3947?focusedCommentId=440399). He later [confirmed step 7 was done](https://exasol.atlassian.net/browse/L3-3947?focusedCommentId=440558). The handoff occurred; visibility into the wider migration was still incomplete. |
| [L3-4084 — Totally Group / Production2](https://exasol.atlassian.net/browse/L3-4084), July 2026 | On [07-24, Fardin explicitly tagged Mihai, Edis, Avantika and Andrew to run post-migration steps](https://exasol.atlassian.net/browse/L3-4084?focusedCommentId=472005), linking the procedure. | [Mihai replied that the work was already done](https://exasol.atlassian.net/browse/L3-4084?focusedCommentId=472006). On [07-27, Fardin requested the task again from Haibo](https://exasol.atlassian.net/browse/L3-4084?focusedCommentId=472301); [Haibo then listed completed post-migration tasks](https://exasol.atlassian.net/browse/L3-4084?focusedCommentId=472337). The repeated requests and differing completion reports show that status and scope were not consistently understood. |

These examples establish a documented practice, not consistently clear or verified end-to-end execution. They do **not** establish that VENI's handoff or post-migration configuration was completed, nor what was communicated to VENI's customer. The VENI-specific evidence gap remains.

Source coverage: all 6 comments on L3-3926, all 9 on L3-3947 and all 43 on L3-4084 were retrieved on 2026-09-11. The examples concern March and July work, not September delivery.

### VENI-specific tracking gap

The investigation's Jira searches did not identify a VENI post-migration configuration task:

- `text ~ "post-migration"` created ≥ 2026-06-01 — nothing on VENI.
- `text ~ "exa_monitoring_user"` across all of Jira — the search was recorded as returning no issue. Its exact execution time was not retained; this is not a current census, because SPOT-32540 was subsequently documented in this investigation.
- [L3-4267](https://exasol.atlassian.net/browse/L3-4267) has **no comment after 2026-07-02**. Edis's 07-01 Slack note says "we still need to perform some additional configuration before the customer can see the database in the UI". No linked implementation task or completion comment was found in the reviewed material.
- L3-4267 was **auto-closed**: `Automation for Jira`, 2026-07-14 08:30:34, resolution `Success`, triggered by the Salesforce case flipping to `Closed`. No human resolved it. Last human action was Edis moving it to In Review on 07-01 16:08.

Adjacent but not the same thing: [SPOT-31015](https://exasol.atlassian.net/browse/SPOT-31015) "EXAmigration: Migrated connections missing passwords" (Major, Stefan Reich, Resolved, 05.06.2026) — that is about CONNECTION objects, not database users, so it does not cover the `exa_monitoring_user` breakage.

**Configuration completion is not documented in the reviewed recovery records.** SPOT-32540 tracks alerting for failed auto-stop connections, but does not establish that credentials or other post-migration configuration have been repaired.

[SPOT-32614](https://exasol.atlassian.net/browse/SPOT-32614), created 2026-09-11, separately tracks automatic repair of missing technical users, credential drift and missing required grants. The goal is to remove manual technical-user synchronization from the post-migration procedure; other configuration steps remain unchanged. Filing the story does not establish that the affected databases have been repaired.

## The customer-facing RCA — L3-4267 attachment 128736

[`RCA No SaaS Databases in Account - Case 96293.pdf`](https://exasol.atlassian.net/rest/api/3/attachment/content/128736) — 4 pages, dated 03.07.2026, attached to [L3-4267](https://exasol.atlassian.net/browse/L3-4267) on 2026-07-07 10:56 by the Salesforce connector as attachment `128736`. Salesforce case 00096293. SDM Gerardo Abihaggle, AE Brian Cunningham. **Customer-facing RCA; delivery is supported by the case workflow, but the outbound message is not included in the reviewed evidence.**

The document lives on the ticket, not in this vault. Local working copies (outside the vault, so they do not sync or render here): `~/exports/l3-4443-veni/RCA No SaaS Databases in Account - Case 96293.pdf` and the extracted text `~/exports/l3-4443-veni/rca-96293-layout.txt`.

The timeline below follows the document's own row order, preserved by layout-mode text extraction.

Its timeline, verbatim:

| RCA says | |
|---|---|
| 2026-06-02 16:01 | Offboarding case created — Commercial Delivery created offboarding case 00095779 |
| 2026-06-29 09:26 | Database deleted — for account `acc_JLkQkqwHTuaFW9sqf-r-xQ` |
| 2026-06-30 08:48 | Incident created — Blocker, SF case 00096293 |
| 2026-06-30 11:40 | Restore procedure started — **"Restore procedure was started for database VENI01"** |
| 2026-07-30 21:29 | Restore issue identified — "Post-recovery storage validation identified inconsistencies that prevented certification of the recovered environment for production use" |
| 2026-07-01 09:30 | Recovery path changed — **"Migrate from database VENI01 to database VENI03 using Exasol ExaMigration tool"** |
| 2026-07-01 16:07 | Database running — **"The new database was scaled down to size S and confirmed up and running"** |
| 3. July 2026 09:28 | Confirmation — running normally, data loading completed |

The RCA timeline identifies VENI01 as the initial restore target and later migration source, and the ExaMigration target as the delivered environment. It independently supports that "scaled down to size S" refers to the **new** database, not VENI01.

Root cause stated in the RCA: *"execution of an approved SaaS offboarding workflow that deleted the customer's database environment after contract expiration validation. The offboarding process did not include a mandatory operational and customer confirmation checkpoint before executing the destructive action."* Contributing factors: commercial status used as the primary readiness signal; no dual approval; customer operational access expectations not validated. Corrective actions listed: mandatory customer confirmation before deletion, dual approval, formal offboarding checklist, better visibility between CD / Support / Account Management, regular recovery testing, periodic audit. Related process work is tracked in [SPOT-31532](https://exasol.atlassian.net/browse/SPOT-31532)'s subtasks; the four listed subtasks do not explicitly cover every RCA action.

**What is wrong with it:**

1. **A wrong date in the timeline — confirmed.** The row `2026-07-30 21:29 | Restore issue identified` sits between the `2026-06-30 11:40` and `2026-07-01 09:30` rows in the document's own layout, and describes the storage error found on **2026-06-30** 21:29 ([c465871](https://exasol.atlassian.net/browse/L3-4267?focusedCommentId=465871) is 20:51 CEST that evening). `07-30` should read `06-30`. Layout-mode extraction preserves the row order, so this is a month error in the RCA rather than a cell-ordering artefact.
    The separate `2026-06-02 16:01 | Offboarding case created` row is not a date error. It refers to *Salesforce* case 00095779, which can predate [L3-4264](https://exasol.atlassian.net/browse/L3-4264)'s 26.06 Jira creation — [CD-7941](https://exasol.atlassian.net/browse/CD-7941) on the same offboarding goes back to 03.03.2026.
2. **It does not address the remaining databases.** VENI01 after migration, VENI02 in `maintenance`, Database01 and Database02 do not appear. The RCA closes with "The customer's service has been fully restored in a new production environment" and says nothing about four surplus databases remaining on the account — the subject of L3-4443 items 1 and 3.

**Naming:** the RCA calls the delivered database **VENI03**, while the platform names it `Migration` (`jLoRP5ZSSF-NQuh898tzvw`). The customer identifies `Migration` in L3-4443.

### What the RCA does and does not support

The RCA documents the intended handover, but not the cleanup or instructions about the remaining databases.

**Intended handover.** VENI01 appears twice in the RCA, both times as a recovery step:

- `2026-06-30 11:40 | Restore procedure started | Restore procedure was started for database VENI01.`
- `2026-07-01 09:30 | Recovery path changed | Migrate from database VENI01 to database VENI03 using Exasol ExaMigration tool.`

The delivered environment is named in the singular: *"restored to **a new production environment**, which was returned to service on 1st July 2026"* (Executive Summary) and *"The customer's service has been fully restored in **a new production environment**"* (Customer Communication). VENI01 is described as a recovery step, not as that delivered environment.

**Cleanup and use instructions.** The RCA never says VENI01 should not be used, is temporary, or will be removed — the words *remove*, *decommission*, *temporary*, *intermediate* and *surplus* do not appear in relation to it. `deleted` appears only about the original databases and the offboarding process. VENI02, Database01 and Database02 are never named.

A customer reading the RCA and seeing five databases in the UI receives no instruction in that document to avoid four of them. The phrase *"fully restored"* could reasonably be read as normal service restored, not as a warning about surplus environments.

**Conclusion:** the intended handover is on the record; instructions not to use VENI01 are not. "We did not intend to hand VENI01 over" is supported by the RCA's timeline. The RCA does not establish that the customer was told this.

### What the RCA is evidence of

**The RCA is Exasol's customer-facing account of the incident.** It carries Exasol letterhead, hotline and portal details, is addressed to VENI Energy Group, and names SDM Gerardo Abihaggle and AE Brian Cunningham on its Contact page. It reached Jira through the Salesforce connector from the customer-facing case. L3-4267 changed to `Waiting for Customer` three seconds before the attachment landed (07-07 10:56:44 → 10:56:47). This supports intended customer delivery, but does not replace the outbound message or establish the contents of other emails and calls.

**What it therefore does and does not establish:**

| claim | supported? |
|---|---|
| VENI01 was where the restore was attempted | **yes** — timeline, 06-30 11:40 |
| the ExaMigration target is what was delivered | **yes** — timeline 07-01 09:30, plus *"restored to a new production environment"* twice |
| the customer was told VENI01 was surplus / not to be used | **not established by the RCA** — it never says this; other correspondence remains unreviewed |
| the customer was told anything about VENI02, Database01, Database02 | **not established by the RCA** — these are never named; other correspondence remains unreviewed |

The Customer Communication section claims only: acknowledged the incident, diagnosed it as related to the prior offboarding, executed recovery, *"provided regular status updates throughout the restoration efforts"*, and *"The customer's service has been fully restored in a new production environment."* No instruction about which database to use or leave alone appears anywhere in it.

**Conclusion for the customer reply:** the RCA supports that VENI01 was not the intended handover database. It does not support a claim that the customer was told not to use it. The transition history shows that VENI01 remained startable at Medium; any separate instruction or cleanup decision still needs evidence.

---

## Verified on the live `Migration` DB (2026-09-08 14:09 CEST)

Nodes for `jLoRP5ZSSF-NQuh898tzvw` (stack `kpcgenarvghd`, eu-west-1, profile `prodc-admin`), all `running`:
`n10 i-013c37278983abe59` · `n11 i-0c9e296c207a95761` · `n12 i-0fb78a59e86b29687` · `n13 i-0b4ec8bfda835d503` · `n14 i-0c69d707cf266f54c`.
n10 refuses 8563 (`Connection refused`); the DB answers on **n11–n14** — cluster nodes carry the `saas:ClusterUUID` tag, n10 does not.

`SELECT 1` succeeds on n11, but **as `sys`** — `cos_exaplus_query` hardcodes `-u sys` with the `dwad_client` password and takes no user/password argument. **`sys` is not the auto-shutdown credential** (`auto_shutdown.py` connects as `exa_monitoring_user` with the SSM password), so this proves only that the database is up and reachable. The monitoring-user failure is established from the two sources below.

### Monitoring-user authentication failures and the credential hypothesis

| USER_NAME | CREATED | PASSWORD_STATE | FAILED_LOGIN_ATTEMPTS |
|---|---|---|---|
| **EXA_MONITORING_USER** | 2023-12-27 10:21:28 | VALID | **86,593** |
| EXA_SAAS_ADMIN_USER | 2023-12-27 10:21:17 | VALID | 0 |
| EXA_EXTERNAL_USAGE_USER | 2023-12-27 10:21:28 | VALID | 0 |
| SYS | 2026-07-01 12:52:17 | VALID | 0 |

The user table and Lambda logs support the following findings:

1. **Authentication failures are confirmed; an SSM/DB credential mismatch is the leading explanation.** `exa_monitoring_user` exists with `PASSWORD_STATE` = `VALID` and **86,593** failed login attempts. The auto-shutdown Lambda separately reports connection failures:

    | source | evidence |
    |---|---|
    | Caller side — CloudWatch `/aws/lambda/prod-auto-shutdown-StopDatabases` | `Connection to database failed: … jLoRP5ZSSF-NQuh898tzvw=>qYelI2ZcQ9-fqQ47ir1oJA, Error:` in sampled 15-minute runs: 2026-08-05 12:00, 2026-08-20 12:00, 2026-09-03 12:00 |
    | Database side — `SYS.EXA_DBA_USERS` on n11, 2026-09-08 | `EXA_MONITORING_USER` `FAILED_LOGIN_ATTEMPTS` = **86,593**, `PASSWORD_STATE` = `VALID` |

    These independent sources are consistent with a credential mismatch, but the cumulative counter does not tie individual failures to the Lambda. No direct monitoring-credential authentication result or successful post-repair idle check is recorded.
2. **The service-user dates support inheritance from the deleted database.** All three service users carry `CREATED 2023-12-27 10:21`, the creation date of `EXA_DB` (`S11uTYyGRDeIuR4wivF-3Q`, created 2023-12-27 09:09:05), rather than this deployment. Only `SYS` shows this DB's own date, 2026-07-01 12:52:17. Inherited password hashes not reconciled with new deployment secrets are a plausible mechanism; creation dates alone do not prove which password was retained or which configuration step was omitted.

### Potential impact beyond auto-stop — unverified

If all **86,593** failures accrued in the 69 days since 2026-07-01, the average would be ~1,250/day, approximately one per minute. Auto-stop's 15-minute schedule accounts for 96 runs/day. This raises the possibility of other failing consumers, but the counter's start/reset time, retry behavior, and caller breakdown are unknown.

In `saas-terraform`, `monitoring_db_user` also feeds `modules/saas-monitoring/sensors/select1-lambda.tf` (`EXA_USER`) and `modules/volume-snapshot/snapshot-policy/lambda.tf` (`DATABASE_USER`). Shared credentials make the availability sensor and snapshot policy candidates for the same failure. Their logs, schedules, and successful runs must be checked before claiming either was affected or failed since 01 July.

`EXA_SAAS_ADMIN_USER` and `EXA_EXTERNAL_USAGE_USER` show **0** failures. This does not establish that they are unused; successful logins would not raise a failed-login counter.

### Session views and limits of the available history

The session views resolve without the `SYS.` qualifier. A query using `SYS.EXA_DBA_SESSIONS_LAST_DAY` returns "object not found"; this does not establish that the view is missing or auditing is disabled.

| database | query | result |
|---|---|---|
| prod mgmt saasdb `i-0af4f9152b7b8ad1c` | `SELECT COUNT(*) FROM SYS.EXA_DBA_SESSIONS_LAST_DAY` | object not found |
| prod mgmt saasdb | `SELECT COUNT(*) FROM EXA_DBA_SESSIONS_LAST_DAY` | **2,659 rows** |
| `Migration` `qYelI2ZcQ9-fqQ47ir1oJA` | `SELECT COUNT(*), MIN(LOGIN_TIME), MAX(LOGIN_TIME) FROM EXA_DBA_SESSIONS_LAST_DAY` | **2,028 rows, 2026-07-21 03:17 → 2026-09-08 15:19** |

These are separate recorded observations, not a reconciled snapshot. The grouped counts below sum to **2,056**, not **2,028**; capture times, filters, and the result's time zone are missing.

`EXA_SYSCAT` lists the full family on both: `EXA_DBA_AUDIT_SESSIONS`, `EXA_DBA_AUDIT_SQL`, `EXA_DBA_SESSIONS_LAST_DAY`, `EXA_SQL_LAST_DAY`, `EXA_DBA_PROFILE_LAST_DAY` and others.

**Implications for auto-stop and the August investigation:**

1. `auto_shutdown.py`'s idle query reads `EXA_SQL_LAST_DAY` and `EXA_DBA_SESSIONS_LAST_DAY`. The recorded checks identify these views on `Migration` and the management DB; the session query returns rows. A `SYS.` lookup failure is not evidence that the idle-query views are absent. A successful idle check after credential repair still needs verification.
2. **An old login timestamp does not establish extended retention.** `MIN(LOGIN_TIME)` is 2026-07-21 because one session opened that day remains connected (`LOGOUT_TIME` is null). The recorded login-day breakdown for `Migration` is one session from 2026-07-21, 1,063 from 2026-09-07, and 992 from 2026-09-08, with none in between. This does not demonstrate 49 days of session retention.
3. **Restarting cannot recreate expired session history.** Edis's proposed check ([c484791](https://exasol.atlassian.net/browse/L3-4443?focusedCommentId=484791), "start the DB and check active sessions") can inspect current sessions, not reconstruct August workload. The observations above concern `Migration`; they do not establish the contents or retention of VENI01's separate audit views or archived logs.

---

## Follow-up ticket raised from this investigation

[SPOT-32540](https://exasol.atlassian.net/browse/SPOT-32540) — **"Auto-stop silently skips the idle check when it cannot connect to the database - add an alert"**. Story, component `SaaS`, created by Mihai Dinca 2026-09-08 12:58, **Draft, unassigned**, linked to [L3-4443](https://exasol.atlassian.net/browse/L3-4443) as *is part of*. Updated 2026-09-08 13:50.

The ticket proposes closing an observability gap; **no deployed fix is recorded**. `check_database()` in `modules/auto-shutdown-idle-databases/src/auto_shutdown.py` catches the connection exception, logs one line, returns `None`, and issues no stop or alert. A broken monitoring login can therefore leave a cluster running without an idle check. VENI01's recorded continuous interval is 719.51 h; `Migration` had reached approximately 69 days as of 09-08.

The ticket includes both DB and cluster UUIDs, the Lambda log-line samples, and the 86,593 failed-login counter. The select1 / snapshot-policy inference is marked *not yet verified*.

**Scope recommendation, not yet agreed:** cover authentication failures across consumers, rather than auto-stop alone. `monitoring_db_user` is shared by auto-shutdown, `modules/saas-monitoring/sensors/select1-lambda.tf` (`EXA_USER`), and `modules/volume-snapshot/snapshot-policy/lambda.tf` (`DATABASE_USER`). An auto-stop-only alert would not report the other services' authentication failures if they occur. Their actual impact remains unverified.

### Existing select1 creation fix and deployment evidence

**Checked against Jira, GitHub source, and CI records on 2026-09-10.** The direct-creation fix is tracked under [SPOT-31207](https://exasol.atlassian.net/browse/SPOT-31207), **"database recovery e2e test is broken"** (Resolved, assigned to Haibo Lei), not the old implementation story SPOT-26133. Its description is empty; the implementation scope is documented in [saas-terraform PR #1160](https://github.com/exasol/saas-terraform/pull/1160), merged **2026-06-24 11:17:38 UTC**, commit `2a9caf3aa35d7867c26c06a7f9f95fa13697c349`.

The fix calls the select1 schedule-creation SFN directly from `database_create`, immediately after `CreateBackupSensor`. It removes that path's dependency on a matching SNS/SQS/pipe event. After retries are exhausted, it alerts and continues database creation. This is separate from monitoring-user credential repair and SPOT-32540's auto-stop alert proposal.

**Merge is not deployment.** The fix's [production job](https://github.com/exasol/saas-terraform/actions/runs/28094670177/job/83181034075) remained waiting and executed no steps; it ultimately failed on 24 July with a deployment-protection annotation. From 25 June, normal main-branch deployments targeted test and limited master modules, not production. The reviewed release runs before `Migration`'s creation contained no `v*` production release. The successful [26 June production job](https://github.com/exasol/saas-terraform/actions/runs/28237875751/job/83657030266) only updated the Datadog agent configuration.

**Conclusion:** CI history supports the hypothesis that the direct select1 creation fix had not reached production when `Migration` was created on **2026-07-01 10:18:56 UTC**, despite having been merged a week earlier. It does not establish the exact historical AWS definition or exclude a deployment outside CI. Those remain the checks needed to confirm the deployed-code explanation; a missing schedule alone does not establish that restore/examigration caused its absence.

---

## Billing query and complete interval rows

Supplied 2026-09-10 by Mihai. Source: `SAAS.CLUSTER_USAGE_INTERVALS` and `SAAS.PRICES`. Times are UTC in 2026; a time without a date uses the date at the start of its row. `service_from_ts` / `service_to_ts` are the interval intersected with the in-service window; capped billable transition rows must not be read as the full transition duration. `USD = billing_vcpu_hours × price_per_unit`, where price is per vCPU-hour. The query selects `subscription_status`; that column was not included in the supplied formatted tables.

```sql
SELECT CASE c.db_uuid WHEN '24TAKI_mQOahKMm2FiGlpw' THEN 'VENI01' ELSE 'VENI02' END AS db,
       c.tshirt_size, c.family_name, c.from_status, c.subscription_status,
       c.service_from_ts, c.service_to_ts,
       ROUND(HOURS_BETWEEN(c.service_to_ts, c.service_from_ts),4) AS wall_h,
       c.vcpu_rate,
       ROUND(c.billing_vcpu_hours,4)                          AS vcpu_h,
       p.price_per_unit                                       AS usd_per_vcpu_h,
       ROUND(c.billing_vcpu_hours * p.price_per_unit,2)       AS usd
FROM saas.CLUSTER_USAGE_INTERVALS c
JOIN saas.PRICES p ON p.name = c.product_name
WHERE c.db_uuid IN ('24TAKI_mQOahKMm2FiGlpw','VK8805V4RbSicxSIYihpFg')
ORDER BY db, c.service_from_ts, c.from_status;
```

### VENI01 — 41 interval rows

Database `24TAKI_mQOahKMm2FiGlpw`. `rate` is cluster vCPU count; row USD values are individually rounded.

| # | size/fam | status | window (UTC) | wall h | rate | vCPU-h | $/vCPU-h | USD |
|---|---|---|---|---|---|---|---|---|
| 1 | XS r5d | tocreate | 06-30 09:56:19.657 → 09:56:22.986 | 0.0009 | 8 | 0 | 0.45 | 0 |
| 2 | XS r5d | creating | 06-30 09:56:22.986 → 10:11:22.986 | 0.2500 | 8 | 2.0000 | 0.45 | 0.90 |
| 3 | XS r5d | running | 06-30 10:13:51.807 → 10:45:52.230 | 0.5335 | 8 | 4.2676 | 0.45 | 1.92 |
| 4 | XS r5d | tostop | 06-30 10:45:52.230 → 10:46:03.551 | 0.0031 | 8 | 0 | 0.45 | 0 |
| 5 | XS r5d | stopping | 06-30 10:46:03.551 → 10:48:49.169 | 0.0460 | 8 | 0.3680 | 0.45 | 0.17 |
| 6 | XS r5d | stopped | 06-30 10:48:49.169 → 11:35:46.837 | 0.7827 | 8 | 0 | 0.45 | 0 |
| 7 | XS r5d | maintenance | 06-30 11:35:46.837 → 07-01 06:54:49.371 | 19.3174 | 8 | 0 | 0.45 | 0 |
| 8 | XS r5d | running | 07-01 06:54:49.371 → 07:44:33.763 | 0.8290 | 8 | 6.6320 | 0.45 | 2.98 |
| 9 | XS r5d | maintenance | 07-01 07:44:33.763 → 09:24:43.803 | 1.6695 | 8 | 0 | 0.45 | 0 |
| 10 | XS r5d | scaling | 07-01 09:24:43.803 → 09:30:15.706 | 0.0922 | 8 | 0.7376 | 0.45 | 0.33 |
| 11 | XS r5d | running | 07-01 09:30:15.706 → 10:23:13.298 | 0.8827 | 8 | 7.0613 | 0.45 | 3.18 |
| 12 | M r5d | toscale | 07-01 10:23:13.298 → 10:23:39.734 | 0.0073 | 32 | 0 | 0.45 | 0 |
| 13 | M r5d | scaling | 07-01 10:23:39.734 → 10:29:08.796 | 0.0914 | 32 | 2.9250 | 0.45 | 1.32 |
| 14 | M r5d | running | 07-01 10:29:08.796 → 10:29:54.723 | 0.0128 | 32 | 0.4082 | 0.45 | 0.18 |
| 15 | M r5d | error | 07-01 10:29:54.723 → 10:30:11.176 | 0.0046 | 32 | 0 | 0.45 | 0 |
| 16 | M r5d | running | 07-01 10:30:11.176 → 10:30:25.862 | 0.0041 | 32 | 0.1305 | 0.45 | 0.06 |
| 17 | M r5d | error | 07-01 10:30:25.862 → 10:31:25.026 | 0.0164 | 32 | 0 | 0.45 | 0 |
| 18 | M r5d | running | 07-01 10:31:25.026 → 10:48:39.525 | 0.2874 | 32 | 9.1955 | 0.45 | 4.14 |
| 19 | M r5d | error | 07-01 10:48:39.525 → 10:51:10.560 | 0.0420 | 32 | 0 | 0.45 | 0 |
| 20 | M r5d | running | 07-01 10:51:10.560 → 18:10:47.188 | 7.3268 | 32 | 234.4589 | 0.45 | 105.51 |
| 21 | M r5d | tostop | 07-01 18:10:47.188 → 18:11:14.231 | 0.0075 | 32 | 0 | 0.45 | 0 |
| 22 | M r5d | stopping | 07-01 18:11:14.231 → 18:14:02.256 | 0.0467 | 32 | 1.4936 | 0.45 | 0.67 |
| 23 | M r5d | stopped | 07-01 18:14:02.256 → 07-31 10:33:24.000 | 712.3227 | 32 | 0 | 0.45 | 0 |
| 24 | M r5d | stopped | 07-31 10:33:24.000 → 08-05 11:51:19.628 | 121.2988 | 32 | 0 | 0.45 | 0 |
| 25 | M r5d | tostart | 08-05 11:51:19.628 → 11:51:33.921 | 0.0040 | 32 | 0 | 0.45 | 0 |
| 26 | M r5d | starting | 08-05 11:51:33.921 → 11:54:18.861 | 0.0458 | 32 | 1.4661 | 0.45 | 0.66 |
| 27 | M r5d | running | 08-05 11:54:18.861 → 08-31 10:33:23.000 | 622.6511 | 32 | 19,924.8368 | 0.45 | 8,966.18 |
| 28 | M r5d | running | 08-31 10:33:23.000 → 09-04 11:25:06.564 | 96.8621 | 32 | 3,099.5872 | 0.45 | 1,394.81 |
| 29 | M r5d | tostop | 09-04 11:25:06.564 → 11:25:15.436 | 0.0025 | 32 | 0 | 0.45 | 0 |
| 30 | M r5d | stopping | 09-04 11:25:15.436 → 11:27:36.959 | 0.0393 | 32 | 1.2580 | 0.45 | 0.57 |
| 31 | M r5d | stopped | 09-04 11:27:36.959 → 11:34:47.638 | 0.1196 | 32 | 0 | 0.45 | 0 |
| 32 | M r5d | tostart | 09-04 11:34:47.638 → 11:35:04.906 | 0.0048 | 32 | 0 | 0.45 | 0 |
| 33 | M r5d | starting | 09-04 11:35:04.906 → 11:37:14.918 | 0.0361 | 32 | 1.1557 | 0.45 | 0.52 |
| 34 | M r5d | running | 09-04 11:37:14.918 → 11:37:53.997 | 0.0109 | 32 | 0.3474 | 0.45 | 0.16 |
| 35 | XS r6id | toscale | 09-04 11:37:53.997 → 11:37:55.682 | 0.0005 | 8 | 0 | 0.495 | 0 |
| 36 | XS r6id | scaling | 09-04 11:37:55.682 → 11:38:21.351 | 0.0071 | 8 | 0.0570 | 0.495 | 0.03 |
| 37 | XS r6id | scaling | 09-04 11:38:21.351 → 11:42:53.698 | 0.0757 | 8 | 0.6052 | 0.495 | 0.30 |
| 38 | XS r6id | running | 09-04 11:42:53.698 → 11:45:35.081 | 0.0448 | 8 | 0.3586 | 0.495 | 0.18 |
| 39 | XS r6id | tostop | 09-04 11:45:35.081 → 11:45:39.966 | 0.0014 | 8 | 0 | 0.495 | 0 |
| 40 | XS r6id | stopping | 09-04 11:45:39.966 → 11:47:34.529 | 0.0318 | 8 | 0.2546 | 0.495 | 0.13 |
| 41 | XS r6id | stopped | 09-04 11:47:34.529 → 09-10 07:06:13 (open) | 139.3109 | 8 | 0 | 0.495 | 0 |

### VENI02 — 9 interval rows

Database `VK8805V4RbSicxSIYihpFg`. `rate` is cluster vCPU count; row USD values are individually rounded.

| # | size/fam | status | window (UTC) | wall h | rate | vCPU-h | $/vCPU-h | USD |
|---|---|---|---|---|---|---|---|---|
| 1 | XS r5d | tocreate | 06-30 09:57:50.716 → 09:57:53.785 | 0.0009 | 8 | 0 | 0.45 | 0 |
| 2 | XS r5d | creating | 06-30 09:57:53.785 → 10:12:53.785 | 0.2500 | 8 | 2.0000 | 0.45 | 0.90 |
| 3 | XS r5d | running | 06-30 10:15:29.819 → 11:00:51.440 | 0.7560 | 8 | 6.0480 | 0.45 | 2.72 |
| 4 | XS r5d | tostop | 06-30 11:00:51.440 → 11:01:02.116 | 0.0030 | 8 | 0 | 0.45 | 0 |
| 5 | XS r5d | stopping | 06-30 11:01:02.116 → 11:03:48.351 | 0.0462 | 8 | 0.3694 | 0.45 | 0.17 |
| 6 | XS r5d | stopped | 06-30 11:03:48.351 → 13:51:29.305 | 2.7947 | 8 | 0 | 0.45 | 0 |
| 7 | XS r5d | maintenance | 06-30 13:51:29.305 → 07-31 10:33:24.000 | 740.6985 | 8 | 0 | 0.45 | 0 |
| 8 | XS r5d | maintenance | 07-31 10:33:24.000 → 08-31 10:33:23.000 | 743.9997 | 8 | 0 | 0.45 | 0 |
| 9 | XS r5d | maintenance | 08-31 10:33:23.000 → 09-10 07:06:13 (open) | 236.5474 | 8 | 0 | 0.45 | 0 |
