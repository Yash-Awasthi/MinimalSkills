---
name: odoo
description: >-
  24 Odoo skills spanning accounting and payroll, country localization and e-invoicing,
  sales, purchase, inventory, manufacturing, and project timesheets, eCommerce plus
  Shopify, WooCommerce, and EDI integrations, the RPC API, module development, ORM,
  QWeb, XML views, automated tests, access rules, performance tuning, Docker deployment,
  backup and restore, and version migration and upgrade. Use when a task touches an
  Odoo model, view, module, localization, integration, or deployment, or when the user
  names an odoo skill.
metadata:
  curated_from: 24
  skills: 24
  groups: 6
---

# odoo

24 skills. 6 groups. One hub. Every source body is preserved verbatim in
`references/skills/<skill>.md`. These sources ship no non-SKILL.md files, so
`references/assets/` stays empty. Load one body for the task.

`SOURCES.md` maps every source path to its canonical skill and group.
`references/INDEX.md` groups the links, `references/skills.tsv` carries every
description, and `references/GUIDE.md` holds the long-form group prose.

## Pack contract

**The version decides the answer.** Odoo changes APIs, view syntax, menus, and module
availability across releases. Establish the exact version, edition, and installed
modules before writing code or steps. A body written for 14 to 17 may not hold on 18 or
19, and a module name is not evidence that every listed report or integration exists.

**Prove it on a copy.** Configuration, migration, and upgrade work runs against a
duplicate or staging database with a current database and filestore backup. Never run a
schema change, module install, or upgrade on production first.

**Back up both halves.** A database dump alone omits the filestore that holds
attachments and images. Quiesce writers for the dump and archive interval, or use a
snapshot procedure proven consistent, and verify the result with a restore test.

**Test with fixture users, never real credentials.** Create isolated test users with
explicit test-only passwords and the groups the test needs. Never assume a user's
password equals their login.

**Integration users are least privilege.** Never use the master admin password for an
API integration or connector. Create a dedicated user with the minimum permissions the
job needs, and keep keys and session cookies out of logs and shared examples.

**Verify the boundary before you trust the payload.** Shopify webhooks are checked
against `X-Shopify-Hmac-SHA256` on the raw request bytes and rejected with 401 when the
HMAC fails. Imported records are deduplicated on the provider's own id. A 997
acknowledgment reports syntax and functional acceptance, not business acceptance.

**Inventory is a candidate, not a finding.** `sudo()` bypasses access rules and record
rules. A wildcard group, a broad model access row, and a permissive domain are
candidates. Confirm effective rights against the actual groups, companies, and record
rules before calling a path open.

**Read the body before the menu path.** Menu paths and example values are illustrative
and version dependent. The body carries the constraints, the order, and the checks that
make the example safe.

**Write clean as you draft.** Short declarative sentences. No em dash. A colon may
introduce a list and may not connect two clauses. Sentence case headings. No chatbot
framing, no generic closer.

## Routing

| The user wants | Group |
| --- | --- |
| Accounting configured, payroll reviewed, or a country localization installed | Finance and payroll |
| Sales, purchase, inventory, manufacturing, or timesheet work | Sales, purchasing, and operations |
| A store configured, or Shopify, WooCommerce, EDI, or RPC integration | eCommerce and integrations |
| A module, ORM query, QWeb report, XML view, or test suite | Development and views |
| Access rules written, or a performance problem diagnosed | Security and performance |
| Docker deployment, a backup and restore, or a version migration or upgrade | Deployment, backup, and upgrades |

## Full roster

### Finance and payroll

| Skill | What it does |
| --- | --- |
| [`accounting-setup`](references/skills/accounting-setup.md) | Configures the chart of accounts, journals, fiscal positions, taxes, payment terms, and bank reconciliation models from scratch. |
| [`hr-payroll-setup`](references/skills/hr-payroll-setup.md) | Reviews salary structures and Python payslip rules, time off types, employee contracts, and the payroll to accounting journal flow. |
| [`l10n-compliance`](references/skills/l10n-compliance.md) | Installs and validates the country localization, then prepares taxes, e-invoicing, and fiscal reports for qualified local review. |

### Sales, purchasing, and operations

