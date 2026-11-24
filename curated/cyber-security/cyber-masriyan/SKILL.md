---
name: cyber-masriyan
description: >-
  22 security skills covering the full defensive and offensive lifecycle: recon and
  OSINT, vulnerability scanning, network, web, cloud, and crypto assessment, exploit
  development, red team operations, purple team emulation, reverse engineering,
  malware analysis, threat hunting, incident response, log and SIEM analysis, blue
  team hardening, AI and LLM security, mobile security, OT and ICS security, supply
  chain security, CSOC automation, GRC compliance, and threat intelligence. Use when a
  task matches any of those, or when the user names a cyber masriyan skill.
metadata:
  curated_from: 22
  skills: 22
  groups: 5
---

# cyber-masriyan

22 skills. 5 groups. One hub. Every source body is preserved verbatim in
`references/skills/<skill>.md`, and every non-SKILL.md file from a source pack sits at
the same relative path under `references/assets/<skill>/`. Load one body for the task.

`SOURCES.md` maps every source path to its canonical skill and group.
`references/INDEX.md` groups the links, `references/skills.tsv` carries every
description, and `references/GUIDE.md` holds the long-form group prose.

## Pack contract

**Authorization comes before technique.** Every active skill requires written
authorization for the named scope. No scope, no scanning, no payload, no live-fire
emulation. Passive analysis and document work can proceed without it. If
authorization cannot be confirmed, restrict the answer to planning, coverage
analysis, detection engineering, and tabletop work, and say so.

**Evidence contract on every finding.** Separate **observed**, **inferred**, and
**unverified**. Record the source or artifact reference, the SHA-256 when a file is
available, the collection time, the validation performed, the limitation, and the next
verification step. Extraction confidence is not maliciousness confidence. Unknown
maliciousness stays unknown.

**A script output is a candidate, not a conclusion.** The bundled scripts parse,
extract, score, and format. They do not prove compromise. State what each script did
and did not do, and never present simulated or sample output as live evidence.

**Read the body's execution order.** Several skills carry a hard sequence, such as
memory first in incident response, passive first in OT, or a tight failing loop in
diagnosis. The sequence is the method. Do not reorder it for speed.

**Safety boundaries are real.** Never execute suspicious files outside an isolated
VM with network isolation and snapshots. Never send active OT commands to production
equipment. Never log everything and grep. Never ship a TLS or crypto configuration
with `verify=False`, a hardcoded key, or a reused nonce.

**Reporting is the deliverable.** Each skill ends in a named report shape with an
executive summary, findings, evidence, and prioritized recommendations. Keep ids,
hashes, CVSS vectors, ATT&CK technique ids, and error strings verbatim.

**Frameworks keep their own words.** NIST SP 800-61 and 800-82, SANS PICERL, OWASP
Top 10 and LLM Top 10 2025, OWASP MASVS and MASTG, MITRE ATT&CK, IEC 62443, NIST CSF
2.0, ISO 27001:2022, SOC 2, CIS Controls v8, SLSA, and Sigstore. Name the framework and
version you used, and do not claim coverage you did not test.

**Write clean as you draft.** Short declarative sentences. No em dash. A colon may
introduce a list and may not connect two clauses. Sentence case headings. No chatbot
framing, no generic closer.

## Routing

| The user wants | Group |
| --- | --- |
| Recon, a vuln scan, or a network, web, cloud, or crypto assessment | Discovery and assessment |
| A PoC, a red team plan, or a purple team emulation cycle | Offensive operations and emulation |
| Binary, malware, threat hunt, incident, or log work | Malware, forensics, and response |
| Host, AI, mobile, OT, or supply chain hardening and testing | Defensive engineering |
| SOC triage, risk and control mapping, or threat intel production | Governance and intelligence |

## Full roster

### Discovery and assessment

