---
name: mattpocock
description: >-
  39 skills for running a disciplined engineering loop end to end: routing across the
  flow, grilling a plan until it is sharp, turning it into a spec and tracer-bullet
  tickets, implementing with TDD, reviewing on standards and spec axes, and handing
  work to another agent. Also covers deep-module codebase design, domain modeling,
  bug diagnosis, writing documents for agents, teaching, prototype spikes, setup
  scaffolding, git guardrails, and long-running chief-of-staff and software-factory
  work. Use when a task matches any of those, or when the user names a mattpocock skill.
metadata:
  curated_from: 39
  skills: 39
  groups: 7
---

# mattpocock

39 skills. 7 groups. One hub. Every source body is preserved verbatim in
`references/skills/<skill>.md`, and every non-SKILL.md file from a source pack sits at
the same relative path under `references/assets/<skill>/`. Load one body for the task.

`SOURCES.md` maps every source path to its canonical skill and group.
`references/INDEX.md` groups the links, `references/skills.tsv` carries every
description, and `references/GUIDE.md` holds the long-form group prose.

## Pack contract

**The map is not the skill.** `ask-matt` orients you. Before you state what a skill
does, recommend skipping a step, or cite a rule, read that skill's body.

**Skills compose in a flow.** Most work runs the main line, an on-ramp, then the next
step. `to-spec` collapses context into a plan, `to-tickets` cuts it into
tracer-bullet slices with blocking edges, and `implement-spec` works the graph from
its frontier. Do not skip from idea to code.

**Phase boundaries are hard.** Grilling produces decisions, not code. A prototype
answers one question and dies. A spec is synthesis, so `to-spec` does not interview.
A ticket is a vertical slice, not a step in a list. Keep the artifact each step
produces and hand it forward by path.

**Repo conventions come first.** These skills assume a configured repo. If the issue
tracker, triage labels, or domain docs are missing, run
`setup-matt-pocock-skills` before the skill that needs them.

**Domain words are exact.** `codebase-design` fixes the vocabulary as module,
interface, depth, seam, adapter, leverage, locality. `domain-modeling` owns
`GLOSSARY.md` and the ADRs. Use those words and do not drift into component, service,
API, or boundary.

**One round at a time.** Grilling asks the whole frontier in one round with a
recommended answer attached to each question, then waits. Never batch a later round
into the current one, and never act until the user confirms a shared understanding.

**A loop is proof.** Diagnosis and TDD both start from a failing observable. Build the
loop, watch it go red, then fix. A passing suite you never saw fail is not evidence.

**Private context stays local.** Handoffs and retro read session logs, so redact keys,
passwords, and personal data. Handoff documents go to the temp directory, not the
workspace, unless the skill says otherwise.

**Write clean as you draft.** Short declarative sentences. No em dash. A colon may
introduce a list and may not connect two clauses. Sentence case headings. No chatbot
framing, no generic closer.

## Routing

| The user wants | Group |
| --- | --- |
| To know which skill fits, to hand work to another agent, a retro, or a re-pitch | Router, handoff, and retro |
| A plan or decision stress-tested, a decision map, a questionnaire, or a workflow spec | Grilling and decision shapes |
| A spec, tickets, triage on an issue, or implementation of a spec | Specs, tickets, and implementation |
| A module interface designed, a domain model sharpened, an architecture scan, or a spike | Codebase design and domain |
| TDD, a hard bug diagnosed, a two-axis review, a PR body, pre-commit, or git blocking | Engineering practice |
| A skill, AGENTS.md, CLAUDE.md, or any article assembled from raw material | Writing |
| A long goal run across sessions, a factory design, teaching, research, or repo setup | Long-running work, teaching, and setup |

## Full roster

### Router, handoff, and retro

| Skill | What it does |
| --- | --- |
| [`ask-matt`](references/skills/ask-matt.md) | The router over this pack. Names the right flow, on-ramp, or standalone skill for the situation and refuses to summarize a skill it has not read. |
| [`claude-handoff`](references/skills/claude-handoff.md) | Writes the same handoff, then launches a named background Claude agent seeded with it so the work continues immediately. |
| [`handoff`](references/skills/handoff.md) | Compacts the current conversation into a handoff document in the temp directory, with a suggested-skills section and no duplicated artifact content. |
| [`retro`](references/skills/retro.md) | Retrospects a coding session and proposes improvements to the agent's environment, not to the product code. |
| [`wait-what`](references/skills/wait-what.md) | The user's last message did not land. Re-pitch the same idea with context, in Simplified Technical English, and in the project glossary's words. |

