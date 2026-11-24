# reliability

Load for queues, retries, idempotency, rate limits and failure handling.

## retry

| class | retry |
| --- | --- |
| 408, 429, 5xx | yes, with backoff |
| 400, 401, 403, 404, 422 | never |
| timeout | yes, if the operation is idempotent |
| connection reset before write | yes |

Backoff: exponential with full jitter, cap at 30s, max 3 attempts, total deadline enforced.

```ts
const delay = Math.min(30_000, 200 * 2 ** attempt) * Math.random();
```

## idempotency

- Key from the client, stored with the response, 24 hour window.
- Server-side dedupe on the natural key when the client cannot send one.
- A retried write must produce one effect. Test it: send the same request twice, assert one row.

## queues

- At-least-once delivery is the default; key the consumer on `(queue, message_id)` with a unique index, so a redelivery fails the insert instead of double-charging.
- Visibility timeout longer than the p99 handler time.
- Dead letter queue with an alarm. A DLQ nobody reads is a silent outage.
- One message shape, versioned. A schema change is a new queue version.

## backpressure

- Bound every queue and pool: set max concurrency and max depth, and reject with 429 past the depth instead of growing memory.
- Reject with 429 or 503 when saturated, do not queue without limit.
- Circuit breaker on every third-party call: open after N failures, half-open probe.

## timeouts

| hop | timeout |
| --- | --- |
| client to api | 10s |
| api to database | 2s statement, 5s connect |
| api to third party | 3s, below the client timeout |
| job handler | under the visibility timeout |

Every timeout is smaller than its caller's. Otherwise the caller gives up first and the work continues blind.

## rate limits

- Per key and per route class.
- Sliding window, stored in redis or the db.
- Return `X-RateLimit-Remaining` and `Retry-After`.

## graceful shutdown

1. Stop accepting new work.
2. Drain in-flight requests with a deadline.
3. Flush the queue consumer, commit offsets.
4. Close pools.

A process killed without drain loses in-flight work and duplicates the rest.
## queue index

| tool | the rule that matters |
| --- | --- |
| BullMQ | `attempts` with `backoff: { type: 'exponential', delay: 1000 }`; a job id is the idempotency key; `removeOnComplete` or Redis grows forever. |
| Inngest | Steps are memoized: `step.run` retries alone, a plain await re-runs the whole function on failure. |
| QStash | HTTP delivery with `Upstash-Retries`; a 2xx is required within the timeout or the message is retried. |
| DBOS Python | Workflows are durable: `@DBOS.workflow` replays from the last completed step, so steps must be idempotent. |
| Cron doctor | Every cron has an owner, a runtime budget, a failure alert and a last-success check; a silent cron is an outage. |
| Performance | Queue depth, age of the oldest message and consumer lag are the three metrics; p95 of the handler hides a growing backlog. |
| Project state governor | One write path per entity; a second writer (admin script, migration, cron) is how state diverges. |
| Cross-platform contract propagation | A schema change lands in the API, the client types, the queue payload and the docs in one PR, or the queue deserializes garbage. |
