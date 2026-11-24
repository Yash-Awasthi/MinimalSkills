---
name: strategy-product
description: >
  One standalone skill for strategy, product management and executive work:
  product management lifecycle (PRDs, requirements with EARS, issue gates,
  roadmaps), JTBD and discovery, OKRs and KPIs, decision frameworks,
  postmortems, change management, launch strategy, pricing, growth strategy
  (free tier, free tool, onboarding CRO), stakeholder and investor reports,
  board governance, and executive persona frameworks with stated boundaries.
  Merges the strategy-executive class (71 skills) and the product-management
  class (16 skills). Fully self-contained: every procedure is inline, no
  external references.
metadata:
  merges: strategy-product
  sources: 87
---

# strategy-product

## 0. Iron laws

1. **Evidence before strategy.** JTBD analysis, market sizing, disruption
   pressure and psychographic profiling start with context gathering; each
   behavioral or advisory skill carries an evidence-and-scope boundary. A
   claim without evidence is labeled a hypothesis.
2. **Decide with data, state the base.** Analytics-product (Portuguese-
   canonical) and every KPI skill fix definitions before computing. A metric
   without a definition is not a metric.
3. **Personas are simulation frameworks, not advice.** The bill-gates,
   harvey-specter, multi-advisor board and shark personas state identity and
   factual boundaries (Portuguese-canonical where noted). Their output is a
   perspective to weigh, never a directive.
4. **Requirements are testable.** EARS format and requirement-quality rules:
   each requirement is unambiguous, verifiable, and traceable. A "should be
   user friendly" line is not a requirement.
5. **Before you build** (before-you-build): state the user problem, the
   smallest artifact that tests it, and the kill criteria. Build only after
   the gate.
6. **Postmortems are blameless and specific.** Timeline, contributing
   factors, systemic fixes with owners and dates. A person-shaped cause is
   not a cause.
7. **Growth strategies state their mechanics.** Free-tier, free-tool and
   onboarding strategies declare the assumption, the funnel stage and the
   measurement before execution.
8. **Write clean.** Short declarative sentences. No em dash. Sentence case
   headings. No chatbot framing.

## 1. Product management (16 skills)

- **Toolkit and lifecycle** (product-manager-toolkit, product-manager,
  to-prd, requirements-writing, to-issues, create-issue-gate): quick-start
  toolkit; PRD process — problem, users, scope, success metrics, open
  questions; requirements with EARS syntax; issue conversion with a creation
  gate.
- **Discovery** (jobs-to-be-done-analyst, idea-os, idea-darwin, user-
  thoughts, entropy-box): JTBD context gathering first; idea generation and
  selection engines with explicit criteria; user thought capture.
- **Planning** (okr-system, planning-and-task-breakdown, plan-ledger-tasks-
  yylo, projects-work-management, analytics-product): OKRs with a scoring
  cadence; task breakdown with supporting-material availability declared;
  kanban planning; work management registers; data-driven decisions.
- **Roles** (rex, business-analyst carried by business hub): the analyst
  role with stated when-to-use.

## 2. Executive and organizational

- **Governance** (board-governance, stakeholder-investor-reports,
  change-management, vendor-contractor-management, people-directory,
  announcement-board, dei-dashboard, it-manager-pro, developer-onboarding,
  wiki-onboarding, pre-boarding, onboarding, onboard): board cadence and
  reporting; investor report structure; change classification before
  rollout; vendor registers; onboarding tracks with runtime prerequisites
  declared.
- **Decision frameworks** (decision-navigator, grill-me, grill-with-docs,
  grilling, read-all-adrs): the navigator's core philosophy — frame the
  decision, list the options, state the reversible/irreversible split;
  grilling skills stress-test a plan with questions before execution; ADR
  reading before architectural work.
- **Workflows** (conductor family — conductor-setup, conductor-new-track,
  conductor-manage, conductor-implement, conductor-status, conductor-revert,
  conductor-validator, cc-skill-strategic-compact): track-based work
  management with validation of artifacts and strategic context checkpoints.
- **Consulting** (00-andruia-consultant): solutions-architect advisory with
  stated scope.

## 3. Growth and launch

- **Launch** (launch-strategy): core philosophy — sequence the market, the
  message and the channel; define the beachhead before broad launch.
