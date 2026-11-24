# Azure SDK index

127 SDK guides across 30 families. Load only the SDK for the target service and language.

| Family | Guides | Languages |
| --- | --- | --- |
| `ai` | 28 | python 11, java 7, dotnet 5, typescript 5 |
| `management` | 12 | dotnet 8, python 4 |
| `storage` | 10 | python 4, typescript 3, rust 2, java 1 |
| `monitor` | 9 | python 4, java 3, guide 1, typescript 1 |
| `keyvault` | 7 | rust 3, typescript 2, guide 1, python 1 |
| `resource-manager` | 7 | dotnet 7 |
| `communication` | 5 | java 5 |
| `cosmos` | 5 | python 2, java 1, rust 1, typescript 1 |
| `eventhub` | 5 | dotnet 1, java 1, python 1, rust 1, typescript 1 |
| `identity` | 5 | dotnet 1, java 1, python 1, rust 1, typescript 1 |
| `servicebus` | 4 | dotnet 1, python 1, rust 1, typescript 1 |
| `appconfiguration` | 3 | java 1, python 1, typescript 1 |
| `eventgrid` | 3 | dotnet 1, java 1, python 1 |
| `search` | 3 | dotnet 1, python 1, typescript 1 |
| `security` | 3 | java 2, dotnet 1 |
| `data` | 2 | java 1, python 1 |
| `functions` | 2 | guide 2 |
| `messaging` | 2 | java 1, python 1 |
| `aks` | 1 | guide 1 |
| `compute` | 1 | java 1 |
| `containerregistry` | 1 | python 1 |
| `devops` | 1 | guide 1 |
| `maps` | 1 | dotnet 1 |
| `networking` | 1 | guide 1 |
| `playwright` | 1 | typescript 1 |
| `postgres` | 1 | typescript 1 |
| `speech` | 1 | python 1 |
| `sql` | 1 | guide 1 |
| `vms` | 1 | guide 1 |
| `web` | 1 | typescript 1 |

## ai

