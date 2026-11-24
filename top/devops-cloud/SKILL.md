---
name: devops-cloud
description: >
  One standalone skill for DevOps and cloud engineering: AWS (CDK/SST,
  EC2/ECS/Lambda, VPC, S3, RDS, IAM, Secrets Manager, CloudTrail, audits,
  authorized pentesting, FinOps), Azure SDK across five languages, GCP,
  Terraform, CloudFormation, Kubernetes and Helm, Docker and Podman, CI/CD
  (GitHub Actions, GitLab CI, Jenkins, CircleCI, ArgoCD GitOps), observability
  (OpenTelemetry, Prometheus, Grafana, Loki, Datadog, New Relic, eBPF,
  tracing, SLOs), secrets, incident management, Linux/shell operations, Vercel
  and Cloudflare deploys, and cost optimization. Merges the devops-cloud class
  (185 skills) and the aws + azure-sdk deep packs. Fully self-contained: every
  procedure is inline, no external references.
metadata:
  merges: devops-cloud
  sources: 185
---

# devops-cloud

## 0. Iron laws

**From the aws pack (bind everything below):**

1. **Verify the fact, then act.** Region, instance class, engine version,
   parameter range, price, quota and API shape change. Check current official
   documentation or an available MCP tool before stating one. With no source
   available, say the fact is unverified rather than filling it from memory.
2. **Read-only is the default.** Establish account, role, partition, region
   and resource before collecting evidence; confirm identity with
   `aws sts get-caller-identity`. Any command that creates, changes, deletes,
   rotates, enables or spends needs an approved change scope, a rollback
   plan and explicit authorization for that turn.
3. **Destructive and costly actions are separate.** Deleting a volume,
   bucket, database, trail, key or role — and anything that moves money —
   needs its own confirmation with the exact resource ids. An unattached or
   stopped resource can still be a recovery asset. Cleanup runs dry first.
4. **Evidence is per control.** A security or compliance result names the
   account, region, resource, check and an evidence timestamp, with `PASS`,
   `FAIL`, `UNKNOWN` or `NOT-APPLICABLE`. Never compute a score from skipped
   checks or stubs; list the regions and services you did not query.
5. **Secrets never surface.** Values live in a private file with mode 0600,
   an environment variable, or a secrets manager. Never in argv, a log, a
   commit or a chat message. Log ARNs and access metadata only; never print
   a new access key.
6. **Inventory is not exploitability.** IAM enumeration, wildcard policies
   and open groups are candidate paths. Explicit denies, SCPs, RCPs,
   permission boundaries, session policies, resource policies, conditions
   and service prerequisites decide whether a path works. Prove it or label
   it unproven.
7. **Templates keep their own rules.** Where a body says a command replaces
   a whole configuration (bucket policy, lifecycle rule, tagging set),
   inspect and preserve the existing entries first.

**From the azure-sdk pack (bind all SDK work):**

8. **Credential first.** `DefaultAzureCredential` in application code;
   managed identity or workload identity in Azure production; CLI or
   `DeveloperToolsCredential` (Rust) locally. Never hardcode a key,
   connection string or secret. Keys are fallback only, read from
   environment or secret manager.
9. **One client, one credential.** Create once, reuse across requests and
   clients. Check thread-safety and lifetime per guide. Dispose at shutdown:
   Python `async with`/`close()`, .NET `await using`, Java
   try-with-resources, Rust drop per crate guidance. Close child
   senders/receivers before the parent client.
10. **Catch the SDK exception.** .NET `RequestFailedException`/
    `ClientResultException`, Python `HttpResponseError`, Java
    `HttpResponseException`, TypeScript `RestError`. Branch on status, not
    message text. Status map: 400 shape, 401 credential, 403 authorization
    or policy, 404 missing resource, 409 conflict or state, 429 throttle,
    5xx transient.
11. **Retry once at one layer.** The SDK retries transient failures; never
    wrap calls in another unbounded retry loop. For 429 honor `Retry-After`,
    then exponential backoff with jitter, capped attempts.
12. **Paginate.** List operations return pages — iterate every page with the
    SDK pager or continuation token. Never assume one page.
13. **Long-running operations.** `begin_*` returns a poller; wait or call
    `.result()`, bound the wait, handle failure and cancellation states.
