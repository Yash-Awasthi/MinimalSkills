<!-- source: catalog/code-quality/rhdh-rhdh-release-status -->
<!-- source-name: rhdh-rhdh-release-status -->

# RHDH release status

Answer "how is this release doing" with numbers that carry a Jira link and a
timestamp. Read-only: this skill never edits Jira and never posts anything.

## Route

Load `workflows/release-status.md`. It maps each question to the
`scripts/release.py` subcommand that answers it, and carries the two scope rules
the CLI output does not explain on its own.

For readiness at the Feature and Program Increment level rather than the issue
level — "are we ready to ship", PI funnel, dependency map, per-Feature coherence
— load `references/feature-readiness.md` instead. It runs quick mode for ceremony
prep and deep mode for full coherence analysis. Both are read-only.

## Rich Filter ownership

This skill owns the Rich Filter configuration prose. `references/config.md` holds
the spreadsheet IDs, the discovery rule, and the `RHDH_RICH_FILTER_PATH`
override; `references/rich-filter-coverage.md` records which release behaviours
come from the export and which JQL stays local and why. Another skill that hits
an unavailable Rich Filter template names `/rhdh-release-status` rather than
restating the setup.

## Boundary with the neighbouring skills

- Milestone dates — Feature Freeze, Code Freeze, GA — are `/rhdh-release-schedule`.
- Whether a named team can fit the `rhdh-X.Y-candidate` Features through Code
  Freeze is `/rhdh-release-capacity-plan`. This skill reports status, not fit.
- A Slack freeze announcement is `/rhdh-release-announce`.
- The SoS check-in report for team leads is `/rhdh-release-sos`.
- The team roster, leads, and Cloud IDs are `/rhdh-release-teams`. This skill
  counts issues per team; it does not publish the roster.
- Reading a single issue, a board, or a sprint is `/rhdh-jira-api`. Any Jira
  write is `/rhdh-jira-update`.
- Creating, aligning, or deleting **project** fix versions across RHIDP,
  RHDHPLAN, and RHDHBUGS is `/rhdh-release-fixversions`. This skill only
  queries issues by fix version.

## Completion

Complete when every number in the answer names the subcommand or JQL that
produced it, states when it was read, and carries the Jira search link behind it.
A count the
CLI reported as truncated is reported as a floor, not a total. A field Jira could
not supply is listed as unverified — never carried over from an earlier release
or inferred from a neighbouring count. When the Rich Filter was unavailable, say
which scopes went unanswered instead of substituting a hand-written query.
