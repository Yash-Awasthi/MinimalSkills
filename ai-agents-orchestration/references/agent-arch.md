# agent-arch

Load when choosing the control flow for an LLM system.

## ladder

| level | shape | use when |
| --- | --- | --- |
| 1 | one call, one prompt | input maps to output, no tools |
| 2 | call plus schema | output feeds code |
| 3 | tool loop | needs lookup or side effects |
| 4 | plan and execute | goal decomposes into steps |
| 5 | supervisor plus workers | independent subtasks, fan-out |
| 6 | graph with checkpoints | long runs, resume after failure |

Start at the lowest level that passes the eval set. Each level up costs latency, tokens and a new failure mode.

## patterns

- ReAct: interleaved think and act. Cap iterations. Log each step.
- Plan and execute: plan once, execute steps, replan on failure. Cheaper than ReAct for stable tasks.
- Tool registry: select tools by description, not by index. Above 20 tools, retrieve candidates.
- Supervisor: routes to workers, never does the work. Workers return structured results.
- Checkpoint recovery: persist state per step, resume by id. Required past 2 minutes of work.

## failure modes

| failure | cause | guard |
| --- | --- | --- |
| infinite loop | no iteration cap | max_steps, repeated-action detection |
| silent wrong answer | tool error swallowed | return the error text to the model |
| tool soup | 40 tools, vague descriptions | fewer tools, sharper descriptions |
| context rot | everything in the window | summarize, drop, or retrieve |
| cascade | one agent, then another, then another | one agent first, measure |
| no recovery | state only in the window | checkpoint to a store |

## interface

```ts
type Step = { thought: string; tool?: string; input?: unknown };
type Result<T> = { ok: true; value: T } | { ok: false; error: string; retryable: boolean };

async function run(task: string, limits: Limits): Promise<Result<Out>> {
  for (let i = 0; i < limits.maxSteps; i++) {
    const step = await model.next(task, history);
    if (!step.tool) return { ok: true, value: step.answer };
    const r = await tools.call(step.tool, step.input);
    history.push(r.ok ? r.value : `tool_error: ${r.error}`);
  }
  return { ok: false, error: 'step_limit', retryable: false };
}
```

Tool errors go back into the history. A retryable flag lets the model choose a different path.

## cost shape

- Prompt tokens grow with history: summarize past a threshold.
- Parallel tool calls cut wall clock, not cost.
- A reranker adds a call per query; measure the gain before keeping it.

## review questions

1. What happens on step 40.
2. What happens when the tool returns 500.
3. What happens when the model returns invalid json.
4. What stops a spend runaway.
5. How do you replay a failed run.

## framework shapes

- LangGraph: state is a typed dict, nodes are functions, edges are conditional. `graph.ainvoke(state)` for one run, `astream_events` for tokens. Checkpoint with `MemorySaver` in dev and a Postgres saver in prod, or a resumed run loses its place.
- PydanticAI: `Agent(model, result_type=Invoice)` validates the output against the model. `@agent.tool` registers a tool; a validation failure raises and the retry carries the error text.
- Vercel AI SDK: `streamText({ model, tools, maxSteps: 5 })`; `maxSteps` is the loop cap, not a suggestion.
- CrewAI and AutoGen: role-based crews. Use them only when the roles are genuinely different; otherwise a tool loop is cheaper and easier to eval.
- OpenAI Assistants: state lives server side under a thread id; polling a run costs one request per poll.
- Pin the SDK major version. Tool-call formats changed across majors and an unpinned upgrade breaks argument parsing.
## provider index

| provider | the rule that matters |
| --- | --- |
| Gemini APIs | `generateContent` with `responseSchema` for structured output; a function call comes back as a `functionCall` part, not text. |
| Microsoft 365 / Azure hosted agents | Foundry agent service: a thread id holds state, tool auth is a connection, and a run poll is a request. |
| Computer use | Screenshot, action, wait: the loop needs a step cap, an action allowlist and a timeout per action, or it clicks forever. |
| AI security operations | Log every tool call with its arguments; a red-team run replays the trace, not the prompt. |

## adjacent practices

| practice | the rule that matters |
| --- | --- |
| Bounded build loop | Time-box the attempt, state the stop condition, report what was tried and what failed. |
| Spec-driven development | Write the eval cases before the prompt; a spec that cannot fail is documentation. |
| Bug hunt swarm | One bug per agent, shared repro corpus, dedupe before triage. |
| Unship | Delete the prompt, the tool, the eval and the flag in one change; a dead agent left running still costs per call. |
| Progressive estimation | Estimate the next slice only; a token-cost estimate for a 6-month roadmap is a guess. |
| Project development methodology | Fixed cadence, variable scope; a scope fixed at kickoff is how the date slips. |
| GDB | `gdb -p <pid>`, `bt full`, `catch throw`; a hung agent process is usually a blocked network read, check `info threads`. |
| pstack/poteto style | `pstack <pid>` for a native snapshot; the style is one expression per line, no nested ternaries. |
| Idea evaluation | Score reach, impact, confidence, effort; an agent feature with no baseline metric is a demo. |
