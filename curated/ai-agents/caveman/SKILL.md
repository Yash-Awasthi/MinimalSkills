---
name: caveman
description: >-
  22 skills for terse agent output and disciplined engineering. Three caveman voice
  modes (caveman, ultracave, megacave) plus help and session stats, compressed commit
  and review formats, cavecrew delegation presets and a read-only explorer, six
  engineering disciplines (investigate first, lean build, migration, safe refactor,
  surgical patch, verify and stop), memory compression and cost-lowering edits, and the
  Caveman Cloud workflow, evidence, experiment, optimization, and gateway setup skills.
  Use when a task matches any of those, or when the user names a caveman skill.
metadata:
  curated_from: 22
  skills: 22
  groups: 6
---

# caveman

22 skills. 6 groups. One hub. Every source body is preserved verbatim in
`references/skills/<skill>.md`, and every non-SKILL.md file from a source pack sits at
the same relative path under `references/assets/<skill>/`. Load one body for the task.

`SOURCES.md` maps every source path to its canonical skill and group.
`references/INDEX.md` groups the links, `references/skills.tsv` carries every
description, and `references/GUIDE.md` holds the long-form group prose.

## Pack contract

**A voice is not broken grammar.** Caveman drops ceremony, articles, and connective
filler. It never drops `not`, `never`, `no`, `only`, or `except`, and it never alters
code, commands, paths, API names, error strings, numbers, or units. One term per
thing. The user's language wins, and quoted text never switches it.

**Do not perform caveman.** No `me think`, no `Caveman:` prefix, no normal answer
followed by a caveman copy, no decorative tables or emoji. Never add a word to sound
caveman. If the caveman phrasing is not shorter than plain, use plain.

**Mode persists until stopped.** `/caveman`, `/caveman ultra`, and `/caveman wenyan`
select a voice. `stop caveman` or `normal mode` ends it. `/caveman status` reports and
changes nothing, and a hook's `Caveman mode: <mode>` value is relayed when present.

**Compression keeps meaning.** `caveman-compress` protects fenced blocks and file
extensions, keeps a readable `.original.md` backup outside the source tree, and refuses
secret-looking files before reading them. Data leaves the machine when it compresses,
so say so.

**Evidence before edits.** The six engineering skills share one rule. Separate the
observed symptom from the inferred cause, trace the mechanism, then change the
narrowest responsible layer. Do not edit until one credible mechanism explains the
evidence.

**Verification brackets the change.** Every engineering skill names the proof it
needs, runs focused checks before wider gates, and keeps pass, fail, unavailable, and
blocked as distinct results. A green build is not proof of the user-visible outcome.

**Cloud actions fail closed.** `caveman-manage` and `caveman-evidence-review` are
read-only. They never approve pending results, never convert a lift into verified
savings, never supply an organization id, and never emit or run an executable lifecycle
command. Unknown state is not a pass.

**Reported numbers are measurements.** Cite trace ids and exact time windows. State
the window a number covers and never multiply it into a month or a run rate. Never
infer saved tokens, percentages, or dollars without a paired measured comparison.

**Write clean as you draft.** Short declarative sentences. No em dash. A colon may
introduce a list and may not connect two clauses. Sentence case headings. No chatbot
framing, no generic closer.

## Routing

| The user wants | Group |
| --- | --- |
| A terse voice, a help card, or session token stats | Voice modes and help |
| A commit message or a code review | Compressed output |
| Cheaper delegation or read-only code localization | Delegation and exploration |
| A bug investigated, a build scoped, a migration, a refactor, a patch, or proof | Engineering discipline |
| A memory file compressed or a token cost lowered | Token cost and memory |
| Gateway setup, workflow labels, spend evidence, an experiment, or an optimization | Caveman Cloud |

## Full roster

### Voice modes and help