| SDK | Language | Purpose |
| --- | --- | --- |
| [`azure-ai-agents-persistent-dotnet`](sdks/azure-ai-agents-persistent-dotnet.md) | dotnet | Azure AI Agents Persistent SDK for .NET. Low-level SDK for creating and managing AI agents with threads, messages, runs, and tools. |
| [`azure-ai-agents-persistent-java`](sdks/azure-ai-agents-persistent-java.md) | java | Azure AI Agents Persistent SDK for Java. Low-level SDK for creating and managing AI agents with threads, messages, runs, and tools. |
| [`azure-ai-anomalydetector-java`](sdks/azure-ai-anomalydetector-java.md) | java | Build anomaly detection applications with Azure AI Anomaly Detector SDK for Java. Use when implementing univariate/multivariate anomaly detection, time-series analysis, or AI-powered monitoring. |
| [`azure-ai-contentsafety-java`](sdks/azure-ai-contentsafety-java.md) | java | Build content moderation applications using the Azure AI Content Safety SDK for Java. |
| [`azure-ai-contentsafety-py`](sdks/azure-ai-contentsafety-py.md) | python | Azure AI Content Safety SDK for Python. Use for detecting harmful content in text and images with multi-severity classification. |
| [`azure-ai-contentsafety-ts`](sdks/azure-ai-contentsafety-ts.md) | typescript | Analyze text and images for harmful content with customizable blocklists. |
| [`azure-ai-contentunderstanding-py`](sdks/azure-ai-contentunderstanding-py.md) | python | Azure AI Content Understanding SDK for Python. Use for multimodal content extraction from documents, images, audio, and video. |
| [`azure-ai-document-intelligence-dotnet`](sdks/azure-ai-document-intelligence-dotnet.md) | dotnet | Azure AI Document Intelligence SDK for .NET. Extract text, tables, and structured data from documents using prebuilt and custom models. |
| [`azure-ai-document-intelligence-ts`](sdks/azure-ai-document-intelligence-ts.md) | typescript | Extract text, tables, and structured data from documents using prebuilt and custom models. |
| [`azure-ai-formrecognizer-java`](sdks/azure-ai-formrecognizer-java.md) | java | Build document analysis applications using the Azure AI Document Intelligence SDK for Java. |
| [`azure-ai-language-conversations-py`](sdks/azure-ai-language-conversations-py.md) | python | Implement Conversational Language Understanding (CLU) using the azure-ai-language-conversations Python SDK. Use when working with ConversationAnalysisClient to analyze conversation intent and entities, building NLP features, or integrating language understandi |
| [`azure-ai-ml-py`](sdks/azure-ai-ml-py.md) | python | Azure Machine Learning SDK v2 for Python. Use for ML workspaces, jobs, models, datasets, compute, and pipelines. |
| [`azure-ai-openai-dotnet`](sdks/azure-ai-openai-dotnet.md) | dotnet | Azure OpenAI SDK for .NET. Client library for Azure OpenAI and OpenAI services. Use for chat completions, embeddings, image generation, audio transcription, and assistants. |
| [`azure-ai-projects-dotnet`](sdks/azure-ai-projects-dotnet.md) | dotnet | Azure AI Projects SDK for .NET. High-level client for Azure AI Foundry projects including agents, connections, datasets, deployments, evaluations, and indexes. |
| [`azure-ai-projects-java`](sdks/azure-ai-projects-java.md) | java | Azure AI Projects SDK for Java. High-level SDK for Azure AI Foundry project management including connections, datasets, indexes, and evaluations. |
| [`azure-ai-projects-py`](sdks/azure-ai-projects-py.md) | python | Build AI applications on Microsoft Foundry using the azure-ai-projects SDK. |
| [`azure-ai-projects-ts`](sdks/azure-ai-projects-ts.md) | typescript | High-level SDK for Azure AI Foundry projects with agents, connections, deployments, and evaluations. |
| [`azure-ai-textanalytics-py`](sdks/azure-ai-textanalytics-py.md) | python | Azure AI Text Analytics SDK for sentiment analysis, entity recognition, key phrases, language detection, PII, and healthcare NLP. Use for natural language processing on text. |
| [`azure-ai-transcription-py`](sdks/azure-ai-transcription-py.md) | python | Azure AI Transcription SDK for Python. Use for audio-file transcription with timestamps; distinguish this client from streaming and asynchronous batch Speech APIs. |
| [`azure-ai-translation-document-py`](sdks/azure-ai-translation-document-py.md) | python | Azure AI Document Translation SDK for batch translation of documents with format preservation. Use for translating Word, PDF, Excel, PowerPoint, and other document formats at scale. |
| [`azure-ai-translation-text-py`](sdks/azure-ai-translation-text-py.md) | python | Azure AI Text Translation SDK for real-time text translation, transliteration, language detection, and dictionary lookup. Use for translating text content in applications. |
| [`azure-ai-translation-ts`](sdks/azure-ai-translation-ts.md) | typescript | Text and document translation with REST-style clients. |
| [`azure-ai-vision-imageanalysis-java`](sdks/azure-ai-vision-imageanalysis-java.md) | java | Build image analysis applications with Azure AI Vision SDK for Java. Use when implementing image captioning, OCR text extraction, object detection, tagging, or smart cropping. |
| [`azure-ai-vision-imageanalysis-py`](sdks/azure-ai-vision-imageanalysis-py.md) | python | Azure AI Vision Image Analysis SDK for captions, tags, objects, OCR, people detection, and smart cropping. Use for computer vision and image understanding tasks. |
| [`azure-ai-voicelive-dotnet`](sdks/azure-ai-voicelive-dotnet.md) | dotnet | Azure AI Voice Live SDK for .NET. Build real-time voice AI applications with bidirectional WebSocket communication. |
| [`azure-ai-voicelive-java`](sdks/azure-ai-voicelive-java.md) | java | Azure AI VoiceLive SDK for Java. Real-time bidirectional voice conversations with AI assistants using WebSocket. |
| [`azure-ai-voicelive-py`](sdks/azure-ai-voicelive-py.md) | python | Build real-time voice AI applications with bidirectional WebSocket communication. |
| [`azure-ai-voicelive-ts`](sdks/azure-ai-voicelive-ts.md) | typescript | Azure AI Voice Live SDK for JavaScript/TypeScript. Build real-time voice AI applications with bidirectional WebSocket communication. |


