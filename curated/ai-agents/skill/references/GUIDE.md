# skill guide

The long-form group prose and the full roster. `SKILL.md` is the loadable hub, and
`references/skills/<skill>.md` is the verbatim body to follow for one task.

### Authoring

| Skill | What it does |
| --- | --- |
| [`creator`](references/skills/creator.md) | Scaffolds a skill draft with bundled Python helpers for init, frontmatter validation, and ZIP packaging, and a detailed authoring guide. |
| [`creator-ms`](references/skills/creator-ms.md) | Creates SDK and API skills that target Azure SDKs and Microsoft Foundry, starting from the real package, language, version, and docs. |
| [`developer`](references/skills/developer.md) | Explains the two-hook activation system and the skill types, then adds a skill file and its trigger rules for Claude Code. |
| [`seekers`](references/skills/seekers.md) | Converts approved docs, a repository, or a PDF into a skill with the Skill Seekers workflow, then reviews the generated output. |
| [`skill`](references/skills/skill.md) | Writes or audits a skill against one test, does the model act differently, using forcing functions, triggerable descriptions, and a static health score. |
| [`writer`](references/skills/writer.md) | Runs a path-based authoring workflow: resolve the target, synthesize, iterate, author, optimize the description, evaluate, and validate. |

### Review and quality

| Skill | What it does |
| --- | --- |
| [`audit`](references/skills/audit.md) | A six-phase pre-install review of a skill's content, scripts, permissions, social engineering, repo, and verdict. Fails closed. |
| [`check`](references/skills/check.md) | Validates a SKILL.md against the agentskills specification and Anthropic practice, with structural, semantic, naming, and quality checks. |
| [`improver`](references/skills/improver.md) | Runs a fix-review loop with the skill-reviewer agent until the skill clears its quality bar, and reports any blocked stop. |
| [`issue`](references/skills/issue.md) | Grades each SKILL.md A to F on activation, simulates which skill a prompt fires, and flags collisions where one shadows another. |
| [`optimizer`](references/skills/optimizer.md) | Scores a skill across eight dimensions with session data and static analysis, including the four dimensions people skip. |

### Security

| Skill | What it does |
| --- | --- |
| [`scanner`](references/skills/scanner.md) | Scans a skill for prompt injection, dangerous code, excessive permissions, secret exposure, and supply chain risk, with a static helper. |
| [`security-audit`](references/skills/security-audit.md) | Read-only review of a skill, MCP server, connector, or extension by tracing code, dependencies, credentials, data flow, and irreversible actions. |
| [`sentinel`](references/skills/sentinel.md) | Audits a whole skill ecosystem for code quality, security, cost, gaps, duplicates, dependencies, and health trends, with a report database. |

### Installation and porting

| Skill | What it does |
| --- | --- |
| [`installer`](references/skills/installer.md) | Validates and installs an explicitly selected local skill tree, with full-tree registration, backups, and ZIP packaging. |
| [`porter`](references/skills/porter.md) | Previews conservative tool-name translations and copies a complete local bundle for manual adaptation to Google Antigravity. |

### Discovery and routing

| Skill | What it does |
| --- | --- |
| [`router`](references/skills/router.md) | Interviews the user, then recommends at most one primary and two secondary skills with exact invocation syntax. |
| [`suggester`](references/skills/suggester.md) | Mines authorized opencode prompt history for repeated workflows and proposes new skill or command candidates. |

### Capability and framework work

| Skill | What it does |
| --- | --- |
| [`gap-analysis`](references/skills/gap-analysis.md) | Builds a skill gap register with employee, skill area, current and required level, severity, and recommended training. |
| [`rails-upgrade`](references/skills/rails-upgrade.md) | Assesses a Rails app upgrade by checking the version, guides, Rails Diff, JavaScript dependencies, migrations, and merge risk. |
## Group notes

### Authoring

`creator` ships the mechanical path. `scripts/init_skill.py` scaffolds, `quick_validate.py`
checks frontmatter, and `package_skill.py` builds a ZIP. Read
`references/detailed-guide.md` first, then `workflows.md` and `output-patterns.md` as the
task needs them. Verify the target host's own requirements separately, since the pack's
validator is not the host's validator.

`creator-ms` is the Azure SDK and Microsoft Foundry variant. Establish the SDK package,
target language, installed version, and primary documentation from the project or the
user before writing. Ask only for the missing essentials, and keep the examples matched
to the real package version.

`developer` documents an illustrative two-hook activation architecture. It covers
guardrail skills, domain skills, `skill-rules.json`, and trigger testing. The hooks are
advisory examples, not a supported host contract, so verify them against the actual
runtime. Never use editable markers or environment overrides to bypass a real policy
gate.

