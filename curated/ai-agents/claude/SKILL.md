---
name: claude
description: >-
  12 Claude skills. Covers Claude API and Agent SDK building, Claude Code configuration
  and settings audit, delegated coding sessions, performance monitoring, Claude in Chrome
  repair, SpecKit updates on Windows 11, d3.js visualisation, health record organisation,
  scientific research routing, and an RSVP speed reader. Use when a task builds with
  Claude SDKs, configures or audits Claude Code, delegates a coding task, diagnoses
  slowness or a broken browser bridge, updates SpecKit, makes a d3.js chart, or names
  one of the assistant skills.
metadata:
  curated_from: 12
  skills: 12
  groups: 6
---

# claude

12 skills. 6 groups. One hub. Every source body is preserved verbatim in
`references/skills/<skill>.md`, and every non-SKILL.md file from a source pack sits at
the same relative path under `references/assets/<skill>/`. Load one body for the task.

`SOURCES.md` maps every source path to its canonical skill and group.
`references/INDEX.md` groups the links, `references/skills.tsv` carries every
description, and `references/GUIDE.md` holds the long-form group prose.

## Pack contract

**Scope is the trigger, not the topic.** `api` applies only when the task builds with
the Claude API, Anthropic SDKs, or the Agent SDK, or when code imports
`anthropic`, `@anthropic-ai/sdk`, or `claude_agent_sdk`. It does not apply to general
programming, OpenAI SDK work, or ML and data-science tasks. Read the language-specific
files only after detecting the project language.

**Model and authorization are user-owned.** Choose a model from the user's quality, latency
and budget constraints, and never force a premium model or override an explicitly selected
provider. Resolve exact IDs and capabilities through the account's Models API and the
official model documentation; never invent a dated suffix or promise a cached model
remains available. Confirm authorized scope, destination, and resource budget before
installing SDK or MCP packages, uploading files, creating batches, running tools, or
persisting memory. Keep credentials in approved secret storage, never in source, prompts,
logs, or command history. Uploads and server tools disclose content to an external
provider, so review sensitive data and retention before use.

**Pinned SDKs and bounded requests.** Use a reviewed SDK version and its lockfile. Snippets
may need imports, async context, and application-owned implementations, and no snippet is
a production security boundary. Set request deadlines and bounded retries, turns, tool
calls, and output or storage budgets. SDK permission rules and cwd are not OS isolation.
Tool, document, web, and model output is untrusted input; validate schemas, paths, and
business authority before side effects. Do not execute returned code or install the latest
MCP packages automatically. Streaming improves delivery but does not raise the output
limit, prevent truncation, or guarantee a timeout-free request. Check the final stop
reason and usage, and treat a refusal, partial stream, or token-limit stop as an
unvalidated answer.

**A broad prefix is not a read-only sandbox.** `find` can execute or delete, `gh api` can
POST, PATCH, or DELETE, and `git branch`, `git remote`, and `git tag` have mutating forms.
Build tools such as `make -n`, Gradle, Maven, and package managers may evaluate project
code or write caches. Recommend narrow reviewed commands or purpose-built read tools,
never auto-allow arbitrary arguments because a command is usually observational. Redact
settings and MCP secret values before display, preserve existing deny and ask rules, and
produce a proposal rather than silently installing permissions or servers. Skill
invocation permissions can authorize mutating workflows and are not read-only by name.

**Delegation is explicit and the orchestrator lands.** Use `delegate` only when the human
explicitly asks for a separate Claude Code process or session. The orchestrator writes the
brief, dispatches one bounded task, reviews the diff, and commits. The implementer has no
orchestrator chat history; it loads `CLAUDE.md` but not `AGENTS.md`, so copy every
load-bearing constraint and real gate command into the brief. The relay is documentation
only and `scripts/relay.mjs` is absent; require a separately obtained, pinned, reviewed
upstream runtime and never run a missing local path. Treat the implementer's report and
gate outcomes as claims, review edits to existing tests before a green gate, re-run the
project's gates, read the full diff including untracked and staged content, and resume
the same session with a delta brief for rework. `--read-only` is a reporting tripwire,
not an OS boundary. `--dangerously-skip-permissions` is an explicit opt-in and only
with the human's acceptance. Native Windows has no Claude shell sandbox.

