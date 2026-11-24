---
name: skill
description: >-
  20 skills for authoring, reviewing, hardening, installing, routing, and auditing agent
  skills. Covers skill scaffolding for generic and Azure SDK targets, the two-hook
  activation model, path-based authoring, forcing functions and effect tests, specification
  validation, activation grading and collisions, review loops, eight-dimension
  optimization, pre-install security review, static scanning, full-ecosystem health
  audits, local installation and Antigravity porting, skill routing and history mining,
  plus a capability gap register and a Rails upgrade assessment. Use when a task creates,
  fixes, audits, installs, or routes a skill, or when the user names a skill skill.
metadata:
  curated_from: 20
  skills: 20
  groups: 6
---

# skill

20 skills. 6 groups. One hub. Every source body is preserved verbatim in
`references/skills/<skill>.md`, and every non-SKILL.md file from a source pack sits at
the same relative path under `references/assets/<skill>/`. Load one body for the task.

`SOURCES.md` maps every source path to its canonical skill and group.
`references/INDEX.md` groups the links, `references/skills.tsv` carries every
description, and `references/GUIDE.md` holds the long-form group prose.

## Pack contract

**A skill earns its tokens or it is deleted.** For every paragraph, ask what the model
will do differently because of it. If nothing changes, the line belongs in a reference
that a step names, or nowhere. Length is not the defect. Lines that change nothing are.

**A description is the whole trigger surface.** The agent sees `name` and `description`
before anything else. A perfect body with a vague description never fires. Write the
trigger clause a real user would say, keep the scope boundary, and check for a sibling
that silently wins.

**Review is read-only.** Static review does not install dependencies, execute project
code, sign in, provide credentials, or connect to a real account. Reviewers report what
they observed and mark the rest unverified. Install only an explicitly selected local
tree that the user asked for.

**Fail closed on uncertainty.** An unclear permission, an obfuscated script, or an
unexplained credential path is a reason not to install. Never soften the verdict to be
polite, and never call a project safe, malicious, official, or compliant without
evidence for that specific claim.

**Intent decides a false positive.** Security skills reference attack patterns on
purpose. Judge intent from the surrounding code and output, not from a banned string.
Automated findings are candidates and go to a human.

**Every number has a source or a label.** Scanner coverage, prevalence, incident counts,
time savings, and health scores are claims. Cite the evidence, or label the figure
estimated, illustrative, or unavailable.

**An install needs an explicit target.** Creating a skill does not authorize installing
it, overwriting another skill, installing every discovered candidate, or changing global
agent configuration. Show the plan, then execute only the named target.

**A pass marker is loop control.** The improver's marker ends that loop. It does not
certify safety, tests, provenance, or a merge gate. A blocked tool, an exhausted budget,
and a cancellation are reported as blockers.

**Write clean as you draft.** Short declarative sentences. No em dash. A colon may
introduce a list and may not connect two clauses. Sentence case headings. No chatbot
framing, no generic closer.

## Routing

| The user wants | Group |
| --- | --- |
| A new skill, an SDK skill, a trigger model, or a skill rewritten to bite | Authoring |
| A skill validated, graded, improved against a review, or scored across dimensions | Review and quality |
| A pre-install review, a static scan, or a whole-library security audit | Security |
| A local skill installed, packaged, or ported to another host | Installation and porting |
| A skill recommended for a vague goal, or candidates mined from history | Discovery and routing |
| A capability gap register, or a Rails upgrade assessment | Capability and framework work |

## Full roster

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
## Output contract

- Name the skill and the target skill, host, or file in the first line of your reasoning and in the todolist.
- Report the artifact. A skill path, a check result, a grade, a scan report, an install destination, a register row, or a diff.
- Keep skill names, frontmatter keys, ids, categories, and error strings verbatim.
- State what was static, what was executed, and what stayed unverified.
- Keep open work open. A blocked marker, a skipped dimension, and an unavailable number are reported, never rounded up.
- Never print a secret, token, or private prompt. Redact it and name the rule.
- Write through `unslop`. Short declarative sentences, sentence case headings, no em dash, no colon connecting two clauses, no chatbot framing.

## Failure handling

| Situation | Response |
| --- | --- |
| The skill's trigger is unclear | Rewrite the description with a real user phrase and a scope boundary before touching the body. |
| A reviewer wants to install or execute to check | Stop. Static review is read-only. Report what could not be verified. |
| A security hit could be a legitimate pattern | Judge intent from the code and output. Send the candidate to a human. |
| A number has no source | Label it estimated, illustrative, or unavailable. Never present it as measured. |
| The install target is ambiguous | Ask. Creating a skill does not authorize installing or overwriting one. |
| A review loop cannot continue | Report the blocker: cancellation, missing tool, or exhausted budget. |
| A Rails update would overwrite customization | Show the diff and stop for a decision. |
| The evidence contradicts the requested verdict | Show the evidence and stop. |

## Provenance

20 `sickn33-skill-*` source directories became 20 canonical skills in 6 groups. Each
source had one body, so no merge or variant resolution was needed. Every body is
verbatim at `references/skills/<skill>.md` with its original frontmatter removed, and
every other file from a source pack is copied under `references/assets/<skill>/` at the
same relative path. 66 asset files totaling 448,369 bytes were copied, including the
skill-creator scripts and references, the sentinel analyzer package, the scanner and
installer helpers, the porting script and its test, the upstream licence and notice
files, and the writer's twelve-path reference set.

`skill-gap-analysis` is an HR capability register and `skill-rails-upgrade` is a Rails
upgrade assessment. They share the `sickn33-skill-` prefix but not the authoring
subject, and they stay in their own group rather than being folded into authoring.

Upstream collection `sickn33`. Original catalog paths are preserved in `SOURCES.md` and
under `_archive/skill/catalog/`.
