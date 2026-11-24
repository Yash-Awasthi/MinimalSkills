---
name: general-operations
description: "One merged skill for general cross-domain work: prior-work retrieval, artifact capture, numeric claim checking, OSS opportunity hunting, perk verification, floorplan lookup, reverse engineering stripped Go/Rust, Chinese structural diagnosis, persona simulation, and collaborative discovery. Terse."
license: MIT
---

# General Operations

> Merged from general catalog. Tooling in `scripts/`.

## Routing

- Explicit prior-work/reuse request -> `prior-work-retrieval`.
- Durable record -> `artifact-yylo`.
- Number/speedup/eval claim -> `principle-explain-the-number`.
- OSS contribution -> `oss-hunter`.
- Free credits/tiers/perks -> `perq`.
- Floorplan lookup -> `floorplan-finder`.
- Stripped Go/Rust binary -> `go-rust-reverse`.
- Chinese structural diagnosis -> CrossFrame suite.
- Public persona style -> labelled simulation; verify facts separately.
- Collaborator discovery -> `syncbook-discovery`.
- Audit -> `audit`.

## Workflows

### Prior work retrieval

- Only for explicit history/reuse, not status checks.
- Search existing work; verify artifact; check freshness and scope.
- Reuse only when plausible. Do not treat stale artifact as current execution.
- Report source, version, verification, cost/scope.

### Artifact YYLO

- Profile, payload mode, provenance, retention, secret-safe immutable evidence.
- Capture -> store -> retrieve. Keep evidence immutable.

### Explain the number

- Before acting on a measured number: find limiting factor.
- Rule out that it measured the wrong work.
- Report speedup/regression/latency/throughput/eval with denominator, baseline, condition.

### OSS hunter

- Scan trending repos for high-impact contribution gaps.
- Score impact, fit, maintainer need.
- Output candidate + evidence + action.

### Perq

- Find free AI credits, tiers, startup programs, student perks.
- Attach vendor source link + last-verified date.
- Do not assume availability.

### Floorplan finder

- Find existing residential floor plans; check layout, entrance orientation, source identity.
- Not for designing, generating, certifying drawings.

### Go/Rust reverse

- Recognise runtime; recover pclntab/module metadata; analyse panic strings; use idiomatic decompilation strategies.
- Keep uncertainty explicit.

### CrossFrame suite

- Explicit Chinese structural diagnosis of relationships, organisations, institutions, disputes, long-term evolution.
- Casebook -> reusable cases, anonymised entries, mechanisms, retrieval index.
- Essay -> critical insight/commentary/structure-to-article.
- Public -> governance, policy, institutional responsibility, appeals, compliance evidence.
- Review -> reasoning fidelity, evidence boundaries, source anchors, concept drift, repair.

### Persona simulation

- Label ficticia/ simulation. Separate style from facts. Verify claims.
- Elon Musk / Yann LeCun themes: first principles, neural nets, predictive learning.

### Syncbook discovery

- Find reciprocal collaborators; draft private profile for human review.
- Use only explicitly supplied task facts.

### Audit

- User-authored audit: inspect, report, verify; no auto-fix unless asked.

## Tooling

- `scripts/prior_work.py`, `prior_work_hook.py`, `surface_version.py`, `verify_artifact.py`.
- `scripts/governance.py` for leiloeiro editais.
- `scripts/hunter.py` for OSS hunting.
- Artifact/CrossFrame tooling where present in `scripts/`.

## Output

`request -> route -> evidence/check -> action -> uncertainty`