| Skill | What it does |
| --- | --- |
| [`inventory-optimizer`](references/skills/inventory-optimizer.md) | Configures FIFO or AVCO valuation, reordering rules, putaway, routes, multi-step receiving, and multi-warehouse flows. |
| [`manufacturing-advisor`](references/skills/manufacturing-advisor.md) | Builds bills of materials, work centers, routing operations, and production orders, then runs the MRP scheduler against real demand. |
| [`project-timesheet`](references/skills/project-timesheet.md) | Creates billable projects, task stages, timesheet logging and approval, budget alerts, and invoicing from approved hours. |
| [`purchase-workflow`](references/skills/purchase-workflow.md) | Runs RFQ to purchase order to receipt to vendor bill, with purchase agreements, vendor pricelists, reordering, and 3-way matching. |
| [`sales-crm-expert`](references/skills/sales-crm-expert.md) | Sets up CRM pipeline stages, quotation templates, pricelists, sales teams, lead assignment, and the sales to invoice path. |

### eCommerce and integrations

| Skill | What it does |
| --- | --- |
| [`ecommerce-configurator`](references/skills/ecommerce-configurator.md) | Publishes a catalog, wires a payment provider, sets shipping rates and free thresholds, and covers cart recovery and order fulfillment. |
| [`edi-connector`](references/skills/edi-connector.md) | Maps X12 and EDIFACT documents to Odoo objects, onboards partners, parses an 850 into a sale order, and sends a 997 acknowledgment. |
| [`rpc-api`](references/skills/rpc-api.md) | Authenticates over JSON-RPC and XML-RPC, then performs search, read, create, write, and delete with a dedicated integration user. |
| [`shopify-integration`](references/skills/shopify-integration.md) | Syncs products, inventory, orders, and customers, and verifies the webhook HMAC before parsing or enqueuing a payload. |
| [`woocommerce-bridge`](references/skills/woocommerce-bridge.md) | Builds a WooCommerce to Odoo sync bridge for catalog, stock, orders, and customers over the REST APIs, with idempotent imports. |

### Development and views

| Skill | What it does |
| --- | --- |
| [`automated-tests`](references/skills/automated-tests.md) | Writes TransactionCase and HttpCase tests plus browser tours, isolates fixture users, and runs tagged suites in CI. |
| [`module-developer`](references/skills/module-developer.md) | Scaffolds a custom module with a manifest, namespaced models, inherited views, security files, and Odoo coding conventions. |
| [`orm-expert`](references/skills/orm-expert.md) | Searches, writes, and computes through the ORM with domain filters, relational fields, and batched calls that avoid N+1 queries. |
| [`qweb-templates`](references/skills/qweb-templates.md) | Writes QWeb XML for PDF reports, email templates, and website pages with t-if, t-foreach, t-field, and report actions. |
| [`xml-views-builder`](references/skills/xml-views-builder.md) | Builds Form, List, Kanban, Search, Calendar, and Graph views for Odoo 14 to 17, including the attrs to inline expression change. |

### Security and performance

| Skill | What it does |
| --- | --- |
| [`performance-tuner`](references/skills/performance-tuner.md) | Diagnoses slow pages, database bottlenecks, worker misconfiguration, and memory bloat with PostgreSQL and Odoo profilers. |
| [`security-rules`](references/skills/security-rules.md) | Writes ir.model.access.csv entries, ir.rule record rules, groups, and multi-company domains without over-granting delete. |

### Deployment, backup, and upgrades

| Skill | What it does |
| --- | --- |
| [`backup-strategy`](references/skills/backup-strategy.md) | Backs up the database and filestore together, uploads offsite, and restores through a tested sequence. |
| [`docker-deployment`](references/skills/docker-deployment.md) | Runs Odoo and PostgreSQL under Compose with persistent volumes, environment configuration, and an optional Nginx TLS proxy. |
| [`migration-helper`](references/skills/migration-helper.md) | Migrates custom modules across major versions by verifying each changed model, field, method, and view against the real branches. |
| [`upgrade-advisor`](references/skills/upgrade-advisor.md) | Runs a pre-upgrade checklist, chooses the Enterprise or OpenUpgrade path, checks OCA compatibility, and validates after the upgrade. |

## Group notes

### Finance and payroll

`accounting-setup` builds the books in order. Install the country chart of accounts and
the localization first, then journals, taxes, fiscal positions, payment terms, and bank
reconciliation models. A fiscal position maps a tax to a replacement tax and its
reporting tags, so it needs the localization-approved tax, not an ad hoc one. VAT
settings depend on registration and transaction eligibility, so confirm both before
changing a rate.

