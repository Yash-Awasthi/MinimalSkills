---
name: backend-api
description: >
  One standalone skill for backend and API engineering: API design and
  contracts (REST, GraphQL, gRPC, webhooks, events), databases (Postgres,
  MySQL, MongoDB, Redis, Neon, PlanetScale, Supabase, Convex, vector DBs),
  backend frameworks (FastAPI, Django, Laravel, NestJS, .NET, Rails, Express),
  ORMs (Prisma, Drizzle), auth and identity, payments, queues and background
  jobs, file storage, performance and shutdown, OpenAPI docs, contract
  testing, and authorized API security testing. Merges the backend-api class
  (218 skills) and the api deep pack (20). Fully self-contained: every
  procedure is inline, no external references.
metadata:
  merges: backend-api
  sources: 218
---

# backend-api

## 0. Iron laws (api pack contract — bind everything below)

1. **The contract is the artifact.** A schema, spec or signed agreement
   defines the interface. Generated types, a green build and a passing
   happy-path call are not proof the wire format still matches. Bind the
   exact contract and verify at the boundary.
2. **Add before you change.** Prefer a new field, endpoint or version over a
   modification that breaks an existing consumer. Hyrum's law: every
   observable behavior will be depended on, so undocumented behavior is part
   of the interface.
3. **Inspection does not send.** Reviewing a pasted request executes
   nothing; a verdict of "syntactically consistent" is not server
   acceptance, credential validity or authorization.
4. **Authorization gates every probe.** Any skill that attacks, fuzzes or
   scans starts with a mandatory confirmation gate: exact target URL, IP,
   account or resource; request-rate and concurrency budgets; stop
   conditions; out-of-scope surfaces — agreed before the first request.
5. **Retries are bounded and idempotent.** Parse `Retry-After` in both
   seconds and HTTP-date form, cap the delay, add jitter, stop at a
   deadline. Never replay a non-idempotent write. A semaphore caps
   concurrency, not requests per second — add a token bucket for real RPS.
6. **Token checks happen before claims.** Verify signature, algorithm,
   audience, issuer and expiry against the real identity provider. Never
   accept a caller-selected algorithm, never act on a decoded-but-unverified
   claim, never reuse an access token as a refresh token. Secrets stay in
   the approved store, out of code, logs and examples.
7. **Missing material fails closed.** A named reference the pack does not
   carry is resolved from its declared upstream or the claim is not made.
   Never fabricate the file.
8. **Numbers are targets or measurements.** Say whether a figure is
   illustrative, measured, or a provider statement; never turn a target into
   a result.
9. **Verification before completion.** The iron law: no "done" claim without
   a fresh command and its output.

## 1. API design and contracts

**Interface design** (and-interface-design, design-principles, patterns,
api-designer):
- Five rules: contract first; consistent error semantics; validate at
  boundaries; prefer addition over modification; predictable naming.
- Includes Hyrum's law, the one-version rule, resource design, cursor
  pagination, PATCH semantics, discriminated unions, and input/output
  separation.
- REST and GraphQL guide with a design checklist, REST template, best
  practices, GraphQL schema design and an implementation playbook — read
  only what the task needs.
- Patterns is a router over ten decision files: REST, GraphQL, tRPC,
  response formats, versioning, pagination, rate limiting, auth,
  documentation, security testing. Start from the content map; read only the
  relevant file. It teaches the decision, not a fixed copy.
- Designer: complete REST specification with CRUD plus domain actions, auth,
  pagination, request bodies, responses with status codes. Mark required and
  optional fields in prose tables or JSON Schema, not JSON comments.

**GraphQL** (graphql, graphql-architect, graphql-schema): schema-first
design; N+1 resolution watched with dataloaders; persisted queries for
public surfaces; schema patterns with project prerequisites stated.

**gRPC** (grpc-golang): service definition, streaming patterns, deadline
propagation, interceptors for auth and logging.

**Webhooks and events** (integration, integration-architect):
- Signed outbound webhooks with replay protection; inbound registration API;
  chaining; CloudEvents schemas; topics and queues; saga pattern; outbox
  pattern. Every step handles failure independently, uses an idempotency
  key, and retries with exponential backoff. A signature comparison uses a
  constant-time check, never `assert`.
- Integration architect: read schema, auth, rate limits and pagination
  before code; narrowest scope; secrets out of code; request body matches
  the schema; instrument the client; bound total deadlines and retry waits.

## 2. Building endpoints and clients

