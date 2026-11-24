<!-- source: catalog/product-management/rhdh-rhdh-jira-sprint-plan -->
<!-- source-name: rhdh-rhdh-jira-sprint-plan -->

# Plan an RHDH sprint

Produce the numbers a planning call needs, before the call. Read-only until the
team decides something.

## Route

Load `workflows/plan-sprint.md`. Run it before each bi-weekly sprint planning
call.

## Boundary with the neighbouring skills

- The review of the sprint that just ended — committed versus completed,
  per-member results, demo checklist — is `/rhdh-jira-sprint-report`. This skill
  looks forward; that one looks back.
- Making the backlog worth planning from is `/rhdh-jira-refine`.
- Pre-refinement ceremony analysis and facilitator brief is
  `/rhdh-prepare-refinement`.
- Picking and setting an assignee is `/rhdh-jira-update`. This skill invokes it
  for fill suggestions rather than scoring assignees itself.
- Board IDs, sprint naming, JQL, and the Team field's JQL limitation are
  `/rhdh-jira-api`.
- Whether a team can fit `rhdh-X.Y-candidate` Features through Code Freeze is
  `/rhdh-release-capacity-plan`. This skill fills the next sprint only.
- Release-level readiness is `/rhdh-release-status`.

## Completion

Complete when velocity names the three sprints it averaged, carryover names every
issue counted, and available capacity shows the subtraction that produced it.
Report the JQL behind each number and whether any search was truncated. Say when
story-point coverage is too thin to trust a velocity figure rather than
publishing a number that looks solid. Fill suggestions are presented as
suggestions — team members self-select during planning, and nothing here assigns
anyone without approval.
