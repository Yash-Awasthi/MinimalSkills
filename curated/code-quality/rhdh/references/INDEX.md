# RHDH skill index

72 skills in 8 groups. Load one skill for the task.

| Group | Skills |
| --- | --- |
| **Foundations & routing** | 4 |
| **OpenSpec workflow** | 13 |
| **Jira & planning** | 9 |
| **Release & Konflux** | 11 |
| **Plugins & Backstage** | 13 |
| **PR, CI & testing** | 11 |
| **Local, platform & docs** | 6 |
| **Authoring & prose** | 5 |

## Foundations & routing

| Skill | Purpose |
| --- | --- |
| [`ask-rhdh`](skills/ask-rhdh.md) | Human wayfinder for the RHDH skills collection. |
| [`context`](skills/context.md) | Resolves the environment the other RHDH skills start from and hands back one JSON document: which RHDH repositories are checked out and where — rhdh, rhdh-operator, rhdh-plugins, rhdh-plugin-export-overlays, rhdh-plugin-catalog, rhdh-cli... |
| [`forge`](skills/forge.md) | Reads GitHub and GitLab and constructs unexecuted forge payloads for the other RHDH skills: parse an issue, pull request, or merge request reference, fetch issue detail, resolve a plugin workspace, inspect checks or pipelines, read repos... |
| [`setup-rhdh-skills`](skills/setup-rhdh-skills.md) | Install, configure, diagnose, or repair the complete RHDH skills environment. |


## OpenSpec workflow

