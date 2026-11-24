---
name: security
description: >-
  12 security skills. Covers security-first web hardening, an architecture control checklist,
  a MUST and SHOULD policy builder, authorized-use payload and audit workflows, a broad
  DevSecOps auditor, GDPR, HIPAA, SOC2, and PCI-DSS readiness, security requirement
  extraction from a threat model, security pipeline and supply-chain automation, dependency
  and SBOM scanning, SAST, and a coordinated hardening program. Use when a task hardens,
  audits, assesses, automates, or writes policy for a system, or when the user names a
  security skill.
metadata:
  curated_from: 12
  skills: 12
  groups: 5
---

# security

12 skills. 5 groups. One hub. Every source body is preserved verbatim in
`references/skills/<skill>.md`, and every non-SKILL.md file from a source pack sits at
the same relative path under `references/assets/<skill>/`. Load one body for the task.

`SOURCES.md` maps every source path to its canonical skill and group.
`references/INDEX.md` groups the links, `references/skills.tsv` carries every
description, and `references/GUIDE.md` holds the long-form group prose.

## Pack contract

**Authorized use only for offensive work.** `arsenal` and `audit` carry a mandatory
confirmation gate. Ask for the exact target URL, IP, account, or resource, the written
scope, and the test window before any probe. Never point a payload or an exploit at a
system you do not own or are not engaged to test, and never use a finding to cause harm.
`auditor` and `scanning-security-hardening` also forbid intrusive production testing
without written approval.

**Defense is not offense.** `and-hardening`, `checklist`, `bluebook-builder`,
`compliance-compliance-check`, `requirement-extraction`, `automation`, and the scanning
skills are defensive or administrative. They still need an authorized scope, but they do
not carry the offensive gate. Keep the two roles separate in the report.

**Evidence, not a claim.** A control is not in place because a document says so. Record
the configuration, the command output, the screenshot, or the policy section that proves
it, with the date and the system. An unverified control is reported as unverified. A
checklist is not a certification, and a policy is not an audit.

**Compliance is not legal advice.** The compliance skill maps a framework to controls and
evidence. It does not determine the legal obligation, the regulator's interpretation, or
the penalty. A qualified owner confirms the applicability and the evidence sufficiency.
Never state that a system is compliant when the evidence or the scope is missing.

**A scanner result is a candidate.** A SAST match, a dependency advisory, and a secret
pattern need triage for reachability, exploitability, and the actual version. Confirm the
finding before reporting a vulnerability, and state the rule, the file, and the version.
A false positive is not a defect, and an unpatched dependency is not automatically
exploitable.

**Pin every automation action and scope every credential.** A CI action reference is a
supply-chain dependency, so select a maintained action, review it, and pin the full commit
SHA. Grant `contents: read` unless a job truly needs more, never expose a secret to
untrusted pull-request code, and install a scanner at a reviewed version before its step.
A workflow that runs on a fork is attacker-controlled.

**A remediation captures state first.** Read-only inventory before any active step. Before
a mutation, capture the existing configuration and an approved rollback plan. Automated
remediation that changes a live control is a production change with the same approval,
canary, and rollback requirements as a manual one.

**A missing support file fails closed.** `bluebook-builder` names
`<support-root>/references/bluebook_template.md`, which was absent before the move.
Resolve it from the declared upstream or ask for the original material, and do not run a
dependent step or claim the procedure until it exists. Never fabricate the template.

**A policy is short and enforceable.** Use MUST, SHOULD, and CAN. State the assumptions,
the scope, and the gates. Fail closed when a required capability is unavailable. Never put
a secret, a token, or an internal credential in the document.

**Write clean as you draft.** Short declarative sentences. No em dash. A colon may
introduce a list and may not connect two clauses. Sentence case headings. No chatbot
framing, no generic closer.

## Routing

| The user wants | Group |
| --- | --- |
| A feature hardened, an architecture reviewed, or a security policy written | Defensive build |
| An authorized payload test, audit, or DevSecOps assessment | Authorized testing |
| A framework readiness check or requirements from a threat model | Compliance and requirements |
| A security pipeline or a dependency and SBOM review | Automation and supply chain |
| A SAST pass or a multi-layer hardening program | Code and infrastructure scanning |

## Full roster

### Defensive build

| Skill | What it does |
| --- | --- |
| [`and-hardening`](references/skills/and-hardening.md) | Security-first web development across input, auth, storage, and integrations, with the boundary tiers, the never-do list, and the OWASP patterns. |
| [`bluebook-builder`](references/skills/bluebook-builder.md) | Builds a short enforceable security policy with MUST, SHOULD, and CAN language, explicit assumptions, scope, and security gates. |
| [`checklist`](references/skills/checklist.md) | Reviews a scoped architecture against evidence-based network, identity, data, secrets, dependency, and incident-response controls. |

