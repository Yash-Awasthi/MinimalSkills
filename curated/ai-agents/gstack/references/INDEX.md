# gstack command index

71 commands in 8 groups. Load only the command for the task.

| Group | Commands |
| --- | --- |
| **Suite & session** | 15 |
| **Planning & specs** | 13 |
| **Review & quality** | 10 |
| **Ship & deploy** | 7 |
| **QA & browser** | 8 |
| **Design & docs** | 8 |
| **iOS** | 4 |
| **Platform & infra** | 6 |

## Suite & session

| Command | Purpose |
| --- | --- |
| [`alpha`](commands/alpha.md) | Fixture dispatcher with a mode table and forced-read references. |
| [`beta`](commands/beta.md) | Clean fixture tool skill with no forced reads and no mode table. |
| [`captain`](commands/captain.md) | Run a crew of coding agents from one controller (also /crew): lanes send READY blocks and never merge; the controller merges through trains, keeps the digest, relays approvals, fixes flakes daily. (gstack) |
| [`careful`](commands/careful.md) | Safety guardrails for destructive commands. (gstack) |
| [`context-restore`](commands/context-restore.md) | Restore working context saved earlier by /context-save. (gstack) |
| [`context-save`](commands/context-save.md) | Save working context. (gstack) |
| [`freeze`](commands/freeze.md) | Restrict file edits to a specific directory for the session. (gstack) |
| [`garrytan-gstack`](commands/garrytan-gstack.md) | Router for the gstack skill suite. (gstack) |
| [`gstack`](commands/gstack.md) | Install and use gstack in Capy and Claude Code. Load at session start to check this machine, and for gstack planning, code review, debugging, QA, design, security, documentation, and shipping workflows. |
| [`guard`](commands/guard.md) | Full safety mode: destructive command warnings + directory-scoped edits. (gstack) |
| [`health`](commands/health.md) | Code quality dashboard. (gstack) |
| [`pair-agent`](commands/pair-agent.md) | Pair a remote AI agent with your browser. (gstack) |
| [`runaway-stopper`](commands/runaway-stopper.md) | Find runaway Capy threads and subagents, stop or rotate them safely, and prevent repeats. (gstack) |
| [`unfreeze`](commands/unfreeze.md) | Clear the freeze boundary set by /freeze, allowing edits to all directories again. (gstack) |
| [`upgrade`](commands/upgrade.md) | Upgrade gstack to the latest version. |


## Planning & specs

| Command | Purpose |
| --- | --- |
| [`autoplan`](commands/autoplan.md) | Auto-review pipeline — runs the CEO, design, eng and DX reviews in order (lean run: one reviewer), auto-deciding. (gstack) |
| [`office-hours`](commands/office-hours.md) | YC Office Hours — two modes. (gstack) |
| [`openclaw-ceo-review`](commands/openclaw-ceo-review.md) | Use when asked to review a plan, challenge a proposal, run a CEO review, poke holes in an approach, think bigger about scope, or decide whether to expand or reduce the plan. |
| [`openclaw-office-hours`](commands/openclaw-office-hours.md) | Use when asked to brainstorm, evaluate whether an idea is worth building, run office hours, or think through a new product idea or design direction before any code is written. |
| [`openclaw-retro`](commands/openclaw-retro.md) | Weekly engineering retrospective. Analyzes commit history, work patterns, and code quality metrics with persistent history and trend tracking. Team-aware with per-person contributions, praise, and growth areas. Use when asked for weekly... |
| [`plan`](commands/plan.md) | Use before building a feature: challenge the scope, then review architecture, code quality, tests and performance, and end with a plan to build. (gstack) |
| [`plan-ceo-review`](commands/plan-ceo-review.md) | CEO/founder-mode plan review. (gstack) |
| [`plan-design-review`](commands/plan-design-review.md) | Designer's eye plan review — interactive, like CEO and Eng review. (gstack) |
| [`plan-devex-review`](commands/plan-devex-review.md) | Interactive developer experience plan review. (gstack) |
| [`plan-eng-review`](commands/plan-eng-review.md) | Eng manager-mode plan review. (gstack) |
| [`plan-tune`](commands/plan-tune.md) | Self-tuning question sensitivity + developer psychographic for gstack (v1: observational). (gstack) |
| [`retro`](commands/retro.md) | Weekly engineering retrospective. (gstack) |
| [`spec`](commands/spec.md) | Turn vague intent into a precise, executable spec in five phases. (gstack) |


## Review & quality

| Command | Purpose |
| --- | --- |
| [`benchmark`](commands/benchmark.md) | Web performance regression detection. (gstack) |
| [`benchmark-models`](commands/benchmark-models.md) | Cross-model benchmark for gstack skills. (gstack) |
| [`cso`](commands/cso.md) | Security audit: supported static findings; qualified profiles add reproduction and repair candidates. (gstack) |
| [`deslop-shared-libs`](commands/deslop-shared-libs.md) | Find worthwhile shared-code extractions in recent work. (gstack) |
| [`devex-review`](commands/devex-review.md) | Live developer experience audit. (gstack) |
| [`eval-plan`](commands/eval-plan.md) | \| |
| [`modernize`](commands/modernize.md) | Bring an aging PR onto its current base and decide: MODERNIZE, REWORK or CLOSE. (gstack) |
| [`review`](commands/review.md) | Use when you review this PR's diff. (gstack) |
| [`test-audit`](commands/test-audit.md) | Find low-value or duplicate tests and the test-only code they keep alive. (gstack) |
| [`verify`](commands/verify.md) | Use when coding: run the checks and tests /ship picks until green. (gstack) |