## management

| SDK | Language | Purpose |
| --- | --- | --- |
| [`azure-mgmt-apicenter-dotnet`](sdks/azure-mgmt-apicenter-dotnet.md) | dotnet | Azure API Center SDK for .NET. Centralized API inventory management with governance, versioning, and discovery. |
| [`azure-mgmt-apicenter-py`](sdks/azure-mgmt-apicenter-py.md) | python | Azure API Center Management SDK for Python. Use for managing API inventory, metadata, and governance across your organization. |
| [`azure-mgmt-apimanagement-dotnet`](sdks/azure-mgmt-apimanagement-dotnet.md) | dotnet | Azure Resource Manager SDK for API Management in .NET. |
| [`azure-mgmt-apimanagement-py`](sdks/azure-mgmt-apimanagement-py.md) | python | Azure API Management SDK for Python. Use for managing APIM services, APIs, products, subscriptions, and policies. |
| [`azure-mgmt-applicationinsights-dotnet`](sdks/azure-mgmt-applicationinsights-dotnet.md) | dotnet | Azure Application Insights SDK for .NET. Application performance monitoring and observability resource management. |
| [`azure-mgmt-arizeaiobservabilityeval-dotnet`](sdks/azure-mgmt-arizeaiobservabilityeval-dotnet.md) | dotnet | Azure Resource Manager SDK for Arize AI Observability and Evaluation (.NET). |
| [`azure-mgmt-botservice-dotnet`](sdks/azure-mgmt-botservice-dotnet.md) | dotnet | Azure Resource Manager SDK for Bot Service in .NET. Management plane operations for creating and managing Azure Bot resources, channels (Teams, DirectLine, Slack), and connection settings. |
| [`azure-mgmt-botservice-py`](sdks/azure-mgmt-botservice-py.md) | python | Azure Bot Service Management SDK for Python. Use for creating, managing, and configuring Azure Bot Service resources. |
| [`azure-mgmt-fabric-dotnet`](sdks/azure-mgmt-fabric-dotnet.md) | dotnet | Azure Resource Manager SDK for Fabric in .NET. |
| [`azure-mgmt-fabric-py`](sdks/azure-mgmt-fabric-py.md) | python | Azure Fabric Management SDK for Python. Use for managing Microsoft Fabric capacities and resources. |
| [`azure-mgmt-mongodbatlas-dotnet`](sdks/azure-mgmt-mongodbatlas-dotnet.md) | dotnet | Manage MongoDB Atlas Organizations as Azure ARM resources with unified billing through Azure Marketplace. |
| [`azure-mgmt-weightsandbiases-dotnet`](sdks/azure-mgmt-weightsandbiases-dotnet.md) | dotnet | Azure Weights & Biases SDK for .NET. ML experiment tracking and model management via Azure Marketplace. Use for creating W&B instances, managing SSO, marketplace integration, and ML observability. |


## storage

