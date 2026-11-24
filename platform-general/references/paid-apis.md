# paid-apis

Load for metered data, scraping and enrichment services.

## before the first call

| question | why |
| --- | --- |
| price per unit | a loop becomes an invoice |
| free tier limit | the first surprise |
| concurrency limit | 429 storms |
| data license | redistribution may be forbidden |
| retention | storing the data may be restricted |
| sla | a pipeline built on best-effort breaks |

## client shape

```ts
async function call(path: string, body: unknown, attempt = 0): Promise<Result<Data>> {
  const res = await fetch(base + path, {
    method: 'POST',
    headers: { authorization: `Bearer ${env.KEY}`, 'content-type': 'application/json' },
    body: JSON.stringify(body),
    signal: AbortSignal.timeout(20_000),
  });
  if (res.status === 429 || res.status >= 500) {
    if (attempt >= 2) return { ok: false, error: `http_${res.status}`, retryable: false };
    await sleep(500 * 2 ** attempt * Math.random());
    return call(path, body, attempt + 1);
  }
  if (!res.ok) return { ok: false, error: `http_${res.status}`, retryable: false };
  return { ok: true, value: await res.json() };
}
```

## cost control

- Batch where the provider supports it.
- Cache responses by input hash. Enrichment is stable for days.
- Cap the run: max items, max spend, then stop and report.
- Log units consumed per call, not just status.
- Alert at 80% of the monthly budget.

## scraping

| rule | detail |
| --- | --- |
| robots and terms | check before the first request |
| rate | one request per second unless the site allows more |
| identity | a real user agent with a contact url |
| payload | the smallest page that answers the question |
| storage | keep the derived value, not the whole page |
| failure | a block is reported, not retried in a loop |

## data quality

- Record the source url and the fetch time with every record.
- A field the provider returns empty is empty: map it to `null`, not `false`, or a downstream filter reads it as a no.
- Dedupe on the provider id, not on the name.
- Spot-check 20 records by hand before trusting a batch.

## review

- Key from the secret store, absent from logs.
- Total deadline on the whole run, not only per call.
- A dry-run mode that reports the cost without spending.

## apify actors

```bash
curl -s -X POST "https://api.apify.com/v2/acts/<actor>/runs?token=$KEY" \
  -H 'content-type: application/json' \
  -d '{"input":{"startUrls":[{"url":"https://example.com"}],"maxPages":50}}'
```

- The run returns an id immediately. Poll `/v2/actor-runs/<id>` until `SUCCEEDED`, then read `/dataset/items?format=json`.
- Billing is compute units: a 50-page crawl at 1 GB memory is roughly 0.05 CU. Check the actor's price before any loop.
- `maxPages` and `maxRequestsPerCrawl` are the only guards against a runaway bill. Set both.
- A run that ends `FAILED` still bills for the time it ran.
- `--max-pages` on the CLI and `maxPages` in the input are different knobs; the input wins.
