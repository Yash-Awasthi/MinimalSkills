---
name: backend-api
description: Use when designing or changing a server API, persistence layer, auth, jobs or integrations: REST and RPC contracts, schema and migrations, sessions and scopes, queues and retries, rate limits, idempotency. Triggers: endpoint, migration, webhook, auth, queue.
---

# backend-api

## use when

- endpoint shape, status codes, versioning -> references/api-design.md
- schema, query, index, migration -> references/databases.md
- session, token, permission, secret -> references/auth-secrets.md
- queue, retry, idempotency, rate limit -> references/reliability.md
- payments, webhooks, third-party api -> references/payments.md

not for: deploy and infra (devops-cloud), client-side fetching (frontend-ui), datasets and models (data-ml)

## rules

- Conflict order: data integrity, then authorization, then latency; the first two are not tradeable.
- The contract is the schema. Validate at the boundary, type the rest; `as T` checks syntax, not shape.
- Authorize the record, not the route: fetch by id and compare the owner, or an id swap passes.
- A migration is expand then contract: add nullable, backfill in batches, deploy, then drop.
- A write is idempotent or carries an idempotency key with a 24h replay window.
- Retry only 429 and 5xx; 400, 401, 403, 404, 422 are terminal and need a request fix.
- Compare a token with `crypto.timingSafeEqual`, never `==`; no secret in code, log, error or body, and error text is a code.

## change

1. Locate: handler, request schema, migration, and every client that calls the route.
2. Propose the contract change with its status codes, and the alternative you rejected.
3. Predict before running: response shape per branch, query plan, migration duration on a copy.
4. Back up the original handler and schema in context, pinned to `git rev-parse HEAD`.
5. Apply one concern per edit; a validation change and an index change are two edits.
6. Verify: contract test per error code, `explain (analyze)` on the new query, migration up and down.
7. Regress: every client version, the stored idempotency replay and the webhook receiver.
8. Compare against the prediction; a changed status code you did not plan is a stop.
9. Report endpoints, migration and test exit status, then take the next item.

## endpoint

1. Name the resource and the operation. Verbs in the path only for a sub-action.
2. Define request schema, response schema and every error code.
3. Handler order: validate, authorize, act, return.
4. Test the happy path and each error branch.
5. Add the route to the openapi file.

```ts
const Body = z.object({ amount: z.number().int().positive(), note: z.string().max(280) });

export async function POST(req: Request) {
  const user = await requireUser(req);              // 401
  const parsed = Body.safeParse(await req.json());  // 400
  if (!parsed.success) return err('invalid_body', 400, parsed.error.issues);
  const invoice = await invoices.create({ ...parsed.data, ownerId: user.id });
  return json(invoice, 201);
}
```

Error body shape, every time: `{ "error": { "code": "invalid_body", "message": "amount must be positive", "requestId": "..." } }`. The message is for the developer, never a stack trace.

## auth

- Session cookie: `HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=604800`. No token in `localStorage`.
- Rotate the session id on login and on privilege change. A fixed id before and after login is session fixation.
- Access token 15 minutes, refresh token 30 days, refresh rotation with reuse detection.
- Check scope on the handler, ownership on the row. Two checks, two failure codes: 403 and 404.
- A 404 for a foreign id leaks less than a 403. Choose one and keep it consistent.
- Password reset: single-use token, 15 minute expiry, invalidate all sessions on use.

## webhook

```ts
const raw = await req.text();                       // before json parsing
const ok = crypto.timingSafeEqual(
  Buffer.from(hmac('sha256', secret, raw)),
  Buffer.from(req.headers.get('x-signature') ?? ''),
);
if (!ok) return err('bad_signature', 401);
const event = JSON.parse(raw);
await dedupe(event.id, () => handle(event));        // 24h window, stored result
return json({ received: true });                    // 200 fast, work in a queue
```

- Verify the signature on the raw body. Parsing first breaks the digest.
- Dedupe on the provider event id, not the payload hash.
- Return 2xx before slow work; a provider timeout triggers a retry storm.
- A failed handler goes to a dead letter queue with the event id, never silently dropped.

## query

1. Index the columns in `where`, `join`, `order by`, in selectivity order.
2. `explain (analyze, buffers)` before claiming a query is fast.
3. Kill N+1: one query with `in`, not a loop. Prisma `include`/`select`, not a per-row fetch.
4. Cursor pagination, never offset past 10k rows.
5. A count for a badge comes from a counter or an estimate, not `count(*)` on every render.

## migrate

```sql
-- expand, deploy, backfill, then contract in a later release
alter table invoices add column currency text;
update invoices set currency = 'USD' where currency is null;  -- batched, 5k rows per run
alter table invoices alter column currency set not null;      -- only after backfill is done
```

- One migration per release. A rename is add, copy, deploy, drop: three releases, zero downtime.
- The down migration runs on a copy before it runs on production.

## queue

- Retry with exponential backoff and jitter: 3 attempts, 30s cap, then dead letter.
- Visibility timeout longer than the job's p99, or a second worker takes the same job.
- A job carries its own idempotency key; a redelivered message must not double-charge.

## decide

| condition | action |
| --- | --- |
| breaking change | new version, old one with a sunset date |
| read heavy, same shape | cache with an explicit invalidation key |
| client retry on a write | idempotency key, stored response |
| task over 5s | accept 202, process in a queue |
| third-party call in the request path | 3s timeout, circuit break, no unbounded retry |
| error is the client's fault | 4xx with a code, never 500 |
| money involved | integer minor units, never float |
| duplicate webhook | dedupe on the event id |
| foreign id requested | 404, not 403, unless the api is internal |

## numbers

| item | value |
| --- | --- |
| pagination | cursor, 50 default, 200 max |
| idempotency window | 24h, replay returns the stored response |
| db statement timeout | 2s |
| third-party call | 3s, below the client timeout |
| retry | 3 attempts, jitter, 30s cap |
| rate limit | per key, sliding window |

## check

- [ ] input validated, unknown fields rejected
- [ ] authorization checked against the record owner
- [ ] error codes documented and tested
- [ ] index exists for every filter and sort
- [ ] migration runs forward and back on a copy
- [ ] webhook signature verified on the raw body
- [ ] no secret in the response: `rg -i "password|token|secret" src/`

## stop

| condition | action |
| --- | --- |
| schema change is destructive | ask for a migration plan |
| auth model unclear | ask before implementing |
| payment or pii in scope | confirm the compliance path |
| provider key missing | ask the owner to set it |

## emit

- endpoints changed with status codes
- migration files and rollback command
- tests run with exit status