### Grilling and decision shapes

| Skill | What it does |
| --- | --- |
| [`grill-me`](references/skills/grill-me.md) | Two-line alias that calls grilling. |
| [`grill-with-docs`](references/skills/grill-with-docs.md) | Calls grilling and domain-modeling together, so the interview also writes ADRs and glossary entries as decisions settle. |
| [`grilling`](references/skills/grilling.md) | The interview primitive. Maps the decision as a design tree, works one frontier of questions per round, attaches a recommended answer to each, and stops when the frontier is empty. |
| [`loop-me`](references/skills/loop-me.md) | A stateful grilling session whose only output is workflow specs, aimed at the recurring loops in the user's life and work. |
| [`to-questionnaire`](references/skills/to-questionnaire.md) | Grills the send, not the subject, then writes a markdown questionnaire that pulls the missing knowledge out of one named recipient. |
| [`wayfinder`](references/skills/wayfinder.md) | Charts a huge effort as a shared map of decision tickets on the issue tracker, resolves them one at a time, then hands off to to-spec. |

### Specs, tickets, and implementation

| Skill | What it does |
| --- | --- |
| [`implement`](references/skills/implement.md) | Implements the work in a spec or ticket, states the ticket title, uses tdd at agreed seams, and runs typecheck and tests as it goes. |
| [`implement-spec`](references/skills/implement-spec.md) | Implements a whole spec on one integration branch by working the ticket task graph from its frontier, not by following a step list. |
| [`to-spec`](references/skills/to-spec.md) | Synthesizes the existing conversation and repo state into a spec and publishes it. No interview. |
| [`to-tickets`](references/skills/to-tickets.md) | Breaks a spec or plan into tracer-bullet vertical slices, records each blocking edge, quizzes the user, and publishes to the configured tracker. |
| [`triage`](references/skills/triage.md) | Moves issues and external PRs through the five triage roles, writes agent-ready briefs, and stamps every posted comment with the triage disclaimer. |

### Codebase design and domain

| Skill | What it does |
| --- | --- |
| [`codebase-design`](references/skills/codebase-design.md) | The shared deep-module vocabulary: module, interface, depth, seam, adapter, leverage, locality, with the deletion test and the two-adapter rule. |
| [`domain-modeling`](references/skills/domain-modeling.md) | Actively sharpens the project's domain model and writes glossary entries and ADRs the moment a term or decision settles. |
| [`improve-codebase-architecture`](references/skills/improve-codebase-architecture.md) | Scans for shallow modules, presents deepening candidates as an HTML report, then grills one candidate through to a decision. |
| [`prototype`](references/skills/prototype.md) | Builds throwaway code that answers one design question, either a logic demo or a UI shell, and deletes it once answered. |
| [`setup-ts-deep-modules`](references/skills/setup-ts-deep-modules.md) | Wires dependency-cruiser so each TypeScript package is a deep module reachable only through its root entry points, then proves the rules bite. |

### Engineering practice

| Skill | What it does |
| --- | --- |
| [`code-review`](references/skills/code-review.md) | Reviews the diff since a supplied fixed point on two independent axes, repo standards and the originating spec, in parallel sub-agents. |
| [`diagnosing-bugs`](references/skills/diagnosing-bugs.md) | A six-phase diagnosis loop for hard bugs. Build a tight failing loop first, then reproduce, minimise, hypothesise, instrument, fix, and clean up. |
| [`git-guardrails-claude-code`](references/skills/git-guardrails-claude-code.md) | Installs a Claude Code PreToolUse hook that blocks dangerous git commands such as push, reset --hard, clean, and branch -D. |
| [`migrate-to-shoehorn`](references/skills/migrate-to-shoehorn.md) | Migrates test files from `as` assertions to @total-typescript/shoehorn `fromPartial` and `fromAny`. Test code only. |
| [`pr`](references/skills/pr.md) | The PR body template: summary with a diagram or diff sketch, evidence, merge danger, and section guidance. |
| [`setup-pre-commit`](references/skills/setup-pre-commit.md) | Installs Husky, lint-staged with Prettier, typecheck, and tests as a pre-commit gate, then verifies it fires. |
| [`tdd`](references/skills/tdd.md) | The red-green reference. Defines a good test, where seams go, the anti-patterns, and the rules of the loop on every cycle. |