### Authorized testing

| Skill | What it does |
| --- | --- |
| [`arsenal`](references/skills/arsenal.md) | Authorized-use payload, bypass, and wordlist reference for XSS and SSRF testing, with the always-rejected list and the chain table. |
| [`audit`](references/skills/audit.md) | An authorized security audit workflow across recon, scanning, web testing, API testing, and hardening, with a mandatory confirmation gate. |
| [`auditor`](references/skills/auditor.md) | A broad DevSecOps auditor role across SDLC controls, auth, cloud, compliance, monitoring, and incident response, with an intrusive-test limit. |

### Compliance and requirements

| Skill | What it does |
| --- | --- |
| [`compliance-compliance-check`](references/skills/compliance-compliance-check.md) | Assesses GDPR, HIPAA, SOC2, and PCI-DSS readiness, builds the control and evidence map, and gives implementation guidance. |
| [`requirement-extraction`](references/skills/requirement-extraction.md) | Turns a threat model and the business context into actionable security requirements, user stories, and test cases with acceptance criteria. |

### Automation and supply chain

| Skill | What it does |
| --- | --- |
| [`automation`](references/skills/automation.md) | Builds a security pipeline, automated remediation, SOAR, and compliance as code, with pinned actions and scoped credentials. |
| [`scanning-security-dependencies`](references/skills/scanning-security-dependencies.md) | Scans dependencies across ecosystems for vulnerabilities and license risk, generates an SBOM, and proposes a bounded remediation. |

### Code and infrastructure scanning

| Skill | What it does |
| --- | --- |
| [`scanning-security-hardening`](references/skills/scanning-security-hardening.md) | Coordinates a defense-in-depth program across assessment, remediation, controls, and validation on application, infrastructure, and mobile layers. |
| [`scanning-security-sast`](references/skills/scanning-security-sast.md) | Runs a static application security review across languages and frameworks, with the detailed guide carrying the full procedure. |

## Group notes

### Defensive build

`and-hardening` is the coding standard. A threat model first, then three boundary tiers,
an always-do list, a never-do list, and the OWASP patterns for injection, broken auth,
XSS, broken access control, misconfiguration, sensitive data, and SSRF. Input validation,
schema checks at the boundary, and file upload safety. Every external input is hostile,
every secret is protected, and every authorization check is mandatory. Never trust client
validation, never commit a secret, never log sensitive data, never store an auth token in
client-accessible storage, and never expose a stack trace. The checklist reference is
bundled.

`checklist` reviews an architecture. Network, authentication and authorization, API, data,
secrets, supply chain, incident response, and applicable compliance. It asks for evidence
per control, and it says it is not certification, legal advice, or permission to apply a
control. A WAF, an ORM, a token, or an encrypted database does not prove the control works.

`bluebook-builder` writes the policy. Gather the inputs, draft with MUST, SHOULD, and CAN,
enforce the guardrails, then run the quality checks. The result is one coherent document
with assumptions, scope, and gates. It fails closed when a capability is missing, and it
contains no secret. The named template was absent before the move, so resolve it or skip
that step.

### Authorized testing

`arsenal` is the payload and bypass reference. XSS probes with a non-sensitive proof of
execution, CSP bypass, DOM sources and sinks, SSRF payloads, cloud metadata endpoints,
internal service fingerprinting, IP bypass forms, DNS rebinding, and a redirect chain.
It carries an always-rejected list and a conditionally-valid-with-chain table in its
details reference. Use a unique canary in an owned test session. Never collect a live
cookie or token. Script execution alone does not prove account takeover, and an HttpOnly
cookie is not readable with `document.cookie`.

`audit` is the workflow bundle. Reconnaissance, vulnerability scanning, web application
testing, API testing, and hardening, with prompts per phase. The confirmation gate is
mandatory before any probing, exploitation, or credential-access command. A phase that
needs a tool the environment lacks is reported, not simulated.

`auditor` is the broad role skill. DevSecOps automation, modern auth, OWASP and
vulnerability management, application security testing, cloud security, compliance,
secure coding, network and infrastructure, monitoring and incident response, emerging
technology, and validation. It forbids intrusive production tests without written
approval. A capability list is a map, not a claim that every tool is installed.

### Compliance and requirements

`compliance-compliance-check` assesses readiness. GDPR, HIPAA, SOC2, and PCI-DSS, a
control checklist, audit evidence, implementation guidance, and the required records. It
stops when scope approval or the evidence is unavailable. The playbook is bundled, and it
is conceptual scaffolding rather than a certified control set. Legal applicability belongs
to a qualified owner, not to this skill.