- **Endpoint builder**: scaffold route, validation, handler, auth, error
  shape, docs and a test. Validate before processing; auth on protected
  routes; the right status code; never expose sensitive fields. The example
  is Express — map the pattern to the project's actual stack.
- **SDK generator**: produces a draft client, not a finished library — base
  client, resource classes, typed errors, pagination, language idioms for
  Python and TypeScript. Retry only eligible operations inside a deadline;
  parse both `Retry-After` forms; never replay a non-idempotent write;
  always send a `User-Agent` naming the SDK and version. Production
  readiness needs the real contract, tests and target-language review.
- **Backend frameworks:**
  - **FastAPI** (fastapi-pro, fastapi-router-py, fastapi-templates,
    python-fastapi-development): Pydantic v2 validation at the edge;
    dependency injection for auth and DB sessions; async handlers for IO;
    routers per domain; project templates with tests and CI.
  - **Django** (django-pro, django-access-review, django-perf-review):
    access-control review investigates actual object-level permission
    checks (IDOR) rather than pattern-matching decorators; performance
    review reads query counts (`django-debug-toolbar`, `n+1` detection) with
    a stated review approach.
  - **Laravel** (laravel-expert, laravel-development-workflow): establish
    the contract first; Eloquent N+1 watched; form requests for validation;
    queues for slow work.
  - **NestJS** (nestjs-expert): modules, providers, DI; guards and
    interceptors; read the detailed guide before executing.
  - **.NET** (dotnet-backend, dotnet-architect, csharp-pro): ASP.NET Core
    minimal APIs or controllers; EF Core migration discipline; options
    pattern; enterprise API expertise.
  - **Rails** (new-rails-project): tech stack and guidance stated before
    scaffolding.
  - **Go** (golang-pro, boost-asio-pro, temporal-golang-pro, dbos-golang):
    idiomatic Go services; Asio-style async in C++ equivalents; Temporal Go
    SDK workflows deterministic with activities for IO; DBOS Go durability
    with reliability and version boundaries.
  - **Java/Kotlin/Spring** (java-pro, kotlin): layered architecture, beans
    for DI, transactions at the service boundary.
  - **PHP** (php-pro): modern PHP with types, PSR standards, composer.
  - **Python** (python-pro, python-development, python-development-python-
    scaffold): scaffolding with structure, tests, linting from the start.
  - **JavaScript/TypeScript** (javascript-pro): async patterns, error
    handling, module design.
  - **Rust/C/C++/C#/Ruby** (c-pro, cpp-pro, csharp-pro, ruby-pro): systems
    and service work with memory and concurrency discipline.
- **Convex** (convex, convex-backend): functions, schema, reactive queries;
  prerequisites before use.
- **Firebase** (firebase, firebase-app-platform): Auth/Firestore/Functions
  patterns; app platform prerequisites.
- **WordPress plugins / WooCommerce** (wordpress-plugin-development,
  wordpress-woocommerce-development): hooks, activation/deactivation
  lifecycle, nonces and capability checks; Woo cart/order hooks.
- **Discord/Telegram bots** (discord-bot-architect, telegram,
  telegram-bot-messaging, telegram-mini-app): Discord — slash commands,
  intents, sharding; Telegram — Bot API integration (Portuguese-canonical),
  messaging with a safety gate, Mini Apps with initData validation.
- **Microservices** (microservices-patterns in game-dev class; event-
  sourcing-architect): event sourcing — append-only event store, projections
  as rebuildable views, versioned events, upcasters; capabilities stated
  before use.

## 3. Databases

**Postgres** (postgresql, postgresql-optimization, postgres-best-practices,
supabase-postgres-best-practices, postgresql-devsec, postgres-readonly-
queries, postgresql-cli):
- Table design: normal until a measured reason not to; appropriate types
  (never store money in float); indexes for actual query patterns.
- Optimization workflow: EXPLAIN ANALYZE first; fix the plan (index, stats,
  query shape) before hardware; connection pooling (PgBouncer) for high
  churn.
- Supabase best practices: RLS policies on every table; service-role key
  server-side only; rule categories by priority.
- Read-only queries: declared execution boundary; requirements before
  running.
- psql: execution boundary and prerequisites stated.

**Managed Postgres** (neon-postgres, neon-postgres-branches, neon-functions,
neon-postgres-egress-optimizer, planetscale, claimable-postgres):
- Neon: serverless scaling, branching per environment (branch type decision
  first), functions, egress optimization with measurement and database
  boundaries.