| Skill | What it does |
| --- | --- |
| [`01-recon-osint`](references/skills/01-recon-osint.md) | Passive and active reconnaissance, subdomain enumeration, DNS analysis, technology fingerprinting, OSINT correlation, and a sourced asset report. Authorization required. |
| [`02-vulnerability-scanner`](references/skills/02-vulnerability-scanner.md) | Dependency auditing, config review for nginx, sshd, Docker, and Kubernetes, CVSS v3.1 scoring, NSE scanning, and a prioritized vulnerability report. |
| [`08-network-security`](references/skills/08-network-security.md) | PCAP analysis with tshark, beaconing and DNS tunnelling detection, Suricata rule writing, firewall audit, and anomaly findings. |
| [`09-web-security`](references/skills/09-web-security.md) | OWASP Top 10 testing, injection probes with blind timing and DNS callbacks, API abuse checks, auth testing, and a scoped web assessment report. |
| [`10-cloud-security`](references/skills/10-cloud-security.md) | AWS, Azure, and GCP audit commands, Docker and Kubernetes hardening, IaC scanning, and a cloud compliance posture report. |
| [`13-crypto-analysis`](references/skills/13-crypto-analysis.md) | TLS configuration audit with openssl, sslyze, and testssl, cipher and hash strength review, and code-level crypto weakness detection. |

### Offensive operations and emulation

| Skill | What it does |
| --- | --- |
| [`03-exploit-development`](references/skills/03-exploit-development.md) | CVE research, PoC development, payload generation for Python, Bash, and PowerShell, buffer overflow and web payload patterns, and mitigation notes. |
| [`14-red-team-ops`](references/skills/14-red-team-ops.md) | Engagement planning, rules of engagement, deconfliction, C2 architecture, Active Directory attack paths, OPSEC, and a professional report. |
| [`22-purple-team`](references/skills/22-purple-team.md) | Threat-informed emulation planning, the detect-tune-validate loop, DeTT&CT and Navigator coverage, safe execution, deconfliction, and MTTD reporting. |

### Malware, forensics, and response

| Skill | What it does |
| --- | --- |
| [`04-reverse-engineering`](references/skills/04-reverse-engineering.md) | Binary triage, strings, ELF and PE analysis, entropy and checksec, assembly reading, firmware extraction, and protocol reverse engineering. |
| [`05-malware-analysis`](references/skills/05-malware-analysis.md) | Static and dynamic malware analysis, YARA rule generation tested against benign files, ssdeep family matching, sandbox setup, and IOC output. |
| [`06-threat-hunting`](references/skills/06-threat-hunting.md) | IOC extraction, ATT&CK mapping, hunt hypotheses, Splunk, Sentinel, Elastic, and Sigma queries, and a labelled coverage limit note. |
| [`07-incident-response`](references/skills/07-incident-response.md) | NIST SP 800-61 and SANS PICERL playbooks, memory first evidence collection, chain of custody, timeline building, and breach notification duties. |
| [`12-log-analysis`](references/skills/12-log-analysis.md) | Auth log parsing, anomaly detection across volume, time, entity, and sequence, SIEM query libraries, and Sigma and correlation rules. |

### Defensive engineering

| Skill | What it does |
| --- | --- |
| [`15-blue-team-defense`](references/skills/15-blue-team-defense.md) | Linux and Windows hardening, detection engineering, baseline monitoring, patch management, and defense-in-depth posture work. |
| [`16-ai-llm-security`](references/skills/16-ai-llm-security.md) | OWASP LLM Top 10 2025 testing, prompt injection and jailbreak probes, RAG and agent tool-use review, model supply chain, and output guardrails. |
| [`17-mobile-security`](references/skills/17-mobile-security.md) | APK and IPA static analysis, MASVS storage, network, platform, and resilience verification, dynamic instrumentation, and mobile malware triage. |
| [`18-ot-ics-security`](references/skills/18-ot-ics-security.md) | Purdue segmentation review, passive-first Modbus, DNP3, S7, and EtherNet/IP analysis, ATT&CK for ICS, and IEC 62443 alignment. Safety first. |
| [`20-supply-chain-security`](references/skills/20-supply-chain-security.md) | SBOM generation, dependency confusion and typosquatting checks, malicious package indicators, CI/CD hardening, and SLSA and Sigstore provenance. |

### Governance and intelligence

| Skill | What it does |
| --- | --- |
| [`11-csoc-automation`](references/skills/11-csoc-automation.md) | Alert triage, SOAR-compatible playbooks, escalation paths and templates, shift handover reports, and SOC KPI tracking. |
| [`19-grc-compliance`](references/skills/19-grc-compliance.md) | Risk scoring and register, control mapping across NIST CSF 2.0, ISO 27001:2022, SOC 2, and CIS v8, gap analysis, evidence index, and policy drafting. |
| [`21-threat-intelligence`](references/skills/21-threat-intelligence.md) | The intelligence cycle, IOC normalisation and enrichment, Diamond, Kill Chain, and ATT&CK models, source scoring, actor tracking, and BLUF products. |

