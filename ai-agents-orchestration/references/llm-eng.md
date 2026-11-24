# llm-eng

Load for prompting, structured output, caching, cost and provider calls.

## prompt shape

```
role:      one line
task:      one imperative sentence
input:     delimited block, labeled as data
rules:     numbered, testable
output:    schema or exact format
```

A rule that cannot be tested by reading the output does not belong in the prompt; move it to a validator that fails the build.

## structured output

```ts
const Schema = z.object({ verdict: z.enum(['pass', 'fail']), reasons: z.array(z.string()) });
const out = Schema.parse(JSON.parse(text));  // throws, does not guess
```

- Write the schema before the prompt; a field the schema cannot express fails at parse time instead of in the consumer.
- On parse failure: one repair attempt with the error text, then fail.
- Never regex a model's json. Never `eval` it.

## parameters

| goal | setting |
| --- | --- |
| extraction, classification | temperature 0 |
| drafting | temperature 0.4-0.7 |
| deterministic tool args | temperature 0, schema enforced |
| long context recall | place the question after the documents |

## cost

- Cache the stable prefix. Provider prompt caching cuts input cost on repeated system prompts.
- Batch offline jobs where the provider supports it.
- Route by difficulty: small model first, escalate on low confidence.
- Measure tokens per task, not per call. Retries hide cost.
- A price table is an illustration; reconcile the invoice against measured tokens per request before quoting a unit cost.

## retrieval

- Chunk on headings and function boundaries; a fixed 500-token cut through a function separates the signature from its body and retrieves half a call.
- Hybrid: keyword plus vector. Pure vector misses ids and names.
- Rerank the top 50 to top 5 when precision matters.
- Always return the source id with the chunk. A claim without a source is unverifiable.
- Partition the index by tenant. A shared index leaks across tenants.

## streaming

- Stream tokens to the user, validate on completion.
- Partial json is not parseable. Stream events, not fragments of a schema.
- On abort, cancel the upstream request. A dangling stream keeps billing.

## failure handling

| failure | action |
| --- | --- |
| 429 | exponential backoff with jitter, honor retry-after |
| 5xx | retry twice, then fail loudly |
| context overflow | summarize or drop oldest, never truncate mid-instruction |
| refusal | surface the refusal text, do not rewrite the prompt silently |
| invalid schema | one repair, then fail |

## secrets

Keys live in the environment or a secret store. Never in a prompt, a log line, a fixture or a client bundle. Redact provider errors before logging: they can echo the request.
