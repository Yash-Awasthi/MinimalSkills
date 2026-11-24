---
name: api
description: >-
  20 API skills for design, build, documentation, testing, and security. Covers interface
  and contract design, REST and GraphQL patterns, endpoint and SDK generation, webhook and
  event integration, OpenAPI and portal documentation, developer onboarding, request
  review, contract testing, rate limit and retry handling, realistic mocks, and authorized
  API security and fuzzing work. Use when a task designs, documents, tests, debugs,
  secures, or reviews an API, or when the user names an api skill.
metadata:
  curated_from: 20
  skills: 20
  groups: 5
---

# api

20 skills. 5 groups. One hub. Every source body is preserved verbatim in
`references/skills/<skill>.md`, and every non-SKILL.md file from a source pack sits at
the same relative path under `references/assets/<skill>/`. Load one body for the task.

`SOURCES.md` maps every source path to its canonical skill and group.
`references/INDEX.md` groups the links, `references/skills.tsv` carries every
description, and `references/GUIDE.md` holds the long-form group prose.

## Pack contract

**The contract is the artifact.** A schema, a spec, or a signed agreement defines the
interface. Generated types, a green build, and a passing happy-path call are not proof
that the wire format still matches. Bind the exact contract and verify at the boundary.

**Add before you change.** Prefer a new field, endpoint, or version over a modification
that breaks an existing consumer. Hyrum's law says every observable behavior will be
depended on, so treat undocumented behavior as part of the interface.

**Inspection does not send.** `analyzer` reviews a pasted request without executing it,
and contract tests run against local fixtures or an authorized environment. A verdict of
syntactically consistent is not server acceptance, credential validity, or authorization.

**Authorization gates every probe.** Any skill that attacks, fuzzes, or scans a target
starts with the mandatory confirmation gate and an exact target URL, IP, account, or
resource. Request-rate and concurrency budgets, stop conditions, and out-of-scope
surfaces are agreed before the first request.

**Retries are bounded and idempotent.** Parse `Retry-After` in both seconds and HTTP
date form, cap the delay, add jitter, and stop at a deadline. Never replay a
non-idempotent write without documented support. A semaphore caps concurrency, not
requests per second.

**Token checks happen before claims.** Verify the signature, the algorithm, the
audience, the issuer, and the expiry against the real identity provider. Never accept a
caller-selected algorithm, never act on a decoded-but-unverified claim, and never reuse
an access token as a refresh token. Keep secrets in the approved store and out of code,
logs, and examples.

**Missing material fails closed.** When a body names an external reference that the pack
does not bundle, resolve it from the declared upstream or a user installation, verify
its license, and read it before claiming the procedure was followed. Never fabricate the
file or substitute a same-named unrelated one.

**Numbers are targets or measurements.** An onboarding time, a latency budget, and a
rate limit are claims. Say whether a figure is illustrative, measured, or a provider
statement, and never turn a target into a result.

**Write clean as you draft.** Short declarative sentences. No em dash. A colon may
introduce a list and may not connect two clauses. Sentence case headings. No chatbot
framing, no generic closer.

## Routing

| The user wants | Group |
| --- | --- |
| An interface designed, a style chosen, or a contract reviewed | Design and contracts |
| An endpoint, SDK, or integration built or debugged | Build and generate |
| OpenAPI docs, a developer portal, or a faster first call | Documentation and onboarding |
| A request reviewed, a contract test, retry logic, or a mock | Testing and reliability |
| An authorized API assessment or fuzzing engagement | Security |

## Full roster

### Design and contracts

| Skill | What it does |
| --- | --- |
| [`and-interface-design`](references/skills/and-interface-design.md) | Designs stable REST, GraphQL, module, and prop interfaces with Hyrum's law, one version, contract first, and additive change. |
| [`design-principles`](references/skills/design-principles.md) | Covers REST and GraphQL design for intuitive, scalable APIs, with a checklist, a REST template, and a GraphQL reference set. |
| [`designer`](references/skills/designer.md) | Generates a full REST endpoint specification with CRUD, auth, pagination, and realistic bodies, and states its missing external references. |
| [`patterns`](references/skills/patterns.md) | Chooses REST, GraphQL, or tRPC and settles versioning, pagination, errors, auth, and rate limits from a selective reading map. |

### Build and generate

| Skill | What it does |
| --- | --- |
| [`endpoint-builder`](references/skills/endpoint-builder.md) | Scaffolds a reviewable REST endpoint with route, input validation, handler, auth, errors, docs, and a test example. |
| [`integration`](references/skills/integration.md) | Designs webhooks, API chaining, event streams, outbox, and sagas with signatures, idempotency, backoff, and dead letters. |
| [`integration-architect`](references/skills/integration-architect.md) | Designs, implements, and debugs an API client from the contract, with least privilege, bounded retries, and observability. |
| [`sdk-generator`](references/skills/sdk-generator.md) | Drafts a typed client SDK with base client, resource classes, error types, pagination, retries, and a User-Agent header. |

