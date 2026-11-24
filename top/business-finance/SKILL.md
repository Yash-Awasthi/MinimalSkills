---
name: business-finance
description: >
  One standalone skill for business, finance and ERP work: Odoo end to end
  (accounting, payroll, country localization and e-invoicing, sales, purchase,
  inventory, manufacturing, timesheets, eCommerce with Shopify/WooCommerce/EDI,
  RPC API, module development, ORM, QWeb, XML views, tests, security rules,
  performance, Docker deployment, backup and migration), accounting registers
  and reconciliation, market data and trading tools, startup finance and
  metrics, pricing, SaaS operations, and document verification. Merges the
  business-finance class (109 skills) and the odoo deep pack (24). Fully
  self-contained: every procedure is inline, no external references.
metadata:
  merges: business-finance
  sources: 109
---

# business-finance

## 0. Iron laws (odoo pack contract — bind everything below)

1. **The version decides the answer.** Odoo changes APIs, view syntax, menus
   and module availability across releases. Establish the exact version,
   edition and installed modules before writing code or steps. A body
   written for 14–17 may not hold on 18–19; a module name is not evidence
   that every listed report or integration exists.
2. **Prove it on a copy.** Configuration, migration and upgrade work runs
   against a duplicate or staging database with a current database and
   filestore backup. Never run a schema change, module install or upgrade on
   production first.
3. **Back up both halves.** A database dump alone omits the filestore that
   holds attachments and images. Quiesce writers for the dump and archive
   interval, or use a snapshot procedure proven consistent, and verify with
   a restore test. Never delete the last known recoverable backup.
4. **Test with fixture users, never real credentials.** Isolated test users
   with explicit test-only passwords and the groups the test needs. Never
   assume a user's password equals their login.
5. **Integration users are least privilege.** Never use the master admin
   password for an API integration. Create a dedicated user with the minimum
   permissions; keep keys and session cookies out of logs and shared
   examples.
6. **Verify the boundary before you trust the payload.** Shopify webhooks
   are checked against `X-Shopify-Hmac-SHA256` on the raw request bytes and
   rejected with 401 on failure. Imported records deduplicate on the
   provider's own id. A 997 acknowledgment reports syntax and functional
   acceptance, not business acceptance.
7. **Inventory is a candidate, not a finding.** `sudo()` bypasses access
   rules and record rules. A wildcard group, a broad model access row and a
   permissive domain are candidates — confirm effective rights against the
   actual groups, companies and record rules before calling a path open.
8. **Numbers are claims.** Worker counts, memory limits, valuation figures
   and projections are illustrative or measured — say which. Never turn an
   estimate into a result.

## 1. Odoo — finance and payroll

- **Accounting setup** (accounting-setup): build the books in order —
  install the country chart of accounts and localization first, then
  journals, taxes, fiscal positions, payment terms, bank reconciliation
  models. A fiscal position maps a tax to a replacement tax and its
  reporting tags, so it needs the localization-approved tax, not an ad hoc
  one. VAT settings depend on registration and transaction eligibility —
  confirm both before changing a rate.
- **Payroll** (hr-payroll-setup, payroll-finance): start from the installed
  country localization and the effective payroll year. Record pay frequency,
  contract dates, taxable wage bases, approved earnings and deductions,
  statutory caps, withholding elections. Always set an active employee
  contract with correct dates and salary before generating payslips; review
  a salary structure rather than editing a live one blind.
- **Localization compliance** (l10n-compliance): install and validate a
  localization against the deployed version — Mexico CFDI 4.0, Italy
  FatturaPA, Poland SAF-T each have their own module and authority
  requirements. Do not apply one zero-rate rule to all EU goods and
  services; confirm the supply, the customer VAT status, the place-of-supply
  rule and the evidence with local guidance. Fiscal output goes to a
  qualified local reviewer.

## 2. Odoo — sales, purchasing and operations

- **Sales/CRM** (sales-crm-expert): pipeline stages, quotation templates,
  pricelists, teams, lead assignment, the sales-to-invoice path. Online
  signature and payment become required only when the template and
  confirmation settings say so. Check the installed edition before building
  a feature the vendor already ships (e.g. commissions).
