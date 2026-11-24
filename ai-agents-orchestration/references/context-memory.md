# context-memory

Load when designing what the model sees and what it remembers.

## window budget

| block | share | note |
| --- | --- | --- |
| system rules | 5-10% | stable, cacheable prefix |
| task and constraints | 5% | do not repeat every turn |
| retrieved evidence | 40-60% | cite, and drop when stale |
| working state | 10-20% | plan, decisions, open questions |
| conversation | remainder | summarize past a threshold |

Every token competes: a 60k file in a 200k window leaves 140k for the task and buries the instruction mid-context, where recall drops.

## selection

- Retrieve by the current step, not by the original task.
- Rank by recency and relevance; ids and names need keyword search.
- Deduplicate near-identical chunks before adding.
- Keep the source id with each chunk.
- Send `path:line-range` plus the excerpt; a whole file spends budget on code the step never reads.

## summarization

```
keep:    decisions, constraints, open questions, ids
drop:    reasoning that led nowhere, repeated tool output, restated rules
format:  bullet per decision, one line each
trigger: 60% of window, or a phase change
```

A summary that loses a constraint causes the same mistake twice.

## memory

| store | lifetime | use |
| --- | --- | --- |
| window | one turn | working state |
| scratch file | one task | plan, findings, ids |
| session store | one session | resume, checkpoints |
| durable memory | across sessions | preferences, invariants |

Rules for durable memory:

- Retrieve the stored fact before planning, write the new one after the decision with the date and the source that produced it.
- One fact per entry, with a date and a source.
- Supersede with an end date, never overwrite. Show contradictions with both dates.
- Never store secrets, credentials or personal data.
- Every entry carries `expires_at`; a preference applied after it lapsed is a wrong answer with a citation attached.

## retrieval quality

| symptom | fix |
| --- | --- |
| answers miss an obvious doc | add keyword search, widen top-k |
| answers cite the wrong doc | rerank, require the quote |
| answers blend two tenants | partition the index by tenant key |
| answers stale | store an as-of date, filter on it |
| context overflow | summarize the conversation, not the evidence |

## failure

- No relevant chunk found: say so. Do not answer from general knowledge as if retrieved.
- Conflicting chunks: show both, name the dates, ask or pick by policy.
- Chunk has no source: drop it.
