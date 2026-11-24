---
name: security-operations
description: >
  One standalone skill for offensive and defensive security plus compliance:
  authorized red team operations (ROE, deconfliction, OPSEC, ATT&CK lifecycle,
  reporting), bug hunting (57 vulnerability classes, kill list, 7-question
  gate, chaining, evidence hygiene), product security controls for AI/MCP/
  inference/K8s (MUST/SHOULD verdicts), the defensive and offensive lifecycle
  (recon, scanning, exploit dev, malware, forensics, threat hunting, incident
  response, SIEM, hardening, OT/ICS, GRC, threat intel), and compliance
  frameworks (GDPR, ISO 27001, SOC 2, PCI DSS, HIPAA, FedRAMP). Merges the
  cyber-security (153) and compliance-audit (27) classes and five deep packs
  (security 12, red-team 77, bug-hunting 141, prodsec 145, cyber-masriyan
  22). Fully self-contained: every procedure is inline, no external
  references.
metadata:
  merges: cyber-security, compliance-audit
  sources: 180
---

# security-operations

## 0. Authorization policy (applies to everything below)

1. **Signed authorization is mandatory for any active testing.** The rules
   of engagement (ROE) are a legal document, not a formality. No signature,
   no testing. Every active skill requires written authorization for the
   named scope: target list, scope, time window, allowed techniques, and
   emergency contact. Missing any: stop.
2. **The ROE must contain:** authorization window with exact dates and
   hours; authorized techniques and permitted ATT&CK tactics; notification
   thresholds; a 24/7 emergency phone for deconfliction; a legal shield
   referencing the CFAA (US), Computer Misuse Act (UK), or local equivalent.
3. **Record what is out of scope:** production systems that cannot tolerate
   downtime, third-party SaaS without authorization, destructive actions,
   and social engineering of named individuals (executives, legal counsel).
4. **Authorization is not permission to cause harm.** Minimum necessary
   action; reversible over irreversible. No destructive action, no denial of
   service, no real-user harm unless the ROE explicitly authorizes it.
5. **Stop and notify** on discovering an active threat actor, child
   exploitation material, or accidental data destruction. These are
   notification thresholds, not judgment calls.
6. **Kill dates on every beacon.** A forgotten callback months later is
   legal liability. Scope expired or revoked: stop; no resumption without
   new written authorization.
7. **Ownership is guilty until proven.** An asset belongs to the target
   only with a concrete signal: owned domain, publisher account, org repo,
   or org tenant. A scanner keyword or name match is not proof. Third-party
   same-name assets are quarantined, never tested.
8. **Authorized is not unrestricted.** Minimum necessary extraction. Three
   records that should need auth prove the missing check; three thousand
   create liability, not stronger evidence. Stop on real user data; redact
   before storage.
9. **Social engineering only when the ROE explicitly allows it.** Wireless
   deauth, RF replay and similar stay lab-only. No destructive action,
   persistence, or lockout.
10. **No scope, no scanning** — restrict the answer to planning, coverage
    analysis, detection engineering, and tabletop work, and say so. Passive
    analysis and document work can proceed without authorization.

## 1. Evidence contract (every finding, every pack)

- Separate **observed**, **inferred**, and **unverified**. Record the source
  or artifact reference, the SHA-256 when a file is available, the
  collection time, the validation performed, the limitation, and the next
  verification step.
- Extraction confidence is not maliciousness confidence; unknown
  maliciousness stays unknown. A script output is a candidate, not a
  conclusion — state what each tool did and did not do; never present
  simulated or sample output as live evidence.
- A control is not in place because a document says so. Record the
  configuration, command output, screenshot, or policy section that proves
  it, with the date and the system. An unverified control is reported as
  unverified. A checklist is not a certification; a policy is not an audit.
- A scanner result is a candidate. A SAST match, dependency advisory, or
  secret pattern needs triage for reachability, exploitability, and the
  actual version before it is a vulnerability. State the rule, the file,
  and the version. A false positive is not a defect; an unpatched
  dependency is not automatically exploitable.
- A scan or query returning nothing is reported as a negative with scope
  and method — never call it clean. A partial or truncated result is
  reported as the bounded window, never as complete.
- Capture for every finding and action: UTC timestamp (ISO 8601), source IP
  including pivots, target host/URL/RPC interface, action sent, result
  received, hash of any extracted data.
- Redaction before any artifact leaves the secure environment: credentials
  become placeholders (`<REDACTED-PASSWORD>`, `<TOKEN-A1>`); extracted PII
  is hashed, never real names/emails/SSNs in screenshots; crop screenshots
  and check browser tabs for session tokens; `exiftool -all= *.png`; remove
  debug toolbars revealing client infrastructure.

## 2. Bug hunting (57 classes, 26 playbooks)

