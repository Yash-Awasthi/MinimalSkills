# saas-automation

Load when an agent acts on a SaaS tool: crm, docs, issues, mail, chat.

## before acting

| check | question |
| --- | --- |
| identity | which account is connected, whose data |
| scope | read only, or write |
| target | exact record, channel, repo, doc |
| reversibility | can the action be undone |
| audience | who sees the result |

A write to the wrong workspace is not undoable: resolve the workspace id from the authenticated account, never from a name or the last-used default.

## permission tiers

| tier | example | gate |
| --- | --- | --- |
| read | list issues, fetch a doc | none beyond connection |
| create | draft a doc, open a ticket | confirm the target |
| update | change status, edit a field | confirm record and value |
| send | email, chat message, comment | confirm text and recipients |
| delete | remove a record | explicit request, named record |

## field mapping

- Map provider fields to a typed model before use. Field names differ per tool.
- Store the provider id as the join key; a name match breaks on rename and merges two records into one.
- Null and empty differ: `null` is unset, `""` is cleared; map each to its own field or the sync flips one into the other.
- Pagination: follow the cursor, cap the pages, report the cap.

## idempotency

- Search by the natural key before create; a duplicate ticket costs a merge and breaks every external reference to it.
- Store the external id with the local record.
- A retried send needs a dedupe key or a sent-marker.

## bulk operations

- Chunk to the provider's batch limit.
- Report per-item success and failure, not one summary.
- A partial failure leaves a resumable checkpoint.

## failure

| case | action |
| --- | --- |
| token expired | refresh once, then report |
| scope missing | report which scope, do not ask for a broader one silently |
| rate limited | backoff, resume from the checkpoint |
| record not found | report the id, do not create a duplicate |

## review

- Every write names its target in the output.
- Every send is quoted back before it goes out.
- A dry-run mode exists for bulk actions.

## composio actions

- One connected account per user. `entity_id` scopes every call to that user's tokens, so a shared id leaks access.
- `composio.tools.execute("GMAIL_SEND_EMAIL", { entity_id, arguments: { ... } })`.
- Action names are prefixed per app: `GMAIL_`, `SLACK_`, `NOTION_`, `LINEAR_`. List the toolkit before guessing a name.
- A 401 means the connection expired: send the user a reconnect link, do not retry the call.
- Rate limits are per connected account, not per app key, so one busy user can throttle themselves only.
| Reverse engineering | `apktool d`, `jadx-gui`, `frida -U -f pkg` for a runtime hook; authorized targets only, and never against a third-party app without written scope. |
