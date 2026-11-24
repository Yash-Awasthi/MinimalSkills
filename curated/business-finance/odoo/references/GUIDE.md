# odoo guide

The long-form group prose and the full roster. `SKILL.md` is the loadable hub, and
`references/skills/<skill>.md` is the verbatim body to follow for one task.

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