14. **Async stays async.** Never block the event loop; pass timeout and
    cancellation where supported.
15. **Pin versions.** Stable over preview unless a preview feature is
    required and reviewed. Use the exact endpoint form from the guide — some
    services require a custom subdomain, not a regional endpoint.
16. **Redact.** Never log keys, tokens, connection strings or full payloads;
    log resource ids and status codes.

## 1. AWS architecture and infrastructure as code

- **Planning entry** (skills): establish requirements, existing services,
  target account and region, constraints; read the repo's infrastructure
  definitions; choose a workflow. Planning does not prove a deployment
  works — never claim account, pricing, permission or availability facts
  without current evidence.
- **CDK** (cdk-development, cdk-patterns): TypeScript or Python stacks with
  three validation layers — IDE real-time feedback, `cdk synth` required,
  pre-commit safety net. Validation runs the project's own app and
  dependencies, may write `cdk.out` and call context providers; review the
  project and context first. It does not deploy.
- **SST** (sst-development): SST v4 Ion on Pulumi. Hard rules: never
  interpolate a Pulumi `Output<T>` into a plain JavaScript template literal;
  plan stateful migrations before any replacement; give every new Lambda,
  queue or schedule an alarm and a link. References cover authoring, deploy
  and troubleshoot, testing.
- **CloudFormation** (cloudformation): stack lifecycle, change sets,
  drift detection; prerequisites stated.
- **Terraform** (terraform-skill, terraform-specialist, terraform-
  infrastructure, terraform-aws, terraform-aws-modules, terraform-azure,
  terraform-gcp, terraform-module-library): remote state with locking;
  plan → review → apply; modules with pinned versions; provider
  configuration per cloud; Azure variant requires a reviewed,
  organization-approved package installed; module library with supporting
  material availability declared.
- **ARM/Bicep** (arm-templates): Azure CLI installed first; template
  deployment with what-if.
- **Multi-cloud / hybrid** (multi-cloud-architecture, hybrid-cloud-
  architect, hybrid-cloud-networking, cloud-architect): bundled upstream
  support declared where absent; architecture decisions with stated
  constraints; networking fragments with material availability declared.

## 2. AWS compute, serverless and event-driven

- **EC2**: select instance type; launch with IMDSv2 required via
  `--metadata-options "HttpTokens=required"`; bootstrap with user data;
  launch templates and auto-scaling groups.
- **ECS/Fargate**: cluster insights, ECR authentication and push, task
  definitions, service behind an ALB, CloudWatch log group must exist
  first.
- **Lambda**: build the deployment package; create and update the function;
  publish immutable versions; alias per version; weighted alias for canary
  traffic splits. Layers hold dependencies; event source mappings wire
  triggers; avoid a VPC unless required (it lengthens cold starts).
- **Serverless production path** (serverless): Lambda + API Gateway +
  DynamoDB + SQS/SNS with SAM or CDK deployment and cold-start work.
- **Event-driven design** (serverless-eda): speedy, simple, singular. Think
  concurrent requests, not total requests. Share nothing; assume no
  hardware affinity. Orchestrate with state machines instead of function
  chaining. Use events to trigger transactions. Design for failures and
  duplicates. Always configure dead letter queues. Instrument before launch.

## 3. AWS networking, storage and databases

- **VPC**: multi-AZ with public, private and isolated data subnets;
  internet gateway; one NAT gateway per AZ for high availability; per-AZ
  route tables; security groups scoped to actual traffic.
- **S3**: block all public access before anything else, then versioning,
  SSE-KMS, access logging, tags, an HTTPS and VPC-endpoint bucket policy,
  lifecycle rules, cross-region replication (needs versioning on both
  buckets). Policy, lifecycle and tagging calls replace existing
  configuration — read and merge first. A VPC-endpoint deny policy can lock
  out console and admin access; verify a recovery path before applying.
  Object Lock in compliance mode cannot be bypassed.
- **RDS**: two-AZ subnet group, Multi-AZ instance, master password in
  Secrets Manager, custom parameter group, read replicas including
  cross-region for DR. Engine versions, classes and parameter ranges in
  older bodies are historical examples — discover what the target region
  supports. Some parameter changes need a reboot; failover only when the
  operator asks.

