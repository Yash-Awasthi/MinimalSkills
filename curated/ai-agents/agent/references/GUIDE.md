# agent guide

The long-form group prose and the full roster. `SKILL.md` is the loadable hub, and
`references/skills/<skill>.md` is the verbatim body to follow for one task.

### Creation and orchestration

| Skill | What it does |
| --- | --- |
| [`creator`](references/skills/creator.md) | Builds a custom subagent plugin: requirements, persona, folder structure, plugin.json, agent file, and an optional routing skill. |
| [`manager-skill`](references/skills/manager-skill.md) | Runs several local CLI agents in separate tmux sessions, with start, stop, log tail, and task assignment inside an authorized workspace. |
| [`orchestration-improve-agent`](references/skills/orchestration-improve-agent.md) | Improves an existing agent through baseline metrics, failure classification, prompt changes, A/B tests, and a rollback path. |
| [`orchestration-multi-agent-optimize`](references/skills/orchestration-multi-agent-optimize.md) | Profiles a multi-agent system, then tunes context, coordination, and cost with measured before and after results. |
| [`orchestrator`](references/skills/orchestrator.md) | Scans installed skills, matches them by capability, coordinates multi-skill workflows, and maintains a registry cache. |
| [`squad`](references/skills/squad.md) | A main orchestrator that routes work to a named squad, compresses each report, and never writes application code or picks sides. |

### Evaluation and QA

| Skill | What it does |
| --- | --- |
| [`evals`](references/skills/evals.md) | Builds unit, tool, end-to-end, and safety eval suites with golden data, an LLM judge, promptfoo config, and a CI gate. |
| [`evaluation`](references/skills/evaluation.md) | Compares agent behavior on versioned cases with explicit verifiers and a declared task distribution, not a public benchmark score. |
| [`evaluation-reporting`](references/skills/evaluation-reporting.md) | Turns eval runs into a report with mutually exclusive outcomes, locked denominators, honest latency and cost, and predeclared gates. |
| [`qa-authoring`](references/skills/qa-authoring.md) | Writes Agent QA tests, suites, and hooks through MCP or CLI while preserving canonical ids and the schema contract. |
| [`qa-debug-fix`](references/skills/qa-debug-fix.md) | Repairs a failed Agent QA run from recorded evidence, with the smallest justified change and no test rewrite to hide a defect. |
| [`qa-result-triage`](references/skills/qa-result-triage.md) | Classifies a failed Agent QA run into one fixed category, with confidence, ownership, and the next evidence-backed action. |

### Memory

| Skill | What it does |
| --- | --- |
| [`memory`](references/skills/memory.md) | A hybrid local memory bank with search, write, read, and stats tools that syncs with project documentation. |
| [`memory-discipline`](references/skills/memory-discipline.md) | Standing rules for when to recall before acting and when to save a decision, correction, or failure, on any backend. |
| [`memory-mcp`](references/skills/memory-mcp.md) | The same memory bank delivered as an MCP server, with setup, tool contracts, and a local-only dashboard. |
| [`memory-systems`](references/skills/memory-systems.md) | Designs tenant-scoped semantic, episodic, and procedural memory, with retrieval, retention, and identity-bound access. |

### Runtime reliability

| Skill | What it does |
| --- | --- |
| [`harness-fault-injection`](references/skills/harness-fault-injection.md) | Injects scheduled sandbox, tool, worker, checkpoint, memory, and orchestration faults to prove recovery and containment. |
| [`observability`](references/skills/observability.md) | Instruments an agent with traces, token and cost metrics, latency, structured logs, SLOs, and PII redaction. |
| [`self-scheduling`](references/skills/self-scheduling.md) | Chooses cron, a systemd timer, a bounded loop, or the host scheduler, with timezone, stop conditions, and an overlap lock. |

### Tools and frameworks

