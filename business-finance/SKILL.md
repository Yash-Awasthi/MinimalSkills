---
name: business-finance
description: Use when handling money, books or ledgers: chart of accounts, journal entries, reconciliation, invoicing, payroll, ERP configuration in Odoo, market prices and trading logic, SaaS unit economics. Triggers: ledger, invoice, payroll, Odoo, P&L, margin.
---

# business-finance

## use when

- Odoo module, model, workflow or deploy -> references/odoo.md
- ledger, journal, reconciliation, statements -> references/accounting.md
- price, quote, market series, portfolio -> references/markets.md

not for: product pricing strategy (strategy-product), payment api code (backend-api)

## rules

- Conflict order: ledger integrity, then the reporting deadline, then convenience; a late close outranks a broken balance.
- Money is an integer in minor units with an explicit currency code; a float is a rounding error at close.
- Every journal entry balances to the cent; a one-sided write surfaces at close, not at write time.
- A posted entry is corrected by a reversal dated today, never edited; the trail is the audit evidence.
- Every rate, tax rule and FX conversion records its source, timestamp and jurisdiction; an undated figure cannot be reproduced.
- A forecast states its horizon, assumptions and range; a point estimate alone is not a forecast.
- No real customer or card data in a fixture, test or log; generate ids and amounts.

## change

1. Locate: the entry, its account pair, the open period and every report that reads the line.
2. Propose the posting or rule change in one sentence, with the treatment you rejected.
3. Predict before posting: debits, credits, the account balances and the affected statement line.
4. Back up the original entry and reconciliation state in context, pinned to `git rev-parse HEAD`.
5. Apply one concern per edit; a rate change and a tax rule change are two edits.
6. Verify: debits equal credits to the cent, then the reconciliation run on a copy.
7. Regress: the affected statement, the period close checklist and any fixture using the account.
8. Compare the balances against the prediction; an unexplained difference stops the posting.
9. Report entries, amounts and reconciliation status, then take the next item.

## journal

1. Identify the accounts and the direction: debit or credit, per line.
2. Sum debits and credits. They must match to the cent.
3. Attach the source document id and the date.
4. Post. A posted entry is immutable.
5. Reconcile against the bank or provider feed.
6. Explain every unreconciled line before closing the period.

```sql
select sum(debit_cents) as dr, sum(credit_cents) as cr
from journal_lines where entry_id = $1;
-- dr must equal cr
```

| event | debit | credit |
| --- | --- | --- |
| invoice issued | receivable | revenue |
| payment received | cash | receivable |
| bill received | expense | payable |
| payroll run | salary expense | payroll payable |
| depreciation | depreciation expense | accumulated depreciation |

## odoo

- `_name` for a new model, `_inherit` to extend, `_inherits` for composition.
- `Monetary` with an explicit `currency_id` field. Never a bare float.
- An access rule line in `ir.model.access.csv` per model, plus record rules for row scope.
- `sudo()` bypasses every rule: only with a written reason.
- Posted records immutable; corrections are reversals.
- A schema change needs a migration script in `migrations/<version>/`, or the upgrade fails on an existing database.

## lifecycle

```
draft    editable, no ledger impact
posted   journal entry written, immutable
paid     payment matched, receivable cleared
closed   period locked, only reversals allowed
```

- An invoice cannot skip posted. A payment on a draft is an unapplied cash item, not revenue.
- Matching is a join, not a guess:

```sql
select p.id, p.amount_cents from payments p
left join bank_lines b on b.id = p.bank_line_id
where b.id is null and p.created_at < now() - interval '2 days';
```

Unmatched after two days is a reconciliation item, not a rounding error.
Payroll journal lines and the month-end close checklist: references/accounting.md.

## numbers

| item | rule |
| --- | --- |
| amount | integer minor units, currency explicit |
| entry | debits equal credits, to the cent |
| posting | immutable after post, reverse to correct |
| fx | rate and its date on every converted amount |
| rounding | one stated rule, one rounding account |
| period | closed only after reconciliation |
| price series | adjusted or raw, labeled, with the source |

## decide

| condition | action |
| --- | --- |
| provider fee on a payment | separate fee line, not a net amount |
| backtest without costs | add spread, fee and slippage before trusting it |

## check

- [ ] debits equal credits for every entry
- [ ] currency explicit on every amount
- [ ] source document id present
- [ ] period open before posting
- [ ] reconciliation run and differences explained
- [ ] no pii in fixtures or logs

## stop

| condition | action |
| --- | --- |
| jurisdiction unknown | ask before applying a tax rule |
| instruction to edit a posted entry | refuse, reverse instead |
| ledger period closed | ask which period to post into |
| real financial data requested in a test | refuse, use a fixture |

## emit

- entries created with ids and amounts
- reconciliation status and any difference
- what is an estimate versus a posted number