## 4. AWS identity, secrets and audit

- **IAM**: policy JSON shape, trust policies, instance profiles,
  cross-account assume roles, GitHub Actions OIDC with a repo-scoped trust
  condition, permission boundaries. Minimum actions and resources always.
- **IAM hardening** (iam-best-practices): review wildcard actions, inline
  policies that should be managed, users without MFA, access keys older
  than 90 days. Rotate by writing the new key to a private file, testing
  it, then deactivating the old one. Never print the secret. A policy name
  alone does not establish effective permissions.
- **Secrets Manager**: store JSON, binary and KMS-encrypted secrets; read
  specific versions; list, tag, soft-delete with recovery window.
- **Rotation** (secrets-rotation): four-step Lambda — `setSecret` writes
  `AWSPENDING`, `testSecret` proves the target accepts it, `finishSecret`
  moves `AWSPENDING` to `AWSCURRENT`. Never write `AWSCURRENT` into the
  database by mistake; never substitute an asynchronous master-password
  change for a working rotation. Completion requires the expected `VersionId`
  at `AWSCURRENT` plus successful target authentication.
- **CloudTrail**: organization trail with a dedicated bucket, a write policy,
  public access blocked, versioning, SSE, lifecycle policy; advanced event
  selectors; CloudWatch metric filters and alarms for unauthorized calls,
  root use, console login without MFA, IAM policy changes. Log file
  validation detects tampering and does not prevent deletion; versioning
  alone is not immutable retention.
- **Security audit** (security-audit): read-only, per-control results with
  account, region, resource, timestamp; covers IAM, network, data
  protection; names the regions it did not query.
- **Compliance** (compliance-checker): maps an account to CIS AWS
  Foundations, PCI-DSS, HIPAA and SOC 2 — read the detailed procedure
  before execution.
- **Penetration testing** (penetration-testing): authorized-use only,
  mandatory confirmation gate (exact target URL, IP, account or resource).
  Covers IAM enumeration, privilege escalation candidates, metadata SSRF
  including IMDSv2, S3 exposure, Lambda code extraction, persistence.
  Inventory is not proof of exploitability; never change user agents or
  disable logging to evade detection.
- **Cloud IAM deep** (cloud-iam-deep): credential identification in the
  first 60 seconds; scope and evidence stated.

## 5. AWS cost and AI platform

- **Cleanup** (cost-cleanup): unattached EBS volumes, snapshots past
  retention, idle Elastic IPs, stale S3 objects. Dry run first; final
  snapshot before deletion; tested restore plan required.
- **Optimizer** (cost-optimizer, cost-optimization, cost-optimization
  catalog variant): CLI analysis for waste, idle instances, rightsizing;
  every deletion marked medium risk. FinOps review: rightsize, autoscale,
  plan commitments, storage lifecycle, budgets at 80 and 100 percent, Cost
  Anomaly Detection with an impact threshold. Never treat an estimate as a
  bill.
- **Cost operations** (cost-operations): pricing, Cost Explorer and
  CloudWatch MCP servers; estimate before deploying; budgets and alarms;
  query logs; read CloudTrail; assess posture.
- **Bedrock AgentCore** (agentic-ai): nine services — Gateway, Runtime,
  Memory, Identity, Code Interpreter, Browser, Observability, Agent
  Registry, Evaluations. Workflows: deploy a gateway target, manage
  credentials, discover agents and tools, evaluate agent quality, monitor.
- **MCP setup** (mcp-setup): check existing tool availability and config
  files before changing anything; verify `uvx` and Python 3.10+; verify
  credentials. The full server is only for API access; the documentation
  server needs no auth. Current AWS MCP forwards the caller's credentials
  downstream — grant only the actions and resources the task needs. A
  preview-era action set does not prove the current one.

## 6. Azure

