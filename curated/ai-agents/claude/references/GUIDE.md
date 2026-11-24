# claude guide

The long-form group prose and the full roster. `SKILL.md` is the loadable hub, and
`references/skills/<skill>.md` is the verbatim body to follow for one task.

### Claude API and SDK building

| Skill | What it does |
| --- | --- |
| [`api`](references/skills/api.md) | Builds Claude API, Anthropic SDK and Agent SDK applications with language detection, surface choice, batching, files, streaming, tool use, and current model verification. |

### Claude Code configuration

| Skill | What it does |
| --- | --- |
| [`code-expert`](references/skills/code-expert.md) | Configures and troubleshoots Claude Code CLI, project instructions, hooks, MCP, permissions, memory, and subagents against installed-version documentation. |
| [`code-guide`](references/skills/code-guide.md) | Writes project CLAUDE.md instructions and defines verified build, test, and debugging workflows without treating instructions as a security boundary. |
| [`settings-audit`](references/skills/settings-audit.md) | Infers a narrow read-only settings.json permission allow list from a repository's stack, tooling, and monorepo layout, and proposes it rather than installing it. |

### Delegation

| Skill | What it does |
| --- | --- |
| [`delegate`](references/skills/delegate.md) | Dispatches one bounded coding task to a separate Claude Code session, then reviews the diff and lands the commit as orchestrator. |

### Diagnostics and repair

| Skill | What it does |
| --- | --- |
| [`in-chrome-troubleshooting`](references/skills/in-chrome-troubleshooting.md) | Resolves Claude in Chrome MCP native-host and socket conflicts on macOS with one profile, one session, and restart ordering. |
| [`monitor`](references/skills/monitor.md) | Diagnoses local versus Claude API slowness through CPU, RAM, browser, disk, and network checks, with optional continuous monitoring. |
| [`win11-speckit-update-skill`](references/skills/win11-speckit-update-skill.md) | Reviews SpecKit updates on Windows 11 with PowerShell while preserving local templates and customizations through a three-way diff. |

### Visualisation

| Skill | What it does |
| --- | --- |
| [`d3js-skill`](references/skills/d3js-skill.md) | Builds custom interactive d3.js data visualisations with scales, patterns, templates, and choreographed transitions. |

### Specialized assistants

| Skill | What it does |
| --- | --- |
| [`ally-health`](references/skills/ally-health.md) | Organises supplied symptom notes and records into a source-linked timeline and clinician questions without diagnosing or prescribing. |
| [`scientific-skills`](references/skills/scientific-skills.md) | Routes a scientific question to the upstream library, reviews the relevant skill and dependencies, and records methods, versions, and provenance. |
| [`speed-reader`](references/skills/speed-reader.md) | Guides an RSVP reader for supplied text at a user-chosen rate, with a verified upstream reader and no comprehension claim. |
## Group notes

### Claude API and SDK building

`api` starts by choosing the simplest surface that meets the task. A single call covers
classification, summarisation, extraction, and Q&A. Batches cover offline generation at
50 percent cost. Claude API plus tool use covers code-controlled workflows. Agent SDK
covers agents that need built-in file, web, terminal, permission, and MCP support. Build
an agent only when complexity, value, viability, and cost of error all justify it.

Detect the project language from files, ask when ambiguous, use cURL for unsupported
languages, and read only the reference files the task needs. Messages use
`POST /v1/messages`, with separate batches, files, model discovery, and token-counting
endpoints. Tool runner handles user-defined tools. Server tools run on Anthropic
infrastructure. Structured outputs use `output_config.format` with
`client.messages.parse()`, and the old `output_format` is deprecated. Anthropic has no
embedding model, so embeddings need a separately approved provider. The 26 bundled files
include language API and Agent SDK guides, shared tool-use and error references, live
documentation URLs, and a test file.

### Claude Code configuration

`code-expert` reads its bundled `references/detailed-guide.md` before execution and treats
its safety, prerequisites, and validation requirements as mandatory. It configures or
troubleshoots Claude Code CLI, project instructions, hooks, MCP connections, permissions,
and supported automation using the installed version's documentation.

`code-guide` reads existing project instructions first and updates `CLAUDE.md` only
within the requested scope, preserving repository conventions. Its React and
TypeScript npm template is illustrative; replace commands and stack rules with verified
project facts. Thinking keywords describe tasks and are not guaranteed reasoning
switches. For debugging, save task state and evidence before a new session, give
explicit paths and outcomes, and check logs or run verbose commands. Use `rg` to
locate files instead of dumping the codebase, iterate in small verified changes,
and correct mistakes immediately. Inspect the resulting diff, confirm the instructions
load in the installed host, keep secrets out of tracked instructions, and check current
memory features against official documentation.

