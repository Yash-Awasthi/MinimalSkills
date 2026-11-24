---
name: fp
description: >-
  15 functional TypeScript skills built around fp-ts. Covers the pragmatic 80/20 entry
  point, pipe and flow, the type decision card, Option and Either references, TaskEither
  async pipelines, error handling as values, everyday data transforms, backend services
  with ReaderTaskEither and functional dependency injection, React integration, and a
  refactor path from imperative code. Use when a task writes, refactors, reviews, or
  teaches fp-ts or functional TypeScript, or when the user names an fp skill.
metadata:
  curated_from: 15
  skills: 15
  groups: 6
---

# fp

15 skills. 6 groups. One hub. Every source body is preserved verbatim in
`references/skills/<skill>.md`, and every non-SKILL.md file from a source pack sits at
the same relative path under `references/assets/<skill>/`. Load one body for the task.

`SOURCES.md` maps every source path to its canonical skill and group.
`references/INDEX.md` groups the links, `references/skills.tsv` carries every description,
and `references/GUIDE.md` holds the long-form group prose.

## Pack contract

**Pin fp-ts, TypeScript, the framework, and the client.** The bodies are excerpts, not a
compiled package. They omit application types and helpers, and a snippet that type-checks
in isolation may not compile against the installed versions. Record the versions and
verify the imports before presenting code.

**A type is not a runtime check.** `Either`, `Option`, and `TaskEither` track values the
code actually produced. A JSON parse or an `as T` assertion checks syntax or satisfies the
compiler, not the shape. Decode unknown input with a real schema at the boundary. A thrown
exception or a rejected promise still needs handling unless an adapter wrapped it.

**TaskEither does not make a workflow transactional.** A pipeline over a database, an
inventory check, a payment, and a shipment is not a transaction or a saga. Keep the
uniqueness constraint, use durable or provider idempotency, and reconcile an ambiguous
charge. A failure value in the middle does not roll back work that already happened.

**Do not hide an authorization failure behind a default.** A fallback user or a default
branch on an authentication or authorization check is a security defect. Return the
failure and let the caller deny. Retry only a transient idempotent operation, with a bound
and a backoff.

**Prefer the plain construct when it is clearer.** The pragmatic bodies say so. A single
null check, a simple loop, hot performance code, and a team that does not know fp-ts are
all reasons to stay imperative. Functional style is a tool, not a requirement, and a
rewrite needs a measured reason.

**React integrations are sketches.** The React bodies are untested integration sketches.
Effects in render, stale closures, strict-mode double runs, and server and client
boundaries are real. Decode external data, place effects deliberately, and test the
lifecycle before adopting a hook pattern.

**Node and Deno are not interchangeable.** Deno needs explicit npm and runtime
configuration, and Node APIs are not portable by default. Check the target runtime before
copying a backend example, and keep the Prisma and framework versions in view.

**Bundled guides are the source of truth.** Ten skills point at a detailed guide that is
bundled under `references/assets/<skill>/`. Read it before executing the skill. It retains
the full procedure, and its safety, prerequisite, and validation rules are mandatory. The
short body is a summary, not the whole method.

**Duplicate pairs stay.** `pragmatic` and `ts-pragmatic`, `errors` and `ts-errors`, and
`react` and `ts-react` carry near-identical content under two names. Each source is a
separate skill and stays verbatim, so pick the name the user or project expects. Never
merge the pair or drop one silently.

**One file per skill.** The body is a reference card or a guide. Report the pattern, the
type, and the boundary. A type signature is not a tested implementation.

**Write clean as you draft.** Short declarative sentences. No em dash. A colon may
introduce a list and may not connect two clauses. Sentence case headings. No chatbot
framing, no generic closer.

## Routing

| The user wants | Group |
| --- | --- |
| A first look at functional TypeScript, or a pipe, flow, or type choice | Core concepts |
| A nullable value or a synchronous fallible operation | Option and Either |
| An async pipeline or a TaskEither question | Async and TaskEither |
| Errors handled as values instead of thrown | Error handling |
| Array and object transforms, or a backend service | Data and backend |
| fp-ts in React, or a migration from imperative code | React and refactoring |

## Full roster

### Core concepts

