# prd

Load for a PRD, a one-pager, prioritization or a launch plan.

## one-pager

```
problem:   who cannot do what, and what it costs them today
evidence:  n interviews, n tickets, one metric with period
bet:       the smallest change that could move it
metric:    one primary, one guardrail
not doing: what is explicitly out of scope
review:    date and owner
```

Keep it to one page; past that, the problem statement is carrying solution detail that belongs in the spec.

## prd

| section | content | failure |
| --- | --- | --- |
| context | the problem and the evidence | a solution with no problem |
| users | who, how many, which segment | "everyone" |
| scope | in, out, later | no explicit out |
| behavior | states, edge cases, errors | happy path only |
| metrics | primary, guardrail, instrumentation | no event defined |
| risks | what could make it fail | optimism |
| rollout | flag, cohort, rollback | big bang |

Acceptance criteria are testable statements: "a user with two invoices sees both within 2s".

## rice

```
score = (reach * impact * confidence) / effort
reach        users per quarter
impact       3 massive, 2 high, 1 medium, 0.5 low, 0.25 minimal
confidence   1.0 high, 0.8 medium, 0.5 low
effort       person-weeks
```

Score orders the list; it does not decide. Write the reason for every override, or the next reader re-litigates it.

## okr

- Objective: qualitative, one sentence, no numbers.
- Key result: a number with a baseline and a date. "p95 latency from 900ms to 300ms by 30 June".
- Three key results maximum. A fourth dilutes attention.
- A key result states the number that would make it fail; without that threshold it is a task with a percentage.

## launch

| gate | check |
| --- | --- |
| support | docs and a runbook exist |
| billing | the price is in the system, proration tested |
| analytics | the event fires in staging |
| rollback | a flag, and someone who can flip it |
| comms | one owner, one date, one message |

## pricing

- Model churn and revenue at three elasticities. Label them as assumptions.
- Anchor on the value the job delivers (hours saved times loaded rate); cost sets the floor, and a price at cost leaves the value with the customer.
- Test on new cohorts before migrating existing customers.
- A price change needs a grandfathering rule and a notice period.

## stakeholder update

```
decided:    what and why, one paragraph
numbers:    metric, value, delta, period
risks:      what could change the plan
ask:        the one decision you need
```

## rice scales

RICE = (reach x impact x confidence) / effort

| factor | scale |
| --- | --- |
| reach | users per quarter, counted |
| impact | 3 massive, 2 high, 1 medium, 0.5 low |
| confidence | 100% data, 80% strong signal, 50% a guess |
| effort | person-weeks, not story points |

## pricing model

- Model revenue at churn of 5, 10 and 20% before recommending a price.
- Elasticity: a 10% raise at -0.5 keeps revenue, at -1 it is flat only if churn holds.
- Segment first. One price for self-serve and enterprise leaves money on both sides.
- Grandfather existing customers for one renewal cycle, or state the churn you accept.
- A price change ships with the migration note for existing accounts.

## okr set

```text
Objective: make reconciliation self-serve
KR1  scheduled export adopted by 40% of active admins by 2026-03-31 (baseline 0%)
KR2  median reconciliation time 6h -> 2h by 2026-03-31 (event log, not a survey)
KR3  export-related tickets under 10 per month (baseline 34, 90-day average)
```

- Three KRs maximum. Each carries a baseline, a target and a date.
- A KR without a baseline is a wish. A KR phrased as a task ("ship the export") is a project, not a result.
- A guardrail sits beside the objective: support tickets must not rise more than 10% during the rollout.

## launch gates

| gate | evidence | owner |
| --- | --- | --- |
| flag | on for 5% internal, 24h with no error spike | eng |
| docs | README section and changelog entry merged | docs |
| support | macro plus two canned replies | support |
| rollback | flag off proven in staging | eng |
| metric | dashboard shows adoption and error rate | pm |

All five green is a launch. Three of five is a beta, and is labeled one in the announcement.

## stakeholder update

```text
Decision needed: approve the export flag rollout to 25% on 2026-12-08
Why now: 40% adoption at 5%, error rate flat at 0.2%
Cost: 2 engineer-weeks, no new infra
Risk: csv encoding on legacy exports, mitigation in the doc
Ask: yes or no by 2026-12-05
```

- One decision per update, in the first line. An update with three asks gets none.
- Every number carries its period and its base: "adoption up 4pp in 6 weeks across 120 accounts" is a number; "adoption is up" is not.
- The risk line names the mitigation, not the worry.
## org index

| topic | the rule that matters |
| --- | --- |
| Executive and organizational | Exec update is one decision, one number, one date; a status deck with no ask is a newsletter. |
| Governance | Who decides, with what threshold, in what forum; a decision with no owner is re-litigated monthly. |
| Workflows | Intake, review, decision, record; a request that skips intake has no priority and no owner. |
| Consulting | Scope, deliverable, fee, out-of-scope list; an engagement without the last line expands until it is unprofitable. |
| Advisory personas | A persona is a review lens, not evidence; label the opinion and keep the facts separate. |
