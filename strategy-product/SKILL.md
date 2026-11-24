---
name: strategy-product
description: Use when deciding what to build or how to position it: problem framing, opportunity sizing, prioritization, roadmaps, launch plans, pricing, competitive analysis, OKRs, stakeholder updates. Triggers: roadmap, prioritization, launch, pricing, OKR.
---

# strategy-product

## use when

- frame a problem, size an opportunity
- prioritize a backlog, cut scope
- write a roadmap, one-pager or PRD -> references/prd.md
- plan a launch, a pricing change
- set OKRs, write the stakeholder update

not for: execution detail (engineering-craft), financial statements (business-finance)

## rules

- Conflict order: evidence, then reversibility, then speed; a bet without a kill condition is a wish.
- The first line names the user, the job they cannot do, and what they do instead today.
- Every number carries a source, a period and a method; a guess carries its range.
- One primary metric per initiative, one guardrail metric, and the threshold that stops the rollout: no threshold, no launch.
- A roadmap row is a bet with a confidence, kill condition and review date, not a delivery promise.
- The not-building list ships with the roadmap; a cut nobody wrote down is re-proposed next quarter.
- A quote is verbatim with source and date; a metric is measured, never rounded up.

## change

1. Locate: the metric or bet, its baseline, and every doc that quotes the number.
2. Propose the scope or priority change in one sentence, with the option you rejected.
3. Predict before writing: reach, cost, the guardrail it moves, who objects.
4. Back up the original number and its source in context, pinned to the period it covers.
5. Apply one concern per edit; a metric change and a scope cut are two decisions.
6. Verify: recompute the number from its source and period, not from the previous doc.
7. Regress: every roadmap row, OKR and launch gate quoting the metric.
8. Compare against the prediction; an unexplained number stops the decision.
9. Report the decision, evidence with n and period, and the review date, then continue.

## frame

```text
problem:  finance admins cannot reconcile 400 invoices a month because the export is csv-only
evidence: 34 tickets, 6 interviews, 2.1% of sessions hit the export page
bet:      scheduled export -> reconciliation time 6h to 2h per month
kill if:  under 10% of admins enable it within 30 days
```

- The kill condition is observable and dated, or the bet is a wish.

## prioritize

RICE = (reach x impact x confidence) / effort

| item | reach | impact | conf | effort | score |
| --- | --- | --- | --- | --- | --- |
| scheduled export | 1200 | 2 | 0.8 | 2 | 960 |
| bulk edit | 800 | 1 | 0.8 | 3 | 213 |
| sso | 300 | 3 | 0.5 | 6 | 75 |

Reach is users per quarter, impact 3/2/1/0.5, effort in person-weeks. The SSO row scores last
and is still the right call if an enterprise deal depends on it: write the override and why.
OKR set with baselines and launch gates: references/prd.md.

## pricing

- Model revenue at churn of 5, 10 and 20% before recommending a price.
- A 10% raise at -0.5 elasticity keeps revenue; at -1 it is flat only if churn holds.

## decide

| condition | action |
| --- | --- |
| no evidence | run the smallest test first |
| two metrics conflict | name the primary, the other is a guardrail |
| scope grows in review | cut a feature, do not move the date silently |

## check

- [ ] problem statement names who and the current workaround
- [ ] evidence with n and period
- [ ] one primary metric and one guardrail
- [ ] what is explicitly not being built
- [ ] owner and review date

## stop

| condition | action |
| --- | --- |
| no user evidence and no data | say so, propose the test |
| request to invent a metric or quote | refuse |
| decision already made | state the risk once, then execute |

## emit

- the decision, one line
- evidence with n and period
- the bet, the kill condition and the review date
