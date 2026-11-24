---
name: prodsec
description: >
  Product-security controls for AI systems, agents, MCP servers and clients, inference
  engines, model registries, RAG, API gateways, Kubernetes/OpenShift, containers, crypto,
  web apps, supply chain, fuzzing, and secure code review. Use when designing, reviewing,
  auditing, or threat-modeling an AI product or its infrastructure; when checking authn,
  authz, TLS, secrets, tokens, model integrity, SBOM, logging, or container hardening;
  or when a review needs a MUST/SHOULD security verdict with evidence.
metadata:
  curated_from: 145
  controls: 145
  assets: 7
---

# prodsec

145 controls. One hub. Every original body preserved verbatim in
`references/controls/<name>.md`. Route by category, load only the controls for the target.

## When to use

Use when:
- Designing or reviewing an AI system, agent, MCP server, MCP client, inference engine, model registry, RAG pipeline, or API gateway.
- Auditing authn, authz, OAuth/OIDC, SPIFFE/SPIRE, mTLS, tokens, secrets, TLS, or key lifecycle.
- Reviewing Kubernetes, OpenShift, containers, Helm, CI/CD, supply chain, SBOM, or signing.
- Reviewing crypto, web input handling, serialization, file uploads, database access, or messaging.
- Running or reviewing fuzzing, sanitizers, CodeQL, Semgrep, or variant analysis.
- Reviewing AI-generated code or a patch for security.

Do not use when:
- Task is pure feature work with no trust boundary, credential, data, or deployment surface.
- Target is a compliance certificate. Controls inform evidence; they do not certify.

## Severity rule

- `MUST` / `MUST NOT` violation: blocking. Report before approval.
- `SHOULD` / `SHOULD NOT` deviation: advisory. Report with the accepted risk or the reason.
- Missing control for the target: say `no control`. Do not invent one.
- Two controls conflict: stricter control wins. Name both.

## Blocking floor

1. Each agent MUST have its own identity: service account or SPIFFE ID. Never inherit or impersonate a human identity.
2. Agent-to-agent traffic MUST use SPIFFE/SPIRE plus mTLS.
3. Every principal MUST be identified, authenticated, and authorized before a request reaches a model or external data source. Authentication alone is not authorization.
4. Authorization MUST live in the business-logic layer. Not in individual resolvers.
5. Credentials MUST NEVER be stored in source code. Use a secret manager, workload identity, or short-lived scoped tokens.
6. MCP servers MUST NOT forward user credentials or tokens to downstream tools or third-party APIs. Obtain separate downstream credentials.
7. MCP servers MUST act as OAuth 2.1 resource servers by default; implement Protected Resource Metadata (RFC 9728); validate every token; enforce granular scopes and explicit user consent.
8. Inference engines MUST use JWT access tokens with a maximum TTL of 15 minutes and MUST validate against the IdP JWKS endpoint on every request.
9. Every network connection MUST use TLS. Clients MUST verify the server identity. No prompts or responses over plaintext.
10. All security controls MUST be server-side. Client-side validation is UX only.
11. MCP servers MUST treat every input as untrusted and MUST resist tool/server injection and rug-pulls.
12. Model files, RAG data, and model storage MUST be protected against unauthorized access and modification.
13. Every release MUST include an SBOM. CI/CD MUST scan for vulnerabilities before production.
14. Binaries and container images MUST be digitally signed. Verify provenance before deploy.
15. Containers MUST run as a non-root user.
16. Sensitive external-data access MUST be logged. Logs MUST scrub secrets and sensitive data.
17. Untrusted input MUST be validated at the trust boundary and MUST never be interpreted as code.
18. Model code and agent tools MUST run in an isolated sandbox that cannot reach the host, network, or secrets beyond its grant.

## Strong defaults

