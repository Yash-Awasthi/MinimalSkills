# observability

Load for metrics, logs, traces, alerts and incidents.

## three signals

| signal | question | cost |
| --- | --- | --- |
| metric | is it healthy, how fast | low, aggregate |
| log | what happened in this case | high, per event |
| trace | where the time went | medium, sampled |

Instrument all three for a request path. One alone cannot answer "why slow".

## golden signals

- latency: p50, p95, p99, per endpoint
- traffic: requests per second
- errors: rate by class, 4xx separate from 5xx
- saturation: cpu, memory, queue depth, connection pool

Alert on symptoms users feel: error rate, latency, saturation. A CPU alert pages someone for a machine that is doing its job.

## alert rules

```yaml
- alert: ApiErrorRateHigh
  expr: sum(rate(http_requests_total{code=~"5.."}[5m])) / sum(rate(http_requests_total[5m])) > 0.02
  for: 10m
  labels: { severity: page }
  annotations: { runbook: https://runbooks/api-error-rate }
```

- Every page has a runbook. No runbook, no page.
- `for:` suppresses flapping. A page that fires on a single spike trains people to ignore it.
- Two severities: page (human now), ticket (next business day).
- Review alerts quarterly. Delete the ones nobody acted on.

## logs

- Structured json, one event per line.
- Include: timestamp, level, service, request id, user id hashed, latency, outcome.
- Never log: tokens, passwords, full card numbers, raw request bodies with pii.
- Sample high-volume debug logs. Keep errors complete.

## traces

- Propagate the request id across services.
- Span per outbound call, with the target and the status.
- Sample head 10%, keep all errors.
- A trace without a service map answers nothing. Tag spans with the operation name.

## incident

1. Declare. One incident commander, one channel.
2. Stabilize: roll back or shift traffic. Diagnosis waits.
3. Communicate on a clock: first update within 15 minutes, then every 30.
4. Record the timeline with timestamps as you go, not after.
5. Resolve, then write the review within 48 hours.

## postmortem

```
impact:    users affected, duration, error budget spent
timeline:  detection, response, mitigation, resolution
cause:     the trigger and the latent condition
actions:   owner, date, verifiable outcome
```

Blameless means the system is the subject: name the check that was missing, the alert that did not fire and the runbook step that was absent.
## telemetry index

| tool | the rule that matters |
| --- | --- |
| OpenTelemetry | One `TracerProvider` per process, `BatchSpanProcessor` in prod; a span attribute with a user id is PII, hash it. |
| eBPF | `bpftrace -e 'tracepoint:syscalls:sys_enter_openat { printf("%s\n", str(args->filename)); }'`; kernel 4.9+ and root, or the probe silently attaches nothing. |
| Instrumentation | RED for services (rate, errors, duration), USE for resources (utilisation, saturation, errors); a dashboard without a threshold is a wall of lines. |
| Cost and FinOps extras | Cost per request, cost per tenant, cost per environment; an untagged resource is unattributable and unbudgetable. |
| Audit | Who changed what, when, from where; an audit log without the actor is a changelog. |