## Group notes

### Discovery and assessment

`01-recon-osint` starts passive and stays passive until scope allows contact. It
enumerates subdomains, reads DNS, fingerprints technology, and correlates OSINT into
an asset inventory with a source for each entry. Its scripts are `subdomain_enum.py`,
`dns_recon.py`, and `tech_fingerprint.py`, and `resources/common_subdomains.txt` is the
seed list.

`02-vulnerability-scanner` audits dependencies, then reads configuration against
concrete checklists. Nginx needs the four security headers, SSH needs the hardened
`sshd_config` directives, Docker needs a pinned base image and dropped capabilities,
and Kubernetes needs CPU and memory limits plus a restricted pod security posture.
CVSS v3.1 scoring uses `cvss_calculator.py`, and the report is prioritized rather than
a flat list.

`08-network-security` reads PCAPs with tshark. Regular connection intervals indicate
beaconing, long DNS names or high-volume DNS to one domain indicate tunnelling, and
lateral movement shows up in SMB. `09-web-security` covers the OWASP Top 10, injection
with Linux and Windows separators, blind timing and DNS callback detection, and SSTI
probes for Pug, Jinja2, and Twig. Its API checks include introspection left enabled,
batch abuse, and circular query denial of service.

`10-cloud-security` runs provider audit commands, including IAM users without MFA,
overly permissive policies, public buckets, wide-open security groups, CloudTrail
state, and the root account. Azure covers RBAC, storage public access, NSG rules, and
Key Vault policy. `13-crypto-analysis` audits TLS with openssl, sslyze, and testssl,
checks cipher suites, DH parameter size, HSTS, and OCSP stapling, and flags hardcoded
keys, `verify=False`, and nonce reuse in code.

### Offensive operations and emulation

`03-exploit-development` runs an authorization verification step before any PoC. It
researches the CVE, determines prerequisites such as authentication, network position,
and version, builds the PoC in Python, Bash, or PowerShell, and documents the
mitigation class. Modern hardware CFI such as Intel CET and ARM PAC/BTI breaks naive
ROP and JOP, so the write-up names the mitigation and the bypass class rather than
assuming one.

`14-red-team-ops` plans the engagement first, covering objectives, threat profile,
kill-chain phases, rules of engagement, deconfliction contacts, and an emergency abort
procedure. The team server is never exposed to the internet and is reached over VPN.
Redirectors pass only the C2 traffic and send everything else to a legitimate domain.

`22-purple-team` picks an engagement model, plans threat-informed emulation with
ATT&CK, CTID, Atomic Red Team, or CALDERA, then runs detect, tune, validate. Coverage
is measured with DeTT&CT or ATT&CK Navigator. `detection_validator.py` scores supplied
outcomes and does not execute rules or techniques. `--attack-version` sets Navigator
metadata only, so it does not validate technique ids against a release.

### Malware, forensics, and response

`04-reverse-engineering` triages with `file`, strings, entropy, and checksec, then
reads assembly, spots crypto constants, extracts firmware with binwalk, and reverses
protocols. `05-malware-analysis` does static analysis and a VirusTotal hash lookup,
generates YARA rules with `yara_generator.py`, tests them against benign files, then
runs dynamic analysis in a dedicated VM. An ssdeep similarity above 70 percent
suggests the same family. Never use the main machine.

`06-threat-hunting` extracts and normalizes IOCs, maps to ATT&CK, writes hunt
hypotheses, and emits Splunk SPL, Sentinel KQL, Elastic EQL, and Sigma. Its mapper is a
limited ATT&CK v14 subset, so resolve actor-to-technique links from a separate dataset
and supply ids with `--input`. Generated queries need backend testing before
production.

`07-incident-response` follows PICERL with target times per phase. Capture memory
first, then disk, then logs, keeping a chain of custody form for every item. The report
names the breach notification duty that applies, including GDPR at 72 hours, HIPAA at
60 days, and card brand notice for PCI. `12-log-analysis` parses auth logs for failed
then successful logins, sudo use, cron, and new users, and detects anomalies across
volume, time, entity, and sequence.

### Defensive engineering