| Skill | What it does |
| --- | --- |
| [`caveman`](references/skills/caveman.md) | The base terse voice. Answer first, every technical fact kept, fluff gone. Stays on until stop caveman or normal mode. |
| [`caveman-help`](references/skills/caveman-help.md) | The one-shot reference card for modes, commands, deactivation, language rules, and the default-mode setting. Changes no state. |
| [`caveman-stats`](references/skills/caveman-stats.md) | Prints the hook's recorded output and cache-read token report verbatim for the current Claude Code session, or points at the host's native usage report. |
| [`megacave`](references/skills/megacave.md) | Caveman in Classical Chinese. 文言文 register, particles instead of connective phrases, technical payload in its original script. |
| [`ultracave`](references/skills/ultracave.md) | Caveman with the grammar stripped. Fragments, one word where one word is enough, each fact once. Invoke only with /ultracave. |

### Compressed output

| Skill | What it does |
| --- | --- |
| [`caveman-commit`](references/skills/caveman-commit.md) | Conventional Commits subject and body, compressed to intent. Types, imperative mood, and the cases that always need a body. |
| [`caveman-review`](references/skills/caveman-review.md) | One line per finding. Location, problem, fix. Optional severity prefix, no throat-clearing, paste-ready comments. |

### Delegation and exploration

| Skill | What it does |
| --- | --- |
| [`cavecrew`](references/skills/cavecrew.md) | Three subagent presets, investigator, builder, and reviewer, that return compressed output so main context lasts longer. |
| [`caveman-explore`](references/skills/caveman-explore.md) | FastContext, a read-only explorer that returns only path and line-range citations and never edits, runs commands, or proposes fixes. |

### Engineering discipline

| Skill | What it does |
| --- | --- |
| [`investigate-first`](references/skills/investigate-first.md) | Gathers evidence before editing. Separates symptom from cause, ranks hypotheses by cheap falsification, and edits only after one mechanism explains the evidence. |
| [`lean-build`](references/skills/lean-build.md) | Builds a narrow end-to-end outcome that fits the system. Derives acceptance and non-goals, reuses fitting seams, and states an explicit stop condition. |
| [`migration`](references/skills/migration.md) | Reversible compatibility-safe transitions for schema, data, API, protocol, config, or dependencies, with a forward and rollback path and preserved data. |
| [`safe-refactor`](references/skills/safe-refactor.md) | Restructures code while preserving behavior, one ownership boundary at a time, with verification bracketing every structural move. |
| [`surgical-patch`](references/skills/surgical-patch.md) | Fixes the narrowest layer that owns the wrong behavior, with regression proof and no cleanup, renaming, or abstraction outside the fix. |
| [`verify-and-stop`](references/skills/verify-and-stop.md) | Proves existing work meets acceptance without expanding scope. Runs focused checks first and distinguishes pass, fail, unavailable, and blocked. |

### Token cost and memory

| Skill | What it does |
| --- | --- |
| [`caveman-compress`](references/skills/caveman-compress.md) | Compresses a memory file such as CLAUDE.md into caveman speak, keeps an out-of-tree readable backup, and refuses secret-looking files before reading them. |
| [`caveman-learn`](references/skills/caveman-learn.md) | Turns a Caveman learn report into consent-gated edits that lower tokens per turn, with a net-negative gate that reverts any edit that does not pay off. |

### Caveman Cloud

| Skill | What it does |
| --- | --- |
| [`caveman-discover`](references/skills/caveman-discover.md) | Finds and labels every LLM workflow in the repo so Caveman Cloud groups spend by workflow, then proposes the label wiring before applying it. |
| [`caveman-evidence-review`](references/skills/caveman-evidence-review.md) | Read-only review of Caveman cost, Cave Score, workflows, traces, latency, errors, routing, and savings. Never starts, approves, or rolls back an experiment. |
| [`caveman-manage`](references/skills/caveman-manage.md) | Inspects experiment lifecycle and blocks unsafe execution. Never approves pending results and never runs a lifecycle mutation, even after approval. |
| [`caveman-optimize`](references/skills/caveman-optimize.md) | Turns a report-only observation into an operator-chosen candidate with a paired baseline eval. Needs explicit approval and never converts tokens into dollars. |
| [`caveman-setup`](references/skills/caveman-setup.md) | Wires the repo through the Caveman gateway in record mode, with exact callsites, a real request to verify, and verbatim failure templates. |