`writer` selects one path from `references/mode-selection.md`: synthesis, iteration,
authoring, description optimization, evaluation, or registration. Read only the paths the
task needs. Reject shallow output that fails a depth gate or a required artifact check.
Its example folder carries a workflow-process item.

`skill` is the fast path. Distil a workflow from real work, convert each rule into a
required artifact, a gate, or a reference that a step names, and keep `SKILL.md` under
500 lines. Audit statically, then run an effect test. A reference nothing points to is
never read. Mark verified facts and unverified numbers separately, and never let an
unverified number become a rule.

`seekers` turns approved documentation, a repository, or a PDF into a skill. Fix the
source, the allowed extraction scope, the desired trigger, the target agent, and the
output directory first. Check the license, exclude credentials, and never bypass a
source access control.

### Review and quality

`check` parses, validates, scores, and reports against the agentskills specification. It
is read-only and returns warnings, suggestions, and passed checks. `issue` handles the
other failure, a skill that is well written and never fires. It grades activation A to
F, simulates which skill a prompt would select, and shows the margin when two skills
collide.

`improver` loops with the `skill-reviewer` agent from the `plugin-dev` plugin. Critical
and major issues are fixed before minors, and each minor is evaluated rather than
assumed. The completion marker must appear in the output, and "looks good" does not end
the loop. Stop on cancellation, unavailable tooling, or exhausted budget, and report the
blocker.

`optimizer` must run all eight dimensions. Trigger rate, post-invocation reaction,
workflow completion, static quality, false positive rate, undertrigger detection,
cross-skill conflicts, environment consistency, and token economics. The four that are
easy to skip are the valuable ones. A high all-caps directive density is a flag.

`audit` is a manual six-phase framework, not an implemented scanner. Surface scan,
script inspection, permission audit, social engineering check, repo intelligence, then a
verdict. Its upstream prevalence and incident claims are not supported by evidence in
the pack, so do not report them as measured. Uncertainty means recommend against.

### Security

`scanner` runs `scripts/scan_skill.py` and reads the three pattern references. Resolve
the installed skill directory explicitly, run it from a reviewed Python environment with
PyYAML, and do not let it fetch dependencies. Low findings are not reported. Intent
decides whether a hit is a real finding, and the report recommends a scoped review,
more evidence, or no adoption.

`security-audit` traces an unfamiliar skill, MCP server, connector, or extension without
installing it. Follow the code, the dependencies, the permissions, the credentials, the
data flow, and the irreversible actions. The output is one of safe to review further,
review required, or do not install, with the evidence for each. A token path with no
explanation is a blocker.

`sentinel` is the Portuguese-language ecosystem auditor. It scores code quality,
security, cost, gaps, duplicates, dependencies, and documentation, writes to a local
database, and compares against the previous audit. Its analyzers are in
`references/assets/sentinel/scripts/analyzers/`, and `run_audit.py` is the entry point.

### Installation and porting

`installer` works on one explicitly selected local tree. Inspect the `SKILL.md`,
scripts, references, license, and data, run the validator and the dry-run, then install
only if the user asked. It registers the full tree, keeps a backup, and can package or
remove a skill. `--all` discovery expands the read scope and can disclose local
filenames, so use it only on request. Never use `--detect --auto` to install silently.

`porter` adapts a locally obtained Claude Code, Cursor, Codex, or generic bundle for
Google Antigravity. It previews conservative tool-name substitutions and copies the
whole bundle for manual adaptation. A preview is not proof of client compatibility, and
it should not run against a tree that is being edited.

### Discovery and routing

`router` interviews one question at a time, then recommends at most one primary and two
secondary skills with exact invocation syntax. Do not dump the library. Verify the
recommendation against the installed skill before sending it.

`suggester` reads opencode prompt history inside the authorized window, looks for
multi-step sequences of five or more tool calls, and proposes candidates with redacted
excerpts. Tool-call counts and time savings are marked unavailable unless measured.

### Capability and framework work

`gap-analysis` builds a skill gap register with employee, skill area, current level,
required level, gap severity, target date, and recommended training. The default output
is a recommendation, not a database. It records unknown as unknown, creates `.xlsx` only
when asked, and never requests a Notion password or token. It is not payroll, tax, or
legal advice.

`rails-upgrade` assesses a Rails app through its current version, the latest version, the
upgrade guide, Rails Diff, JavaScript dependencies, importmap pins, and required
migrations. Prefer a reviewed selective merge over `rails app:update` when local
customization matters. Always show what would be overwritten before proceeding, and
never overwrite without checking first.