| SDK | Language | Purpose |
| --- | --- | --- |
| [`azure-storage-blob-java`](sdks/azure-storage-blob-java.md) | java | Build blob storage applications using the Azure Storage Blob SDK for Java. |
| [`azure-storage-blob-py`](sdks/azure-storage-blob-py.md) | python | Azure Blob Storage SDK for Python. Use for uploading, downloading, listing blobs, managing containers, and blob lifecycle. |
| [`azure-storage-blob-rust`](sdks/azure-storage-blob-rust.md) | rust | Azure Blob Storage SDK for Rust. Use for uploading, downloading, and managing blobs and containers. |
| [`azure-storage-blob-ts`](sdks/azure-storage-blob-ts.md) | typescript | Azure Blob Storage JavaScript/TypeScript SDK (@azure/storage-blob) for blob operations. Use for uploading, downloading, listing, and managing blobs and containers. |
| [`azure-storage-file-datalake-py`](sdks/azure-storage-file-datalake-py.md) | python | Azure Data Lake Storage Gen2 SDK for Python. Use for hierarchical file systems, big data analytics, and file/directory operations. |
| [`azure-storage-file-share-py`](sdks/azure-storage-file-share-py.md) | python | Azure Storage File Share SDK for Python. Use for SMB file shares, directories, and file operations in the cloud. |
| [`azure-storage-file-share-ts`](sdks/azure-storage-file-share-ts.md) | typescript | Azure File Share JavaScript/TypeScript SDK (@azure/storage-file-share) for SMB file share operations. |
| [`azure-storage-queue-py`](sdks/azure-storage-queue-py.md) | python | Azure Queue Storage SDK for Python. Use for reliable message queuing, task distribution, and asynchronous processing. |
| [`azure-storage-queue-rust`](sdks/azure-storage-queue-rust.md) | rust | Azure Queue Storage library for Rust. Send, receive, and manage queue messages. Triggers: "queue storage rust", "QueueClient rust", "send message rust", "receive messages rust", "QueueServiceClient rust", "queue rust". |
| [`azure-storage-queue-ts`](sdks/azure-storage-queue-ts.md) | typescript | Azure Queue Storage JavaScript/TypeScript SDK (@azure/storage-queue) for message queue operations. Use for sending, receiving, peeking, and deleting messages in queues. |


## monitor

| SDK | Language | Purpose |
| --- | --- | --- |
| [`azure-monitor-audit`](sdks/azure-monitor-audit.md) | guide | Configure Azure Monitor and Activity Log for auditing. Set up diagnostic |
| [`azure-monitor-ingestion-java`](sdks/azure-monitor-ingestion-java.md) | java | Azure Monitor Ingestion SDK for Java. Send custom logs to Azure Monitor via Data Collection Rules (DCR) and Data Collection Endpoints (DCE). |
| [`azure-monitor-ingestion-py`](sdks/azure-monitor-ingestion-py.md) | python | Azure Monitor Ingestion SDK for Python. Use for sending custom logs to Log Analytics workspace via Logs Ingestion API. |
| [`azure-monitor-opentelemetry-exporter-java`](sdks/azure-monitor-opentelemetry-exporter-java.md) | java | Azure Monitor OpenTelemetry Exporter for Java. Export OpenTelemetry traces, metrics, and logs to Azure Monitor/Application Insights. |
| [`azure-monitor-opentelemetry-exporter-py`](sdks/azure-monitor-opentelemetry-exporter-py.md) | python | Azure Monitor OpenTelemetry Exporter for Python. Use for low-level OpenTelemetry export to Application Insights. |
| [`azure-monitor-opentelemetry-py`](sdks/azure-monitor-opentelemetry-py.md) | python | Azure Monitor OpenTelemetry Distro for Python. Use for one-line Application Insights setup with auto-instrumentation. |
| [`azure-monitor-opentelemetry-ts`](sdks/azure-monitor-opentelemetry-ts.md) | typescript | Auto-instrument Node.js applications with distributed tracing, metrics, and logs. |
| [`azure-monitor-query-java`](sdks/azure-monitor-query-java.md) | java | Azure Monitor Query SDK for Java. Execute Kusto queries against Log Analytics workspaces and query metrics from Azure resources. |
| [`azure-monitor-query-py`](sdks/azure-monitor-query-py.md) | python | Azure Monitor Query SDK for Python. Use for querying Log Analytics workspaces and Azure Monitor metrics. |


## keyvault

