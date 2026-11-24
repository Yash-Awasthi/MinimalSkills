---
name: bug-hunting
description: >
  Authorized bug hunting and red-team testing: 57 vulnerability classes plus 26 engagement
  playbooks, from scoping and ownership triage through recon, exploitation, A-to-B chaining,
  validation, evidence hygiene, and reporting. Use when testing a web, API, cloud, mobile,
  AI/LLM, GraphQL, auth, OAuth/OIDC, Kubernetes, CI/CD, or business-logic surface; when
  hunting IDOR, SSRF, XSS, SQLi, race conditions, cache poisoning, request smuggling, or
  auth bypass; or when validating or writing a finding. Requires explicit written
  authorization and a defined scope.
metadata:
  curated_from: 141
  classes: 57
  playbooks: 26
  assets: 28
---

# bug-hunting

141 skills collapsed: 57 vulnerability classes, 26 playbooks. Both source versions of every
duplicated class kept verbatim. Load one class or playbook. Not the whole tree.

## Authorization floor

1. **Written authorization required.** Target list, scope, time window, allowed techniques, and emergency contact. Missing any: stop.
2. **Ownership is guilty until proven.** An asset belongs to the target only with a concrete signal: owned domain, publisher account, org repo, or org tenant. Scanner keyword match is not proof.
3. **Soft-404 control before any exposure claim.** Request the "finding" and a random junk path. Identical status and byte length: false positive, discard.
4. **Authorized is not unrestricted.** Minimum necessary extraction. Three records that should need auth prove the missing check. Three thousand records create liability, not stronger evidence.
5. **No destructive action, persistence, lockout, or real-user harm.** Stop on real user data. Redact before storage.
6. **Third-party same-name assets are out of scope.** Quarantine them; never test them.
7. **Social engineering only when the rules of engagement explicitly allow it.**
8. **Scope expired or revoked: stop.** Do not resume without new authorization.

## Kill list

Do not report these standalone:

```
theoretical / "could" / dead code / unreachable
scanner output without reproduction
soft-404, catch-all, public data, analytics keys
missing CSP / HSTS / SPF / DKIM / DMARC / cookie flags alone
banner or version without working CVE exploit
clickjacking on non-sensitive page; tabnabbing
CSV injection without code execution
CORS wildcard without credentialed exfiltration
logout CSRF; self-XSS
open redirect alone; SSRF DNS-only; host-header alone
rate limit on non-critical form
session not invalidated on logout; concurrent sessions
internal IP in error; mixed content; weak ciphers; broken links
autocomplete on password fields; GraphQL introspection alone; pre-ATO
```

Chain required before reporting: open redirect → OAuth code theft, clickjacking → sensitive action, CORS → credentialed PII read, CSRF → funds/email/delete, rate-limit bypass → OTP/reset brute force, SSRF → internal data, host header → reset poisoning, prompt injection → cross-user data, bucket listing → secret → OAuth chain.

## 7-question gate

Ask in order. One fail kills that finding, not the engagement.