- **SDK usage**: 127 guides across 30 families and 6 language groups
  (Python 36, .NET 27, Java 26, TypeScript 20, Rust 9, 9 language-neutral
  guides). Families: ai (28), management (12), storage (10), monitor (9),
  resource-manager (7), keyvault (7), communication (5), eventhub (5),
  identity (5), cosmos (5), servicebus (4), eventgrid (3), search (3),
  security (3), appconfiguration (3), data (2), functions (2), messaging
  (2), plus maps, postgres, aks, compute, containerregistry, devops,
  networking, speech, sql, vms, web, playwright (1 each). Workflow:
  identify service and language → confirm install command, package version
  and required environment variables → authenticate → build the client once
  → execute (paginate or poll) → handle exception and retry policy →
  dispose → verify with a read-back or returned id.
- **Language conventions**: Python `azure-*` packages, async clients in
  `aio`; .NET `Azure.*`, `await using`; Java `com.azure.*`,
  `DefaultAzureCredentialBuilder`, try-with-resources; TypeScript
  `@azure/*`; Rust `azure_*` crates with `DeveloperToolsCredential` for
  local tools.
- **azd** (azd-deployment): Azure Developer CLI Container Apps deployment
  with authorization and preparation steps.
- **GCP** (gcp-compute, gcp-cloud-run, gcp-cloud-functions, gcp-cloud-sql,
  gcp-gke, gcp-networking, gcp-secret-manager, gcp-audit-logs): every skill
  states target, billable effects and recovery boundaries before acting;
  project, cost and identity boundaries on GKE; network change and fragment
  scope; enable Data Access logs at organization level; Secret Manager with
  API enablement.

## 7. Containers and Kubernetes

- **Docker** (docker-expert, docker-management, docker-compose): execution
  scope stated when invoked; Compose with declared execution scope.
- **Podman** (podman): rootless containers; prerequisites stated.
- **Apple container** (apple-container): safety gate before use.
- **Hardening and scanning** (container-hardening, container-scanning,
  container-registries): Dockerfile security (non-root user, minimal base,
  no secrets in layers, pinned digests); scan images in CI; registries with
  prerequisites.
- **Kubernetes** (kubernetes-architect, kubernetes-ops, kubernetes-
  deployment, k8s-manifest-generator, k8s-security-policies, gpu-
  kubernetes-operations, openshift): core resources and prerequisites;
  deployment workflow; manifest generation with stated scope; security
  policies with material availability declared; GPU scheduling with
  prerequisites; OpenShift with cluster and privilege scope.
- **Helm** (helm-charts, helm-chart-scaffolding): chart structure, values
  layering, templating; scaffolding with declared scope.
- **Kustomize** (kustomize): overlays per environment; prerequisites.
- **Service mesh** (service-mesh, service-mesh-expert, service-mesh-
  observability, istio-traffic-management): mesh adoption criteria;
  traffic management (virtual services, destination rules, retries,
  timeouts); mesh telemetry.
- **ArgoCD GitOps** (argocd-gitops, gitops-workflow): Git as source of
  truth; sync policies; drift detection; prerequisites stated.
- **mirrord**: run local code against a remote cluster.

## 8. CI/CD and delivery

- **GitHub Actions** (github-actions, github-actions-advanced,
  github-actions-templates): scope and fragment prerequisites; advanced
  patterns (reusable workflows, matrices, OIDC, caching); workflow pattern
  templates with declared inputs.
- **GitLab CI** (gitlab-ci, gitlab-ci-patterns): stages, runners, rules,
  includes; prerequisites stated.
- **Jenkins** (jenkins): controller, agent and secret scope stated.
- **CircleCI** (circleci): orbs, workflows; prerequisites.
- **Pipeline design** (deployment-pipeline-design, devops-pipeline-builder,
  ci-cd-and-automation, cicd-automation-workflow-automate): decision
  framework for build → test → scan → deploy stages; automation scope
  declared.
- **Deployment strategies** (blue-green-deploy, deployment-engineer,
  deployment-procedures, deployment-validation-config-validate): platform
  selection first; blue-green, canary, rolling with prerequisites;
  configuration validation before rollout.
- **Pre-ship gate** (pre-ship-gate): checklist before release — tests green,
  migrations reversible, feature flags default-safe, rollback named.
- **Production runtime certification** (production-runtime-certification):
  certify runtime behavior before declaring production readiness.
- **Closed-loop delivery** (closed-loop-delivery, acceptance-orchestrator,
  aegisops-ai): delivery loop from acceptance criteria through verified
  rollout; autonomous governance orchestrator with stated goal and scope.
