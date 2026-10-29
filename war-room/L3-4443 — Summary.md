---
ticket: L3-4443
status: in-review
tags:
  - saas
  - l3
  - veni
  - auto-stop
---

# L3-4443 — Summary

## Issue

The customer reported that the `VENI01` database (`MainCluster`, size M) ran continuously from **2026-08-05 11:54 UTC** until they stopped it on **2026-09-04 11:25 UTC**—approximately **719.5 hours / 720 cluster hours**—despite not using it. The database was created during the June/July recovery and was not intended to be the customer’s production database; `Migration` was the environment handed over to the customer.

Jira: [L3-4443](https://exasol.atlassian.net/browse/L3-4443) · Current status: **In Review** · Priority: **Normal**

## Findings

- The continuous run is confirmed in cluster history: `VENI01` stayed in `running` at size M for 719.51 hours with no state change.
- `marius.dyrseth@venienergy.com` started the cluster on 2026-08-05. The customer later stopped and resized it themselves.
- The database showed very little traffic compared with `Migration` (14.13 GB egress in August versus 3,758.80 GB for `Migration`). This supports low usage but does not prove that no workload ran.
- VENI01 had `auto_stop_enabled=true` and `auto_stop_idle_time=30` minutes. The setting was not the problem.
- Auto-stop could not connect to the database using `exa_monitoring_user`. The connection failure was swallowed by the auto-stop code, so no idle measurement or stop command was issued and no alert was generated.
- The likely cause was a recovery/migration configuration failure: technical-user credentials inherited during restore/examigration no longer matched the credentials held by the auto-stop service. This caused repeated login failures after the restore.
- VENI01 was not placed in maintenance mode or removed after it was superseded. Because it remained in a normal stopped state, the customer could start it.

## Customer and billing impact

- VENI01 incurred approximately **$10,360.99** in compute charges for the continuous 2026-08-05 → 2026-09-04 run, based on the supplied billing interval data.
- The customer was charged when VENI01 was started. VENI02 was in maintenance mode and did not incur maintenance compute charges, although other cost views may show non-compute costs.
- The approved credit or final commercial resolution is not recorded in the Jira discussion.

## Remediation and follow-up

- A manual technical-user credential synchronization was completed for `Migration`; idle measurements resumed and auto-stop subsequently stopped `Migration` at its 120-minute threshold. **VENI01 was not repaired**.
- [SPOT-32540](https://exasol.atlassian.net/browse/SPOT-32540) tracks alerting when auto-stop cannot connect to a database.
- [SPOT-32614](https://exasol.atlassian.net/browse/SPOT-32614) tracks automatic reconciliation of SaaS technical users when credentials or permissions fail.
- The repair must update existing technical users in place and should also account for required post-migration schedules; user synchronization alone does not recreate missing schedules.

## Open points

1. Confirm whether backups, migration tests, or another workload ran against VENI01 during the 719.5-hour window.
2. Confirm whether the customer was ever told that VENI01 could be used or tested; current evidence suggests only `Migration` was handed over.
3. Confirm the final credit/refund decision and reconcile it with the billing evidence.
4. Remove or safely retire the remaining recovery databases and ensure future recovery workflows complete the post-migration configuration.

## Source note

This summary is based on the Jira description and comments for L3-4443, including the cluster-history, auto-stop log, credential-failure, billing, and remediation findings. The longer investigation record is in [[L3-4443 — VENI01 ran 24-7 (Aug 2026) — investigation (1)]].
