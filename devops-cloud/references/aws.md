# aws

Load for AWS provisioning, identity, networking and cost.

## terraform shape

```hcl
terraform {
  backend "s3" {
    bucket         = "org-tfstate"
    key            = "prod/network.tfstate"
    region         = "us-east-1"
    dynamodb_table = "tfstate-lock"
    encrypt        = true
  }
}
```

- One state per environment and per layer. A single state for everything serializes the team.
- `prevent_destroy` on databases and buckets with data.
- Tags on every resource: `env`, `owner`, `cost-center`.
- Pin the provider version. An unpinned provider changes behavior on the next init.

## identity

| need | choice |
| --- | --- |
| workload in aws | instance or task role |
| ci from another cloud | oidc federation |
| human access | sso with short sessions |
| cross-account | role assumption with an external id |

- No long-lived access keys. A key older than 90 days is a finding.
- One role per workload, scoped to the actions used. `*` on `*` is a finding.
- Permissions boundary on anything that can create roles.

## network

```
vpc 10.0.0.0/16
  public subnets   -> alb, nat
  private subnets  -> app, db
  endpoints        -> s3, dynamodb, secretsmanager
```

- Databases in private subnets, no public ip.
- Security groups reference groups, not cidr, for internal traffic.
- VPC endpoints for s3 and dynamodb: cuts nat cost and egress.

## compute

| workload | choice |
| --- | --- |
| request-driven, under 15 min | lambda |
| steady container | ecs fargate |
| kubernetes needed | eks with managed node groups |
| batch | batch or step functions |

Lambda: set memory from a measured run, not the default. Provisioned concurrency only after cold start is measured as the problem.

## storage and data

- S3: block public access at the account level, versioning on, lifecycle rules.
- RDS: multi-az for production, automated backups with a tested restore.
- DynamoDB: on-demand unless traffic is predictable, then provisioned with autoscaling.

## cost

```bash
aws ce get-cost-and-usage --time-period Start=2026-01-01,End=2026-02-01 \
  --granularity MONTHLY --metrics UnblendedCost --group-by Type=DIMENSION,Key=SERVICE
```

- Turn on cost allocation tags before optimizing; the top line item is usually data transfer or idle capacity, not the service named in the complaint.
- Delete unattached volumes and idle load balancers.
- Buy savings plans only after 90 days of stable baseline; a plan on a shrinking workload is a prepaid loss.

## review

- `terraform plan` replacements listed explicitly.
- IAM diff read line by line.
- Deletion protection on stateful resources.

## pagination and long jobs

- List calls return one page. Iterate with `--paginate`, or pass `--limit 500` on a bulk search. The default page is often 30.
- `begin_*` returns a poller. Wait on it, or store the id and poll with a deadline.
- A long job that outlives the request goes to a queue, not to a longer timeout.
## iac and platform index

| tool | the rule that matters |
| --- | --- |
| Planning entry | Before any change: account, region, environment, blast radius, rollback. A plan without the account id is a guess. |
| CDK | `cdk synth` is the artifact; `cdk diff` before deploy; a construct that calls `context` at synth time makes the build non-deterministic. |
| SST | Wraps CDK for app stacks: `sst dev` runs live Lambda, `sst deploy --stage prod`; a stage name is the environment. |
| CloudFormation | `DeletionPolicy: Retain` on stateful resources; `--no-execute-changeset` to inspect, then execute the same changeset. |
| ARM/Bicep | `az deployment group what-if` before create; `bicep build` to JSON so the diff is reviewable. |
| Multi-cloud / hybrid | One source of truth per resource; a resource managed by two tools (console plus IaC) drifts on the next apply. |
| EC2 | Instance profile over access keys; a user-data script that fails leaves a running instance with no service, check the console log. |
| Rotation | Four steps: create pending, test against the target, promote, delete the old. Skipping the test rotates into an outage. |
| CloudTrail | Management events on by default; data events cost per 100k and must be enabled per bucket. |
| Compliance | AWS Config rules plus Security Hub findings; a rule in `NON_COMPLIANT` with no owner is decoration. |
| Cleanup | Unattached EBS, old snapshots, idle load balancers, unused elastic IPs; tag every resource with owner and expiry or cleanup is guesswork. |
| Optimizer | Savings Plans before Reserved Instances for spiky workloads; a rightsizing recommendation without a 14-day metric window is noise. |
| Bedrock AgentCore | Agent runtime with session isolation; a tool Lambda needs its own IAM role, not the agent's. |
| GCP | `gcloud` project per environment, `--impersonate-service-account` over a downloaded key, org policy to block key creation. |