| Skill | What it does |
| --- | --- |
| [`pipe-ref`](references/skills/pipe-ref.md) | A short reference for pipe and flow, covering value transformation, reusable pipelines, typed use, and the common composition pattern. |
| [`pragmatic`](references/skills/pragmatic.md) | The 80/20 entry point to functional programming in TypeScript, with plain explanations and an explicit list of cases where ordinary code is better. |
| [`ts-pragmatic`](references/skills/ts-pragmatic.md) | The fp-ts branded copy of the pragmatic guide, with the same 80/20 approach and the same stop conditions for simple code. |
| [`types-ref`](references/skills/types-ref.md) | A decision card for Option, Either, Task, TaskEither, and related fp-ts types, plus common imports and one-line patterns. |

### Option and Either

| Skill | What it does |
| --- | --- |
| [`either-ref`](references/skills/either-ref.md) | A short reference for Either: create, transform, extract, common validation patterns, and the comparison with try/catch. |
| [`option-ref`](references/skills/option-ref.md) | A short reference for Option: create, transform, extract, common nullable patterns, and the comparison with plain nullable values. |

### Async and TaskEither

| Skill | What it does |
| --- | --- |
| [`async`](references/skills/async.md) | Builds async pipelines with TaskEither for fetch, database, and file work, replacing nested try/catch with typed, composable failure. |
| [`taskeither-ref`](references/skills/taskeither-ref.md) | A short reference for TaskEither, including its lazy shape, creation, transforms, execution, and the comparison with async/await. |

### Error handling

| Skill | What it does |
| --- | --- |
| [`errors`](references/skills/errors.md) | Treats errors as values with Either and TaskEither, with the type and side-effect boundaries that the pattern does not cover. |
| [`ts-errors`](references/skills/ts-errors.md) | The fp-ts branded copy of the error-as-value guide, with the same JSON decoding and authorization warnings. |

### Data and backend

| Skill | What it does |
| --- | --- |
| [`backend`](references/skills/backend.md) | fp-ts backend patterns for Node.js and Deno with ReaderTaskEither, functional dependency injection, Prisma, and version-scoped caveats. |
| [`data-transforms`](references/skills/data-transforms.md) | Everyday array, object, grouping, aggregation, and null-safe transformations, shown imperative first and functional second with honest trade-offs. |

### React and refactoring

| Skill | What it does |
| --- | --- |
| [`react`](references/skills/react.md) | fp-ts with React across hooks, state, forms, and data fetching, as untested integration sketches that require lifecycle and decoding checks. |
| [`refactor`](references/skills/refactor.md) | A staged migration from imperative TypeScript to fp-ts, with pattern selection, incremental steps, and a tested boundary for each change. |
| [`ts-react`](references/skills/ts-react.md) | The fp-ts branded React copy, with the same hook and lifecycle caveats and the same requirement to validate external JSON. |

## Group notes

### Core concepts

`pragmatic` is the entry point. It explains what matters without category theory, then
lists the cases where functional style is the wrong tool. Plain null checks, simple loops,
performance-critical code, and a team without fp-ts experience are all stop signs. Read
this before a broad rewrite.

`ts-pragmatic` is the same guide under the fp-ts name. The two bodies carry the same
advice and the same exclusions, so use the name the project references.

`pipe-ref` covers composition. `pipe` applies a value through a sequence, `flow` builds a
reusable function, and both work with the fp-ts types. It is a reference card, not a
tutorial.

`types-ref` is the decision card. It maps a task to `Option`, `Either`, `Task`, or
`TaskEither`, lists common imports, and shows one-line patterns and a pattern match.
Choose the type from the effect and the failure mode, not from habit.

### Option and Either

`option-ref` covers a value that may not exist. `Some` and `None`, creation, transform,
extract, common patterns, and the comparison with plain nullable values. `Option` removes
repeated null checks, but it does not validate a decoded shape.

`either-ref` covers a synchronous operation that can fail. `Right` and `Left`, creation,
transform, extract, validation patterns, and the comparison with try/catch. Keep the error
type meaningful, and do not collapse distinct failures into one string.

### Async and TaskEither

`async` builds the async pipeline. `TaskEither` as an async operation with tracked
failure, a fetch wrapper, database work with Prisma, and file operations. Replace nested
try/catch with a composable chain, and keep the boundary where a real exception can still
escape. A pipeline is not a transaction, so preserve the constraints and the idempotency
keys behind the calls.

`taskeither-ref` is the reference card. Its shape is lazy, `() => Promise<Either<E, A>>`,
so construction does nothing until execution. Creation, transform, execute, common
patterns, and the comparison with async/await.

