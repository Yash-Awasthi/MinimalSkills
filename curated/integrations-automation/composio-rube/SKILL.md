---
name: composio-rube
description: >
  Automate 823 SaaS apps through Composio toolkits on Rube MCP — Slack, Notion, Google
  Drive, HubSpot, Salesforce, Stripe, Shopify, GitHub, Jira, Linear, Zendesk, QuickBooks,
  Datadog, and long-tail tools. Use when a task must read or write data in a
  third-party SaaS account and RUBE_* MCP tools exist or can be connected. Discover
  schemas first. Never hardcode a tool slug.
metadata:
  curated_from: 845
  replaces: "composio-<app>-automation, sickn33-<app>-automation"
  deep_workflows: 106
---

# composio-rube

One skill. 823 app toolkits. 845 per-app skills collapsed. Canonical workflow + app
catalog + 106 deep workflow references. No workflow, command, param, or rule dropped.

## When to use

Use when:
- User names an app plus an action: post, read, create, update, search, upload, invite, pay.
- Task needs third-party SaaS data or a side effect in a SaaS account.
- `RUBE_*` MCP tools are present.
- `https://rube.app/mcp` can be added as an MCP server.

Do not use when:
- App absent from `references/app-catalog.tsv` and `RUBE_SEARCH_TOOLS` returns no toolkit. Use the native API, CLI, or UI; say which.
- Task touches only local files or the local machine.

## Hard rules

1. **Search first.** Call `RUBE_SEARCH_TOOLS` before every workflow. Schemas change. Never hardcode a tool slug, field name, or argument type.
2. **Connect before execute.** `RUBE_MANAGE_CONNECTIONS` must report `ACTIVE` for the toolkit. Not `ACTIVE`: return the auth link and stop. No execute attempt.
3. **Exact schema.** Use field names and types from the latest search result. Do not invent or rename fields.
4. **`memory` always.** Include `memory` in every `RUBE_MULTI_EXECUTE_TOOL` call, even empty: `memory: {}`.
5. **Reuse session.** Same session id within one workflow. New session for a new workflow.
6. **Paginate to the end.** Follow pagination tokens until absent. Keep date and result windows bounded. Report if stopped early.
7. **Read is not write permission.** Search or read does not authorize create, update, delete, send, schedule, invite, publish, or pay. Perform writes only under a matching user instruction, scoped to the named account, workspace, channel, or record.
8. **Preview broadcast and destructive actions.** Mass mentions, bulk deletes, payments, cross-workspace or shared-channel exposure: state target and count before execution.
9. **Verify writes.** Read back the created or updated object, or persist the returned id and timestamp. Uncertain send: reconcile history before retry. No blind retry.
10. **Identifiers verbatim.** Timestamps as strings. Ids, slugs, currency, units, error strings unchanged.
11. **Redact.** Never echo tokens, secrets, or private content. Redact before reporting.
12. **One toolkit per workflow** unless a cross-app chain is explicit. State chain order first.

## Setup

1. Add `https://rube.app/mcp` as an MCP server. No API key for the endpoint; the target account still authenticates.
2. Verify `RUBE_SEARCH_TOOLS` responds.
3. Call `RUBE_MANAGE_CONNECTIONS` with toolkit `<slug>`.
4. Not `ACTIVE`: open the returned auth link. Complete OAuth and grant the required scopes.
5. Confirm `ACTIVE` before any workflow.

## Canonical workflow

### Step 1 — discover tools

```
RUBE_SEARCH_TOOLS
queries: [{use_case: "<app> <task>", known_fields: ""}]
session: {generate_id: true}
```

Returns tool slugs, input schemas, recommended execution plans, known pitfalls.

### Step 2 — check connection

```
RUBE_MANAGE_CONNECTIONS
toolkits: ["<slug>"]
session_id: "<session_id>"
```

### Step 3 — execute

```
RUBE_MULTI_EXECUTE_TOOL
tools: [{
  tool_slug: "TOOL_SLUG_FROM_SEARCH",
  arguments: { /* schema-compliant args from search results */ }
}]
memory: {}
session_id: "<session_id>"
```

