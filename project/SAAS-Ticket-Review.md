---
id: SAAS-Ticket-Review
aliases:
  - SAAS ticket review
tags:
  - project
  - jira
  - triage
---

# SAAS ticket review (updated 2026-11-11)

These are all the open tickets in the SAAS project (37 total): 8 assigned to me, 0 unassigned, and 29 assigned to others. For each one, tick it once reviewed and write the decision: **close**, **keep**, **reassign**, or **move to SPOT**.

JQL: `project = SAAS AND statusCategory != Done`
Backlink: [[2026-11-11]]

> [!info] Cleanup on 2026-11-11
> - 69 of my tickets were closed as **Obsolete** with `scripts/close_obsolete_saas_tickets.py`: the 66 last updated before 2025, plus SAAS-1697, SAAS-1759 and SAAS-1760.
> - 10 more of my tickets were closed by hand: SAAS-1716, 1788, 1793, 1799, 1851 and 1856 as Obsolete; SAAS-1744, 1752 and 1845 as Fixed; SAAS-1730 as Done.
> - 59 unassigned tickets with no activity since before 2026 were closed as **Obsolete** with the same script.
> - 8 more closed: SAAS-6, 270, 451, 913 (Former user) and SAAS-529, 882 (Manuel Hiemer) as Obsolete; SAAS-1794 as Fixed; SAAS-1813 as Won't Do. SAAS-1823 was assigned to me.

## Assigned to me (8)