**Kill list — never report standalone:** theoretical/"could"/dead code/
unreachable; scanner output without reproduction; soft-404, catch-all,
public data, analytics keys; missing CSP/HSTS/SPF/DKIM/DMARC/cookie flags
alone; banner or version without working CVE exploit; clickjacking on
non-sensitive page; tabnabbing; CSV injection without code execution; CORS
wildcard without credentialed exfiltration; logout CSRF; self-XSS; open
redirect alone; SSRF DNS-only; host-header alone; rate limit on non-critical
form; session not invalidated on logout; concurrent sessions; internal IP in
error; mixed content; weak ciphers; broken links; autocomplete on password
fields; GraphQL introspection alone; pre-ATO.

**Chain required before reporting:** open redirect → OAuth code theft;
clickjacking → sensitive action; CORS → credentialed PII read; CSRF →
funds/email/delete; rate-limit bypass → OTP/reset brute force; SSRF →
internal data; host header → reset poisoning; prompt injection → cross-user
data; bucket listing → secret → OAuth chain.

**7-question gate** (ask in order; one fail kills that finding, not the
engagement):
1. Can an attacker do this right now, step by step, with a real HTTP request?
2. Is the impact on the program's accepted list?
3. Is the root cause in an in-scope production asset?
4. Does it avoid privileged access an attacker cannot realistically get?
5. Is it already known or accepted behavior?
6. Is impact proven beyond "technically possible"? (XSS → session hijack,
   SSRF → internal data, SQLi → real rows, IDOR → another user's data)
7. Is it free of the never-submit list?

Q6 weak: downgrade severity, do not kill. Q1, Q2, Q3, Q5, Q7 fail: kill.

**Layer-ordering trap:** a validation error does not prove auth bypass —
global parsers and sanitizers often run before auth. Probe auth with the
simplest valid body; input-shape errors are parser errors; a WAF/CDN block
is not origin behavior. Only a well-formed request that still reaches
business logic proves the layer order.

**Soft-404 control:** request the "finding" and a random junk path.
Identical status and byte length: false positive, discard.

**Workflow:** authorize (record target, scope, window, techniques) → recon
(subdomains, assets, fingerprints, JS bundles, source, APIs; triage
ownership) → fingerprint (stack, auth model, data value, deploy surface) →
route (pick one class) → hunt deep (one class at a time, do not spray) →
confirm (real request, real response, real impact; blind findings get an OOB
callback with a unique marker) → chain (map siblings, test A→B→C) → gate →
evidence (redact cookies, tokens, PII; keep trace ids and request-shape
metadata) → report (one report per chain) → resume coverage on untested
classes.

**A→B escalation signals:** IDOR read → PUT/DELETE same endpoint → full
record manipulation; SSRF → cloud metadata 169.254.169.254 → IAM
credentials → RCE; stored XSS → HttpOnly absent → session hijack → ATO;
open redirect → OAuth redirect_uri accepts domain → auth code theft → ATO;
bucket listing → JS bundles → OAuth secret → chain; rate-limit bypass → OTP
brute force → ATO; GraphQL introspection → missing field auth → mass PII;
debug endpoint → env vars → cloud credentials; CORS reflect origin →
credentialed request → data theft; host header injection → password reset
link → ATO. Cluster protocol: confirm A → map siblings → test same pattern
→ chain a different class → quantify → report one chain.

**Class index (57):** injection & execution (sqli, nosqli, ldap, ssti, xxe,
deserialization, rce, lfi, html-injection); client-side (xss, dom, csrf,
clickjacking, cors, open-redirect); auth & session (auth-bypass, ato,
brute-force, forgot-password, mfa-bypass, oauth, saml, jwt-crypto, session,
ntlm-info); access & logic (idor, business-logic, race-condition,
captcha-bypass); request & transport (http-smuggling, host-header,
cache-poison, ssrf, tls-network, websocket, grpc); API & protocol
(api-misconfig, graphql, fintech-graphql, shadow-api, spa-api); files &
disclosure (file-upload, source-leak, exceptional-conditions); framework &
stack (aspnet, laravel, nextjs, nodejs, springboot, sharepoint); cloud & CI
(cloud-misconfig, k8s, cicd, subdomain); AI systems (llm-ai, rag-vector);
misc.

**Playbooks (26):** engagement (bug-bounty, bb-methodology, bb-local-
toolkit, recon-scope-triage, security-arsenal, web2-recon, supply-chain-
attack-recon, cloud-iam-deep); reporting (report-writing, bugcrowd-
reporting, redteam-report-template, triage-validation, evidence-hygiene);
red team (redteam-mindset, mid-engagement-ir-detection, enterprise-vpn-
attack, m365-entra-attack, okta-attack, vmware-vcenter-attack,
apk-redteam-pipeline, ios-redteam-pipeline); OSINT (offensive-osint,
osint-methodology); web3 (web3-audit, meme-coin-audit); routing
(hunt-dispatch).

**Severity:** Critical — any-user ATO without interaction, RCE, SQLi with
data exfiltration, admin auth bypass. High — mass PII, privilege
escalation, internal SSRF with data, stored XSS affecting all users. Medium
— IDOR on one user's non-critical data, XSS on a sensitive page requiring a
click. Low — non-sensitive disclosure, clickjacking with a working PoC. The
program's own severity list wins; context beats class.

**Report format:** title `[Bug Class] in [Endpoint] allows [actor] to
[impact]`; include copy-pasteable HTTP request or exact steps; evidence of
actual impact, not a 200 status; CVSS 3.1 vector plus the program's
severity mapping; one or two sentences of concrete remediation; redacted
cookies, tokens, and other-user PII. Banned phrases: "could potentially",
"may allow", "theoretically".

## 3. Red team operations (77 tactics)

**Engagement objectives** (pick in writing): data exfiltration (retrieve
specific records), domain dominance (Domain Admin or equivalent), business
process disruption (halt a critical workflow), physical access. Scenarios:
assumed breach (standard-user foothold, test post-exploitation), external
to internal (full chain from the internet), insider threat (legitimate
credentials, data loss and sabotage), physical/cyber hybrid (tailgating,
badge cloning, drop box).

**Lifecycle (ATT&CK):** planning (scope, ROE, deconfliction, legal) →
infrastructure (domain aging, VPS, redirectors, TLS; TA0042) → initial
access (phishing, exploitation, physical; TA0001) → execution (loader →
minimal implant → full C2; TA0002) → persistence (registry, scheduled
tasks, DLL hijack; TA0003) → privilege escalation (token manipulation, UAC
bypass, kerberoast; TA0004) → defense evasion (AMSI bypass, ETW patch,
unhook, LOLBins; TA0005) → credential access (LSASS dump, kerberoast,
DCSync; TA0006) → discovery (AD enumeration, network scanning; TA0007) →
lateral movement (WinRM, SMB, DCOM, RDP hijack; TA0008) → collection
(stage sensitive data, encrypt; TA0009) → exfiltration (DNS tunnel, HTTPS
chunked, cloud storage; TA0010) → C2 (malleable profiles, sleep/jitter,
fallbacks; TA0011) → cleanup (remove artifacts, verify, document) →
reporting (narrative, findings, ATT&CK map, debrief).

**Deconfliction:** trusted agent (one or two defenders who know and can
confirm or deny activity on a secure channel), code word embedded in
tooling or traffic, and a timestamped log shared near-real-time. Log entry
format: timestamp | operator | action | target | technique (T-id) | tool |
notes | deconfliction code. All operator communications use end-to-end
encrypted channels; never discuss target details over plain email or Slack.

**OPSEC non-negotiables:** team server binds to 127.0.0.1 only, all
external access via redirector/tunnel; kill dates on every beacon, no
exceptions; zero-sleep only during active hands-on-keyboard, 60s+ otherwise;
encrypt all collected data immediately, never store plaintext credentials;
separate infrastructure per tier — burning T1 must not expose T3; strip
metadata from all delivered files; log every action with timestamp, target,
technique, deconfliction code; never reuse infrastructure, domains or
tooling across engagements.

**Infrastructure:** three tiers — T1 delivery (burn expected), T2
short-haul C2 (interactive), T3 long-haul C2 (protect). Separate domains,
VPS providers and operator accounts per tier. Register domains 14–30 days
before the engagement; categorize as Business or Technology, never
Uncategorized. Never expose the team server directly; filter at the
redirector by URI and User-Agent. TLS from Let's Encrypt or a commercial
CA, never self-signed.

**C2 profile checklist:** host_stage=false (disable staging); sleep/jitter
configured per beacon tier; User-Agent matches the target's legitimate
traffic; URIs mimic real application endpoints; memory obfuscation enabled
(sleep_mask, obfuscate); valid TLS certificate in keystore; spawn-to
process set to a legitimate binary (not rundll32); named pipes randomized
(not default CS pattern). Beacon timing: interactive 5–10s sleep / 30–50%
jitter; idle 60–300s / 30–50%; long-haul 12–24h / 50%; exfiltration 30–60s
/ 20%. Fallback chain: HTTPS via CDN → DNS-over-HTTPS → DNS TXT → ICMP/raw
TCP as last resort. Failed channels back off exponentially, then dormant
retry; never noisy failed connections.

**Attribution and tooling:** dedicated VPN or Tor for engagement activity;
engagement-specific pseudonyms and disposable email; no reuse across
engagements. Strip metadata (`exiftool -all= file`, verify with grep for
author/creator/company/producer; `strip --strip-all implant`; `objcopy
--remove-section=.note.gnu.build-id implant`). Modify tool signatures:
Cobalt Strike — never the default profile; change named pipes, watermark,
injection technique. Mimikatz — build from source or use `nanodump`,
`PPLdump`, or `comsvcs.dll`. Impacket — change default service names, pipe
names, banners. Maintain a running indicator list (files dropped, registry
keys, services, scheduled tasks, accounts created); remove every artifact
at engagement end or hand the client the complete list. Clear event logs
only when the ROE explicitly authorizes it.

**Data handling:** encrypt collected data immediately; never store
plaintext credentials, PII or sensitive business data unencrypted. Stage
before exfiltration: copy to a staging directory, compress, encrypt,
transfer — never exfiltrate directly from the source. Chain of custody:
SHA-256 hash every file at collection, log who accessed what and when,
store on encrypted access-controlled media, destroy client data after the
agreed retention period (typically 30–90 days post-report). Example:
`tar czf - loot/ | gpg --symmetric --cipher-algo AES256 --batch
--passphrase-file /path/to/engagement.key > loot.tar.gz.gpg`, then scp to
the evidence store and write a `.sha256` sidecar.

**Evasion baseline:** AMSI inspects PowerShell, VBScript, JScript and .NET
assembly loads — bypass before suspicious commands in those contexts (patch
`AmsiScanBuffer` to return clean or set `amsiInitFailed`). ETW feeds EDR
telemetry — patching `EtwEventWrite` in ntdll to `0xC3` neutralizes that
channel. Unhooking and direct syscalls avoid user-mode hooks; prefer direct
or indirect syscalls from a clean ntdll copy where the EDR watches for
in-memory patching. LOLBins blend execution into legitimate binaries —
prefer signed system binaries over dropped tooling.

**Tactic groups:** Web & API (xss, ssrf, ssti, xxe, idor, file-upload,
deserialization, request-smuggling, race-condition, toctou,
parameter-pollution, open-redirect, jwt, oauth, graphql, api-abuse,
api-security, business-logic, waf-bypass, crypto-attacks, vuln-classes,
fast-checking); Windows & AD (windows-privesc, windows-mitigations,
windows-boundaries, active-directory, lateral-movement, persistence,
anti-forensics, netexec, edr-evasion, shellcode, keylogger-arch); exploit
dev & research (linux-privesc, basic-exploitation, crash-analysis,
exploit-development, exploit-dev-course, mitigations, fuzzing,
fuzzing-course, bug-identification); cloud & supply chain (cloud,
k8s-attacks, container-escape, cicd-pipeline, cicd-secrets,
dependency-confusion, supply-chain); network & operations (network-attacks,
tls-attacks, data-exfiltration, c2-frameworks, initial-access,
advanced-redteam); wireless/RF/hardware (wifi, wifi-recon, wpa2-psk,
wpa3-sae, wpa-enterprise, wps, evil-twin, deauth-disassoc,
krack-fragattacks, bluetooth-ble, bluetooth-classic, zigbee-thread-matter,
z-wave, lorawan-sub-ghz, iot); OSINT/social/mobile (osint,
osint-methodology, social-engineering, phishing, mobile); AI security
(ai-security); reporting.

**Report structure:** 1) executive summary, 1–2 pages, business impact,
non-technical; 2) engagement overview (scope, objectives, timeline,
methodology, limitations); 3) attack narrative — chronological chain from
initial access to objective with timestamps and screenshots; 4) technical
findings — description, affected systems, MITRE ATT&CK mapping, evidence,
risk rating, remediation; 5) ATT&CK heat map — techniques used, where
detection succeeded and failed; 6) remediation roadmap prioritized by
effort and impact; 7) indicator appendix — every IOC introduced (IPs,
domains, file hashes, accounts, registry keys). One finding per file or
section; executive summary last to write, first to read. Each finding:
summary, background, description, reproduction steps, evidence, impact,
remediation (fix the bug → defense in depth → detection), references,
retest notes. Chains get their own narrative because the combination often
warrants higher severity than any single finding.

