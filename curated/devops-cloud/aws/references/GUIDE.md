# aws guide

The long-form group prose and the full roster. `SKILL.md` is the loadable hub, and
`references/skills/<skill>.md` is the verbatim body to follow for one task.

### Architecture and infrastructure as code

| Skill | What it does |
| --- | --- |
| [`cdk-development`](references/skills/cdk-development.md) | Builds TypeScript or Python CDK apps with three validation layers, real-time IDE feedback, required synth, and a pre-commit net. |
| [`skills`](references/skills/skills.md) | Chooses an AWS architecture or infrastructure workflow for an existing app and reviews the plan before any cloud change. |
| [`sst-development`](references/skills/sst-development.md) | Writes SST v4 Ion apps that manage AWS resources as code through Pulumi, including links, stateful migrations, and an observability gate. |

### Compute and serverless

| Skill | What it does |
| --- | --- |
| [`ec2`](references/skills/ec2.md) | Launches and manages EC2 instances, AMIs, and auto-scaling groups with IMDSv2 required, user data, launch templates, and instance-type guidance. |
| [`ecs-fargate`](references/skills/ecs-fargate.md) | Deploys containers on ECS and Fargate with ECR pushes, task definitions, services behind an ALB, and rolling deployments. |
| [`lambda`](references/skills/lambda.md) | Builds Lambda functions with deployment packages, versions, aliases, weighted canaries, layers, and event source mappings. |
| [`serverless`](references/skills/serverless.md) | Builds production serverless apps on Lambda, API Gateway, DynamoDB, and SQS or SNS, with SAM or CDK deployment and cold-start work. |
| [`serverless-eda`](references/skills/serverless-eda.md) | Event-driven design from the Well-Architected serverless principles, including state machines, duplicate handling, dead letter queues, and observability. |

### Networking and storage

| Skill | What it does |
| --- | --- |
| [`s3`](references/skills/s3.md) | Creates hardened buckets with public access block first, versioning, SSE-KMS, logging, HTTPS and endpoint policies, lifecycle, replication, and presigned URLs. |
| [`vpc`](references/skills/vpc.md) | Builds a multi-AZ VPC with public, private, and isolated subnets, per-AZ NAT, route tables, and least-open security groups. |

### Databases

| Skill | What it does |
| --- | --- |
| [`rds`](references/skills/rds.md) | Provisions RDS with a two-AZ subnet group, Multi-AZ, Secrets Manager master password, parameter groups, and cross-region read replicas. |

### Identity and secrets

| Skill | What it does |
| --- | --- |
| [`iam`](references/skills/iam.md) | Writes least-privilege IAM roles and policies, instance profiles, cross-account assume roles, GitHub OIDC trust, and permission boundaries. |
| [`iam-best-practices`](references/skills/iam-best-practices.md) | Reviews and hardens IAM with wildcard, inline, MFA, and access-key checks, read-only first and explicit change scope for any rotation. |
| [`secrets-manager`](references/skills/secrets-manager.md) | Stores JSON, binary, and KMS-encrypted secrets with versions, recovery windows, tags, and a Lambda rotation function. Never logs a value. |
| [`secrets-rotation`](references/skills/secrets-rotation.md) | Automates secret rotation for RDS and API keys through a four-step Lambda, verifying AWSPENDING and AWSCURRENT before declaring success. |

### Audit, compliance, and testing

| Skill | What it does |
| --- | --- |
| [`cloudtrail`](references/skills/cloudtrail.md) | Configures an organization trail with a hardened log bucket, event selectors, metric filters, and alarms for root use, MFA gaps, and policy changes. |
| [`compliance-checker`](references/skills/compliance-checker.md) | Checks an account against CIS AWS Foundations, PCI-DSS, HIPAA, and SOC 2 through the bundled detailed guide. |
| [`penetration-testing`](references/skills/penetration-testing.md) | Authorized AWS red team techniques: IAM enumeration, metadata SSRF, S3, Lambda extraction, and persistence, behind a mandatory confirmation gate. |
| [`security-audit`](references/skills/security-audit.md) | Read-only posture assessment across IAM, network, and data protection, with per-control PASS, FAIL, UNKNOWN, and NOT-APPLICABLE results. |

### Cost

