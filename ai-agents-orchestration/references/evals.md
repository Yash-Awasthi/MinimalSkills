# evals

Load when measuring quality, gating a change, or comparing models.

## build first

1. Collect 30-100 real inputs, including the ugly ones.
2. Write the expected outcome for each. Exact match, schema, or rubric.
3. Split: 70% dev, 30% holdout. Never tune on the holdout.
4. Run the baseline. Record the number before changing anything.
5. Change one thing. Re-run. Keep or revert.

An eval set written after the change measures the change, not the quality.

## scoring

| output type | scorer |
| --- | --- |
| classification | exact match, confusion matrix |
| extraction | field-level precision and recall |
| free text | rubric per criterion, two judges |
| tool use | trace match: right tool, right args, right order |
| code | tests pass, plus a human read |

Model as judge: pin the judge model and version, give it the rubric, score 1-5 per criterion, and spot-check 20 samples by hand. A judge that agrees with everything is broken.

## gates

| metric | gate |
| --- | --- |
| task success | not below baseline minus 2 points |
| schema validity | 100% |
| latency p95 | under the product budget |
| cost per task | under the unit economics |
| unsafe output | 0 on the red-team set |

## sample size

| delta to detect | samples per arm |
| --- | --- |
| 20 points | 20 |
| 10 points | 60 |
| 5 points | 300 |
| 2 points | 1500 |

Report the n and the interval: below 30 samples the interval is wider than the effect you are claiming, so the number proves nothing.

## regression

```bash
pnpm eval --set dev --baseline baseline.json --fail-on-regression 2
```

- Store the baseline with the model id, prompt hash and date.
- A prompt change without an eval run is an unmeasured change.
- Cache evals by (prompt hash, input hash, model) so reruns are cheap.

## reporting

- metric, n, interval, baseline, delta
- what changed between runs
- what the eval set does not cover