`hr-payroll-setup` starts from the installed country localization and the effective
payroll year. Record pay frequency, contract dates, taxable wage bases, approved
earnings and deductions, statutory caps, and withholding elections. Always set an
active employee contract with correct dates and salary before generating payslips, and
review a salary structure rather than editing a live one blind.

`l10n-compliance` installs and validates a localization against the deployed version.
Mexico CFDI 4.0, Italy FatturaPA, and Poland SAF-T each have their own module and
authority requirements, and the body links the current documentation for the version in
use. Do not apply one zero-rate rule to all EU goods and services. Confirm the supply,
the customer VAT status, the place-of-supply rule, and the evidence with local
guidance. Fiscal output goes to a qualified local reviewer.

### Sales, purchasing, and operations

`sales-crm-expert` sets pipeline stages, quotation templates, pricelists, teams, lead
assignment, and the sales to invoice path. Online signature and payment only become
required when the template and the confirmation settings say so. Check the installed
edition before building a feature the vendor already ships, such as commissions.

`purchase-workflow` runs RFQ, purchase order, receipt, and vendor bill, with purchase
agreements, quantity-break vendor pricelists, reordering, and 3-way matching. A 2-level
approval adds a gate before confirmation, so name who holds each level. Match the bill
to the receipt and the order before posting it.

`inventory-optimizer` chooses FIFO or AVCO, sets min and max reordering rules, and
configures putaway, routes, and multi-step receiving. Valuation method changes affect
existing stock, so understand the accounting impact first. A 3-step delivery is receive,
quality, then store, and each step needs its own operation type.

`manufacturing-advisor` builds bills of materials, work centers, and routing
operations, then runs the MRP scheduler. MRP suggests; availability still depends on
demand accuracy, lead times, stock, and supply execution. Do not hand-create purchase
orders for MRP-managed items, and override a suggestion only with a stated reason.
Maintenance, PLM, and Quality are separate apps.

`project-timesheet` creates billable projects with budgets, task stages, timesheet
logging, approval, and invoicing from approved hours. A clear timesheet description is
recommended for the invoice, not required by the model. Approval must be enabled before
the invoice run, or unapproved hours bill.

### eCommerce and integrations

`ecommerce-configurator` publishes products, configures a payment provider such as
Stripe, sets shipping rates and a free threshold, and covers abandoned cart recovery
and the order to fulfillment flow. Use a duplicate test database and sandbox
credentials. Publication, live payments, carrier bookings, and outbound marketing need
explicit scope, and the provider webhook events depend on the installed module.

`edi-connector` maps X12 and EDIFACT documents to Odoo objects, onboards a partner, and
parses an 850 into a sale order. Implement against the selected library and version and
the partner's implementation guide, since `pyx12` dictionary access and helpers vary.
The 997 is a syntax and functional acknowledgment, not a business acceptance.

`shopify-integration` and `woocommerce-bridge` sync catalog, inventory, orders, and
customers. Verify the connector's publisher, support, license, and version compatibility
rather than assuming an official Enterprise connector, and select API versions both
systems support. Inbound webhooks are HMAC verified on the raw bytes before any parse,
deduplicated on the provider id, and enqueued durably. Import status never doubles as a
customer-facing payment or fulfillment marker.

`rpc-api` covers JSON-RPC and XML-RPC authentication, model calls, and CRUD in Python,
JavaScript, and curl. Supply an authorized session through a protected cookie store, and
never paste session cookies or keys into logs or shared examples. A dedicated
integration user replaces the master admin password.

### Development and views

`module-developer` scaffolds a module with `__manifest__.py`, namespaced models,
inherited views, security files, and the standard directory layout. Prefix `_name` with
a namespace such as `hospital.patient` so the model cannot collide with another module.

`orm-expert` covers search, browse, create, write, and unlink, with domains, computed
fields, relational fields, and batched writes that avoid N+1 queries. Batch calls reduce
repeated round trips but can still trigger extra compute and tracking queries. Use
`sudo()` sparingly and only with the security implications understood. Datetime filters
need UTC bounds built from the intended business timezone.

`qweb-templates` writes QWeb XML for PDF reports, email templates, and website pages
with `t-if`, `t-foreach`, `t-field`, and report actions. `xml-views-builder` builds Form,
List, Kanban, Search, Calendar, and Graph views for 14 to 17. The `attrs` syntax works
through 16, and 17 uses inline expressions such as `required="state == 'sale'"`. For 17
use the `oe_chatter` block and confirm the model inherits the mail mixins.