## Group notes

### Voice modes and help

`caveman` is the base voice. Answer first, kill ceremony, choose the short word, make
articles optional, one idea per sentence, payload verbatim, and a bounded status line
around tool runs. It breaks its own rules for safety warnings, irreversible actions,
ambiguous instructions, and anything where terseness would mislead.

`ultracave` strips the grammar. Fragments, one word where one word is enough, each
fact once, conjunctions cut only when the order still survives. `megacave` is the same
discipline in Classical Chinese, using particles such as 之, 乃, 為, 其, 則, 故, 以 in
place of connective phrases, with negations, numerals, and technical payload kept in
their original script. Token savings in 文言 are small and noisy, so never claim them.

`caveman-help` prints the mode table, the skill list, the deactivate commands, the
language rule, and how to set a default mode. It is one-shot and changes no state.
`caveman-stats` prints the hook's report verbatim inside a fenced block and never
recalculates it. On Gemini CLI it points at `/stats model` or `/stats session`, because
a custom command cannot read live session metrics. Savings stay unknown without a
measured comparison.

### Compressed output

`caveman-commit` writes Conventional Commits. The subject is
`<type>(<scope>): <imperative summary>` with type from feat, fix, refactor, perf,
docs, test, chore, build, ci, style, or revert, and the verb in imperative mood. A body
is always required for a breaking change, a security fix, a data migration, or a
revert, because a future debugger needs that context.

`caveman-review` writes one line per finding as `L<line>: <problem>. <fix>.`, or
`<file>:L<line>: ...` across a multi-file diff. A severity prefix such as `🔴 bug:` is
optional and only when severities are mixed. It keeps the same auto-clarity exceptions
as the voice skills.

### Delegation and exploration

`cavecrew` provides three presets. `cavecrew-investigator` answers where code lives,
`cavecrew-builder` handles a one or two file edit, and `cavecrew-reviewer` reviews a
diff. Their tool output is compressed, which is the real gain, since main context
shrinks with every delegation. Use plain `Explore` when architecture commentary is the
point rather than localization.

`caveman-explore` is FastContext, a read-only explorer. It fires several searches in
parallel on the first turn, cites only line ranges it actually read, and replies with
an evidence block and nothing else. It never edits, never runs commands, and never
proposes a solution.

### Engineering discipline

`investigate-first` handles unknown causes, intermittent behavior, and performance
regressions. Map inputs, state transitions, ownership boundaries, and the exact
failure output, then rank hypotheses by evidence and cheap falsification value.
`lean-build` turns a feature into a narrow end-to-end outcome, derives acceptance and
non-goals, and delivers across the layers that own the invariants rather than forcing
the work into one file.

`migration` maps current readers, writers, data shape, compatibility window, and
ownership before editing. It defines a forward and a rollback path, keeps mixed-version
operation safe, and sequences expand, migrate, verify, contract. Destructive steps are
explicit and separately authorized.

`safe-refactor` fixes the behavior-preservation boundary and the proof before it moves
anything, keeps feature changes out, moves one ownership boundary at a time, and keeps
intermediate states buildable. `surgical-patch` reproduces the failure first when that
is economical, traces the symptom to the responsible mechanism, and changes only that
layer. `verify-and-stop` translates acceptance into the smallest sufficient proof,
reuses still-current results, runs focused checks before wide gates, and never edits
product code unless the request included fixes.

### Token cost and memory

`caveman-compress` rewrites a natural-language memory file into caveman speak. The
compressed version overwrites the source, and the readable backup lands at
`<filename>.original.md` outside the source tree. It never modifies fenced code, never
merges sections around code, and never touches source, config, lock, or shell files.
Secret-looking names are refused before the read, and credentials found in the text are
refused before anything is sent.