`15-blue-team-defense` hardens Linux SSH and sysctl settings, Windows service
accounts, and detection content, with baseline monitoring and patch management. The
detection examples are behavioural, such as a web server that never spawns
`cmd.exe` and alerts on log clearing.

`16-ai-llm-security` tests against the OWASP LLM Top 10 2025. It covers direct and
indirect prompt injection, jailbreaks, RAG poisoning, agent and MCP tool abuse, and
model supply chain risk. The hard output rule is never to pass raw model output into
`eval`, SQL, a shell, or `innerHTML`. Encode or parameterize at the sink.

`17-mobile-security` inspects APKs and IPAs, verifies MASVS storage, network,
platform, and resilience controls, and instruments at runtime. `18-ot-ics-security`
reads the Purdue model and zone and conduit design before touching a device, prefers
passive protocol capture over active queries, and names the physical consequence of a
crashed PLC. Never send active commands to production equipment.

`20-supply-chain-security` generates and reads an SBOM, checks dependency confusion
and typosquatting, looks for malicious package indicators, and hardens CI/CD,
including GitHub Actions pinning and least-privilege tokens. Provenance uses SLSA and
Sigstore signing.

### Governance and intelligence

`11-csoc-automation` triages alerts, writes SOAR-compatible playbooks, defines
escalation paths with notification templates, and produces shift handover reports and
SOC KPIs. AI-assisted triage may summarize, cluster, enrich, and draft a disposition,
but containment waits on a human gate.

`19-grc-compliance` scores risk with `risk_register.py`, maps controls across NIST CSF
2.0, ISO 27001:2022, SOC 2, and CIS Controls v8 with `control_mapper.py`, and runs gap
analysis with a remediation roadmap naming owner, effort, and target date. Its evidence
index maps each control to the required artifact, location, owner, and cadence. This
skill is analytical and document based, so it needs no live target.

`21-threat-intelligence` runs the intelligence cycle from requirements to
dissemination. `cti_processor.py` separates `extraction_confidence`, which describes
recognition only, from `maliciousness_confidence`. Products use the Diamond model,
Kill Chain, and ATT&CK, score sources, track actors and campaigns, keep attribution
discipline, and lead with a BLUF.

## Output contract

- Name the skill, the target, and the authorization state in the first line of your
  reasoning and in the todolist.
- Lead each finding with severity, then the evidence, then the impact, then the fix.
- Keep hashes, CVSS vectors, CVE ids, ATT&CK technique ids, and error strings verbatim.
- Label every statement observed, inferred, or unverified. Never promote an extraction
  score into a compromise claim.
- State what was out of scope, skipped, or only sampled. A bounded check is not full
  coverage.
- Write through `unslop`. Short declarative sentences, sentence case headings, no em
  dash, no colon connecting two clauses, no chatbot framing.
- Redact credentials, tokens, personal data, and customer identifiers from any report
  or public output.

## Failure handling

| Situation | Response |
| --- | --- |
| No written authorization for the scope | Stop. Offer planning, coverage analysis, or tabletop work only. |
| A required script, example, or resource file is missing | Fail closed. Name the missing path. |
| A scan or query returns nothing | Report the negative with the scope and method. Never call it clean. |
| A tool result is partial or truncated | Report the bounded window. Never present it as complete. |
| A script prints sample output | Label it simulated. Never present it as live evidence. |
| A framework version is unknown | Name the version you used, or say you did not verify it. |
| A finding would need live OT, malware, or exploit execution | State the safety rule and stop at the safe boundary. |
| The evidence contradicts the requested conclusion | Show the evidence and stop. |

## Provenance

22 `cyber-masriyan-*` source directories became 22 canonical skills in 5 groups. Each
source had one body, so no merge or variant resolution was needed. Every body is
verbatim at `references/skills/<skill>.md` with its original frontmatter removed, and
every other file from a source pack is copied under `references/assets/<skill>/` at
the same relative path. 57 asset files totaling 471,443 bytes were copied, including
the per-skill `scripts/` and `examples/example_usage.md`.

Two companions stay outside this pack. `curated/cyber-security/prodsec/`,
`curated/cyber-security/bug-hunting/`, and `curated/cyber-security/red-team/` cover
adjacent work from other authors. `cyber-y2k` is a visual design skill nested inside a
different catalog pack and is not part of this curriculum.

Upstream author `masriyan`. Original catalog paths are preserved in `SOURCES.md` and
under `_archive/cyber-masriyan/catalog/`.