| Skill | What it does |
| --- | --- |
| [`framework-azure-ai-py`](references/skills/framework-azure-ai-py.md) | Builds hosted agents on Azure AI Foundry with the Microsoft Agent Framework Python SDK, async context managers, tools, and threads. |
| [`tool-builder`](references/skills/tool-builder.md) | Designs agent tools from JSON Schema to description, validation, error handling, and the tool-call loop. |

### Media

| Skill | What it does |
| --- | --- |
| [`reels`](references/skills/reels.md) | Finds animation and video references on the 1human network and contributes only with prior owner permission and a reviewed publish scope. |

## Group notes

### Creation and orchestration

`creator` asks for the target host and its supported schema and path before writing
anything. It then generates a persona, scaffolds the plugin folder, writes `plugin.json`
and the agent file, and adds a companion routing skill only when asked. The Prompt
Defense Baseline goes in verbatim. Tool access is never assumed. Bash is granted only
on an explicit request, and Codex and Claude distribution stay blocked in the metadata
until compatible packaging is validated.

`orchestrator` is a Portuguese-language meta-skill. It scans installed skills, matches
by capability, coordinates a multi-skill workflow when two or more match, and maintains
a registry with a hash cache. Discovery is requested and the plan is reviewable. Its
`scripts/scan_registry.py`, `scripts/match_skills.py`, and `scripts/orchestrate.py` do
the work, with `references/capability-taxonomy.md` and
`references/orchestration-patterns.md` behind them.

`orchestration-improve-agent` runs four phases. Baseline metrics, prompt improvements,
test and A/B validation, then a rollback-safe rollout. Do not run hosted evaluations,
message teams, or deploy merely because a phase names them. Keep traces private and
redacted, and cap spend. `orchestration-multi-agent-optimize` profiles the system first,
then tunes context compression, coordination, and cost. Every optimization has a
measured before and after.

`squad` is the main orchestrator over eight named agents. It routes work, receives a
structured report, and relays a compressed summary that links the artifact. It never
writes application code, never makes an architecture decision, never passes a full
report into another agent, and never invokes Max without an explicit request.
`manager-skill` runs local CLI agents in separate tmux sessions inside one authorized
workspace. It starts, stops, tails logs, and assigns tasks, and prepares a scoped plan
for repeated work only when scheduling was requested.

### Evaluation and QA

`evals` builds four layers: unit evals for prompt correctness, tool evals for decision
quality, end-to-end evals for multi-step tasks, and safety evals for adversarial
resistance. It adds an LLM judge, a `promptfooconfig.yaml`, and a CI gate. The example
CI needs pinned action and dependency versions, least-privilege permissions, private
artifacts, and a budget. Never expose provider secrets to untrusted pull request code,
and never deploy to production without approval.

`evaluation` compares observable behavior across versioned cases with explicit
verifiers. Pin the case set, the task distribution, and the harness before the run.
Report uncertainty and errors honestly. Do not infer readiness from a public benchmark
percentage or a generic score threshold. `references/architecture-sketches.md` is
optional reading only when designing a custom harness, and its classes need
application-specific adapters.

`evaluation-reporting` freezes the comparison contract, builds a mutually exclusive
outcome ledger, locks each metric to a denominator, and keeps latency and cost
populations honest. Preserve attempt id, task id or seed, retry index, parent attempt
id, configuration label, outcome, intervention count, duration, cost, evaluator
evidence, and invalid reason. Map the evidence to gates declared before the run, and
report `unavailable` or `inconclusive` instead of inventing a number.

`qa-authoring` writes Agent QA tests, suites, and hooks without inventing schema fields
or ids. Prefer the MCP tools, use `references/agent-qa-contracts.json` for exact fields,
and validate every definition. Never hand-write an id, never use a legacy root config
bucket, and never mutate files outside the configured workspace patterns.

