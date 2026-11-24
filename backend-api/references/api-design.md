# api-design

Load when shaping or changing an HTTP or RPC contract.

## resource shape

```
GET    /v1/invoices?cursor=abc&limit=50
POST   /v1/invoices
GET    /v1/invoices/{id}
PATCH  /v1/invoices/{id}
DELETE /v1/invoices/{id}
POST   /v1/invoices/{id}/void
```

- Nouns in the path, verbs in the method. A sub-action is a sub-resource.
- Plural collections. Ids opaque, never sequential integers in a public api.
- Filter by query params, not by path segments.

## status codes

| code | use |
| --- | --- |
| 200 | read or update with a body |
| 201 | created, with `Location` |
| 202 | accepted, async work queued |
| 204 | no content |
| 400 | malformed or invalid input |
| 401 | no or bad credentials |
| 403 | authenticated, not allowed |
| 404 | not found, or hidden from this caller |
| 409 | state conflict, duplicate, stale version |
| 422 | semantically invalid |
| 429 | rate limited, with `Retry-After` |
| 500 | server fault, never a validation error |

## error body

```json
{ "error": { "code": "invoice_already_void", "message": "Invoice 42 is already void.", "details": [] } }
```

One error shape everywhere: `{"error":{"code":"rate_limited","message":"...","request_id":"..."}}`; clients branch on `code`, never on `message`.

## pagination

```json
{ "data": [], "next_cursor": "eyJpZCI6NDJ9", "has_more": true }
```

Cursor over offset: stable under inserts. Offset drifts and gets slower deep in the list.

## versioning

- Major in the path: `/v1/`. Minor changes are additive only.
- Additive: new optional field, new endpoint, new enum value behind a flag.
- Breaking: removed field, type change, new required field, changed default.
- Deprecation: announce, add `Deprecation` and `Sunset` headers, keep for a stated window.

## idempotency

```
POST /v1/payments
Idempotency-Key: 7c1f...
```

Store the key with the response for 24 hours. A replay returns the stored response. A key reused with a different body returns 409.

## rate limits

- Per key, not per ip, for authenticated traffic.
- Return the remaining budget in headers.
- Sliding window over fixed window: no burst at the boundary.

## docs

Openapi generated from the schema, not hand-written. Examples in the spec, tested in CI. A doc that drifts is worse than none.

## review

- Every endpoint has an auth decision written down.
- Every error branch has a code.
- No field added without a consumer.
## framework index

| stack | the rule that matters |
| --- | --- |
| FastAPI | `response_model` strips fields you did not declare; a `Depends` with `yield` runs cleanup after the response, so a commit there can fail silently. |
| Django | `select_related` for a forward FK, `prefetch_related` for many; `ATOMIC_REQUESTS` hides partial writes, prefer an explicit `transaction.atomic`. |
| Laravel | Form requests for validation, policies for authorization, `DB::transaction` around multi-write; `$fillable` or mass assignment opens. |
| NestJS | DTO with `class-validator`, `ValidationPipe({ whitelist: true })` drops unknown fields; a guard per controller, not per module. |
| Rails | Strong params, `includes` to kill N+1, `find_by` returns nil where `find` raises; a callback that writes is a hidden side effect. |
| Java/Kotlin/Spring | `@Transactional` on a public method through a proxy; a self-invocation skips the proxy and the transaction. |
| PHP | `declare(strict_types=1)`, PDO prepared statements, never `mysqli_real_escape_string` as the only defense. |
| Python | Type hints at the boundary, pydantic for input, `async def` for IO, a sync DB call inside an async handler blocks the loop. |
| JavaScript/TypeScript | Zod at the edge, `unknown` for input, `Promise.all` only for independent calls, abort on timeout. |
| Rust/C/C++/C#/Ruby | Rust: `Result` over panic in a handler. C: no fixed buffers. C#: `async` all the way. Ruby: `freeze` constants. |
| SDK generator | One OpenAPI file generates the client and the docs; a hand-written client drifts on the first schema change. |
| Microservices | One database per service; a shared table is a distributed monolith with extra network hops. |
| Convex | Queries are reactive and must be deterministic; a mutation is the only writer; `ctx.db.patch` not read-modify-write. |
| Firebase | Security rules are the authorization layer; a client SDK bypasses every check your API makes. |
| WordPress plugins / WooCommerce | Nonce on every form, `current_user_can` before a write, `$wpdb->prepare` for SQL. |
| Discord/Telegram bots | Verify the interaction signature, respond within 3 seconds, defer for slow work. |
| Clerk | `clerkMiddleware` sets `auth()`; check `userId` server-side, never trust a client-passed id. |
| Azure authentication events | Event Grid `Microsoft.Graph` change notifications carry a validation token you must echo. |
| Varlock | Secret manager wrapper: `varlock run --` injects env vars per command; never `console.log` the resolved map. |
| MCP server security | A tool description is untrusted input to the model; scope each tool to one action and validate arguments server-side. |

## docs index

| practice | the rule that matters |
| --- | --- |
| Documentation four phases | Reference, how-to, tutorial, explanation; a page that mixes two is unreadable at the moment of need. |
| Generators | OpenAPI to HTML, typedoc, sphinx; generated docs are never hand-edited, they regenerate on release. |
| Postman | A collection is a runnable contract; environment variables for host and token, tests on status and shape. |
| Analyzer | Spectral lints the OpenAPI file: operation ids, examples, error schema; a warning is a broken client. |
| Mocks | A mock server serves the examples; a client built against a mock that drifted from the schema fails in production. |
