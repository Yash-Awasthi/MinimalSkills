# compliance

Load when mapping controls, preparing audit evidence, or answering a framework gap.

## evidence rule

A control is not in place because a document says so. Record the configuration, command output, screenshot or policy section that proves it, with a date and a system name.

| claim | proof |
| --- | --- |
| encryption at rest | `aws s3api get-bucket-encryption` output, dated |
| access review quarterly | review tickets for the last 4 quarters |
| logging enabled | trail status plus one event from last week |
| patching under 30 days | scanner export with versions |
| mfa enforced | idp policy plus a test login |
| backups restorable | restore log from the last drill, with the row count |
| change reviewed | one merged PR with an approval and a linked ticket |
| offboarding within 24h | the last three leavers with their revocation timestamps |

Freshness per evidence class, because an auditor rejects stale proof:

```
config export      30 days
screenshot         90 days, with the url bar and a date visible
access review      the most recent completed cycle, no gap between cycles
pen test           annual, plus a remediation letter for open findings
restore drill      annual, or per the policy you wrote
training record    annual per person, including joiners mid-year
```

## mapping

| framework | unit | typical evidence |
| --- | --- | --- |
| SOC 2 | trust criteria + control | policy, config export, ticket |
| ISO 27001 | annex a control | statement of applicability, audit log |
| PCI DSS | requirement | scan report, segmentation test |
| HIPAA | safeguard | risk analysis, access log |
| GDPR | article | record of processing, dpa |

One control can satisfy several frameworks. Map once, reference many times.

Anchor points worth knowing by id, because auditors ask by id:

- SOC 2 common criteria run CC1 (control environment) through CC9 (risk mitigation); CC6 covers logical access, CC7 operations and monitoring, CC8 change management. Security is the only mandatory category; availability, processing integrity, confidentiality and privacy are added by scope.
- ISO 27001:2022 Annex A has 93 controls in four themes: organizational (5), people (6), physical (7), technological (8). A.8.16 is monitoring, A.5.15 access control, A.8.8 technical vulnerability management.
- PCI DSS v4.0 has 12 requirements; 3 protects stored account data, 4 protects data in transit, 10 logs and monitors, 11 tests security regularly. Segmentation evidence is a test, not a diagram.
- HIPAA Security Rule splits into administrative, physical and technical safeguards plus the risk analysis, which is the item most often missing.
- GDPR: Art 30 records of processing, Art 32 security of processing, Art 33 breach notification within 72 hours, Art 35 DPIA for high-risk processing, Art 28 processor contracts.

## gaps

```
control:  A.8.16 monitoring activities
status:   partial
gap:      alerts route to an unmonitored mailbox
risk:     detection delay over 24h
action:   route to on-call, test with a synthetic event
owner:    platform
due:      2026-04-01
```

"In progress" without a target date is not a status: record partial with the gap named, or absent.

Status vocabulary, fixed so a report is comparable across quarters: `in place` (tested, evidence dated), `partial` (control exists with a named gap), `absent` (no control), `not applicable` (with the scope reason). Anything else is prose.

## audit prep

1. Freeze the scope: systems, period, framework version.
2. Build the evidence index before the auditor asks.
3. Sample: 3 items per control per quarter is typical.
4. Pre-read every artifact for a stale date, a wrong system name, a redaction miss.
5. Log every request and every artifact handed over.

The evidence index is one row per control: id, control text, owner, system, artifact path, date, sampling method. An auditor who has to ask where something lives turns a two-week audit into a two-month one.

Sample selection: random within the period, not the three easiest. Keep the population list and the seed so the sample is reproducible; an auditor may ask to re-draw it.

## breach clock

- Start the clock at awareness, not at confirmation. The 72 hours in GDPR Art 33 run from the moment you knew.
- Log the awareness timestamp in the incident channel as the first message.
- Decide notify or not against the risk to rights and freedoms, and record the reasoning even when the answer is no.
- A processor notifies the controller without undue delay; the controller owns the regulator filing.
- State-level breach notification laws use different clocks and thresholds; a us incident can need notification in 50 jurisdictions with different content.

## claims discipline

- No certification claim from a checklist.
- No "compliant" without a scope statement.
- A control tested on one account does not cover the organization.
- Vendor attestation is evidence about the vendor, not about your integration.
- A SOC 2 report covers a period and a system list; quoting it for a service outside that list is a misstatement.
- Marketing may say "SOC 2 Type II" only with the report period, and never "certified", which SOC 2 is not.