- PlanetScale: branching and deploy requests; no foreign keys by default —
  enforce in the app layer.

**MySQL/MongoDB/Redis** (mysql, mongodb, redis, redis-cli, upstash-redis,
upstash-qstash, upstash-ratelimit):
- MySQL: InnoDB, indexing, EXPLAIN.
- MongoDB: document design, aggregation pipeline, indexes; prerequisites.
- Redis: data structures by use case (hash, set, sorted set, stream);
  TTLs; redis-cli with prerequisites; Upstash Redis serverless, QStash for
  message queues with signing, Ratelimit with sliding windows.

**Vector databases** (vector-database-ops, weaviate): comparison by
filtering, hybrid search and scale; Weaviate cloud instance operations.

**Database operations** (database, database-admin, database-architect,
database-design, database-optimizer, database-security, database-backups,
database-migration, database-migrations-sql-migrations):
- Workflow bundle routes design → build → optimize → secure → migrate.
- Admin: users, roles, least privilege; architect: schema design with
  selective reading rule — read only the relevant section.
- Optimizer: slow query log → EXPLAIN → index → verify.
- Security assessment: accounts, encryption, network exposure, audit
  logging (Chinese-canonical scope note).
- Backups: prerequisites stated; test restores, not just backups.
- Migrations: expand → migrate → contract; never destructive without a
  tested rollback; SQL migration strategy with stated compatibility
  windows.

**ORMs** (prisma-expert, drizzle-orm-expert): Prisma — schema-first, migrations
disciplined, `include`/`select` to avoid over-fetching; step 0 recommends the
specialist and stops when out of scope. Drizzle — SQL-like type-safe queries,
migration generation, relational queries.

## 4. Auth, identity and secrets

- **Clerk** (clerk-auth): hosted auth integration with session handling.
- **Identity federation** (identity-federation): SAML/OIDC/OAuth flows with
  scope notes (Chinese-canonical).
- **Connection auth rules** (connection-auth-rules-builder): declare auth
  rules for connections before use.
- **Azure authentication events** (microsoft-azure-webjobs-extensions-
  authentication-events-dotnet): supported events and installation.
- **Varlock** (varlock, varlock-claude-skill in engineering-craft): core
  principle — secrets never exposed; typed env access with leak detection.
- **MCP server security** (mcp-server-security): threat model, transport
  security, auth for MCP servers.

## 5. Payments and integrations

- **Stripe** (stripe-integration): webhook signature verification,
  idempotency keys, checkout vs payment intents, test clocks.
- **PayPal** (paypal-integration): supporting material availability
  declared when the upstream guide is absent.
- **Plaid** (plaid-fintech): bank linking with detailed guide.
- **Pakistan payments stack** (pakistan-payments-stack): authenticity and
  verification rules mandatory; verified context is public and high-level.
- **Payments received** (payments-received): register of incoming payments.
- **DoomPay** (doom-pay): checkout and payment verification with a runtime
  prerequisite.
- **x402** (x402-express-wrapper): HTTP 402 payment wrapper (Spanish-
  canonical procedure).
- **Nano settlement** (nano-settlement-verify): settlement verification
  before serving paid calls — one inline read-only script, no seed, no
  wallet.
- **Segment CDP** (segment-cdp): event tracking plan, identity resolution.
- **Twilio** (twilio-communications): SMS/voice with credentials in env.
- **Sendblue** (sendblue-cli): iMessage/SMS from the shell.
- **TextMe** (textme): messaging utility.
- **RestoSignals** (restosignals): restaurant signals integration.
- **ComfyUI Gateway** (comfyui-gateway): image-generation gateway.
- **Fal platform** (fal-platform): fal.ai API access.
- **Gemini API integration** (gemini-api-integration): server-side Gemini
  calls with key handling.
- **vLLM server** (vllm-server-management): version and exposure boundary —
  never expose an inference server publicly without auth.

## 6. Queues, jobs and reliability

- **BullMQ** (bullmq-specialist): principles and capabilities — job
  retry/backoff, rate limiting, priority, stalled-job detection, queues per
  concern.
- **Inngest** (inngest): event-driven functions with retries and
  concurrency controls.
- **Trigger.dev** (trigger-dev): background jobs with versioned tasks.
- **QStash** (upstash-qstash): HTTP message queues with signing.
- **DBOS Python** (dbos-python): durable execution — workflows idempotent,
  steps recorded; runtime boundaries stated.