**The browser bridge conflict is macOS-specific and version-sensitive.** Claude.app Cowork
and Claude Code register different native messaging configs and use different socket
formats, so a wrong active config yields "Browser extension is not connected". The paths
are historical observations, not a universal restriction; confirm the active host, versions,
and profile first, and use supported reconnect or repair before changing registrations.
Back up registrations, refuse destination collisions, and do not install the toggle in
shell startup without a request. MCP connects at startup, so restart Chrome and then
Claude Code. Keep the Claude extension in one Chrome profile and run one Claude Code
session at a time. Closing Chrome interrupts unrelated work, so preserve tabs and forms
and obtain authorization. Redact private paths from diagnostics.

**Diagnose before acting.** `monitor` separates local bottlenecks from remote API latency.
Its health check reports CPU, RAM, browsers, Claude Code processes, disk, network latency,
and an automatic diagnosis with `bottleneck`, `severity`, `suggestions`, and a summary.
Thresholds are CPU 60 to 85 percent warning and above 85 critical, RAM 70 to 85 warning,
browser RAM 3 to 6 GB warning, browser processes 30 to 60 warning, free disk 10 to 15
percent warning, and network latency 200 to 500 ms warning. Never close processes without
explicit permission. `api_bench.py` measures DNS, TCP, and TLS handshake only, not local
process behavior, HTTP response, or inference time. Requires Python 3.10+ and a pinned
psutil install, and no API key.

**SpecKit updates preserve locals.** Confirm Windows, PowerShell, Git, and the existing
SpecKit installation, record the installed version, the current diff, and the intended
upstream revision, keep a separate copy of local customizations, review the three-way
changes, and apply only accepted changes inside the project. Never run `specify init
--force` as a shortcut or claim preservation before inspecting the result. No updater
scripts are bundled; if the legacy updater is absent, produce a reviewable migration plan
and do not invent its slash command.

**Visualisation choice is deliberate.** Use `d3js-skill` for custom encodings and layouts,
complex pan, zoom, or brush interaction, network and hierarchy diagrams, custom geographic
projections, choreographed transitions, publication-quality styling, and chart types no
standard library provides. Use Three.js instead of d3.js for 3D visualisation. Read the
bundled detailed guide before executing, and treat its safety, prerequisites, and
validation requirements as mandatory.

**Assistants stay inside their boundaries.** `ally-health` organises supplied notes and
records into a source-linked timeline or appointment summary, separates patient-reported
symptoms from documented findings, marks missing or conflicting records, keeps sensitive
records local unless sharing is authorized, and cites current authoritative sources. It
cannot diagnose, recommend treatment changes, certify wellness, or replace urgent care.
Do not run the workflow when the user reports an apparent medical emergency. The upstream
project redirects to WellAlly-health, and its implementation needs separate review.

`scientific-skills` is a discovery guide. Identify the question, discipline, data,
environment, and evidence, then inspect the specific upstream skill's instructions, files,
dependencies, data licenses, and limits. Do not load the whole library or run unreviewed
scripts. Record methods, package versions, provenance, uncertainty, and actual checks,
and separate reproduced results from proposals or vendor claims. The library now calls
itself Scientific Agent Skills.

`speed-reader` verifies an installed, reviewed upstream reader. `/speed` is documented
only for Claude Code and may not exist in other hosts. Confirm the text, exclude sensitive
response history from external tools unless sharing is authorized, start at a comfortable
adjustable rate, and check that the reader actually opens and displays the intended text.
Merely printing the command is not proof it ran. RSVP presentation rate is not proof of
comprehension, and no browser assets are installed automatically.

## Routing

| The user wants | Group |
| --- | --- |
| Build with the Claude API, Anthropic SDK, or Agent SDK | Claude API and SDK building |
| Configure, document, or audit Claude Code | Claude Code configuration |
| Delegate a coding task to another Claude Code session | Delegation |
| Diagnose slowness, repair the Chrome bridge, or update SpecKit | Diagnostics and repair |
| Build a custom d3.js chart | Visualisation |
| Organise health records, route scientific research, or speed read text | Specialized assistants |

## Full roster

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
## Output contract