- API keys SHOULD NOT be used in production. Prefer short-lived, scoped bearer tokens from an identity provider.
- MCP servers SHOULD avoid sampling; it creates a bidirectional trust relationship.
- A guardrail SHOULD inspect data in both directions between users and models.
- API gateways SHOULD rate-limit and reject malformed requests before dispatch.
- MCP servers SHOULD implement RBAC as defense in depth, mapping token claims to internal roles.
- Network ACLs SHOULD allow external data sources only from known sources.
- MCP servers SHOULD run in containers with platform security defaults.
- Model registries SHOULD verify signatures. Inference engines SHOULD scan models and verify signatures before load.
- Internal applications SHOULD route through the API gateway, not directly to guardrails or inference engines.
- Dependencies SHOULD be pinned and patched on a defined CVE response plan.

## Route the target

| Category | Controls | Use for |
| --- | --- | --- |
| `secure_development` | 117 | authn/authz, agents, MCP, inference, registries, RAG, Kubernetes/OpenShift, containers, crypto, web, data, supply chain, languages |
| `security_testing` | 17 | fuzzing, sanitizers, constant-time, property-based tests, variant analysis, coverage |
| `security_auditing` | 7 | AI code review, differential review, audit context, false-positive gate, dependency audit, agentic actions |
| `developer_tooling` | 4 | CodeQL, Semgrep, Semgrep rule creation, SARIF parsing |

31 subcategories. Full map: `references/INDEX.md`. Machine-readable:
`references/controls.tsv` — `name, category, subcategory, description, file, source`.

## Workflow

1. **Scope.** Name the target, trust boundaries, data classes, identities, and deploy surface.
2. **Route.** Pick the category and subcategory from `references/INDEX.md`.
3. **Load.** Read only the matching `references/controls/<name>.md` files.
4. **Check.** For each control: pass, fail, not applicable, or unverified. Quote the exact requirement.
5. **Evidence.** Bind every failure to a file and line, config key, command output, or reproduced request.
6. **Fix.** State the smallest change that satisfies the control. Include the safe code or config pattern from the control body.
7. **Recheck.** Re-run the check. Mark unverified items as unverified, never as pass.

## Review verdicts

- `BLOCKED`: any confirmed `MUST` violation, confirmed secret in code, auth bypass, or unsigned deployable.
- `CHANGES`: `MUST` violation requiring design change, or a cluster of `SHOULD` deviations with real exposure.
- `PASS`: all applicable `MUST` controls pass; `SHOULD` deviations listed.
- `UNVERIFIED`: evidence missing. Never fold into `PASS`.

## Evidence rules

- No finding without evidence. Confabulation is not a finding.
- Separate confirmed from suspected. Label each.
- Reproduction beats description: exact request, command, manifest, or diff.
- Redact secrets and personal data in the report. Cite the location, not the value.
- One finding per control. Do not merge unrelated failures.

## Output contract

```
verdict: BLOCKED | CHANGES | PASS | UNVERIFIED
target: <system/component>
controls_checked: <n>  must_fail: <n>  should_fail: <n>  unverified: <n>
```

Then one row per finding:

```
control: <name>  level: MUST|SHOULD  status: fail|unverified
evidence: <file:line | config key | command output>
fix: <smallest change>
ref: references/controls/<name>.md
```

Then one line for the next action. No restated control text.

## Failure handling

| Symptom | Action |
| --- | --- |
| No control for target | Say `no control`. Check sibling subcategory. Do not invent. |
| Two controls conflict | Apply the stricter. Note both. |
| Framework or cloud mismatch | Keep the control requirement; map it to local config. |
| Can't inspect runtime | Mark `unverified`. State the missing evidence. |
| Control body cites a tool | Run the tool. Do not simulate its verdict from memory. |
| Secret found | Block. Report location, never the value. Require rotation and history scan. |

## Provenance

- `SOURCES.md` — all 145 source skills, control name, category.
- `references/controls/` — 145 bodies verbatim, frontmatter stripped, source path in an HTML comment.
- `references/INDEX.md` — category and subcategory map.
- `references/controls.tsv` — 145 rows, lookup table.
- `references/assets/` — 7 support files from 2 controls, original relative paths kept.