### Writing

| Skill | What it does |
| --- | --- |
| [`writing-beats`](references/skills/writing-beats.md) | Writing, exploit. Assembles a fixed pile of raw material into a beat-by-beat journey, one beat at a time. |
| [`writing-for-agents`](references/skills/writing-for-agents.md) | The reference for any document an agent consumes: skills, AGENTS.md, CLAUDE.md. Context pointers, the two loads, information hierarchy, completion criteria, and when to split. |
| [`writing-fragments`](references/skills/writing-fragments.md) | Writing, explore. Grills the writer and appends raw fragments to one file, with no outline or structure yet. |
| [`writing-shape`](references/skills/writing-shape.md) | Writing, exploit. Shapes raw material into an article block by block, with the raw file read-only. |

### Long-running work, teaching, and setup

| Skill | What it does |
| --- | --- |
| [`chief-of-staff`](references/skills/chief-of-staff.md) | Pursues one long-running goal across a long session by coordinating subagents, schedules, and a wiki, and writes history rather than the present tense. |
| [`research`](references/skills/research.md) | Delegates a question to a background agent that reads primary sources only and writes one cited markdown note where the repo keeps such notes. |
| [`scaffold-exercises`](references/skills/scaffold-exercises.md) | Creates lint-clean exercise directories with sections, problems, solutions, and explainers for the course layout. |
| [`setup-matt-pocock-skills`](references/skills/setup-matt-pocock-skills.md) | Scaffolds the per-repo configuration the engineering skills assume: issue tracker, triage label vocabulary, and domain doc layout. |
| [`software-factory`](references/skills/software-factory.md) | The shared language for designing a software factory: its tasks, runs, and the ticket, git, runner, and observability services it plugs into. |
| [`teach`](references/skills/teach.md) | A stateful teaching workspace with a mission, resources, lessons, reference docs, and format files for each, built for fluency and storage strength. |
| [`wizard`](references/skills/wizard.md) | Generates an interactive bash wizard from template.sh for steps only a human can perform, with stage gates, secret entry, and idempotent .env upserts. |

## Group notes

### Router, handoff, and retro

`ask-matt` is the map, not the work. It describes the main flow from idea to ship and
the on-ramps that merge onto it, and it hands off rather than building. Its summaries
are orientation only, so read the named skill's `SKILL.md` before repeating a claim.

`handoff` compacts a conversation into one document in the OS temp directory, names
the skills the next agent should load, and references existing specs, plans, ADRs,
issues, commits, and diffs by path or URL instead of copying them. Redact secrets and
personal data. `claude-handoff` writes the same summary and then runs
`claude --bg --name "<descriptive name>" -- "$(cat <summary file>)"` so a fresh
background agent starts immediately. Passing the file keeps the shell from expanding
backticks or `$`, and the name is mandatory because it labels the job list, session
picker, and terminal title.

`retro` improves the agent's environment, not the product. It reads the session's
primary sources, calls `writing-for-agents` for style, and separates implementation
work from review work. `wait-what` is the recovery move when a message did not land.
It re-pitches with context in ASD-STE100 Simplified Technical English and the
project's own glossary words.

### Grilling and decision shapes

`grilling` is the primitive every other grilling skill calls. It models the work as a
design tree and asks the whole **frontier**, every decision whose prerequisites are
settled, in one numbered round with a recommended answer per question. Facts are the
agent's job and decisions are the user's. The session ends when the frontier is empty,
and nothing is acted on until the user confirms the shared understanding.

`grill-me` is a two-line alias. `grill-with-docs` calls grilling and
`domain-modeling` together so ADRs and glossary entries land as decisions settle.
`loop-me` points the same discipline at the recurring loops in a person's life and
emits workflow specs, with no structure mandated that the grilling did not earn.