| SDK | Language | Purpose |
| --- | --- | --- |
| [`azure-keyvault`](sdks/azure-keyvault.md) | guide | Manage secrets and certificates in Azure Key Vault. Configure access |
| [`azure-keyvault-certificates-rust`](sdks/azure-keyvault-certificates-rust.md) | rust | Azure Key Vault Certificates SDK for Rust. Use for creating, importing, and managing certificates. |
| [`azure-keyvault-keys-rust`](sdks/azure-keyvault-keys-rust.md) | rust | Azure Key Vault Keys SDK for Rust. Use for creating, managing, and using cryptographic keys. Triggers: "keyvault keys rust", "KeyClient rust", "create key rust", "encrypt rust", "sign rust". |
| [`azure-keyvault-keys-ts`](sdks/azure-keyvault-keys-ts.md) | typescript | Manage cryptographic keys using Azure Key Vault Keys SDK for JavaScript (@azure/keyvault-keys). Use when creating, encrypting/decrypting, signing, or rotating keys. |
| [`azure-keyvault-py`](sdks/azure-keyvault-py.md) | python | Azure Key Vault SDK for Python. Use for secrets, keys, and certificates management with secure storage. |
| [`azure-keyvault-secrets-rust`](sdks/azure-keyvault-secrets-rust.md) | rust | Azure Key Vault Secrets SDK for Rust. Use for storing and retrieving secrets, passwords, and API keys. Triggers: "keyvault secrets rust", "SecretClient rust", "get secret rust", "set secret rust". |
| [`azure-keyvault-secrets-ts`](sdks/azure-keyvault-secrets-ts.md) | typescript | Manage secrets using Azure Key Vault Secrets SDK for JavaScript (@azure/keyvault-secrets). Use when storing and retrieving application secrets or configuration values. |


## resource-manager

| SDK | Language | Purpose |
| --- | --- | --- |
| [`azure-resource-manager-cosmosdb-dotnet`](sdks/azure-resource-manager-cosmosdb-dotnet.md) | dotnet | Azure Resource Manager SDK for Cosmos DB in .NET. |
| [`azure-resource-manager-durabletask-dotnet`](sdks/azure-resource-manager-durabletask-dotnet.md) | dotnet | Azure Resource Manager SDK for Durable Task Scheduler in .NET. |
| [`azure-resource-manager-mysql-dotnet`](sdks/azure-resource-manager-mysql-dotnet.md) | dotnet | Azure MySQL Flexible Server SDK for .NET. Database management for MySQL Flexible Server deployments. |
| [`azure-resource-manager-playwright-dotnet`](sdks/azure-resource-manager-playwright-dotnet.md) | dotnet | Azure Resource Manager SDK for Microsoft Playwright Testing in .NET. |
| [`azure-resource-manager-postgresql-dotnet`](sdks/azure-resource-manager-postgresql-dotnet.md) | dotnet | Azure PostgreSQL Flexible Server SDK for .NET. Database management for PostgreSQL Flexible Server deployments. |
| [`azure-resource-manager-redis-dotnet`](sdks/azure-resource-manager-redis-dotnet.md) | dotnet | Azure Resource Manager SDK for Redis in .NET. |
| [`azure-resource-manager-sql-dotnet`](sdks/azure-resource-manager-sql-dotnet.md) | dotnet | Azure Resource Manager SDK for Azure SQL in .NET. |


## communication

| SDK | Language | Purpose |
| --- | --- | --- |
| [`azure-communication-callautomation-java`](sdks/azure-communication-callautomation-java.md) | java | Build server-side call automation workflows including IVR systems, call routing, recording, and AI-powered interactions. |
| [`azure-communication-callingserver-java`](sdks/azure-communication-callingserver-java.md) | java | ⚠️ DEPRECATED: This SDK has been renamed to Call Automation. For new projects, use azure-communication-callautomation instead. This skill is for maintaining legacy code only. |
| [`azure-communication-chat-java`](sdks/azure-communication-chat-java.md) | java | Build real-time chat applications with thread management, messaging, participants, and read receipts. |
| [`azure-communication-common-java`](sdks/azure-communication-common-java.md) | java | Azure Communication Services common utilities for Java. Use when working with CommunicationTokenCredential, user identifiers, token refresh, or shared authentication across ACS services. |
| [`azure-communication-sms-java`](sdks/azure-communication-sms-java.md) | java | Send SMS messages with Azure Communication Services SMS Java SDK. Use when implementing SMS notifications, alerts, OTP delivery, bulk messaging, or delivery reports. |