- **Purchase** (purchase-workflow): RFQ → purchase order → receipt → vendor
  bill, with purchase agreements, quantity-break vendor pricelists,
  reordering and 3-way matching. A 2-level approval adds a gate before
  confirmation — name who holds each level. Match the bill to the receipt
  and the order before posting.
- **Inventory** (inventory-optimizer, inventory-demand-planning,
  inventory-stock-reconciliation): choose FIFO or AVCO; set min/max
  reordering rules; configure putaway, routes and multi-step receiving.
  Valuation method changes affect existing stock — understand the accounting
  impact first. A 3-step delivery is receive, quality, then store, each with
  its own operation type. Reconciliation: counts against ledger, variance
  explained, adjustments approved.
- **Manufacturing** (manufacturing-advisor, production-scheduling): build
  bills of materials, work centers and routing operations, then run the MRP
  scheduler. MRP suggests; availability still depends on demand accuracy,
  lead times, stock and supply execution. Do not hand-create purchase orders
  for MRP-managed items; override a suggestion only with a stated reason.
  Maintenance, PLM and Quality are separate apps.
- **Timesheets** (project-timesheet): billable projects with budgets, task
  stages, timesheet logging, approval and invoicing from approved hours.
  Enable approval before the invoice run, or unapproved hours bill.

## 3. Odoo — eCommerce and integrations

- **eCommerce** (ecommerce-configurator): publish products, configure a
  payment provider (Stripe), set shipping rates and a free threshold,
  abandoned-cart recovery, order-to-fulfillment flow. Use a duplicate test
  database and sandbox credentials. Publication, live payments, carrier
  bookings and outbound marketing need explicit scope.
- **Shopify / WooCommerce** (shopify-integration, woocommerce-bridge,
  shopify-review-triage): sync catalog, inventory, orders, customers.
  Verify the connector's publisher, support, license and version
  compatibility rather than assuming an official Enterprise connector;
  select API versions both systems support. Inbound webhooks are HMAC
  verified on the raw bytes before any parse, deduplicated on the provider
  id, and enqueued durably. Import status never doubles as a
  customer-facing payment or fulfillment marker. Review triage: public
  low-star reviews to a P0–P3 brief.
- **EDI** (edi-connector): map X12 and EDIFACT documents to Odoo objects;
  onboard a partner; parse an 850 into a sale order. Implement against the
  selected library and version and the partner's implementation guide —
  `pyx12` dictionary access and helpers vary. The 997 is a syntax and
  functional acknowledgment, not business acceptance.
- **RPC API** (rpc-api): JSON-RPC and XML-RPC authentication, model calls,
  CRUD in Python, JavaScript and curl. Supply an authorized session through
  a protected cookie store; never paste session cookies or keys into logs or
  shared examples.

## 4. Odoo — development, security, performance, deployment

- **Module development** (module-developer): scaffold with
  `__manifest__.py`, namespaced models, inherited views, security files and
  the standard directory layout. Prefix `_name` with a namespace (e.g.
  `hospital.patient`) so the model cannot collide with another module.
- **ORM** (orm-expert): search, browse, create, write, unlink; domains,
  computed fields, relational fields; batched writes that avoid N+1 queries.
  Batch calls reduce round trips but can still trigger extra compute and
  tracking queries. Use `sudo()` sparingly and only with the security
  implications understood. Datetime filters need UTC bounds built from the
  intended business timezone.
- **Views and reports** (qweb-templates, xml-views-builder): QWeb XML for
  PDF reports, email templates and website pages with `t-if`, `t-foreach`,
  `t-field` and report actions. Form, List, Kanban, Search, Calendar and
  Graph views for 14–17. The `attrs` syntax works through 16; 17 uses inline
  expressions such as `required="state == 'sale'"`; for 17 use the
  `oe_chatter` block and confirm the model inherits the mail mixins.
- **Tests** (automated-tests): TransactionCase unit tests, HttpCase
  controller tests and browser tours; isolate fixture users; run tagged
  suites from the CLI and in CI against a disposable database, never
  production.