- **Graceful shutdown** (graceful-shutdown): stop accepting, drain in-flight
  work, close connections, exit clean — SIGTERM handling in every service.
- **Cron doctor** (cron-doctor): audit scheduled jobs for overlap, failure
  alerting and idempotency.
- **Server management** (server-management, windows-server, gpu-server-
  management): process management principles and tool selection; Windows
  Server administration prerequisites; GPU server management with
  prerequisites.
- **App deploy** (appdeploy): first-time setup then deploy flow.

## 7. Performance and production

- **Performance** (performance-optimizer, performance-tuning,
  weather-pipeline-performance-diagnosis): optimization process — measure,
  identify the bottleneck, change one thing, re-measure; prerequisites
  stated before tuning; pipeline-specific diagnosis.
- **Production audit** (production-audit): configuration, logging, error
  handling, security headers, dependency versions.
- **Project state governor** (project-state-governor): mission and scope
  stated; governs what may change.
- **Cross-platform contract propagation audit**
  (cross-platform-contract-propagation-audit): verify a contract change
  propagated to every consumer platform.
- **jq** (jq): JSON querying and transformation from the shell.
- **File uploads** (file-uploads): principles and sharp edges — validate
  type/size, scan, store outside webroot, signed URLs for serving, never
  trust the filename.

## 8. API documentation and developer experience

- **Documentation four phases** (documentation): discovery → OpenAPI →
  developer guide with runnable examples → interactive docs.
- **Generators** (documentation-generator, documenter, openapi-spec-
  generation, openapi-spec-generator): from codebase — endpoints,
  parameters, schemas, auth, errors, examples for REST/GraphQL/WebSocket;
  OpenAPI 3.1 and AsyncAPI, portals, SDK generation, versioning and
  migration, developer-experience metrics. Spec generation with version and
  completeness boundaries.
- **Postman** (postman-collection-generator, postman-openapi-converter):
  extract API info into collections; convert OpenAPI to Postman with
  input validation.
- **Developer onboarding** (onboarding): target time-to-first-API-call.
  Simplify the auth flow without removing abuse controls; sandbox with
  deterministic test cards; try-it docs; measure each funnel step. TTFAC
  targets are illustrative, not benchmarks.

## 9. API testing and reliability

- **Analyzer** (analyzer): answers in one or two lines; checks method, URL,
  headers, body, auth and query parameters against the supplied contract;
  asks one question only when the answer would change the verdict; never
  executes the request; never infers server acceptance or credential
  validity from appearance.
- **Contract testing** (contract-testing): bind the contract and the
  affected clients; classify the change; build a small matrix; verify each
  boundary. Required fields, wrong types and explicit nulls are separate
  cases. Exercise the provider handler locally and pass its serialized
  output through the real consumer parser. A schema pass is not
  authorization or security proof; a malformed fixture is never coerced to
  match a defect.
- **Rate-limit handling** (rate-limit-handler): 429 and transient 5xx are
  retryable; 400/401/403/404 are terminal and need a request fix. Provider
  `Retry-After` wins over a computed delay. Proactive client limiter,
  idempotency key, deadline, jitter; never retry a non-idempotent write.
- **Mocks** (testing-observability-api-mock): scenario state, latency, error
  injection, fixture data so frontend and integration work run in parallel.
  Keep the mock honest to the contract; never let it drift into a second
  implementation.

## 10. API security (authorized use only)

- **security, security-testing, fuzzing-bug-bounty**: mandatory confirmation
  gate — exact target, request-rate and concurrency budgets, stop
  conditions, excluded surfaces. Ten-phase assessment: discovery,
  authentication, BOLA, IDOR, BFLA, GraphQL, input validation, business
  logic, WebSocket, rate limits, data exposure, CI integration. Do not
  expand the checklist into every attack automatically.
- **security-best-practices** (defensive): authenticate the exact token
  contract; verify before reading claims; authorize the resource and the
  operation separately; parse once and use the validated value; control
  abuse without claiming DDoS protection. Passwords checked against a
  breached list, passphrases supported. Secrets in the approved mechanism.
  Report any untested route, tenant path and failure mode.
- **Broken authentication** (broken-authentication): prerequisites and
  purpose stated before testing.
- **Django access review** (django-access-review): investigation over
  pattern matching for IDOR.
- **Database security** (database-security): accounts, encryption, network.
- **VMware vCenter** (vmware-vcenter-attack): evidence and scope stated;
  version fingerprinting first — authorized engagements only.
