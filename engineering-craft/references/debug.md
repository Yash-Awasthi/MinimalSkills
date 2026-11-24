# debug

Load when a symptom exists and the cause does not.

## loop

1. Reproduce with one command. Record it and its exit status.
2. Freeze the tree: `git rev-parse HEAD`, `git status --porcelain`.
3. State a hypothesis as a prediction: "if X, then Y changes".
4. Test one variable. Log the result next to the hypothesis.
5. Fix the trigger. Add the regression test before the fix.
6. Re-run the reproduction, then the full suite.

Three failed hypotheses in a row means the model of the system is wrong. Re-read the code path from the entry point.

Keep the hypothesis log in the transcript, one line each:

```
H1  if the cache key omits the tenant, user B sees user A's row   -> not it, key includes tenant
H2  if the worker reuses a pooled connection after rollback      -> confirmed, pool returns dirty conn
```

A hypothesis that cannot be phrased as "if X then Y changes" is a guess; turn it into one or drop it.

## reproduce

- Shrink the input before reading code. Half the time the bug is in the part you delete.
- Fix the environment variables that matter: timezone, locale, `NODE_ENV`, feature flags, seed.
- Record the versions that reproduce: runtime, package lock hash, database, browser.
- If it only reproduces on one machine, diff the environment before diffing the code: `node -p process.versions`, `pip freeze`, `uname -a`, `printenv | sort`.
- A bug that reproduces once in ten runs is a race or a state leak. Run the reproduction 20 times and count.

## bisect

```bash
git bisect start HEAD v1.4.0
git bisect run pnpm vitest run src/parser.test.ts
```

Automate the predicate. A manual bisect with an unreliable test finds noise. The predicate must exit 0 for good and non-zero for bad, nothing else.

Input bisect: shrink the failing input by halves until removal stops the failure. Keep every shrunk case as a fixture.

Code-level narrowing when history is linear:

```bash
git log -S"discountRate" --oneline        # commits that changed the count of this string
git log -L 40,80:src/pricing.ts           # every change to this function body
git blame -L 40,80 src/pricing.ts         # who last touched each line, and in which commit
```

## by symptom

| symptom | first check |
| --- | --- |
| works locally, fails in CI | env vars, versions, timezone, case-sensitive paths |
| intermittent | shared mutable state, ordering, missing await, timer |
| slow after change | N+1 query, unbounded loop, sync IO on the hot path |
| memory grows | retained listeners, caches without eviction, closures |
| hangs | lock order, unbounded wait, missing cancellation |
| wrong value only sometimes | race, stale cache, float, timezone |
| fails only under load | connection pool size, file descriptor limit, thread starvation |
| fails after deploy only | config drift, migration not run, stale build artifact |
| fails only for one user | data shape, locale, permission, tenant routing |

## race

1. Assume the interleaving is legal until proven otherwise. "It cannot happen" is the bug report.
2. Widen the window artificially: add a sleep between the two operations, confirm the failure rate rises.
3. Log the ordering with a monotonic clock and a request id on every line, then sort by time.
4. Name the invariant that broke: "one row per (user, day)", "balance never negative".
5. Fix with the narrowest primitive that enforces the invariant: unique index, conditional update, single writer, or a lock held across both steps.
6. Remove the artificial sleep and run the reproduction 100 times.

## memory and crash

```bash
node --heapsnapshot-signal=SIGUSR2 app.js       # snapshot on demand, load in chrome devtools
valgrind --leak-check=full --show-leak-kinds=definite ./bin
heaptrack ./bin                                  # allocation flame graph
gdb -p 1234 -ex "thread apply all bt" -ex detach  # every thread, then leave the process alive
kubectl logs deploy/api --previous               # the container that died, not its replacement
```

- A crash loop shows the previous container's log, never the current one.
- An OOM kill leaves no stack: check the kernel log or the cgroup event, then look at the allocation curve.
- A leak with a flat heap graph is native memory, not javascript.

## tools

```bash
node --inspect-brk dist/main.js        # breakpoint at start
pytest -x --lf                          # stop on first, last failed
cargo run 2>&1 | head -40               # first failure, not the flood
strace -f -e trace=network ./bin        # syscall boundary
```

- Print at the boundary where data enters, not where it fails.
- Delete debug output before commit. A leftover print is a review block.
- Compare against a known-good revision with `git stash` before bisecting by hand.
- Prefer a debugger over ten prints when the state is large; prefer one print when the path is obvious.

## production

No reproduction available: work from evidence, not from guesses.

1. Bound the blast radius first: feature flag off, roll back, or shed load. Diagnosis after mitigation.
2. Pull the three timelines that matter: deploy time, error-rate onset, latency onset. A deploy inside the window is the first suspect.
3. Compare a failing request id across logs, traces and metrics. One request end to end beats a thousand aggregates.
4. Check the dependency edges before the code: database connections, queue depth, third-party status.
5. Fix forward only with a revert path already tested.

## stop

- No reproduction after two honest attempts: ask for input, version, env.
- Cause in a dependency: pin, patch or report upstream. Do not fork silently.
- Cause is a design flaw: state it, propose the smallest structural change, do not patch around it.
- Cause is data, not code: say so, name the rows, and add the constraint that makes the shape impossible.
