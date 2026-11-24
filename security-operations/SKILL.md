---
name: security-operations
description: Use when testing, reviewing or auditing under written authorization: web and application assessment, auth and access control, cloud and container posture, red team planning, control mapping, finding writeups. Triggers: pentest, ROE, OWASP, finding, audit evidence.
---

# security-operations

## use when

- web, auth or access control test -> references/appsec.md
- red team, adversary simulation, detection -> references/redteam.md
- cloud, container, kubernetes posture -> references/cloud.md
- control mapping, audit evidence, framework gap -> references/compliance.md
- finding writeup, evidence handling, redaction -> references/evidence.md

not for: product hardening outside a test (backend-api), code review severity (engineering-craft)

## rules

- Conflict order: authorization, then target safety, then coverage; coverage never justifies the first two.
- No written authorization, no active testing. Scope, window, techniques, emergency contact.
- Minimum necessary action: reversible over irreversible, and a stop on real user data.
- Ownership proven before testing: owned domain, publisher account, org tenant. A name match is not proof.
- Separate observed, inferred and unverified; record time, target, action, result and hash for each, and redact before any artifact leaves the environment, never storing real PII.
- A scanner hit is a candidate. Reachability and version confirmed before it is a vulnerability.
- Nothing returned is reported as clean; state the scope, method and window with it.

## change

1. Locate: the endpoint, the account role used, and the evidence id that covers it.
2. Propose the test action with its expected signal, and the alternative you rejected.
3. Predict before sending: status, response body, and whether the check passes.
4. Back up the request and the pre-test state in context, pinned to the ROE window.
5. Apply one request per variable; two payload changes produce unreadable evidence.
6. Verify: reproduce from a clean session on the same account type, hash the response.
7. Regress: one payload variation to prove the class is closed, not just the string.
8. Compare the response against the prediction; an unexpected 200 stops the sequence.
9. Report finding, evidence id and scope, then take the next item.

## authorize

1. Collect: signed ROE, target list, window with dates and hours, allowed techniques, emergency contact, legal reference.
2. Record out of scope: systems that cannot take downtime, third-party SaaS, destructive actions, social engineering of named individuals.
3. Set a kill date on every beacon and callback.
4. Missing any item: stop, ask. Authorization is not permission to cause harm.

```
scope:    app.example.com, api.example.com (owned, verified by DNS TXT)
window:   2026-12-01 09:00 to 2026-12-05 18:00 UTC
allow:    authenticated web testing, 2 accounts per role
deny:     DoS, phishing, production data exfiltration, third-party SaaS
contact:  security@example.com, +1-555-0100 (24h)
```

## classes

| class | probe | signal |
| --- | --- | --- |
| injection | `' OR 1=1--`, `${7*7}` | error text, 49, time delta |
| xss | `<img src=x onerror=alert(1)>` | reflected unencoded, stored |
| ssrf | `http://169.254.169.254/latest/meta-data/` | metadata body |
| idor | swap an id for another user's | foreign object returned |
| traversal | `../../etc/passwd`, `%2e%2e%2f` | file content |
| open redirect | `?next=https://evil.test` | 302 to a foreign host |
| mass assignment | add a field the ui never sends | field accepted |
| auth bypass | replay with a lower-privilege token | object returned |

One parameter per request. Two variables produces unreadable evidence.

## test

1. Passive first: DNS, certificates, public metadata. No packets to the target: `subfinder -d example.com -silent`, `curl -sI https://target.example.com`.
2. Confirm the ownership signal. No signal, quarantine the asset.
3. Active: rate limited, minimum proof. Three records prove a missing check; three thousand create liability.
4. Capture per action: UTC ISO 8601, source IP, target, payload, response, hash of extracted data.
5. Stop on PII, credentials or a live threat actor. Notify per the ROE threshold.

## evidence

```json
{"ts":"2026-12-01T10:14:22Z","actor":"tester-1","src":"203.0.113.9",
 "target":"api.example.com","method":"GET","path":"/v1/invoices/1042",
 "payload":null,"status":200,"bytes":812,"note":"foreign tenant invoice",
 "hash":"sha256:4f1c..."}
```

- One record per request that matters, written as it happens, not reconstructed.
- The hash proves the artifact did not change after capture.
- Screenshots include the URL bar and a clock. A cropped screenshot is not evidence.
- Store in an encrypted volume; delete at the end of the engagement and record the deletion.

## report

```
Finding: IDOR on invoice read
Severity: high (single-tenant data, authenticated)
Endpoint: GET /v1/invoices/{id}
Repro: 1. sign in as tenant A  2. request tenant B's id  3. 200 with their data
Impact: any authenticated user reads any invoice by id enumeration
Fix: authorize the row owner; return 404 for a foreign id
Evidence: ev-014.json, sha256:4f1c...
```

- Severity from impact and reachability, not the scanner label.
- Repro is numbered and works from a clean session. A repro that needs your notes is unusable.
- Fix is one sentence a developer can act on. "Improve authorization" is not a fix.
- Every finding names its evidence id, so a reviewer can check the claim.

## severity

| level | criteria |
| --- | --- |
| critical | unauthenticated remote execution, auth bypass, mass data |
| high | single-user data, privilege escalation, stored injection |
| medium | limited disclosure, requires interaction, defense in depth |
| low | hardening gap, no demonstrable impact, defense in depth only |

## retest

1. Re-run the exact repro from the report, same account type.
2. Fixed only when the original request now fails and the legitimate path still works.
3. A fix that blocks the payload but not the class is partial: test one variation.
4. Record the retest date and the build or commit tested.

## decide

| condition | action |
| --- | --- |
| no signature | planning and passive analysis only |
| shared or third-party asset | quarantine, do not test |
| proof needs destructive action | stop, report the theory |
| live adversary discovered | stop, notify per ROE |
| real user data reachable | capture minimal, hash ids |
| scope expired | stop, new authorization required |
| finding is a scanner hit | triage reachability and version |

## check

- [ ] ROE signed and on file
- [ ] target list matches DNS and whois
- [ ] every beacon has a kill date
- [ ] every finding has a timestamp and an evidence hash
- [ ] artifacts redacted, exif stripped: `exiftool -all= out.png`
- [ ] out-of-scope list written down

## stop

| condition | action |
| --- | --- |
| no authorization | refuse active work |
| ownership ambiguous | treat as third-party |
| production with no window | refuse until a window exists |
| request to weaken a control | refuse, report |

## emit

- scope tested, window, techniques
- findings with severity, evidence, reproduction
- what was not tested and why
