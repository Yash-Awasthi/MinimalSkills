<!-- source: catalog/product-management/rhdh-rhdh-jira-sprint-report -->
<!-- source-name: rhdh-rhdh-jira-sprint-report -->

# Report on an RHDH sprint

Say what the sprint actually delivered, with the numbers traceable to a query.
Read-only.

## Route

Load `workflows/summarize-sprint.md`. Run it at the end of a sprint, before the
review and demo meeting.

## Boundary with the neighbouring skills

- Preparing the sprint that has not started — carryover, capacity, ready queue —
  is `/rhdh-jira-sprint-plan`. This skill looks back; that one looks forward.
- Judging whether individual issues are in good shape is `/rhdh-jira-refine`.
- Board IDs, sprint naming, JQL, and custom field IDs are `/rhdh-jira-api`.
- Whether a team can fit `rhdh-X.Y-candidate` Features through Code Freeze is
  `/rhdh-release-capacity-plan`.
- Release-level readiness across sprints is `/rhdh-release-status`.

## Completion

Complete when committed and completed totals name the sprint and the JQL behind
them, the partition into completed, carried over, and added mid-sprint accounts
for every issue in the sprint, and epic progress states both the numerator and
the denominator. Report whether any search was truncated. The per-member
breakdown says out loud that it covers only Jira-tracked work — code review,
documentation, support, and meetings do not appear in it, and someone with zero
completions has not necessarily done nothing.
