---
name: rhdh
description: >
  Red Hat Developer Hub engineering operations: 72 project skills for OpenSpec change
  workflow, Jira RHIDP/RHDHPLAN/RHDHBUGS/RHDHSUPP work, sprint and release management,
  Konflux and base images, Backstage plugin authoring, export, wiring, and NFS migration,
  overlays and CVE exports, PR/MR creation and review, Prow CI and smoke tests, local RHDH,
  platform lifecycle, docs and translations, prose editing, and skill authoring. Use when
  working in any RHDH repository or on an RHDH release, plugin, test plan, or Jira issue.
metadata:
  curated_from: 72
  skills: 72
  groups: 8
---

# rhdh

72 RHDH skills. 8 groups. One hub. Every source body preserved verbatim in
`references/skills/<skill>.md`. Load one skill.

## Environment

Before a domain skill needs repository, tool, version, or configuration facts:

```bash
python scripts/context.py --project-root <repo> --json
```

It prints one JSON object: `repositories` as `{name, path}`, `tools` as
`installed|missing|not-probed`, and `configuration` with `targetRhdh`,
`targetBackstage`, and `source`. Source is `user` for `--target-rhdh`, `repository`
for a pinned `backstage.json`, `rhdh-context` for the compatibility matrix. Consume
the whole object and reuse it for the session.

The CLI is bundled, not installed:

```bash
uv run scripts/rhdh status
uv run scripts/rhdh doctor
uv run scripts/rhdh config ...
uv run scripts/rhdh setup submodule ...
uv run scripts/rhdh workspace ...
uv run scripts/rhdh log ...
uv run scripts/rhdh todo ...
```

Missing capability: name it and tell the human to run `/setup-rhdh-skills`. A model
skill cannot invoke that human-only entry point.

Setup doctor, before any branch:

```bash
uv run scripts/setup.py doctor --json
```

It reports installed skills, missing skills, capability status, and configuration
locations. It does not read credentials. Install or repair with
`scripts/setup.py install-plan`, then `scripts/setup.py apply --plan <file> --confirm`.
Credentials stay in the owning tool's store or the OS keyring.

## Write gate

An external write is anything the user cannot undo by closing the session: a pushed
commit, an opened PR or MR, a Jira transition, a posted message, a file changed in
someone else's repository. Reading is not a write. A request to fetch, triage,
analyze, or report approves nothing.

Invoke `mutation-gate` before any external write. State every operation in order:

| Field | Carries |
| --- | --- |
| Target | `owner/repo#412`, `RHIDP-1234`, branch, channel |
| Command | Exact command or request, not a paraphrase |
| Preview | Body, label, field value, or diff that will land |
| Precondition | What must be true; check immediately before, stop the batch if false |
| On failure | What happens to later operations |
| Recovery | How to undo or contain this one after it happens |

Recovery is mandatory and distinct from failure handling. An operation with no undo
says so: "Cannot be undone; the message stays." Silence is not a recovery entry.
Approval binds to the exact stated set. A changed target, extra operation, or edited
body is a new plan. Report each operation as completed, failed, or skipped, in
planned order. Never quietly retry a failed write into a different shape. Large plans
go to a file in the OS temporary directory, never the user's checkout. Credentials
never reach a preview; scan the command before showing it.

## Jira model

- **RHIDP** — engineering: Epic, Story, Task, Spike, Vulnerability.
- **RHDHPLAN** — Feature and Feature Request.
- **RHDHBUGS** — Bug.
- **RHDHSUPP** — support conversation.

Picking the issue type is `jira-create`'s job, not the caller's. Editing or
transitioning an existing key is not creation.

Two silent traps:

1. **Default page size is 30.** Rows past 30 drop with no warning. Pass `--limit 500` or `--paginate` on every bulk search; use `--count` when the total matters.
2. **Custom fields are absent unless requested.** `search --json` and `view KEY --json` return only assignee, issuetype, priority, status, and summary. Story Points, Team, Size, and Sprint come back empty. Enrich with `scripts/parse_issues.py --enrich` or `view KEY --fields '*all' --json` before claiming a field is missing.

