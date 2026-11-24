# test

Load when designing tests, triaging a flaky test, or deciding what to cover.

## loop

1. Write the failing test. Run it. Confirm the failure message is the expected one.
2. Write the smallest code that passes.
3. Refactor with the test green.
4. Commit the test with the change.

A test that has never failed proves nothing: break the code once, watch it go red, then restore it.

## layer choice

| layer | scope | speed | use for |
| --- | --- | --- | --- |
| unit | one function, no IO | ms | branching, parsing, math |
| integration | module + real dependency | 100ms-2s | queries, handlers, queues |
| contract | provider vs consumer | 1s | API shape between services |
| e2e | browser or device, real stack | 10s+ | 3-5 critical journeys |

Test behavior through the public interface. A test that breaks on rename is testing structure.

## naming

```
describe('parseInvoice')
  it('rejects a trailing comma')
  it('keeps cents as integers')
```

Name the input and the expected outcome. `works` and `test1` carry nothing.

## flake triage

```bash
for i in $(seq 1 100); do pnpm vitest run path.test.ts || echo "fail $i"; done
```

| cause | signal | fix |
| --- | --- | --- |
| time | fails near midnight or DST | inject a clock |
| order | fails alone, passes in suite | remove shared state |
| async | fails under load | await the real condition, not a sleep |
| network | fails on CI only | stub the boundary, keep one real call |
| random | port, temp path, uuid collision | allocate per test |

Quarantine after a 1% failure rate over 100 runs. File the cause. Do not retry into green.

## fixtures

- One factory per domain object, overridable per field.
- No shared mutable fixture between tests.
- Snapshot only stable, human-reviewed output. Regenerate with a diff read, never blind.
- Time, randomness and ids are injected, not patched globally.

## coverage

- Gate changed lines, not the repository total.
- 100% on parsers, money math, auth decisions.
- Skip coverage theater on generated code, type declarations and glue.

## commands

```bash
pnpm vitest run --coverage
pytest -x -q --cov=app --cov-report=term-missing
go test ./... -race -count=1
cargo test --all-features
```

`-count=1` and `--no-cache` matter: a cached pass is not a run.

## browser e2e

- Playwright over Cypress: parallel by default, one context per test, trace on first retry.

```bash
npx playwright test --trace on-first-retry --reporter=line
```

- Select by role and name: `page.getByRole('button', { name: 'Approve' })`. A class selector breaks on the next redesign.
- No `waitForTimeout`. Wait on state: `await expect(row).toHaveCount(3)`.
- Log in once per worker with `storageState`, not through the UI per test.
- Seed the database through an API, not by clicking through setup.
- A test that fails only in CI: check viewport, locale, timezone and font loading first.
- Keep `trace.zip`, screenshot and video on failure for 7 days; a flake with no trace is unarguable.

## load

```bash
k6 run --vus 50 --duration 2m load.js
```

- Assert p95 and error rate, never the average: `thresholds: { http_req_duration: ['p(95)<500'], http_req_failed: ['rate<0.01'] }`.
- Ramp 0 to 50 vus over 30s, hold 2m, ramp down. A flat start measures warmup, not capacity.
- One bottleneck per run; change one variable between runs.

## test stack index

| tool | the rule that matters |
| --- | --- |
| Jest | `--onlyChanged` in a watch loop; `testEnvironment: jsdom` for DOM; `jest.useFakeTimers()` before the timer is created, not after. |
| JUnit 5 | `@ParameterizedTest` over a loop of asserts; `@TempDir` for files; `assertAll` so one failure does not hide the rest. |
| TestNG | `@DataProvider` for matrices; `groups` for suites; `priority` is a smell, order should not matter. |
| Cucumber/BDD | Steps are glue, not prose: one action per step, no assertion in a `Given`; a scenario that needs three `When`s is three scenarios. |
| Selenium | Explicit `WebDriverWait`, never `sleep`; `By.cssSelector` over XPath; quit the driver in `finally`. |
| Puppeteer | `waitForSelector` with a timeout; `page.evaluate` returns serializable data only; a missing `--no-sandbox` fails in Docker. |
| Browser automation general | One browser context per test for isolation; record a trace on failure; assert on state, not on timing. |
| AWT | Java desktop tests need `java.awt.headless=true` in CI, or the toolkit throws on `Toolkit.getDefaultToolkit()`. |
