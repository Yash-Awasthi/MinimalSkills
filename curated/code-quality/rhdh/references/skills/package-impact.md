<!-- source: catalog/code-quality/rhdh-rhdh-package-impact -->
<!-- source-name: rhdh-rhdh-package-impact -->

# RHDH package impact

For a **workspace** under a plugins monorepo checkout (`rhdh-plugins` or
`community-plugins`): discover Dependabot packages, classify impact, check patch
status, bump when needed, and dismiss only when policy allows.

Dismissal targets exact `RUNNER`, `PLUGIN_DEV`, or `WORKSPACE_DEV` — never
`PLUGIN_PROD`.

## Route

| Intent | Load |
| --- | --- |
| Classify / patch-status / report | [workflows/assess.md](workflows/assess.md) |
| Prepare branch + yarn bump + PR tables | [workflows/bump-workspace.md](workflows/bump-workspace.md) |
| Close Dependabot alerts | [workflows/dismiss-alerts.md](workflows/dismiss-alerts.md) |

References (on demand):

- [classifications.md](references/classifications.md) — labels and verdicts
- [dismissal-policy.md](references/dismissal-policy.md) — A/B/C hard rules
- [repo-layouts.md](references/repo-layouts.md) — `--repo-root`, tokens, future `rhdh`

## Fullsend default

```bash
SKILL_DIR=<this skill directory>
node "$SKILL_DIR/scripts/workspace-cve-bump.js" \
  --repo-root "$REPO" --workspace <workspace> --json --dry-run
```

After `/mutation-gate` approval, drop `--dry-run`, commit on the prepared
branch, then open with `/rhdh-pr-mr` using `prTitle` / `prBody` from the JSON.
Exit `2` means partial leftovers — stop for a human; do not invent ancestor
bumps outside the allowlist.

## Do not reimplement

Run the scripts under `scripts/`. Do not hand-assemble Dependabot dismiss lists
or CVE PR tables in chat. Auth for Dependabot is `GH_TOKEN` / `GITHUB_TOKEN`
through these scripts (GitHub REST), not ad-hoc `gh api` scraping.

## Writing rules

Cite `/mutation-gate` for bump, dismiss, push, and PR open. Cite `/rhdh-pr-mr`
to publish. Never dismiss `PLUGIN_PROD`. Never `yarn up` `@backstage/*` or
`@backstage-community/*` (scripts skip them).

## Completion

Assess: classification or patch-status table (or JSON) for every package, with
dismiss vs bump recommendation. Bump: version before/after, status per package,
`prTitle`/`prBody` when opening a PR, exit `2` called out when leftovers remain.
Dismiss: every alert outcome reported, including skipped. No token in output.
