---
name: business-finance-ops
description: "One merged skill for SMB accounting, financial analysis, SaaS metrics, pricing, procurement, contracts, market data, growth and legal risk. Route ask -> pick register/tool -> gather evidence -> reconcile -> decide. Terse, no filler."
license: MIT
---

# Business Finance Operations

> Merged from business-finance catalog. No external refs. Tooling in `scripts/`; assets in `assets/`.

## Routing

- Ask vague finance -> pick module: accounting, cash flow, analysis, SaaS, pricing, procurement, contract, market data, growth.
- Accounting ask -> register + reconciliation workflow.
- Analysis ask -> DCF, ratios, forecast, variance, market sizing.
- SaaS ask -> metrics, pricing, MVP, multi-tenant, scaffolder.
- Vendor/contract ask -> TCO, review, redline, triage.
- Market/stock ask -> data source -> verify -> value.
- Growth ask -> startup analysis, market sizing, M&A, expansion.
- Legal ask -> contract/NDA/tender/legal risk -> escalate.

## Hard rules

- Missing data -> abstain. Never invent.
- Evidence -> cite page/source. Mark assumptions.
- Separate fact, assumption, recommendation.
- Deal / contract -> no auto-approval. Route to approver.
- Financial advice -> decision support, not legal/tax advice.

## Accounting registers

Extract from inbox, PDF, photo, CSV, ledger. Normalize fields. Code to ledger account/job. Reconcile. Report variance.

- Audit / accounting system -> select software via scored fields -> route modules -> close monthly.
- Day book -> opening/closing balance per book; in/out; debit/credit; reconciliation status.
- Expense accounting -> expense no/date, payee PAN/VAT, bill ref, doc type, amount+VAT, ledger account, approver, status.
- Expense management -> claim id, employee/dept, amount/tax, approver level, category, cost centre, budget line, receipt, status.
- Invoice / billing -> invoice no, client, project, issue/due dates, subtotal, discount, tax/withholding, total, payments, balance, aging.
- Purchase -> supplier, invoice, gross, VAT/TDS, net payable, ledger account, payment balance.
- Receipt -> payer, mode, gross received, invoice allocation, unapplied, TDS collected.
- Payment -> voucher no/date, paid to/purpose, mode, gross, TDS rate/deducted, net paid, invoice allocation, ledger, reconciliation.
- Payroll -> employee/dept/month, basic/DA/HRA/TA, bonus, deductions, net pay, period, payment date/method.
- Salary -> gross, allowances, TDS/provident fund deductions, net pay, statutory reconciliation.
- Petty cash -> entry no/date/type, payee/purpose, cash in/out, running balance, limit flag, custodian, physical count/variance.
- Budget cash flow -> budget vs actual by dept/category/period; variance, % used, linked expenses.
- Tax register -> sales/purchase tax, withholding deducted/received, net payable, filing due date, days remaining.
- Attendance -> check-in/out, hours, work mode, late minutes, leave/regularisation flags.
- Contract renewal -> counterparty, owner, start/end, auto-renewal, notice deadline, value/tax basis.
- Inventory reconciliation -> count date, item, warehouse, book vs physical qty, variance qty/value, reason, damage/expiry, adjustment/approval.
- Asset IT -> serial, model, condition, assignee, location, purchase value, warranty expiry, return date.
- Company email accounts -> employee, type, aliases, groups, tool, licence cost, 2FA/password state, access-review dates.
- SOP company wiki -> title, category, dept, owner, version, priority, review dates.
- Events -> type/date/time, venue, organiser, audience, budget vs actual, RSVP/attendance, feedback score.

## Month-end close chain

1. `month-end-prep`: reconcile ledger (MYOB, NetSuite, QuickBooks, Xero, Zoho Books) vs PayPal, Shopify, Square, Stripe.
2. Flag transactions: suspicious duplicates, missing receipts, attention items.
3. Write plain-English P&L narrative.
4. `cash-flow-snapshot`: 30/60/90-day forecast; percentage-variance confidence.
5. `financial-statements`: income statement, balance sheet, cash flow; period-over-period variance.
6. `variance-analysis`: decompose drivers, narrative, waterfall.
7. `tax-prep`: confirm closed books -> quarterly estimated payment or year-end 1099-NEC + accountant packet.

## Financial analysis

- DCF -> revenue/cost/cash flow -> scenario -> discount -> valuation.
- Ratios -> gross/net margin, burn, runway, ARR, MRR, churn, LTV, CAC, NRR, quick ratio.
- Forecast -> rolling forecast, accuracy tracker, pipeline coverage, magic number, CAC payback.
- Market sizing -> TAM/SAM/SOM; assumptions; ranges.
- Stock/company analysis -> public data -> ratios -> score -> valuation; verify data.
- Investment -> ROI, IRR, NPV, payback, build vs buy, lease vs buy.
- Portfolio/risk -> R-multiple, position limits, hedging, expectancy, stop-loss.
- Quant -> backtest, risk metrics, portfolio optimisation, statistical arbitrage.

## SaaS

- Metrics coach -> ARR/MRR/churn/LTV/CAC/NRR/quick ratio/unit economics.
- Pricing -> seat/usage/value/freemium/hybrid; Van Westendorp WTP; Good/Better/Best; model revenue across tiers; return range not single number.
- Usage-based -> API/metered billing; cost calculator; pricing transparency; developer acceptance.
- MVP -> idea validation, stack, auth, payments, launch checklist.
- Scaffolder -> Next.js App Router, TypeScript, Tailwind, shadcn/ui, Drizzle, Stripe billing, dashboard.
- Multi-tenant -> row-level security, tenant-scoped queries, shared schema, safe admin patterns.

## Procurement / vendor / contract

