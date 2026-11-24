# security guide

The long-form group prose and the full roster. `SKILL.md` is the loadable hub, and
`references/skills/<skill>.md` is the verbatim body to follow for one task.

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