- **Vercel** (deploy-to-vercel, vercel-cli-with-tokens, vercel-deployment,
  vercel-deployments, vercel-optimize): gather project state first (git
  remote, framework, build command); locate the Vercel token from
  `VERCEL_TOKEN` env or config; deploy with prerequisites; optimize with
  framework support matrix.
- **Cloudflare** (cloudflare-pages, cloudflare-workers,
  cloudflare-workers-expert, cloudflare-r2, cloudflare-zero-trust): Pages
  with prerequisites; Workers with declared instructions; R2 with object and
  public-access scope; Zero Trust with prerequisites.
- **Publishing helpers** (dropthehassle-publish, shipvela-publish):
  external tool prerequisites and publishing paths declared.
- **Feature flags** (feature-flags): flag types (release, ops, experiment,
  permission); kill switches; flag hygiene and removal.
- **Policy as code** (policy-as-code): OPA Rego policies with an
  enforcement contract.

## 9. Observability

- **OpenTelemetry** (opentelemetry, distributed-tracing): prerequisites and
  core workflow; traces with context propagation across services; inputs
  and prerequisites stated.
- **Metrics and dashboards** (prometheus-configuration, prometheus-grafana,
  grafana-dashboards, sre-dashboards, datadog, new-relic): Prometheus with
  material availability declared; PromQL for RED/USE metrics; Grafana
  dashboards with stated instructions; SRE dashboards with prerequisites;
  SaaS agents with prerequisites.
- **Logs** (loki-logging, elk-stack): Loki with prerequisites; ELK with
  prerequisites.
- **eBPF** (ebpf-observability): kernel version requirements stated.
- **SLOs** (slo-implementation, observability-monitoring-slo-implement):
  SLI definition, error budgets, burn-rate alerting.
- **Instrumentation** (observability-and-instrumentation,
  observability-engineer, observability-monitoring-monitor-setup,
  observability-cloud-planning): instrument before launch; monitor setup
  with declared scope; planning across cloud and observability.
- **Error tracking** (error-diagnostics-error-trace): declared scope.
- **AI observability** (langfuse, rag-observability-evals, llmops-platform-
  engineering, model-registry-governance, model-serving-kubernetes,
  ml-pipeline-workflow, monte-carlo-monitor-creation,
  monte-carlo-monitoring-advisor, monte-carlo-prevent, recsys-pipeline-
  architect): LLM tracing and evals with inputs and prerequisites; RAG
  measurement; LLMOps platform with prerequisites; model registry
  governance; serving on K8s; data-quality monitors with activation and
  non-activation conditions; supporting material availability declared
  where absent.

## 10. Incidents, runbooks and operations

- **Incident management** (incident-management, incident-responder):
  severity levels defined; declared instructions for response roles.
- **Runbooks** (runbook-creation): full template — service/process name,
  purpose, scope, prerequisites, step-by-step procedure with expected
  output at each step, rollback, escalation contacts, verification.
- **Linux operations** (linux-administration, linux-troubleshooting,
  linux-shell-scripting, systemd-services, bash-linux, bash-pro,
  bash-scripting, bash-defensive-patterns, posix-shell-pro, os-scripting):
  prerequisites stated; troubleshooting workflow; production shell scripts
  with defensive patterns (set -euo pipefail, traps, quoting, mktemp);
  systemd unit management; OS/scripting troubleshooting bundle.
- **Windows** (powershell-windows, windows-shell-reliability): operator
  syntax rules with parentheses required; encoding and redirection
  reliability patterns.
- **SSH and remote** (ssh-configuration, sshepherd, vpn-setup, mac-api-
  connection-diagnostics): SSH config with prerequisites; host registry;
  VPN with prerequisites; diagnostics with declared scope.
- **VPS and servers** (vps-server-management, server-management, dep,
  cloudish, command-center-ui, user-management, admin-access-register):
  server inventories with host contracts; DevOps engineer persona with host
  and scope contract; user management with prerequisites; admin access
  register.
- **Backups** (backup-recovery, time-machine-recovery, rclone-cli):
  prerequisites; identify the failure before restoring; rclone with
  prerequisites for cloud storage sync.