A field you could not retrieve is reported as unretrieved, never as empty.

## OpenSpec lifecycle

Schema: `proposal -> {specs, design} -> tasks -> apply`. Project schema files live in
`openspec/config.yaml` and `openspec/schemas/rhdh-spec-driven/`; install with:

```bash
python3 scripts/install_project_schema.py
```

Idempotent; `--force` only to replace a customized copy. Confirm with
`openspec schemas --json`, then omit `--schema` to take the configured default.

Change state: `openspec/changes/<change>/`, with an append-only
`journal.jsonl`. Main specs: `openspec/specs/<capability>/spec.md`. Archive:
`openspec/changes/archive/`. The Canonical Touchpoints rule ties a change back to
`specifications/prd/`, `specifications/adr/`, and the capability spec.

Flow:

| Stage | Skill |
| --- | --- |
| Think, compare options | `openspec-explore` |
| Scaffold the change directory | `openspec-new-change` |
| One artifact at a time | `openspec-continue-change` |
| All remaining artifacts | `openspec-ff-change` |
| Pre-implementation artifact audit | `openspec-audit-change` |
| Implement tasks | `openspec-apply-change` |
| Post-implementation verification | `openspec-verify-change` |
| Merge delta specs into main | `openspec-sync-specs` |
| Archive one or many | `openspec-archive-change`, `openspec-bulk-archive-change` |
| Journal events | `openspec-journal` |
| Learn the whole cycle on a real task | `openspec-onboard` |

`new-change` creates the directory and shows the first template without writing it.
`continue-change` creates exactly one artifact and stops. `apply-change` is not
phase-locked; it can run whenever tasks exist. Archive warns on incomplete artifacts
but does not block; the user decides.

## Release model

Milestones: Feature Freeze, Code Freeze, Docs Input Freeze, Docs Freeze, Go/No Go &
Push, GA announce. Active releases come from the RHDHPLAN release Feature; planned
ones from the RHDH release schedule spreadsheet. Every date names its source. Dates
the two sources disagree on are shown side by side. A source that says TBD is
reported as TBD, never estimated.

Branches: pre-2.1 uses per-plugin `release-x.y/{plugin}`; 2.1 and later use a
unified `release-x.y` branch. Backport modes: `auto` (full workflow), `create` (PR
only, stops for review), `finish` (after manual merge).

Release work splits by verb:

- Dates: `release-schedule`.
- Open work and readiness: `release-status`.
- Team roster and Jira Cloud IDs: `release-teams`.
- Capacity forecast: `release-capacity-plan`.
- Fix versions across projects: `release-fixversions`.
- Propagate dates into `release-schedule.yaml` and `release_calendar.yaml`: `release-date-update`.
- Freeze announcement text: `release-announce`.
- Scrum-of-Scrums report: `release-sos`.
- Backport: `backport`.
- Konflux RPA tags: `konflux-rpa`.

## Plugin pipeline

1. **Author** in `rhdh-plugins` or `community-plugins` with `plugin-authoring`. Scaffold backend dynamic plugins with `createBackendPlugin` or `createBackendModule` from `@backstage/backend-plugin-api`; frontend against Backstage UI (`@backstage/ui`), MUI, Scalprum, `fetchApi`, i18n, and test utilities. Build gates: `yarn tsc:full`, `yarn build:api-reports:only`.
2. **Upgrade Backstage** with `backstage-upgrade`. Read `backstage.json` and `package.json`, pick the target from the RHDH compatibility matrix, run `versions:bump` and `versions:migrate`, preserve the repo's dependency range style.
3. **Migrate to NFS** with `plugin-nfs-migration`. Replace `createPlugin` and `createRoutableExtension` with `createFrontendPlugin`, `PageBlueprint`, `EntityContentBlueprint`, `AppDrawerContentBlueprint`, and `createFrontendModule`. Add the `./alpha` export without breaking legacy consumers.
4. **Export** with `plugin-export`. `@red-hat-developer-hub/cli plugin export` produces `dist-dynamic` and `dist-scalprum`; package as OCI, tgz, or npm; generate SHA-512 or sha256 integrity values.
5. **Wire** with `plugin-wiring`. Derive the Scalprum name from `plugin-manifest.json` or the package name; write `pluginConfig.dynamicPlugins.frontend` with `dynamicRoutes`, `menuItems`, `mountPoints`, `appIcons`, `apiFactories`, `routeBindings`, entity tabs, cards, context menu items, and providers.
6. **Publish and promote** with `pr-create`, then `plugin-midstream-propagate`: changeset and npm publish, overlays `source.json` to the Version Packages SHA, then a surgical catalog MR touching `overlay-repo/`, `workspaces/`, `plugin_builds/`, and `.tekton` PLR tags.