## cosmos

| SDK | Language | Purpose |
| --- | --- | --- |
| [`azure-cosmos-db-py`](sdks/azure-cosmos-db-py.md) | python | Build production-grade Azure Cosmos DB NoSQL services following clean code, security best practices, and TDD principles. |
| [`azure-cosmos-java`](sdks/azure-cosmos-java.md) | java | Azure Cosmos DB SDK for Java. NoSQL database operations with global distribution, multi-model support, and reactive patterns. |
| [`azure-cosmos-py`](sdks/azure-cosmos-py.md) | python | Azure Cosmos DB SDK for Python (NoSQL API). Use for document CRUD, queries, containers, and globally distributed data. |
| [`azure-cosmos-rust`](sdks/azure-cosmos-rust.md) | rust | Azure Cosmos DB SDK for Rust (NoSQL API). Use for document CRUD, queries, containers, and globally distributed data. |
| [`azure-cosmos-ts`](sdks/azure-cosmos-ts.md) | typescript | Azure Cosmos DB JavaScript/TypeScript SDK (@azure/cosmos) for data plane operations. Use for CRUD operations on documents, queries, bulk operations, and container management. |


## eventhub

| SDK | Language | Purpose |
| --- | --- | --- |
| [`azure-eventhub-dotnet`](sdks/azure-eventhub-dotnet.md) | dotnet | Azure Event Hubs SDK for .NET. |
| [`azure-eventhub-java`](sdks/azure-eventhub-java.md) | java | Build real-time streaming applications with Azure Event Hubs SDK for Java. Use when implementing event streaming, high-throughput data ingestion, or building event-driven architectures. |
| [`azure-eventhub-py`](sdks/azure-eventhub-py.md) | python | Azure Event Hubs SDK for Python streaming. Use for high-throughput event ingestion, producers, consumers, and checkpointing. |
| [`azure-eventhub-rust`](sdks/azure-eventhub-rust.md) | rust | Azure Event Hubs SDK for Rust. Use for sending and receiving events, streaming data ingestion. |
| [`azure-eventhub-ts`](sdks/azure-eventhub-ts.md) | typescript | High-throughput event streaming and real-time data ingestion. |


## identity

| SDK | Language | Purpose |
| --- | --- | --- |
| [`azure-identity-dotnet`](sdks/azure-identity-dotnet.md) | dotnet | Azure Identity SDK for .NET. Authentication library for Azure SDK clients using Microsoft Entra ID. Use for DefaultAzureCredential, managed identity, service principals, and developer credentials. |
| [`azure-identity-java`](sdks/azure-identity-java.md) | java | Authenticate Java applications with Azure services using Microsoft Entra ID (Azure AD). |
| [`azure-identity-py`](sdks/azure-identity-py.md) | python | Azure Identity SDK for Python authentication. Use for DefaultAzureCredential, managed identity, service principals, and token caching. |
| [`azure-identity-rust`](sdks/azure-identity-rust.md) | rust | Azure Identity SDK for Rust authentication. Use for DeveloperToolsCredential, ManagedIdentityCredential, ClientSecretCredential, and token-based authentication. |
| [`azure-identity-ts`](sdks/azure-identity-ts.md) | typescript | Authenticate to Azure services with various credential types. |


## servicebus

| SDK | Language | Purpose |
| --- | --- | --- |
| [`azure-servicebus-dotnet`](sdks/azure-servicebus-dotnet.md) | dotnet | Azure Service Bus SDK for .NET. Enterprise messaging with queues, topics, subscriptions, and sessions. |
| [`azure-servicebus-py`](sdks/azure-servicebus-py.md) | python | Azure Service Bus SDK for Python messaging. Use for queues, topics, subscriptions, and enterprise messaging patterns. |
| [`azure-servicebus-rust`](sdks/azure-servicebus-rust.md) | rust | Azure Service Bus library for Rust. Send and receive messages using queues, topics, and subscriptions. Triggers: "service bus rust", "ServiceBusClient rust", "send message servicebus rust", "receive message servicebus rust", "queue rust messaging", "topic subs |
| [`azure-servicebus-ts`](sdks/azure-servicebus-ts.md) | typescript | Enterprise messaging with queues, topics, and subscriptions. |


