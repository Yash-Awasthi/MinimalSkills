# orchestration

Load when splitting work across agents, subagents or parallel workers.

## when to split

Split when subtasks are independent, read-heavy and verifiable. Do not split when the subtasks share mutable state, need one voice, or the handoff costs more than the work.

## contract

```
input:   typed payload, no prose instructions
output:  typed result + evidence + status
status:  VERIFIED | NOT VERIFIED | BLOCKED
budget:  max steps, max tokens, timeout
```

A subagent that returns prose instead of a typed result forces the parent to re-read everything.

## delegation rules

- One responsibility per agent. "Research and also write and also test" is three agents or one.
- The parent owns the summary. Never pass a child's claim through unread.
- A child's failure is not "no findings". Mark coverage incomplete.
- Retry a transient failure once. Retry a malformed output once. Never retry a permission denial.
- Pass the minimum context: task, constraints, output schema. Not the whole transcript.

## fan-out

```python
results = await asyncio.gather(*(worker(t) for t in tasks), return_exceptions=True)
ok = [r for r in results if not isinstance(r, Exception)]
failed = [t for t, r in zip(tasks, results) if isinstance(r, Exception)]
```

Collect exceptions. A gather that raises on the first failure loses the rest of the work.

## review agents

| setup | signal |
| --- | --- |
| same prompt, different model | genuine second opinion |
| same model, same prompt | correlated, low value |
| two reviewers on the same diff | useful only if scopes differ |

Report agreement and disagreement separately; on a split, re-run the disputed item against the source, and the source wins over the vote.

## write gate

Publishing, posting, pushing, spending and deploying need an explicit request naming the target. A plan does not authorize execution. A skill in the context is not permission.

## anti-patterns

- agent that summarizes another agent's summary
- supervisor with one worker
- router that always picks the same route
- retry loop around a deterministic failure
- parallel writers to one file