## Ship & deploy

| Command | Purpose |
| --- | --- |
| [`canary`](commands/canary.md) | Post-deploy canary monitoring. (gstack) |
| [`document-generate`](commands/document-generate.md) | Generate missing documentation from scratch for a feature, module, or entire project. (gstack) |
| [`document-release`](commands/document-release.md) | Release documentation audit. (gstack) |
| [`land-and-deploy`](commands/land-and-deploy.md) | Land and deploy workflow. (gstack) |
| [`landing-report`](commands/landing-report.md) | Read-only queue dashboard for workspace-aware ship. (gstack) |
| [`setup-deploy`](commands/setup-deploy.md) | Configure deployment settings for /land-and-deploy. |
| [`ship`](commands/ship.md) | Ship it: merge the base, run tests, review the diff, bump VERSION and CHANGELOG, push and create a PR. (gstack) |


## QA & browser

| Command | Purpose |
| --- | --- |
| [`browse`](commands/browse.md) | Drive a real browser through Aside: open a page, read it, click through a flow, take screenshots, check console errors. (gstack) |
| [`hackernews-frontpage`](commands/hackernews-frontpage.md) | Scrape the Hacker News front page (titles, points, comment counts). |
| [`open-gstack-browser`](commands/open-gstack-browser.md) | Launch GStack Browser — AI-controlled Chromium with the sidebar extension baked in. |
| [`qa`](commands/qa.md) | Use when you test the site, API or CLI and fix bugs. (gstack) |
| [`qa-only`](commands/qa-only.md) | Report browser/API/CLI/job/worker/webhook bugs. (gstack) |
| [`scrape`](commands/scrape.md) | Pull data from a web page through the Aside browser — your real, already signed-in sessions. (gstack) |
| [`setup-browser-cookies`](commands/setup-browser-cookies.md) | Import cookies from your real Chromium browser into the headless browse session. (gstack) |
| [`skillify`](commands/skillify.md) | Codify the most recent successful /scrape flow into a permanent browser-skill on disk. (gstack) |


## Design & docs

| Command | Purpose |
| --- | --- |
| [`design-consultation`](commands/design-consultation.md) | Design consultation: understands your product, researches the landscape, proposes a complete design system (aesthetic, typography, color, layout, spacing, motion), and generates font+color preview... (gstack) |
| [`design-html`](commands/design-html.md) | Design finalization: generates production-quality Pretext-native HTML/CSS. (gstack) |
| [`design-motion`](commands/design-motion.md) | Design motion: animate an approved design into a seamless MP4 and GIF loop. (gstack) |
| [`design-review`](commands/design-review.md) | Designer's eye QA: finds visual inconsistency, spacing issues, hierarchy problems, AI slop patterns, and slow interactions — then fixes them; --build checks UI while you build it. (gstack) |
| [`design-shotgun`](commands/design-shotgun.md) | Design shotgun: generate multiple AI design variants, open a comparison board, collect structured feedback, and iterate. (gstack) |
| [`diagram`](commands/diagram.md) | Turn an English description (or mermaid source) into a diagram triplet: the source, an editable .excalidraw file you can open on excalidraw.com, and rendered SVG + PNG. (gstack) |
| [`ios-design-review`](commands/ios-design-review.md) | Visual design audit for iOS apps on real hardware. (gstack) |
| [`make-pdf`](commands/make-pdf.md) | Turn any markdown file into a publication-quality PDF. (gstack) |


## iOS

| Command | Purpose |
| --- | --- |
| [`ios-clean`](commands/ios-clean.md) | Remove the DebugBridge SPM package and all #if DEBUG wiring from an iOS app. (gstack) |
| [`ios-fix`](commands/ios-fix.md) | Autonomous iOS bug fixer. (gstack) |
| [`ios-qa`](commands/ios-qa.md) | Live-device iOS QA for SwiftUI apps. (gstack) |
| [`ios-sync`](commands/ios-sync.md) | Regenerate the iOS debug bridge against the latest upstream gstack templates. (gstack) |


## Platform & infra

| Command | Purpose |
| --- | --- |
| [`codex`](commands/codex.md) | OpenAI Codex CLI wrapper — three modes. (gstack) |
| [`learn`](commands/learn.md) | Manage project learnings. |
| [`setup-gbrain`](commands/setup-gbrain.md) | Set up gbrain for this coding agent: install the CLI, initialize a local PGLite or Supabase brain, register MCP, capture per-remote trust policy. (gstack) |
| [`sync-gbrain`](commands/sync-gbrain.md) | Keep gbrain current with this repo's code and refresh agent search guidance in CLAUDE.md. (gstack) |
| [`ubicloud`](commands/ubicloud.md) | Run a heavy suite, build or eval on an ephemeral 16-vCPU Ubicloud VM: TTL-named VMs, a reaper, quota preflight and a hang watchdog. (gstack) |
| [`write-skill`](commands/write-skill.md) | Write a new agent skill or improve one without bloat: the edit ladder, levels, drift and size checks, full diets. (gstack) |