- Procurement -> SaaS audit, category spend, slow purchasing cycles, supplier consolidation.
- Channel economics -> cost to serve, channel ROI, channel mix under constraints.
- Vendor review -> cost, risk, recommendation, TCO, negotiation points.
- Vendor check -> CLM/CRM/email/doc storage; gaps; upcoming deadlines.
- Contract review -> clause-by-clause vs negotiation playbook; redlines; business impact.
- Contract/proposal writer -> freelance contract, proposal, SOW, NDA, MSA; US/EU/UK/DACH; Markdown -> docx; not legal advice.
- Deal desk -> score deal; approver router; term redliner; never auto-approve.
- Commercial policy -> discount matrix, approver thresholds, exception flows, policy linter.
- NDA triage -> GREEN/YELLOW/RED; embedded non-solicit/non-compete checks.
- RFP responder -> parse mandatory vs weighted; proof-point answers; win chance.
- Signature request -> pre-signature checklist, signing order, send.
- No free work -> classify scope; draft reply + priced change order.

## Legal

- Legal research -> organised facts, official sources, professional review.
- Legal risk -> severity x likelihood; escalation criteria.
- Legal response -> templates + escalation checks.
- Employment contract templates -> jurisdiction-specific review.
- Tenders -> open AU/NZ tenders; fit + gap analysis.
- Property/auction -> valuation scenarios; market/method limits.
- Stock/company legal exposure -> review before signing.

## Market / data integrations

- Alpha Vantage -> equities/options/forex/crypto/commodities/indicators.
- FXMacroData -> macro indicators, policy rates, FX, CFTC, 22 currencies.
- Equibles -> SEC filings, XBRL, earnings transcripts, 13F, prices.
- Longbridge -> quotes, charts, fundamentals, market data, derivatives, research, quant.
- TraderSpy -> market briefing, signals, trading ledger.
- Financial data collector -> yfinance -> structured JSON -> DCF/comps.
- US property data -> valuation, listings, price/tax history, schools.
- PlaceCall -> outbound calls; book/ask/quotes/outcome.
- Options flow -> put/call ratios with premium/delta/expiry assumptions.

## Growth / strategy

- Startup analyst -> market sizing, financial modelling, competitive analysis, strategy.
- Business case -> market, solution, financials, strategy.
- Financial projections -> 3-5 year revenue/cost/cash flow/scenarios.
- Market opportunity -> TAM/SAM/SOM.
- Metrics framework -> seed through Series A.
- Micro-SaaS / Notion templates -> idea validation, MVP, pricing, launch, sustainable revenue.
- M&A / market entry / international expansion -> diligence, valuation, terms, integration, localisation, regulation, GTM.
- Founder / delegation / capacity -> bottlenecks, energy/calendar audits, succession.
- Name fit / brand -> pronunciation, bad meanings, trust per market.
- Internal narrative -> one company story; flag contradictions.
- Process doc -> flowcharts, RACI, SOPs, exceptions.
- Company OS -> EOS/Scaling Up/OKRs, accountability chart, scorecard, meeting rhythm, quarterly rocks.

## Productivity / operations

- Deep work -> time-block calendar/tasks; cut shallow work; focus hours; session/streak log; shutdown ritual.
- Close calendar -> task sequencing, dependencies, status, blockers.
- Monday brief / business pulse -> cash, sales, pipeline, commitments, urgent work.
- Restock -> sales velocity, stockout date, reorder size, purchase order, vendor email, stage entries.
- Payroll plan -> cash forecast, overdue invoice reminders, timesheets, anomalies, staged run.
- Invoice chase -> overdue reminders matched to payment history and tone.
- AP processor / pay the bills -> read/code bills -> cash check -> staged payment run.
- Process doc -> SOP, RACI, exceptions.

## Tooling

Run `python3 scripts/<name>.py`. Core scripts:
- accounting/budget: `budget_variance_analyzer.py`, `forecast_builder.py`, `ratio_calculator.py`, `dcf_valuation.py`.
- churn/CS: `churn_impact_calculator.py`, `churn_risk_analyzer.py`, `health_score_calculator.py`, `expansion_opportunity_scorer.py`.
- pricing: `pricing_modeler.py`, `pricing_model_picker.py`, `wtp_analyzer.py`, `packaging_designer.py`.
- procurement/channel: `spend_categorizer.py`, `supplier_consolidation.py`, `purchasing_cycle_analyzer.py`, `cost_to_serve_calculator.py`, `channel_roi_analyzer.py`, `channel_mix_optimizer.py`.
- contracts/deals: `deal_scorer.py`, `discount_approval_router.py`, `terms_redliner.py`, `discount_matrix_builder.py`, `exception_router.py`, `policy_linter.py`, `rfp_parser.py`, `response_drafter.py`, `winrate_predictor.py`.
- market/stock: `collect_data.py`, `validate_data.py`, `ratios.py`, `score.py`, `valuation.py`, `verify_data.py`.
- SaaS: `metrics_calculator.py`, `quick_ratio_calculator.py`, `unit_economics_simulator.py`, `project_bootstrapper.py`.
- research finance: `program_budget_planner.py`, `burn_runway_tracker.py`, `capex_vs_opex_router.py`.
- revenue: `pipeline_analyzer.py`, `forecast_accuracy_tracker.py`, `gtm_efficiency_calculator.py`.

## Output shape

`request -> selected module -> inputs/assumptions -> register/tool run -> reconciliation -> variance -> decision/range -> blockers`

## Stop conditions

- Missing ledger or payment source -> ask or abstain.
- Suspicious duplicate -> flag, do not silently reconcile.
- Contract/deal -> escalate unless approver rule met.
- Legal/tax -> professional review.
- Forecast -> range + confidence, not point promise.
