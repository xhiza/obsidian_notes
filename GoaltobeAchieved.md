---
title: Goals to Be Achieved
review: Midyear Review June–September 2026
source: HiBob manager review
date: 2026-09-18
tags:
  - performance
  - goals
  - 2026
---

# Goals to Be Achieved

## Current assessment

Overall achievement: **Fully meets expectations** (manager rating: 3.50).

The strongest areas are production deployment ownership, customer-update support, and company-wide CloudOps work. The main development theme is turning successful delivery into repeatable documentation, clearer success criteria, and proactive goal tracking.

## Achieved / on track

- **Co-own deployments and knowledge sharing:** Carried the largest share of `saas-terraform` production deployments in H1 and is a production approver. Created the Update Database Playbook, ran support enablement sessions, and published postmortems, including one on the day of the failed upgrade.
- **Company-wide CloudOps:** Delivered certificate and access work, IAM roles and queue access, quota cleanup, account removals, and resolved 32 SaaS tickets in a timely manner.
- **Customer success contribution:** Completed 22 of 25 weekly SLI reports with per-incident root cause analysis; initiated the customer-update pitch, playbook, Salesforce scheduled-update ticket, and customer database updates.
- **Technical delivery:** Delivered the c4 AWS SDK v2 migration in March and completed the Ubuntu 20 → 24 migration for production SaaS instances on 1 June.
- **Ways of working:** Strongest values demonstrated were Take Ownership, Live Customer Centricity, and Deliver Results. Customer updates were scheduled around customer needs, and a risky update was halted when a concern was raised.

## Goals needing focus

### 1. Redefine customer success for this role

The current customer-profiling goal assumes direct customer contact that this role does not have. Rework it after the VENI01 CoE so that customer success is measured through SLI data: identify recurring defects, build a profile from those patterns, and use it to influence defect prioritization and reduce recurring downtime.

### 2. Migration, recovery, and offboarding documentation

Complete the documentation covering migration, recovery, and offboarding paths. Use the SaaS-to-CD process work in `SPOT-32369` as the landing place and agree how the work gets onto the planning table.

### 3. c4 SDK v2 rollout

The migration was delivered, but rollout is still pending. Identify what is blocking it, then move through testing/staging and production without downtime.

### 4. Support readiness for update crashes

Continue improving the recovery experience. Alerts now carry instructions and support has received live training and recordings, but there is still no one-click recovery path.

### 5. Proactive goal ownership

Keep goals visible by reporting their status, escalating blockers, proposing measurable criteria, and flagging when planning capacity needs to be negotiated. The manager owns creating the space; I own keeping the goals in front of the manager.

## Follow-up actions

- [ ] Agree Goal 4 success criteria.
- [ ] Rewrite Goal 1 after the VENI01 CoE.
- [ ] Identify and remove the blocker for the c4 SDK v2 rollout.
- [ ] Add migration, recovery, and offboarding documentation to `SPOT-32369`.
- [ ] Define the desired one-click recovery experience for update crashes.
- [ ] Reserve planning capacity for documentation work.
- [ ] Review and reconcile the self-review goal grid with the tracked goals.
- [ ] Track the unplanned Datadog-agent automation work separately from planned goals.

## Context / lessons

- The two Corrections of Error indicate process and documentation improvements, not individual fault; confirmation was requested before the deletion action.
- The POC-coordination goal had no meaningful H1 activity because no customer migration or POC occurred and the open Adidas POC was paused.
- Customer-update communication improved through the Customer Updates pitch.
- Migration documentation did not progress as planned; time-logging was not assessed in this cycle.

## Next review check-in

Bring an updated status for each action, especially the rewritten customer-success criteria, `SPOT-32369` documentation, and the c4 rollout blocker.