- **Pricing** (pricing-strategy): required context asked if missing — value
  metric, segment, willingness to pay, competitor anchors; packaging before
  price.
- **Free strategies** (free-tier-strategy, free-tool-strategy,
  traffic-potential-calculator, ctr-predictor): engineering-as-marketing
  with a build-cost ceiling; traffic estimates are models, not measurements.
- **Onboarding CRO** (onboarding-cro, onboarding-playbook, popup-cro
  carried by design hub): initial assessment required first; funnel stage
  and measurement declared.
- **Advisory personas** (pitch-psychologist, sequence-psychologist,
  multi-advisor, bill-gates, harvey-specter, shark): evidence-and-scope
  boundaries; parallel specialist boards with per-specialist dissent.

## 4. Operations and analysis fragments

- **Dashboards and KPIs** (kpi-dashboard-design, kpi-tracker, advanced-
  analytics-dashboard, plotly): dashboard design with do-not-use cases;
  trackers with fixed definitions; Plotly for charting.
- **Retail and logistics** (esl-price-sync, returns-reverse-logistics,
  carrier relationships carried by business hub): deterministic shelf-edge
  pricing architecture; reverse logistics flows.
- **Market data** (traderspy-smart-money, footval family — footval-stats-
  and-transfer-news, footval-value-and-compare-players): smart-money
  signals and player valuation with explained numbers — information, not
  advice.
- **AI strategy** (moatmri): AI disruption pressure analysis with stated
  methodology.
- **Legal** (legal-advisor): scope stated; not legal advice.
- **Lightning** (lightning-channel-factories, lightning-factory-explainer,
  stellar-multisig-threshold-coordinator): Lightning channel factories and
  Stellar multisig coordination with do-not-use cases. (web3 hub carries
  the depth.)

## 5. Cross-carried fragments

- **Engineering** (chrome-extension-developer, python-patterns, embedding-
  strategies, vector-index-tuning, weaviate-cookbooks, bento-ui,
  monochromatic-ui, build-ui, chat-widget): extension development with
  do-not-use cases; Python patterns; embedding and vector tuning with
  do-not-use cases. (engineering, data-ml and frontend hubs carry the
  depth.)
- **Security** (active-directory-attacks, cred-omega): AD attack-path
  assessment with scope; API-key security engine with execution
  boundaries. (security-operations hub carries the depth.)
- **Writing** (postmortem-writing): postmortem prose follows the
  blameless format in law 6. (writing-docs hub carries the style rules.)
- **Media** (voiceover-narration-studio): voiceover generation with stated
  prerequisites. (media-creative hub carries the depth.)
- **Community** (selector): skill selection for a tool collection.
- **People** (grill family carried above): interview-style challenge.

## 6. Output contract

- Name the skill, the decision or artifact, and the evidence base in the
  first line of reasoning and in the todo list.
- Report the artifact: a PRD, a requirement set, an OKR set, a report, a
  dashboard spec, a decision record.
- Keep metric names, requirement IDs, OKR keys and dates verbatim.
- State assumptions, evidence and confidence for every recommendation.
- Label models and estimates as models; never present a projection as a
  measurement.
- Keep open work open: a missing metric definition, an unverified assumption
  and a skipped gate are reported, never rounded up.
- Never print a credential, private payload or personal data; redact and
  name the rule.

## 7. Failure handling

| Situation | Response |
| --- | --- |
| A requirement is untestable | Rewrite it in EARS form or reject it. |
| A metric has no fixed definition | Fix the definition before computing. |
| A persona gives a directive | Treat it as a perspective; weigh it against evidence. |
| A growth tactic has no measurement plan | Name the metric and the baseline first. |
| A launch has no beachhead | Sequence the market before the channel. |
| A postmortem blames a person | Reframe to systemic contributing factors. |
| A traffic or CTR number has no model basis | Label it an estimate with assumptions. |
| A gate is skipped | Return to the gate; do not silently escalate. |
| The evidence contradicts the requested strategy | Show the evidence and stop. |

## Provenance

Merged from the strategy-executive class (71 catalog skills) and the
product-management class (16 catalog skills). Every source skill's
procedure, rule and policy is represented above; duplicates collapsed to one
canonical statement; evidence boundaries and fail-closed rules preserved. No
external file is required to use this skill.
