# workspace

Load for sheets, docs, calendar mechanics and meeting notes.

## email

| class | action | time |
| --- | --- | --- |
| needs a decision from me | reply now, one ask | 2 min |
| needs work | task with a date, archive | 1 min |
| needs someone else | delegate with context, archive | 1 min |
| informational | read, archive | 15 sec |
| newsletter | unsubscribe or filter | once |

Reply shape: the answer first, the context second, the ask and deadline last. One ask per message.

## calendar

- Every meeting has an owner, an agenda and a decision to make. No agenda, no meeting.
- Time zones in the invite text, not only in the client.
- Buffer 10 minutes between calls; back-to-back loses the notes.
- Focus blocks are meetings with yourself: decline conflicts.
- Recurring meeting with no decision in three sessions: cancel it.

## sheets

```gs
=QUERY(A:D, "select A, sum(D) where B = 'paid' group by A label sum(D) 'total'", 1)
=XLOOKUP(A2, Config!A:A, Config!B:B, "missing")
=ARRAYFORMULA(IF(A2:A="",,A2:A*B2:B))
=IFERROR(VLOOKUP(A2, Ref!A:C, 3, FALSE), "not found")
```

- Header row frozen, one table per tab, no merged cells in data.
- Units in the header: `amount_cents`, not `amount`.
- A hardcoded date in a formula is a future bug: put it in a config cell.
- Named ranges for anything referenced twice.
- Numbers right aligned, text left, one decimal convention per column.

## docs

- Title, one-line purpose, decision, open questions. In that order.
- A doc with two owners has none: name one.
- Decisions go at the top, discussion below. A reader should stop after the first screen.
- Every doc has a review date. An undated doc is a claim about the past.

## meeting notes

```
date, attendees, absent
decisions: what was decided, by whom
actions: owner, what, when
open: what needs another session
```

Send within an hour. A summary that quotes the decision, not the discussion.

## tasks

- One list, one owner per item, one date.
- A task without a verb is a topic.
- Weekly review: close, reschedule or delete. A list that only grows stops being read.

## meeting note

```
date:     2026-11-24, 14:00-14:30 UTC
decision: ship the export behind a flag on 2026-12-01
owner:    ada
next:     flag config in the release branch, review on 2026-11-27
open:     csv encoding, unresolved
```

A note without a decision and an owner is a transcript.

## sheet formulas

- `=SUMIFS(D:D, B:B, "open", C:C, ">="&DATE(2026,11,1))` sums one condition set.
- `=XLOOKUP(A2, Rates!A:A, Rates!B:B, "missing", 0)` replaces the VLOOKUP column index.
- `=IFERROR(1/(1/rate), 0)` guards a divide without hiding the error type.
- Freeze the header row, one table per tab, no merged cells in data, units in the header.
- A formula with a hardcoded date is a future bug. Point it at a named range.

## chat

```text
#ops (channel, decision)
"Decision: export ships behind a flag on 2026-12-01. Owner: ada. Detail in the thread."
  thread: "Flag is export_v2. Rollout 5% -> 25% -> 100% over 3 days. Rollback: flag off."
```

- A decision goes in the channel, the detail in the thread. A decision buried in a thread is not a decision.
- Never DM a decision; copy it to the channel or the doc the same day.
- `@here` only for something that needs action in the next hour.

## knowledge base page

```text
# Reconciliation runbook
Owner: ada   Updated: 2026-11-24   Review: 2027-02-24
## When to use   month-end close, or an unmatched payment older than 2 days
## Steps         1 run query  2 match on amount and date  3 post the adjustment  4 log it
## Escalate      finance-ops@, page on-call if close is within 24h
```

- Every page has an owner, an updated date and a review date. A page with no owner is deleted at the next cleanup.
- Steps are numbered commands, not descriptions. A runbook that says "investigate" is a note, not a runbook.
- The escalate line names a channel and a trigger. Without it the reader improvises.

## career and personal

- 1:1 note: wins since last time, one blocker, one ask, one decision. Three lines, sent before the meeting.
- Review doc: impact with numbers, scope, and what you would do differently. A review without numbers is a self-assessment.
- Travel: arrive the day before a morning meeting, buffer 90 minutes on each side, never book the last flight of the day.
- A recurring personal block (deep work, gym) is a calendar event, not an intention.
## workspace index

| surface | the rule that matters |
| --- | --- |
| Gmail | Labels are filters, not folders; a filter that skips the inbox is the only triage that scales; `+alias` per service for filtering. |
| Notion | A database is the source of truth, a page is a view; a relation beats a duplicated select. |
| Obsidian | Plain markdown plus backlinks; a daily note is a scratchpad, the decision log is a separate page with a date. |
| Notifications | Batch to two windows a day, mute channels, one alert channel that pages; a notification with no action is noise. |
| Registers | Decision log, risk log, holiday calendar: each entry has an owner and a date, or it is a note. |
| Job search | One tracker with stage, contact, next action and date; a role with no next action is dead. |
| Tools and automation | Zapier or n8n for the repeatable path, a manual fallback documented; an automation with no owner breaks silently. |
| Workflow | Capture, clarify, organise, review; an inbox that is never reviewed is storage. |
| Systems | One system per job: tasks in one tool, docs in one, chat in one; a second system for the same job is where work gets lost. |
| General | Reply to the person, not the thread; a thread with no owner dies. |
| GIFs | A GIF in a status update is decoration; in a bug report it is evidence, so keep it under 5MB and name the step. |