- **Security rules** (security-rules): two levels — `ir.model.access.csv`
  grants model access per group; `ir.rule` domains limit which records a
  user sees. Define the module manager group before loading the CSV; do not
  reuse a broad settings or administration group for patient or customer
  data. Grant `perm_unlink` only where the business process requires
  deletion. A multi-company rule needs the company field in its domain.
- **Performance** (performance-tuner): diagnose slow pages, database
  bottlenecks, worker configuration, memory limits and bloat. Worker counts
  and memory limits in older bodies are illustrative — measure the workload
  and total memory before applying them. PostgreSQL slow-query logs and the
  built-in Odoo profiler are the evidence; verify a tuning change against
  the same workload.
- **Deployment** (docker-deployment): Odoo and PostgreSQL under Compose with
  persistent volumes, environment-based configuration, optional Nginx TLS
  proxy. Compose expands `${VAR}` in the Compose file, not in an arbitrary
  mounted application config — render required configuration through an
  approved private secret mechanism. Stop the normal workers and back up
  both halves before a module update. Restart Odoo alone for a harmless
  restart, not the database.
- **Backup and migration** (backup-strategy, migration-helper,
  upgrade-advisor): back up the database dump and filestore archive
  together, upload offsite, restore in the documented order; verify the
  filestore path with `odoo-bin shell` before a restore; apply a shorter
  retention only after an upload check and a successful restore test.
  Migration moves custom modules between major versions — compare every
  used model, field, method and view in the exact source and target
  branches; the `attrs`-to-inline-expression change is the common view break
  from 16 to 17. Upgrade: pre-upgrade checklist, Enterprise upgrade service
  or OpenUpgrade (which supplies addons, not the server — install a reviewed
  target-version server and include `openupgrade_framework` and
  `openupgrade_scripts` in the addons path), OCA compatibility, validate
  after. Disable outbound mail, cron, payments and external connectors on
  the cloned database.

## 5. Accounting registers and bookkeeping

- **Registers** (day-book, invoices-billing, tax-register, payment-
  accounting, purchase-accounting, receipt-accounting, sales-accounting,
  salary-wage-accounting, expense-accounting, expense-management, petty-cash-
  management, party-ledger-reconciliation, trading-ledger, atlas-ledger,
  atlas-contract): each register defines its columns, evidence rule and
  reconciliation cadence. Ledger reconciliation matches counterpart entries
  and ages the unmatched. Atlas ledger/contract: read-back hook runs first.
- **Audit and systems** (accounting-audit-system-builder, accounting-
  software-selection, json-schema-manual, local-schema-builder): build an
  audit-ready accounting system with stated scope; software selection with
  criteria; schema builders with declared boundaries.

## 6. Market data and trading

- **Data providers** (alpha-vantage, equibles, fxmacrodata, us-property-
  data, longbridge family — longbridge, longbridge-market-data,
  longbridge-fundamentals, longbridge-derivatives, longbridge-quant,
  longbridge-research): API key setup required first; each provider states
  its coverage and rate limits. Bundled upstream support declared where
  absent.
- **Analysis** (quant-analyst, options-flow-analyzer, traderspy-market-
  briefing, traderspy-trading-signals, traderspy-position-check, chord-
  onchain-trading, xvary-stock-research, warren-buffett persona): analysis
  outputs are information, not advice; signals carry confidence and
  evidence; position checks read-only; the Buffett persona is a simulation
  framework (Portuguese-canonical), not investment advice.
- **Web3 finance** (soroban-contract-audit, soroban-token-minter,
  stellar-escrow-timelock): contract audits with kill signals; token
  minting architecture; escrow/timelock patterns. (web3 hub carries the
  depth.)

## 7. Startup and SaaS

- **Business analysis** (business-analyst, startup-analyst, startup-
  business-analyst-business-case, startup-business-analyst-financial-
  projections, startup-business-analyst-market-opportunity, startup-
  financial-modeling, startup-metrics-framework, market-sizing-analysis):
  business cases with assumptions stated; financial projections with
  drivers, not hockey sticks; market sizing top-down and bottom-up; metrics
  framework (MRR, churn, CAC, LTV, payback) with definitions fixed before
  computing.