`wayfinder` handles an idea too big for one session. It charts a destination, writes
a shared map of **decision tickets** on the issue tracker, and resolves them one at a
time. Research tickets go to a subagent running `research`. Grilling tickets call
grilling and domain-modeling. When the route is clear the map hands off to `to-spec`
instead of continuing to loop. `to-questionnaire` grills only the send, meaning the
recipient, their role, and what is needed back, then writes a document that targets
the gap between what that person knows and what the user needs.

### Specs, tickets, and implementation

`to-spec` synthesizes what is already known and does not interview. It explores the
repo, uses the domain glossary, respects ADRs, and produces problem statement,
solution, user stories, implementation decisions, testing decisions, out of scope, and
further notes. `to-tickets` cuts that into vertical tracer-bullet slices, each with a
parent, what to build, acceptance criteria, and a **blocked by** line that names the
tickets which genuinely gate it. It quizzes the user on the slices and the edges
before publishing.

`triage` is a small state machine over issues and external PRs, since a PR is an issue
with attached code. It resolves bare references per the tracker config, moves work
through the five canonical roles, verifies, grills when the request is unclear, and
writes an agent-ready brief. Every comment it posts starts with the triage
disclaimer.

`implement` works one ticket or spec, states the ticket title first, asks when the
reference is ambiguous, uses `tdd` at pre-agreed seams, runs typecheck and single test
files regularly, and runs the full suite once at the end. `implement-spec` runs the
whole spec on one integration branch. Tickets are a task graph, not a step list, so it
keeps grabbing from the frontier and may send an exploration subagent to read code or
docs and save its notes.

### Codebase design and domain

`codebase-design` supplies the only vocabulary these skills use. A **module** hides
behaviour behind an **interface**, which includes invariants, ordering, error modes,
configuration, and performance, not just the type signature. **Depth** is behaviour
per unit of interface. A **seam** is where a module can be swapped. One adapter is a
hypothetical seam and two make it real. The deletion test asks whether deleting the
module concentrates complexity or merely moves it.

`domain-modeling` is the active discipline. Challenge terms, invent edge-case
scenarios, write `GLOSSARY.md` inline, and offer an ADR sparingly. Create files lazily.
The glossary holds no implementation details. `improve-codebase-architecture` scans
for shallow modules, presents deepening candidates as an HTML report built from
`HTML-REPORT.md`, and then grills one candidate through to a decision.

`setup-ts-deep-modules` enforces the shape with dependency-cruiser, keeping a package's
public surface at its root entry files and hiding subfolders, then proves the rules
bite. `prototype` writes throwaway code for one design question. The logic branch is
a single HTML file the user double-clicks. The UI branch starts from one project task
runner command. Both are trivial to run and are deleted after the answer.

### Engineering practice

`tdd` is the reference for a loop worth keeping. A good test asserts behaviour at a
seam, names the domain word, and fails for one reason. Read the anti-patterns and the
rules of the loop before and during every cycle, not after.

`diagnosing-bugs` runs six phases and skips one only with a stated reason. Redact
first, then build a tight feedback loop and watch it go red. Do not proceed until the
bug is reproduced and minimised. Never log everything and grep. Fix, add the
regression test, then clean up instrumentation.

`code-review` pins a fixed point, finds the spec source and the standards sources,
then runs Standards and Spec as parallel sub-agents so their contexts stay clean. It
aggregates both and treats each smell as a labelled heuristic rather than a hard
violation, skipping anything the tooling already enforces. `pr` is the body template,
with a summary diagram or diff sketch, evidence, and a merge danger section.

`migrate-to-shoehorn` replaces `as` in test files with `fromPartial` and `fromAny`,
and never uses shoehorn in production code. `setup-pre-commit` detects the package
manager, installs Husky and lint-staged with Prettier, adds typecheck and tests, and
verifies the hook. `git-guardrails-claude-code` installs a PreToolUse hook that blocks
push, reset --hard, clean, branch -D, and their variants, then verifies it.

### Writing

`writing-for-agents` is the reference for anything an agent consumes. A **context
pointer** names out-of-context material and the condition for reaching it, which is
what a skill description is. Every document carries two loads, the pointer and the
content it gates. Use the information hierarchy, give every step its completion
criterion, and split only when the cut earns the extra load. Read
`SKILL-MECHANICS.md` when the document is a skill.

