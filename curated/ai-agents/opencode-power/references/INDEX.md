# OpenCode power index

57 skills in 8 groups. Load one skill for the task.

| Group | Skills |
| --- | --- |
| **Core dev workflow** | 10 |
| **Project rules & prose** | 3 |
| **Security audit** | 14 |
| **HF CLI & SageMaker** | 8 |
| **HF Hub, Spaces & apps** | 10 |
| **Model training & inference** | 5 |
| **Agent tooling & meta** | 4 |
| **Research & model selection** | 3 |

## Core dev workflow

| Skill | Purpose |
| --- | --- |
| [`ai-slop`](skills/ai-slop.md) | Operational rubric that turns "don't make AI slop" into observable properties, severity levels, evidence requirements, and repair actions for interface design. Use as the reference rubric when building or reviewing marketing sites, produ... |
| [`code-architect`](skills/code-architect.md) | Design a feature architecture by analyzing existing codebase patterns and conventions, then provide a comprehensive implementation blueprint with specific files to create or modify, component designs, data flows, and a build sequence. Us... |
| [`code-explorer`](skills/code-explorer.md) | Deeply analyze an existing codebase feature by tracing execution paths, mapping architecture layers, understanding patterns and abstractions, and documenting dependencies. Use this skill when you need to understand how a feature works be... |
| [`code-quality`](skills/code-quality.md) | Agents should invoke this skill for code reviews, linting/formatting setup, maintainability checks, complexity concerns, warning cleanup, coding standards, or quality gates in Rust, TypeScript, Python, shell, and mixed repos. |
| [`code-review`](skills/code-review.md) | Review a pull request or a set of code changes for bugs, logic errors, and project-convention violations using a confidence-filtered, multi-agent process. Use this skill when the user asks to review a PR, audit pending changes, or inspec... |
| [`code-reviewer`](skills/code-reviewer.md) | Review code for bugs, logic errors, security vulnerabilities, code quality issues, and adherence to project conventions, using confidence-based filtering to report only high-priority issues that truly matter. Use this skill when reviewin... |
| [`design-patterns`](skills/design-patterns.md) | Agents should invoke this skill when choosing patterns, designing traits/interfaces/components, deciding abstraction boundaries, evaluating dependency injection/callbacks, or comparing implementation approaches in Rust, TypeScript/React,... |
| [`differential-review`](skills/differential-review.md) | Performs security-focused differential review of code changes (PRs, commits, diffs). Adapts analysis depth to codebase size, uses git history for context, calculates blast radius, checks test coverage, and generates comprehensive markdow... |
| [`feature-dev`](skills/feature-dev.md) | Guide a feature implementation through a structured seven-phase workflow with deep codebase understanding, clarifying questions, parallel architecture design, and quality review. Use this skill when the user asks to build a new feature,... |
| [`frontend-design`](skills/frontend-design.md) | Create distinctive, production-grade frontend interfaces with high design quality and accessible markup. Use this skill when the user asks to build or beautify web components, pages, applications, landing pages, dashboards, artifacts, or... |


## Project rules & prose

| Skill | Purpose |
| --- | --- |
| [`agents-md-improver`](skills/agents-md-improver.md) | Audit and improve project-rules files (AGENTS.md, CLAUDE.md, .agents/instructions, local overrides) so the agent keeps accurate project context. Use when the user asks to check, audit, review, update, improve, or fix their AGENTS.md or C... |
| [`agents-md-revise`](skills/agents-md-revise.md) | Capture learnings from the current session into the project-rules file (AGENTS.md, CLAUDE.md, or local override) so future sessions benefit. Use when the user says "revise the rules", "update AGENTS.md / CLAUDE.md with what we just learn... |
| [`humanizer`](skills/humanizer.md) | Rewrite AI-generated copy in Spanish and English so it sounds direct, concrete and human while preserving meaning, facts and numbers exactly. Use when drafts feel robotic, verbose or translated and need short active sentences without em-... |


