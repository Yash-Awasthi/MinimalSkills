---
name: compliance-program
description: "One merged skill for compliance and audit work across GDPR, ISO 27001, SOC 2, PCI DSS, HIPAA, NIST, FedRAMP, FIPS, CMMC, ISO 42001, EU AI Act, ISO 13485/QMS, CAPA, FDA, vendor risk, access lifecycle and audit evidence. Terse."
license: MIT
---

# Compliance Program

> Merged from compliance-audit catalog. Tooling in `scripts/`.

## Routing

- Framework unclear -> selector; map overlap; mock audit; evidence pool.
- Access -> access lifecycle / matrix / review.
- Privacy -> GDPR / DPIA / privacy-by-design / data privacy controls.
- Security controls -> ISO 27001 / SOC 2 / NIST / PCI / FedRAMP / FIPS / HIPAA.
- AI -> EU AI Act / ISO 42001 / AIMS / trust metadata.
- Medical device -> ISO 13485 / QMS / CAPA / FDA / MDR.
- Vendor -> vendor scorer / SLA / risk tier.
- Identity/ad adverse media -> identity pack / adverse media screen.
- Audit trail -> audit log / logging / preparation / support.

## Core workflow

1. Select framework(s).
2. Build control matrix / overlap map.
3. Assess risk and gaps.
4. Gather evidence per control.
5. Run mock/internal audit.
6. Classify findings.
7. Remediate or CAPA.
8. Track closeout and next review.

## Frameworks

- GDPR/DSGVO: scan codebase, DPIA, data-subject-rights deadline, consent, data minimization, retention, lawful basis, access roles, encryption.
- ISO 27001: ISMS, risk assessment, Annex A control evidence, Statement of Applicability, nonconformities, Stage 1/2, surveillance audit.
- SOC 2: Trust Service Criteria, control matrix, evidence, gap analysis, Type I/II observation.
- PCI DSS v4.0.1: cardholder data environment, payment flows, control IDs, remediation; scoped assessment, not certification claim.
- HIPAA: PHI protections, BAA, security/privacy rules.
- NIST CSF 2.0 / 800-53 / SP 800-171: control mapping, gap analysis, POA&M.
- FedRAMP: NIST controls, continuous monitoring.
- FIPS 140-2/3: RHEL/OpenShift/Go crypto policy, validated modules.
- CMMC 2.0 L2: SPRS score, scope, POA&M closeout, C3PAO.
- EU AI Act 2024/1689: risk tier, Art. 43 conformity, Annex IV, obligations by role.
- ISO 42001: clauses 4-10 gap, AI risk register, Annex A, audit schedule.
- ISO 13485/QMS: audit program, findings, CAPA, management review, quality KPIs, cost of quality.
- FDA: 510(k)/De Novo/PMA, QMSR 820, HIPAA, cybersecurity; food safety FSMA/HACCP/PCQI.
- MDR 2017/745: Annex VIII classification, technical file gaps, clinical evaluation, PMS/PSUR, notified body.
- ISO 14971: hazard analysis, FMEA, fault trees, risk controls, benefit-risk, residual risk.
- SOX 404: control testing, sample selection, workpapers, deficiency classification.

## Registers

- Access matrix: role x module permission, scope, confidentiality, SME tier.
- Access review: periodic review, certification, governance.
- Access lifecycle: leavers lose access; orphaned/ownerless service accounts; auditor requests.
- Audit log: timestamp, user, module, record, action, field changed, old/new, reason.
- Audit preparation: document, period, request/receipt dates, preparer/reviewer, queries, adjustments.
- Data export log: source, purpose, format, requester/approver, dates, personal-data flag, status.
- Data privacy controls: category, lawful basis, retention, access roles, encryption, consent.
- Policy library: name, version, category, owner/approver, applies to, framework, acknowledgement, effective, next review.
- Policy acknowledgement: employee, policy/version, sent/due, acknowledged, overdue, reminder.
- Legal compliance vault: type, framework, owner/dept, effective/expiry, renewal, storage link, confidentiality, status.
- Identity pack: AFP 100-point / AUSTRAC safe-harbour check; report missing.
- Vendor register: scorecard, SLA/service credits, risk tier, tier-1 review.

## Tooling

- `framework_selector.py`, `cross_framework_mapper.py`, `audit_simulator.py`, `evidence_pool_generator.py`.
- `access_diff.py`, `access_review_campaign.py`, `control_evidence_mapper.py`.
- `gdpr_compliance_checker.py`, `dpia_generator.py`, `data_subject_rights_tracker.py`.
- `risk_assessment.py`, `compliance_checker.py`, `isms_audit_scheduler.py`.
- `aims_gap_analyzer.py`, `ai_risk_register_builder.py`, `aims_audit_scheduler.py`.
- `ai_system_risk_classifier.py`, `conformity_assessment_planner.py`, `ai_act_obligation_tracker.py`.
- `control_matrix_builder.py`, `evidence_tracker.py`, `gap_analyzer.py`.
- `sprs_score.py`, `scope_classifier.py`, `poam_closeout.py`.
- `capa_tracker.py`, `root_cause_analyzer.py`, `audit_schedule_optimizer.py`.
- `management_review_tracker.py`, `quality_effectiveness_monitor.py`.
- `regulatory_pathway_analyzer.py`, `regulatory_tracker.py`.
- `fmea_analyzer.py`, `risk_matrix_calculator.py`.
- `vendor_scorer.py`, `sla_compliance_tracker.py`, `vendor_risk_classifier.py`.
- `control_mapper.py`, `risk_register.py`.

## Guardrails

- Compliance evidence != certification claim.
- Missing evidence -> gap, not pass.
- Medical/legal -> professional review.
- AI Act -> role-specific obligations.
- Audit findings -> classify severity, remediate, close.
- Sensitive data -> minimize, redact, retain originals.
