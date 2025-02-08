---
id: "2024-05-14"
aliases:
  - Backlog
tags: []
---

- Security Hardening
- Log Management (including Centralised Log Management)
- Monitoring migration from Datadog to internal stack
- AWS Account Migration
- Disaster Recover Tests & Automation
- Further operational tests, such as multi-node setup for management node (not a priority right now)
- Multi-region saas management system
- Cost Optimisation
- CI/CD for deployment, as well as for customer database?
- AWS Log Management? Related to Datadog to internal stack migration
- Improvements of AWS account management (multiple accounts for customer deployment)
- Implementation of new monitoring features, such as backup monitoring, monitoring using logs, etc
- SLO monitoring & alerting & root cause analyse
- Capacity Management
- etc

Security Backlog Ideas:

- Security Hub findings - created a review ticket (
  https://exasol.atlassian.net/browse/SAAS-1384
  ) - in progress* IMDSv1 -> IMDSv2 - Tested and works fine ( implementation done, c4 has configurable parameter for IMDSv1 and IMDSv2)* Guardduty - auto remediation if there is a security breach & alert mechanism -> Centralised Security Log Management ( in discussion)\* Infrastructure pen test (epic ticket SPOT-16938, in progress )Priority ordered:

- Security Patch Management (agreement reached regarding to short term, blocked by customer db updates, but still prepare the solution just in case)_ Backup monitoring & testing (blocked, waiting for the cos team, agreement reached regarding to short term solution)_ Cost control measures (done)\* SLI -> Datadog (done)
- Script to collect Data from instances (done)
- R&D cloud cost dashboard (done)
- Prepare update script to invoke by e2e tests, as input, region, new version, DB UUID (done, Mihai can use update script)
- Datadog plugin migration to lambda function to use sns/sqs events (in progress)
- Log collection adjustments (in discussion)\* Disaster Recover Tests & Automation (

https://exasol.atlassian.net/wiki/spaces/SAAS/pages/10518716/SaaS+Disaster+Recovery+Plan

Define scope for the test & automation. Simple cases, such as if we loose management node what will happen?)