- [ ] [SAAS-1823](https://exasol.atlassian.net/browse/SAAS-1823): AWS Request
  - Open · Task · updated 2026-11-11 · reporter Yuvaraj Muniyandi
  - Decision: 
- [ ] [SAAS-1798](https://exasol.atlassian.net/browse/SAAS-1798): AWS Request
  - Draft · Task · updated 2026-11-11 · reporter Automation for Jira
  - Decision: 
- [ ] [SAAS-1795](https://exasol.atlassian.net/browse/SAAS-1795): I need access to AWS prod SaaS for monitoring and alert resolution
  - Draft · Task · updated 2026-11-11 · reporter Automation for Jira
  - Decision: 
- [ ] [SAAS-1782](https://exasol.atlassian.net/browse/SAAS-1782): Reset AWS PW - Iaroslav Babanin
  - Draft · Task · updated 2026-11-11 · reporter Cameron Woods
  - Decision: 
- [ ] [SAAS-1857](https://exasol.atlassian.net/browse/SAAS-1857): [Prod Maintenance] Restart SaaS Management Node to mitigate CVE
  - In Review · Task · updated 2026-11-11 · reporter Aditya Bora
  - Decision: 
- [ ] [SAAS-1731](https://exasol.atlassian.net/browse/SAAS-1731): Please disable clud accounts for Fabian Wolff and Sebastian Nehls
  - In Review · Bug · updated 2026-11-10 · reporter Andreas Schmidt
  - Decision: 
- [ ] [SAAS-1844](https://exasol.atlassian.net/browse/SAAS-1844): AWS Request [Want access to S3 bucket]
  - Open · Bug · updated 2026-11-06 · reporter Sree Sankar Krishna Madhavan
  - Decision: 
- [ ] [SAAS-1787](https://exasol.atlassian.net/browse/SAAS-1787): AWS access to upload to s3 buckets x - t
  - In Review · Bug · updated 2026-01-26 · reporter Manomay Mali
  - Decision: 

## Unassigned (0)


## Assigned to others (29)

### Andrew MacLean (8)

- [ ] [SAAS-910](https://exasol.atlassian.net/browse/SAAS-910): Disaster Recovery
  - In Review · Sub-task · updated 2023-11-16 · reporter Mark Rees
  - Decision: 
- [ ] [SAAS-1552](https://exasol.atlassian.net/browse/SAAS-1552): R&D CI missing aws permissions
  - Open · Task · updated 2023-08-24 · reporter Benedikt McMullin
  - Decision: 
- [ ] [SAAS-920](https://exasol.atlassian.net/browse/SAAS-920): Vulnerability Scanning
  - In Implementation · Sub-task · updated 2023-06-15 · reporter Mark Rees
  - Decision: 
- [ ] [SAAS-917](https://exasol.atlassian.net/browse/SAAS-917): HR Security
  - In Implementation · Sub-task · updated 2023-06-15 · reporter Mark Rees
  - Decision: 
- [ ] [SAAS-916](https://exasol.atlassian.net/browse/SAAS-916): Separate Dev/Testing & Production Environments
  - In Implementation · Sub-task · updated 2023-06-15 · reporter Mark Rees
  - Decision: 
- [ ] [SAAS-898](https://exasol.atlassian.net/browse/SAAS-898): Complete ITSec and Compliance Requirements for SaaS GA Release
  - In Implementation · Task · updated 2023-06-08 · reporter Mark Rees
  - Decision: 
- [ ] [SAAS-433](https://exasol.atlassian.net/browse/SAAS-433): SEC- AWS Well Architected Framework assessment
  - Draft · Task · updated 2023-05-25 · reporter Former user
  - Decision: 
- [ ] [SAAS-1279](https://exasol.atlassian.net/browse/SAAS-1279): Test multi-AZ setup
  - Draft · Task · updated 2023-05-25 · reporter Ali Ismayilov
  - Decision: 

### Ali Mohamed (3)

- [ ] [SAAS-1852](https://exasol.atlassian.net/browse/SAAS-1852): Read access to AWS invoice summaries for the BI data warehouse (4 AWS accounts)
  - Open · Task · updated 2026-10-23 · reporter Mikhail Zhadanov
  - Decision: 
- [ ] [SAAS-1832](https://exasol.atlassian.net/browse/SAAS-1832): AWS Request - Cost Explorer Permissions
  - Open · Task · updated 2026-07-15 · reporter Daniel Zinser
  - Decision: 
- [ ] [SAAS-1827](https://exasol.atlassian.net/browse/SAAS-1827): AWS Request
  - In Review · Bug · updated 2026-07-02 · reporter Andrii Kulyk
  - Decision: 

### Mohamed Tamraz (3)

- [ ] [SAAS-900](https://exasol.atlassian.net/browse/SAAS-900): PCI DSS Compliant
  - In Implementation · Sub-task · updated 2021-11-22 · reporter Mark Rees
  - Decision: 
- [ ] [SAAS-904](https://exasol.atlassian.net/browse/SAAS-904): Cloud Security
  - In Implementation · Sub-task · updated 2021-10-18 · reporter Mark Rees
  - Decision: 
- [ ] [SAAS-902](https://exasol.atlassian.net/browse/SAAS-902): GDPR Compliance
  - In Implementation · Sub-task · updated 2021-10-15 · reporter Mark Rees
  - Decision: 

### Majaydul Chowdhury (2)

- [ ] [SAAS-1657](https://exasol.atlassian.net/browse/SAAS-1657): CLONE - Carbon Footprint Report for Cloud
  - Draft · Task · updated 2024-06-25 · reporter Katharina Berger
  - Decision: 
- [ ] [SAAS-1547](https://exasol.atlassian.net/browse/SAAS-1547): Carbon Footprint Report for Cloud
  - In Implementation Done · Task · updated 2024-05-07 · reporter Edis Shabi
  - Decision: 

### Mihai Dinca (2)

- [ ] [SAAS-1826](https://exasol.atlassian.net/browse/SAAS-1826): Payouts didn't hit our account
  - In Implementation Done · Task · updated 2026-08-18 · reporter Daniel Zinser
  - Decision: 
- [ ] [SAAS-1834](https://exasol.atlassian.net/browse/SAAS-1834): Provide a customer-facing breakdown of the additional infrastructure costs incurred during the VENI database restore.
  - Draft · Task · updated 2026-08-03 · reporter Brian Cunningham
  - Decision: 

### Sebastian Beisch (2)

- [ ] [SAAS-1563](https://exasol.atlassian.net/browse/SAAS-1563): SaaS - Consumption Report - Wrong values in Country and Compnay
  - Draft · Bug · updated 2023-09-25 · reporter Andreas Bonet
  - Decision: 
- [ ] [SAAS-540](https://exasol.atlassian.net/browse/SAAS-540): Okta Discussions - IAM Tenants, URLs, Templates, Email, Configurations
  - Draft · Task · updated 2022-11-04 · reporter Former user
  - Decision: 

### Andreas Bonet (1)

- [ ] [SAAS-186](https://exasol.atlassian.net/browse/SAAS-186): SaaS - Support Policy and Service Level Agreement
  - Open · Sub-task · updated 2026-04-27 · reporter Katharina Berger
  - Decision: 

### Fardin Sabzi (1)

- [ ] [SAAS-1485](https://exasol.atlassian.net/browse/SAAS-1485): Need to generate a new access key
  - Open · Task · updated 2023-05-08 · reporter Fardin Sabzi
  - Decision: 

### Marcel Kempken (1)

- [ ] [SAAS-1414](https://exasol.atlassian.net/browse/SAAS-1414): Google GCP Global HMAC Limit reached
  - Open · Task · updated 2023-06-21 · reporter Automation for Jira
  - Decision: 

### Marco Nätlitz (1)

- [ ] [SAAS-1467](https://exasol.atlassian.net/browse/SAAS-1467): Restrict yotilla-cdk permissions
  - Draft · Task · Major · updated 2023-04-11 · reporter Edis Shabi
  - Decision: 

### Mark Rees (1)

- [ ] [SAAS-901](https://exasol.atlassian.net/browse/SAAS-901): Security and Privacy Policies for SaaS Webseite
  - In Implementation · Sub-task · updated 2021-10-11 · reporter Mark Rees
  - Decision: 

### Marlene Kreß (1)

- [ ] [SAAS-1541](https://exasol.atlassian.net/browse/SAAS-1541): AzureML subcription no cores available for creation of endpoint.
  - Draft · Task · updated 2023-08-21 · reporter Marlene Kreß
  - Decision: 

### Michael Trebes (1)

- [ ] [SAAS-1538](https://exasol.atlassian.net/browse/SAAS-1538): Cloud Accounts
  - In Implementation · Task · updated 2023-11-28 · reporter Florian Wenzel
  - Decision: 

### Nina Sahnow (1)

- [ ] [SAAS-1332](https://exasol.atlassian.net/browse/SAAS-1332): Wrong Company address at Market Place Account - Payer Account 602894545240
  - In Review · Task · updated 2023-03-21 · reporter Nina Sahnow
  - Decision: 

### Thomas Bestfleisch (1)

- [ ] [SAAS-1545](https://exasol.atlassian.net/browse/SAAS-1545): AWS accounts access
  - In Review · Task · updated 2023-08-17 · reporter Oleksandr Kozachuk
  - Decision:
