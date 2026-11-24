---
name: azure-sdk
description: >
  Azure SDK usage across .NET, Java, Python, TypeScript, and Rust: AI/Foundry, OpenAI,
  Document Intelligence, Vision, Speech, Storage, Cosmos DB, Identity, Key Vault, Event
  Hubs, Event Grid, Service Bus, Monitor, Search, App Configuration, management-plane
  clients, containers, networking, SQL, and Functions. Use when writing, reviewing, or
  debugging Azure SDK code; choosing a credential; handling pagination, long-running
  operations, retries, throttling, or client disposal; or provisioning Azure resources
  from code.
metadata:
  curated_from: 127
  families: 30
  assets: 73
---

# azure-sdk

127 SDK guides. 30 service families. 6 language groups. One hub. Every guide preserved
verbatim in `references/sdks/<sdk>.md`.

## Use when

Use when:
- Writing or reviewing code that calls an Azure service through an official SDK.
- Choosing authentication: `DefaultAzureCredential`, managed identity, workload identity, service principal, or local developer credential.
- Debugging pagination, long-running operations, throttling, retries, timeouts, or client disposal.
- Provisioning through `Azure.ResourceManager.*` or `azure-mgmt-*` clients.
- Porting an operation between .NET, Java, Python, TypeScript, and Rust.

Do not use when:
- Authoring Bicep or Terraform. Use the infrastructure skill.
- Designing cloud architecture without SDK code. Use the architecture skill.
- The service has no SDK guide here. Check the family index, then the official Azure SDK docs.

## Hard rules

1. **Credential first.** Use `DefaultAzureCredential` in application code. Azure production: managed identity or workload identity. Local: Azure CLI, Azure Developer CLI, or `DeveloperToolsCredential` for Rust. Never hardcode a key, connection string, or secret.
2. **Keys are fallback.** API key or connection string only when the service cannot use Microsoft Entra ID. Read from an environment variable or secret manager. Never in source.
3. **One client.** Create once, reuse across requests. Clients and credentials are reusable; check the guide for thread-safety and lifetime.
4. **One credential.** Reuse the credential instance across clients. Do not build a new credential per call.
5. **Dispose.** Close async clients and credentials. Python: `async with` or `close()`. .NET: `await using`. Java: try-with-resources. Rust: drop per crate guidance. Close child senders, receivers, and processors before the parent client.
6. **Catch the SDK exception.** .NET: `RequestFailedException` or `ClientResultException`. Python: `HttpResponseError`. Java: `HttpResponseException`. TypeScript: `RestError`. Branch on status, not message text.
7. **Status map.** `400` request shape. `401` credential. `403` authorization or policy. `404` missing resource. `409` conflict or state. `429` throttle. `5xx` transient.
8. **Retry once at one layer.** The SDK retries transient failures. Do not wrap calls in another unbounded retry loop. For `429`, honor `Retry-After`, then exponential backoff with jitter. Cap attempts.
9. **Paginate.** List operations return pages. Iterate every page with the SDK pager or continuation token. Never assume one page.
10. **Long-running operations.** `begin_*` returns a poller. Wait or call `.result()`. Bound the wait with a timeout. Handle failure and cancellation states.
11. **Async stays async.** Use the async client in async code. Never block the event loop. Pass timeout and cancellation where supported.
12. **Pin versions.** Stable over preview unless a preview feature is required and reviewed. Record the API version where the guide does.
13. **Endpoint shape.** Use the exact endpoint form from the guide. Some services require a custom subdomain, not a regional endpoint.
14. **Redact.** Never log keys, tokens, connection strings, or full payloads. Log resource ids and status codes.

## Workflow

1. Identify service and language.
2. Pick the SDK from `references/INDEX.md` or `references/sdks.tsv`.
3. Read `references/sdks/<sdk>.md`.
4. Confirm install command, package version, and required environment variables.
5. Authenticate with a credential.
6. Build the client once.
7. Execute the operation. Paginate or poll as required.
8. Handle the service exception and retry policy.
9. Dispose clients and credentials.
10. Verify with a read-back or returned id.

## Family index