### Bulk and loops

`RUBE_REMOTE_WORKBENCH` with `run_composio_tool()`.

### Full schema

`RUBE_GET_TOOL_SCHEMAS` for tools that return a `schemaRef`.

## Find the app

`references/app-catalog.tsv` — 823 rows, tab-separated:

| Column | Meaning |
| --- | --- |
| `slug` | Value for `RUBE_MANAGE_CONNECTIONS` |
| `app` | Display name |
| `docs` | `https://composio.dev/toolkits/<slug>` |
| `mode` | `template` = canonical only; `detailed` = deep workflow exists |
| `description` | What the toolkit automates |
| `source_count` | Number of per-app skills merged |
| `paths` | Original source folders |

Lookup:

```bash
rg -i "slack" references/app-catalog.tsv
```

```powershell
Select-String -Path references/app-catalog.tsv -Pattern "slack"
```

App missing: run `RUBE_SEARCH_TOOLS` by use case. Rube can expose toolkits beyond this catalog.

## Deep workflows

106 apps have tested sequences beyond the canonical pattern. Full map in
`references/workflows/INDEX.md`:

active_campaign, airtable, amplitude, anthropic_administrator, asana, bamboohr,
basecamp, bitbucket, box, brevo, cal, calendly, canva, capsule_crm, circleci,
clickup, close, coda, confluence, datadog, discordbot, docker_hub, docusign,
dropbox, figma, fillout_forms, freshdesk, freshservice, github, gitlab,
google_admin, google_analytics, google_classroom, google_maps,
google_search_console, googledocs, googlemeet, googlephotos, googlesheets,
googleslides, googletasks, helpdesk, hubspot, instagram, intercom, jira, kit,
klaviyo, launch_darkly, lemon_squeezy, linear, linkedin, mailchimp, make,
many_chat, metabase, microsoft_clarity, microsoft_teams, miro, mistral_ai,
mixpanel, monday, new_relic, notion, one_drive, onesignal_rest_api, outlook,
pagerduty, pipedrive, posthog, postmark, reddit, render, ring_central,
salesforce, segment, sendgrid, sentry, share_point, shopify,
similarweb_digitalrank_api, slack, square, stripe, supabase, survey_monkey,
telegram, tiktok, todoist, trello, twitter, vercel, wave_accounting, webflow,
whatsapp, wrike, youtube, zendesk, zoho, zoho_bigin, zoho_books, zoho_desk,
zoho_inventory, zoho_invoice, zoho_mail, zoom.

1. Find the slug in `references/app-catalog.tsv`.
2. Read `references/workflows/<slug>.md`.
3. Load only that file. One app per task.

Conflict: deep file wins on app specifics — tool order, key parameters, pitfalls, boundaries.
This file wins on universal rules.

## Failure handling

| Symptom | Action |
| --- | --- |
| Connection not `ACTIVE` | Return auth link. Stop. |
| Tool slug or schema not found | Re-run `RUBE_SEARCH_TOOLS` with a different `use_case`. No guessed slug. |
| `ok=true` but empty result | Check the data path, widen filters or dates, verify account permissions. |
| More results | Continue pagination tokens until absent. |
| Validation error, `invalid_blocks`, `Invalid request data provided` | Load the app deep file. Fix the payload. Retry once. |
| Uncertain write | Read back by id. Reconcile. Only then decide retry. |
| Rate limit | Back off, shrink the batch, keep the session. |
| Auth scope missing | Re-run `RUBE_MANAGE_CONNECTIONS`, grant scopes, confirm `ACTIVE`. |

## Output contract

Report, one line per action:

```
app=<app> toolkit=<slug> tool=<tool_slug> args=<redacted> result=<ids/status> verified=<yes/no> remaining=<none|count>
```

Then one line for the outcome. No restated workflow.

## Provenance

- `SOURCES.md` — all 845 source skills, slug, canonical or deep.
- `references/app-catalog.tsv` — 823 slugs, deduplicated.
- `references/workflows/` — 113 deep bodies verbatim across 106 slugs.
- 732 canonical bodies differed only by app name and slug; the pattern above is their union.
