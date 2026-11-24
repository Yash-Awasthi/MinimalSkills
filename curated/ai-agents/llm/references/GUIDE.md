# llm guide

The long-form group prose and the full roster. `SKILL.md` is the loadable hub, and
`references/skills/<skill>.md` is the verbatim body to follow for one task.

### Application patterns

| Skill | What it does |
| --- | --- |
| [`app-patterns`](references/skills/app-patterns.md) | Architecture and integration sketches for LLM applications, with retrieval, tool, privacy, and verification boundaries stated up front. |
| [`application-dev-ai-assistant`](references/skills/application-dev-ai-assistant.md) | Designs a conversational assistant with context management, integration boundaries, a verification plan, and a conceptual playbook. |
| [`application-dev-langchain-agent`](references/skills/application-dev-langchain-agent.md) | LangChain and LangGraph agent patterns for state, memory, RAG, tools, and production serving with async calls and tracing. |
| [`ops`](references/skills/ops.md) | A Portuguese-language LLM operations overview across RAG, embeddings, vector databases, fine-tuning, prompt engineering, cost, evals, caching, and streaming. |

### Security

| Skill | What it does |
| --- | --- |
| [`app-security`](references/skills/app-security.md) | Hardens chatbots, RAG pipelines, and embedded AI features against prompt injection, data leakage, tool abuse, and unsafe output. |
| [`security`](references/skills/security.md) | Authorized assessment of an LLM application or agent across prompt injection, tool abuse, RAG exposure, memory poisoning, and system-prompt extraction. |

### Prompting and output

| Skill | What it does |
| --- | --- |
| [`application-dev-prompt-optimize`](references/skills/application-dev-prompt-optimize.md) | Improves a prompt through task-specific evaluation, structured instructions, regression checks, and a documented before and after. |
| [`prompt-optimizer`](references/skills/prompt-optimizer.md) | Turns a weak prompt into a precise one with role, structure, context, instruction, and format, plus few-shot, chain-of-thought, and compression patterns. |
| [`structured-output`](references/skills/structured-output.md) | Gets typed JSON from OpenAI, Anthropic, and Google APIs through response_format, tool_use, and responseSchema, with schema-driven retries. |

### Cost and caching

| Skill | What it does |
| --- | --- |
| [`caching`](references/skills/caching.md) | Adds exact-match, semantic, gateway, and provider-side prompt caching, with the cache key, tenant scope, invalidation, and metrics defined. |
| [`cost-optimization`](references/skills/cost-optimization.md) | Reduces LLM spend through cost tracking, model right-sizing, prompt caching, batching, and self-hosting, measured against quality and total cost. |
| [`gateway`](references/skills/gateway.md) | Deploys a LiteLLM or Bifrost gateway with virtual keys, rate limits, semantic cache, fallback routing, health checks, and spend tracking. |

### Evaluation and tuning

| Skill | What it does |
| --- | --- |
| [`evaluation`](references/skills/evaluation.md) | Builds automated metric, human review, LLM-as-judge, and A/B evaluation suites with baselines, agreement checks, and guarded statistics. |
| [`fine-tuning`](references/skills/fine-tuning.md) | Sets up QLoRA, LoRA, full fine-tuning, DPO, adapter merging, and Kubernetes training with TRL, Axolotl, and DeepSpeed or FSDP. |

### Council and scaling

| Skill | What it does |
| --- | --- |
| [`council`](references/skills/council.md) | Runs a Fireworks-hosted open-weight model council that selects models, collects all responses, ranks them, and synthesizes a final answer. |
| [`inference-scaling`](references/skills/inference-scaling.md) | Autoscales Kubernetes LLM inference with GPU metrics, KEDA queue scaling, vLLM, and a mixed on-demand and spot node pool. |
## Group notes

### Application patterns

`app-patterns` is the architecture sketch. It names the request path, retrieval, tool
boundaries, privacy controls, and a verification plan, and it asks for provider and SDK
versions, authorized data and tools, request and response schemas, latency and cost
budgets, and the expected task outcome. The detailed guide is bundled and holds the
complete procedure, so read it before executing. The code is an integration sketch with
adapter seams for the model, database, parser, and provider response. Replace each seam
with a tested implementation.

`application-dev-ai-assistant` designs a conversational assistant. Context management,
integration boundaries, requirements, instructions, and a playbook. The playbook is
bundled at `resources/implementation-playbook.md`, and its Python strings are conceptual
rather than a runnable project. Clarify goals, constraints, and inputs first, and stop
when a permission, safety boundary, or success criterion is missing.

`application-dev-langchain-agent` covers LangChain 0.1 and LangGraph. State and graph
structure, model and embedding selection, agent types, memory, a RAG pipeline, tools, a
FastAPI server with streaming, and observability. Use async calls throughout, `ainvoke`,
`astream`, and `aget_relevant_documents`, and trace runs. A suggested embedding model is a
recommendation, not an installed dependency, and a reranker is a separate component.

`ops` is a Portuguese-language operations overview. RAG, embeddings, Pinecone, Chroma, and
pgvector, fine-tuning, advanced prompt engineering, cost, evals, semantic cache, streaming,
and agents. It gives a full RAG architecture, an indexing and query pipeline, vector
database selection, an elite prompt structure, a cost estimate, and an evaluation
framework. Treat every figure as an order of magnitude, and keep its safety limits.

### Security