`caveman-learn` is the consent-gated half of the learn report. It reviews ranked token
sinks, proposes one edit at a time, and measures before and after. `cache_efficiency`
is a rate the other sinks are priced at, never a volume to add. A subagent-spend figure
is visibility only. Any edit that does not lower tokens per turn is reverted, and no
saving is claimed that was not measured.

### Caveman Cloud

`caveman-setup` wires the repository through a byte-preserving proxy in record mode.
The prompt supplies `GATEWAY`, an app slug, and a key, and a missing value is a stop,
never a guess. Find every live callsite, wire it with the provided key from an
environment variable or gitignored file, verify with one real request, and report an
unverified integration as unverified. The failure templates are used verbatim, never
softened.

`caveman-discover` labels LLM workflows so spend groups by job rather than one
`unlabeled-workflow` bucket. It inventories, names, proposes, applies through normal
review, verifies nothing broke, and reports the workflows labeled. `caveman-evidence-review`
is read-only. It loads project context, establishes a baseline, tests the leading
explanation with traces, inspects representative traces, and reports without fetching
prompt or artifact payloads unless asked.

`caveman-manage` inspects an experiment and blocks unsafe execution. It never approves
an experiment with pending results or a missing required field, never converts lift
into `verified_savings`, never supplies an organization id, and never runs a lifecycle
mutation even after user approval. Unknown states and server errors fail closed.
`caveman-optimize` treats report-only observations as diagnostic input, asks the
operator to choose a candidate, designs a paired baseline eval, applies only the
approved candidate, and reports observations rather than savings.

## Output contract

- Name the skill and the mode in the first line of your reasoning and in the todolist.
- Keep the payload. Code, commands, paths, API names, error strings, numbers, and units
  stay verbatim, and negations stay.
- Report the actual result. A measured before and after, a trace id, a cited
  `path:line`, a created file, or a tool response with its key fields.
- State the window a number covers. Never turn a measurement into a projection.
- Keep open work open. A blocked gate, an unverified integration, and an unknown state
  are reported, never rounded up.
- Never claim a saving you did not measure, and never call an estimate verified.
- Redact keys, tokens, prompts, and customer data from any report or public output.
- Write clean as you draft. Short declarative sentences, sentence case headings, no em
  dash, no colon connecting two clauses, no chatbot framing.

## Failure handling

| Situation | Response |
| --- | --- |
| A mode or command is ambiguous | Print the help card. Change no state. |
| A required gateway value is missing | Stop and ask. Never guess a URL or mint a key. |
| A file looks like a secret, or contains a credential | Refuse before reading or sending. Name the rule. |
| An edit does not lower tokens per turn | Revert it and report the measurement. |
| An experiment has pending results or a missing field | Fail closed. Absence is not a pass. |
| A lifecycle mutation is requested | Explain the read-only limit. Emit no executable command. |
| A test, gate, or proof fails | Keep the failure, fix the cause, never weaken the check. |
| The evidence contradicts the requested change | Show the evidence and stop. |

## Provenance

22 `caveman-*` source directories became 22 canonical skills in 6 groups. Each source
had one body, so no merge or variant resolution was needed. Every body is verbatim at
`references/skills/<skill>.md` with its original frontmatter removed, and every other
file from a source pack is copied under `references/assets/<skill>/` at the same
relative path. 26 asset files totaling 104,862 bytes were copied, including the
compression scripts, the reader and skill tests, the two SVG marks, and the per-skill
`README.md` and `agents/openai.yaml` files.

The engineering skills and the voice skills are independent, and the pack does not
require the Caveman Cloud service. Only the five cloud skills need gateway access or
the Cloud MCP, and each fails closed without it.

Upstream author `caveman`. Original catalog paths are preserved in `SOURCES.md` and
under `_archive/caveman/catalog/`.