## appconfiguration

| SDK | Language | Purpose |
| --- | --- | --- |
| [`azure-appconfiguration-java`](sdks/azure-appconfiguration-java.md) | java | Azure App Configuration SDK for Java. Centralized application configuration management with key-value settings, feature flags, and snapshots. |
| [`azure-appconfiguration-py`](sdks/azure-appconfiguration-py.md) | python | Azure App Configuration SDK for Python. Use for centralized configuration management, feature flags, and dynamic settings. |
| [`azure-appconfiguration-ts`](sdks/azure-appconfiguration-ts.md) | typescript | Centralized configuration management with feature flags and dynamic refresh. |


## eventgrid

| SDK | Language | Purpose |
| --- | --- | --- |
| [`azure-eventgrid-dotnet`](sdks/azure-eventgrid-dotnet.md) | dotnet | Azure Event Grid SDK for .NET. Client library for publishing and consuming events with Azure Event Grid. Use for event-driven architectures, pub/sub messaging, CloudEvents, and EventGridEvents. |
| [`azure-eventgrid-java`](sdks/azure-eventgrid-java.md) | java | Build event-driven applications with Azure Event Grid SDK for Java. Use when publishing events, implementing pub/sub patterns, or integrating with Azure services via events. |
| [`azure-eventgrid-py`](sdks/azure-eventgrid-py.md) | python | Azure Event Grid SDK for Python. Use for publishing events, handling CloudEvents, and event-driven architectures. |


## search

| SDK | Language | Purpose |
| --- | --- | --- |
| [`azure-search-documents-dotnet`](sdks/azure-search-documents-dotnet.md) | dotnet | Azure AI Search SDK for .NET (Azure.Search.Documents). Use for building search applications with full-text, vector, semantic, and hybrid search. |
| [`azure-search-documents-py`](sdks/azure-search-documents-py.md) | python | Azure AI Search SDK for Python. Use for vector search, hybrid search, semantic ranking, indexing, and skillsets. |
| [`azure-search-documents-ts`](sdks/azure-search-documents-ts.md) | typescript | Build search applications with vector, hybrid, and semantic search capabilities. |


## security

| SDK | Language | Purpose |
| --- | --- | --- |
| [`azure-security-keyvault-keys-dotnet`](sdks/azure-security-keyvault-keys-dotnet.md) | dotnet | Azure Key Vault Keys SDK for .NET. Client library for managing cryptographic keys in Azure Key Vault and Managed HSM. Use for key creation, rotation, encryption, decryption, signing, and verification. |
| [`azure-security-keyvault-keys-java`](sdks/azure-security-keyvault-keys-java.md) | java | Azure Key Vault Keys Java SDK for cryptographic key management. Use when creating, managing, or using RSA/EC keys, performing encrypt/decrypt/sign/verify operations, or working with HSM-backed keys. |
| [`azure-security-keyvault-secrets-java`](sdks/azure-security-keyvault-secrets-java.md) | java | Azure Key Vault Secrets Java SDK for secret management. Use when storing, retrieving, or managing passwords, API keys, connection strings, or other sensitive configuration data. |


## data

| SDK | Language | Purpose |
| --- | --- | --- |
| [`azure-data-tables-java`](sdks/azure-data-tables-java.md) | java | Build table storage applications using the Azure Tables SDK for Java. Works with both Azure Table Storage and Cosmos DB Table API. |
| [`azure-data-tables-py`](sdks/azure-data-tables-py.md) | python | Azure Tables SDK for Python (Storage and Cosmos DB). Use for NoSQL key-value storage, entity CRUD, and batch operations. |


## functions

| SDK | Language | Purpose |
| --- | --- | --- |
| [`azure-functions`](sdks/azure-functions.md) | guide | Expert patterns for Azure Functions development including isolated worker model, Durable Functions orchestration, cold start optimization, and production patterns. Covers .NET, Python, and Node.js programming models. |
| [`azure-functions-devsec`](sdks/azure-functions-devsec.md) | guide | Build serverless applications on Azure Functions. Configure triggers, |


## messaging

| SDK | Language | Purpose |
| --- | --- | --- |
| [`azure-messaging-webpubsub-java`](sdks/azure-messaging-webpubsub-java.md) | java | Build real-time web applications with Azure Web PubSub SDK for Java. Use when implementing WebSocket-based messaging, live updates, chat applications, or server-to-client push notifications. |
| [`azure-messaging-webpubsubservice-py`](sdks/azure-messaging-webpubsubservice-py.md) | python | Azure Web PubSub Service SDK for Python. Use for real-time messaging, WebSocket connections, and pub/sub patterns. |


## aks

| SDK | Language | Purpose |
| --- | --- | --- |
| [`azure-aks`](sdks/azure-aks.md) | guide | Deploy and manage Azure Kubernetes Service clusters. Configure node pools, |


## compute

| SDK | Language | Purpose |
| --- | --- | --- |
| [`azure-compute-batch-java`](sdks/azure-compute-batch-java.md) | java | Azure Batch SDK for Java. Run large-scale parallel and HPC batch jobs with pools, jobs, tasks, and compute nodes. |


## containerregistry

| SDK | Language | Purpose |
| --- | --- | --- |
| [`azure-containerregistry-py`](sdks/azure-containerregistry-py.md) | python | Azure Container Registry SDK for Python. Use for managing container images, artifacts, and repositories. |


## devops

| SDK | Language | Purpose |
| --- | --- | --- |
| [`azure-devops`](sdks/azure-devops.md) | guide | Set up Azure Pipelines for CI/CD, configure build and release pipelines, |


## maps

| SDK | Language | Purpose |
| --- | --- | --- |
| [`azure-maps-search-dotnet`](sdks/azure-maps-search-dotnet.md) | dotnet | Azure Maps SDK for .NET. Location-based services including geocoding, routing, rendering, geolocation, and weather. Use for address search, directions, map tiles, IP geolocation, and weather data. |


## networking

| SDK | Language | Purpose |
| --- | --- | --- |
| [`azure-networking`](sdks/azure-networking.md) | guide | Configure Azure VNets, NSGs, and Azure Firewall. Implement hub-spoke |


## playwright

| SDK | Language | Purpose |
| --- | --- | --- |
| [`azure-microsoft-playwright-testing-ts`](sdks/azure-microsoft-playwright-testing-ts.md) | typescript | Run Playwright tests at scale with cloud-hosted browsers and integrated Azure portal reporting. |


## postgres

| SDK | Language | Purpose |
| --- | --- | --- |
| [`azure-postgres-ts`](sdks/azure-postgres-ts.md) | typescript | Connect to Azure Database for PostgreSQL Flexible Server from Node.js/TypeScript using the pg (node-postgres) package. |


## speech

| SDK | Language | Purpose |
| --- | --- | --- |
| [`azure-speech-to-text-rest-py`](sdks/azure-speech-to-text-rest-py.md) | python | Azure Speech to Text REST API for short audio (Python). Use for simple speech recognition of audio files up to 60 seconds without the Speech SDK. |


## sql

| SDK | Language | Purpose |
| --- | --- | --- |
| [`azure-sql`](sdks/azure-sql.md) | guide | Provision Azure SQL Database and Cosmos DB. Configure security, backups, |


## vms

| SDK | Language | Purpose |
| --- | --- | --- |
| [`azure-vms`](sdks/azure-vms.md) | guide | Manage Azure Virtual Machines and scale sets. Configure availability |


## web

| SDK | Language | Purpose |
| --- | --- | --- |
| [`azure-web-pubsub-ts`](sdks/azure-web-pubsub-ts.md) | typescript | Real-time messaging with WebSocket connections and pub/sub patterns. |