`qa-debug-fix` repairs a failed run from MCP evidence, artifacts, logs, and local
source. The classifier is a hypothesis. Inspect the local files directly, do not infer a
patch from an artifact alone, and never rewrite a test just to make it pass when the
artifact shows a product or runtime defect. `qa-result-triage` assigns one fixed
category from `references/triage-categories.md`, plus confidence, likely ownership, and
the next evidence-backed action. Neither skill invents a screenshot, log, or source
file.

### Memory

`memory` and `memory-mcp` expose the same local hybrid memory bank, the first as a
skill and the second as an MCP server. Both offer `memory_search`, `memory_write`,
`memory_read`, and `memory_stats`, need Node.js 18 or newer, and keep the dashboard off
the network. Write new findings only when persistent storage is authorized, and check
the resulting documentation diff.

`memory-discipline` is the missing half. Recall before acting, save after deciding, and
write an entry that survives a new session. Close a superseded entry with an end date
and a pointer to its replacement instead of deleting it. Show a contradiction with both
dates and ask which holds. An observation becomes policy only when a human confirms it,
a decision record merges, or an authorized owner adopts it. Never save secrets, tokens,
or personal data.

`memory-systems` designs the backend. Semantic records hold facts and preferences,
episodic records hold events, and procedural records hold reusable methods. Bind
persistent access to a verified tenant and user, keep retrieval quality separate from
storage volume, and set a retention limit with the task. Read
`references/detailed-guide.md` before executing, and treat its storage, chunking, and
safety sections as mandatory.

### Runtime reliability

`harness-fault-injection` runs a deterministic fault schedule against a local harness.
Sandbox denial, tool failure, worker restart, checkpoint loss, memory loss, budget
exhaustion, and an orchestration join each have a required observation and an expected
containment. Select the smallest fault set that covers the new recovery logic. Never
retry a side effect unless the tool contract says the key is safe to reuse. A required
fact that disappears means ask or stop.

`observability` covers core metrics, latency split across the full turn, a single model
call, and tool calls, plus tokens, cost, tool success, and retries. It adds
OpenTelemetry traces, tools spans, context propagation, structured logs, SLOs, and PII
redaction. The `llm.*` attributes are custom and are not a claim of current
semantic-convention compliance. Import shared metric definitions once and keep label
values bounded.

`self-scheduling` picks a clock. Cron with a one minute floor, a systemd timer that
survives reboot, a bounded loop when sub-minute timing is required, or the host
scheduler. Scheduling needs a direct request, so preserve timezone, cadence,
notification preference, and stop conditions, and update a matching job rather than
duplicating it. Never install an indefinite model-calling loop by default. Do not
disable sandboxing to dodge an unattended permission prompt, and verify the job fires
before reporting success.

### Tools and frameworks

`tool-builder` treats the schema, the description, validation, and error handling as one
design. A tool that fails silently or wastes tokens is a design defect. Read
`references/detailed-guide.md` before executing. The Python SDK snippet is a historical
sketch, not a copy-and-run client.

`framework-azure-ai-py` builds hosted agents on Azure AI Foundry with the Microsoft Agent
Framework Python SDK. Always use the provider as an async context manager, pin reviewed
package versions in the project lockfile, and follow the current Foundry integration for
model providers and hosted tools. The examples preserve an older Agent Framework
generation and are not verified against the current package. `UPSTREAM-NOTICE.md`
records the pinned sources, licenses, hashes, and import changes, and
`UPSTREAM-LICENSE.txt` is kept with it.

### Media

`reels` uses the 1human network at `https://reels.1human.tech` for an owner-authorized
animation, short-video, motion, or generative-art task. Joining or installing is not
publication permission. New profiles start with `policy.publish: false` and stay paused
until the human reviews the upload scope and enables participation. Show a concrete
proposed scope before publishing, and review the actual artifact, rights, and owner
policy first. Report what was reused, what was built, and any publication performed, and
never present a registration, a scheduled visit, or a demo as an external customer.