## Security audit

| Skill | Purpose |
| --- | --- |
| [`agentic-actions-auditor`](skills/agentic-actions-auditor.md) | Audit GitHub Actions that run AI agents for prompt injection, unsafe interpolation, sandbox gaps, and permissive actor rules. Use for agentic CI workflows, not general application code review. |
| [`codeql`](skills/codeql.md) | Run CodeQL database creation and security queries, add data-extension models, or process CodeQL SARIF. Use when CodeQL is explicitly requested; use security-review for a broader manual security review. |
| [`fp-check`](skills/fp-check.md) | Systematically verifies suspected security bugs to eliminate false positives. Produces TRUE POSITIVE or FALSE POSITIVE verdicts with documented evidence for each bug. |
| [`insecure-defaults`](skills/insecure-defaults.md) | Detects fail-open insecure defaults (hardcoded secrets, weak auth, permissive security) that allow apps to run insecurely in production. Use when auditing security, reviewing config management, or analyzing environment variable handling. |
| [`sarif-parsing`](skills/sarif-parsing.md) | Parses and processes SARIF files from static analysis tools like CodeQL, Semgrep, or other scanners. Triggers on \"parse sarif\", \"read scan results\", \"aggregate findings\", \"deduplicate alerts\", or \"process sarif output\". Handles... |
| [`security-review`](skills/security-review.md) | Perform a focused security review of pending git changes to identify high-confidence security vulnerabilities with real exploitation potential. Use this skill when the user asks for a security review, security audit, vulnerability scan,... |
| [`security-threat-model`](skills/security-threat-model.md) | Create a repository-grounded AppSec threat model covering assets, trust boundaries, attackers, abuse paths, and mitigations. Use only for explicit threat-modeling requests, not general architecture or code review. |
| [`semgrep`](skills/semgrep.md) | Run Semgrep static analysis across a codebase, optionally using Semgrep Pro for cross-file taint analysis. Use when Semgrep or a static-analysis scan is requested; use security-review for a manual audit. |
| [`semgrep-rule-creator`](skills/semgrep-rule-creator.md) | Creates custom Semgrep rules for detecting security vulnerabilities, bug patterns, and code patterns. Use when writing Semgrep rules or building custom static analysis detections. |
| [`semgrep-rule-variant-creator`](skills/semgrep-rule-variant-creator.md) | Creates language variants of existing Semgrep rules. Use when porting a Semgrep rule to specified target languages. Takes an existing rule and target languages as input, produces independent rule+test directories for each language. |
| [`sharp-edges`](skills/sharp-edges.md) | Identify error-prone APIs, dangerous configuration, and footgun designs that enable security mistakes. Use for API ergonomics, misuse resistance, secure defaults, or pit-of-success reviews; use code-review for general defects. |
| [`supply-chain-risk-auditor`](skills/supply-chain-risk-auditor.md) | Identifies dependencies at heightened risk of exploitation or takeover. Use when assessing supply chain attack surface, evaluating dependency health, or scoping security engagements. |
| [`variant-analysis`](skills/variant-analysis.md) | Find similar vulnerabilities and bugs across codebases using pattern-based analysis. Use when hunting bug variants, building CodeQL/Semgrep queries, analyzing security vulnerabilities, or performing systematic code audits after finding a... |
| [`vuln-report`](skills/vuln-report.md) | Turn one confirmed security finding into a disclosure-ready GitHub advisory with root cause, proof of concept, impact, and source evidence. Use for reporting an established vulnerability, not discovering or validating one. |


## HF CLI & SageMaker

