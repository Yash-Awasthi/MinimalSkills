<!-- source: catalog/code-quality/rhdh-rhdh-release-announce -->
<!-- source-name: rhdh-rhdh-release-announce -->

# RHDH freeze announcements

Produce a Slack message a human posts under their own name. The counts come from
the CLI; the voice must not sound machine-written.

## Delivery boundary

Never post to Slack. This skill hands the user a message to copy; the user
decides whether, when, and where it goes out.

## Route

Load `workflows/freeze-announcement.md`. It maps the four announcements to their
CLI tokens and carries the milestone-versus-update distinction, which is the
thing people get wrong.

## Boundary with the neighbouring skills

- The date a freeze falls on is `/rhdh-release-schedule`.
- The underlying counts, on their own and without a message around them, are
  `/rhdh-release-status`.
- The team roster and Slack handles are `/rhdh-release-teams`.
- Rich Filter configuration lives in `/rhdh-release-status`. When the CLI reports
  a template unavailable, run `uv run scripts/release.py --json check`, follow its
  `next_steps`, and retry. Never substitute a hand-written query for a Rich Filter
  scope.

## Completion

Complete when the message is the edited draft, wrapped in a triple-backtick
block ready to paste, with every placeholder filled and every count carrying a
URL-encoded Jira search link. State which of the four announcements was drafted
and whether it is the milestone or the update, so the sender knows what day it
belongs to. A figure the CLI could not produce is named as missing in the note
beside the draft rather than left as a placeholder or filled with a plausible
number. Say explicitly that nothing was posted.