`requirement-extraction` turns a threat model into requirements. Security user stories and
test cases with acceptance criteria, traced from the threat and the business context. A
requirement without a test is a wish, and a test without a threat trace is ungrounded. The
playbook is bundled.

### Automation and supply chain

`automation` builds the pipeline. A security workflow, automated remediation, SOAR, and
compliance as code. The action references are historical examples, so select a maintained
action, review it, and pin the full commit SHA. Grant the least permission, never expose a
secret to untrusted pull-request code, and install a scanner at a reviewed version. A
custom Checkov check must target the real Terraform resource schema in the deployed
provider version. A remediation captures the configuration and a rollback first.

`scanning-security-dependencies` covers the dependency layer. Vulnerability analysis
across ecosystems, license risk, SBOM generation, and remediation. An advisory needs the
installed version, the reachable path, and the fixed version. A license flag needs the
distribution model. The playbook is bundled.

### Code and infrastructure scanning

`scanning-security-sast` is the static review. Languages, frameworks, and security
patterns, with the detailed guide carrying the full procedure. A match is a candidate, so
confirm reachability and the framework's own escaping before a report. The detailed guide
is bundled.

`scanning-security-hardening` coordinates the program. Assessment, vulnerability
remediation, controls, then validation and compliance across application, backend,
frontend, mobile, auth, infrastructure, and secrets. It follows shift-left and
defense-in-depth. Each phase builds on the last, so a skipped assessment leaves the later
controls ungrounded. An intrusive validation needs written approval.
## Output contract

- Name the skill, the target system, and the authorization basis in the first line of your reasoning and in the todolist.
- Report the artifact. A hardening change, a control review, a policy, a finding, a requirement, a pipeline, an SBOM, or a scan result.
- Keep control ids, framework names, rule ids, CVE ids, file paths, and evidence locations verbatim.
- State the exact evidence behind a control, with the system, the date, and the command or document.
- State what was tested, what was only reviewed, and what stayed unverified.
- Keep open work open. An unverified control, an untriaged match, and a missing template are reported, never rounded up.
- Never print a secret, a credential, a live cookie, personal data, or an internal host. Redact it and name the rule.
- Write through `unslop`. Short declarative sentences, sentence case headings, no em dash, no colon connecting two clauses, no chatbot framing.

## Failure handling

| Situation | Response |
| --- | --- |
| An offensive action has no written scope | Stop. Require the target, the scope, and the confirmation gate. |
| A control has no evidence | Mark it unverified. A document is not proof of configuration. |
| A compliance claim exceeds the evidence | State the gap and let a qualified owner decide applicability. |
| A scanner match is called exploitable | Triage reachability and version first. Label it a candidate until then. |
| A CI action is unpinned | Select a maintained action, review it, and pin the full commit SHA. |
| A secret would reach untrusted PR code | Remove it from that workflow and scope the token. |
| A remediation has no rollback | Capture the configuration and an approved rollback before the change. |
| A live cookie or token would be collected | Use a canary instead. Never collect a real credential. |
| A missing template is invented | Resolve it from the upstream or skip the step. |
| The evidence contradicts the requested claim | Show the evidence and stop. |

## Provenance

12 `sickn33-security-*` source directories became 12 canonical skills in 5 groups. Each
source had one body, so no merge or variant resolution was needed. Every body is verbatim
at `references/skills/<skill>.md` with its original frontmatter removed, and every other
file from a source pack is copied under `references/assets/<skill>/` at the same relative
path. 6 asset files totaling 104,345 bytes were copied: the hardening checklist, the
arsenal details reference, the three compliance and requirement playbooks, the dependency
playbook, and the SAST detailed guide.

The canonical name drops the `sickn33-security-` prefix, so
`sickn33-security-and-hardening` becomes `and-hardening` and
`sickn33-security-scanning-security-sast` becomes `scanning-security-sast`.

`arsenal` and `audit` are authorized-use only and carry the mandatory confirmation gate.
`auditor` and `scanning-security-hardening` forbid intrusive production testing without
written approval. `and-hardening` is the defensive counterpart and carries no such gate.
The pack keeps each role separate.

`bluebook-builder` names `<support-root>/references/bluebook_template.md`, which was absent
before the move. The body says it is an external prerequisite, and the pack keeps that
statement rather than fabricating the template. The compliance and dependency playbooks
are described as conceptual scaffolding rather than certified control sets.

Upstream collection `sickn33`. Original catalog paths are preserved in `SOURCES.md` and
under `_archive/security/catalog/`.