**Severity:** CVSS v3.1 as the floor, then sanity-check against business
impact; justify every metric in one sentence; if two reasonable people
would score differently, document why. CVSS v4.0 only when the client
mandates it. Never over-CVSS — a "Medium" XSS in an authenticated PII panel
can outrank an unauthenticated "High" on a metadata-less internal service;
add a Business Impact Adjustment rather than lie with the score. Anchors:
Critical — domain dominance, RCE, mass data exfiltration, full auth
bypass. High — privilege escalation, lateral movement to tier-0, targeted
sensitive data access, detection evasion across the estate. Medium —
limited access or disclosure requiring conditions the attacker can meet.
Low — information disclosure or hygiene issue with no direct path. The
ROE, client risk model and demonstrated impact outrank the class.

**Common mistakes to avoid:** CVSS 9.0 on everything, marketing language,
raw tool output as evidence, generic remediation, missing reproduction
steps, untimed evidence, ungrouped identical findings, no retest plan,
conflating scope with limitations, informational findings used as filler.

**Deliverables:** Markdown is the single source of truth; generate PDF,
DOCX, HTML, JSON and CSV from it. Never maintain parallel formats by hand.
Purple-team debrief within one week of report delivery: walk the chain with
red and blue present; at each step — did blue detect it, how fast, and if
not why not; map gaps to logging, alerting or tooling; write detection
rules for techniques that evaded monitoring; replay techniques in a
controlled setting so defenders can tune.

