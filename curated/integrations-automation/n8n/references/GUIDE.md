# n8n guide

The long-form group prose and the full roster. `SKILL.md` is the loadable hub, and
`references/skills/<skill>.md` is the verbatim body to follow for one task.

### Workflow design

| Skill | What it does |
| --- | --- |
| [`node-configuration`](references/skills/node-configuration.md) | Resolves an operation-aware node setup from property dependencies, required fields, resource and operation pairs, and the node family gotchas. |
| [`subworkflows`](references/skills/subworkflows.md) | Builds a reusable sub-workflow with typed Define Below inputs, an all or each mode, a return contract, naming, and agent-tool exposure. |
| [`workflow-patterns`](references/skills/workflow-patterns.md) | The five core n8n architectures, the trigger and output components, the data flow shapes, and the planning, validation, and deployment checklist. |

### Data and expressions

| Skill | What it does |
| --- | --- |
| [`binary-and-data`](references/skills/binary-and-data.md) | Moves files and binary data across upload, download, transform, multimodal agent input, and chat surfaces, including the CDN requirement. |
| [`code-javascript`](references/skills/code-javascript.md) | Writes JavaScript in an n8n Code node with `$input`, `$json`, and `$node`, picks the HTTP Request node for network access, and handles dates with DateTime. |
| [`code-python`](references/skills/code-python.md) | Writes bounded Python in a native n8n Code node under the task runner, with the standard library limits and the runtime contract. |
| [`code-tool`](references/skills/code-tool.md) | Writes and debugs the AI-callable Custom Code Tool, with a schema, a return shape, sandbox limits, and the two input modes. |
| [`expression-syntax`](references/skills/expression-syntax.md) | Writes and fixes `{{}}` expressions over `$json`, `$node`, and webhook data, with item linking, encoding, and untrusted-value guards. |

### AI agents

| Skill | What it does |
| --- | --- |
| [`agents`](references/skills/agents.md) | Designs n8n AI Agents, chains, classifiers, extractors, tools, memory, RAG, structured output, and human review with deterministic authorization. |

### Error handling

| Skill | What it does |
| --- | --- |
| [`error-handling`](references/skills/error-handling.md) | Makes n8n failures visible and recoverable through node error outputs, bounded retries, an Error Trigger workflow, and mapped HTTP error responses. |

### MCP and validation

| Skill | What it does |
| --- | --- |
| [`mcp-tools-expert`](references/skills/mcp-tools-expert.md) | Uses the n8n-mcp server to search nodes, validate configuration, read templates, edit a workflow, and deploy it, with the side-effect boundary. |
| [`multi-instance`](references/skills/multi-instance.md) | Selects, verifies, and switches an n8n MCP target across production, staging, teams, and clients, with a read-only check before a write. |
| [`validation-expert`](references/skills/validation-expert.md) | Reads an n8n validation error, separates a schema failure from a runtime failure, and applies the smallest fix before another validation run. |
## Group notes

### Workflow design

`workflow-patterns` is the starting point. Five core patterns, a selection guide, the
trigger, data, transform, output, and error components, and the planning, implementation,
validation, and deployment checklist. Choose the shape before the nodes. A linear flow, a
branch, a parallel fan-out, and a scheduled sync have different failure and retry needs.

`subworkflows` extracts shared or multi-step logic. Search for an existing workflow first.
Use an Execute Workflow Trigger with Define Below and typed fields, not passthrough. Declare
the input and output contract, choose `mode` all or each deliberately, and decide whether
the caller waits. A long side effect belongs in a non-blocking dispatch with its own
status. Expose a state-changing sub-workflow as an agent tool only with a clear
description and a review gate.

`node-configuration` is operation-aware. A node's required fields depend on its resource
and operation, so pick those first, then read the property dependencies. Use the right
`get_node` detail level, and check the node family gotchas. Read the existing workflow and
credential references before a targeted update. The detailed guide and the gotchas file
are both bundled.

### Data and expressions

`expression-syntax` covers `{{}}`. `$json` is the current input item, not a completed node
output, so inspect the execution data and the item link. Code-node APIs differ between
per-item and all-items modes. Use a credential for a secret, because `$env` examples can
expose a value and may be disabled. Encode a URL path and query component, guard a missing
array or object, and validate untrusted input before a downstream action. The detailed
guide is bundled, and it says its named `EXAMPLES.md` and `COMMON_MISTAKES.md` are absent.

`binary-and-data` moves files. The two binary slots, producing binary, reading and writing
it in a Code node, keeping it alive across a transform, the agent-tool boundary, and the
CDN requirement for a chat surface. Treat an uploaded file and a generated URL as
sensitive, take approval before a new external host, use the narrowest retention, and
never log bytes or base64.

`code-javascript` covers the JavaScript Code node. `$input`, `$json`, and `$node`, the
HTTP Request node for network access, DateTime for dates, the two node modes, and the
common errors. The detailed guide is bundled. The node is for bounded transforms, so keep a
large job in its own service.

`code-python` covers the native Python Code node. Check the installed version and the task
runner first. The runtime is bounded, the standard library is limited, and remote access
needs a managed credential with allowed destinations. Do not log a secret or a payload.
The detailed guide is bundled.

`code-tool` is the AI-callable Custom Code Tool, not the ordinary Code node. The tool has
two input modes, unstructured by default and a structured schema, plus a return shape and
a sandbox. Constrain the input with a schema, validate the output, stringify a structured
result, allowlist a network destination, and ask before testing a tool that writes or
calls an external service. Keep the tool name and description precise, because the agent
selects by them.

### AI agents

`agents` is the agent design guide. Pick the node before the prompt, then the sub-node
pattern. System prompt, tool description, the four tool types, `$fromAI()`, structured
output with a manual JSON Schema, memory choice, the binary boundary, human review for a
destructive tool, chat surfaces, and RAG. A buffer window is process-local, so use a
durable backend when history must survive a restart or be shared. Always filter the bot's
own user id on a chat reply. Gate a destructive tool with review, and stop on a denial or a
timeout. Nine references are bundled, including the chat patterns, examples, human review,
memory, RAG, structured output, sub-workflow as tool, system prompt, and tools.

### Error handling

`error-handling` makes a failure visible. Wire every fallible node's error output on a
webhook or API workflow, and add a workflow-level error workflow for a scheduled or
unattended run. Use `retryOnFail` for a retry-safe node before a custom path. Map a cause to
a status code, and keep the default envelope `{"error": "<code>", "message": "<text>"}`.
Never leak a stack trace, SQL, an upstream body, or a token to a caller. An Error Trigger is
not an OOM or crash guarantee, and it does not fire for a manual editor run. Four
references are bundled.

### MCP and validation

`mcp-tools-expert` covers the n8n-mcp server. Search nodes, validate a configuration, read
a template, edit a workflow, and deploy it. The server reports the tool's own errors, so
read them. A deploy or a template that applies to a live instance is a side effect, so get
approval. The detailed guide is bundled.

`multi-instance` handles one MCP connection over several n8n targets. List, resolve, switch
in its own turn, then verify with a read-only health check. An `INSTANCE_AMBIGUOUS` result
means the session never switched, and a `NOT_FOUND` for an object you know exists usually
means the wrong instance. Never guess a credential target. This skill ships no extra
files.

`validation-expert` interprets a validation error. Identify the node and the field, decide
whether it is a schema or a runtime failure, apply one fix, then validate again. Keep the
reported text. A passing preview is not authorization to activate. The detailed guide is
bundled.