1. Can an attacker do this right now, step by step, with a real HTTP request?
2. Is the impact on the program's accepted list?
3. Is the root cause in an in-scope production asset?
4. Does it avoid privileged access an attacker cannot realistically get?
5. Is it already known or accepted behavior?
6. Is impact proven beyond "technically possible"? (XSS → session hijack, SSRF → internal data, SQLi → real rows, IDOR → another user's data)
7. Is it free of the never-submit list?

Q6 weak: downgrade severity, do not kill. Q1, Q2, Q3, Q5, Q7 fail: kill.

## Layer-ordering trap

A validation error does not prove auth bypass. Global parsers and sanitizers often run before auth.

```bash
# malformed body — may hit sanitiser before auth
curl -s -X POST https://target/api/v1/resource -d '{'

# same endpoint, well-formed empty object — now auth is reached
curl -s -X POST https://target/api/v1/resource -H 'Content-Type: application/json' -d '{}'
```

Probe auth with the simplest valid body. Input-shape errors are parser errors. WAF/CDN block is not origin behavior. Only a well-formed request that still reaches business logic proves the layer order.

## Workflow

1. **Authorize.** Record target, scope, window, techniques.
2. **Recon.** Subdomains, assets, fingerprints, JS bundles, source, APIs. Triage ownership.
3. **Fingerprint.** Stack, auth model, data value, deploy surface.
4. **Route.** Pick one class from the index. Load `references/classes/<class>.md`.
5. **Hunt deep.** One class at a time. Do not spray.
6. **Confirm.** Real request, real response, real impact. Blind: OOB callback with unique marker.
7. **Chain.** Map siblings. Test A→B→C. Build the chain before reporting.
8. **Gate.** 7 questions, then 4 pre-submission gates.
9. **Evidence.** Redact cookies, tokens, PII. Keep trace IDs and request-shape metadata.
10. **Report.** One report per chain. Then resume coverage on untested classes.

## A→B signals

| Bug A | Hunt B | Escalate C |
| --- | --- | --- |
| IDOR read | PUT/DELETE same endpoint | full record manipulation |
| SSRF any | cloud metadata `169.254.169.254` | IAM credentials → RCE |
| Stored XSS | cookie `HttpOnly` absent | session hijack → ATO |
| Open redirect | OAuth `redirect_uri` accepts domain | auth code theft → ATO |
| Bucket listing | JS bundles | OAuth secret → chain |
| Rate-limit bypass | OTP brute force | ATO |
| GraphQL introspection | missing field auth | mass PII |
| Debug endpoint | env vars | cloud credentials |
| CORS reflect origin | credentialed request | data theft |
| Host header injection | password reset link | ATO |

Cluster protocol: confirm A → map siblings → test same pattern → chain different class → quantify → report one chain.

## Class index

| Group | Classes |
| --- | --- |
| Injection & execution | `sqli` `nosqli` `ldap` `ssti` `xxe` `deserialization` `rce` `lfi` `html-injection` |
| Client-side | `xss` `dom` `csrf` `clickjacking` `cors` `open-redirect` |
| Auth & session | `auth-bypass` `ato` `brute-force` `forgot-password` `mfa-bypass` `oauth` `saml` `jwt-crypto` `session` `ntlm-info` |
| Access & logic | `idor` `business-logic` `race-condition` `captcha-bypass` |
| Request & transport | `http-smuggling` `host-header` `cache-poison` `ssrf` `tls-network` `websocket` `grpc` |
| API & protocol | `api-misconfig` `graphql` `fintech-graphql` `shadow-api` `spa-api` |
| Files & disclosure | `file-upload` `source-leak` `exceptional-conditions` |
| Framework & stack | `aspnet` `laravel` `nextjs` `nodejs` `springboot` `sharepoint` |
| Cloud & CI | `cloud-misconfig` `k8s` `cicd` `subdomain` |
| AI systems | `llm-ai` `rag-vector` |
| Misc | `misc` |

Full table with descriptions: `references/classes.tsv`.
Class bodies: `references/classes/<class>.md`. Each contains every source version.

## Playbooks

| Group | Playbooks |
| --- | --- |
| Engagement | `bug-bounty` `bb-methodology` `bb-local-toolkit` `recon-scope-triage` `security-arsenal` `web2-recon` `supply-chain-attack-recon` `cloud-iam-deep` |
| Reporting | `report-writing` `bugcrowd-reporting` `redteam-report-template` `triage-validation` `evidence-hygiene` |
| Red team | `redteam-mindset` `mid-engagement-ir-detection` `enterprise-vpn-attack` `m365-entra-attack` `okta-attack` `vmware-vcenter-attack` `apk-redteam-pipeline` `ios-redteam-pipeline` |
| OSINT | `offensive-osint` `osint-methodology` |
| Web3 | `web3-audit` `meme-coin-audit` |
| Routing | `hunt-dispatch` |

Bodies: `references/playbooks/<name>.md`. Details and descriptions: `references/playbooks.tsv`.
OSINT scripts and references: `references/assets/`.

## Severity

- **Critical:** any-user ATO without interaction, RCE, SQLi with data exfiltration, admin auth bypass.
- **High:** mass PII, privilege escalation, internal SSRF with data, stored XSS affecting all users.
- **Medium:** IDOR on one user's non-critical data, XSS on a sensitive page requiring a click.
- **Low:** non-sensitive disclosure, clickjacking with a working PoC.
- Program's own severity list wins. Context beats class.

## Reporting

Title: `[Bug Class] in [Endpoint] allows [actor] to [impact]`.

Include:
1. Copy-pasteable HTTP request or exact steps.
2. Evidence of actual impact, not a 200 status.
3. CVSS 3.1 vector plus the program's severity mapping.
4. One or two sentences of concrete remediation.
5. Redacted cookies, tokens, and other-user PII.

Banned phrases: "could potentially", "may allow", "theoretically".

## Output contract

```
target= scope= class= status=confirmed|killed|blocked
request=<method> <path>  evidence=<artifact>  impact=<what attacker gains>  chain=<A->B->C|none>
gate=<pass|fail:Qn>  severity=<critical|high|medium|low|info>
next=<class|report|stop>
```

One line per confirmed chain. One line per killed finding, with the failing gate. No narrative.

## Failure handling

| Symptom | Action |
| --- | --- |
| No ownership proof | Quarantine. Do not test. |
| All 401/403/404 after 5 minutes | Move to another surface. |
| Stuck 1 hour on one target | Switch context. Return later. |
| WAF, captcha, lockout | Note the control. Do not bypass out of scope. |
| Cannot reproduce from fresh session | Kill or downgrade. No report. |
| Possible duplicate | Deduplication gate. Search disclosed reports, issues, changelog. |
| Impact is only "technically possible" | Downgrade, do not inflate. |
| Real user data encountered | Stop extraction. Redact. Report the missing check with minimum proof. |
| Scope exhausted | Stop. Report coverage gaps. |

## Provenance

- `SOURCES.md` — all 141 sources, kind, reference file.
- `references/classes/` — 57 classes, 114 source bodies verbatim. Both versions kept.
- `references/playbooks/` — 26 playbooks, 27 source bodies verbatim.
- `references/classes.tsv`, `references/playbooks.tsv` — lookup tables.
- `references/INDEX.md` — grouped map.
- `references/assets/` — 28 files from 7 sources, including OSINT scripts and reference corpora.