| Skill | Purpose |
| --- | --- |
| [`openspec-apply-change`](skills/openspec-apply-change.md) | Implements the pending tasks of an OpenSpec change against its proposal, specs, and design, looping until done or blocked. Use for "implement this change", "start/continue implementing", "work through the tasks", or "keep going on <chang... |
| [`openspec-archive-change`](skills/openspec-archive-change.md) | Archives a completed OpenSpec change into openspec/changes/archive/, after confirming artifact and task completion and offering to sync any delta specs into the main specs first. Use for "archive this change", "finalize <change>", or "th... |
| [`openspec-audit-change`](skills/openspec-audit-change.md) | Adversarially audits an OpenSpec change's artifacts against each other — and lightly against the codebase and repository conventions — for cross-artifact consistency before implementation. Use for "audit this change" or "run the audit".... |
| [`openspec-bulk-archive-change`](skills/openspec-bulk-archive-change.md) | Archives several completed OpenSpec changes in one batch, detecting and agentically resolving spec conflicts by checking the codebase for what is actually implemented. Use for "archive these changes", "clean up finished changes", or "arc... |
| [`openspec-continue-change`](skills/openspec-continue-change.md) | Creates exactly the next ready OpenSpec artifact for a change, one at a time — proposal, then specs or design (siblings), then tasks. Use for "what's the next artifact", "create the next artifact", "draft the next OpenSpec file", or when... |
| [`openspec-explore`](skills/openspec-explore.md) | Enters explore mode — a thinking partner for investigating problems, comparing options, and clarifying requirements before or during an OpenSpec change. Use when the user wants to think something through, is stuck mid-implementation, or... |
| [`openspec-ff-change`](skills/openspec-ff-change.md) | Fast-forwards an OpenSpec change by generating every remaining artifact needed before implementation — proposal, specs, design, and tasks — in one pass, for a brand-new or an existing change, with progress tracked via TodoWrite. Use for... |
| [`openspec-journal`](skills/openspec-journal.md) | Owns the append-only interaction journal for an OpenSpec change — `openspec/changes/<change>/journal.jsonl` — and the fixed event vocabulary written to it (change.created, artifact.added/revised, mode.chosen, task.start/complete/blocked,... |
| [`openspec-new-change`](skills/openspec-new-change.md) | Scaffolds a new OpenSpec change directory and shows the first artifact's template without writing it. Use for "start a new change", "scaffold a change", "set up a change for X", or "what's the first artifact I need" — when the user wants... |
| [`openspec-onboard`](skills/openspec-onboard.md) | Guided, narrated walkthrough of one complete OpenSpec cycle — explore, create a change, build proposal then sibling specs/design then tasks, implement, archive — using a real small task in the user's own codebase. Use for "walk me throug... |
| [`openspec-sync-specs`](skills/openspec-sync-specs.md) | Syncs a change's delta specs into the long-lived main specs under openspec/specs/, without archiving the change. Use for "sync specs for <change>", "update main specs with these changes", or as a step inside openspec-archive-change/opens... |
| [`openspec-verify-change`](skills/openspec-verify-change.md) | Verifies that an implementation matches its OpenSpec change's artifacts — completeness (tasks, spec coverage), correctness (requirement and scenario coverage), and coherence (design adherence, pattern consistency) — post-implementation,... |
| [`spec-driven-schema`](skills/spec-driven-schema.md) | Owns RHDH's project-local OpenSpec workflow definition — the `rhdh-spec-driven` schema (proposal -> {specs, design} -> tasks -> apply), its four artifact templates, the Canonical Touchpoints rule that ties a change back to `specification... |


## Jira & planning

| Skill | Purpose |
| --- | --- |
| [`jira-api`](skills/jira-api.md) | Reads RHDH Jira and owns the mechanics every other RHDH Jira skill needs: `acli` flags and their traps, JQL for RHIDP, RHDHPLAN, RHDHBUGS and RHDHSUPP, custom field IDs, GraphQL and REST fallbacks, board and sprint IDs, the component cat... |
| [`jira-authoring`](skills/jira-authoring.md) | Supplies the craft of writing good RHDH Jira work in RHIDP, RHDHPLAN, RHDHBUGS, and RHDHSUPP: the Feature, Epic, Story, Task, and Bug description templates with filled examples, the RHDH challenge matrix that stress-tests scope, sizing,... |
| [`jira-create`](skills/jira-create.md) | Opens new work in RHDH Jira and decides what kind of work it is — Feature or Feature Request in RHDHPLAN, Epic, Story, Task, Spike or Vulnerability in RHIDP, Bug in RHDHBUGS, support conversation in RHDHSUPP — then interviews, drafts, an... |
| [`jira-link`](skills/jira-link.md) | Ties a GitHub pull request or GitLab merge request to an RHDH Jira issue in RHIDP, RHDHPLAN, RHDHBUGS, or RHDHSUPP: attach the Jira Web link titled `repo #N: <title>`, post or update the structured comment, fill empty issue fields, move... |
| [`jira-refine`](skills/jira-refine.md) | Judges whether RHDH Jira work that already exists is ready to move forward — in RHIDP, RHDHPLAN, RHDHBUGS, and RHDHSUPP. Checks an issue, a JQL result, a sprint, or a backlog against the exit criteria for its status, then reports missing... |
| [`jira-sprint-plan`](skills/jira-sprint-plan.md) | Builds the planning package for an RHDH scrum team's next sprint from Jira RHIDP, RHDHPLAN, RHDHBUGS, and RHDHSUPP: carryover from the active sprint, three-sprint velocity, per-member capacity, the ready-for-planning queue, available cap... |
| [`jira-sprint-report`](skills/jira-sprint-report.md) | Summarizes an RHDH sprint that has finished or is finishing, from Jira RHIDP, RHDHPLAN, RHDHBUGS, and RHDHSUPP: committed versus completed story points, scope added mid-sprint, per-member breakdown, epic progress, the demo checklist with... |
| [`jira-update`](skills/jira-update.md) | Changes an RHDH Jira issue you already have a key for, in RHIDP, RHDHPLAN, RHDHBUGS, or RHDHSUPP: post a progress comment, transition status, add an issue link or a web link to a PR, close with a resolution and rationale, and pick and se... |
| [`prepare-refinement`](skills/prepare-refinement.md) | Intelligent refinement brief for RHDH scrum teams. Analyzes the queue, surfaces non-obvious risks (scope unclear, blockers, stale work, timeline unrealistic), identifies patterns, and makes recommendations about what to discuss. Say "pre... |


## Release & Konflux

| Skill | Purpose |
| --- | --- |
| [`backport`](skills/backport.md) | Automate the RHDH plugin backport process from PR cherry-pick to changelog. Handles: cherry-pick with AI conflict resolution, PR creation, CI monitoring, auto-merge, Version Packages detection, and overlays update. Pre-2.1: release-x.y/{... |
| [`konflux-rpa`](skills/konflux-rpa.md) | Updates the RHDH ReleasePlanAdmission tag values in konflux-release-data for one patch release while preserving stream tags and plugin version suffixes. Use for "update the RHDH RPA tags for 1.9.7". |
| [`konflux-tasks`](skills/konflux-tasks.md) | Bumps Konflux Tekton task bundle digests in `.tekton` and `.tekton-templates`, applies each task's MIGRATION.md, regenerates PipelineRuns, and checks pins against data-acceptable-bundles so ECP does not reject expired or untrusted tag@sh... |
| [`release-announce`](skills/release-announce.md) | Drafts the Slack message for an RHDH Feature Freeze or Code Freeze — either the milestone announcement sent on the day or the status update sent ahead of it — filling team counts, blocker bugs, CVEs, release notes, feature demos, and Tes... |
| [`release-capacity-plan`](skills/release-capacity-plan.md) | Forecasts whether a named RHDH scrum team can take the rhdh-X.Y-candidate Features for a release from Jira RHIDP, RHDHPLAN, RHDHBUGS, and RHDHSUPP: three-week remaining sprints through Code Freeze, PTO from the shared calendar, sample-sp... |
| [`release-date-update`](skills/release-date-update.md) | Diffs RHDH milestone dates (Feature Freeze, Code Freeze, GA, targeted Backstage version) from the RHDHPLAN release Feature in Jira and the RHDH release schedule spreadsheet against release-schedule.yaml in redhat-developer/rhdh-plugin-ex... |
| [`release-fixversions`](skills/release-fixversions.md) | Lists and synchronizes Jira fix versions across RHIDP, RHDHPLAN, and RHDHBUGS using the invoker's local Jira credentials — create missing versions, align dates and released or archived flags, and delete or archive orphans when explicitly... |
| [`release-schedule`](skills/release-schedule.md) | Gives the milestone dates for an RHDH version — Feature Freeze, Code Freeze, Docs Input Freeze, Docs Freeze, Go/No Go & Push, and GA announce — reading active releases from the RHDHPLAN release Feature in Jira and planned ones from the R... |
| [`release-sos`](skills/release-sos.md) | Builds the RHDH release check-in report for Scrum of Scrums with team leads — milestone calendar, timeline-aware checks from references/sos-checks.md, and Jira counts from the RHIDP Operational Rich Filter. Use for "SoS report for 2.1.0"... |
| [`release-status`](skills/release-status.md) | Reports what is still open against an RHDH release from Jira RHIDP, RHDHPLAN, RHDHBUGS, and RHDHSUPP: issue counts by type, blocker bugs, CVEs, Engineering EPICs, per-team breakdowns, release-note lifecycle, Post Code Freeze scope, and a... |
| [`release-teams`](skills/release-teams.md) | Resolves the RHDH team roster from the RHDH Team Mapping spreadsheet — team name, category, team ID, leads, Slack handles, and the Jira Cloud ID used in `"Team[Team]"` JQL clauses. Use for "who leads the Plugins team", "list RHDH teams",... |


## Plugins & Backstage

| Skill | Purpose |
| --- | --- |
| [`backstage-api-changes`](skills/backstage-api-changes.md) | Names the breaking and notable changes between the early Backstage New Frontend System alpha and the current GA surface, for Red Hat Developer Hub plugins: NavItemBlueprint removed in favour of nav auto-discovery from PageBlueprint, conf... |
| [`backstage-upgrade`](skills/backstage-upgrade.md) | Moves the @backstage/* dependency versions of a Backstage plugin, workspace, app, or the redhat-developer/rhdh monorepo forward to a chosen release, staying within what a Red Hat Developer Hub version ships: read backstage.json and packa... |
| [`overlay`](skills/overlay.md) | Manages the rhdh-plugin-export-overlays repository and Extensions Catalog: onboard plugins, update upstream versions, repair export or publish failures, inspect workspace health, triage the overlay PR backlog by label, staleness and merg... |
| [`overlay-cve-export`](skills/overlay-cve-export.md) | Builds the "RHDH CVE Management - <version>-plugins.csv" export by walking `rhdh-plugin-export-overlays` git history on a release branch since a revision, scoped to generally-available plugin workspaces, then enriching each CVE from Jira... |
| [`package-impact`](skills/package-impact.md) | Classifies whether an npm package in an RHDH plugins monorepo (rhdh-plugins, community-plugins) reaches published plugin code (PLUGIN_PROD), plugin harnesses (PLUGIN_DEV), local runners packages/app\|app-legacy\|backend (RUNNER), or work... |
| [`plugin-authoring`](skills/plugin-authoring.md) | Writes Backstage plugin source for Red Hat Developer Hub in rhdh-plugins or community-plugins: scaffold a backend dynamic plugin with createBackendPlugin or createBackendModule from @backstage/backend-plugin-api, scaffold a frontend dyna... |
| [`plugin-bug-fix`](skills/plugin-bug-fix.md) | Reproduces, diagnoses, and fixes a defect in a Backstage plugin inside the rhdh-plugins or community-plugins repositories: resolve the report from a RHIDP, RHDHBUGS, RHDHPLAN or RHDHSUPP Jira key, a GitHub issue, or plain prose; locate t... |
| [`plugin-catalog-index-status-and-update-flow`](skills/plugin-catalog-index-status-and-update-flow.md) | Reports Red Hat Developer Hub plugin catalog index status for a release branch or x.y.z and updates the downstream quay.io/rhdh/plugin-catalog-index after you approve the push. Reads the upstream Plugin-Catalog-Status wiki and midstream... |
| [`plugin-export`](skills/plugin-export.md) | Turns a Backstage plugin you are developing into a deployable Red Hat Developer Hub dynamic plugin artifact: run @red-hat-developer-hub/cli plugin export to produce dist-dynamic and dist-scalprum, choose shared, embedded and bundled depe... |
| [`plugin-midstream-propagate`](skills/plugin-midstream-propagate.md) | Propagates an rhdh-plugins workspace change through overlays and rhdh-plugin-catalog (midstream): changeset + npm publish, overlays source.json to the Version Packages SHA, then a surgical catalog MR (overlay-repo/, workspaces/, plugin_b... |
| [`plugin-nfs-migration`](skills/plugin-nfs-migration.md) | Converts a legacy Backstage frontend plugin used by Red Hat Developer Hub to the New Frontend System (NFS): replace createPlugin and createRoutableExtension with createFrontendPlugin, PageBlueprint, EntityContentBlueprint, AppDrawerConte... |
| [`plugin-wiring`](skills/plugin-wiring.md) | Generates the Red Hat Developer Hub dynamic-plugins.yaml configuration that makes an exported Backstage frontend plugin appear in RHDH: derive the Scalprum name from plugin-manifest.json or the package name, and write the pluginConfig.dy... |
| [`yarn-bump`](skills/yarn-bump.md) | Bumps Yarn Berry across the RHDH repos — rhdh-plugins, rhdh midstream, rhdh-plugin-export-overlays, rhdh-cli, and GitLab CEE rhidp/rhdh and rhdh-plugin-catalog — with `yarn set version` plus install, and rewrites the pins Yarn cannot see... |


## PR, CI & testing

| Skill | Purpose |
| --- | --- |
| [`operator-pr-test`](skills/operator-pr-test.md) | Tests an rhdh-operator pull request's CI-built operator, operator-bundle, and operator-catalog images on a live OpenShift cluster with oc, and reports evidence plus rollback. Use for "test this operator PR on a cluster", redhat-developer... |
| [`playwright`](skills/playwright.md) | Use when navigating, testing, or verifying a RHDH instance via playwright-cli. Covers guest login, sidebar navigation, catalog browsing, entity page inspection, tab verification, and plugin exploration. Trigger on "check RHDH", "verify c... |
| [`pr-create`](skills/pr-create.md) | Publishes verified changes from rhdh-plugins or community-plugins: detect the repository and affected workspaces, run the repository build pipeline, create package changesets, stage generated files safely, create a signed-off commit and... |
| [`pr-mr`](skills/pr-mr.md) | Pushes a topic branch and opens a GitHub pull request or GitLab CEE merge request for CI and agent automation after validating AI/tool attribution and a linked Jira issue in its description, then links Jira via /rhdh-jira-link. Use for "... |
| [`pr-review`](skills/pr-review.md) | Reviews Red Hat Developer Hub pull request code on GitHub in rhdh, rhdh-operator, rhdh-plugins, or community-plugins. Use for a GitHub PR URL or number, "review this PR", analysis-only review, or posting inline comments. For label and me... |
| [`prow-jobs`](skills/prow-jobs.md) | Lists, generates, and removes RHDH test entries and Hive ClusterPools in the openshift/release Prow ci-operator configuration. Covers OCP `e2e-ocp-vX-Y-helm-nightly` entries, `cluster_claim.version`, the `rhdh-cluster-pool` Hive pools, a... |
| [`prow-release-branch`](skills/prow-release-branch.md) | Commissions or decommissions the openshift/release Prow configuration for a single RHDH release branch: the ci-operator config `redhat-developer-rhdh-release-{version}.yaml`, the jobs `make update` generates from it, the `release-{versio... |
| [`prow-trigger`](skills/prow-trigger.md) | Runs an RHDH nightly ProwJob on demand through the OpenShift CI Gangway REST API, for `periodic-ci-redhat-developer-rhdh-*-nightly` and `periodic-ci-redhat-developer-rhdh-plugin-export-overlays-*-nightly` jobs, with optional image regist... |
| [`smoke-tests`](skills/smoke-tests.md) | Walks RHDH smoke tests: inspect plugin-catalog-index OCI refs first, then Helm and Operator in parallel (one namespace each): install the previous GA, upgrade to this RC, then if this stream is not the newest, upgrade to the latest GA of... |
| [`test-placement`](skills/test-placement.md) | Advises where a permanent automated test for the Red Hat Developer Hub dynamic-plugin ecosystem should live: which repository (rhdh, rhdh-plugins, or rhdh-plugin-export-overlays), which layer (L1 unit, L2 startTestBackend integration, L3... |
| [`test-plan-review`](skills/test-plan-review.md) | Reviews the platform and integration version tables and the key-date table in an RHDH test-plan Jira issue against vendor lifecycle data and the release schedule, then applies the accepted edits. Covers OCP, ARO, OSD, ROSA, AKS, EKS, GKE... |


## Local, platform & docs

| Skill | Purpose |
| --- | --- |
| [`base-images`](skills/base-images.md) | Analyzes and updates the `FROM` base images, Node headers, Go toolchain, and `rpms.lock.yaml` files in rhdh, rhdh-operator, and rhdh-must-gather; pin plugin-catalog `builder.Containerfile` / `.nvm/` / `konflux.additional-tags`; and bump... |
| [`feature-docs`](skills/feature-docs.md) | Generate actual RHDH documentation content (AsciiDoc) for features by analyzing Jira tickets, PRs, and existing docs. Produces ready-to-use documentation files following RHDH docs repository structure, or identifies specific updates need... |
| [`local`](skills/local.md) | Operates a local Red Hat Developer Hub environment with the rhdh-local-setup customization system: enable or disable dynamic plugins, apply configuration, switch pristine and customized modes, start or stop containers, inspect health and... |
| [`platform-lifecycle`](skills/platform-lifecycle.md) | Reports vendor support phases and end-of-life dates for RHDH and the platforms it runs on: OpenShift, ARO, OSD, ROSA, AKS, EKS, GKE, PostgreSQL, Red Hat build of Keycloak, and Quay. Use for "is OCP 4.16 still supported", "when does Postg... |
| [`translation-deploy`](skills/translation-deploy.md) | Downloads completed translations from TMS (Memsource), merges them into locale TypeScript files for rhdh-plugins and community-plugins (update matching keys only), merges backstage/community-plugins/rhdh JSON into rhdh/translations/, and... |
| [`translation-upload`](skills/translation-upload.md) | Extracts translation strings from rhdh-plugins, rhdh, community-plugins, and backstage, compares against the source of truth to find new keys and changed English values, applies RHDH-priority overrides for backstage, and uploads delta re... |


## Authoring & prose

| Skill | Purpose |
| --- | --- |
| [`agent-readiness`](skills/agent-readiness.md) | Assesses and improves a git repository's readiness for AI coding agents with the agentready tool, and reports the score, the certification level, the failing findings, and where the report was written. Covers one repository or every RHDH... |
| [`clean-prose`](skills/clean-prose.md) | Human-only entry point that passes supplied prose or a file path to the pack's prose editor. Use only when a person explicitly invokes /clean-prose. |
| [`mutation-gate`](skills/mutation-gate.md) | Supplies the approval rule another RHDH skill applies when it is already about to change something outside the session: how to state each operation, what approval binds to, what to report afterwards, and how to keep credentials out of a... |
| [`prose-editing`](skills/prose-editing.md) | Edits or audits prose that the caller supplies as text or a file, preserves its claims and voice, removes machine-writing patterns, and verifies the result with the bundled linter. Use for explicit requests such as "rewrite this draft",... |
| [`skill-authoring`](skills/skill-authoring.md) | Creates, audits, and consolidates Agent Skills that follow the Agent Skills open standard, and hands back a drafted or repaired skill with the review checklist for its branch applied. Use for "create a skill", "draft a SKILL.md", "packag... |