- **Anti-deception** (anti-deception): harness for detecting deceptive
  outputs with examples.

## 11. Domain specialists carried in this class

- **Research/data** (pubmed-database, uniprot-database, scanpy, biopython,
  radar-satellite-analysis, food-database-query): bundled upstream support
  with material availability declared; specialized data access with
  prerequisites. (Research and data-ml hubs carry the depth.)
- **Marketing fragments** (bounce-rate-estimator, page-speed-score-
  simulator, same-idea-both-platforms, creative-psychology-hooks, ux-
  persuasion-engineer, page-cro, form-cro, wechat-official-account-
  strategist, social-orchestrator, dev-to-hashnode, anywrite): CRO with
  evidence-first phases (Phase 0 evidence and constraints), persuasion with
  evidence and scope, cross-platform repurposing. (Marketing and design hubs
  carry the depth.)
- **Business/HR registers** (clients-accounts, payments-received, offers,
  credit-cycle-analysis, tds-booking-payment, alumni-re-hire-tracker,
  disciplinary-pip-tracker, mentorship-program, performance-management,
  project-based-performance, quality-nonconformance, junta-leiloeiros,
  leiloeiro-mercado): registers with evidence and action boundaries.
  (Business and people hubs carry the depth.)
- **Agent/tooling fragments** (bdi-mental-states, behavioral-modes,
  behavioral-xray, compile-knowledge, faf-expert, loop-library, looot,
  lognorm, altorank, cline-pilot, cowork-to-code-bridge, web-access,
  lead-signals, datawebot, bowmark, tweetapi, webly, satori, executing-
  plans, brainstorming, multi-agent-brainstorming, web-project-brainstorming,
  session-handoff, not-a-vibe-coder fragments, sharp-coder, logic-locate,
  dwarf-expert, m365-agents-dotnet, monopoly family): the MONOPOLY system
  design suite — design patterns deep dive, scale benchmarks and estimation
  formulas, security hardening checklist, technology decision matrix.
  (ai-agents hub carries agent depth.)
- **Coupons** (takeout-coupon, movie-coupon): coupon fetchers with
  redemption instructions. (Platform hub carries the set.)
- **Quit sponsor** (quit-sponsor): non-judgmental, evidence-informed,
  consented smoking-cessation support that escalates to human or clinical
  help — explicitly not medical care.
- **VR/AR** (vr-ar): platform selection first. (Mobile hub carries device
  depth.)
- **Fixing motion performance** (fixing-motion-performance): how-to-use
  stated. (Frontend hub carries the depth.)
- **NeverApply** (neverapply): US healthcare jobs MCP, read-only.

## 12. Output contract

- Name the skill, the API, and the environment in the first line of
  reasoning and in the todo list.
- Report the artifact: a spec path, an endpoint, a client file, a test
  result, a mock, or a request verdict.
- Keep routes, status codes, header names, field names, error strings and
  schema keys verbatim.
- State whether the work was static, run against a local fixture, or run
  against an authorized live target.
- Keep open work open: an untested route, a missing reference and an
  unverified claim are reported, never rounded up.
- Never print a token, key, session cookie or customer record; redact and
  name the rule.

## 13. Failure handling

| Situation | Response |
| --- | --- |
| A named reference file is missing | Fail closed; resolve from upstream or ask. Never fabricate. |
| A request would be sent to a live target | Confirm authorization and the exact target first. Inspection alone sends nothing. |
| A security test has no agreed scope | Stop at the confirmation gate. |
| A retry would replay a write | Do not retry unless documented idempotent. |
| A token claim not verified | Do not act on it; verify signature, algorithm, audience, issuer, expiry. |
| A contract test passes but the fixture is malformed | Fix the fixture; never coerce it to match a defect. |
| A number has no source | Label it illustrative, estimated, or a provider statement. |
| The evidence contradicts the requested design | Show the evidence and stop. |
| A migration is destructive without a rollback | Stop; write and test the rollback first. |
| A webhook signature compared non-constant-time | Fix to constant-time before shipping. |
| A mock drifted from the contract | Realign the mock; it is not a second implementation. |

## Provenance

Merged from the backend-api class (218 catalog skills) and the api curated
pack (20 sources). Every source skill's procedure, rule and policy is
represented above; duplicates collapsed to one canonical statement;
fail-closed and authorization gates preserved. No external file is required
to use this skill.
