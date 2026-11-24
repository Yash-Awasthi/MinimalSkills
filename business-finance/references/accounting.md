# accounting

Load for ledgers, statements, reconciliation and close.

## double entry

| event | debit | credit |
| --- | --- | --- |
| invoice issued | accounts receivable | revenue |
| payment received | cash | accounts receivable |
| bill received | expense | accounts payable |
| bill paid | accounts payable | cash |
| payroll run | salary expense | payroll payable |
| depreciation | depreciation expense | accumulated depreciation |

Every event touches at least two accounts. A single-sided entry hides an error until the statements do not tie.

## statements

| statement | answers | period |
| --- | --- | --- |
| P&L | did we make money | a period |
| balance sheet | what do we own and owe | a point in time |
| cash flow | where did cash move | a period |

The balance sheet balances by construction. If it does not, the ledger has a one-sided entry.

## reconciliation

1. Pull the bank or provider feed for the period.
2. Match on amount, date window and reference.
3. Auto-match exact, then fuzzy on amount within a date window.
4. List unmatched on both sides.
5. Explain each: timing, fee, duplicate, error.
6. Post adjustments, then re-run until both sides are empty.

A difference above 0.01 in the functional currency is unexplained until a document accounts for it; name the document, not the cent.

## close checklist

- [ ] all bank accounts reconciled
- [ ] accruals posted for known costs
- [ ] prepaid expenses amortized
- [ ] revenue recognized per the policy
- [ ] intercompany entries matched
- [ ] fx revaluation at the closing rate
- [ ] trial balance reviewed
- [ ] period locked

## controls

| control | test |
| --- | --- |
| segregation of duties | the person who creates a payment cannot approve it |
| approval threshold | a payment above the limit needs a second actor |
| sequence gaps | invoice numbers have no holes |
| immutable posted entries | an update attempt fails |
| audit trail | every change has an actor and a timestamp |

## review

- Every report query filters by period and entity.
- No `select *` into a report; columns are explicit.
- Rounding rule stated once, applied everywhere.

## payroll run

| line | debit | credit |
| --- | --- | --- |
| gross wages | salary expense | payroll payable |
| employer tax | payroll tax expense | tax payable |
| withholding | payroll payable | tax payable |
| net pay | payroll payable | cash |

Check: gross minus withholding minus employer tax equals the cash out, to the cent. A run where net pay does not equal gross minus deductions is a mapping error, not a rounding error.

## month-end close

1 Bank feed reconciled, zero unexplained lines.
2 AR and AP aged, everything over 90 days carries a reason.
3 Accruals posted: utilities, payroll in transit, unbilled revenue.
4 FX revaluation at the closing rate, difference to the fx account.
5 Inventory and COGS tie to the physical count.
6 Trial balance: debits equal credits, to the cent.
7 Period locked, report snapshot stored with its timestamp.

The close is done at step 6 with step 7 recorded. A close with an open reconciliation is a draft, and is labeled one.
