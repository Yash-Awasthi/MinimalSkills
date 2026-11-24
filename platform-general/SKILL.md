---
name: platform-general
description: Use when wiring third-party services or automation: paid feeds and scraping providers, SaaS tool actions across CRM, files and tickets, workflow builders, webhooks, credentials, rate limits, retries, cost per run. Triggers: integration, automation, n8n, credential, webhook.
---

# platform-general

## use when

- paid data, scraping, enrichment provider -> references/paid-apis.md
- act on a SaaS tool: crm, docs, issues, mail -> references/saas-automation.md
- workflow automation, scheduled job, n8n -> references/workflows.md

not for: first-party endpoints (backend-api), deploy delivery (devops-cloud), datasets (data-ml)

## rules

- Conflict order: credential safety, then the cost ceiling, then speed; an uncapped retry is a stop.
- Read the provider's price, rate limit and quota before the first call; an unbounded loop is an invoice.
- Retry only idempotent calls, three attempts with jitter, then dead letter with the request id.
- Every integration has a failure path that keeps the payload: dead letter, alert or recorded skip.
- Scrape only what the terms allow, at the published crawl delay; a 429 is a stop, not a challenge.
- The owner's key stays server side in a secret store; one scoped key per integration, rotated on a schedule and revoked when the integration is removed.
- An empty response is reported as empty with its scope and query, never as success.

## change

1. Locate: the client call, its credential scope, and every workflow that invokes it.
2. Propose the integration change in one sentence, with the alternative you rejected.
3. Predict before calling: units consumed, cost per run, which failure path triggers.
4. Back up the original client and config in context, pinned to `git rev-parse HEAD`.
5. Apply one concern per edit; a retry change and a new endpoint are two edits.
6. Verify: one real call with latency and units logged, then the 429 path.
7. Regress: every workflow calling the client, the cost alert and the dead-letter queue.
8. Compare the call against the prediction; an unplanned unit count stops the loop.
9. Report the endpoint, scopes and measured cost, then take the next item.

## integrate

```bash
curl -s https://api.provider.com/v1/health -H "authorization: Bearer $KEY"
```

1. Read the provider docs: auth, limits, price, idempotency, webhook signature.
2. Put the key in the secret store. Confirm it is not in the tree: `rg -i "sk-|api_key" .`
3. Write the client with a timeout, a retry policy and a typed response.
4. Make one real call. Record the latency, the units consumed and the cost.
5. Add the failure path: dead letter, alert, or a recorded skip.
6. Document the limit and the cost per run in the PR body.

## webhook receiver

```ts
const raw = await req.text();                                  // before any json parse
const expected = createHmac('sha256', secret).update(raw).digest('hex');
if (!timingSafeEqual(Buffer.from(expected), Buffer.from(sig))) return bad(401);
const event = JSON.parse(raw);
if (await seen(event.id)) return ok();                          // 24h dedupe
await queue.push(event);
return ok();                                                    // 2xx before slow work
```

- The signature covers the raw body. Parsing first changes the bytes and the digest fails.
- A receiver that returns 5xx gets retried for hours; accept, queue, then process.
- Replay the same event id twice in a test. A duplicate charge is the failure this prevents.

## failure

| status | meaning | action |
| --- | --- | --- |
| 400 | bad shape | fix the request, never retry |
| 401 | key invalid or expired | refresh, then report |
| 403 | scope missing | name the missing scope, do not widen silently |
| 404 | wrong id or path | verify, do not create a duplicate |
| 409 | duplicate or conflict | search before create |
| 429 | rate limited | honor `Retry-After`, resume from the checkpoint |
| 5xx | provider fault | retry twice with jitter, then fail loudly |

## decide

| condition | action |
| --- | --- |
| provider has no idempotency | dedupe locally on the natural key |
| price per call above the value | batch, cache, or drop the feature |
| webhook has no signature | poll instead, or verify at the edge |
| rate limit hit | backoff, queue, never hammer |
| terms forbid scraping | stop, ask for a licensed source |
| credential needed from the user | point to the secret store, never chat |
| automation touches money or mail | confirm before enabling |

## numbers

| item | value |
| --- | --- |
| retry | 3 attempts, 200ms doubling, full jitter |
| timeout | 20s per call, a total deadline per run |
| webhook | signature verified, dedupe 24h |
| cost | units logged per call, alert at 80% of budget |

## check

- [ ] key only in the secret store, absent from the repo
- [ ] timeout, retry cap and total deadline set
- [ ] webhook signature verified
- [ ] cost per run recorded

## stop

| condition | action |
| --- | --- |
| no key and no way to set one | report the blocker |
| terms unclear | ask before scraping |
| request to send mail or spend money | confirm the exact target and amount |
| provider deprecation announced | plan the migration, do not patch around it |

## emit

- integrations wired, with the endpoint and the scopes
- one measured call: latency, units, cost
- what was skipped and why