Overlays: `overlay` manages `rhdh-plugin-export-overlays` and the Extensions Catalog
(`source.json`, `plugins-list.yaml`, `backstage.json`, catalog metadata, `/publish`).
`plugin-catalog-index-status-and-update-flow` reports index status and updates
`quay.io/rhdh/plugin-catalog-index` after approval.

Dependency impact classes: `PLUGIN_PROD`, `PLUGIN_DEV`, `RUNNER`,
`WORKSPACE_DEV`. Bump with `yarn up -R`, plus allowlisted ancestor bumps; dismiss
runner-only, plugin-dev-only, and workspace-dev-only Dependabot alerts only when
policy allows.

## PR, CI, and tests

- `pr-create` — verified plugin changes: build, changesets, signed-off commit, branch, push, GitHub PR, optional recordings, Jira link.
- `pr-mr` — topic branch and GitHub PR or GitLab CEE MR for CI and agent automation; validates AI/tool attribution and a linked Jira issue, then links Jira.
- `pr-review` — code review on GitHub in `rhdh`, `rhdh-operator`, `rhdh-plugins`, `community-plugins`; analysis-only or inline comments.
- `jira-link` — attach the Jira Web link `repo #N: <title>`, post the structured comment, fill empty fields, move an RHDHPLAN item to RHIDP, mark merged or closed.
- `prow-jobs` — test entries and Hive ClusterPools in `openshift/release`; OCP `e2e-ocp-vX-Y-helm-nightly`, `cluster_claim.version`, `rhdh-cluster-pool`, AKS/EKS/GKE with `MAPT_KUBERNETES_VERSION`.
- `prow-release-branch` — commission or decommission one release branch: `redhat-developer-rhdh-release-{version}.yaml`, generated jobs, `release-{version}` branch protection, `#rhdh-e2e-alerts-X-Y`, `rhdh-send-alert` Vault webhook.
- `prow-trigger` — on-demand nightly through the OpenShift CI Gangway REST API.
- `smoke-tests` — catalog index OCI refs first, then Helm and Operator in parallel, one namespace each. Install the previous GA, upgrade to this RC, and if this stream is not newest, upgrade to the latest GA of the next minor. Set `global.clusterRouterBase` on every helm command; never `--reuse-values`.
- `operator-pr-test` — CI-built operator, bundle, and catalog images on a live OpenShift cluster with `oc`; report evidence and rollback.

Test placement: repositories `rhdh`, `rhdh-plugins`, `rhdh-plugin-export-overlays`.
Layers: L1 unit, L2 `startTestBackend` integration, L3 React Testing Library
component, L4a cluster-free Playwright, L4b cluster e2e. Advice only; it writes no
test.

## Local, platform, docs