| Skill | What it does |
| --- | --- |
| [`cost-cleanup`](references/skills/cost-cleanup.md) | Finds and removes unused EBS volumes, old snapshots, idle EIPs, and stale S3 objects, dry-run first and with a backup plan. |
| [`cost-operations`](references/skills/cost-operations.md) | Cost and operations work through pricing, Cost Explorer, and CloudWatch MCP servers, from pre-deploy estimates to budgets and alarms. |
| [`cost-optimization`](references/skills/cost-optimization.md) | FinOps review with rightsizing, autoscaling, commitment planning, storage lifecycle, budgets, and anomaly detection. |
| [`cost-optimizer`](references/skills/cost-optimizer.md) | CLI cost analysis that finds unattached volumes, idle instances, old snapshots, and rightsizing gaps, with deletion marked medium risk. |

### AI platforms

| Skill | What it does |
| --- | --- |
| [`agentic-ai`](references/skills/agentic-ai.md) | Deploys and manages Bedrock AgentCore across its nine services, including Gateway, Runtime, Memory, Identity, Code Interpreter, Browser, Observability, Agent Registry, and Evaluations. |

### Tooling

| Skill | What it does |
| --- | --- |
| [`mcp-setup`](references/skills/mcp-setup.md) | Configures the AWS MCP servers for docs and API access, checks existing config and credentials first, and limits IAM to the actions the task needs. |

## Group notes

### Architecture and infrastructure as code

`skills` is the planning entry. Establish requirements, existing services, target
account and region, and constraints, read the repo's infrastructure definitions, then
choose a workflow. Planning does not prove a deployment works, so never claim account,
pricing, permission, or availability facts without current evidence.

`cdk-development` builds TypeScript or Python stacks with three validation layers. The
IDE layer gives real-time feedback, the synth layer is required, and the pre-commit
layer is the safety net. `scripts/validate-stack.sh` runs `cdk synth` from the caller's
project root, which executes that project's app and dependencies, may write `cdk.out`,
and may call AWS context providers for lookups. Review the project and context before
running it. The helper does not deploy.

`sst-development` covers SST v4 Ion on Pulumi. Read the relevant reference before
editing. Its hard rules are to never interpolate a Pulumi `Output<T>` into a plain
JavaScript template literal, to plan stateful migrations before any replacement, and to
give every new Lambda, queue, or schedule an alarm and a link. References cover
authoring, deploy and troubleshoot, and testing.

### Compute and serverless

`ec2` selects an instance type, launches with IMDSv2 required through
`--metadata-options "HttpTokens=required"`, bootstraps with user data, and manages
launch templates and auto-scaling groups. `ecs-fargate` covers cluster insights, ECR
authentication and push, task definitions, a service behind an ALB, and the CloudWatch
log group that must exist first.

`lambda` builds the deployment package, creates and updates the function, publishes
immutable versions, points an alias at a version, and splits traffic with a weighted
alias for a canary. Layers hold dependencies, event source mappings wire triggers, and
a VPC is avoided unless required because it lengthens cold starts. `serverless` is the
broader production path across Lambda, API Gateway, DynamoDB, and SQS or SNS, with SAM
or CDK deployment and cold-start work in `references/detailed-guide.md`.

`serverless-eda` supplies the Well-Architected design principles. Speedy, simple, and
singular. Think concurrent requests, not total requests. Share nothing and assume no
hardware affinity. Orchestrate with state machines instead of function chaining. Use
events to trigger transactions. Design for failures and duplicates. Always configure
dead letter queues, and instrument before launch.

### Networking and storage

`vpc` builds a multi-AZ VPC with public, private, and isolated data subnets, an
internet gateway, one NAT gateway per AZ for high availability, per-AZ route tables,
and security groups scoped to the actual traffic. `s3` blocks all public access before
anything else, then adds versioning, SSE-KMS, access logging, tags, an HTTPS and
VPC-endpoint bucket policy, lifecycle rules, and cross-region replication, which needs
versioning on both buckets.

Buckets are where replacement bites. Policy, lifecycle, and tagging calls replace the
existing configuration, so read and merge first. A VPC-endpoint deny policy can lock
out console and admin access, so verify a recovery path before applying. Object Lock in
compliance mode cannot be bypassed.