- **Pricing** (pricing, saas-pricing-strategist, usage-based-pricing):
  value metrics, packaging tiers, usage-based models with metering
  discipline.
- **Launch and ops** (micro-saas-launcher, saas-mvp-launcher, saas-multi-
  tenant, notion-template-business, business-website-setup, viboscope,
  find-complementary-founders, find-matching-tenders, no-free-work):
  launcher checklists; multi-tenant architecture patterns; tender matching
  with declared sources.
- **Churn and support** (churn-prevention, developer-churn, customer-
  support, review-response-generator, second-deposit-igaming): churn
  signals and save plays; support workflows with declared scope.
- **Company operations** (business-finance-ops, budget-cash-flow, business-
  continuity, attendance, company-email-accounts, contract-document-
  renewal, events-activities, asset-it-management, carrier-relationship-
  management, energy-procurement, logistics-exception-management, mdm-
  device-management, inventory-demand-planning, production-scheduling,
  sop-company-wiki, leave-management): registers and planners with evidence
  rules; continuity planning with RTO/RPO; procurement with approvals.
- **Legal** (advogado-especialista, leiloeiro family — leiloeiro-juridico,
  leiloeiro-ia, leiloeiro-avaliacao, leiloeiro-risco, lex, employment-
  contract-templates, verify-document, extract-document-data): Brazilian
  legal practice and auction analysis (Portuguese-canonical) with scope and
  verification rules; legal-entity cross-reference; document verification
  and data extraction with confidence stated. Templates are starting points,
  not legal advice.
- **Risk and supply chain** (risk-manager, supply-chain-risk-auditor,
  supply-chain-attack-response, sbom-supply-chain): risk registers with
  scoring; supply-chain audit and response with detection steps.
  (security-operations hub carries the security depth.)

## 8. Cross-carried fragments

- **Agent/tooling** (aria, evaluation, advanced-evaluation, infinity,
  recursive-context-pruning-token-budgeting, resumable-implementation-
  contracts, repo-foundation, pydantic-models-py, placecall, nap-
  consistency-checker): evaluation methods for agent systems; input boundary
  and validation protocol; token budgeting; resumable contracts.
  (ai-agents hub carries the depth.)
- **SEO** (nap-consistency-checker): local-listing consistency.
- **IT ops** (startup-it-troubleshooting): triage with stated scope.
  (devops hub carries the depth.)

## 9. Output contract

- Name the skill, the Odoo version and edition (or the financial system),
  and the database in the first line of reasoning and in the todo list.
- Report the artifact: a module path, a view id, a CSV row, a test result, a
  backup file, a register, a model, or a command output with its key fields.
- Keep ids, model names, field names, XML, account codes and error strings
  verbatim.
- State what was tested and where. A staging result is not a production
  result; a projection is not a measurement.
- Keep open work open: a missing module, an unverified connector, an
  untested restore are reported, never rounded up.
- Never print a password, key, session cookie, payroll figure or personal
  data; redact and name the rule.

## 10. Failure handling

| Situation | Response |
| --- | --- |
| The Odoo version or edition is unclear | Stop and confirm. Never guess the API. |
| A schema change or upgrade is requested on production | Prove it on a copy first, with a two-half backup. |
| A webhook arrives without a valid HMAC | Reject with 401 before any parse. |
| A 997 acknowledgment is treated as business acceptance | It is not. Confirm business acceptance separately. |
| `sudo()` appears in a proposed change | Justify it or remove it; confirm effective rights first. |
| A valuation method change is requested | State the accounting impact on existing stock first. |
| A restore has never been tested | Run the restore test before trimming retention. |
| A payroll figure or personal record would print | Redact and name the rule. |
| A market-data number has no source or timestamp | Label it unverified. |
| A projection is presented as a fact | Relabel it a projection with its assumptions. |
| The evidence contradicts the requested figure | Show the evidence and stop. |

## Provenance

Merged from the business-finance class (109 catalog skills) and the odoo
curated pack (24 sources, 6 groups). Every source skill's procedure, rule
and policy is represented above; duplicates collapsed to one canonical
statement; version discipline, backup/restore gates and least-privilege
rules preserved. No external file is required to use this skill.