`app-security` is the defensive build standard. The OWASP LLM Top 10 risk map, input
validation, structural checks, prompt injection detection in Python and Node.js, the
OpenAI moderation API, a full input pipeline, system prompt protection, instruction
hierarchy enforcement, tool and plugin allowlisting, output safety, Presidio PII scrubbing,
a dependency-free PII fallback, and a toxicity classifier. Detection rules are heuristics,
so a match is a review candidate and not a confirmed attack. Never rely on a classifier as
the only control.

`security` is the authorized assessment methodology. Reconnaissance of the AI attack
surface, prompt injection per OWASP LLM01 and ASI01, tool abuse per ASI02, ASI03, and
ASI05, memory and context poisoning per ASI06, output safety per LLM05, and system prompt
extraction per LLM07. It requires explicit written permission and the mandatory
confirmation gate before any probe. Four references are bundled: the agent obedience
engineering guide, the agent security testing guide, the OWASP LLM Top 10 map, and the
prompt injection methodology. A finding needs a reproducible request and a stated impact.

### Prompting and output

`application-dev-prompt-optimize` treats a prompt as a testable artifact. Define the task
and the success criteria, write structured instructions, build a small evaluation set, and
run a regression check against the prior prompt. The implementation playbook is bundled.
Do not declare an improvement without the before and after on the same cases.

`prompt-optimizer` is the technique catalog. Diagnose the weak prompt, then apply the
RSCIT frame of role, structure, context, instruction, and format. Chain-of-thought,
few-shot examples, structured JSON output, hallucination reduction, and prompt compression.
Always state the output format. A compressed prompt is only valid if it preserves the
measured quality, so compare it rather than assuming equivalence.

`structured-output` covers the three provider paths. OpenAI `response_format` with a JSON
Schema and Pydantic or Zod, Anthropic `tool_use` with the data in the `tool_use` block, and
Google `responseSchema`. The core workflow uses a schema-first extractor, a schema-constrained
call, validation, and a bounded retry that feeds the error back. Never use
`response_format: { type: "json_object" }` without a schema. Never parse Anthropic text
blocks for structured data. Never omit field descriptions, and never set
`additionalProperties: true` under strict mode.

### Cost and caching

`caching` builds the layers. Exact match in Redis, semantic match with GPTCache or a
custom store, a gateway-level semantic cache, and provider-side prompt caching for
Anthropic and OpenAI. The cache key includes the tenant and access scope, the model
revision, the system and developer prompts, the conversation and tool context, the
parameters, and the locale. Always filter a semantic cache by model. Partition by tenant
so one customer's answer cannot reach another. Measure hit rate, latency, and spend, and
invalidate on a prompt or model change.

`cost-optimization` starts with tracking. Per-model cost accounting, custom callbacks,
model right-sizing by task, provider prompt caching, the OpenAI Batch API discount,
semantic caching, quantization, and self-hosting. Compare quality and total cost, not
sticker price, because a cheaper model that fails more often can cost more. The price
table in the body is approximate and dated.

`gateway` puts one endpoint in front of many backends. LiteLLM Proxy with a config file, a
Docker Compose stack, virtual keys and per-team rate limits, spend views, Bifrost as an
alternative, an Nginx round-robin in front of vLLM replicas, and health checks. Keep
`proxy_buffering off` for SSE streaming. A fallback chain needs a bound and a terminal
error, or a failing provider loops forever. A gateway concentrates credentials, so protect
its admin surface and rotate keys.

### Evaluation and tuning

`evaluation` builds the suite. Automated metrics such as BLEU, ROUGE, BERTScore, and
custom metrics, human evaluation, LLM-as-judge, and A/B testing. Define the suite and the
test cases, run the baseline, then compare. The body contains a deliberate
`NotImplementedError("A verified fact-checking adapter is required")` where a real adapter
must be supplied, and a guard that raises when a group has fewer than two observations.
Keep both. A judge needs agreement against a human-labeled sample, and a p-value on two
observations is not evidence.

`fine-tuning` covers the training path. QLoRA with 4-bit quantization, LoRA configuration,
Axolotl for production runs, DeepSpeed for multi-GPU, DPO and RLHF alignment data, adapter
merging for vLLM serving, and a Kubernetes training job. Confirm the data rights, consent,
and base model license first. Publishing weights is a separate authorized action after a
license and privacy review. A merged adapter is a new artifact with its own evaluation.

### Council and scaling

`council` runs a Fireworks-hosted open-weight council. Select the models and the chairman,
collect every member response, rank the responses, then synthesize. Always show all
individual responses, all rankings, and the final synthesis, and never skip the ranking
phase. The model table and the question-tool syntax in the body are examples. Verify the
account's current model IDs, obtain authorization for metered calls, and use the host's
supported input mechanism. The detailed guide is bundled, and `references/assets/council/`
also carries `.env.example`.

`inference-scaling` autoscales GPU inference on Kubernetes. The NVIDIA GPU operator, a
vLLM deployment with GPU resources, KEDA on Prometheus metrics, queue-based scaling with
Redis, a ScaledJob for async batch work, a mixed on-demand and spot node pool with node
affinity, the cluster autoscaler, and the metrics that drive a scale decision. Watch the
vLLM queue depth and KV cache utilization rather than only GPU percent. Spot GPUs are
evicted, so keep an on-demand floor and a drain path. A manifest that was not applied to a
cluster is untested.
