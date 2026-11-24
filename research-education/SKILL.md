---
name: research-education
description: Use when investigating a question or teaching a concept: literature search, source evaluation, citations, fact checking, study and course design, explanations at a stated level, math and proof, paper outline. Triggers: research, citation, fact check, explain, curriculum.
---

# research-education

## use when

- answer a question that needs sources -> references/sources.md
- evaluate a claim or a source
- cite, quote, or format references
- explain a concept at a level
- design a lesson, exercise or curriculum

not for: writing mechanics of a doc (writing-docs), product decisions (strategy-product)

## rules

- Conflict order: source quality, then recency, then fluency; a fluent claim without a locator is unverified.
- Answer from a source or say you cannot; a plausible reconstruction is the failure this skill exists to prevent.
- Every claim carries a locator; quotes are verbatim with a page or timestamp, and a blended sentence is neither source nor paraphrase.
- Primary over secondary; when only the secondary is at hand, attribute the claim to it by name.
- A time-sensitive fact carries its date; a 2019 figure presented as current is wrong even when it was right.

## change

1. Locate: the claim, the sentence citing it, and every section that depends on the same source.
2. Propose the correction in one sentence, with the phrasing you rejected.
3. Predict before editing: which other claims move, which citation changes, what becomes unverified.
4. Back up the original sentence and citation in context, pinned to the source locator.
5. Apply one concern per edit; a fact correction and a rewording are two edits.
6. Verify: re-open the source at the locator and quote the exact words.
7. Regress: every claim resting on that source, plus the reference list entry.
8. Compare the edited text against the source; a paraphrase beyond it stops the edit.
9. Report the claim, the locator and what stayed unverified, then continue.

## research

1. Restate the question as one sentence with its scope.
2. Search three angles: the term of art, the critique, the survey.
3. Read the abstract and the method, not only the result.
4. Record: title, author, year, venue, doi or url, the claim, the page.

```bash
curl -s "https://api.crossref.org/works?query.bibliographic=<terms>&rows=5" | jq '.message.items[].title'
curl -s "https://api.semanticscholar.org/graph/v1/paper/search?query=<terms>&fields=title,year,abstract" | jq '.data[0]'
```

## review

```text
1 Question     one paragraph: the question, the scope, why it is open now
2 Method       databases, query string, inclusion rules, n screened, n included
3 Themes       3-5 headings; each = claim, 2-3 sources, where they disagree
4 Gaps         what no included study covers, stated as a limit
5 Conclusion   what the evidence supports, at which tier
```

- Method before themes. A reader who cannot repeat the search cannot trust the themes.
- Every theme names its disagreement. A theme with one source is a citation, not a review.
- The gap section is the contribution; a review with no gap restates the literature.
- Tiers: meta-analysis, randomised trial, cohort, expert opinion, in that order of weight.
Fact-check worksheet with verdicts: references/sources.md.

## evaluate

| question | fail signal |
| --- | --- |
| who wrote it, what is their stake | no author, no affiliation |
| what is the sample | n unknown or tiny |
| is the journal real | absent from doaj.org, no scope statement |

## cite

- APA 7: Author, A. A. (2024). Title. Journal Name, 12(3), 45-67. https://doi.org/10.xxxx/yyyy
- Page number on every quote: `(Author, 2024, p. 46)`. A doi, not a landing page.

## teach

- Beginner: one concrete example, then the rule. Intermediate: the rule, then the edge case.
- Expert: the trade-off, then the evidence. Exercises: one worked, one near-transfer, one that needs it.

## check

- [ ] every claim has a source or a label
- [ ] quotes verbatim with a locator
- [ ] no fabricated citation

## stop

| condition | action |
| --- | --- |
| no source found | say so, give the search path |
| sources conflict | present both, name the dates |
| request to cite something unread | refuse |

## emit

- the answer with sources
- what is contested or unverified
- the search path so it can be repeated
