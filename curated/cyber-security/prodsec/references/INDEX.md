# Control index

145 controls. Category -> subcategory -> control. Load only the controls for the target.

| Category | Controls |
| --- | --- |
| `secure_development` | 117 |
| `security_testing` | 17 |
| `security_auditing` | 7 |
| `developer_tooling` | 4 |

## secure_development

### agent

| Control | What it enforces |
| --- | --- |
| [`agent-identity`](controls/agent-identity.md) | Enforce that AI agents have their own identity separate from human users. Use when designing, building, or reviewing agent identity management, agent authentication, or agent permission models. |
| [`agent-to-agent-auth`](controls/agent-to-agent-auth.md) | Enforce SPIFFE/SPIRE plus mTLS for agent-to-agent communication. Use when designing, building, or reviewing authentication between AI agents or multi-agent systems. |
| [`agent-to-mcp-server-auth`](controls/agent-to-mcp-server-auth.md) | Enforce authentication for agents connecting to MCP servers via MCP clients. Use when designing or reviewing how AI agents authenticate to MCP servers. |

### ai-systems

| Control | What it enforces |
| --- | --- |
| [`ai-systems-security`](controls/ai-systems-security.md) | Secure AI-powered products and infrastructure. Use when integrating LLM APIs, deploying model-serving infrastructure, building agent workflows, connecting MCP servers, or reviewing AI system architecture for security gaps. |

### api-gateway

| Control | What it enforces |
| --- | --- |
| [`authentication-enforcement`](controls/authentication-enforcement.md) | Enforce authentication and authorization at the API gateway for AI systems. Use when designing, building, or reviewing API gateways that front inference engines, LLM APIs, or AI model endpoints. |
| [`internal-application-routing`](controls/internal-application-routing.md) | Route internal application traffic through the API gateway for AI systems. Use when designing AI system architecture or reviewing network topology for inference engines and model endpoints. |
| [`rate-limiting`](controls/rate-limiting.md) | Enforce rate limiting at the API gateway to protect AI models from extraction attacks. Use when designing, building, or reviewing API gateways that protect inference engines or LLM endpoints. |
| [`request-validation`](controls/request-validation.md) | Enforce request validation and filtering at the API gateway for AI systems. Use when designing, building, or reviewing API gateways that protect inference engines, guardrails, or prompt orchestrators. |

### api-keys

| Control | What it enforces |
| --- | --- |
| [`avoid-api-keys`](controls/avoid-api-keys.md) | Avoid using API keys in production AI systems. Use when reviewing authentication mechanisms, designing production deployments, or auditing credential management in AI and agentic systems. |

### authorization-server

| Control | What it enforces |
| --- | --- |
| [`client-metadata-support`](controls/client-metadata-support.md) | Support OAuth Client ID Metadata Documents in authorization servers. Use when building or reviewing authorization server client validation and registration mechanisms for MCP ecosystems. |
| [`discovery-mechanism`](controls/discovery-mechanism.md) | Enforce authorization server metadata discovery for MCP ecosystems. Use when configuring or reviewing authorization server endpoint publication and discovery metadata. |
| [`dynamic-client-registration`](controls/dynamic-client-registration.md) | Support OAuth 2.0 Dynamic Client Registration in authorization servers. Use when building or reviewing authorization server client management for MCP ecosystems. |
| [`oauth21-implementation`](controls/oauth21-implementation.md) | Enforce OAuth 2.1 implementation in authorization servers for MCP ecosystems. Use when building, configuring, or reviewing authorization servers that serve MCP clients and servers. |

### cloud-infrastructure

| Control | What it enforces |
| --- | --- |
| [`aws-security`](controls/aws-security.md) | Enforce AWS security baselines for IAM, networking, logging, and managed services like RDS. Use when building, reviewing, or auditing AWS infrastructure, IAM policies, VPC configuration, or RDS deployments. |
| [`database-security`](controls/database-security.md) | Enforce database security for schema design, access control, encryption, and operational hardening. Use when building, reviewing, or auditing database schemas, connection handling, credential management, or database deployment configuration. |

### container-security

| Control | What it enforces |
| --- | --- |
| [`secdevai-oci-image-security`](controls/secdevai-oci-image-security.md) | Analyze OCI container images for security vulnerabilities, misconfigurations, supply chain risks, and hardening gaps. Use when reviewing container images from Red Hat, Quay.io, Docker Hub, or any OCI-compliant registry. Covers CVE analysis, config security, EOL component detection, credential exposu |

### crypto

