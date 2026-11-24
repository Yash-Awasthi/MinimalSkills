# cicd

Load for pipelines, releases and environment promotion.

## pipeline shape

```
lint -> typecheck -> test -> build -> scan -> deploy(staging) -> smoke -> deploy(prod)
```

- Fail fast: cheapest check first.
- Cache dependencies keyed by the lockfile hash.
- One job per concern, with the artifact passed between jobs, not rebuilt.
- Pin action and image versions by digest or tag. `@main` is a supply-chain hole.

## required checks

| check | blocks merge |
| --- | --- |
| lint and format | yes |
| typecheck | yes |
| unit and integration tests | yes |
| build | yes |
| dependency and image scan | high and critical |
| secret scan | any hit |
| coverage on changed lines | project policy |

A workflow that is not a required check in branch protection does not block anything.

## environments

| env | data | access | deploy |
| --- | --- | --- | --- |
| preview | synthetic | team | per PR |
| staging | anonymized | team | on merge |
| production | real | break-glass | on approval |

- No production credentials in a preview job.
- Preview environments expire. An orphaned preview is a cost and a leak.

## deploy strategy

| strategy | use when | rollback |
| --- | --- | --- |
| rolling | default | previous image |
| blue-green | instant cutover needed | switch back |
| canary | risk is measurable | shift traffic to zero |

Canary needs a metric and a threshold before it starts: error rate over 1% or p95 over 500ms for 5 minutes rolls back automatically.

## secrets

- Injected at runtime from the platform store.
- Masked in logs, never echoed.
- Scoped per environment, rotated on a schedule.
- A secret printed in a log is compromised. Rotate first, then purge.

## artifacts

```bash
docker build -t app:${GIT_SHA} .
docker push registry/app:${GIT_SHA}
```

- Tag with the commit sha. `latest` is not a version.
- Sign the image and verify at deploy.
- Keep the SBOM with the artifact.

## release notes

Generated from merged PR titles, grouped by type, linked to issues. Written by the pipeline, reviewed by a human.
## ci platform index

| platform | the rule that matters |
| --- | --- |
| GitLab CI | `rules:` over `only/except`; `needs:` for a DAG; `cache:key:files: [lockfile]` or the cache grows stale. |
| Jenkins | Declarative pipeline, `agent { docker }`, credentials via `withCredentials`; a plugin update is a production change, pin versions. |
| CircleCI | `restore_cache` keyed on the lockfile hash; `when: always` for artifact upload, or a failed build loses its logs. |
| Pre-ship gate | Tests, lint, typecheck, secret scan, migration dry run; a gate that can be skipped is not a gate. |
| Production runtime certification | The artifact that passed staging is the one promoted; a rebuild per environment invalidates the test. |
| Vercel | Preview per PR, `VERCEL_ENV` differs per target; a serverless function has a 10s default timeout and no persistent disk. |
| Cloudflare | Workers have 128MB and CPU-time limits, not wall-clock; `wrangler tail` for logs, KV is eventually consistent. |
| Publishing helpers | `npm publish --provenance`, `cargo publish --dry-run`, a signed tag; a publish without the changelog is a support ticket. |
| HyperExecute | Parallel test orchestration: `hyperexecute.yaml` with a matrix; a flaky test retried in the matrix hides the flake. |
| WebdriverIO | `wdio.conf.ts` with `specFileRetries: 1`; a retry that passes still needs a flake ticket. |
| Newman CI/CD | `newman run collection.json -e env.json --bail`; the collection is the contract test, keep it in the repo. |
