# odoo

Load for Odoo modules, models, workflows and deployment.

## model

```python
class Invoice(models.Model):
    _name = "acme.invoice"
    _description = "Invoice"

    amount_cents = fields.Monetary(currency_field="currency_id", required=True)
    currency_id = fields.Many2one("res.currency", required=True)
    partner_id = fields.Many2one("res.partner", required=True, index=True)
    state = fields.Selection([("draft", "Draft"), ("posted", "Posted")], default="draft")
```

- One model per concept. `_inherit` to extend, `_inherits` for composition.
- Index every field used in a domain filter.
- `Monetary` with an explicit currency field. Never a bare float.
- Access rules in `ir.model.access.csv`, record rules for row scope.

## security

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_acme_invoice_user,acme.invoice.user,model_acme_invoice,base.group_user,1,1,1,0
```

- Every model has an access line. A missing line is an install-time warning and a runtime hole.
- Record rules for multi-company and per-user scope.
- `sudo()` only with a written reason. It bypasses every rule.

## views and actions

- Form, list, search, kanban per model as needed.
- A button calls a method that returns an action or True. No business logic in the view.
- Menus attach to an existing `parent_id`; a new top-level root needs its own `ir.ui.menu` record and a group, or the item is invisible to non-admins.

## workflows

- Use `state` fields and guarded transitions. A transition checks the source state.
- A posted move is corrected by a reversal dated today, not edited; an edit to a posted line breaks the audit trail the ledger exists to provide.
- Automations in `ir.cron` carry a name, an interval and an idempotent body.

## upgrade

```bash
odoo-bin -c odoo.conf -u acme_invoice --stop-after-init
```

- Test the upgrade on a copy with production data.
- Migrations live in `migrations/<version>/pre-*.py` and are idempotent.
- A schema change without a migration script fails on an existing database.

## performance

- `search` with a domain and an explicit `limit`.
- `read` specific fields, not `browse` in a loop.
- Batch writes with `write` on a recordset.
- Check slow queries in the log at `--log-level=debug_sql`.

## review

- Access rules present for every new model.
- No `sudo()` without a reason comment.
- Migration script present for every schema change.
## odoo module index

| module | the rule that matters |
| --- | --- |
| Purchase | RFQ to PO to receipt to bill; a bill without a receipt leaves stock and ledger disagreeing. |
| Manufacturing | BOM plus routing; a component consumed at a different step needs a byproduct line, or the cost is wrong. |
| Timesheets | `account.analytic.line` feeds the invoice; a timesheet with no analytic account never reaches a project cost. |
| eCommerce | Product published to the website needs a delivery method, or checkout fails at the last step. |
| Shopify / WooCommerce | Sync on the external id, not the SKU; a re-sync after a price change overwrites the catalogue without a log. |
| Localization compliance | A localisation module ships the chart of accounts and tax report; installing it after postings corrupts the tax mapping. |

## analysis index

| topic | the rule that matters |
| --- | --- |
| Registers | Journal, sales, purchase, payment: each register is a filtered view of the same lines, so a total that disagrees is a filter bug. |
| Analysis | Margin = (revenue - cogs) / revenue per order; an average across products hides the loss-making half. |
| Churn and support | Churn is logo and revenue separately; a support ticket per account per month above 3 predicts churn better than NPS. |
| Legal | Entity, jurisdiction, contract term, renewal date; an auto-renewing contract with no notice window is a budget surprise. |
| Risk and supply chain | Lead time, single-source flag, exposure per supplier; a single-source component with a 12-week lead time is a plan risk, not a purchasing detail. |
## odoo ecommerce and integrations

- Website product needs a delivery method and a payment provider, or checkout fails at the last step.
- Shopify or Woo connector syncs on the external id; a price sync overwrites the catalogue, so log every write.
- A connector that runs on a cron needs a lock: two workers importing the same order create duplicates.
- Outgoing webhooks retry three times; the receiver must dedupe on the Odoo record id.

## odoo development, security, performance and deployment

- Model: `_name` for new, `_inherit` to extend, `_inherits` for composition; `_order` set explicitly or the list view is unstable.
- Access: one `ir.model.access.csv` line per model plus record rules for row scope; `sudo()` needs a written reason in the commit.
- Performance: `search_count` over `len(search())`, `read_group` for aggregates, `prefetch` is automatic within a recordset loop but not across a `search` per row.
- Deployment: `--db-filter` pinned, workers = 2 x CPU + 1, `--limit-time-real` below the proxy timeout, and a migration script under `migrations/<version>/` for every schema change.
