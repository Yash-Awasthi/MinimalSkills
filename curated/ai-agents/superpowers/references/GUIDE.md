# superpowers guide

The long-form group prose and the full roster. `SKILL.md` is the loadable hub, and
`references/skills/<skill>.md` is the verbatim body to follow for one task.

### Entry and diagnosis

| Skill | What it does |
| --- | --- |
| [`diagnosing-superpowers`](references/skills/diagnosing-superpowers.md) | Read-only investigation of a session that went wrong, with transcript evidence and an optional bug bundle the partner must request. |
| [`using-superpowers`](references/skills/using-superpowers.md) | The entry rule. If a skill might apply, invoke it before any response, including a clarifying question. |

### Discovery and design

| Skill | What it does |
| --- | --- |
| [`brainstorming`](references/skills/brainstorming.md) | Finds what the partner actually wants before anything is built, through a grounded conversation, a playback, and a written design. |

### Planning and execution

| Skill | What it does |
| --- | --- |
| [`dispatching-parallel-agents`](references/skills/dispatching-parallel-agents.md) | Splits two or more independent tasks across isolated agents, with constructed context and no inherited session history. |
| [`executing-plans`](references/skills/executing-plans.md) | Runs the plan inline as the implementer, with the brief as spec, a ledger as memory, TDD per task, and one fresh review at the end. |
| [`subagent-driven-development`](references/skills/subagent-driven-development.md) | Runs a plan with a fresh implementer per task, a spec and quality review after each, and one broad whole-branch review at the end. |
| [`writing-plans`](references/skills/writing-plans.md) | Writes an implementation plan for an engineer who has not seen the codebase, with decided files, names, signatures, values, and proving tests. |

### Development loop

| Skill | What it does |
| --- | --- |
| [`systematic-debugging`](references/skills/systematic-debugging.md) | Root cause before any fix. Four phases, each completed before the next, with symptom fixes treated as failure. |
| [`test-driven-development`](references/skills/test-driven-development.md) | Red, green, refactor. Write the test, watch it fail, write minimal code, watch it pass, then clean up. |
| [`verification-before-completion`](references/skills/verification-before-completion.md) | No completion claim without a fresh command and its output. Includes the revert-and-watch-it-fail proof. |

### Code review

| Skill | What it does |
| --- | --- |
| [`receiving-code-review`](references/skills/receiving-code-review.md) | Verifies feedback before implementing, asks before assuming, and pushes back with evidence when the reviewer is wrong. |
| [`requesting-code-review`](references/skills/requesting-code-review.md) | Dispatches a reviewer subagent with precisely crafted context, never the session history, early and often. |

### Workspace and integration

| Skill | What it does |
| --- | --- |
| [`finishing-a-development-branch`](references/skills/finishing-a-development-branch.md) | Verifies tests, detects the environment, presents the merge, PR, and keep options, executes the choice, then cleans up. |
| [`using-git-worktrees`](references/skills/using-git-worktrees.md) | Establishes an isolated workspace through native tools first and a git worktree fallback, after proving the target directory is ignored. |

### Skill authoring

| Skill | What it does |
| --- | --- |
| [`writing-skills`](references/skills/writing-skills.md) | Skill authoring as TDD applied to documentation, with micro-tests, a no-guidance control, and a required deployment pass. |

## Group notes

### Entry and diagnosis

`using-superpowers` sets one rule. If there is even a one percent chance a skill
applies, invoke it. If it applies, there is no choice. It also sets skill priority
when several could apply, lists the red flags that mean you skipped the rule, and maps
the platform tool names for Claude Code, Codex, Gemini, Antigravity, Hermes, Muse, and
Pi through `references/`.

`diagnosing-superpowers` is read-only. Pin down with the partner what went wrong, read
the session transcripts on disk, and report what happened with evidence. Never modify,
move, or delete a session file. Never name a defect in a skill or propose a change,
because triage decides that. Build an export bundle only when the partner asks, and
follow `references/redaction-policy.md` and `references/context-safety.md` when you do.
Its `prompts/` directory holds the analyst passes for repeated work, cost and time,
plan adherence, quality evidence, request conflicts, skill timeline, stumbles, and
similar sessions.