| Skill | Purpose |
| --- | --- |
| [`hf-cli`](skills/hf-cli.md) | Use the `hf` CLI for Hub authentication, downloads, uploads, repositories, cache, jobs, buckets, webhooks, and endpoint administration. Use for CLI operations, not model recommendations, paper analysis, training design, or building a Space. |
| [`hf-cloud-aws-context-discovery`](skills/hf-cloud-aws-context-discovery.md) | Discover the active AWS profile, region, account, and caller identity before SageMaker or AWS work. Use when local AWS context is needed or unspecified; do not use for cloud-agnostic model planning. |
| [`hf-cloud-python-env-setup`](skills/hf-cloud-python-env-setup.md) | Create an isolated Python environment with a compatible Python version and boto3 for SageMaker or AWS automation. Use before executing AWS Python code; do not use for general Python environment setup. |
| [`hf-cloud-sagemaker-deployment-planner`](skills/hf-cloud-sagemaker-deployment-planner.md) | Plan and coordinate a model deployment to Amazon SageMaker, including serving stack and real-time versus async inference. Use as the entry point for SageMaker hosting requests, before image, IAM, and endpoint implementation skills. |
| [`hf-cloud-sagemaker-iam-preflight`](skills/hf-cloud-sagemaker-iam-preflight.md) | Verify or select a SageMaker execution role before creating models, endpoints, or training jobs. Use when a role ARN is missing or IAM access fails; inspect existing roles before proposing role creation. |
| [`hf-cloud-sagemaker-production-defaults`](skills/hf-cloud-sagemaker-production-defaults.md) | Implement a production SageMaker endpoint with autoscaling, CloudWatch alarms, and tags. Use after the serving image and IAM role are known; use the deployment planner first when architecture is undecided. |
| [`hf-cloud-serving-image-selection`](skills/hf-cloud-serving-image-selection.md) | Select and verify the current region-specific serving container URI for a SageMaker model deployment. Use after the deployment pathway is chosen and before endpoint code; never infer an image URI from memory. |
| [`hf-mem`](skills/hf-mem.md) | Hugging Face CLI to estimate the required memory to load Safetensors or GGUF model weights for inference from the Hugging Face Hub. |


## HF Hub, Spaces & apps

| Skill | Purpose |
| --- | --- |
| [`huggingface-community-evals`](skills/huggingface-community-evals.md) | Run evaluations for Hugging Face Hub models using inspect-ai and lighteval on local hardware. Use for backend selection, local GPU evals, and choosing between vLLM / Transformers / accelerate. Not for HF Jobs orchestration, model-card PR... |
| [`huggingface-datasets`](skills/huggingface-datasets.md) | Use this skill for Hugging Face Dataset Viewer API workflows that fetch subset/split metadata, paginate rows, search text, apply filters, download parquet URLs, and read size or statistics. |
| [`huggingface-gradio`](skills/huggingface-gradio.md) | Build Gradio web UIs and demos in Python. Use when creating or editing Gradio apps, components, event listeners, layouts, or chatbots. |
| [`huggingface-local-models`](skills/huggingface-local-models.md) | Use to select models to run locally with llama.cpp and GGUF on CPU, Mac Metal, CUDA, or ROCm. Covers finding GGUFs, quant selection, running servers, exact GGUF file lookup, conversion, and OpenAI-compatible local serving. |
| [`huggingface-lora-space-builder`](skills/huggingface-lora-space-builder.md) | Build and publish a Gradio Hugging Face Space for a user-provided image or video LoRA, including pipeline selection and model-card settings. Use for LoRA demos; use huggingface-spaces for general Space work. |
| [`huggingface-paper-publisher`](skills/huggingface-paper-publisher.md) | Publish and manage research papers on Hugging Face Hub. Supports creating paper pages, linking papers to models/datasets, claiming authorship, and generating professional markdown-based research articles. |
| [`huggingface-spaces`](skills/huggingface-spaces.md) | Build, deploy, debug, or maintain a Hugging Face Space using Gradio, Docker, or Static SDKs. Use for general Space hosting and configuration; use huggingface-zerogpu for ZeroGPU runtime constraints and lora-space-builder for LoRA demos. |
| [`huggingface-tool-builder`](skills/huggingface-tool-builder.md) | Use this skill when the user wants to build tool/scripts or achieve a task where using data from the Hugging Face API would help. This is especially useful when chaining or combining API calls or the task will be repeated/automated. This... |
| [`huggingface-trackio`](skills/huggingface-trackio.md) | Track and visualize ML training experiments with Trackio. Use when logging metrics during training (Python API), firing alerts for training diagnostics, or retrieving/analyzing logged metrics (CLI). Supports real-time dashboard visualiza... |
| [`huggingface-zerogpu`](skills/huggingface-zerogpu.md) | Implement or debug Hugging Face Spaces ZeroGPU code using `@spaces.GPU`, including isolation, state, duration, sizing, and CUDA-wheel constraints. Use for ZeroGPU-specific behavior; use huggingface-spaces for general hosting. |