## 4. Product security controls (MUST/SHOULD verdicts)

**Severity rule:** a `MUST`/`MUST NOT` violation is blocking — report before
approval. A `SHOULD`/`SHOULD NOT` deviation is advisory — report with the
accepted risk or the reason. A missing control for the target: say `no
control`, do not invent one. Two controls conflict: the stricter wins; name
both.

**Blocking floor (MUST):**
1. Each agent has its own identity: service account or SPIFFE ID. Never
   inherit or impersonate a human identity.
2. Agent-to-agent traffic uses SPIFFE/SPIRE plus mTLS.
3. Every principal is identified, authenticated and authorized before a
   request reaches a model or external data source. Authentication alone is
   not authorization.
4. Authorization lives in the business-logic layer, not in individual
   resolvers.
5. Credentials are never stored in source code — secret manager, workload
   identity, or short-lived scoped tokens.
6. MCP servers never forward user credentials or tokens to downstream tools
   or third-party APIs; obtain separate downstream credentials.
7. MCP servers act as OAuth 2.1 resource servers by default; implement
   Protected Resource Metadata (RFC 9728); validate every token; enforce
   granular scopes and explicit user consent.
8. Inference engines use JWT access tokens with a maximum TTL of 15 minutes
   and validate against the IdP JWKS endpoint on every request.
