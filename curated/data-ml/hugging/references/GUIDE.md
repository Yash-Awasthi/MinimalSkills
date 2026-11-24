# hugging guide

The long-form group prose and the full roster. `SKILL.md` is the loadable hub, and
`references/skills/<skill>.md` is the verbatim body to follow for one task.

### Hub CLI and API

| Skill | What it does |
| --- | --- |
| [`hf-cli`](references/skills/hf-cli.md) | The `hf` command inventory for auth, cache, buckets, collections, datasets, models, spaces, jobs, repos, papers, webhooks, and endpoints. |
| [`tool-builder`](references/skills/tool-builder.md) | Builds reusable command line scripts around the Hugging Face API and the `hf` CLI, with chaining, piping, and intermediate processing. |

### Datasets and viewer

| Skill | What it does |
| --- | --- |
| [`dataset-viewer`](references/skills/dataset-viewer.md) | Runs read-only Dataset Viewer API calls to explore and extract rows, splits, and parquet links without downloading the full dataset. |
| [`datasets`](references/skills/datasets.md) | Creates and manages Hub datasets: repo init, configs and system prompts, streaming row updates, SQL transforms, and schema and leakage checks. |

### Evaluation

| Skill | What it does |
| --- | --- |
| [`community-evals`](references/skills/community-evals.md) | Runs inspect-ai and lighteval against Hub models on local GPUs or remote inference providers, with backend and hardware selection. |
| [`evaluation`](references/skills/evaluation.md) | Adds evaluation results to a model card through model-index, with extraction, an external API import, and local vLLM or lighteval runs. |

### Training and jobs

| Skill | What it does |
| --- | --- |
| [`jobs`](references/skills/jobs.md) | Prepares and runs a CPU, GPU, or TPU workload on Hugging Face Jobs with scoped secrets, hardware choice, Hub persistence, and monitoring. |
| [`model-trainer`](references/skills/model-trainer.md) | Plans and runs SFT, DPO, and GRPO training with TRL or Unsloth, plus GGUF conversion, cost estimation, and held-out evaluation. |
| [`vision-trainer`](references/skills/vision-trainer.md) | Runs a bounded image classification, object detection, or SAM and SAM2 segmentation pilot, with dataset inspection and artifact persistence. |

### Apps and tracking

| Skill | What it does |
| --- | --- |
| [`gradio`](references/skills/gradio.md) | Builds Gradio web UIs and demos in Python with components, event listeners, layouts, and chatbots. |
| [`trackio`](references/skills/trackio.md) | Logs, alerts on, and retrieves ML training metrics with Trackio, including a Space dashboard and an experiment workflow. |

### Papers

| Skill | What it does |
| --- | --- |
| [`paper-publisher`](references/skills/paper-publisher.md) | Publishes and manages a Hugging Face paper page, links models and datasets, claims authorship, and renders a markdown research article. |
| [`papers`](references/skills/papers.md) | Reads Hugging Face paper pages and the papers API for metadata, authors, linked models, datasets, spaces, and repositories. |
## Group notes

### Hub CLI and API

`face-cli` is the command inventory. Auth, cache, buckets, collections, datasets,
discussions, endpoints, extensions, jobs, models, papers, repos, skills, spaces, and
webhooks, plus common options and mounting a repo as a local filesystem. It describes a
specific upstream version, so check `hf version` and the per-command help first. Install by
downloading the installer, reviewing it, and running the reviewed file in the same shell.
Exiting a pager is not approval.

`tool-builder` writes reusable scripts around the API and the CLI. Chaining, piping,
intermediate processing, the high-level endpoints, direct API access, and the CLI path. It
names four shell helpers under `<support-root>/references/` that are not bundled, so ask for
the original material or skip the dependent step. It does not identify a verified download
source for them.

### Datasets and viewer

`dataset-viewer` is read-only. Query rows, splits, and parquet links through the Dataset
Viewer API without downloading the whole set. It has sensible default limits, so state the
split, the offset, and the length. A viewer response is a sample, not a full count.