### Documentation and onboarding

| Skill | What it does |
| --- | --- |
| [`documentation`](references/skills/documentation.md) | Runs a four-phase documentation workflow from API discovery to OpenAPI, developer guide, runnable examples, and interactive docs. |
| [`documentation-generator`](references/skills/documentation-generator.md) | Generates endpoint documentation from a codebase: parameters, schemas, auth, errors, and request and response examples. |
| [`documenter`](references/skills/documenter.md) | Builds OpenAPI 3.1 and AsyncAPI docs, interactive portals, SDKs, versioning notes, and developer onboarding. |
| [`onboarding`](references/skills/onboarding.md) | Lowers time-to-first-API-call by simplifying auth, adding a sandbox, and removing the documented onboarding failure points. |

### Testing and reliability

| Skill | What it does |
| --- | --- |
| [`analyzer`](references/skills/analyzer.md) | Checks a pasted request against its contract in one line and never sends it or infers server acceptance. |
| [`contract-testing`](references/skills/contract-testing.md) | Turns an API change into provider and consumer wire-level checks, covering required fields, types, nulls, and error mapping. |
| [`rate-limit-handler`](references/skills/rate-limit-handler.md) | Handles 429 and transient 5xx with Retry-After, bounded jittered backoff, idempotency keys, and proactive client limits. |
| [`testing-observability-api-mock`](references/skills/testing-observability-api-mock.md) | Builds realistic mock services with scenario state, latency, failures, and contract fixtures for parallel development. |

### Security

| Skill | What it does |
| --- | --- |
| [`fuzzing-bug-bounty`](references/skills/fuzzing-bug-bounty.md) | Authorized API fuzzing and bug bounty technique for REST, SOAP, and GraphQL, including IDOR and auth bypass, behind a gate. |
| [`security`](references/skills/security.md) | Runs an authorized ten-phase API assessment across REST, GraphQL, WebSocket, and SOAP, behind a mandatory confirmation gate. |
| [`security-best-practices`](references/skills/security-best-practices.md) | Hardens the request boundary: token verification, resource authorization, one validated parse, abuse control, secrets, and logs. |
| [`security-testing`](references/skills/security-testing.md) | Runs an authorized API security workflow across discovery, authentication, authorization, input validation, and rate limits. |

## Group notes

### Design and contracts

`and-interface-design` covers REST, GraphQL, module boundaries, and component props with
five rules. Contract first, consistent error semantics, validate at boundaries, prefer
addition over modification, and predictable naming. It includes Hyrum's law, the
one-version rule, resource design, cursor pagination, PATCH semantics, discriminated
unions, and input and output separation.

`design-principles` is the broad REST and GraphQL guide. It ships
`assets/api-design-checklist.md`, `assets/rest-api-template.py`,
`references/rest-best-practices.md`, `references/graphql-schema-design.md`, and
`resources/implementation-playbook.md`, and says to read only what the task needs.

`patterns` is a router over ten decision files: REST, GraphQL, tRPC, response formats,
versioning, pagination, rate limiting, auth, documentation, and security testing. Start
from the content map and read only the relevant file. Its
`references/assets/patterns/scripts/api_validator.py` backs the example validation step.
It teaches the decision, not a fixed copy.

`designer` produces a complete REST specification with CRUD plus domain actions, auth,
pagination, request bodies, and responses with status codes. Mark required and optional
fields in prose tables or JSON Schema, not in JSON comments. Two support paths,
`references/domains.md` and `references/testmu_example.md`, are not bundled. Resolve them
from the LambdaTest upstream or a user installation, and do not claim the procedure ran
until the file exists.

### Build and generate

`endpoint-builder` scaffolds route, validation, handler, auth, error shape, docs, and a
test. Validate before processing, require auth on protected routes, return the right
status, and never expose sensitive fields. Its example is JavaScript and Express, so map
the pattern to the project's actual stack.

`sdk-generator` produces a draft client, not a finished library. Base client, resource
classes, typed errors, pagination, and language idioms for Python and TypeScript. Retry
only eligible operations inside a deadline, parse both `Retry-After` forms, and never
replay a non-idempotent write. Always send a `User-Agent` that names the SDK and version.
Production readiness needs the real contract, tests, and target-language review.

`integration` designs the connections between systems. Signed outbound webhooks with
replay protection, an inbound registration API, chaining, CloudEvents schemas, topics
and queues, the saga pattern, and the outbox pattern. Every step handles failure
independently, uses an idempotency key, and retries with exponential backoff. A signature
comparison uses a constant-time check, never `assert`.

`integration-architect` is the delivery counterpart. Read schema, auth, rate limits, and
pagination before code. Use the narrowest scope, keep secrets out of code, match the
request body to the schema, and instrument the client. Its semaphore template caps
concurrency, so add a token bucket or scheduler for a real RPS limit, and bound total
deadlines and retry waits.

### Documentation and onboarding

