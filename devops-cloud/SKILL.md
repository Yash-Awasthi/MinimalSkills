---
name: devops-cloud
description: Use when deploying, provisioning or operating infrastructure: AWS and Azure resources, containers and Kubernetes, CI/CD delivery, observability, incidents and runbooks, environments and secrets. Triggers: terraform, deploy, k8s, alert, rollback.
---

# devops-cloud

## use when

- AWS resource, IAM, cost -> references/aws.md
- Azure resource, identity, networking -> references/azure.md
- container, image, kubernetes -> references/kubernetes.md
- pipeline, release, environment -> references/cicd.md
- metrics, logs, traces, alerts, incident -> references/observability.md

not for: application code (engineering-craft), cloud attack surface under authorization (security-operations)

## rules

- Conflict order: data safety, then availability, then speed; a rollback that loses data is not a rollback.
- Read the plan before apply; production needs a request naming the environment, and every deploy carries a rollback command exercised once in staging.
- State lives remote and locked: a local state file is a data-loss path.
- Secrets from a store at runtime, file mode 0600; never in an image, a repo or a pipeline log.
- Retry once, at one layer; the SDK already retries transient failures.
- Pin the provider and SDK version; stable over preview unless a preview feature is the reason.
- A green pipeline is not a working service: probe it, and label every unmeasured number an estimate.

## change

1. Locate: the module or manifest, the plan diff and every environment that shares it.
2. Propose the change with its blast radius, and the alternative you rejected.
3. Predict before applying: resources replaced, downtime, probe signal, cost delta.
4. Back up the current state version and manifest in context, pinned to `git rev-parse HEAD`.
5. Apply one concern per edit; a version bump and a network rule are two changes.
6. Verify: `terraform plan` reviewed, then the deploy to the smallest environment, then the probe.
7. Regress: every environment sharing the module, the alert on it and the rollback path.
8. Compare the plan against the prediction; a replacement you did not list stops the apply.
9. Report resources changed, probe output and rollback command, then take the next item.

## deploy

1. Read the diff: `terraform plan -out=tf.plan`, `kubectl diff -f k8s/`.
2. List every resource that is replaced, not updated. A replacement on stateful data stops the run.
3. Confirm the rollback: previous image digest, previous state version, migration reversibility.
4. Apply to the smallest environment first.
5. Probe: health endpoint, one real request, error rate for 5 minutes.
6. Record: image digest, config version, actor, timestamp.

## kubernetes

```yaml
spec:
  replicas: 3
  strategy: { rollingUpdate: { maxUnavailable: 0, maxSurge: 1 } }
  containers:
    - name: api
      image: registry/api@sha256:9f2c...        # digest, never :latest
      resources: { requests: {cpu: 250m, memory: 512Mi}, limits: {memory: 512Mi} }
      readinessProbe: { httpGet: {path: /healthz, port: 8080}, periodSeconds: 5, failureThreshold: 3 }
      livenessProbe:  { httpGet: {path: /livez, port: 8080}, periodSeconds: 30, failureThreshold: 3 }
```

- Readiness gates traffic; liveness restarts the pod. Pointing liveness at a dependency restarts every pod when the database blips.
- A memory limit without a request gets a Burstable pod and an eviction under pressure. Set both.
- `kubectl rollout undo deploy/api` is the rollback; `kubectl rollout status` proves it finished.
- A pod stuck in `CrashLoopBackOff` is an application exit, not a node problem: `kubectl logs --previous`.
- `OOMKilled` in `kubectl describe pod` means the limit, not the node, killed it.

## pipeline

```yaml
jobs:
  test:
    steps:
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: pnpm }
      - run: pnpm install --frozen-lockfile
      - run: pnpm test -- --coverage
  deploy:
    needs: test
    environment: production          # required reviewer gate
    steps:
      - run: ./deploy.sh --digest ${{ steps.build.outputs.digest }}
```

- `--frozen-lockfile` in CI. A lockfile drift that installs fine locally fails the build on purpose.
- Cache by lockfile hash. A cache keyed on the branch grows forever and hides dependency drift.
- Build once, promote the same artifact through environments. Rebuilding per environment makes the test meaningless.
- A deploy job needs the test job, a reviewer gate, and the digest it deploys printed in the log.

## incident

1. Declare: SEV1 is customer-facing outage or data loss, SEV2 is degraded with a workaround, SEV3 is internal.
2. First five minutes: stop the bleeding (roll back, flag off, scale), then investigate. Diagnosis before mitigation doubles the outage.
3. One incident commander, one comms owner. Everyone else stays off the channel.
4. Update every 30 minutes, even with no news: impact, action, next update time.
5. Timeline in UTC as you go: time, action, actor, result. Memory reconstructs it wrong.
6. Postmortem within 48 hours: cause, detection gap, action items with owners and dates.

## sdk errors

| status | meaning | action |
| --- | --- | --- |
| 400 | shape | fix the request, do not retry |
| 401 | credential | refresh, check expiry, do not retry blind |
| 403 | authorization or policy | check the role and the resource policy |
| 404 | missing resource | verify the id and the region |
| 409 | conflict or state | read the current state, then decide |
| 429 | throttle | honor `Retry-After`, capped backoff |
| 5xx | provider fault | retry twice, then fail loudly |

A .NET client raises `RequestFailedException`, a Python client a `ClientAuthenticationError` or `HttpResponseError`. Catch the typed error and read the status, never the message text.

## decide

| condition | action |
| --- | --- |
| plan replaces a stateful resource | stop, get approval |
| migration not reversible | snapshot first |
| no health endpoint | add one before the next deploy |
| alert without a runbook | write the runbook or delete the alert |
| p95 over budget after deploy | roll back, then diagnose |
| secret in a pipeline log | rotate, purge the log |
| cost jump over 20% week over week | attribute before optimizing |
| SEV1 with an unknown cause | roll back first, diagnose after |

## numbers

| item | value |
| --- | --- |
| rollout | maxUnavailable 0, maxSurge 1 |
| readiness probe | 5s period, 3 failures |
| liveness probe | 30s period, never on a dependency |
| page threshold | 5xx rate over 2% for 10 min |
| backup | RTO 1h, RPO 15 min, restore tested |
| state | remote, locked, versioned |
| IAM key age | 90 days maximum |

## check

- [ ] plan reviewed, replacements listed
- [ ] remote state locked, versioning on
- [ ] image pinned by digest, not `latest`
- [ ] limits and requests set for every container
- [ ] rollback command written in the PR
- [ ] post-deploy probe recorded with its output

## stop

| condition | action |
| --- | --- |
| production target not named | ask which environment |
| destructive change without a backup | refuse until a snapshot exists |
| credentials requested in chat | refuse, use the secret store |
| incident in progress | stabilize first, no refactors |

## emit

- resources changed, with the plan summary
- probe output and error rate window
- rollback command
- what was not verified