The three writing skills form explore, then exploit. `writing-fragments` grills and
appends fragments to one file with no structure. `writing-beats` takes a fixed pile
and builds a beat-by-beat journey, grounding each term before a beat leans on it.
`writing-shape` shapes the same pile into an article block by block. All three re-read
the file from disk before every write, append instead of overwriting, and never write
ahead.

### Long-running work, teaching, and setup

`chief-of-staff` runs one long goal as the directly responsible individual, on two
tracks at once. The tactical track finishes the immediate task. The strategic track
changes the environment so the next task goes better. It schedules subagents, keeps a
wiki, and writes history with a date or commit, never the present tense.

`software-factory` is vocabulary for a system of agents that turns tickets, PRs, and
schedules into merged, deployed code. A **task** is defined once and run many times. A
**run** is one execution. Use its words for tasks, services, runners, git hosts,
ticket trackers, and observability, start slow, and question every task.

`teach` treats the directory as a teaching workspace with `MISSION.md`, lessons,
reference HTML, resources, learning records, and notes, each with a format file. It
targets the zone of proximal development, teaches the knowledge a skill needs, then
has the user practise it, and never trusts parametric knowledge where a real resource
exists. `research` delegates to a background agent that reads primary sources only and
writes one cited file.

`setup-matt-pocock-skills` runs once per repo. It discovers the issue tracker, the
triage label strings, and the domain doc layout, recommends an answer first, and writes
`docs/agents/issue-tracker.md`, `domain.md`, and, only when triage is installed,
`triage-labels.md`. It never creates `AGENTS.md` beside an existing `CLAUDE.md` or
the reverse. `scaffold-exercises` builds lint-clean exercise folders. `wizard` turns a
manual procedure only a human can perform into a staged bash wizard from
`template.sh`, with confirmation gates, hidden secret entry, cross-platform URL
opening, and idempotent `.env` and `gh secret` writes, and it is deleted after the run
unless the user wants it committed.

## Output contract

- Name the skill you ran in the first line of your reasoning and in the todolist.
- Follow the skill's own artifact shape. A decision stays a decision, a spec stays a
  spec, a ticket stays a slice, and a prototype stays throwaway.
- Report the artifact path and what it contains. A summary in chat is not the
  deliverable when the skill writes a file.
- Keep evidence and interpretation apart. A loop that went red, a command output, a
  file path, a cited primary source.
- Keep open work open. An unresolved frontier, a missing tracker config, and an
  unverified fix are reported, never rounded up.
- Write through the pack's own standard. Short declarative sentences, sentence case
  headings, no em dash, no colon connecting two clauses, no chatbot framing.
- Redact keys, passwords, and personal data from any handoff, retro, research note, or
  public output.

## Failure handling

| Situation | Response |
| --- | --- |
| The issue tracker, triage labels, or domain docs are missing | Run `setup-matt-pocock-skills` first, or name the gap. |
| A grilling frontier is not empty | Ask the next round and wait. Do not start building. |
| A bug has no failing loop | Say so and construct one. Never fix blind. |
| A review finding looks serious | Prove it with a command or a `file:line` before reporting. |
| A test, property, or gate fails | Keep the failure, fix the cause, and never weaken the check. |
| A skill points at a sibling skill or format file | Load it before citing or applying it. |
| A handoff or retro would expose a secret | Redact it and say what was removed. |
| The evidence contradicts the requested change | Show the evidence and stop. |

## Provenance

39 `mattpocock-*` source directories became 39 canonical skills in 7 groups. Each
source had one body, so no merge or variant resolution was needed. Every body is
verbatim at `references/skills/<skill>.md` with its original frontmatter removed, and
every other file from a source pack is copied under `references/assets/<skill>/` at
the same relative path. 70 asset files totaling 134,832 bytes were copied, mostly one
`agents/openai.yaml` per skill plus the format files, templates, and scripts the
bodies point at.

Several skills delegate to an installed sibling or to the repo's own tooling,
including `tdd`, `writing-for-agents`, `codebase-design`, `domain-modeling`,
`research`, and `grilling`. The delegated skill remains the authority for its domain,
and the referenced file remains the authority for its format.

Upstream author `mattpocock`. Original catalog paths are preserved in `SOURCES.md`
and under `_archive/mattpocock/catalog/`.