`automated-tests` writes TransactionCase unit tests, HttpCase controller tests, and
browser tours, isolates fixture users, and runs tagged suites from the CLI and in CI.
Tests run against a disposable database, never production.

### Security and performance

`security-rules` covers the two levels. `ir.model.access.csv` grants model access per
group, and `ir.rule` domains limit which records a user sees. Define the module manager
group before loading the CSV, and do not reuse a broad settings or administration group
for patient or customer data. Grant `perm_unlink` only where the business process
requires deletion. A multi-company rule needs the company field in its domain.

`performance-tuner` diagnoses slow pages, database bottlenecks, worker configuration,
memory limits, and bloat. Worker counts and memory limits in the body are illustrative,
so measure the workload and total memory before applying them. PostgreSQL slow-query
logs and the built-in Odoo profiler are the evidence, and a tuning change is verified
against the same workload.

### Deployment, backup, and upgrades

`docker-deployment` runs Odoo and PostgreSQL under Compose with persistent volumes, an
environment-based configuration, and an optional Nginx TLS proxy. Compose expands
`${VAR}` in the Compose file, not in an arbitrary mounted application config, so render
required configuration through an approved private secret mechanism. Stop the normal
workers and back up the database and filestore before a module update. Restart Odoo
alone for a harmless restart, not the database.

`backup-strategy` backs up the database dump and the filestore archive together, uploads
offsite, and restores in the documented order. Quiesce writers for the whole dump and
archive interval or use a proven snapshot. Verify the filestore path with `odoo-bin
shell` before a restore, and apply a shorter retention only after an upload check and a
successful restore test. Never delete the last known recoverable backup.

`migration-helper` moves custom modules between major versions. Compare every used
model, field, method, and view in the exact source and target branches and installed
addons. Do not apply a blanket rename or assume a report-method signature. The `attrs`
to inline expression change is the common view break from 16 to 17.

`upgrade-advisor` runs the pre-upgrade checklist, picks the Enterprise upgrade service
or OpenUpgrade, checks OCA module compatibility, and validates after. Always upgrade a
copy of production first. Modern OpenUpgrade supplies addons, not the Odoo server, so
install a reviewed target-version server and include `openupgrade_framework` and
`openupgrade_scripts` in the addons path. Disable outbound mail, cron, payments, and
external connectors on the cloned database.

## Output contract

- Name the skill, the Odoo version and edition, and the database in the first line of
  your reasoning and in the todolist.
- Report the artifact. A module path, a view id, a CSV row, a test result, a backup
  file, or a command output with its key fields.
- Keep ids, model names, field names, XML, and error strings verbatim.
- State what was tested and where. A staging result is not a production result.
- Keep open work open. A missing module, an unverified connector, and an untested
  restore are reported, never rounded up.
- Never print a password, key, session cookie, payroll figure, or personal data. Redact
  it and name the rule.
- Write through `unslop`. Short declarative sentences, sentence case headings, no em
  dash, no colon connecting two clauses, no chatbot framing.

## Failure handling

| Situation | Response |
| --- | --- |
| The Odoo version, edition, or installed module is unknown | Stop and confirm before writing code or steps. |
| A change would run on production | Move it to a duplicate or staging database with a current backup. |
| A backup has no restore test | Do not call it recoverable, and do not prune older copies. |
| An integration user is the master admin | Replace it with a least-privilege user. Name the rule. |
| A webhook fails HMAC verification | Reject it with 401 and log no payload. |
| A permission path is only a candidate | Label it unproven until the effective rights are confirmed. |
| A migration rename or signature is assumed | Verify it in the exact branches and addons first. |
| The evidence contradicts the requested change | Show the evidence and stop. |

## Provenance

24 `sickn33-odoo-*` source directories became 24 canonical skills in 6 groups. Each
source had one body, so no merge or variant resolution was needed. Every body is
verbatim at `references/skills/<skill>.md` with its original frontmatter removed. The
sources carry no non-SKILL.md files, so `references/assets/` is empty and no asset bytes
were copied.

The bodies are written for the Odoo 14 to 19 range, and several state that menus,
module availability, and API details depend on the exact version and edition. That
statement is kept. Verify the deployed version before applying an example.

Upstream collection `sickn33`. Original catalog paths are preserved in `SOURCES.md` and
under `_archive/odoo/catalog/`.