## Model training & inference

| Skill | Purpose |
| --- | --- |
| [`huggingface-llm-trainer`](skills/huggingface-llm-trainer.md) | Train or fine-tune language models with TRL or Unsloth on Hugging Face Jobs, including SFT, DPO, GRPO, reward models, and GGUF conversion. Use for cloud LLM training; use huggingface-vision-trainer for vision tasks. |
| [`huggingface-vision-trainer`](skills/huggingface-vision-trainer.md) | Train object-detection, image-classification, or SAM segmentation models on Hugging Face Jobs. Use for vision fine-tuning and evaluation; use huggingface-llm-trainer for language models. |
| [`train-sentence-transformers`](skills/train-sentence-transformers.md) | Train or fine-tune SentenceTransformer bi-encoders, CrossEncoder rerankers, or SparseEncoder models, including losses, negatives, evaluation, distillation, LoRA, and Matryoshka. Use for sentence-transformers training tasks. |
| [`transformers-js`](skills/transformers-js.md) | Run Hugging Face models in JavaScript or TypeScript with Transformers.js, WebGPU, or WASM across browser, Node.js, Bun, and Deno. Use for client-side or JS-runtime inference, not Python training. |
| [`trl-training`](skills/trl-training.md) | Train and fine-tune transformer language models using TRL (Transformers Reinforcement Learning). Supports SFT, DPO, GRPO, KTO, RLOO and Reward Model training via CLI commands. |


## Agent tooling & meta

| Skill | Purpose |
| --- | --- |
| [`agent-git-helper`](skills/agent-git-helper.md) | Provides git workflow assistance, branch management, and commit message optimization |
| [`agent-test-skill`](skills/agent-test-skill.md) | A test skill to verify all plugin tools work correctly - use_skill, read_skill_file, run_skill_script, find_skills |
| [`mcp-builder`](skills/mcp-builder.md) | Guide the creation of high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when the user wants to build an MCP server to integrate an external API or servi... |
| [`skill-creator`](skills/skill-creator.md) | Create new skills (SKILL.md files), modify and improve existing skills, and design skill descriptions for accurate triggering. Use when the user wants to create a new skill from scratch, edit an existing skill, optimize a skill's descrip... |


## Research & model selection

| Skill | Purpose |
| --- | --- |
| [`huggingface-best`](skills/huggingface-best.md) | Find and compare recommended Hugging Face models for a task using benchmarks, model size, and device constraints. Use for model selection questions; use huggingface-local-models for GGUF setup and hf-cli for Hub operations. |
| [`huggingface-papers`](skills/huggingface-papers.md) | Look up and read Hugging Face paper pages in markdown, and use the papers API for structured metadata such as authors, linked models/datasets/spaces, Github repo and project page. Use when the user shares a Hugging Face paper page URL, a... |
| [`paper-summarizer`](skills/paper-summarizer.md) | Agents should invoke this skill for academic or technical papers, arXiv/PubMed/IEEE/ACM links, PDFs, methodology review, limitations, practical implications, or extracting findings for engineering decisions. |

