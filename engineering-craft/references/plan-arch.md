# plan-arch

Load when starting a feature, refactor, migration or a decision that outlives the task.

## slice

1. Restate the goal in one sentence.
2. List constraints: runtime, budget, deadline, team, compatibility.
3. Write the smallest vertical slice that proves the path end to end.
4. Name files to touch, in order.
5. Execute in that order. Report every deviation.

Horizontal layers with nothing calling them are not progress.

## reversible first

| decision | reversibility | default |
| --- | --- | --- |
| library choice | high | pick the boring one |
| data model | low | write the migration plan first |
| public API shape | low | version it from day one |
| queue vs sync call | medium | start sync, measure |
| monorepo split | low | do not split without a second team |

## adr

Write `docs/adr/NNNN-title.md` when a decision is hard to reverse or changes a public interface.

```
status: accepted | superseded by NNNN
context: <forces at play, 3 lines>
decision: <what, 1 line>
consequences: <what gets easier, what gets harder, what is now impossible>
```

Superseded ADRs stay in place, marked. Deleting history makes the same debate repeat.

## c4 levels

- context: who uses the system, what it talks to.
- container: deployable units and their protocols.
- component: modules inside a container.
- code: generate from the tree, never draw from memory.

One diagram, one audience, one idea.

## boundaries

- Name bounded contexts before integrating services.
- Integration styles: shared kernel, customer-supplier, conformist, anti-corruption layer, open host service, published language.
- An anti-corruption layer at every boundary you do not control.
- Shared database between contexts is a coupling decision, not a shortcut.

## monorepo

- Tooling at the root: one lockfile, one task runner, one CI config.
- Per-package ownership in `CODEOWNERS`.
- Build affected only: `nx affected -t build`, `turbo run build --filter=...[HEAD^1]`.
- Cache locally first, remote second, with a fallback path.
- Crossing package boundaries goes through the public entry, never a deep import.

## deep modules

Small interface, large behavior. A shallow module with pass-through methods adds a hop and no value. If a caller must read the implementation to use it, the interface is wrong.

## before coding

```bash
rg "className|functionName" --stats   # does this already exist
cat package.json | head -40           # available deps, scripts, engines
git log --oneline -20 -- path/        # recent churn on the target area
```

Read the conventions file if present: `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`.

## delivery index

| practice | the rule that matters |
| --- | --- |
| Planning and architecture | One page: context, options, decision, consequences, the date. A diagram that needs a legend is two diagrams. |
| Progressive estimation | Estimate the next slice only; a 6-month estimate is a guess with a decimal point. |
| Idea evaluation | Score reach, impact, confidence, effort; a score without a baseline is a preference. |
| Unship | Delete the flag, the route, the docs and the tests in one PR; a dead feature left behind is a maintenance tax. |
| Spec-driven development | Write the spec as tests first; a spec that cannot fail is documentation. |
| Project development methodology | Fixed cadence, variable scope. Scope fixed and cadence variable is how dates slip. |
| Bounded build loop | Time-box the attempt, state the stop condition, report what was tried. |
| Bug hunt swarm | One bug per agent, shared repro corpus, dedupe before triage. |
| Pre-push audit | `git diff --check`, tests, lint, and the secret scan before the push, not after. |
| OpenSpec change workflow | Change proposal, delta spec, tasks, then implement; the spec diff is the review artifact. |
| Jira discipline | One ticket per shippable change; the PR links it; the ticket closes on merge, not on deploy. |
| Rust project scaffolding | `cargo new --lib`, `thiserror` for library errors, `anyhow` at the binary edge, `#[deny(warnings)]` in CI. |
| Vibers | Fast prototype code is quarantined in one module with a test seam before it touches the core. |
| Build a feedback loop | Shorten the loop before adding tests: the fastest failing signal wins. |
| Performance (planning) | State the budget and the measurement before the optimization; a change with no before/after is a guess. |
| Complexity | Cyclomatic over 10 or nesting over 3 is a refactor trigger, not a style opinion. |
| Simplification, five principles | Delete, inline, dedupe, flatten, rename. In that order; renaming first hides the duplication. |
| Untangle | Extract the seam, pin it with a test, then move code across the seam in small commits. |
| Tech debt | A debt item names 
the interest: what it costs per change, and the trigger to pay it. |
| Legacy modernization | Strangler pattern: route a slice through the new path, compare outputs, then delete the old branch. |
| Agent delegation | A brief carries the goal, the files, the constraints, the done test and the report format. |
| Delegates | One owner per file; two agents on one file produce conflicting edits, not parallelism. |
| Persona teammates | A persona changes the review lens, not the facts; label opinions as opinions. |
| Conduct register | Log decisions, owners and dates; an undocumented decision is re-litigated every quarter. |
| Governance | Who approves what, with a threshold: a policy with no threshold is advice. |
| Kaizen | One measurable improvement per cycle, kept; a burst of changes with no measurement is churn. |
| Continuous learning | A postmortem action becomes a test or a runbook step, or it will recur. |
| LintLang | Lint rules encode the team's decisions; a rule disabled inline needs a reason on the same line. |
| Obsess / ponder | Time-box the thinking, then write the decision; open-ended deliberation is a schedule risk. |
