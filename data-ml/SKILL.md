---
name: data-ml
description: Use when working with datasets or models: loading and cleaning, Hugging Face models and datasets, embeddings and vector search, dbt pipelines and quality checks, pandas and notebooks, evaluation, computer vision. Triggers: dataset, embedding, pandas, Hugging Face, dbt, model.
---

# data-ml

## use when

- load, clean, join or validate a dataset -> references/pipelines.md
- dbt model, test, backfill, orchestration -> references/pipelines.md
- Hugging Face model or dataset, tokenizer -> references/models.md
- embedding, vector index, retrieval quality -> references/models.md
- evaluate a model or a split -> references/models.md
- notebook, scientific python, plot, CV preprocessing

not for: agent orchestration and RAG policy (ai-agents-orchestration), server persistence layer (backend-api)

## rules

- Conflict order: leakage, then reproducibility, then speed; a leaked metric is a wrong metric.
- Inspect before transform: shape, dtypes, null rate, cardinality, duplicates; `df.info()` is not inspection.
- One row per entity, stated in the model docs; a join that multiplies rows is a defect, not a quirk.
- Split by entity, not by row; a feature computed from a future value is leakage, so drop it.
- Pin the embedding model by revision; vectors from two models cannot share an index.
- Every metric carries its eval set, its n and its date.
- Land raw data immutable with a pull date and a checksum; a rerun that differs is a broken pipeline.

## change

1. Locate: the model, its upstream `ref`, and every downstream mart and dashboard that reads it.
2. Propose the transform change in one sentence, with the alternative you rejected.
3. Predict before running: row count, null rate, dtypes, and which test fails first.
4. Back up the original model SQL and its config in context, pinned to `git rev-parse HEAD`.
5. Apply one concern per edit; a join fix and a column rename are two edits.
6. Verify: `dbt build --select +model`, then `dbt test --select model`.
7. Regress: every downstream model, the freshness test and the row-count assertion.
8. Compare the row counts with the prediction; an unexplained multiplication stops the run.
9. Report the model, row counts and test exit status, then take the next item.

## pipeline

1. Land raw, immutable, checksummed.
2. Validate schema and ranges at ingest. Fail the run, do not coerce.
3. Transform in typed steps, one step one table.
4. Test: unique, not_null, accepted_values, relationships, freshness.
5. Publish a versioned table. Downstream reads the version, not "latest".
6. Backfill with the same code path as the daily run.

```sql
-- models/fct_invoice.sql
{{ config(materialized='incremental', unique_key='invoice_id') }}
select i.id as invoice_id, i.amount_cents, i.currency, i.status
from {{ ref('stg_invoices') }} i
{% if is_incremental() %}
where i.updated_at > (select max(updated_at) from {{ this }})
{% endif %}
```

```bash
dbt build --select +fct_invoice
dbt test --select fct_invoice
```

Tests on the model: `unique` and `not_null` on invoice_id, `relationships` to dim_customer, `accepted_values` on status.

## decide

| condition | action |
| --- | --- |
| null rate over 20% in a key column | stop, inspect the source |
| duplicate ids after a join | fix the join key, never dedupe silently |
| under 1k rows | report n beside every metric |
| embedding model changes | reindex the whole corpus |
| metric jumps on the test split | audit the split for leakage |
| feature needs tomorrow's value | drop it |
| notebook over 200 cells | extract to a module with a test |
| parquet over memory | stream with `datasets` or chunked read |

## check

- [ ] source, pull date and license recorded
- [ ] row count before and after every join
- [ ] dbt tests green on the changed models
- [ ] split by entity, no overlap, sizes reported
- [ ] metrics with n and the eval set named
- [ ] rerun from raw reproduces the output

## stop

| condition | action |
| --- | --- |
| license unclear | ask before use |
| personal data in the set | stop, mask or drop |
| no eval set | build it before tuning |
| hub token needed | ask the owner to set it |

## emit

- inputs with versions, outputs with row counts
- metrics with n, eval set and date
- what is sampled, estimated or unverified