### Discovery and design

`brainstorming` exists because the builder's belief about what the partner wants is
usually thinner than it feels. Start from what you actually know, look at the code
before asking, and ask only when the answer changes what gets built. Play the
understanding back, size the work, and write the design. A spike that came back
through the gate is not permission to keep building. `scripts/start-server.sh` and the
visual companion files support the optional visual path.

### Planning and execution

`writing-plans` assumes an engineer who has never seen the codebase. They will choose
idiomatically, but they cannot know your decisions, so the plan records the files, the
names and signatures, the values from the spec, and the test that proves each task.
Every plan starts with the required header, then global constraints, review focus, and
bite-sized tasks. `scripts/task-start` and `scripts/task-done` drive
`executing-plans`.

`subagent-driven-development` is the expensive, high-quality path. One fresh
implementer per task, a task review that covers spec compliance and code quality, a
fix loop, and a broad final review. Always name the model explicitly when dispatching.
Never dispatch parallel implementers. Never accept an implementer's self-review in
place of the task review. Never diff from `HEAD~1`, which truncates a multi-commit
task. Its prompt files and `references/` cover batching, cannot-verify cases, the fix
loop, handling reports, preflight, resuming, and the final review.

`executing-plans` is the inline path for when the partner chose it or no subagent tool
exists. The brief is the spec, the ledger is memory, TDD is the per-task gate, and the
whole branch gets one fresh review at the end. `dispatching-parallel-agents` applies
only to tasks with no shared state and no ordering. Each agent gets constructed context,
its own focused prompt, and a review before integration.

### Development loop

`test-driven-development` is the red, green, refactor cycle with its verification
steps. Write the test, run it wrong to watch it fail for the right reason, write the
minimal code, watch it pass, then clean up. Never fix a bug without a test.
`writing-good-tests.md` holds the test-quality standard.

`systematic-debugging` has four phases and requires each to finish before the next.
Root cause investigation, pattern analysis, hypothesis and testing, then implementation.
Symptom fixes are failure. Its supporting files cover root cause tracing,
defense in depth, condition-based waiting, and `find-polluter.sh` for test pollution.

`verification-before-completion` is the gate before any claim of done, fixed, or
passing. Run the command, read the output, then speak. The strongest pattern is to
write, run and pass, revert the fix, run and require a failure, restore, then run and
pass again.

### Code review

`requesting-code-review` dispatches a reviewer with a precisely crafted brief and never
with the session history. Its `code-reviewer.md` is the reviewer prompt. Review early
and often, and before a merge.

`receiving-code-review` is the discipline after feedback arrives. Verify before
implementing, ask before assuming, and treat technical correctness as more important
than social comfort. It lists the forbidden responses, separates handling for the
partner from handling for external reviewers, applies a YAGNI check to
professional-sounding feature requests, sets the implementation order, and covers
pushing back and correcting your own pushback. GitHub thread replies have their own
section.

### Workspace and integration

`using-git-worktrees` detects existing isolation first, then tries native worktree
tools, then falls back to `git worktree`. Never fight the harness. Verify the target
directory is gitignored before creating the worktree, run the project's own setup, and
verify a clean baseline before work starts.

`finishing-a-development-branch` runs verify tests, detect environment, determine the
base branch, present options, execute the choice, then clean up. Capture the values
Step 5 and Step 6 need before the directory change. Never `--force` on your own
initiative. The menu is complete as written, and discard happens only on an explicit
request.

### Skill authoring

`writing-skills` treats skill writing as TDD applied to process documentation. It
defines the skill types, the directory structure, the `SKILL.md` requirements, when to
use flowcharts, how to organize code and references, and how to test. Its references
cover Anthropic best practices, bulletproofing, CLAUDE.md testing, discovery,
flowcharts, Graphviz conventions, persuasion principles, and testing skills with
subagents. Micro-tests come first, and every one needs a no-guidance control. If the
control does not show the failure, there is nothing to fix. After writing any skill you
stop and complete the deployment process.
