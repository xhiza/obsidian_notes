---
id: aws-devops-agent
aliases:
  - AWS DevOps Agent
  - DevOps Agent Evaluation
tags:
  - evaluation
  - aws
  - devops
  - tooling
status: draft / under refinement
owner: Edis Shabi
last-updated: 2026-06-08
---

# AWS DevOps Agent — Evaluation

## 1. Purpose

Evaluate whether the [AWS DevOps Agent](https://aws.amazon.com/devops-agent/) fits as the **first-line responder** when customers of our SaaS report issues — i.e. an automated layer that:

1. Collects context (logs, metrics, recent deploys, dependency state) before a human is paged.
2. Performs initial root-cause hypotheses and runbook-style remediation suggestions.
3. Interacts with the on-call engineer in Slack to share findings and accept follow-up commands.
4. Escalates cleanly to L2/L3 when it cannot resolve.

Goal of this document: produce a **go / no-go decision** with a documented scorecard, a PoC plan, and a list of open questions — not a feature description.

## 2. Product Snapshot (as of 2026-06-08)

- **Status:** Generally Available.
- **Model:** Autonomous agent for incident triage, RCA, proactive recommendations, and on-demand SRE Q&A across AWS, multicloud, and on-prem.
- **Regions launched:** us-east-1, us-west-2, eu-central-1 (Frankfurt), eu-west-1 (Ireland), ap-southeast-2 (Sydney), ap-northeast-1 (Tokyo).
- **Pricing model:** Pay-per-second for agent task time. AWS Support customers receive monthly credits as a percentage of their Support spend. No upfront commitment.
- **Native integrations:** CloudWatch, Datadog, Dynatrace, New Relic, Splunk, Grafana, PagerDuty, ServiceNow, GitHub, GitLab, Azure DevOps, Slack.
- **Extensibility:** Private/remote MCP servers for proprietary tools; built-in Grafana MCP; updated AWS CLI / SDK / MCP server support.
- **Identity:** Direct IdP integration with Okta and Microsoft Entra ID; customer-managed keys supported.

> Treat this snapshot as volatile — verify against the [user guide](https://docs.aws.amazon.com/devopsagent/latest/userguide/) and [GA blog post](https://aws.amazon.com/blogs/mt/announcing-general-availability-of-aws-devops-agent/) before the decision meeting.

## 3. Evaluation Criteria

Each criterion is scored **0 (blocker) / 1 (gap) / 2 (acceptable) / 3 (strong fit)** and weighted. Fill in the **Evidence** column during the PoC.

### 3.1 Functional fit — "first wall"

- [ ] Can the agent ingest an alert (CloudWatch / Datadog / PagerDuty) and produce a triage summary autonomously?
- [ ] Does it pull from logs? — covered in detail in [§3.2 Log collection](#32-log-collection--cloudwatch-and-on-node).
- [ ] Does it correlate across **metrics + logs + recent deploys + infra state**, or only one source?
- [ ] Can it follow a runbook (e.g. "if disk > 90% on node X, suggest cleanup commands")? Custom runbooks supported?
- [ ] Does it surface its reasoning chain (auditable) or only the conclusion?
- [ ] How does it handle a customer-database-specific incident (Exasol DB on EC2) vs. a generic AWS infra incident?

### 3.2 Log collection — CloudWatch and on-node

For our SaaS, "first wall" triage is only useful if the agent can reach **both** sides of the log surface:

- **CloudWatch Logs** — agent / application / system logs shipped to log groups. Access pattern: CloudWatch Logs Insights queries, `GetLogEvents`, `FilterLogEvents`.
- **On-node logs** — files that live on the EC2 instance and are **not** shipped to CloudWatch: Exasol DB logs, `/var/log/messages`, `journalctl`, cloud-init output, package-manager state, in-flight core dumps. Typical access path: SSM Session Manager / SSM Run Command (no inbound SSH), or a sidecar log-collection agent.

Score this strictly — if the agent can only see CloudWatch, it covers a fraction of what L3 actually needs.

**CloudWatch side:**

- [ ] Can it run CloudWatch Logs Insights queries on its own (pick log group, time window, query string), or only summarize logs already attached to an alert?
- [ ] Can it follow log-group references across linked accounts (cross-account log subscription / OAM)?
- [ ] How does it handle large result sets — pagination, truncation, sampling? Does it lose signal on a 50 MB log dump?
- [ ] Does it respect log-group resource policies and KMS-encrypted log groups?
- [ ] Cost awareness — does the agent run Insights queries expensively (full-scan repeatedly), or does it cache / scope?

**On-node side:**

- [ ] Can it invoke **SSM Run Command** / **SSM Session Manager** to fetch logs from the instance, or does it strictly require logs to be in CloudWatch first?
- [ ] If yes — what IAM permissions does it require on the instance role and on the agent's role? (`ssm:SendCommand`, `ssm:GetCommandInvocation`, target tagging.)
- [ ] Can we **whitelist** the commands it is allowed to run on-node (e.g. only `cat`, `tail`, `grep` against an allow-listed path set, no arbitrary shell)?
- [ ] Does it work with nodes that have **no public IP** and use SSM VPC endpoints only?
- [ ] Does it support **Exasol-specific** log paths out of the box (no — assume it doesn't), and can we feed it a runbook / MCP server that knows where to look?
- [ ] What does it do when SSM Agent is **stuck or down** on the instance (which is often the very symptom of the incident)? Fallback path?
- [ ] Audit — is every on-node fetch recorded in CloudTrail and SSM session logs, mappable to the requesting engineer's identity?

**Out-of-band path (when both CloudWatch ingestion and SSM are degraded):**

- [ ] Does the agent have a hook to pull from an **out-of-band log archive** (S3 bucket of rotated logs, our existing collection script — see "Script to collect Data from instances" in [[Backlog]])?
- [ ] Can we point it at our internal log stack endpoint via MCP and have it query there instead?

### 3.3 Slack interaction model

This is the **primary UX** for our use case — score strictly.

- [ ] Does the bot post into a channel **per incident** or a single global channel? Per-customer routing?
- [ ] Can on-call **reply to the bot** with follow-up questions in-thread (interactive), or is it one-shot summary only?
- [ ] Can on-call **trigger actions from Slack** (e.g. "run cleanup", "fetch last 30m of logs", "open Jira ticket")?
- [ ] Slash commands vs. mentions vs. buttons — what is the actual interaction surface?
- [ ] Auth: does the Slack action carry the engineer's identity (IdP-mapped) or run as a service principal? Important for audit.
- [ ] Rate limits / message size — does it truncate long log dumps?

### 3.4 Multi-account / multi-tenant fit

We operate **one AWS account per customer** (or close to it). This criterion is the highest risk for us.

- [ ] How is access scoped across many accounts? One agent per account, or one agent with cross-account roles?
- [ ] Does it support **tenant isolation** so customer-A data never enters a customer-B-scoped chat?
- [ ] Onboarding cost per new account — is it a CloudFormation/Terraform module or per-account UI clicks?
- [ ] Can we drive enrollment from our existing AWS account-management automation?
- [ ] Does it discover resources in accounts it was not explicitly granted, or strictly opt-in?

### 3.5 Observability stack alignment

- [ ] We are mid-migration **Datadog → internal stack** (see [[Backlog]]). Which side does the agent integrate with cleanly?
- [ ] If we keep Datadog short-term, does the agent's Datadog connector cost extra (Datadog seat per agent)?
- [ ] Will the internal stack be reachable via MCP, or do we need to expose endpoints publicly?

### 3.6 Security & compliance

- [ ] Where is data processed (region, AWS-managed vs. shared)? Does it leave the customer's region of residence?
- [ ] What is logged about the agent's actions (CloudTrail coverage)?
- [ ] Customer-managed KMS keys — confirm end-to-end, not just at-rest in one place.
- [ ] Slack content handling — does the agent retain message history? For how long? Where?
- [ ] IdP integration with our identity provider — verify mapping of roles, MFA enforcement.
- [ ] Pen-test / SOC 2 / ISO 27001 statements for the service (compare to [[Backlog]] security work).
- [ ] Data subject considerations (GDPR) — customer data in EU accounts must not flow to us-east-1 endpoints.

### 3.7 Pricing & cost predictability

- [ ] Estimate cost for **1 incident** of typical complexity (e.g. 30-minute triage). Capture in PoC.
- [ ] Per-second model — what is the **idle** cost? Is there a charge for the agent sitting in Slack?
- [ ] How much of our AWS Support spend converts into credits, and what is the realistic monthly burn after credits?
- [ ] Compare to alternative: in-house Bedrock-Agent + Lambda runbooks, or third-party (Rootly AI, Resolve.ai, Cleric, Parity).

### 3.8 Operational fit (L2/L3 escalation)

- [ ] Does it create a clean handoff artifact (Jira / Confluence / Slack canvas) when escalating?
- [ ] Can it open a Jira ticket in our project with structured fields?
- [ ] Does it respect our **change windows** (e.g. no remediation actions during a customer's maintenance freeze)?
- [ ] Failure mode: what happens when the agent itself is unavailable? Does paging fall back to humans?

## 4. Scorecard

| #  | Criterion | Weight | Score (0–3) | Weighted | Evidence / Link |
|----|-----------|:------:|:-----------:|:--------:|-----------------|
|  1 | Functional fit (triage quality) | 5 |   |   |   |
|  2 | Log collection — CloudWatch coverage | 4 |   |   |   |
|  3 | Log collection — on-node (SSM) coverage | 4 |   |   |   |
|  4 | Slack interaction (interactivity, auth) | 5 |   |   |   |
|  5 | Multi-account / tenant isolation | 5 |   |   |   |
|  6 | Observability stack alignment | 3 |   |   |   |
|  7 | Security & compliance | 5 |   |   |   |
|  8 | Pricing predictability | 3 |   |   |   |
|  9 | Operational handoff / escalation | 4 |   |   |   |
| 10 | Onboarding effort (per-account) | 3 |   |   |   |
| 11 | Extensibility (MCP, custom runbooks) | 2 |   |   |   |
|    | **Total**                              | **43** |   |   |   |

**Decision thresholds:**
- ≥ 98 / 129 weighted → adopt for production, broad rollout.
- 74–97 → adopt for a limited cohort, re-evaluate after 90 days.
- < 74 → do not adopt; document gaps, consider alternatives.

## 5. PoC Plan

**Time-box:** 3 weeks. **Scope:** 1 internal sandbox account + 1 volunteer customer account (with explicit written consent — coordinate with Customer Success).

### Test scenarios

1. **Synthetic disk-pressure alert** on a customer DB EC2 — agent should pull metrics, identify the volume, and post a triaged summary to Slack with proposed cleanup commands.
   - Verify it queries CloudWatch Logs Insights for `/var/log/messages` shipped log group, **and** uses SSM Run Command to fetch on-node `df -h`, `du -sh /var/log/*`, and the latest Exasol DB log file that is not shipped to CloudWatch.
   - Capture which IAM permissions it actually called (CloudTrail).
2. **Real low-severity ticket** from a sandbox customer — agent runs in shadow mode, on-call compares its summary to their own triage.
3. **Cross-account RCA** — failure that spans the management node and the customer DB node (see [[Backlog]] DR scope).
4. **Slack interactivity** — on-call asks 3 follow-ups in-thread; measure relevance and latency.
5. **Escalation path** — agent gives up; verify Jira ticket created with the right project / labels / linked logs.
6. **Cost capture** — record per-second usage and translate to a per-incident cost for each scenario.
7. **Degraded-node log fetch** — kill the SSM Agent on a sandbox node and trigger an alert; verify the agent (a) detects SSM unreachable, (b) falls back to CloudWatch-only, and (c) clearly states that on-node evidence is missing rather than hallucinating it.

### Success metrics

- MTTA on the synthetic alert reduced by ≥ 30% vs. baseline.
- ≥ 70% of agent summaries rated "useful" by the on-call (post-scenario survey).
- Zero cross-tenant data leakage observations.
- Total PoC cost (after credits) below an agreed cap — define cap with Finance before start.

## 6. Open Questions

- [ ] Exact pricing per-second rate and how AWS Support credits are calculated for our Business / Enterprise tier.
- [ ] Slack actions — full list (post, react, thread, buttons, slash commands, modal forms).
- [ ] MCP server hosting model — can we run an MCP server inside our VPC for the internal log stack?
- [ ] Data residency for EU customer accounts — strictly eu-central-1 / eu-west-1, or routed via us-east-1?
- [ ] Behavior under degraded mode — does the agent refuse to act if it loses access to one source, or does it answer anyway?
- [ ] Quotas — concurrent investigations per account, max session length.
- [ ] Audit log format — CloudTrail event names, exportability to our SIEM.
- [ ] How does the agent interact with **infrastructure pen tests** in progress (SPOT-16938 in [[Backlog]]) — does it scan, and could it be flagged?
- [ ] Exact mechanism for on-node log access — SSM Run Command, SSM Session Manager, or a separate AWS-managed agent on the instance?
- [ ] Can on-node commands be **constrained to an allow-list** (commands, paths) via SSM document or guardrail?
- [ ] CloudWatch Logs Insights — does the agent generate queries itself, and is there a way to **cap query scan bytes** to prevent cost runaways?
- [ ] Cross-account log access — does it use OAM (Observability Access Manager) sinks, or one role per account?

## 7. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|:---------:|:------:|------------|
| Cross-tenant data leak via shared agent context | Low | Critical | Per-account agent isolation; verify in PoC scenario 2 and 3 |
| Cost runaway if agent loops on a noisy alert | Med | Med | Per-account budget alarm; concurrency cap; PoC scenario 6 |
| Vendor lock to AWS chat-ops surface | Med | Med | Keep runbook content version-controlled, portable to Bedrock Agents if needed |
| Agent action without human approval breaks customer DB | Low | Critical | Disable remediation actions in PoC; advisory-only mode until ≥ 90 days clean run |
| Agent runs unbounded CloudWatch Insights queries, burns cost | Med | Med | Per-account scan-byte budget; verify in PoC scenario 6 |
| On-node command executed by agent leaks sensitive file contents into Slack | Low | High | SSM allow-list of commands and paths; redaction pass before posting; PoC scenario 1 verifies |
| Slack content retention conflicts with customer NDAs | Med | High | Confirm retention policy; route customer-sensitive content to a redacted channel |

## 8. Decision Gate — Must / Should / Nice

**Must-haves (any failure ⇒ no-go):**
- Per-account / per-tenant isolation, verified.
- Interactive Slack threads (not one-shot summaries).
- **CloudWatch Logs access** — agent can query log groups in the customer account, with KMS support.
- **On-node log access** — agent can fetch instance-local logs via SSM (with command/path allow-list), or we have a clear out-of-band path (S3 archive + MCP) that works for nodes with no log shipping.
- Data residency honored for EU customers.
- CloudTrail-grade audit of all agent actions, including every on-node command.
- Predictable cost (credits + ceiling).

**Should-haves:**
- Native integration with the **internal log stack** (or MCP-friendly endpoint).
- Jira ticket creation with our project structure.
- Custom runbook support.

**Nice-to-haves:**
- Proactive recommendations (cost, resilience).
- Dynatrace / New Relic native — we use Datadog today.

## 9. Next Steps

- [ ] Confirm AWS Support tier + credit math with AWS TAM.
- [ ] Select PoC customer account (CS approval).
- [ ] Spin up agent in sandbox account, wire Slack, run scenario 1.
- [ ] Schedule decision review at end of week 3.

## 10. References

- Product page — https://aws.amazon.com/devops-agent/
- User guide — https://docs.aws.amazon.com/devopsagent/latest/userguide/
- GA announcement — https://aws.amazon.com/blogs/mt/announcing-general-availability-of-aws-devops-agent/
- Demo — https://aws.storylane.io/share/fstgtzmjif96
- Related internal: [[Backlog]], [[L3-3351]]