9. Every network connection uses TLS; clients verify server identity; no
   prompts or responses over plaintext.
10. All security controls are server-side; client-side validation is UX
    only.
11. MCP servers treat every input as untrusted and resist tool/server
    injection and rug-pulls.
12. Model files, RAG data and model storage are protected against
    unauthorized access and modification.
13. Every release includes an SBOM; CI/CD scans for vulnerabilities before
    production.
14. Binaries and container images are digitally signed; verify provenance
    before deploy.
15. Containers run as a non-root user.
16. Sensitive external-data access is logged; logs scrub secrets and
    sensitive data.
17. Untrusted input is validated at the trust boundary and never
    interpreted as code.
18. Model code and agent tools run in an isolated sandbox that cannot reach
    the host, network or secrets beyond their grant.

**Strong defaults (SHOULD):** API keys not in production — prefer
short-lived scoped bearer tokens from an IdP. MCP servers avoid sampling
(it creates a bidirectional trust relationship). A guardrail inspects data
in both directions between users and models. API gateways rate-limit and
reject malformed requests before dispatch. MCP servers implement RBAC as
defense in depth, mapping token claims to internal roles. Network ACLs
allow external data sources only from known sources. MCP servers run in
containers with platform security defaults. Model registries verify
signatures; inference engines scan models and verify signatures before
load. Internal applications route through the API gateway, not directly to
guardrails or inference engines. Dependencies pinned and patched on a
defined CVE response plan.

**Control categories:** secure_development (117 controls — authn/authz,
agents, MCP, inference, registries, RAG, Kubernetes/OpenShift, containers,
crypto, web, data, supply chain, languages); security_testing (17 —
fuzzing, sanitizers, constant-time, property-based tests, variant
analysis, coverage); security_auditing (7 — AI code review, differential
review, audit context, false-positive gate, dependency audit, agentic
actions); developer_tooling (4 — CodeQL, Semgrep, Semgrep rule creation,
SARIF parsing).

**Workflow:** scope (name the target, trust boundaries, data classes,
identities, deploy surface) → route (pick category and subcategory) → load
(read only the matching controls) → check (pass, fail, not applicable, or
unverified; quote the exact requirement) → evidence (bind every failure to
a file and line, config key, command output, or reproduced request) → fix
(state the smallest change that satisfies the control, with the safe code
or config pattern) → recheck (mark unverified items unverified, never
pass).

**Review verdicts:** `BLOCKED` — any confirmed MUST violation, confirmed
secret in code, auth bypass, or unsigned deployable. `CHANGES` — MUST
violation requiring design change, or a cluster of SHOULD deviations with
real exposure. `PASS` — all applicable MUST controls pass; SHOULD
deviations listed. `UNVERIFIED` — evidence missing; never folded into
PASS. Evidence rules: no finding without evidence — confabulation is not a
finding; separate confirmed from suspected; reproduction beats description
(exact request, command, manifest, or diff); redact secrets and personal
data, citing the location not the value; one finding per control.

## 5. Defensive and offensive lifecycle (22-skill curriculum)

**Discovery and assessment:**
- **Recon/OSINT** (01-recon-osint, web2-recon, shodan-reconnaissance,
  osint-methodology, offensive-osint, threat-intelligence): starts passive
  and stays passive until scope allows contact. Enumerate subdomains, read
  DNS, fingerprint technology, correlate OSINT into an asset inventory with
  a source per entry. Shodan for internet-exposed services. Threat intel
  runs the intelligence cycle from requirements to dissemination; products
  use Diamond Model, Kill Chain and ATT&CK; keep attribution discipline;
  lead with a BLUF.
