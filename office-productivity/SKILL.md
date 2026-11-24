---
name: office-productivity
description: Use when handling work communication and personal operations: email triage and drafting, calendar and meetings, documents and sheets in a workspace suite, chat and knowledge bases, task tracking, travel and scheduling. Triggers: email, calendar, meeting, spreadsheet, inbox.
---

# office-productivity

## use when

- triage an inbox, draft a reply
- schedule, reschedule, find a slot
- write or restructure a doc or a sheet -> references/workspace.md
- post or summarize in a chat channel
- maintain a task list, a decision log

not for: prose quality in long form (writing-docs), product decisions (strategy-product)

## rules

- Conflict order: recipient safety, then deadline, then brevity; a wrong recipient outranks a late reply.
- Sending is an external write: confirm recipient, body, attachment and time zone before it leaves.
- Never send on someone else's behalf without their explicit instruction in writing.
- One ask per message with a deadline; two asks in one email get one answer.
- A meeting has an agenda, an owner and a recorded decision, or it is declined; the summary quotes the decision and owner, not the discussion.
- Personal data stays out of logs, shared docs and fixtures; reference the record id, not the person.
- Dates are absolute with a zone: 2026-11-25 15:00 UTC, never "tomorrow".

## change

1. Locate: the draft, its recipient list, and every thread or invite that references it.
2. Propose the send or reschedule in one sentence, with the alternative you rejected.
3. Predict before sending: who is affected, which time zone, what the recipient must do.
4. Back up the original draft in context, pinned to the thread it replies to.
5. Apply one concern per message; a correction and a new ask are two messages.
6. Verify: recipient, attachment name and absolute time with zone, read once more.
7. Regress: every attendee or recipient who saw the earlier version.
8. Compare the sent text against the prediction; a wrong recipient stops the send.
9. Report what was sent, to whom and when, then take the next item.

## email

1. Classify: reply now, schedule, delegate, archive, delete.
2. Answer in the first line, context after, the ask and deadline last.
3. Re-read for tone once. Short is not rude.

```text
Subject: Q3 invoice 1042 needs approval by Thu 14:00 UTC

Hi Sam,
Approved. One correction: the PO is PO-8842, not 8841. It went to finance; payment runs Friday 2026-11-27.
No action needed from you unless the PO is wrong.
Ada
```

- The subject states the ask and the deadline; the correction sits in the first line, not paragraph three.

| class | service level |
| --- | --- |
| direct ask from a person | same business day |
| needs a decision from someone else | forward within 1 hour, deadline stated |
| fyi, no action | archive, no reply |

## scheduling

```text
You: Two options, both 30 minutes: Tue 2026-11-25 15:00 UTC, or Wed 2026-11-26 10:00 UTC.
Them: Tue works.
You: invite Tue 15:00-15:30 UTC, agenda in the body, owner named, doc linked.
```

- Two concrete options with a zone beat "when are you free"; a third round is a scheduling failure, and the invite carries the agenda, an owner and a doc.

## notes and sheets

- `=SUMIFS(D:D, B:B, "open", C:C, ">="&DATE(2026,11,1))` sums one condition set.
- `=XLOOKUP(A2, Rates!A:A, Rates!B:B, "missing", 0)` replaces the VLOOKUP column index.
- A formula with a hardcoded date is a future bug; point it at a named range.
- Meeting note: date with time zone, decision, owner, next step, open items.

## chat

- Thread replies for detail, channel for decisions; a decision gets copied to the doc same day.
- Mention a person only when they must act; a broadcast mention is noise.

## check

- [ ] one ask, one deadline, attachment named
- [ ] recipients checked, reply-all not used
- [ ] every absolute time carries its zone

## stop

| condition | action |
| --- | --- |
| send requested on someone's behalf | confirm with that person |
| time proposed without a zone | ask for the zone, do not guess |

## emit

- what was sent, to whom, when
- what was scheduled with the time zone
- what needs a human decision
