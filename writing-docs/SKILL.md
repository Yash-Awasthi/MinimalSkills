---
name: writing-docs
description: Use when writing or editing prose: README and reference docs, tutorials and runbooks, release notes and changelogs, blog posts, slide decks, summaries, editing for clarity, converting formats. Triggers: README, docs, changelog, blog, slides, edit.
---

# writing-docs

## use when

- README, reference page, architecture note -> references/docs.md
- tutorial, how-to, runbook -> references/docs.md
- changelog, release notes, migration guide -> references/docs.md
- editing, shortening, voice, proofreading -> references/prose.md
- blog post, announcement, slide deck

not for: visual design of a page (design-ux), product decisions (strategy-product)

## rules

- Conflict order: accuracy, then the reader's task, then brevity; a short wrong sentence loses.
- Name the reader and the task in the first line, and order the sections in the order the reader performs them; a doc for two audiences is read by neither.
- A claim carries its source, its date and its unit; a number without a unit is a guess.
- Every code sample is run before publication; an untested sample is a support ticket written in advance.
- Active voice, present tense, no em dash, no superlative; a sentence that only decorates is deleted.
- A page over 2000 words splits by task; the old URL redirects to the new one.

## change

1. Locate: the section, the claim it makes, and every page that links to its anchor.
2. Propose the rewrite in one sentence, with the structure you rejected.
3. Predict before editing: word delta, which command output changes, which link moves.
4. Back up the original paragraph in context, pinned to `git rev-parse HEAD`.
5. Apply one concern per edit; a reorder and a rewrite are two passes.
6. Verify: run every command in the section, then the linter.
7. Regress: every page linking the anchor, plus the table of contents.
8. Compare the rendered page against the prediction; a broken anchor stops the edit.
9. Report word count before and after, then take the next item.

## types

| type | reader wants | failure it produces |
| --- | --- | --- |
| tutorial | to learn by doing | steps that assume knowledge |
| how-to | to finish one task | theory before the command |
| reference | to look up a fact | prose where a table belongs |
| explanation | to understand why | steps where reasoning belongs |

## readme

```text
# name            one line: what it does, for whom
## install         one command, prerequisites, supported versions
## quickstart      5-10 lines that produce a visible result
## configure       every option, default, and what breaks when it is wrong
## api             one entry per function: signature, returns, one example
## troubleshoot    the 5 errors a new user hits, with the fix
## license
```

- Install before quickstart, quickstart before configuration. A reader who cannot run it stops reading.
- The quickstart is copied, not read: it must work as pasted.

## procedure

1. State the reader and what they can do after reading.
2. One idea per paragraph, three sentences maximum, example before explanation.
3. Run every command in the document.

```bash
npx markdownlint-cli2 "**/*.md"
vale --minAlertLevel=error docs/
```

## decide

| condition | action |
| --- | --- |
| doc over 2000 words | split by task |
| reader is an expert | cut the tutorial preamble |
| behavior changed | update the doc in the same PR |
| version matters | state the version tested |
| four doc types in one file | split: tutorial, how-to, reference, explanation |
| changelog entry | one line per user-visible change, issue number |

## check

- [ ] every command run, exit status known
- [ ] links resolve
- [ ] version and date where behavior may change

## stop

| condition | action |
| --- | --- |
| no source for a claim | mark it unverified or cut it |
| tone conflicts with the audience | ask once, then proceed |

## emit

- files written, word count before and after
- commands verified with their output
- claims left unverified
