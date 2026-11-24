# docs

Load for README, reference, tutorial, runbook and changelog work.

## four types, never mixed

| type | reader state | shape | test |
| --- | --- | --- | --- |
| tutorial | learning | numbered steps, one path | a beginner finishes |
| how-to | has a goal | prerequisites, steps | the goal is reached |
| reference | needs a fact | every option, type, default | complete against the code |
| explanation | wants the why | prose, trade-offs | a decision is legible |

A page that teaches and also lists every flag serves neither reader.

## readme

```markdown
# name

one line: what it does, for whom.

## install
## quickstart (one runnable example)
## configuration (table: option, default, meaning)
## license
```

- The first screen decides whether the rest is read: title, one sentence on what it does, the install command, no badge wall above the title.
- The quickstart must run as written. Test it in a clean directory.
- A screenshot goes after the quickstart, never before it.

## reference

- One entry per option: name, type, default, effect, example.
- Generate from the schema when possible. A hand-written reference drifts in a week.
- Document errors with their code and the recovery step.

## runbook

```
symptom:   what the alert says
check:     one command that confirms the cause
action:    the fix, ordered
escalate:  who, when, with what context
```

An on-call engineer follows it at 3am without judgment. No prose, no history.

## changelog

Keep a Changelog shape, newest first:

```
## [1.4.0] - 2026-03-04
### Added
### Changed
### Fixed
### Removed
```

- One line per user-visible change, imperative, no ticket ids in the sentence.
- Breaking change: state the migration in the same entry.
- Unreleased section at the top, filled as work lands.

## lint and convert

```bash
npx markdownlint-cli2 "**/*.md"
vale --minAlertLevel=error docs/
pandoc docs/spec.md -o spec.pdf --pdf-engine=typst
lychee --offline docs/
```

- Link checking in CI catches the doc that rotted after a rename.
- One linter and one style guide, run in CI on every PR; a guide nobody runs is decoration.

## changelog shape

```
## [1.4.0] - 2026-11-24
### Added
- export to csv from the invoice list (#4821)
### Fixed
- duplicate line when a discount was applied twice (#4830)
### Removed
- legacy `--fast` flag; use `--parallel`
```

- Sections: Added, Changed, Deprecated, Removed, Fixed, Security. Omit empty ones.
- One line per user-visible change, with the issue number.
- Unreleased work sits under `## [Unreleased]`. A version and an ISO date per release.
- No internal refactors, no dependency bumps the user cannot see.
- A migration guide is separate from the changelog and links the version.

## slide deck

```text
1 Title     the claim, not the topic: "Export cuts close from 6h to 2h"
2 Problem   one number, one sentence
3 Evidence  the chart, one line of interpretation
4 Options   what else was considered, one line each
5 Ask       the decision, the owner, the date
```

- One idea per slide, six words per line, 24pt minimum.
- A deck with no number on any slide is a brochure; if it is read aloud, it is a document and belongs in prose.
- The last slide repeats the ask verbatim, and the email that carries the deck repeats it again.

## conversion

```bash
pandoc README.md -o README.html --standalone --toc
pandoc notes.md -o notes.docx --reference-doc=template.docx
pandoc paper.md -o paper.pdf --pdf-engine=xelatex
pandoc page.html -f html -t gfm -o page.md
```

- `--standalone` or the output loses the head and the stylesheet.
- Convert from the source, never from a converted copy: markdown to docx to markdown loses tables.
- A reference doc keeps the brand fonts and margins; a default docx looks like a draft.
- Check the output, not the exit code: a PDF with a missing font renders boxes.
## other doc shapes

| shape | the rule that matters |
| --- | --- |
| Technical documentation | Reference, how-to, tutorial, explanation; a page that mixes two is unreadable at the moment of need. |
| ADRs | Context, decision, consequences, numbered, one page; a superseded ADR stays and is marked superseded with the date. |
| Generators | typedoc, sphinx, OpenAPI to HTML; generated output is never hand-edited, it regenerates on release. |
| Wiki | Every page has an owner, an updated date and a review date; a page with no owner is deleted at the next cleanup. |
| Diagrams | One idea per diagram, labels not a legend, the source file committed next to the exported image. |
| SEO helpers | Title under 60 characters, description under 155, one `h1`, canonical on every variant. |
| Social repurposing | One thread from the first section of the doc, link back; a thread that restates the whole doc has no reason to exist. |
| PPTX generation | python-pptx or Marp from markdown; six words per line, 24pt floor, the source file is the artifact. |
| Meeting and standup | Decision, owner, date, next step; a standup note is three lines, not a transcript. |
| Extraction and conversion helpers | pandoc in, pandoc out, one source format; a round trip through docx loses tables and comments. |
| Data fetchers | A doc that pulls a number fetches it at build time and stores the date; a hand-copied number goes stale silently. |