- **Vulnerability scanning** (02-vulnerability-scanner,
  vulnerability-scanning, dast-scanning, sast-scanning, sast-configuration,
  scanning-tools, bumblebee): audit dependencies, then read configuration
  against concrete checklists — Nginx four security headers, SSH hardened
  sshd_config directives, Docker pinned base image and dropped
  capabilities, Kubernetes CPU/memory limits plus restricted pod security
  posture. CVSS v3.1 scoring; prioritized report, not a flat list.
- **Network security** (08-network-security, network-101): read PCAPs with
  tshark — regular connection intervals indicate beaconing, long DNS names
  or high-volume DNS to one domain indicate tunnelling, lateral movement
  shows up in SMB.
- **Web security** (09-web-security, top-web-vulnerabilities, xss-html-
  injection, file-path-traversal): OWASP Top 10; injection with Linux and
  Windows separators; blind timing and DNS callback detection; SSTI probes
  for Pug, Jinja2 and Twig; API checks include introspection left enabled,
  batch abuse, circular query denial of service.
- **Cloud security** (10-cloud-security, cloud-penetration-testing,
  saas-security-posture, cloudflare-security-audit): provider audit
  commands — IAM users without MFA, overly permissive policies, public
  buckets, wide-open security groups, CloudTrail state, root account; Azure
  RBAC, storage public access, NSG rules, Key Vault policy.
- **Crypto/TLS** (13-crypto-analysis, ssl-tls-management, mtls-
  configuration, sops-encryption): audit TLS with openssl, sslyze,
  testssl; check cipher suites, DH parameter size, HSTS, OCSP stapling;
  flag hardcoded keys, `verify=False`, nonce reuse in code.
- **Specialized surfaces** (thick-client, smtp-penetration-testing,
  ssh-penetration-testing, firmware-pentest, hardware-security, radio-sdr,
  pentest-commands, pentest-tools, ffuf-claude-skill, ffuf-web-fuzzing,
  burpsuite-project-parser, src-hunter, find-bugs): thick-client testing;
  SMTP/SSH protocol testing; firmware/IoT chains; embedded interface
  security; RF/SDR research (lab-only); fuzzing with ffuf; Burp project
  parsing; source-material availability declared when absent.

**Offensive operations and emulation:**
- **Exploit development** (03-exploit-development, patch-diff-exploit,
  pwn-chain, metasploit-framework, attack-chain): authorization
  verification before any PoC; research the CVE; determine prerequisites
  (authentication, network position, version); build the PoC in Python,
  Bash or PowerShell; document the mitigation class. Modern hardware CFI
  (Intel CET, ARM PAC/BTI) breaks naive ROP and JOP — name the mitigation
  and the bypass class rather than assuming one.
- **Red team ops** (14-red-team-ops, red-team-tactics, red-team-tools,
  redteam-mindset, attack-tree-construction): plan the engagement first —
  objectives, threat profile, kill-chain phases, ROE, deconfliction
  contacts, emergency abort procedure. Team server never exposed to the
  internet; reached over VPN. Redirectors pass only C2 traffic and send
  everything else to a legitimate domain. Attack trees structure the
  threat paths.
- **Purple team** (22-purple-team): pick an engagement model; plan
  threat-informed emulation with ATT&CK, CTID, Atomic Red Team or CALDERA;
  run detect → tune → validate; measure coverage with DeTT&CT or ATT&CK
  Navigator. The validator scores supplied outcomes and does not execute
  rules or techniques.
- **Platform attacks** (enterprise-vpn-attack, m365-entra-attack,
  okta-attack, vmware-vcenter-attack, apk-redteam-pipeline,
  ios-redteam-pipeline): vendor identification/tenant discovery first;
  stage 0 inventories all org-owned apps; all carry the mandatory
  confirmation gate.

**Malware, forensics and response:**
- **Reverse engineering** (04-reverse-engineering, reverse-engineer,
  reverse-engineer-anything, ghidra-reverse, radare2, js-reverse,
  macos-reverse, apk-reverse, dsl-vm-reverse, protocol-reverse,
  protocol-reverse-engineering, binary-analysis-patterns,
  ax-extract-workflow): triage with `file`, strings, entropy, checksec;
  read assembly; spot crypto constants; extract firmware with binwalk;
  reverse protocols; common RE scripting environments; external tool
  prerequisites and supporting-material availability declared when absent.
- **Malware analysis** (05-malware-analysis, malware-analysis,
  malware-analyst): static analysis and a VirusTotal hash lookup; generate
  YARA rules, test them against benign files, then dynamic analysis in a
  dedicated VM. ssdeep similarity above 70 percent suggests the same
  family. Never use the main machine.
- **Threat hunting** (06-threat-hunting, threat-hunting): extract and
  normalize IOCs; map to ATT&CK; write hunt hypotheses; emit Splunk SPL,
  Sentinel KQL, Elastic EQL and Sigma. Generated queries need backend
  testing before production.
