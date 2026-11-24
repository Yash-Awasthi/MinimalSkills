---
name: superpowers
description: >-
  15 skills for a disciplined agent software loop. Covers the entry rule that makes
  skills fire, session diagnosis, brainstorming before creative work, plan writing,
  subagent-driven and inline plan execution, parallel agent dispatch, test-driven
  development, systematic debugging, verification before any completion claim,
  requesting and receiving code review, git worktrees, branch integration, and skill
  authoring as TDD. Use when a task matches any of those, or when the user names a
  superpowers skill.
metadata:
  curated_from: 15
  skills: 15
  groups: 7
---

# superpowers

15 skills. 7 groups. One hub. Every source body is preserved verbatim in
`references/skills/<skill>.md`, and every non-SKILL.md file from a source pack sits at
the same relative path under `references/assets/<skill>/`. Load one body for the task.

`SOURCES.md` maps every source path to its canonical skill and group.
`references/INDEX.md` groups the links, `references/skills.tsv` carries every
description, and `references/GUIDE.md` holds the long-form group prose.

## Pack contract

**A skill that might apply must fire.** That is the entry rule. It applies before any
response, including a clarifying question. A subagent dispatched for one task ignores
the entry skill and follows its brief.

**The iron laws are literal.** Root cause before any fix. A test you never watched
fail proves nothing. No completion claim without a fresh command and its output.
Violating the letter of one of these violates the point of it.

**Design comes before building.** `brainstorming` runs before any creative work,
including a talk or a business plan. It grounds the conversation in what is already
known, asks only questions whose answers change what gets built, plays the
understanding back, and writes the design down before code.

**Subagents get constructed context.** An implementer or reviewer never inherits the
session history. The brief carries exactly what that task needs, including the values
that appear only in the brief. One implementer at a time, because parallel
implementers conflict.

**Plan execution runs continuously.** Do not stop between tasks to ask whether to
continue. The named stop conditions are the only exits. Never start implementation on
`main` or `master` without the partner's explicit permission.

**Review has two directions.** Request it early and often with a crafted brief.
Receive it by verifying before implementing, asking before assuming, and pushing back
with evidence when the feedback is wrong. Performative agreement is a failure.

**Integration is a choice, not a default.** `finishing-a-development-branch` verifies
tests, detects the environment, and presents merge, PR, and keep options. Never
force-push on your own initiative, and never discard work unless the partner asks for
it in those words.

**Report evidence, not confidence.** Name the command, show the output, cite the
`file:line`, and keep pass, fail, blocked, and not verified distinct. A reviewer's
`Minor` label grades the spec's silence, not the user's outcome.

**Write clean as you draft.** Short declarative sentences. No em dash. A colon may
introduce a list and may not connect two clauses. Sentence case headings. No chatbot
framing, no generic closer.

## Routing

| The user wants | Group |
| --- | --- |
| The skill rule, or a look at why a session went wrong | Entry and diagnosis |
| To work out what to build before building it | Discovery and design |
| A plan, a plan executed by subagents, an inline run, or parallel dispatch | Planning and execution |
| TDD, a hard bug investigated, or proof before a completion claim | Development loop |
| A code review requested, or review feedback handled | Code review |
| An isolated worktree, or a branch finished and integrated | Workspace and integration |
| A new or edited skill, tested before deployment | Skill authoring |

## Full roster

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

## Output contract

- Name the skill you ran in the first line of your reasoning and in the todolist.
- Report evidence with the claim. The command, its output, the `file:line`, the test
  name, the exit code.
- Keep the skill's own artifact shape. A design stays a design, a plan stays a plan, a
  review stays a review, and a diagnosis report stays read-only.
- Keep pass, fail, blocked, and not verified as separate results.
- Keep open work open. A skipped task review, a truncated plan, and an unverified
  branch are reported, never hidden behind a pass.
- Never claim a saving, a fix, or a completion you did not measure this turn.
- Redact secrets, tokens, and personal data from any report, bundle, or public output.
- Write through `unslop`. Short declarative sentences, sentence case headings, no em
  dash, no colon connecting two clauses, no chatbot framing.

## Failure handling

| Situation | Response |
| --- | --- |
| A skill applies but you have not read its body | Read it, then act. Never cite a rule you did not load. |
| No root cause is found yet | Say so and keep investigating. Never apply a symptom fix. |
| A test passes on the first run | Suspect it. Prove it fails when the fix is reverted. |
| The plan has an open decision | Name it in the plan. Never leave it for the implementer to guess. |
| A subagent returns a self-review only | Run the task review anyway. |
| A reviewer finding looks wrong | Reproduce it, then push back with evidence. |
| The merge or cleanup would destroy work | Stop and ask. Permission from earlier does not carry. |
| The transcript or source read fails | Report the gap. Never turn it into a negative claim. |

## Provenance

15 `superpowers-*` source directories became 15 canonical skills in 7 groups. Each
source had one body, so no merge or variant resolution was needed. Every body is
verbatim at `references/skills/<skill>.md` with its original frontmatter removed, and
every other file from a source pack is copied under `references/assets/<skill>/` at
the same relative path. 65 asset files totaling 293,556 bytes were copied, including
the plan and review prompts, the session diagnosis prompts and templates, the platform
tool references, the skill-authoring references, and the shell and Node scripts.

Several skills delegate to a sibling in this pack by name, including
`test-driven-development`, `writing-plans`, and `using-superpowers`. Load the sibling
body rather than paraphrasing it.

Upstream author `superpowers`. Original catalog paths are preserved in `SOURCES.md`
and under `_archive/superpowers/catalog/`.