| Control | What it enforces |
| --- | --- |
| [`algorithm-selection`](controls/algorithm-selection.md) | Apply when selecting, reviewing, or configuring cryptographic algorithms, cipher suites, protocol versions, or key exchange mechanisms. Covers banned/deprecated/recommended algorithms, post-quantum readiness, key management, and OpenSSL API migration. |
| [`constant-time-analysis`](controls/constant-time-analysis.md) | Detects timing side-channel vulnerabilities in cryptographic code. Use when implementing or reviewing crypto code, encountering division on secrets, secret-dependent branches, or constant-time programming questions in C, C++, Go, Rust, Swift, Java, Kotlin, C#, PHP, JavaScript, TypeScript, Python, or |
| [`constant-time-testing`](controls/constant-time-testing.md) | Constant-time testing detects timing side channels in cryptographic code. Use when auditing crypto implementations for timing vulnerabilities. |
| [`crypto-protocol-diagram`](controls/crypto-protocol-diagram.md) | Extracts protocol message flow from source code, RFCs, academic papers, pseudocode, informal prose, ProVerif (.pv), or Tamarin (.spthy) models and generates Mermaid sequenceDiagrams with cryptographic annotations. Use when diagramming a crypto protocol, visualizing a handshake or key exchange flow,  |
| [`fips-compliance`](controls/fips-compliance.md) | Enforce FIPS 140-2/140-3 compliance for RHEL, OpenShift, and Go workloads. Use when building, configuring, reviewing, or auditing systems that require FIPS-validated cryptographic modules, RHEL crypto-policy enforcement, FIPS-ready Go binaries, or FIPS-mode kernel and cluster configuration. |
| [`mermaid-to-proverif`](controls/mermaid-to-proverif.md) | Translates Mermaid sequenceDiagrams describing cryptographic protocols into ProVerif formal verification models (.pv files). Use when generating a ProVerif model, formally verifying a protocol, converting a Mermaid diagram to ProVerif, verifying protocol security properties (secrecy, authentication, |
| [`vector-forge`](controls/vector-forge.md) | Mutation-driven test vector generation. Finds implementations of a cryptographic algorithm or protocol, runs mutation testing to identify escaped mutants, then generates new test vectors that deliberately exercise the uncovered code paths. Compares before/after mutation kill rates to prove vector ef |
| [`wycheproof`](controls/wycheproof.md) | Wycheproof provides test vectors for validating cryptographic implementations. Use when testing crypto code for known attacks and edge cases. |
| [`zeroize-audit`](controls/zeroize-audit.md) | Detects missing zeroization of sensitive data in source code and identifies zeroization removed by compiler optimizations, with assembly-level analysis, and control-flow verification. Use for auditing C/C++/Rust code handling secrets, keys, passwords, or other sensitive data. |

### eval-sandbox

| Control | What it enforces |
| --- | --- |
| [`output-validation-sandbox`](controls/output-validation-sandbox.md) | Validate model outputs in an isolated sandbox before execution or delivery. Use when designing AI systems that generate executable code, API calls, or actions that require safety validation. |

### external-data-source

| Control | What it enforces |
| --- | --- |
| [`authentication`](controls/authentication.md) | Enforce standard authentication for external data source connections. Use when integrating, configuring, or reviewing connections from AI systems to external databases, APIs, or data services. |
| [`authorization`](controls/authorization.md) | Enforce authorization checks for external data source access in AI systems. Use when designing, configuring, or reviewing access controls between AI components and external databases or data services. |
| [`encrypted-communication`](controls/encrypted-communication.md) | Enforce encrypted communication with external data sources. Use when designing, configuring, or reviewing network connections between AI systems and external databases, APIs, or data services. |
| [`logging`](controls/logging.md) | Enforce logging of access to sensitive external data sources in AI systems. Use when designing, building, or reviewing audit and logging capabilities for AI systems accessing external databases or data services. |
| [`network-acls`](controls/network-acls.md) | Enforce network ACLs for external data source access in AI systems. Use when designing, configuring, or reviewing network security for connections between AI components and external databases or data services. |
| [`redis-elasticache-security`](controls/redis-elasticache-security.md) | Secure Redis and Amazon ElastiCache for Redis deployments with authentication, encryption, and network isolation. Use when building, reviewing, or auditing Redis cache configuration, ElastiCache clusters, or application-to-cache connectivity. |

### guardrails

| Control | What it enforces |
| --- | --- |
| [`bidirectional-filtering`](controls/bidirectional-filtering.md) | Deploy runtime guardrails for bidirectional prompt and response filtering in AI systems. Use when designing, building, or reviewing AI architectures that need prompt injection protection, content filtering, or input/output safety controls. |

### inference-engine

| Control | What it enforces |
| --- | --- |
| [`isolation-sandboxing`](controls/isolation-sandboxing.md) | Enforce isolation and sandboxing of inference engine execution. Use when deploying, configuring, or reviewing inference engines like vLLM that load and serve AI models, especially third-party models. |
| [`jwt-token-enforcement`](controls/jwt-token-enforcement.md) | Enforce short-lived JWT access token validation for inference engines. Use when implementing or reviewing token validation, access control, or request authentication in inference engine endpoints. |
| [`model-security-scanning`](controls/model-security-scanning.md) | Scan AI models for malicious elements before loading in inference engines. Use when building or reviewing inference engines, model loading pipelines, or model distribution systems. |
| [`model-signature-verification`](controls/model-signature-verification.md) | Verify model signatures before loading in inference engines. Use when building, configuring, or reviewing inference engines that load AI models, or when designing model distribution pipelines. |
| [`oidc-integration`](controls/oidc-integration.md) | Enforce OIDC IdP integration for inference engines. Use when designing, building, or reviewing authentication for inference engines, LLM APIs, or AI model serving endpoints. |
| [`reject-api-keys`](controls/reject-api-keys.md) | Reject raw API key authentication in inference engines. Use when designing, reviewing, or auditing authentication mechanisms for inference engines or LLM API endpoints in production environments. |
| [`token-lifecycle`](controls/token-lifecycle.md) | Enforce token rotation, revocation, and replay prevention for inference engines. Use when implementing or reviewing refresh token handling, token revocation, or replay protection in inference engine authentication. |

### kubernetes

| Control | What it enforces |
| --- | --- |
| [`container-hardening`](controls/container-hardening.md) | Harden container images and runtime configuration. Use when building, reviewing, or auditing Containerfiles, Dockerfiles, container compose files, or Kubernetes pod security settings. |
| [`cpu-performance`](controls/cpu-performance.md) | Configure CPU isolation, scheduling policies, storage provisioning, and image pull policies for latency-sensitive Kubernetes workloads. Use when writing, reviewing, or auditing pod specs for telco, far-edge, or real-time workloads that require deterministic CPU performance. |
| [`health-probes`](controls/health-probes.md) | Configure Kubernetes health probes, lifecycle hooks, and termination policies. Use when writing, reviewing, or auditing pod specs, Deployments, StatefulSets, or Helm templates that define liveness, readiness, startup probes, postStart/preStop hooks, or terminationMessagePolicy. |
| [`helm-chart-security`](controls/helm-chart-security.md) | Secure Helm chart development, dependency management, and secret handling. Use when building, reviewing, or auditing Helm charts, values files, Chart.yaml dependencies, or Helm-based deployment pipelines. |
| [`linux-capabilities`](controls/linux-capabilities.md) | Review and restrict Linux capabilities in Kubernetes containers. Use when writing, reviewing, or auditing pod security contexts that add or drop Linux capabilities such as BPF, NET_ADMIN, NET_RAW, SYS_ADMIN, IPC_LOCK, SYS_NICE, or SYS_PTRACE. |
| [`network-security`](controls/network-security.md) | Configure Kubernetes network security including host access restrictions, network policies, port management, and connectivity requirements. Use when writing, reviewing, or auditing pod specs, Services, NetworkPolicies, or NetworkAttachmentDefinitions. |
| [`observability`](controls/observability.md) | Configure Kubernetes workload observability including container logging, CRD status reporting, port naming conventions, image tagging, and API compatibility. Use when writing, reviewing, or auditing CRDs, container specs, Services, or preparing for OpenShift version upgrades. |
| [`operator-security`](controls/operator-security.md) | Enforce least-privilege RBAC and secure runtime configuration for Kubernetes Operators. Use when building, reviewing, or auditing Operator manifests, ClusterRoles, Roles, OLM bundles, or CRD definitions. |
| [`platform-integrity`](controls/platform-integrity.md) | Validate Kubernetes platform configuration including boot parameters, hugepages, kernel state, sysctl settings, OpenShift lifecycle, and service mesh compliance. Use when auditing cluster node configuration or preparing for platform upgrades. |
| [`pod-access-control`](controls/pod-access-control.md) | Configure Kubernetes RBAC bindings, service accounts, namespaces, resource quotas, and service types for pods. Use when writing, reviewing, or auditing Deployments, ServiceAccounts, Roles, RoleBindings, ResourceQuotas, or Services for least-privilege access control. |
| [`scc-security`](controls/scc-security.md) | Review OpenShift Security Context Constraints for correct privilege levels. Use when auditing pod security, reviewing SCC assignments, or configuring container runtime permissions on OpenShift clusters. |
| [`tls-compliance`](controls/tls-compliance.md) | Enforce TLS compliance for Kubernetes and OpenShift workloads. Use when configuring, reviewing, or auditing TLS settings on Ingress controllers, Routes, Services, or application endpoints for TLS version enforcement, certificate validation, and post-quantum readiness. |
| [`workload-resilience`](controls/workload-resilience.md) | Configure Kubernetes workload resilience including pod scheduling, scaling, high availability, and disruption budgets. Use when writing, reviewing, or auditing Deployments, StatefulSets, CRDs, or any workload that requires scaling, anti-affinity, topology spread, or PodDisruptionBudgets. |

### languages

| Control | What it enforces |
| --- | --- |
| [`compiler-hardening`](controls/compiler-hardening.md) | Apply compiler hardening flags and sanitizers to C/C++ builds. Use when reviewing build configurations, CI pipelines, or Makefiles/CMakeLists for native code projects. |
| [`go-security`](controls/go-security.md) | Enforce secure coding practices in Go applications. Use when building, reviewing, or auditing Go code that handles user input, database access, cryptography, TLS, or uses unsafe/cgo. |
| [`safe-c-functions`](controls/safe-c-functions.md) | Apply when reviewing or writing C/C++ code that uses memory or string operations. Identifies banned functions, provides safe replacements, compiler hardening flags, and refactoring examples. |

### large-language-model

| Control | What it enforces |
| --- | --- |
| [`file-protection`](controls/file-protection.md) | Protect LLM model files against unauthorized access and modification. Use when designing, deploying, or reviewing storage and access controls for AI model files and weights. |
| [`prompt-injection-mitigation`](controls/prompt-injection-mitigation.md) | Mitigate prompt injection risks in LLM-based systems. Use when designing, building, or reviewing AI systems that accept user prompts, or when evaluating model safety for deployment. |
| [`third-party-model-security`](controls/third-party-model-security.md) | Secure the use of third-party AI models hosted in the cloud. Use when integrating, configuring, or reviewing connections to third-party model endpoints like OpenAI, Anthropic, or other hosted LLM services. |

### mcp-client

| Control | What it enforces |
| --- | --- |
| [`discovery-mechanisms`](controls/discovery-mechanisms.md) | Enforce support for OAuth 2.0 and OIDC discovery mechanisms in MCP clients. Use when building, configuring, or reviewing MCP client authentication and authorization server discovery. |
| [`mcp-client-client-metadata-support`](controls/mcp-client-client-metadata-support.md) | Support OAuth Client ID Metadata Documents in MCP clients. Use when building or reviewing MCP client registration and identity presentation to authorization servers. |
| [`mcp-client-dynamic-client-registration`](controls/mcp-client-dynamic-client-registration.md) | Support OAuth 2.0 Dynamic Client Registration in MCP clients. Use when building or reviewing MCP client registration with authorization servers that support dynamic registration. |
| [`mcp-client-protected-resource-metadata`](controls/mcp-client-protected-resource-metadata.md) | Enforce use of OAuth 2.0 Protected Resource Metadata in MCP clients for discovering authorization servers. Use when building or reviewing MCP client authentication flows and authorization server discovery. |
| [`oauth-scopes-handling`](controls/oauth-scopes-handling.md) | Handle OAuth scopes in MCP clients according to the WWW-Authenticate header and Protected Resource Metadata discovery flow. Use when building or reviewing MCP client authorization flows, scope negotiation, or permission handling. |

### mcp-server

| Control | What it enforces |
| --- | --- |
| [`consent-and-scoping`](controls/consent-and-scoping.md) | Enforce granular OAuth scopes and explicit user consent in MCP servers. Use when designing, building, or reviewing MCP server permission models, scope definitions, or consent flows. |
| [`containerization`](controls/containerization.md) | Enforce container security best practices for MCP servers, including OpenShift integration. Use when containerizing MCP servers or reviewing container security configurations for MCP deployments. |
| [`external-idp-integration`](controls/external-idp-integration.md) | Enforce MCP server integration with external centralized identity providers. Use when building, configuring, or reviewing MCP server authentication against external IdPs like Keycloak. |
| [`hardening-local`](controls/hardening-local.md) | Harden locally deployed MCP servers against network exposure and host compromise. Use when building, deploying, or reviewing MCP servers that run on a user's local machine. |
| [`hardening-remote`](controls/hardening-remote.md) | Harden remotely deployed MCP servers with TLS, network segmentation, and server verification. Use when deploying, configuring, or reviewing MCP servers running as remote services. |
| [`input-output-sanitization`](controls/input-output-sanitization.md) | Enforce input and output sanitization in MCP servers. Use when building or reviewing MCP server request handling, tool invocation, or response processing. |
| [`logging-and-observability`](controls/logging-and-observability.md) | Enforce centralized structured logging and audit trails in MCP servers. Use when building, configuring, or reviewing MCP server logging, observability, or audit capabilities. |
| [`no-credential-forwarding`](controls/no-credential-forwarding.md) | Prevent MCP servers from forwarding user credentials or tokens to downstream tools. Use when building, reviewing, or auditing MCP server integrations with external tools or APIs. |
| [`oauth21-resource-server`](controls/oauth21-resource-server.md) | Enforce MCP servers to act as OAuth 2.1 resource servers by default. Use when building, configuring, or reviewing MCP server authentication and authorization defaults. |
| [`os-tool-security`](controls/os-tool-security.md) | Enforce least privilege and sandboxing for MCP server OS tool execution. Use when building, configuring, or reviewing MCP servers that execute operating system commands or local tools. |
| [`protected-resource-metadata`](controls/protected-resource-metadata.md) | Enforce OAuth 2.0 Protected Resource Metadata implementation in MCP servers. Use when building, configuring, or reviewing MCP server authentication and authorization discovery. |
| [`rbac`](controls/rbac.md) | Implement role-based access control in MCP servers by mapping token claims to internal roles. Use when building or reviewing MCP server authorization, permission models, or access control enforcement. |
| [`roots-support`](controls/roots-support.md) | Enforce roots directive support in MCP servers. Use when building or reviewing MCP server filesystem access, directory scoping, or path boundary enforcement. |
| [`runtime-restrictions`](controls/runtime-restrictions.md) | Enforce timeouts and rate limiting in MCP servers to prevent abuse and DoS. Use when building, configuring, or reviewing MCP server runtime controls, resource limits, or abuse prevention. |
| [`sampling-controls`](controls/sampling-controls.md) | Control and restrict MCP server use of sampling. Use when building or reviewing MCP servers that might use sampling to request LLM completions from clients. |
| [`secure-token-handling`](controls/secure-token-handling.md) | Enforce secure token validation and storage in MCP servers. Use when implementing or reviewing token handling, JWT validation, or token storage in MCP servers. |
| [`token-exchange-for-tools`](controls/token-exchange-for-tools.md) | Implement OAuth Token Exchange in MCP servers for secure downstream API access. Use when designing or reviewing how MCP servers authenticate to third-party APIs or web tools. |
| [`tool-server-injection-prevention`](controls/tool-server-injection-prevention.md) | Prevent tool and server injection attacks (rug-pulls) in MCP servers. Use when building, distributing, or reviewing MCP server update mechanisms, versioning, or integrity verification. |

### messaging

| Control | What it enforces |
| --- | --- |
| [`kafka-amq-security`](controls/kafka-amq-security.md) | Secure Kafka and AMQ Streams deployments with encryption, authentication, and authorization. Use when building, reviewing, or auditing Kafka broker configuration, AMQ Streams custom resources, or Kafka client connectivity. |
| [`mqtt-security`](controls/mqtt-security.md) | Secure MQTT broker and client deployments with authentication, topic ACLs, and transport encryption. Use when building, reviewing, or auditing MQTT broker configuration, client connectivity, or IoT messaging security. |

### model-registry

| Control | What it enforces |
| --- | --- |
| [`admin-interface-security`](controls/admin-interface-security.md) | Secure the administrative interface of model registries. Use when building, deploying, or reviewing model registry access controls and admin interfaces. |
| [`model-registry-logging`](controls/model-registry-logging.md) | Enforce centralized security logging for model registries. Use when building, configuring, or reviewing logging and audit capabilities of model registries. |
| [`model-registry-model-security-scanning`](controls/model-registry-model-security-scanning.md) | Scan models for malicious code in model registries. Use when building, configuring, or reviewing model registry security, model ingestion pipelines, or model validation workflows. |
| [`model-registry-model-signature-verification`](controls/model-registry-model-signature-verification.md) | Verify model signatures in model registries to validate provenance. Use when building, configuring, or reviewing model registries, model upload pipelines, or model distribution workflows. |
| [`model-registry-secure-storage`](controls/model-registry-secure-storage.md) | Enforce authenticated and authorized access to model registry storage. Use when deploying, configuring, or reviewing the storage backend for model registries. |

### rag-system

| Control | What it enforces |
| --- | --- |
| [`secure-storage`](controls/secure-storage.md) | Protect RAG system data against unauthorized access and modification. Use when designing, deploying, or reviewing Retrieval-Augmented Generation systems, vector databases, or knowledge base storage. |

### secrets-detection

| Control | What it enforces |
| --- | --- |
| [`secrets-detection-patterns`](controls/secrets-detection-patterns.md) | Detect hardcoded secrets in source code using pattern-based scanning for API keys, tokens, passwords, private keys, and connection strings. Use before committing, during code review, or for post-incident history scanning. Self-contained — no external tools required. |

### secure-config

| Control | What it enforces |
| --- | --- |
| [`agentic-actions-auditor`](controls/agentic-actions-auditor.md) | Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations including Claude Code Action, Gemini CLI, OpenAI Codex, and GitHub AI Inference. Detects attack vectors where attacker-controlled input reaches AI agents running in CI/CD pipelines, including env var intermediary p |
| [`apache-camel-security`](controls/apache-camel-security.md) | Secure Apache Camel route deployments across endpoint, payload, route, and configuration layers. Use when building, reviewing, or auditing Camel routes, integration pipelines, or Camel-based microservices. |
| [`build-yaml-misconfiguration`](controls/build-yaml-misconfiguration.md) | Apply when reviewing or writing GitLab CI (.gitlab-ci.yml), Tekton pipeline/task YAML, or Containerfiles/Dockerfiles used in CI builds. Detects common misconfigurations that expose secrets, weaken isolation, skip security gates, grant excessive privileges, or produce insecure container images. |
| [`insecure-defaults`](controls/insecure-defaults.md) | Detects fail-open insecure defaults (hardcoded secrets, weak auth, permissive security) that allow apps to run insecurely in production. Use when auditing security, reviewing config management, or analyzing environment variable handling. |
| [`sharp-edges`](controls/sharp-edges.md) | Identifies error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes. Use when reviewing API designs, configuration schemas, cryptographic library ergonomics, or evaluating whether code follows 'secure by default' and 'pit of success' principles. Triggers: footgun |

### security-principles

| Control | What it enforces |
| --- | --- |
| [`defense-in-depth`](controls/defense-in-depth.md) | Apply defense-in-depth by layering multiple independent security controls. Use when reviewing system architecture, evaluating whether a single control is the only barrier, or assessing blast radius of a component compromise. |
| [`least-privilege-and-mediation`](controls/least-privilege-and-mediation.md) | Enforce least privilege and complete mediation in access control design. Use when reviewing authorization models, RBAC configurations, API access controls, or evaluating whether every request is authorized before access is granted. |
| [`secure-by-design`](controls/secure-by-design.md) | Apply Secure by Design, by Default, and in Deployment (SD3) principles. Use when reviewing default configurations, setup processes, update mechanisms, or evaluating whether a system fails open or closed. |
| [`simplicity-and-isolation`](controls/simplicity-and-isolation.md) | Apply economy of mechanism and least common mechanism to reduce attack surface through simplicity and component isolation. Use when reviewing system architecture for unnecessary complexity, shared resources, or single points of failure. |
| [`transparency-and-usability`](controls/transparency-and-usability.md) | Apply open design, psychological acceptability, and compromise recording to build transparent, usable, and observable security. Use when reviewing whether security relies on obscurity, whether controls are usable, or whether breach detection and response capabilities exist. |

### spiffe-spire

| Control | What it enforces |
| --- | --- |
| [`service-to-service-mtls`](controls/service-to-service-mtls.md) | Enforce SPIFFE/SPIRE plus mTLS for service-to-service authentication. Use when designing, building, or reviewing authentication between services, workloads, or machines in AI systems. |

### supply-chain

| Control | What it enforces |
| --- | --- |
| [`dependency-vulnerability-audit`](controls/dependency-vulnerability-audit.md) | Supply chain security audit using CLI vulnerability scanners, license compliance checks, and supply chain risk assessment. Use when auditing project dependencies for known CVEs, license concerns, and supply chain health. |
| [`sbom-provenance`](controls/sbom-provenance.md) | Generate Software Bill of Materials (SBOM) for AI software releases. Use when building release pipelines, reviewing supply chain security, or preparing compliance documentation for AI systems. |
| [`secure-pipeline`](controls/secure-pipeline.md) | Enforce SAST and SCA in CI/CD pipelines for AI software. Use when building, configuring, or reviewing CI/CD pipelines for MCP servers, inference engines, or any AI system components. |
| [`software-signing`](controls/software-signing.md) | Enforce digital signing of software binaries and container images. Use when building, releasing, or reviewing CI/CD pipelines for AI software, MCP servers, or any distributed components. |
| [`supply-chain-risk-auditor`](controls/supply-chain-risk-auditor.md) | Identifies dependencies at heightened risk of exploitation or takeover. Use when assessing supply chain attack surface, evaluating dependency health, or scoping security engagements. |
| [`vulnerability-management`](controls/vulnerability-management.md) | Enforce vulnerability management and patching for AI software dependencies. Use when planning, implementing, or reviewing vulnerability response processes for MCP servers, inference engines, or AI system components. |

### web-security

| Control | What it enforces |
| --- | --- |
| [`client-side-security`](controls/client-side-security.md) | Apply when reviewing or writing browser-facing code that handles user input, renders HTML, sets cookies, or loads third-party scripts. Covers XSS, CSRF, CSP, clickjacking, XS-Leaks, and HTTP security headers. |
| [`file-handling-uploads`](controls/file-handling-uploads.md) | Apply when reviewing or writing code that accepts file uploads, processes user-supplied files, or serves stored files. Covers extension validation, content verification, filename security, storage isolation, and scanning. |
| [`graphql-security`](controls/graphql-security.md) | Secure GraphQL API deployments against introspection leaks, deep query abuse, and authorization bypass. Use when building, reviewing, or auditing GraphQL schemas, resolvers, or gateway configurations. |
| [`http-security-headers`](controls/http-security-headers.md) | Verify and configure HTTP response security headers. Use when reviewing web server configuration, reverse proxy setup, or application middleware that sets response headers. |
| [`input-validation-injection`](controls/input-validation-injection.md) | Apply when reviewing or writing code that processes untrusted input, constructs queries or commands, or handles user-supplied data. Covers SQL, LDAP, OS command injection, prototype pollution, and general validation strategy. |
| [`react-security`](controls/react-security.md) | Enforce XSS prevention and secure rendering in React applications. Use when building, reviewing, or auditing React components, especially those that render user-controlled data or use server-side rendering. |
| [`session-management-cookies`](controls/session-management-cookies.md) | Apply when reviewing or writing code that creates, stores, or validates user sessions or sets cookies. Covers session ID generation, cookie security, rotation, timeouts, theft detection, and client-side storage restrictions. |
| [`web-application-security`](controls/web-application-security.md) | Review web application security controls against OWASP-aligned risks. Use when building, auditing, or reviewing server-side web applications that handle user input, sessions, authentication, or access control. |
| [`xml-serialization-security`](controls/xml-serialization-security.md) | Apply when reviewing or writing code that parses XML, processes DTDs, transforms XSLT, or deserializes data from untrusted sources. Covers XXE prevention, entity expansion, parser hardening, and safe deserialization per language. |


## security_testing

### fuzzing

| Control | What it enforces |
| --- | --- |
| [`address-sanitizer`](controls/address-sanitizer.md) | AddressSanitizer detects memory errors during fuzzing. Use when fuzzing C/C++ code to find buffer overflows and use-after-free bugs. |
| [`aflpp`](controls/aflpp.md) | AFL++ is a fork of AFL with better fuzzing performance and advanced features. Use for multi-core fuzzing of C/C++ projects. |
| [`atheris`](controls/atheris.md) | Atheris is a coverage-guided Python fuzzer based on libFuzzer. Use for fuzzing pure Python code and Python C extensions. |
| [`cargo-fuzz`](controls/cargo-fuzz.md) | cargo-fuzz is the de facto fuzzing tool for Rust projects using Cargo. Use for fuzzing Rust code with libFuzzer backend. |
| [`coverage-analysis`](controls/coverage-analysis.md) | Coverage analysis measures code exercised during fuzzing. Use when assessing harness effectiveness or identifying fuzzing blockers. |
| [`fuzzing-dictionary`](controls/fuzzing-dictionary.md) | Fuzzing dictionaries guide fuzzers with domain-specific tokens. Use when fuzzing parsers, protocols, or format-specific code. |
| [`fuzzing-obstacles`](controls/fuzzing-obstacles.md) | Techniques for patching code to overcome fuzzing obstacles. Use when checksums, global state, or other barriers block fuzzer progress. |
| [`harness-writing`](controls/harness-writing.md) | Techniques for writing effective fuzzing harnesses across languages. Use when creating new fuzz targets or improving existing harness code. |
| [`libafl`](controls/libafl.md) | LibAFL is a modular fuzzing library for building custom fuzzers. Use for advanced fuzzing needs, custom mutators, or non-standard fuzzing targets. |
| [`libfuzzer`](controls/libfuzzer.md) | Coverage-guided fuzzer built into LLVM for C/C++ projects. Use for fuzzing C/C++ code that can be compiled with Clang. |
| [`ossfuzz`](controls/ossfuzz.md) | OSS-Fuzz provides free continuous fuzzing for open source projects. Use when setting up continuous fuzzing infrastructure or enrolling projects. |
| [`ruzzy`](controls/ruzzy.md) | Ruzzy is a coverage-guided Ruby fuzzer by Trail of Bits. Use for fuzzing pure Ruby code and Ruby C extensions. |

### static-analysis

| Control | What it enforces |
| --- | --- |
| [`codeql`](controls/codeql.md) | Scans a codebase for security vulnerabilities using CodeQL's interprocedural data flow and taint tracking analysis. Triggers on "run codeql", "codeql scan", "codeql analysis", "build codeql database", or "find vulnerabilities with codeql". Supports "run all" (security-and-quality + security-experime |
| [`sarif-parsing`](controls/sarif-parsing.md) | Parses and processes SARIF files from static analysis tools like CodeQL, Semgrep, or other scanners. Triggers on "parse sarif", "read scan results", "aggregate findings", "deduplicate alerts", or "process sarif output". Handles filtering, deduplication, format conversion, and CI/CD integration of SA |
| [`semgrep`](controls/semgrep.md) | Run Semgrep static analysis scan on a codebase using parallel subagents. Supports two scan modes — "run all" (full ruleset coverage) and "important only" (high-confidence security vulnerabilities). Automatically detects and uses Semgrep Pro for cross-file taint analysis when available. Use when aske |
| [`semgrep-rule-creator`](controls/semgrep-rule-creator.md) | Creates custom Semgrep rules for detecting security vulnerabilities, bug patterns, and code patterns. Use when writing Semgrep rules or building custom static analysis detections. |
| [`semgrep-rule-variant-creator`](controls/semgrep-rule-variant-creator.md) | Creates language variants of existing Semgrep rules. Use when porting a Semgrep rule to specified target languages. Takes an existing rule and target languages as input, produces independent rule+test directories for each language. |


## security_auditing

### audit-workflow

| Control | What it enforces |
| --- | --- |
| [`ai-code-review`](controls/ai-code-review.md) | Security-focused review of AI-generated or AI-assisted code. Use when reviewing code produced by AI coding assistants, auditing AI-generated patches, verifying AI-assisted contributions before merge, or when a review needs to account for failure modes specific to AI code generation. |
| [`audit-context-building`](controls/audit-context-building.md) | Enables ultra-granular, line-by-line code analysis to build deep architectural context before vulnerability or bug finding. |
| [`differential-review`](controls/differential-review.md) | Performs security-focused differential review of code changes (PRs, commits, diffs). Adapts analysis depth to codebase size, uses git history for context, calculates blast radius, checks test coverage, and generates comprehensive markdown reports. Automatically detects and prevents security regressi |
| [`fp-check`](controls/fp-check.md) | Systematically verifies suspected security bugs to eliminate false positives. Produces TRUE POSITIVE or FALSE POSITIVE verdicts with documented evidence for each bug. |
| [`secdevai-fix`](controls/secdevai-fix.md) | Apply suggested security fixes from a prior code review. Use when the user wants to remediate security findings with before/after code diffs, severity filtering, and explicit approval before modifying code. |
| [`secdevai-review`](controls/secdevai-review.md) | Use when performing security code review of source files, git commits, or entire codebases against OWASP Top 10 (2021), CWE/SANS Top 25, and OWASP WSTG v4.2 patterns; applicable to any language or framework. |
| [`variant-analysis`](controls/variant-analysis.md) | Find similar vulnerabilities and bugs across codebases using pattern-based analysis. Use when hunting bug variants, building CodeQL/Semgrep queries, analyzing security vulnerabilities, or performing systematic code audits after finding an initial issue. |


## developer_tooling

### testing

| Control | What it enforces |
| --- | --- |
| [`property-based-testing`](controls/property-based-testing.md) | Provides guidance for property-based testing across multiple languages and smart contracts. Use when writing tests, reviewing code with serialization/validation/parsing patterns, designing features, or when property-based testing would provide stronger coverage than example-based tests. |

### tooling

| Control | What it enforces |
| --- | --- |
| [`devcontainer-setup`](controls/devcontainer-setup.md) | Creates devcontainers with language-specific tooling (Python/Node/Rust/Go) and persistent volumes. Use when adding devcontainer support to a project or setting up isolated development environments. |
| [`git-cleanup`](controls/git-cleanup.md) | Use when a user asks to analyze and safely clean up local git branches and worktrees by categorizing them as merged, squash-merged, superseded, or active work before any deletion. |
| [`modern-python`](controls/modern-python.md) | Configures Python projects with modern tooling (uv, ruff, ty). Use when creating projects, writing standalone scripts, or migrating from pip/Poetry/mypy/black. |