`settings-audit` detects the stack from lock files and config, detects Sentry and Linear
services, reads existing `.claude/settings.json`, and builds a narrow allow list only
for tools actually present. The baseline uses `ls`, `pwd`, `file`, `stat`, `wc`, `head`,
`tail`, `cat`, `tree`, `git status`, `git log`, `git diff`, `git show`, `git branch
--list`, `git remote -v`, `git tag --list`, `git stash list`, `git rev-parse`, and
read-only `gh` views. Stack-specific commands follow detected lock files, and only the
actual package manager is included. Never include absolute paths, project scripts with
side effects, alternative package managers, or install, build, run, write, and delete
commands. The `:*` suffix is broad and its argument effects need verification. MCP
servers belong in `.mcp.json`, and Sentry or Linear configs are suggestions only.

### Delegation

`delegate` casts the current agent as orchestrator and a separate Claude Code CLI session
as implementer. It applies only when the human explicitly asks for delegation, not when
the human asks for direct implementation or the task is small enough to do inline. It
requires an installed and authenticated `claude` CLI, Node 18+, git, and a target
repository passed with `--cd`. The brief is the only context the implementer receives.
Write one task per brief, copy every load-bearing `AGENTS.md` constraint and real gate
command, tell the implementer not to commit, and use the bundled brief, dispatch, review,
and queue references. Dispatch waits for process exit and `result.json`, then reads
`finalMessage`, `touchedFiles`, `resultSubtype`, and artifact paths. A pre-run usage error
exits 2 with no `result.json`; a missing `claude` exits 127 with
`status: "claude_unavailable"`; timeouts preserve an outcome artifact. Review the
complete diff, untracked and staged content, existing test edits, and rerun the project's
actual gates. Land the commit yourself and resume the same session with a delta brief
for rework. The normal profile uses `acceptEdits`, restricts built-in tools to Read,
Glob, Grep, Edit, Write, and the platform shell, enables the shell sandbox on macOS,
Linux, and WSL2, denies MCP tools and connectors, and string-denies direct commit, push,
and nested `claude` forms as a speed bump, not a boundary.

### Diagnostics and repair

`monitor` runs `scripts/health_check.py` for a roughly three-second local diagnosis of
CPU, RAM, browsers, Claude Code processes, disk, network latency, and an automatic
classification with suggestions and a Portuguese summary. It offers corrective actions
but never closes processes without explicit permission. `scripts/monitor.py` records
periodic snapshots with interval, duration, output, CPU alert, and RAM alert options,
then reports peaks, trend, alerts, and a final recommendation. `scripts/api_bench.py`
measures DNS, TCP, and TLS handshake only. The pack ships all four scripts, and the
skill requires Python 3.10+ with a pinned psutil install and no API key.

`in-chrome-troubleshooting` covers macOS only, using `~/Library/Application Support/`
and `osascript`. The primary issue is that Claude.app Cowork and Claude Code CLI register
different native messaging hosts and socket formats. Confirm the active host, versions,
and profile first. Disable the config for the tool not in use, back up registrations,
refuse destination collisions, and use supported repair rather than choosing an
executable by modification time. MCP connects at startup, so restart Chrome, click
the extension icon, verify the host and socket, then restart Claude Code. Other causes
include multiple Chrome profiles, multiple sessions, a hardcoded wrapper version, and
unset `TMPDIR`. The toggle script is illustrative and does not implement the checks.

`win11-speckit-update-skill` is a guide to an archived upstream SpecKit updater, not
Windows administration. No updater scripts are bundled. Confirm Windows, PowerShell, Git,
and the existing SpecKit installation, record the version, current diff, and intended
upstream revision, keep a separate copy of local customizations, review the three-way
changes, and apply only accepted changes. Never run `specify init --force` or claim
preservation before inspecting the result. If the legacy updater is absent, produce a
reviewable migration plan.

### Visualisation

`d3js-skill` uses d3.js for custom encodings and layouts, complex pan, zoom, or brush
interaction, network and hierarchy diagrams, custom geographic projections,
choreographed transitions, publication-quality styling, and novel chart types. Use
Three.js for 3D instead. The skill reads `references/detailed-guide.md` before
execution and treats its safety, prerequisites, and validation requirements as
mandatory. The pack ships the detailed guide, colour schemes, d3 patterns, scale
reference, chart and interactive JSX templates, and sample data.

### Specialized assistants

`ally-health` organises user-supplied symptom notes or records into a source-linked
timeline and clinician questions, separates patient-reported symptoms from documented
findings, marks missing or conflicting records, keeps sensitive records local unless
sharing is authorized, and distinguishes general information from individualized advice.
It cannot diagnose, recommend treatment changes, certify wellness, or replace urgent
care, and it must not delay when the user reports an apparent medical emergency. The
upstream project redirects to WellAlly-health and needs separate review.

`scientific-skills` is a discovery guide, not a bundled scientific library. Identify
the question, discipline, data, environment, and evidence, inspect the specific upstream
skill and its files, dependencies, licenses, and limits, and record methods, versions,
provenance, uncertainty, and checks. Do not load the whole library or run unreviewed
scripts. `speed-reader` verifies an installed, reviewed upstream reader; `/speed` is
documented only for Claude Code. Confirm the text, exclude sensitive history from
external tools, start at a comfortable adjustable rate, and verify the reader actually
opens and displays the text. RSVP rate is not proof of comprehension, and no browser
assets are installed automatically.