- Name the skill, the language or tool version, and the artifact in the first line of your reasoning and in the todolist.
- Report the artifact. A Claude API integration, a CLAUDE.md, a settings.json proposal, a delegation brief or landed diff, a diagnosis, a repaired bridge, a SpecKit review, a d3.js chart, a health timeline, a research route, or a reading session.
- Keep model IDs, SDK versions, endpoint names, environment variable names, thresholds, file paths, and error text verbatim.
- State which SDK and lockfile were used, which requests were bounded, and which stop reason was observed.
- State the active Claude Code host, settings baseline, and whether permissions were proposed or installed.
- Keep open work open. An unmeasured diagnosis, an unverified model capability, a missing relay runtime, and an unaudited diff are reported, never rounded up.
- Never print a secret, an API key, a credential, or private record data. Redact it and name the rule.
- Write through `unslop`. Short declarative sentences, sentence case headings, no em dash, no colon connecting two clauses, no chatbot framing.

## Failure handling

| Situation | Response |
| --- | --- |
| An API task is handled as general coding | Check the SDK import and trigger conditions, or route elsewhere. |
| A model ID or dated suffix was invented | Resolve it through the Models API and official documentation. |
| A snippet is presented as a production security boundary | Add owned auth, deadlines, bounded retries, and validation. |
| A streaming run is called complete | Check the final stop reason and usage. |
| A broad permission prefix is treated as read-only | Narrow the command and verify argument effects. |
| Permissions or MCP servers would be installed silently | Produce a proposal and preserve existing deny and ask rules. |
| Delegation is used without an explicit request | Implement inline or ask the human first. |
| A missing relay runtime is run anyway | Obtain a pinned, reviewed upstream runtime or skip delegation. |
| An implementer gate claim is accepted | Rerun the project gates and inspect the full diff. |
| `--dangerously-skip-permissions` is used without acceptance | Require the human's explicit opt-in. |
| Processes would be closed from a monitor diagnosis | Ask for explicit permission first. |
| A historical Chrome path is treated as current | Confirm host, version, and profile first. |
| `specify init --force` is used to shortcut an update | Inspect and preserve local customizations before applying. |
| A medical emergency is routed through the health workflow | Escalate to urgent care. |
| A diagnosis or treatment is inferred from missing records | Mark the gap and ask for the record. |
| The whole scientific library is loaded | Route to one reviewed skill within scope. |
| The speed reader is claimed to have run | Verify the reader opened and displayed the text. |
| The evidence contradicts the requested claim | Show the evidence and stop. |

## Provenance

12 `sickn33-claude-*` source directories became 12 canonical skills in 6 groups. Each
source had one body, so no merge or variant resolution was needed. Every body is verbatim
at `references/skills/<skill>.md` with its original frontmatter removed. 42 asset files
totaling 353,754 bytes were copied under `references/assets/<skill>/` at the same relative
path.

The canonical name drops the `sickn33-claude-` prefix, so `sickn33-claude-api` becomes
`api`, `sickn33-claude-code-expert` becomes `code-expert`, `sickn33-claude-d3js-skill`
becomes `d3js-skill`, and `sickn33-claude-win11-speckit-update-skill` becomes
`win11-speckit-update-skill`. The 26-file `api` set includes language API and Agent SDK
guides, shared tool-use and error references, live documentation URLs, and a test file.
`code-expert` ships `references/detailed-guide.md`; `d3js-skill` ships its detailed guide,
colour schemes, patterns, scale reference, two JSX templates, and sample data; `delegate`
ships four reference documents; `monitor` ships four scripts. `code-guide`,
`settings-audit`, `ally-health`, `scientific-skills`, `speed-reader`,
`in-chrome-troubleshooting`, and `win11-speckit-update-skill` have no extra files.

The pack keeps the API trigger scope, user-owned model choice, authorization checks,
pinned SDKs, bounded requests, the settings-audit read-only warning, explicit delegation
and orchestrator landing, the monitor permission rule, the macOS-only Chrome repair
with restart ordering, the SpecKit no-force rule, and the medical, scientific, and
reading boundaries. `delegate` is documentation only and `scripts/relay.mjs` is absent.
The Chrome paths are historical observations. `scientific-skills` is a discovery guide,
not a bundled library. `speed-reader` requires an installed upstream reader.

Upstream collection `sickn33`. Original catalog paths are preserved in `SOURCES.md` and
under `_archive/claude/catalog/`.
