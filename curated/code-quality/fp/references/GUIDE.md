# fp guide

The long-form group prose and the full roster. `SKILL.md` is the loadable hub, and
`references/skills/<skill>.md` is the verbatim body to follow for one task.

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