| Family | Guides | Examples |
| --- | --- | --- |
| `ai` | 28 | `azure-ai-projects-py`, `azure-ai-openai-dotnet`, `azure-ai-vision-imageanalysis-java` |
| `management` | 12 | `azure-mgmt-apimanagement-dotnet`, `azure-mgmt-fabric-py`, `azure-mgmt-botservice-dotnet` |
| `storage` | 10 | `azure-storage-blob-py`, `azure-storage-file-share-ts`, `azure-storage-queue-rust` |
| `monitor` | 9 | `azure-monitor-query-py`, `azure-monitor-opentelemetry-ts`, `azure-monitor-ingestion-java` |
| `resource-manager` | 7 | `azure-resource-manager-sql-dotnet`, `azure-resource-manager-cosmosdb-dotnet` |
| `keyvault` | 7 | `azure-keyvault-secrets-rust`, `azure-keyvault-keys-ts`, `azure-keyvault-certificates-rust` |
| `communication` | 5 | `azure-communication-chat-java`, `azure-communication-sms-java` |
| `eventhub` | 5 | `azure-eventhub-dotnet`, `azure-eventhub-java`, `azure-eventhub-py` |
| `identity` | 5 | `azure-identity-dotnet`, `azure-identity-ts`, `azure-identity-rust` |
| `cosmos` | 5 | `azure-cosmos-db-py`, `azure-cosmos-java`, `azure-cosmos-ts` |
| `servicebus` | 4 | `azure-servicebus-dotnet`, `azure-servicebus-py`, `azure-servicebus-rust` |
| `eventgrid` | 3 | `azure-eventgrid-dotnet`, `azure-eventgrid-java`, `azure-eventgrid-py` |
| `search` | 3 | `azure-search-documents-dotnet`, `azure-search-documents-py` |
| `security` | 3 | `azure-security-keyvault-keys-dotnet`, `azure-security-keyvault-secrets-java` |
| `appconfiguration` | 3 | `azure-appconfiguration-java`, `azure-appconfiguration-py` |
| `data` | 2 | `azure-data-tables-java`, `azure-data-tables-py` |
| `functions` | 2 | `azure-functions`, `azure-functions-devsec` |
| `messaging` | 2 | `azure-messaging-webpubsub-java`, `azure-messaging-webpubsubservice-py` |
| `maps` | 1 | `azure-maps-search-dotnet` |
| `postgres` | 1 | `azure-postgres-ts` |
| `aks` | 1 | `azure-aks` |
| `compute` | 1 | `azure-compute-batch-java` |
| `containerregistry` | 1 | `azure-containerregistry-py` |
| `devops` | 1 | `azure-devops` |
| `networking` | 1 | `azure-networking` |
| `speech` | 1 | `azure-speech-to-text-rest-py` |
| `sql` | 1 | `azure-sql` |
| `vms` | 1 | `azure-vms` |
| `web` | 1 | `azure-web-pubsub-ts` |
| `playwright` | 1 | `azure-microsoft-playwright-testing-ts` |

Full map: `references/INDEX.md`. Lookup table: `references/sdks.tsv` — `sdk, family, language, description, file, source`.

## Language matrix

| Language | Guides | Conventions |
| --- | --- | --- |
| Python | 36 | `azure-*` packages. `DefaultAzureCredential`. Async clients in `aio`. `async with` or `close()`. |
| .NET | 27 | `Azure.*` packages. `DefaultAzureCredential`. `await using` where disposable. `RequestFailedException`. |
| Java | 26 | `com.azure.*`. `DefaultAzureCredentialBuilder`. try-with-resources. Sync and async clients. |
| TypeScript | 20 | `@azure/*` packages. `DefaultAzureCredential` from `@azure/identity`. |
| Rust | 9 | `azure_*` crates. `DeveloperToolsCredential` for local tools. Managed identity in Azure. |
| Guide | 9 | Language-neutral service guides: Functions, SQL, VMs, networking, Key Vault, AKS, DevOps. |

Lookup:

```bash
rg -i "storage-blob" references/sdks.tsv
```

```powershell
Select-String -Path references/sdks.tsv -Pattern "storage-blob"
```

## Failure handling

| Symptom | Action |
| --- | --- |
| `401` | Check credential chain, tenant, client id, and local login. |
| `403` | Check RBAC role and data-plane vs management-plane permission. |
| `404` | Check endpoint shape, subscription, resource group, and name. |
| `409` | Read current state. Do not blind retry a conflict. |
| `429` | Honor `Retry-After`. Back off with jitter. Cap attempts. |
| Missing page | Use the pager. Do not assume one response. |
| LRO never completes | Bound the poll, inspect terminal state, check the operation id. |
| Client disposed early | Reuse one client; dispose at shutdown. |
| Wrong endpoint | Use the guide's exact endpoint. Custom subdomain services reject regional hosts. |
| Secret in code or log | Remove, rotate, and scan history. |

## Output contract

Report:

```
sdk=<sdk>  language=<lang>  auth=<credential>  operation=<method/tool>
result=<id|status|count>  retries=<n>  pagination=<complete|stopped>  verified=<yes/no>
```

Then one line for the next action. No restated code.

## Provenance

- `SOURCES.md` — all 127 source skills, SDK name, family, language.
- `references/sdks/` — 127 bodies verbatim, source path in an HTML comment.
- `references/INDEX.md` — 30 families, language breakdown.
- `references/sdks.tsv` — 127 rows.
- `references/assets/` — 73 files from 20 sources: references, licenses, notices, scripts, templates.
