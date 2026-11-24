# azure

Load for Azure provisioning, identity and networking.

## identity

| need | choice |
| --- | --- |
| ci to azure | federated credential on an app registration |
| workload | managed identity, system or user assigned |
| human | entra id with pim for privileged roles |
| cross-tenant | b2b guest with access review |

- No client secrets in a pipeline. Use workload identity federation.
- Scope role assignments to a resource group or resource, not the subscription.
- Owner at subscription scope is a finding.

## resource layout

```
subscription
  rg-prod-network      vnet, nsg, private dns
  rg-prod-app          app service, container apps, acr
  rg-prod-data         sql, storage, key vault
```

- One resource group per layer, per environment. Tags: `env`, `owner`, `cost-center`.
- `az deployment group what-if` before `az deployment group create`.

## network

- Private endpoints for storage, sql and key vault. Public access disabled.
- NSG rules reference service tags or application security groups.
- Private dns zone linked to the vnet for each private endpoint.
- Egress through a firewall or nat gateway with an allowlist.

## compute

| workload | choice |
| --- | --- |
| container, scale to zero | container apps |
| web app, slots needed | app service |
| kubernetes | aks with workload identity |
| job | container apps job or functions |

Container apps: set min replicas above zero for latency-sensitive paths, scale rules on a real metric.

## data

- SQL: private endpoint, entra auth over sql auth, backup retention set.
- Storage: `allowBlobPublicAccess: false`, soft delete on, versioning on.
- Key vault: rbac mode, purge protection on, private endpoint.

## cost

```bash
az consumption usage list --start-date 2026-01-01 --end-date 2026-02-01 --query "[].{name:instanceName,cost:pretaxCost}" -o table
```

- Reserved capacity after 90 days of stable baseline; a reservation on a shrinking workload is sunk cost.
- Delete orphaned disks, public ips and unattached nics.
- Log Analytics keeps 30 days free then bills per GB; set the retention per table and archive the rest.

## review

- what-if output read line by line, deletions listed.
- Role assignments scoped and justified.
- Private endpoints in place for every data service.
## azure conventions

| item | the rule that matters |
| --- | --- |
| Language conventions | Python `azure-*` with `aio` clients, .NET `Azure.*` with `await using`, Java `com.azure.*` with `TokenCredential`, JS `@azure/*`, Rust `azure_*` with `DeveloperToolsCredential` in dev. |
| azd | `azd up` provisions and deploys, `azd env` switches the environment; the `.azure/<env>/.env` holds the subscription and location, never a secret. |