- **Incident response** (07-incident-response, incident-response,
  incident-response-smart-fix, incident-runbook-templates, digital-
  forensics, memory-forensics): follow PICERL with target times per phase.
  Capture memory first, then disk, then logs, keeping a chain-of-custody
  form for every item. The report names the breach notification duty that
  applies: GDPR 72 hours, HIPAA 60 days, card-brand notice for PCI.
- **Log analysis** (12-log-analysis): parse auth logs for failed then
  successful logins, sudo use, cron, new users; detect anomalies across
  volume, time, entity and sequence.

**Defensive engineering:**
- **Blue team** (15-blue-team-defense, linux-hardening, windows-hardening,
  kubernetes-hardening, container-security-hardening, firewall-config,
  waf-setup, zero-trust, cis-benchmarks): harden Linux SSH and sysctl,
  Windows service accounts, detection content, with baseline monitoring
  and patch management. Detection examples are behavioural — a web server
  that never spawns cmd.exe; alert on log clearing.
- **AI/LLM security** (16-ai-llm-security, model-supply-chain-security,
  neon-ai-gateway): test against the OWASP LLM Top 10 2025 — direct and
  indirect prompt injection, jailbreaks, RAG poisoning, agent and MCP tool
  abuse, model supply chain risk. Hard output rule: never pass raw model
  output into `eval`, SQL, a shell, or `innerHTML`; encode or parameterize
  at the sink.
- **Mobile security** (17-mobile-security, mobile-security-coder):
  inspect APKs and IPAs; verify MASVS storage, network, platform and
  resilience controls; instrument at runtime.
- **OT/ICS** (18-ot-ics-security): read the Purdue model and zone/conduit
  design before touching a device; prefer passive protocol capture over
  active queries; name the physical consequence of a crashed PLC. Never
  send active commands to production equipment.
- **Supply chain** (20-supply-chain-security, supply-chain-security,
  supply-chain-attack-recon, client-secret-exposure-audit,
  gha-security-review, openclaw-security-hardening,
  openclaw-deployment-hardening, sharp-edges, variant-analysis): generate
  and read an SBOM; check dependency confusion and typosquatting; look for
  malicious package indicators; harden CI/CD including GitHub Actions
  pinning and least-privilege tokens; provenance with SLSA and Sigstore
  signing; read-only supply-chain exposure review.
- **Platform hardening** (saas-security-posture, launch-check,
  marketplace-rbac-audit, zeroize-audit, agy-auto, laravel-security-audit,
  solidity-security, web3-audit, meme-coin-audit): startup SaaS posture;
  pre-launch checks; marketplace RBAC; Solidity and token audits with
  pre-dive kill signals (web3 hub carries the depth).

**Governance and intelligence:**
- **CSOC automation** (11-csoc-automation, alerting-oncall, on-call-
  handoff-patterns): triage alerts; write SOAR-compatible playbooks;
  define escalation paths with notification templates; produce shift
  handover reports and SOC KPIs. AI-assisted triage may summarize,
  cluster, enrich and draft a disposition, but containment waits on a
  human gate.
- **GRC** (19-grc-compliance, vendor-management, disaster-recovery):
  score risk; map controls across NIST CSF 2.0, ISO 27001:2022, SOC 2 and
  CIS Controls v8; run gap analysis with a remediation roadmap naming
  owner, effort and target date; the evidence index maps each control to
  the required artifact, location, owner and cadence. Vendor risk tiering;
  RTO/RPO planning. Analytical and document-based — needs no live target.
- **Threat modeling** (threat-modeling, threat-modeling-expert, stride-
  analysis-patterns, threat-mitigation-mapping, attack-tree-construction):
  STRIDE per element; mitigation mapping; capabilities stated.
- **Ops** (asset-inventory, access-matrix, audit-log, audit-logging,
  email-security, privacy-mask, load-balancing, reverse-proxy,
  linkerd-patterns, projection-patterns): asset categories and schema;
  access matrices; audit logging; phishing analysis; WAF/reverse-proxy
  patterns.

## 6. Compliance (27 skills)

**Compliance is not legal advice.** The compliance skills map a framework
to controls and evidence; they do not determine the legal obligation, the
regulator's interpretation, or the penalty. A qualified owner confirms
applicability and evidence sufficiency. Never state that a system is
compliant when the evidence or the scope is missing.

- **compliance-program**: the routing hub — scope the program, pick the
  frameworks, assign owners, build the evidence calendar.
- **GDPR** (gdpr-compliance, gdpr-data-handling, data-privacy-controls,
  privacy-by-design): key principles and legal bases; data handling
  procedures; privacy by design controls; records of processing; DSAR
  handling; breach notification at 72 hours.
- **SOC 2** (soc2-compliance): trust services criteria, control evidence,
  readiness assessment.
- **ISO 27001** (iso27001-compliance): ISMS scope, Statement of
  Applicability, risk assessment, internal audit, management review.
- **PCI DSS** (pci-dss-compliance, pci-compliance): cardholder data
  environment scoping, the 12 requirements, evidence review for payment
  data.