- **Cost and FinOps extras** (geminiignore-finops, runaway-guard): cost is
  the third complexity dimension — the iron law: a job without a cost bound
  is a runaway; set $-budgets alongside time and token budgets.
- **Audit** (vibe-code-auditor): identity and purpose stated; audits
  AI-generated code for production readiness.

## 11. Environments and tooling

- **Dev containers** (devcontainer-setup, devcontainers-nix): bundled
  upstream support declared; environment execution boundaries stated.
- **mise** (mise-configurator): tool version management.
- **HyperExecute** (hyperexecute-skill): restored helper safety declared.
- **WebdriverIO** (webdriverio-skill): execution target stated in step 1.
- **Newman CI/CD** (newman-cicd-integration): collect required inputs from
  the user before generating CI integration.
- **gh-attach** (gh-attach): upload/download GitHub user-attachments.
- **Hono** (hono): edge-first web framework.
- **Unity ECS** (unity-ecs-patterns): (game-dev hub carries the depth).
- **Data fetchers** (noaa-radar-satellite-fetching, weather-model-data-
  fetching): weather/radar data pipelines.
- **Compliance** (risk-metrics-calculation, sred-project-organizer,
  sred-work-summary): risk metrics with declared scope; SR&ED project
  organization and work summaries with prerequisites.
- **WhatsApp Cloud API** (whatsapp-cloud-api): professional integration
  (Portuguese-canonical).
- **Alexa** (amazon-alexa): voice skill integration (Portuguese-canonical).
- **Auri** (auri-core): product skill with detailed guide.
- **SolidPing** (solidping): connect-once monitoring.
- **Manifest** (manifest): manifest setup and verification with
  availability declared.
- **Idea evaluator** (idea-evaluator-con): con-agent review perspective.
- **Ilya Sutskever persona** (ilya-sutskever): deep-learning persona
  (Portuguese-canonical). (data-ml hub carries the depth.)

## 12. Output contract

- Name the skill, the account or alias, and the region in the first line of
  reasoning and in the todo list.
- Report the command and its output for every claim about state; keep
  resource ids, ARNs, region codes and error strings verbatim.
- Separate what was observed from what was inferred from documentation or a
  candidate path.
- State the change scope, or state that the run was read-only.
- Keep open work open: an unqueried region, a skipped check and an
  unverified price are reported, never rounded up.
- Never print a secret, key, token or password; redact and name the rule.
- For Azure SDK work report:
  `sdk=<sdk> language=<lang> auth=<credential> operation=<method/tool>
  result=<id|status|count> retries=<n> pagination=<complete|stopped>
  verified=<yes|no>` plus one line for the next action.

## 13. Failure handling

| Situation | Response |
| --- | --- |
| The account, role or region is unclear | Stop and confirm. Never guess a target. |
| The action creates, changes, deletes, rotates or spends | Present exact ids, impact and rollback. Wait for approval. |
| Documentation or MCP is unavailable | Say the fact is unverified. Do not fill it from memory. |
| A security check is skipped or a tool is missing | Report `UNKNOWN` or `NOT-APPLICABLE` with the reason. Never score it. |
| A policy or lifecycle call would replace existing config | Read and merge first; show the preserved entries. |
| A cleanup candidate has no tested restore path | Do not delete it. Name the blocker. |
| A pentest path is only candidate | Label it unproven until a command proves it. |
| Azure `401` / `403` / `404` / `409` / `429` | Credential chain / RBAC plane / endpoint shape / read state, no blind retry / honor Retry-After with capped backoff. |
| A missing page or an LRO that never completes | Use the pager; bound the poll, inspect terminal state, check the operation id. |
| A client disposed early or a wrong endpoint | Reuse one client, dispose at shutdown; use the guide's exact endpoint. |
| A secret appears in code or a log | Remove, rotate, scan history. |
| The evidence contradicts the requested change | Show the evidence and stop. |

## Provenance

Merged from the devops-cloud class (185 catalog skills) and two curated
packs: aws (25 sources, 9 groups) and azure-sdk (127 SDK guides, 30
families, 6 languages, 73 assets). Every source skill's procedure, rule and
policy is represented above; duplicates collapsed to one canonical
statement; read-only defaults, confirmation gates and fail-closed rules
preserved. No external file is required to use this skill.
