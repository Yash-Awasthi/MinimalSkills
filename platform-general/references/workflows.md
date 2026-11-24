# workflows

Load for scheduled jobs, event pipelines and visual automation builders.

## node shape

| node | role | rule |
| --- | --- | --- |
| trigger | webhook, schedule, event | one trigger per workflow |
| fetch | http or connector | timeout and retry set |
| transform | code or map | pure, no side effects |
| branch | condition | explicit default path |
| write | connector action | idempotent or guarded |
| notify | chat, mail | confirm the recipient |

A workflow takes one trigger; a second trigger is a second workflow, or the run log cannot say which one fired.

## schedule

```yaml
schedule:
  cron: "0 */2 * * *"
  timezone: UTC
  overlap: skip          # skip | queue | replace
  catchup: false
```

- Overlap policy explicit. A long run with `queue` builds a backlog.
- Catch-up off unless the job is idempotent and order independent.
- Timezone stated. A local-time cron drifts twice a year.

## reliability

| failure | guard |
| --- | --- |
| partial write | checkpoint per item, resume |
| duplicate run | idempotency key per item |
| silent failure | alert on zero items processed |
| runaway loop | max items and max runtime |
| credential expiry | expiry check before the run |

Alert on absence. A job that stops running looks exactly like a job that succeeds.

## testing

1. Run with a fixture payload, assert the writes.
2. Force a failure at each node, assert the checkpoint and the alert.
3. Run twice with the same payload, assert one effect.
4. Time a full run against the schedule interval.

## cost and limits

- Every run has a token or unit budget.
- Log items processed, failures and duration per run.
- Retain 30 days of run logs. Longer if an audit needs it.

## handoff

Export the workflow definition into the repo. A workflow that exists only in a hosted ui cannot be reviewed, diffed or restored.
## n8n index

| topic | the rule that matters |
| --- | --- |
| Setup. | `docker run -it --rm -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n`; the volume is the whole instance, a container without it loses every workflow. |
| Inspect the live instance and node version | `n8n --version` and the `/rest/settings` endpoint; a node version mismatch explains most import failures. |
| Target the right instance first. | Check the base URL before writing: a workflow built against localhost and imported to cloud keeps the localhost credential id. |
| Agent media stays outside the agent. | Generated images and audio are stored in object storage with a URL, never inlined in the workflow JSON, which has a size limit. |
| RAG is the last resort. | A vector store in n8n is for fuzzy text; a lookup by id is a database node, cheaper and exact. |
| Validation errors are specific. | A Code node returns `{error: "field X missing"}`; a bare throw loses which item failed. |
| Architecture patterns | One workflow per trigger, sub-workflows for reuse, a queue mode for anything over 30 seconds. |
| Routing | Switch node on a typed field, never on free text; a default branch that swallows unknown values hides failures. |
| Discovery | List the trigger node's payload first (`{{ JSON.stringify($json) }}`), then map fields; guessing the shape is the usual bug. |
| Versioning | Export workflows to git as JSON, one file per workflow; editing in the UI without an export is unversioned production code. |
| Personas | An AI node's persona is a system prompt in one place; duplicating it per node drifts. |