`documentation` runs discovery, OpenAPI, developer guide, runnable examples, and
interactive docs as four phases. `documentation-generator` works from a codebase and
covers endpoints, parameters, schemas, auth, errors, and examples for REST, GraphQL, and
WebSocket. `documenter` goes further: OpenAPI 3.1 and AsyncAPI, portals, SDK generation,
versioning and migration, and developer experience metrics.

`onboarding` targets time-to-first-API-call. Simplify the auth flow without removing
abuse controls, provide a sandbox with deterministic test cards, add try-it docs, and
measure each funnel step in your own product. The TTFAC targets in the body are
illustrative, not benchmarks.

### Testing and reliability

`analyzer` answers in one or two lines. It checks method, URL, headers, body, auth, and
query parameters against the supplied contract, and asks one question only when the
answer would change the verdict. It never executes the request, and it never infers
server acceptance or credential validity from appearance.

`contract-testing` binds the contract and the affected clients, classifies the change,
builds a small matrix, and verifies each boundary. Required fields, wrong types, and
explicit nulls are separate cases. Exercise the provider handler locally and pass its
serialized output through the real consumer parser. A schema pass is not authorization
or security proof, and a malformed fixture is never coerced to match a defect.

`rate-limit-handler` classifies each response. 429 and transient 5xx are retryable,
while 400, 401, 403, and 404 are terminal and need a request fix. Provider
`Retry-After` wins over a computed delay. Add a proactive client limiter, an idempotency
key, a deadline, and jitter, and never retry a non-idempotent write.

`testing-observability-api-mock` builds mocks with scenario state, latency, error
injection, and fixture data so frontend and integration work can run in parallel. Keep
the mock honest to the contract, and do not let a mock drift into a second
implementation.

### Security

`security`, `security-testing`, and `fuzzing-bug-bounty` are authorized-use only and
open with the same mandatory confirmation gate. State the exact target URL, IP, account,
or resource. Agree request-rate and concurrency budgets, stop conditions, and excluded
surfaces. The ten-phase assessment covers discovery, authentication, BOLA, IDOR, BFLA,
GraphQL, input validation, business logic, WebSocket, rate limits, data exposure, and CI
integration. Do not expand the checklist into every attack automatically.

`security-best-practices` is the defensive review. Authenticate the exact token contract,
verify before reading claims, authorize the resource and the operation separately, parse
once and use the validated value, and control abuse without claiming DDoS protection.
Passwords are checked against a breached list and support passphrases. Secrets stay in
the approved mechanism. Report any untested route, tenant path, and failure mode.
## Output contract

- Name the skill, the API, and the environment in the first line of your reasoning and in the todolist.
- Report the artifact. A spec path, an endpoint, a client file, a test result, a mock, or a request verdict.
- Keep routes, status codes, header names, field names, error strings, and schema keys verbatim.
- State whether the work was static, run against a local fixture, or run against an authorized live target.
- Keep open work open. An untested route, a missing reference, and an unverified claim are reported, never rounded up.
- Never print a token, key, session cookie, or customer record. Redact it and name the rule.
- Write through `unslop`. Short declarative sentences, sentence case headings, no em dash, no colon connecting two clauses, no chatbot framing.

## Failure handling

| Situation | Response |
| --- | --- |
| A named reference file is missing | Fail closed. Resolve it from the declared upstream or ask. Never fabricate it. |
| A request would be sent to a live target | Confirm authorization and the exact target first. Inspection alone sends nothing. |
| A security test has no agreed scope | Stop at the confirmation gate. Agree target, budgets, and stop conditions. |
| A retry would replay a write | Do not retry unless the operation is documented idempotent. |
| A token claim has not been verified | Do not act on it. Verify signature, algorithm, audience, issuer, and expiry. |
| A contract test passes but the fixture is malformed | Fix the fixture. Never coerce it to match a defect. |
| A number has no source | Label it illustrative, estimated, or a provider statement. |
| The evidence contradicts the requested design | Show the evidence and stop. |

## Provenance

20 `sickn33-api-*` source directories became 20 canonical skills in 5 groups. Each source
had one body, so no merge or variant resolution was needed. Every body is verbatim at
`references/skills/<skill>.md` with its original frontmatter removed, and every other
file from a source pack is copied under `references/assets/<skill>/` at the same relative
path. 21 asset files totaling 115,832 bytes were copied, including the API design
checklist and REST template, the GraphQL and REST references with the implementation
playbook, the ten API pattern decision files and `api_validator.py`, the endpoint builder
README, the onboarding README, the mock playbook, and the JWT/OAuth and REST/GraphQL
testing references.

`api-designer` names two support paths that are not bundled. The body says so and points
at the LambdaTest upstream, and the pack keeps that statement rather than inventing the
files. Three security skills carry an authorized-use gate and a mandatory confirmation
gate, and the pack keeps both.

Upstream collection `sickn33`. Original catalog paths are preserved in `SOURCES.md` and
under `_archive/api/catalog/`.
