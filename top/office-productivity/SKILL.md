---
name: office-productivity
description: >
  One standalone skill for office and personal productivity: email systems
  and sequences, Google Workspace automation (Sheets, Calendar, Drive, Docs,
  Slides, Forms), Slack bots and GIFs, Notion and Obsidian knowledge bases,
  meeting distillation, time tracking and ledgers, CV and job search, billing
  and invoicing, spreadsheets, screenshots, workflow automation with
  reliability limits, and notification hubs. Merges the office-productivity
  class (55 skills). Fully self-contained: every procedure is inline, no
  external references.
metadata:
  merges: office-productivity
  sources: 55
---

# office-productivity

## 0. Iron laws

1. **An automation is a side effect.** Sending email, creating events,
   writing to a sheet, posting to Slack or importing to Notion changes real
   state. Confirm the target account, the scope and the authorization before
   the write. Never send to a recipient list without explicit approval.
2. **Supporting material is declared, not assumed.** Gmail and Google Drive
   automations declare their supporting-material availability; a missing
   dependency fails closed — report the prerequisite, never fabricate a
   credential or a file.
3. **Credentials stay secret.** OAuth tokens, app passwords and API keys are
   never printed, embedded in shared scripts or logged. Use the narrowest
   scope the task needs.
4. **Data hygiene for personal records.** Health trends, diaries, job
   searches and ledgers hold personal data: keep it in the user's own
   storage, never transmit it to a third party without consent, and redact
   it in any shared output.
5. **Registers have contracts.** A ledger, tracker or workpaper defines its
   columns, its entry rule and its reconciliation cadence before use; an
   entry that violates the contract is rejected, not forced.
6. **Reliability limits are stated.** Workflow automation carries reliability
   and example limits — an example is illustrative, not a tested pipeline;
   say what was run.
7. **Write clean.** Short declarative sentences. No em dash. Sentence case
   headings. No chatbot framing.

## 1. Email

- **Systems** (email-systems, cooper-email, business-email-template,
  email-sequence, email-issue-fixer, mailtrap-sending-emails): email
  architecture with detailed guides; templates; sequence design with
  detailed guide; issue fixing; sending via Mailtrap with domain setup
  (frontend hub carries the domain details).
- **Gmail** (gmail-automation): label, filter and draft automation with
  supporting-material availability declared.

## 2. Google Workspace

- **Sheets** (google-sheets-automation, csv-manual-export, spreadsheet-
  manual-build): API-driven reads and writes; CSV export; manual build with
  formula discipline.
- **Calendar** (google-calendar-automation, team-calendar): event creation
  with conflict checks; team calendars with time zones stated.
- **Drive, Docs, Forms** (google-drive-automation, google-no-code): Drive
  automation with supporting-material availability declared; no-code forms
  automation.

## 3. Slack and chat

- **Bots** (slack-bot-builder): bot architecture with an application
  boundary stated — scope tokens, verify signatures, rate-limit replies.
- **GIFs** (slack-gif-creator): Slack targets and recommendations before
  generating.

## 4. Knowledge bases

- **Notion** (notion-manual-import): manual import procedure; never ask for
  a Notion password or token (design hub carries the register rule).
- **Obsidian** (obsidian-bases, obsidian-cli, obsidian-clipper-template-
  creator): Bases databases with detailed guide; CLI usage; web clipper
  template creation.
- **General** (knowledge-base, crossframe-org, crossframe fragments carried
  by writing hub): knowledge base structure; organizational memory.

## 5. Time, meetings and tracking

- **Meetings** (meeting-distiller-pro): distill decisions, owners and
  actions from transcripts; never invent an attendee position.
- **Time** (time-tracking, time-ledger, ledger-tasks-yylo): tracking with
  entry rules; ledgers with the YYLO CLI reference and supported task
  contract.
- **Notifications** (notification-reminder-hub): reminder routing with
  quiet hours.
- **Registers** (bilig-workpaper, billing-automation, invoices carried by
  business hub): workpapers with evidence columns; billing automation with
  approval gates.

## 6. Career and personal

- **Job search** (cv-generator, jobgpt, healthcare-job-search): CV
  generation for FlowFlow/Canva with the detailed guide; search automation
  with rate limits; US healthcare job search with scope stated.
- **Health and personal** (health-trend-analyzer, health-wellness,
  wellally-tech, diary, speed, party-planning, trip-coupon, mcd-secret-menu-
  lab): trend analysis (Chinese-canonical) with a wellness-information
  boundary — not medical advice; wellness registers; digital health
  integration with detailed guide; diary systems; speed reading; personal
  planners. Fun fragments kept with their own boundaries.
- **Communication** (internal-communication): internal comms cadence and
  channels.

## 7. Tools and automation

- **Workflow** (workflow-automation, flowhunt-skill, browser-harness,
  postman-newman-automation, screenshots, bulletmind): automation with
  reliability and example limits; automation discovery audits; browser
  harness for controlled browsing; API collection runs; screenshot
  capture; presentation bullets.
- **Site health** (wp-site-health-auditor): WordPress health audits with
  when-to-use (frontend hub carries the WordPress depth).
- **Data ops** (monte-carlo-asset-health): asset health monitoring with
  bundled upstream support declared (data-ml hub carries the Monte Carlo
  depth).
- **Construction** (blueprint, idea-to-blueprint): plan generation with
  stated scope — plans are drafts, not stamped engineering documents.

## 8. Output contract

- Name the skill, the target system, and the account scope in the first
  line of reasoning and in the todo list.
- Report the artifact: a sent draft, a created event, a sheet range, a
  ledger entry, a document path.
- Keep cell ranges, event ids, message links and error strings verbatim.
- State what was executed and where. A dry run is not a send.
- Keep open work open: a missing credential, an unconfirmed recipient list
  and a skipped reconciliation are reported, never rounded up.
- Never print a token, password or personal record; redact and name the
  rule.

## 9. Failure handling

| Situation | Response |
| --- | --- |
| A send, post or write lacks explicit approval | Stop and ask. |
| A credential is missing or out of scope | Report the prerequisite; never guess. |
| A recipient list is unconfirmed | Do not send. |
| A register entry violates its contract | Reject the entry and state the rule. |
| A personal record would leave the user's storage | Redact or stop. |
| An example workflow is presented as tested | Label it illustrative. |
| A health claim reads as medical advice | Relabel it wellness information. |
| The evidence contradicts the requested action | Show the evidence and stop. |

## Provenance

Merged from the office-productivity class (55 catalog skills). Every source
skill's procedure, rule and policy is represented above; duplicates
collapsed to one canonical statement; side-effect authorization, credential
and fail-closed rules preserved. No external file is required to use this
skill.