- **HIPAA**: safeguards mapping (from the security pack's compliance
  readiness set).
- **FedRAMP** (fedramp-compliance): control baselines, boundary definition,
  continuous monitoring.
- **Sector** (fsi-compliance-checker, customs-trade-compliance, fda-food-
  safety-auditor, check-identity-pack, screen-adverse-media,
  legal-compliance-vault, wgm): financial services checks; customs and
  trade; FDA food safety audits; identity verification packs; adverse
  media screening; legal document vaults.
- **Program operations** (access-review, policy-acknowledgement,
  policy-library, audit-preparation, audit-log, audit-logging,
  data-export-engine, source-document-filing, daily, akf-trust-metadata):
  access review process; policy libraries and acknowledgement tracking;
  audit preparation with evidence collection; data export with privacy
  controls.

## 7. Output contract

- Name the skill, the target system, and the authorization basis in the
  first line of reasoning and in the todo list.
- Lead each finding with severity, then the evidence, then the impact,
  then the fix.
- Keep control ids, framework names, rule ids, CVE ids, CVSS vectors,
  ATT&CK technique ids, file paths, hashes and error strings verbatim.
- State the exact evidence behind a control, with the system, the date,
  and the command or document. State what was tested, what was only
  reviewed, and what stayed unverified.
- Keep open work open: an unverified control, an untriaged match and a
  missing template are reported, never rounded up.
- Never print a secret, credential, live cookie, personal data or an
  internal host; redact and name the rule.
- Red team action block: `phase=<...> tactic=<tactic> target=<...>
  technique=<Txxxx[.xxx]> deconf=<code> status=<ok|blocked|detected|killed>
  action=<what was done> result=<what was observed> evidence=<artifact|hash>
  next=<tactic|phase|report|stop>`. One block per state-changing action;
  log to the deconfliction log before the next.
- Bug hunt line: `target= scope= class= status=confirmed|killed|blocked
  request=<method> <path> evidence=<artifact> impact=<what attacker gains>
  chain=<A->B->C|none> gate=<pass|fail:Qn>
  severity=<critical|high|medium|low|info> next=<class|report|stop>`.
- Review verdict block: `verdict: BLOCKED | CHANGES | PASS | UNVERIFIED;
  target; controls_checked; must_fail; should_fail; unverified` then one
  row per finding with control, level, status, evidence, smallest fix.

## 8. Failure handling

| Situation | Response |
| --- | --- |
| No written scope for an offensive action | Stop. Require target, scope, and the confirmation gate. |
| No ownership proof for an asset | Quarantine. Do not test. |
| Active threat actor present / unintended data destruction | Stop. Notify per ROE. Preserve evidence. |
| Scope or window expired | Stop. No resumption without new authorization. |
| A control has no evidence | Mark it unverified. A document is not proof of configuration. |
| A compliance claim exceeds the evidence | State the gap; a qualified owner decides applicability. |
| A scanner match is called exploitable | Triage reachability and version first; label it a candidate until then. |
| A CI action is unpinned | Select a maintained action, review it, pin the full commit SHA. |
| A secret would reach untrusted PR code | Remove it from that workflow and scope the token. |
| A remediation has no rollback | Capture the configuration and an approved rollback before the change. |
| A live cookie or token would be collected | Use a canary instead. Never collect a real credential. |
| Real user data encountered | Stop extraction. Redact. Report the missing check with minimum proof. |
| All 401/403/404 after 5 minutes, or stuck 1 hour | Move to another surface; switch context and return later. |
| WAF, captcha, lockout | Note the control. Do not bypass out of scope. |
| Cannot reproduce from a fresh session | Kill or downgrade. No report. |
| Possible duplicate | Run the dedup gate: disclosed reports, issues, changelog. |
| Beacon lost / EDR alerts on tooling | Use the fallback channel; change tooling or technique. Do not brute-force the sensor. Detection observed is a debrief finding, not a failure. |
| A required script, example or resource file is missing | Fail closed. Name the missing path. |
| A script prints sample output | Label it simulated. Never present it as live evidence. |
| A framework version is unknown | Name the version you used, or say you did not verify it. |
| A finding would need live OT, malware or exploit execution | State the safety rule and stop at the safe boundary. |
| Two controls conflict | Apply the stricter; note both. |
| Can't inspect runtime | Mark `unverified`; state the missing evidence. |
| The evidence contradicts the requested conclusion | Show the evidence and stop. |

## Provenance

Merged from the cyber-security class (153 catalog skills), the
compliance-audit class (27 catalog skills), and five curated packs:
security (12 sources, 5 groups), red-team (77 tactics, 9 groups),
bug-hunting (141 sources → 57 classes + 26 playbooks), prodsec (145
controls, 4 categories), cyber-masriyan (22 skills, 5 groups). Every
source skill's procedure, rule and policy is represented above; duplicates
collapsed to one canonical statement; authorization gates, kill lists,
evidence contracts and fail-closed rules preserved. No external file is
required to use this skill.