`datasets` creates and manages a Hub dataset. Repo init, configs and system prompts,
streaming row updates, SQL transforms, and the local workflow. The historical
`sql_manager.py`, `dataset_manager.py`, and example JSON are not bundled. Download only
approved data with a pinned client, use a read-only token for discovery, and never enable
remote dataset code. Validate the schema, counts, nulls, duplicates, and train and test
leakage before export, and keep the source revision, the transformation record, and the
license. Inspect an existing repo before an update and never overwrite silently.

### Evaluation

`community-evals` runs evaluations on local hardware. Inspect with remote inference
providers, inspect on a local GPU, or lighteval on a local GPU, with a script choice,
backend selection, hardware guidance, and troubleshooting. The bundled lighteval wrapper is
disabled pending a release-specific CLI migration, because its version range mixes
incompatible APIs. Use the official documentation for a pinned release. The inspect
wrappers also need matching versions. This is not HF Jobs orchestration or model-card
publication.

`evaluation` puts results in a model card. Extract an existing table, import a score from
the Artificial Analysis API, or run a custom evaluation, then write the model-index
metadata. Importing a number or extracting YAML is not running an evaluation or
establishing leaderboard acceptance. Preserve the model revision, the dataset revision and
split, the prompt or chat template, the shots, the decoding parameters, the seed, and the
hardware. The detailed guide is bundled.

### Training and jobs

`model-trainer` covers SFT, DPO, and GRPO with TRL or Unsloth, plus GGUF conversion, cost
estimation, and a held-out check. The Unsloth example is text training, not vision training
and not streaming. Read the detailed guide and the hardware, hub saving, reliability,
trackio, training methods, patterns, troubleshooting, and Unsloth references, plus the
GGUF and local macOS guides. Keep `trust_remote_code=False` unless the code was reviewed.
Uploading is optional.

`vision-trainer` is a bounded pilot for image classification, object detection, and binary
SAM or SAM2 segmentation. It is not clinical validation, autonomous-vehicle certification,
or continuous alpha-matting training. Inspect the dataset, estimate the cost, train, then
evaluate the actual loss, metrics, and predictions on the held-out design. Record the model,
data, SDK, seed, samples, steps, and hardware. Save to approved private storage. The scripts
are pilot templates, not production services. The license and upstream notice are bundled.

`jobs` prepares and runs a CPU, GPU, or TPU workload. Scope, prerequisites, secrets,
hardware, Hub persistence, monitoring, and delivery. Local preparation does not authorize
submission, scheduling, publication, or a paid retry. Authenticate the submission
separately, pass only the permissions the job needs, and never publish source or private
data silently. The Python API receives a real secret value, so a literal variable string is
not expanded, and the returned credential is never printed. Verify the actual output object
and the final commit, not only a success-looking log. The detailed guide, hardware, hub
saving, token, and troubleshooting references are bundled, plus three helper scripts.

### Apps and tracking

`gradio` builds demos. Core patterns, key component signatures, event listeners, layouts,
and chatbots. The signatures are an imported API snapshot, not valid Python stubs or a
universal contract. Check the installed Gradio version before a newer parameter or CLI
command. Keep a demo on loopback unless it was intentionally shared, and never expose a
secret or an unauthenticated write path.

`trackio` logs and retrieves metrics. The Python logging API, alerts, and the CLI retrieval
path, plus a Space dashboard and an experiment workflow. Sync to a Space publishes metrics,
so confirm the target and the data. Alert channels need their own credentials, and a
metric name or run id stays verbatim.

### Papers

`papers` reads the paper pages and the papers API. Parse the id, fetch the page as
markdown, read structured metadata for authors, linked models, datasets, spaces, a GitHub
repo, and a project page, then use the daily, list, search, index, and update endpoints.
Public reads need no authentication. A write endpoint changes the Hub, so confirm the paper
id and the authority first.

`paper-publisher` creates and manages a paper page. Create the page, link models and
datasets, claim authorship, and generate a professional markdown article from a template.
The detailed guide, quick reference, usage example, `paper_manager.py`, and four article
templates are bundled. Claiming authorship and linking a paper are public writes, so
confirm the account and the paper first.
