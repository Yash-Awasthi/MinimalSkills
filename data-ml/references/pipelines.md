# pipelines

Load for ingestion, dbt, quality checks and backfills.

## ingest

```python
df = pd.read_parquet("raw/invoices.parquet")
df = df.convert_dtypes()          # nullable ints, not float with NaN
print(df.shape, df.dtypes.value_counts().to_dict())
print(df.isna().mean().sort_values(ascending=False).head(10))
```

- Read parquet, not csv, for anything over a few MB. Types survive.
- `convert_dtypes()` avoids the int-to-float promotion that silently changes a key.
- Record the row count and the checksum of the raw file before any transform.
- One row per entity: state the key, then assert uniqueness.

## dbt

```sql
{{ config(materialized='incremental', unique_key='invoice_id', on_schema_change='append_new_columns') }}

select invoice_id, owner_id, amount_cents, created_at
from {{ ref('stg_invoices') }}
{% if is_incremental() %}
where created_at > (select coalesce(max(created_at), '1970-01-01') from {{ this }})
{% endif %}
```

Tests in `schema.yml`:

| test | catches |
| --- | --- |
| unique | duplicate key from a join |
| not_null | broken upstream join |
| accepted_values | new status the code does not handle |
| relationships | orphan foreign key |
| freshness | a stalled source |

An incremental model without a lookback window misses late-arriving rows. Use `created_at > max - interval '3 days'`.

## backfill

```bash
dbt run --select fct_invoice --vars '{"start_date": "2026-01-01"}'
```

- Same code path as the daily run. A separate backfill script drifts within a month.
- Idempotent: delete-and-insert by partition, or merge on the key.
- Run in batches with a checkpoint. One long transaction locks the table.

## quality

| signal | threshold | action |
| --- | --- | --- |
| null rate in a key | over 1% | fail the run |
| row count change | over 30% day over day | alert before publishing |
| duplicate rate | over 0% on a unique key | fail |
| freshness lag | over 2x the schedule | alert |
| schema change | column removed or retyped | block the deploy |

Alert on absence too: a job that stops looks identical to a job that succeeds.

## notebooks

Exploration only. A notebook that ships becomes a module with a function, a test and a docstring. Extract when it passes 200 cells or gets a second user.
## pipeline index

| topic | the rule that matters |
| --- | --- |
| Root cause and remediation | A failed test names the column, the row count and the first bad value; a dashboard with no owner is a screenshot. |
| Cost and validation | Cost per run and per backfill, plus a row-count and schema check; a backfill that scans the whole table costs the month. |
| Visualization | One message per chart, axis labelled with units, no dual y-axis; a chart that needs a caption to be read is a table. |
| Data frames and graphs | `groupby` then `agg`, never `apply` row-wise; a join on a float key silently drops rows. |
| Math | Log returns for compounding, simple returns for reporting; mean of log returns is not the return. |
| Science method | Hypothesis, test, result, decision; a notebook that only shows the successful run is a demo, not an experiment. |
