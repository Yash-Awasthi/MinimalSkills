<!-- source: catalog/code-quality/rhdh-rhdh-prepare-refinement -->
<!-- source-name: rhdh-rhdh-prepare-refinement -->

# Prepare RHDH refinement

## Route

Load `workflows/prepare-refinement.md`.

## Inputs

1. **Team** — e.g. "Install", "Plugins", "Frontend". Resolve the board ID
   from `/rhdh-jira-api` (references/jql-patterns.md, Boards table).
2. **Fix version(s)** — e.g. "2.1.0" or "all 2.1.x and 2.2.0". Scopes the queue.

If either is missing, ask.

## Boundary with the neighbouring skills

- Per-issue exit-criteria checks, duplicates, comments → `/rhdh-jira-refine`.
- Sprint planning from refined work → `/rhdh-jira-sprint-plan`.
- Opening new issues → `/rhdh-jira-create`.
- Release-wide status across all teams → `/rhdh-release-status`.

## Completion

Complete when the refinement brief is printed to the conversation with analyzed
issues, identified risks, and actionable recommendations. No files written, no
Jira state modified.