- `local` operates RHDH with `rhdh-local-setup`: enable or disable dynamic plugins, apply configuration, switch pristine and customized modes, start or stop containers, inspect health and logs, verify plugins, back up and restore.
- `platform-lifecycle` reports vendor support phases and EOL for RHDH, OpenShift, ARO, OSD, ROSA, AKS, EKS, GKE, PostgreSQL, Red Hat build of Keycloak, and Quay. Product lifecycle only; RHDH milestones belong to `release-schedule`.
- `base-images` maintains `FROM` images, Node headers, Go toolchain, and `rpms.lock.yaml` in `rhdh`, `rhdh-operator`, and `rhdh-must-gather`; pins plugin-catalog `builder.Containerfile`, `.nvm/`, and `konflux.additional-tags`; bumps overlays `versions.json` `node`.
- `konflux-tasks` bumps Tekton task bundle digests in `.tekton` and `.tekton-templates`, applies each task's `MIGRATION.md`, regenerates PipelineRuns, and checks pins against `data-acceptable-bundles` so ECP does not reject expired or untrusted `tag@sha256` refs (`tasks.unsupported`, `required_untrusted_task_found`).
- `feature-docs` generates AsciiDoc content from Jira, PRs, and existing docs, following the RHDH docs repository structure.
- `translation-upload` extracts strings from `rhdh-plugins`, `rhdh`, `community-plugins`, and `backstage`, applies RHDH-priority overrides for backstage, and uploads delta JSON to TMS (Memsource). English source of truth: `rhdh-plugins/workspaces/translations/sot/`.
- `translation-deploy` downloads completed translations, merges locale TypeScript files (update matching keys only), merges backstage and community JSON into `rhdh/translations/`, and prepares signed-off branches and changesets.

## Authoring and prose

- `skill-authoring` — one skill per trigger phrase; split by verb, never noun; a misrouted write costs more than a misrouted answer. Descriptions under 1024 characters, `SKILL.md` under 500 lines, references one level deep, deterministic work in scripts. Prompt duplication forbidden; code duplication expected. Name `<domain>-<verb>`.
- `prose-editing` — edits or audits caller-supplied prose, preserves claims and voice, removes machine-writing patterns, verifies with the bundled linter. It does not review code or decide content.
- `clean-prose` — human-only entry point that passes text or a file path to `prose-editing`.
- `agent-readiness` — runs `agentready`, reports score, certification level, failing findings, and report path; applies supported fixes across one repo or every RHDH repo under a directory.
- `mutation-gate` — the approval rule above. Not an entry point; it performs no forge, Jira, or repository action itself.

## Skill routing

| Group | Skills |
| --- | --- |
| **Foundations & routing** | `ask-rhdh` `context` `forge` `setup-rhdh-skills` |
| **OpenSpec workflow** | `openspec-apply-change` `openspec-archive-change` `openspec-audit-change` `openspec-bulk-archive-change` `openspec-continue-change` `openspec-explore` `openspec-ff-change` `openspec-journal` `openspec-new-change` `openspec-onboard` `openspec-sync-specs` `openspec-verify-change` `spec-driven-schema` |
| **Jira & planning** | `jira-api` `jira-authoring` `jira-create` `jira-link` `jira-refine` `jira-sprint-plan` `jira-sprint-report` `jira-update` `prepare-refinement` |
| **Release & Konflux** | `backport` `konflux-rpa` `konflux-tasks` `release-announce` `release-capacity-plan` `release-date-update` `release-fixversions` `release-schedule` `release-sos` `release-status` `release-teams` |
| **Plugins & Backstage** | `backstage-api-changes` `backstage-upgrade` `package-impact` `plugin-authoring` `plugin-bug-fix` `plugin-catalog-index-status-and-update-flow` `plugin-export` `plugin-midstream-propagate` `plugin-nfs-migration` `plugin-wiring` `overlay` `overlay-cve-export` `yarn-bump` |
| **PR, CI & testing** | `operator-pr-test` `playwright` `pr-create` `pr-mr` `pr-review` `prow-jobs` `prow-release-branch` `prow-trigger` `smoke-tests` `test-placement` `test-plan-review` |
| **Local, platform & docs** | `base-images` `feature-docs` `local` `platform-lifecycle` `translation-deploy` `translation-upload` |
| **Authoring & prose** | `agent-readiness` `clean-prose` `mutation-gate` `prose-editing` `skill-authoring` |

Full table with descriptions: `references/skills.tsv` (`skill, group, description,
file, source`). Grouped links: `references/INDEX.md`.

Route by outcome:

- "What should I do?" or an ambiguous request → `ask-rhdh`. It names one skill and hands over.
- Repository, tool, or version facts → `context`. Reading GitHub or GitLab → `forge`.
- Install, configure, or repair the pack → `setup-rhdh-skills`.
- Think or compare options → `openspec-explore`. Write a spec → `openspec-new-change`, `openspec-continue-change`, `openspec-ff-change`. Audit or verify → `openspec-audit-change`, `openspec-verify-change`. Implement → `openspec-apply-change`. Finish → `openspec-sync-specs`, `openspec-archive-change`.
- File work → `jira-create`. Judge existing work → `jira-refine`. Sprint prep → `jira-sprint-plan`, `jira-sprint-report`, `prepare-refinement`. Edit an issue → `jira-update`. Tie a PR or MR → `jira-link`. Query mechanics → `jira-api`.
- Release dates → `release-schedule`. Release status → `release-status`. Capacity → `release-capacity-plan`. Announcement → `release-announce`. SoS → `release-sos`. Backport → `backport`.
- Plugin source → `plugin-authoring`. Bug → `plugin-bug-fix`. NFS → `plugin-nfs-migration`. Export → `plugin-export`. Wiring → `plugin-wiring`. Overlay → `overlay`. Promotion → `plugin-midstream-propagate`. CVE CSV → `overlay-cve-export`. Dependabot → `package-impact`. Yarn → `yarn-bump`. Backstage bump → `backstage-upgrade`. API changes → `backstage-api-changes`.
- PR for a plugin change → `pr-create`. PR or MR for CI and automation → `pr-mr`. Code review → `pr-review`. Prow config → `prow-jobs`, `prow-release-branch`. Nightly run → `prow-trigger`. Smoke → `smoke-tests`. Test placement → `test-placement`. Test plan → `test-plan-review`.
- Local instance → `local`. Lifecycle lookup → `platform-lifecycle`. Base images → `base-images`. Docs → `feature-docs`. Translations → `translation-upload`, `translation-deploy`.
- Write or repair a skill → `skill-authoring`. Edit prose → `prose-editing`. Agent readiness → `agent-readiness`. Any external write → `mutation-gate`.

## Output contract

Each skill defines its own completion criteria. Report the pack-level summary line:

```text
skill=<skill>  target=<repo|jira-key|cluster|file>  result=<ok|blocked|skipped>
artifacts=<paths|none>  approvals=<yes|no|n/a>  next=<skill|stop>
```

For a blocked skill, name the missing capability and the exact
`/setup-rhdh-skills <route>` supplying it. For a write, report one outcome per
approved operation in planned order. No narrative.

## Failure handling

| Symptom | Action |
| --- | --- |
| Missing capability | Name it. Human runs `/setup-rhdh-skills <route>`. Do not improvise. |
| Jira count looks low | Page size 30. Add `--limit 500` or `--paginate`; check `--count`. |
| Jira field looks empty | Custom fields were not requested. Enrich or use `--fields '*all'`. |
| OpenSpec schema not found | Run `python3 scripts/install_project_schema.py` in the product repo, then `openspec schemas --json`. |
| Release dates disagree | Show both sources side by side. Never silently reconcile. |
| Milestone is TBD | Report TBD. Never estimate from prior releases. |
| Write has no approval | Stop. State the operation table and get approval for the exact set. |
| Credential in a preview | Remove it before showing. Secrets stay in the keyring or owning tool. |
| `tasks.unsupported` or `required_untrusted_task_found` | Check pins against `data-acceptable-bundles`; use a trusted or unexpired bundle. |
| Pre-2.1 branch shape | Per-plugin `release-x.y/{plugin}`. Do not use the 2.1 unified branch. |
| Smoke test uses `--reuse-values` | Stop. Set `global.clusterRouterBase` on every helm command. |
| Prose linter fails | Fix the reported pattern; preserve claims and voice. |
| Capability still missing at completion | Report it unresolved. Do not close the branch. |

## Provenance

- `SOURCES.md` — all 72 sources, folder, skill, group, reference.
- `references/skills/` — 72 bodies verbatim, source path and original folder in HTML comments.
- `references/INDEX.md` — 8 groups with purpose lines.
- `references/skills.tsv` — 72 rows.
- `references/assets/` — 478 files from all 72 sources: scripts, references, examples, schemas, templates, tests, configs.
