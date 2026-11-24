<!-- source: catalog/product-management/rhdh-rhdh-jira-refine -->
<!-- source-name: rhdh-rhdh-jira-refine -->

# Refine RHDH Jira work

Answer "is this ready" with the criteria the RHDH workflow actually enforces,
and say what is missing rather than guessing at it.

## Route

Load `workflows/refine-issues.md`. It covers both the per-issue readiness audit
and the Feature Exploration checklist — the same checks, applied at different
points in a Feature's life.

## Reads by default, writes only on request

The report is read-only. When the user asks for fixes, each change becomes an
external write: invoke `/mutation-gate` and follow it. A refine pass
typically proposes many small fixes at once, so state them as one set — issue key
and exact command per row — rather than approving them one at a time.

## Boundary with the neighbouring skills

- Opening new work is `/rhdh-jira-create`.
- Updating one known key — status, comment, assignee, link — is
  `/rhdh-jira-update`. Refinement reports across many issues; it does not
  replace that.
- Building the next sprint from the refined backlog is `/rhdh-jira-sprint-plan`.
- Pre-refinement ceremony brief with smart analysis is `/rhdh-prepare-refinement`.
- Exit criteria tables, field IDs, JQL, and the component catalog are
  `/rhdh-jira-api`.
- Sizing scales, duplicate detection, and decomposition rules are
  `/rhdh-jira-authoring`.
- What is still open against a release is `/rhdh-release-status`.

## Completion

Complete when every issue the report covers was actually fetched with its custom
fields enriched — an unenriched search returns empty Story Points, Team, Size,
and Sprint, which looks identical to a field nobody set and is the single most
common source of a false "missing data" finding. Report the JQL, the issue count,
and whether the result was truncated. Every finding names the check that produced
it and its severity. A field that could not be retrieved is reported as
unretrieved, never as missing.