### Error handling

`errors` and `ts-errors` teach errors as values. The same guide appears under two names.
The type and side-effect boundaries are the important part. Decode unknown JSON with a
schema, never use a default user for an auth failure, and retry only a transient idempotent
operation. Read the bundled guide for the full procedure.

### Data and backend

`data-transforms` covers the everyday work. Arrays, object reshaping, API normalization,
grouping, aggregation, and null-safe access. Each section shows the imperative form first
and the functional equivalent second, then says when each one wins. Native methods are
often the right answer, and the body says so.

`backend` is the service layer. `ReaderTaskEither`, functional dependency injection, a
Prisma example, and Node and Deno caveats. Pin fp-ts, TypeScript, the framework, and Prisma.
The excerpts are not a compiled package, and Deno needs its own npm and runtime setup.

### React and refactoring

`react` and `ts-react` apply fp-ts to React. Hooks, state, forms, and data fetching, as
untested integration sketches. Validate external JSON, respect the lifecycle, and verify
the server and client boundary. The two bodies are near-identical, so use the project's
name.

`refactor` is the migration path. Choose the pattern, change one boundary at a time, keep
the tests green, and measure the result. Do not convert a whole codebase in one pass, and
do not adopt fp-ts where the pragmatic guide says plain code is better.
## Output contract

- Name the skill, the fp-ts and TypeScript versions, and the function or module in the first line of your reasoning and in the todolist.
- Report the artifact. A function, a type, a pipeline, a decoded boundary, a refactor step, or a reference answer.
- Keep type names, operators, import paths, and error shapes verbatim.
- State the runtime and framework, and whether the snippet was compiled or only sketched.
- State which boundary decodes unknown input and which failure paths were tested.
- Keep open work open. An uncompiled sketch, an untested lifecycle, and an unhandled rejection are reported, never rounded up.
- Never print a secret, a token, or personal data from a payload. Redact it and name the rule.
- Write through `unslop`. Short declarative sentences, sentence case headings, no em dash, no colon connecting two clauses, no chatbot framing.

## Failure handling

| Situation | Response |
| --- | --- |
| A snippet was never compiled | Say so. Verify the imports and versions before calling it working code. |
| A cast stands in for a runtime check | Decode the input with a schema at the boundary. |
| A TaskEither chain is treated as a transaction | Keep the constraint and the idempotency key. A failure value does not roll back work. |
| An auth failure falls back to a default user | Return the failure and deny. Never mask it. |
| A retry targets a non-idempotent write | Do not retry without a duplicate-safe contract. |
| An fp-ts rewrite adds no measured value | Prefer the plain construct. The pragmatic guide says so. |
| A React hook pattern is untested | Test the lifecycle and the strict-mode path, or label it a sketch. |
| A Deno example copies a Node API | Check the target runtime and configure it explicitly. |
| The evidence contradicts the requested claim | Show the evidence and stop. |

## Provenance

15 `sickn33-fp-*` source directories became 15 canonical skills in 6 groups. Each source
had one body, so no merge or variant resolution was needed. Every body is verbatim at
`references/skills/<skill>.md` with its original frontmatter removed, and every other
file from a source pack is copied under `references/assets/<skill>/` at the same relative
path. 10 asset files totaling 254,329 bytes were copied, all detailed guides. The five
short reference cards, `either-ref`, `option-ref`, `pipe-ref`, `taskeither-ref`, and
`types-ref`, ship no extra files.

The canonical name drops the `sickn33-fp-` prefix, so `sickn33-fp-async` becomes `async`
and `sickn33-fp-data-transforms` becomes `data-transforms`.

Three pairs are near-duplicates under two names. `pragmatic` and `ts-pragmatic`,
`errors` and `ts-errors`, and `react` and `ts-react`. Each is a separate source with its
own frontmatter and description, so each stays as its own canonical skill. The bodies
carry the same caveats, including the JSON decoding rule, the default-user warning for
auth failures, and the untested React sketch note.

Every body warns that the code is an excerpt or an integration sketch, not a compiled
package. The pack keeps that statement. Where a detailed guide is named, it is bundled
under the skill's asset folder, and the body says its safety and validation rules are
mandatory.

Upstream collection `sickn33`. Original catalog paths are preserved in `SOURCES.md` and
under `_archive/fp/catalog/`.
