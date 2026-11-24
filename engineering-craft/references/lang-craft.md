# lang-craft

Load when editing or porting code in a specific language. Apply the section for that language. Do not copy idioms across languages.

## python

- comprehensions and generators over manual append loops.
- `pathlib` over `os.path`. f-strings over `%` and `.format`.
- `dataclass(slots=True)` for records. `Enum` for closed sets.
- context managers for every resource.
- profile before optimizing: `python -m cProfile -s cumtime app.py`.
- package with `pyproject.toml`. `uv sync` and `uv run` for env and speed.
- type hints on public functions. `mypy --strict` or `pyright` in CI.

## typescript

- strict mode and `noUncheckedIndexedAccess` from the first commit; enabling it later surfaces hundreds of errors in code nobody is touching.
- discriminated unions over optional-field soup.
- `unknown` at boundaries, narrowed by guards. `any` is a defect.
- branded types for domain ids: `type UserId = string & { __brand: 'UserId' }`.
- exhaustive switch with a `never` check in the default.
- conditional, mapped and template-literal types only where they delete real duplication.
- prefer `satisfies` over annotation when the literal shape matters.

## javascript

- `const` default. No `var`.
- optional chaining and `??` over manual guards, but not to hide missing data.
- `structuredClone` over JSON round-trip.
- ESM only in new packages.

## go

- errors are values. Wrap with `%w`, check every one.
- small interfaces at the consumer, not the producer.
- goroutines need an owner and a shutdown path: `ctx`, `errgroup`, `WaitGroup`.
- channels for ownership transfer, mutexes for shared state.
- never leak a goroutine. Every `go` has a matching exit condition.
- `go vet ./...` and `staticcheck ./...` before review.

## rust

- prefer a borrow; a clone that outlives the function hides a lifetime the compiler was asking you to name.
- `Option`/`Result` with `?`. No `unwrap` outside tests.
- newtype for invariants: `struct Meters(f64)`.
- one async runtime. Structured concurrency with `JoinSet`.
- `select!` loops must be cancellation safe.
- `cargo clippy -- -D warnings` before review.

## java, kotlin

- streams for transforms, loops for control flow.
- records and data classes for data.
- `Optional` as a return, never a field.
- try-with-resources, `use {}` in kotlin.
- kotlin: coroutines with structured concurrency, state hoisted in compose.

## swift

- `guard let` early exit over nested `if let`.
- prefer a struct; a class shared across threads needs locking the value type does not.
- protocol-oriented at seams, concrete elsewhere.

## c, cpp

- every allocation has one owner and one free path.
- check every return. No `strcpy`, `sprintf`, `gets`.
- cpp: RAII, `std::unique_ptr` by default, `at()` where bounds are uncertain.
- build with warnings as errors: `-Wall -Wextra -Werror`.

## sql

- bind parameters only; concatenation turns a quote in a name into a second statement.
- index the columns in `where`, `join`, `order by`.
- `explain analyze` before claiming a query is fast.
- migrations reversible or explicitly marked one-way.

## review gate

```bash
npx tsc --noEmit
gofmt -l . && go vet ./...
cargo fmt --check && cargo clippy -- -D warnings
ruff check . && ruff format --check .
```

## stack index

| stack | the rule that matters |
| --- | --- |
| Dart | Sound null safety; `late` only for a field set in `initState`; `const` constructors on widgets. |
| Elixir/Erlang | Processes over shared state; `{:ok, v}` / `{:error, e}` tuples, never raise across a boundary; supervision tree restarts, so keep state out of the process. |
| Ruby | `frozen_string_literal: true`; blocks over loops; `!` only for the raising variant of a paired method. |
| Scala | `case class` for data, `sealed trait` for closed unions, exhaustive `match` or the compiler warns. |
| PHP | `declare(strict_types=1)`; PSR-4 autoload; typed properties; `??` over `isset()` chains. |
| React | State is a snapshot: derive, do not mirror; keys are ids; an effect that sets state from props is a render-loop smell. |
| Angular | Signals or `OnPush`; a subscription without `takeUntilDestroyed` leaks; `trackBy` on every `*ngFor`. |
| Bun | `bun install` respects the lockfile; `bun test` is Jest-compatible but `jest.mock` hoisting differs; `Bun.serve` replaces Express for a single-file API. |
| Electron | `contextIsolation: true`, `nodeIntegration: false`, IPC through a typed preload; never load remote content with node access. |
| Temporal | Workflows are deterministic: no `Date.now()`, no random, no direct IO. Activities do the side effects and are retried by policy. |
| ClickHouse | `ORDER BY` is the primary index, choose it for the common filter; `LowCardinality(String)` for enums; avoid `SELECT *` on wide tables. |
| Spark | Partition by the join key; a shuffle per stage; `broadcast()` a small dimension or the join spills. |
| Drizzle | Schema in TypeScript, migrations generated; `.$type<>()` for a branded column; relations are explicit, no lazy loading. |
| WordPress | Never edit core; a plugin's `add_action` priority decides order; escape on output (`esc_html`), sanitize on input. |
| Avalonia/Zafiro | `ReactiveUI` bindings with `WhenAnyValue`; `DataTemplates` for views; `Zafiro` adds shell navigation and dialogs. |
| Robius | Rust UI stack: `makepad-widgets` for rendering, `robius-authentication` for OAuth; async callbacks cross the FFI boundary through a runtime handle. |
| Qiskit | Circuits are immutable: `circuit.measure_all()` returns a new one unless in-place; transpile to the backend's basis gates before `run`. |
| CloudFormation | `DeletionPolicy: Retain` on stateful resources; a stack update that replaces a resource deletes data. |
| OpenTofu | Terraform-compatible, MPL licensed; `tofu init -upgrade` before a provider bump; state encryption is built in. |
| LangChain | Chains are deprecated in favor of LCEL (`prompt | model | parser`); a retriever without a score threshold returns noise. |
| Either | `left` is the error channel, `right` the value; map only the right; do not throw inside a chain. |
| TaskEither | Async Either: `TE.chain` for the next async step, `TE.orElse` to recover; a rejected promise escapes the type. |
| TaskEither is not a transaction | Two `TaskEither` calls are two operations; wrap them in one DB transaction or a partial write survives the failure. |
| Backend (fp-ts) | Decode at the edge with `io-ts`/`zod`, then keep `Either` internally; never leak `unknown` past the handler. |
| React (fp-ts) | Keep the FP core in plain modules; a hook returns `Either` and the component renders the error branch. |
| GDB | `gdb -p <pid>`, `bt full`, `frame N`, `p var`; `catch throw` to stop at the first exception; `info threads` before assuming single-threaded. |
| pstack/poteto | `pstack <pid>` for a native stack snapshot; poteto's style is one expression per line, no nested ternaries, no clever chains. |
| Functional TypeScript | `pipe` applies a value through steps, `flow` builds a reusable function; `Option` for absence, `Either` for errors, `TaskEither` for async errors. Pin fp-ts and TypeScript: a minor bump has broken type inference before. |