### Databases

`rds` creates a two-AZ subnet group, then a Multi-AZ instance with the master password
managed in Secrets Manager, a custom parameter group, and read replicas including a
cross-region one for disaster recovery. Engine versions, classes, and parameter ranges
in the body are historical examples, so discover what the target region supports. Some
parameter changes need a reboot, and a failover happens only when the operator asks for
one.

### Identity and secrets

`iam` covers the policy JSON shape, trust policies, instance profiles, cross-account
assume roles, GitHub Actions OIDC with a repo-scoped trust condition, and permission
boundaries. Always specify the minimum actions and resources. `iam-best-practices`
reviews wildcard actions, inline policies that should be managed, users without MFA,
and access keys older than 90 days. Rotate by writing the new key to a private file,
testing it, then deactivating the old one. Never print the secret. A policy name alone
does not establish effective permissions.

`secrets-manager` stores JSON, binary, and KMS-encrypted secrets, reads specific
versions, lists, tags, and soft-deletes with a recovery window. `secrets-rotation`
implements the four-step Lambda. `setSecret` writes `AWSPENDING`, `testSecret` proves
the target accepts it, and `finishSecret` moves `AWSPENDING` to `AWSCURRENT`. Never
write `AWSCURRENT` into the database by mistake, and never substitute an asynchronous
master-password change for a working rotation. Completion requires the expected
`VersionId` at `AWSCURRENT` plus successful target authentication.

### Audit, compliance, and testing

`cloudtrail` creates an organization trail with a dedicated bucket, a policy that lets
CloudTrail write, public access blocked, versioning, SSE, and a lifecycle policy, then
adds advanced event selectors and CloudWatch metric filters and alarms for
unauthorized calls, root use, console login without MFA, and IAM policy changes. Log
file validation detects tampering and does not prevent deletion. Versioning alone is
not immutable retention.

`security-audit` is read-only and reports per control with account, region, resource,
timestamp, and an explicit result. It covers IAM, network, and data protection, and it
names the regions it did not query. `compliance-checker` maps an account to CIS AWS
Foundations, PCI-DSS, HIPAA, and SOC 2 through `references/detailed-guide.md`, which
carries the full procedure and must be read before execution.

`penetration-testing` is authorized-use only and starts with a mandatory confirmation
gate that asks for the exact target URL, IP, account, or resource. It then covers IAM
enumeration, privilege escalation candidates, metadata SSRF including IMDSv2,
S3 exposure, Lambda code extraction, and persistence. Inventory is not proof of
exploitability, and the skill forbids changing user agents or disabling logging to
evade detection.

### Cost

`cost-cleanup` targets unattached EBS volumes, snapshots older than the retention
window, idle Elastic IPs, and stale S3 objects. It runs dry first, takes a final
snapshot before deletion, and requires a tested restore plan. An old resource can still
be a required recovery asset. `cost-optimizer` runs the CLI analysis for the same
waste, plus idle instances and rightsizing, and marks every deletion as medium risk.

`cost-optimization` is the FinOps review. Rightsize, autoscale, plan commitments, set
storage lifecycle, create budgets at 80 and 100 percent, and enable Cost Anomaly
Detection with an impact threshold. `cost-operations` adds the pricing, Cost Explorer,
and CloudWatch MCP servers, estimates cost before deploying, sets budgets and alarms,
queries logs, reads CloudTrail, and assesses posture. Both restate the least-privilege
rule and never treat an estimate as a bill.

### AI platforms

`agentic-ai` covers Bedrock AgentCore and its nine services: Gateway, Runtime, Memory,
Identity, Code Interpreter, Browser, Observability, Agent Registry, and Evaluations.
Workflows include deploying a gateway target, managing credentials, discovering agents
and tools, evaluating agent quality, and monitoring. Deep-dive and OAuth references
plus runnable CLI script templates are linked from the body.

### Tooling

`mcp-setup` checks existing tool availability and configuration files before changing
anything, verifies `uvx` and Python 3.10 or newer, and verifies credentials. The full
server is only for API access, and the documentation server needs no auth. Current AWS
MCP forwards the caller's credentials downstream, so grant only the actions and
resources the task needs. A preview-era action set does not prove the current one.
