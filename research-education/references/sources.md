# sources

Load for literature search, source evaluation, citation and teaching.

## search

```bash
curl -s "https://api.crossref.org/works?query.bibliographic=retrieval+augmented&rows=5&select=title,author,issued,DOI"
curl -s "https://api.semanticscholar.org/graph/v1/paper/search?query=rag&fields=title,year,venue,citationCount"
```

Three angles per question: the term of art, the critique, the survey. A single query returns the popular paper, not the good one.

## source hierarchy

| rank | source | weight |
| --- | --- | --- |
| 1 | peer reviewed, replicated | highest |
| 2 | peer reviewed, single study | strong |
| 3 | preprint with data | moderate, label it |
| 4 | official documentation or standard | authoritative for its scope |
| 5 | vendor blog | marketing until verified |
| 6 | forum answer | anecdote |

Never present rank 4 to 6 as evidence of an empirical claim.

## evaluate

- Method before result: sample, control, measurement, conflicts.
- n and effect size, not just significance.
- One study is a hypothesis: call it a finding after a second group reproduces it or a meta-analysis pools it.
- Currency: state the year for anything time-sensitive.
- Citation graph: does the paper cite the counter-evidence.

## cite

APA 7:

```
Author, A. A. (2026). Title of work. Journal, 12(3), 45-67. https://doi.org/10.xxxx
```

BibTeX:

```bibtex
@article{author2026title,
  author  = {Author, A.},
  title   = {Title of work},
  journal = {Journal},
  year    = {2026},
  doi     = {10.xxxx/yyyy}
}
```

- Quote verbatim with a page or section locator. Paraphrase with the same citation.
- Never cite a source you did not read. A secondary claim is cited to the secondary.
- One reference list per document, one style, alphabetical.

## verify a claim

1. Find the primary source.
2. Read the method and the limitation.
3. Check whether the claim matches the abstract, the result and the scope.
4. Look for the counter-claim and name it.
5. If steps 1-3 fail: report "unverified", with the search path.

## teach

| level | start | check |
| --- | --- | --- |
| beginner | one concrete example | reproduce the example |
| intermediate | the rule, then the edge | apply to a near case |
| expert | the trade-off and the evidence | critique a bad case |

- One concept per section; a section that introduces two gives the learner two places to fail and one check.
- Worked example, then a near-transfer exercise, then a case that needs the concept.
- Facts go to spaced repetition on a 1/3/7-day schedule; a skill needs a worked case the learner attempts before seeing the answer.

## citation formats

- APA 7: Author, A. A. (2024). Title of the work. Journal Name, 12(3), 45-67. https://doi.org/10.xxxx/yyyy
- BibTeX: `@article{key, author={Last, First}, title={...}, journal={...}, year={2024}, doi={...}}`
- Page number on every direct quote: `(Author, 2024, p. 46)`.
- A doi, not a landing page. A dead link is replaced, not kept.
- A secondary source is cited as "as cited in", never as the original.

## evidence tiers

| tier | evidence |
| --- | --- |
| 1 | systematic review, meta-analysis |
| 2 | randomised trial |
| 3 | cohort or case-control study |
| 4 | case series, expert opinion |

A claim is only as strong as its weakest cited tier: one vendor blog under a systematic review makes the sentence vendor-grade.

## fact check worksheet

| claim | source | date | method | verdict |
| --- | --- | --- | --- | --- |
| dbt used by 40% of data teams | vendor survey, n=412 | 2024-06 | self-reported, vendor-run | weak |
| pandas 2.0 added the arrow backend | pandas 2.0.0 release notes | 2023-04 | primary | confirmed |
| median query 3x faster | benchmark, one machine | 2024-02 | not replicated | unverified |
| GDPR fines capped at 4% of turnover | regulation art. 83 | 2016-04 | primary legal text | confirmed |
| incremental models cut cost 70% | vendor blog, no data | 2025-01 | no method | reject |

- Verdicts: confirmed, weak, unverified, reject. Each verdict states why in the method column.
- A vendor survey is weak evidence about its own product, whatever the n.
- A single-machine benchmark is unverified until a second party reproduces it.
- "No method" is a reject, not an unverified: there is nothing to check.
## research index

| topic | the rule that matters |
| --- | --- |
| Scientific method and math | Hypothesis, operational definition, test, result; a claim with no falsifier is not a finding. |
| Falsification | State what result would prove the claim wrong before running the test; after the fact, every result fits. |
| Verification | Re-run the analysis from the raw data; a number that cannot be reproduced is a claim, not a finding. |
| Transcripts | Time-stamped, speaker-labelled, verbatim; a cleaned quote is a paraphrase and must be cited as one. |
| Management | One source list with ids, one notes file per source, a decision log for what was excluded and why. |
| Domain science | Field conventions differ: effect sizes in psychology, confidence intervals in medicine, error bars in physics. Name the field's standard. |
| Papers and academic writing | Abstract states the result, not the plan; a paper without a limitations section reads as advocacy. |
| Discovery | Search the citation graph both ways: what this cites, and what cites this. |
| Conversion | Units and currencies stated at the point of use; a table mixing them without a column is unreadable. |
| Learning | Retrieval practice beats re-reading; a summary written from memory exposes the gap. |
| Debate and reflection | Steelman the other position before rebutting; a rebuttal of a weak version is a straw man. |
