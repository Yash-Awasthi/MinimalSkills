# daymade guide

The long-form group prose and the full roster. `SKILL.md` is the loadable hub, and
`references/skills/<skill>.md` is the verbatim body to follow for one task.

### Agent CLI setup and model operations

| Skill | What it does |
| --- | --- |
| [`agent-web-search-setup`](references/skills/agent-web-search-setup.md) | Fixes web search on an agent whose model backend can't run it: a relay/reseller proxying Claude or Codex returns empty instead of failing. |
| [`auto-repo-setup`](references/skills/auto-repo-setup.md) | Diagnoses and repairs repository setup and guarded Git workflows for Claude Code or Codex, environment repair, startup sync, hook auditing, collaborator handoff. |
| [`claude-code-hooks`](references/skills/claude-code-hooks.md) | Writes, tests, registers and debugs Claude Code hooks (PreToolUse, PostToolUse, SessionStart, Stop) that turn a rule the model keeps breaking into a hard gate. |
| [`claude-code-ops-router`](references/skills/claude-code-ops-router.md) | Plugin/Skill repair, marketplace, statusline, model profiles/source sync, 1M/[1m] context, usage/quota reset ping, memory to docs, .txt repair, MCP startup context. |
| [`claude-code-ping-start-5h-quota`](references/skills/claude-code-ping-start-5h-quota.md) | Sets a one-shot macOS timer that pings Claude after the quota resets, so the next 5-hour window starts before the user wakes. |
| [`claude-md-progressive-disclosurer`](references/skills/claude-md-progressive-disclosurer.md) | Restructures CLAUDE.md or AGENTS.md with progressive disclosure and no information loss, and proves every pointer lands on real content. |
| [`claude-migrate-memory-to-doc`](references/skills/claude-migrate-memory-to-doc.md) | Migrates Claude Code personal memory (the per-project memory/ directory) into tool-agnostic reference docs so other AI CLIs that auto-load AGENTS.md (Codex primarily) can read the same user profile and preferences. |
| [`claude-switch-models-setup`](references/skills/claude-switch-models-setup.md) | Isolates profiles for multi-provider setup and switching models in separate terminal windows (Kimi, MiniMax, DeepSeek, GLM, StepFun, Anthropic). |
| [`claude-usage-analyst`](references/skills/claude-usage-analyst.md) | Analyze Claude Code and Claude Desktop Code token usage, cost, quota burn, model mix, cache read/write, and 5-hour block consumption using ccusage evidence. |
| [`codex-1m-context-window-setup`](references/skills/codex-1m-context-window-setup.md) | Configures and verifies an expanded, model-aware context window for OpenAI Codex CLI and Desktop. Use to inspect local context settings, lower or set the auto-compaction threshold, expand ~258K context to 500K or 1M... |
| [`codex-image-gallery`](references/skills/codex-image-gallery.md) | Start or reuse a self-contained local web gallery for browsing Codex-generated images. Use when the user asks to browse Codex generated images, open a local image gallery, inspect ~/.codex/generated_images... |
| [`local-codex`](references/skills/local-codex.md) | Launches and manages the local OpenAI Codex CLI as a non-interactive coding sub-agent via ChatGPT OAuth, never API keys. |
| [`openclaw`](references/skills/openclaw.md) | Audits, diffs, copies, and lists OpenClaw providers and models, adds a model, and switches the default in local config. |
| [`openclaw-model-switch`](references/skills/openclaw-model-switch.md) | Switches or repairs an OpenClaw instance's model config: changes the default model, adds model definitions, and fixes 401 "Invalid token", "No available channel / model not found", "Thinking level X is not supported"... |
| [`peer-message`](references/skills/peer-message.md) | Bridges Claude Code and Codex sessions when native tools can't reach the target. Use for 跨产品通信 / 脚本回帖 / 送达排查: cross-product messages, hooks or scripts posting to a session, verifying delivery (Held messages included)... |
| [`statusline-generator`](references/skills/statusline-generator.md) | Installs, configures, customizes, or troubleshoots the Claude Code statusline (cwd, model, token counts). Use when the user wants to set up or change the statusline, switch minimal vs full layouts... |
| [`tibo-reset-codex`](references/skills/tibo-reset-codex.md) | Checks ChatGPT and Codex reset announcements, per-account quota, banked resets, and live account state, and converts Pacific time to Beijing. |

### Local history, continuity, and prior work

| Skill | What it does |
| --- | --- |
| [`claude-export-txt-better`](references/skills/claude-export-txt-better.md) | Fixes broken line wrapping in Claude Code exported .txt conversation files, rebuilds tables, paragraphs, paths and tool calls hard-wrapped at a fixed width. |
| [`continue-claude-code-work`](references/skills/continue-claude-code-work.md) | Continues interrupted Claude Code work after local history is read and reconciled, reconstructs the original outcome, unfulfilled requests, and the next action. |
| [`continue-codex-work`](references/skills/continue-codex-work.md) | Continues interrupted Codex work only after read-codex-history verifies rollout identity and fork/compaction lineage, restores the original outcome, unfulfilled requests, and the next action. |
| [`gemini-history-analyzer`](references/skills/gemini-history-analyzer.md) | Analyze Google Takeout exports of Gemini conversation history. Use when the user mentions Gemini takeout, Gemini export, Gemini history, Gemini conversation analysis, Google Takeout zip analysis... |
| [`ghostty-use`](references/skills/ghostty-use.md) | Snapshots local Codex/Claude CLI sessions across terminals and restores IDs in Ghostty after reboot (保存会话/重启前备份/恢复窗口), audits survivors, and makes change-only automatic backups (定期增量快照). |
| [`local-conversation-history`](references/skills/local-conversation-history.md) | Entry point for local AI conversation history across Claude Code, Codex and Kimi CLI: routes each request to the reader or continuation skill that owns it and keeps the cross-provider inventory. |
| [`prior-work-retrieval`](references/skills/prior-work-retrieval.md) | Only for explicit prior-work/reuse/history requests, not status checks. Finds and verifies existing work before new production when reuse is plausible. |
| [`read-claude-code-history`](references/skills/read-claude-code-history.md) | Reads, searches and exports local Claude Code and Kimi CLI history without resuming work: timelines, verbatim user input, keyword or fuzzy recall, file recovery from transcripts... |
| [`read-claude-web-conversation`](references/skills/read-claude-web-conversation.md) | Reads or exports the COMPLETE transcript of a Claude.ai web conversation, private /chat/... and public /share/... links, via Claude.ai's internal API in the user's logged-in Chrome, plus its files. |
| [`read-codex-history`](references/skills/read-codex-history.md) | Reads, searches and exports local OpenAI Codex history without continuing work: session inventory, timelines, verbatim user input, indexed search, and rollout identity/fork lineage. |

### Skills, plugins, and marketplaces

| Skill | What it does |
| --- | --- |
| [`claude-skills-troubleshooting`](references/skills/claude-skills-troubleshooting.md) | Diagnose and resolve Claude Code plugin and skill issues. This skill should be used when plugins are installed but not showing in available skills list, skills are not activating as expected... |
| [`marketplace-dev`](references/skills/marketplace-dev.md) | Builds and maintains Claude Code plugin marketplaces: converts a skills repo to spec-valid marketplace.json, adds/updates plugin entries, and migrates skills into or between suites. |
| [`marketplace-health-check`](references/skills/marketplace-health-check.md) | Runs an evidence-based health audit of this skills marketplace repo, code safety, docs/SSOT, security/PII, PR/issue triage, manifest integrity, via a parallel workflow, then verifies findings by priority. |
| [`skill-creator`](references/skills/skill-creator.md) | Creates, edits and benchmarks skills; supersedes the official skill-creator plugin, so when both are listed, use this one. |
| [`skill-evolver`](references/skills/skill-evolver.md) | Researches and improves a specified existing Skill using successful/failed work and competitor evidence. Use for 优化这个Skill, 从成功和失败经验改进Skill, or 研究竞品后优化指定技能. Routine creation and editing use skill-creator. |
| [`skill-governance`](references/skills/skill-governance.md) | Governs the Claude Code/Codex Skill surface: reconciles source/install/catalog-visibility drift without losing cold capability. |
| [`skill-reviewer`](references/skills/skill-reviewer.md) | Reviews skill quality with evidence-based design rubrics and read-only batch inventories. Use for self-review, external skill or repository audits, and authorized auto-PR improvements. |
| [`skills-search`](references/skills/skills-search.md) | Finds Skills in configured local repositories before searching CCPM. Use when discovering or reusing a Skill, finding PDF/code-review tools, inspecting a Skill, listing installed/popular/recent Skills... |

### Git and GitHub

| Skill | What it does |
| --- | --- |
| [`git-safety-net`](references/skills/git-safety-net.md) | Audits, preserves and recovers local Git state before cleanup: unpushed or wrong-branch commits, dirty worktrees, duplicate clones, stashes, dangling commits, squash-merge uncertainty. |
| [`github-contributor`](references/skills/github-contributor.md) | Ships pull requests to open-source projects you don't maintain, CONTRIBUTING compliance, PR-size/scope checks, minimal-diff implementation, AI-disclosure PR descriptions, and rebase or bot-review replies. |
| [`github-ops`](references/skills/github-ops.md) | Operates GitHub via gh CLI and REST/GraphQL, PRs, issues, Actions, self-hosted Runner inventory/capacity, repos, collaborators, org permissions, 2FA, with explicit target, authorization, and independent readback. |
| [`github-review-pr`](references/skills/github-review-pr.md) | Reviews PRs against the live base with immutable objects and three-way merges. Use for PR review/merge readiness, main changed, closed-PR reconsideration, open-PR sweeps, review-led repair... |
| [`github-sensitive-data-cleanup`](references/skills/github-sensitive-data-cleanup.md) | Scans and removes sensitive data (secrets, API keys, private domains/IPs, PII) from GitHub repository history, then verifies and force-pushes safely. |
| [`repomix-safe-mixer`](references/skills/repomix-safe-mixer.md) | Safely package codebases with repomix by automatically detecting and removing hardcoded credentials before packing. |
| [`repomix-unmixer`](references/skills/repomix-unmixer.md) | Extracts files from repomix-packed repositories, restoring original directory structures from XML/Markdown/JSON formats. |

### macOS system care

| Skill | What it does |
| --- | --- |
| [`macos-cleaner`](references/skills/macos-cleaner.md) | Diagnoses and safely reclaims macOS disk space: caches, logs, app remnants, large/duplicate files, Docker/OrbStack, Chromium code-sign clones, developer caches. |
| [`macos-load-doctor`](references/skills/macos-load-doctor.md) | Diagnoses macOS system-level slowness, heat and fleet-wide timeouts: high load average, leaked per-session child processes (MCP servers, helpers), fork storms, busy loops. |
| [`macos-permissions`](references/skills/macos-permissions.md) | Diagnoses TCC denials, Local Network access and stuck Keychain dialogs: Full Disk Access, Screen Recording, Microphone, Camera, Accessibility, Automation. |
| [`macos-watchdog`](references/skills/macos-watchdog.md) | Designs and audits macOS launchd watchdogs: LaunchAgent/LaunchDaemon setup, plist edits, scheduled self-healing, repeated notifications, apps reopening after quit, crash/repair loops, Script Editor alerts... |

### Network and connectivity

| Skill | What it does |
| --- | --- |
| [`cloudflare-troubleshooting`](references/skills/cloudflare-troubleshooting.md) | Investigate and resolve Cloudflare configuration issues using API-driven evidence gathering. Use when troubleshooting ERR_TOO_MANY_REDIRECTS, SSL errors, DNS issues, or any Cloudflare-related problems. |
| [`debugging-network-issues`](references/skills/debugging-network-issues.md) | Investigates network, streaming and protocol failures with falsification-first layered experiments, the general fallback for unknown root causes. |
| [`tunnel-doctor`](references/skills/tunnel-doctor.md) | MUST be used first for tunnel / proxy-path connectivity failures or slow throughput (网络故障 / 连不上 / 代理或隧道下超时). Diagnoses Tailscale, proxy, TUN, DNS and SSH-tunnel problems on macOS and Windows/WSL, e.g. |
| [`windows-remote-desktop-connection-doctor`](references/skills/windows-remote-desktop-connection-doctor.md) | Diagnoses Windows App (Remote Desktop / AVD / W365 / direct PC) connection problems on macOS: transport selection (UDP Shortpath vs WebSocket), VPN/proxy interference, and stuck "Configuring remote PC..." dialogs. |

### Desktop app driving and screen evidence

| Skill | What it does |
| --- | --- |
| [`capture-screen`](references/skills/capture-screen.md) | Programmatic screenshot capture on macOS. Find window IDs with Swift CGWindowListCopyWindowInfo, control application windows via AppleScript (zoom, scroll, select), and capture with screencapture. |
| [`cookie-copy`](references/skills/cookie-copy.md) | Copies selected-site cookies between local profiles of the same macOS Chrome. Use for cookie copy, 复制 Cookie, 搬登录态 or reusing an existing ChatGPT session in an isolated profile. |
| [`ima-copilot`](references/skills/ima-copilot.md) | Installs, diagnoses, repairs, and personalizes the official Tencent IMA skill (a wrapper around upstream ima-skill, not a replacement), including fan-out search across IMA knowledge bases with priority boosting. |
| [`kimi-use`](references/skills/kimi-use.md) | Two scopes: (1) drives Kimi.app via computer-use for Work/Agent data-plugin queries (天眼查、同花顺 iFinD、SEC、IMF etc.) and Chat's built-in 深度研究 report... |
| [`terminal-screenshot`](references/skills/terminal-screenshot.md) | MUST be used right after changing any CLI color config (delta/bat/themes/lazygit pager), renders the terminal's colored output to a PNG so Claude can actually SEE contrast, alignment... |

### Documents and conversion

| Skill | What it does |
| --- | --- |
| [`doc-to-markdown`](references/skills/doc-to-markdown.md) | Converts DOCX/PDF/PPTX and saved HTML/HTM to high-quality Markdown with automatic post-processing. Fixes pandoc grid tables, simple tables, image paths, CJK bold spacing, attribute noise, and code blocks... |
| [`docs-cleaner`](references/skills/docs-cleaner.md) | Consolidates redundant documentation while preserving all valuable content; keeps a doc set truthful after things change. |
| [`docs-router`](references/skills/docs-router.md) | Routes a document request to one bundled specialist for Word, PDF, PPTX, HTML, Excel, scans, Mermaid, DOCX review, or cleanup. |
| [`docx-creator`](references/skills/docx-creator.md) | Produces Word (.docx) and exports existing Word/WPS manuscripts to PDF, preserving revisions, tables and images, especially Chinese formal documents via a verified OpenXML generator with mandatory visual verification. |
| [`excalidraw-use`](references/skills/excalidraw-use.md) | Places existing images onto an Excalidraw whiteboard, turns a slide deck into clean per-slide images, and inspects a .excalidraw file. |
| [`excel-automation`](references/skills/excel-automation.md) | Creates formatted Excel reports with openpyxl, parses complex xlsm financial models with stdlib zipfile+xml when openpyxl fails, and controls Excel windows on macOS via AppleScript. |
| [`feishu-doc-scraper`](references/skills/feishu-doc-scraper.md) | Extracts Feishu/Lark Docs, Wiki, Sheets, and Minutes (妙记) transcripts into faithful local Markdown via the lark-cli API, no LLM paraphrasing, browser-DOM fallback when lark-cli can't reach content. |
| [`mermaid-tools`](references/skills/mermaid-tools.md) | Extracts Mermaid diagrams from markdown files and generates high-quality PNG images using bundled scripts. Activates when working with Mermaid diagrams, converting diagrams to PNG, extracting diagrams from markdown... |
| [`pdf-creator`](references/skills/pdf-creator.md) | Converts Markdown to print-ready PDF with proper Chinese typography, themes and a visual self-check. Use for Markdown to PDF, including documents formatted for printing or mobile reading. |
| [`pdf-to-html`](references/skills/pdf-to-html.md) | Converts a PDF into one self-contained, readable HTML file that preserves images, tables, charts and reading order, optionally translating it into another language while keeping every figure. |
| [`photo-to-scanned-pdf`](references/skills/photo-to-scanned-pdf.md) | Turns phone photos of paper documents into a scanner-look PDF, or adds a synthetic signature, with a mandatory whole-document check. |
| [`ppt-creator`](references/skills/ppt-creator.md) | Deprecated presentation entry retained as a compatibility notice. Use to check the retirement status of ppt-creator or identify a legacy installation. This package does not generate PPTX files. |
| [`read-docx-review`](references/skills/read-docx-review.md) | 读取 Word/WPS 审阅后的 docx，把批注（comments）与修订（track changes）提取成可逐条裁决的 markdown 对账表或 JSON。触发场景：对方批注完的合同/协议/书稿/报告回来了要读意见；「提取 docx 批注」「审阅意见对账」「读一下修订」「谁批了什么、批在哪」；WPS 云文档/Word 在线协作 导出的审阅稿；收到带修订模式改动的回稿要看对方改了什么；已有明确基线... |
| [`report-with-html`](references/skills/report-with-html.md) | Produces the reader-facing HTML artifact, report, dashboard, architecture view, data browser, or review workbench, evidence-backed, browser-verified. |
| [`slides-creator`](references/skills/slides-creator.md) | Deprecated slide-creation entry retained as a compatibility notice. Use to check the retirement status of slides-creator or identify a legacy installation. |
| [`wps-doc-scraper`](references/skills/wps-doc-scraper.md) | Faithfully archive public WPS/KDocs/金山文档 links, especially embedded ProcessOn .pof mind maps and canvases, as raw source data, original SVG/PNG, and Markdown. |

### Finance and market data

| Skill | What it does |
| --- | --- |
| [`ashare-news-fetcher`](references/skills/ashare-news-fetcher.md) | 抓取 A 股消息面情报：从财联社、华尔街见闻、金十、新浪 7x24、东财快讯、 证监会/央行/上交所/财政部政策公告、东方财富股吧等公开来源抓取与股票相关的 新闻、政策、情绪，输出结构化 JSON 或 Markdown。 当用户提到“A 股消息面”、“抓新闻”、“个股消息”、“政策监管”、“股吧情绪”、 “财联社”、“东财快讯”、“市场情绪”或需要把某只股票相关的公开情报聚合出来时 触发。 |
| [`bigdata-skill`](references/skills/bigdata-skill.md) | Pulls Bigdata.com (RavenPack) financial and news data via the official bigdata-client SDK and /v1/* REST endpoints, structured financials, prices, analyst estimates, entity-sentiment series, annotated chunk search... |
| [`daymade-sector-research`](references/skills/daymade-sector-research.md) | A-share sector research: computes board-wide Top N gainers, cross-checks week/month announcement windows across two sources, and grades market-sentiment evidence (L1–L3)... |
| [`financial-data-collector`](references/skills/financial-data-collector.md) | Collects real financial data for any US publicly traded company from free public sources (yfinance) and outputs structured JSON for downstream skills (DCF modeling, comps analysis, earnings review): market data... |
| [`financial-router`](references/skills/financial-router.md) | Routes finance: Bigdata/RavenPack, US fundamentals/yfinance, A-share news/policy, sector Top N/公告, Gangtise/岗底斯 setup. Reads one bundled specialist. |
| [`gangtise-copilot`](references/skills/gangtise-copilot.md) | Gangtise (岗底斯投研) OpenAPI skill suite installer and diagnostic tool. One-click install 19 official skills (data, research, utility), configure accessKey/secretAccessKey, run health diagnostics. |
| [`llm-wiki-setup`](references/skills/llm-wiki-setup.md) | Co-creates a personal investment-research LLM Wiki (Karpathy's pattern) by interviewing the user for THEIR OWN analysis framework, not a template, a living CLAUDE.md of pure markdown + wikilinks... |
| [`pharma-daily-report`](references/skills/pharma-daily-report.md) | 生成 A 股医药行业日报：从新浪财经抓取 20 只核心医药股实时行情，分析 7 大细分赛道排名、涨跌榜 TOP 3、资金流向，然后通过飞书发送富文本日报。 覆盖恒瑞医药、百济神州、智飞生物、药明康德、迈瑞医疗、片仔癀、云南白药等 20 只核心标的。 当用户需要 医药日报、医药行业日报、pharma daily report、 新浪财经医药数据、A 股医药板块分析、飞书推送医药数据、 制药行业快报 时触发。 |

### Research, analysis, and product strategy

| Skill | What it does |
| --- | --- |
| [`app-evolver`](references/skills/app-evolver.md) | Improves an existing application using its code, product contract, authorized work history and competitor evidence. Use for 取长补短、取其精华去其糟粕、参考竞品优化应用 or evolving an app from successful and failed work. |
| [`benchmark-due-diligence`](references/skills/benchmark-due-diligence.md) | Runs adversarial due-diligence on a benchmark the user envies, a founder, KOL, company, or product whose success looks inflated, splitting marketing bubble from real signal... |
| [`competitors-analysis`](references/skills/competitors-analysis.md) | Clones and audits competitor repositories into evidence-based intelligence with file:line citations. Use to track competitors, add a competitor repo, review competitor code, compare capabilities... |
| [`deep-research`](references/skills/deep-research.md) | Creates source-traced research reports with a lead agent, subagent lanes, source governance, and an explicit as-of date. |
| [`devils-advocate`](references/skills/devils-advocate.md) | 结构化压力测试一个论点（devil's advocate / 魔鬼代言人）：把论点拆成显性断言与隐性假设（A1/A2 编号）， 逐条在用户给定的证据材料里检索带出处的反方论证，标 High/Medium/Low 风险等级，补基础比率外部视角， 最后给出「可监测的证伪信号」清单；输出结构化 findings + 人读叙事双层结果。找不到反证时如实声明「未找到」， 绝不编造。 |
| [`fact-checker`](references/skills/fact-checker.md) | Verifies factual claims in documents using web search and official sources, then proposes corrections with user confirmation. |
| [`floorplan-finder`](references/skills/floorplan-finder.md) | Finds existing residential floor plans online and checks layout, entrance orientation, and source identity. Use for 找户型图、按楼栋房号找原图、核对同款或镜像户型. Not for designing, generating, or certifying architectural drawings. |
| [`product-analysis`](references/skills/product-analysis.md) | Multi-path parallel product analysis with cross-model test-time compute scaling. Spawns parallel agents (Claude Code agent teams + Codex CLI) to explore product from multiple perspectives... |
| [`product-growth`](references/skills/product-growth.md) | Diagnoses product growth using business data and actively discovered customer feedback, separates attribution from causal effects, and turns findings into measurable actions. |
| [`prompt-optimizer`](references/skills/prompt-optimizer.md) | Transforms vague prompts or feature requests into precise, testable specifications using EARS (Easy Approach to Requirements Syntax) grounded in relevant domain theories (GTD, BJ Fogg, Gestalt). |
| [`scrapling-skill`](references/skills/scrapling-skill.md) | Install, troubleshoot, and use Scrapling CLI to extract HTML, Markdown, or text from webpages. Use this skill whenever the user mentions Scrapling, `uv tool install scrapling`, `scrapling extract`... |
| [`tech-selection`](references/skills/tech-selection.md) | Gated checklist to choose or review a library, framework, storage, data format, model, build-vs-buy or architecture. Run favorites-search before external research when installed. |

### Audio and video

| Skill | What it does |
| --- | --- |
| [`asr-transcribe-to-text`](references/skills/asr-transcribe-to-text.md) | Transcribes audio or video to speaker-labeled, timestamped text, locally with MLX on Apple Silicon or remotely. |
| [`audio-router`](references/skills/audio-router.md) | Routes audio: StepFun ASR/语音识别, StepFun TTS/配音, transcript/妙记 to 会议纪要, merge/review minutes. Reads one bundled specialist; generic ASR and correction stay direct. |
| [`bilibili-source`](references/skills/bilibili-source.md) | Fetches real, citable Bilibili (B站) video data, stats, metadata, tags, and full danmaku text, via login-free API calls, never hand-typed or estimated. |
| [`cli-demo-generator`](references/skills/cli-demo-generator.md) | Generates professional animated CLI demos as GIFs using VHS terminal recordings. Use to create terminal demos, record CLI workflows as GIFs, generate animated documentation, build demo tapes for README files... |
| [`douban-skill`](references/skills/douban-skill.md) | Export and sync Douban (豆瓣) book/movie/music/game collections to local CSV files via Frodo API. Supports full export (all history) and RSS incremental sync (recent items). |
| [`download-gemini-images`](references/skills/download-gemini-images.md) | Download, export, save, or package images from a Google Gemini conversation/chat/app page, especially uploaded images or generated image previews visible in a Gemini thread. |
| [`meme-creator`](references/skills/meme-creator.md) | Creates video/GIF memes by overlaying images (logos, avatars, stickers) onto moving objects in a clip with frame-accurate tracking, then exports MP4 + GIF. |
| [`stepfun-asr`](references/skills/stepfun-asr.md) | Transcribes Chinese/English audio with StepFun's stepaudio-3-asr-max via its SSE endpoint (not /v1/audio/transcriptions), one call handles long-form audio with no chunking. |
| [`stepfun-tts`](references/skills/stepfun-tts.md) | Generates speech with StepFun contextual TTS, including Chinese/Japanese speech, emotional delivery, inline natural-language directions, cloned voices and batch voice lines. |
| [`twitter-reader`](references/skills/twitter-reader.md) | Fetches Twitter/X post and Article content, text, author, engagement metrics and embedded media, downloading images locally and generating complete Markdown with image references. |
| [`video-comparer`](references/skills/video-comparer.md) | Compares two videos with PSNR and SSIM and builds an interactive HTML report with slider, side-by-side, and grid views. |
| [`youtube-downloader`](references/skills/youtube-downloader.md) | Fetch existing YouTube transcripts/subtitles or archive spoken video content as text, and download YouTube videos/audio or HLS streams (m3u8) with yt-dlp and ffmpeg. |

### UI and design quality

| Skill | What it does |
| --- | --- |
| [`data-visualization-discipline`](references/skills/data-visualization-discipline.md) | The judgment layer for any chart or dashboard, loaded before drawing. Decides the conclusion, statistic, form, color, aggregation, and table shape. |
| [`design-style-picker`](references/skills/design-style-picker.md) | Batch-generate and compare visual design directions so a user can choose the style they actually want. Use when the user says they cannot describe an abstract visual style, asks for many style options... |
| [`frontend-visual-qa`](references/skills/frontend-visual-qa.md) | Audits rendered UI and specific task/object-link handoffs; excludes ordinary source citations alone. Audits already-rendered UI and Markdown/Obsidian image layout, web app, deck/slide, dashboard, design-system... |
| [`i18n-expert`](references/skills/i18n-expert.md) | Sets up and audits internationalization in React or TypeScript, enforces en-US and zh-CN key parity, and localizes errors and plurals. |
| [`interaction-design-board`](references/skills/interaction-design-board.md) | Generates several distinct, clickable HTML interaction prototypes for one product surface into a Design Board and collects selection/remix feedback before implementation. |
| [`llm-icon-finder`](references/skills/llm-icon-finder.md) | Finding and accessing AI/LLM model brand icons from lobe-icons library. Use when users need icon URLs, want to download brand logos for AI models/providers/applications (Claude, GPT, Gemini, etc.)... |
| [`ui-designer`](references/skills/ui-designer.md) | Extract design systems from reference UI images and generate implementation-ready UI design prompts. Use when users provide UI screenshots/mockups and want to create consistent designs, generate design systems... |

### Meetings, writing, and notifications

| Skill | What it does |
| --- | --- |
| [`lark-cli-router`](references/skills/lark-cli-router.md) | Routes any Feishu/Lark/Doubao operation, including recording lookup by date (按日期找会议录音), through the version-matched lark-cli domain guide embedded in the installed CLI, then executes and verifies the task. |
| [`meeting-minutes-taker`](references/skills/meeting-minutes-taker.md) | Transforms raw meeting transcripts into structured, evidence-based meeting minutes, merges multiple versions without losing content, reviews existing minutes against the transcript for missing items... |
| [`notify-wecom`](references/skills/notify-wecom.md) | Send a single one-off message to a WeCom (Enterprise WeChat) group bot. Use this skill whenever the user says "/notify-wecom", "send a quick WeCom message", "企微通知一下", "临时发一条企业微信"... |
| [`setup-notifications-via-wecom`](references/skills/setup-notifications-via-wecom.md) | Set up and send technical status notifications through WeCom (Enterprise WeChat) webhooks. Use this skill whenever the user needs to send notifications, alerts, backup completion reports, or status updates via WeCom... |
| [`teams-channel-post-writer`](references/skills/teams-channel-post-writer.md) | Writes educational Teams channel posts about Claude Code features and best practices, using templates emphasizing concrete examples and underlying principles (e.g. context engineering). |
| [`transcript-fixer`](references/skills/transcript-fixer.md) | Corrects ASR/STT transcription errors, homophones, garbled terms, person-name errors, mixed Chinese/English, with dictionary rules plus Claude's built-in AI, no external API key required. |

### Evaluation and QA

| Skill | What it does |
| --- | --- |
| [`llm-eval-harness`](references/skills/llm-eval-harness.md) | Tests/benchmarks a third-party LLM endpoint (OpenAI- or Anthropic-compatible): availability, fidelity, speed, concurrency, protocol compliance, quality regression. |
| [`promptfoo-evaluation`](references/skills/promptfoo-evaluation.md) | Configures and runs LLM evaluation using Promptfoo framework. Use when setting up prompt testing, creating evaluation configs (promptfooconfig.yaml), writing Python custom assertions... |
| [`qa-expert`](references/skills/qa-expert.md) | Sets up QA testing processes: test strategies, Google Testing Standards test cases, P0-P4 bug tracking, quality metrics, progress reports, autonomous execution via master prompts, and OWASP security testing... |

### Infrastructure and app delivery

| Skill | What it does |
| --- | --- |
| [`developing-ios-apps`](references/skills/developing-ios-apps.md) | Builds and ships iOS/macOS apps with XcodeGen, SwiftUI and SPM: Xcode build fixes, device deployment, Apple Developer signing/notarization, CI/CD pipelines. |
| [`terraform-skill`](references/skills/terraform-skill.md) | Diagnoses and designs safe Terraform releases, provisioners (remote-exec/local-exec/file, cloud-init, Compose, Caddy), multi-environment isolation, and fresh-host bootstrap. |

## Group notes

### Agent CLI setup and model operations

`agent-web-search-setup` proves which built-in search tool is dead on this machine,
removes it, installs a replacement, and proves the replacement inside the agent's own
session. Do not take a user's or your own claim about the broken tool. Never print a
key. `claude-code-hooks` is the structural gate, since a prose rule in CLAUDE.md is a
suggestion. Match tokens with shlex, run `bash -n` and a real JSON event before
registering, converge every profile, and make any release valve a human gate rather
than an environment variable the model can set. A hook needs a termination proof if
it demands remediation.

`claude-switch-models-setup` gives each provider its own `.claude.json` while sharing
skills, hooks, and projects, and never runs the converger against a synthetic main.
`claude-md-progressive-disclosurer` treats line count as a symptom, not a KPI, and
proves every pointer lands on content that already exists before writing it. A fake
pointer is worse than a lost section. `claude-migrate-memory-to-doc` moves only
cross-tool content into tool-agnostic docs and verifies by running Codex, not by
reading the file back.

`claude-code-ping-start-5h-quota` is a one-shot macOS timer, with an idempotency check
before creating anything and an independent readback after. `tibo-reset-codex`
separates announced resets, silent platform resets, banked resets, and account-cycle
resets, crosses official status, live product state, and independent readings, and
converts Pacific time to Beijing. `claude-usage-analyst` keeps observed ccusage
numbers separate from interpretation and never infers plan rules from token counts.

`statusline-generator` treats the statusline as a hot path and budgets subprocesses,
never resolving packages at refresh time, then proves the layout by running it.
`codex-1m-context-window-setup` edits only compaction unless the model catalog proves
the maximum, refuses scope expansion, and stops when the live catalog is unavailable.
`openclaw` audits, diffs, copies, and lists providers and models, while
`openclaw-model-switch` repairs a running instance and checks key routing, provider
plugins, and endpoint pairing before changing a model id. Both back up config and
verify end to end. `local-codex` uses ChatGPT OAuth, never an API key, and gates an
account claim on session id, working directory, and runtime. `peer-message` checks
native tools first and treats a denial, a Held message, or an ambiguous send as
reasons to stop, not to switch channels. `codex-image-gallery` serves a local browser
gallery over Codex image output.

### Local history, continuity, and prior work

Reading is not continuing. `read-claude-code-history` and `read-codex-history` never
resume, never edit the old project, and never turn a read into an action. Use the
index before a raw scan, preserve unread ranges as gaps, and never claim a negative
after a timeout. A compact summary is a continuation aid, not verbatim history.
`local-conversation-history` only routes and never parses. `read-claude-web-conversation`
uses the logged-in Chrome channel, never curl, requests the full tool rendering, and
passes a per-item fidelity gate before calling the transcript complete.

`continue-claude-code-work` and `continue-codex-work` require a verified read receipt,
rebuild the continuation contract with evidence for every field, reconcile it with
the current tree, and then execute the still-unfinished business task. They never run
`--resume` or `--continue`, and never report success when only context was extracted.
`claude-export-txt-better` repairs hard-wrapped exports without modifying the original
and validates every check with PASS or FAIL evidence. `gemini-history-analyzer`
verifies keyword hits in context because most matches are false positives.
`ghostty-use` snapshots Codex and Claude sessions before a reboot, restores exact ids,
audits survivors, and honors host denials. `prior-work-retrieval` runs only on an
explicit reuse request, returns a reuse, adapt, or reject receipt, and treats zero
hits as no evidence rather than proof of absence.

### Skills, plugins, and marketplaces

`skill-creator` starts at the unfinished stage, edits the canonical source rather than
an installed copy, picks a verification tier from the change, and runs a sanitization
pass before delivery. `skill-evolver` runs one research-driven improvement round and
accepts an unchanged skill when the evidence supports keeping it. `skill-reviewer`
separates design quality from measured task benefit, is additive by default, and
never rewrites a skill it was asked only to review.

`skill-governance` keeps intended hot entries visible in a fresh host, keeps cold
capabilities reachable, gives editable behavior one canonical owner, and makes every
retirement recoverable. Never copy a cache directly as installation, never enforce a
single cache version, and never remove the last scoped marketplace. `skills-search`
searches configured local repositories first, executes commands itself, and never
lets an external hit hide a failed local scan. `marketplace-dev` rejects `$schema`,
requires `strict: false` when no `plugin.json` exists, and runs its full checklist
after every manifest change. `marketplace-health-check` runs inline, treats agent
findings as hypotheses, and verifies each high or critical finding with its own
command before reporting. `claude-skills-troubleshooting` treats `lastUpdated` as the
only cache-freshness source.

### Git and GitHub

`git-safety-net` is non-destructive or additive until a step is explicitly labeled
destructive, never concludes unmerged from counts, verifies each branch by content,
and deletes only against a fresh inventory with a retained carrier. It preserves
every reported item and never turns one messy audit into a permanent worktree rule.
`github-ops` treats 2xx as acceptance, not proof, classifies read from write, binds
identity, host, and target, mutates once, and verifies through an independent
readback. It reports the business outcome, not the command.

`github-contributor` reads CONTRIBUTING.md as a hard contract, branches from upstream
main, writes a scope contract, keeps the smallest comparable diff, and follows the
phase order because the right action at the wrong phase still fails. `github-review-pr`
reviews immutable objects against the live base with three-way merges, stays read-only
by default, never touches the user's worktree, and keeps each queue item independent.
`github-sensitive-data-cleanup` scans before deciding, rotates the exposed credential,
backs up, rewrites, verifies, checks repository visibility before any push, and never
uses `--no-verify` or forces past a failed guard. `repomix-safe-mixer` scans for
hardcoded credentials before packing. `repomix-unmixer` extracts to a temp directory
and never writes into an important tree without review.

### macOS system care

`macos-cleaner` finishes a read-only diagnosis before any mutation, confirms the exact
target and host identity, prefers supported controls and Finder Trash, avoids broad
`rm -rf`, preserves user state, and stops between phase 2 and phase 3 when approval is
missing. Printing a plan is not approval. Verify after deletion and prove the cleanup
did not damage user data or a co-resident service.

`macos-load-doctor` reads load average first, runs the process census, attributes each
process to an owner, and classifies the shape before proposing a fix. Never terminate
another session's, agent's, or user's processes. `macos-permissions` reproduces the
reported denial, finds the responsible process in the attribution chain, and does not
replace an interaction bug with password instructions. If the protected read now
succeeds, say the cause is unknown rather than repaired. `macos-watchdog` follows the
quiet-watchdog contract, checks its own premises, separates repair patience from an
observation failure, escalates cooldown, never resurrects an app the user quit, loads
with `launchctl bootstrap`, and reads the native job back.

### Network and connectivity

`debugging-network-issues` is the general fallback for an unknown cause. Verify the
premise, falsify before confirming, isolate one layer at a time, cross-check every
probe with an independent channel, classify each finding, and counter-review before
committing to a cause. A green health check certifies only the path it probes.

`tunnel-doctor` owns the Tailscale, proxy, TUN, DNS, and SSH-tunnel layer. Calibrate a
port probe before trusting it, because under a TUN the local stack answers for the
destination and `remote_ip` is the local endpoint. Verify each plane separately and
never chain fixes with `&&`. A missing guest agent does not settle a question that
needs host console access. `windows-remote-desktop-connection-doctor` separates UDP
Shortpath from WebSocket, looks for the process named `Windows`, and reads Windows App
logs before blaming the network. `cloudflare-troubleshooting` investigates with the
API, never logs a key, and treats an empty exact-zone result as a finding, not proof
the site is absent.

### Desktop app driving and screen evidence

`capture-screen` prefers the host's native window inventory, wraps every AppleScript
call in a timeout, and sleeps one second before capturing so rendering finishes.
`terminal-screenshot` captures full-fidelity ANSI to a file, renders it to PNG, and
reads the image to judge contrast and alignment. Never run `brew install freeze`
because that installs an unrelated GUI app.

`kimi-use` picks the desktop-automation branch first and uses the Kimi plugin loop
only for Work or Agent data queries. `ima-copilot` is a wrapper over the official IMA
skill, never vendors upstream files, asks before touching them, and backs up before
any repair. `cookie-copy` works only between profiles of the same macOS Chrome under
the same OS user, copies only an authorized site, keeps backups outside the skill and
Git, verifies the expected ChatGPT account, and never logs cookie values.

### Documents and conversion

`docs-router` selects exactly one document specialist and does not choose a Daymade
child for a new slide deck. `doc-to-markdown` converts DOCX, PDF, PPTX, and saved HTML
with post-processing for tables, image paths, CJK spacing, attribute noise, OCR
garbage, and repeated headers. `pdf-creator` requires visual inspection, treats exit
code 3 as not a pass, checks table borders, and verifies copied commands against the
rendered PDF. `pdf-to-html` runs extract, look, translate, build, and verify, and
delivers one self-contained file with every figure preserved.

`docx-creator` is a thin layer over `minimax-docx`, not an engine. Alignment follows
content role, independent lists restart while continuations keep numbering, CJK fonts
need both font slots, and the visual verification chain is mandatory.
`read-docx-review` reads comments and track changes through the OpenXML engine because
python-docx misses insertions and deletions, and it stays read-only on the other
party's file. `feishu-doc-scraper` extracts through `lark-cli` first, never lets the
document body pass through the model, disables the proxy for Feishu domestic domains,
follows the reference graph breadth first, and runs the residual-tag acceptance gate.
`wps-doc-scraper` archives public links only, never logs in, keeps raw payloads, and
does not infer hidden nodes.

`docs-cleaner` runs the drift test, accounts for every copy of a fact before changing
it, computes derived values instead of writing them, and retires a document whose
premise is gone rather than patching it. `excel-automation` runs `file` before trusting
an extension, uses openpyxl for creation and zipfile plus XML for complex xlsm files,
and wraps Excel AppleScript in a timeout. `mermaid-tools` uses the bundled scripts.
`excalidraw-use` never overwrites a live board and builds a deck from source before
shooting it. `report-with-html` lets the reader's question choose the skeleton,
grounds every section in real evidence, and hands delivery acceptance to an
independent agent. `photo-to-scanned-pdf` rectifies, enhances, assembles, and then
reads a whole-document contact sheet. For identity documents it reconciles the
required sides and the recipient's accepted form. `ppt-creator` and `slides-creator`
are retirement notices and do not generate a deck.

### Finance and market data

`financial-router` selects one finance specialist and never a sequence.
`bigdata-skill` reaches the RavenPack SDK and REST substrate the MCP does not expose,
never hardcodes a key, never invents an endpoint or schema, and keeps chunk cost
visible. `financial-data-collector` forbids fallback values. A missing field is
`null` with `_source: "missing"`, every section carries source attribution, and
yfinance free cash flow is flagged when it ignores stock-based compensation.

`ashare-news-fetcher` collects public Chinese market and policy items into structured
JSON or Markdown. `daymade-sector-research` ranks a sector, checks announcement
windows across two sources, grades sentiment evidence, and runs adversarial
verification. Its first rule is to mark uncertainty rather than give a wrong answer,
and every conclusion traces to a primary source. `gangtise-copilot` installs and
diagnoses the official Gangtise suite without vendoring it and asks before touching
upstream files. `pharma-daily-report` pulls 20 core pharma stocks from Sina and sends
a Feishu report. `llm-wiki-setup` co-creates the user's own investment framework as
plain Markdown with wikilinks, interviews rather than imposing a template, and keeps
retrieval out of the compilation layer.

### Research, analysis, and product strategy

`deep-research` runs a lead agent with subagent lanes, enforces source governance and
an `AS_OF` date, requires an original-source retrieval channel for load-bearing
claims, and never promotes a summary to final evidence. `fact-checker` checks claims
against authoritative sources, always states the date context, and applies corrections
only with user approval. `devils-advocate` numbers explicit claims and hidden
assumptions, hunts counterevidence in the supplied material with citations, assigns
High, Medium, or Low risk, adds a base rate, and ends with falsification signals. It
declares "not found" rather than inventing a counterargument.

`benchmark-due-diligence` assumes the benchmark is inflated until proven otherwise,
guards two injection channels, runs inline rather than forked, and ends with what the
evidence means for this user. `competitors-analysis` clones the competitor and cites
`file:line`, keeping strategic inference separate from repository fact.
`product-analysis` runs Claude and Codex perspectives in parallel and cross-validates
before synthesis. `product-growth` reconstructs the value journey, tests explanations
before assigning causes, scopes every claim to its population and window, and never
promises growth or spends without authorization. `app-evolver` orchestrates an
improvement round, keeps repository, research, and release work with their owners,
and never transfers one platform's contract to another.

`floorplan-finder` retrieves an existing original and never substitutes a generated
drawing, preserves the identity gap, and does not bypass a portal wall.
`prompt-optimizer` converts a vague request into an EARS specification grounded in a
named domain theory. `tech-selection` treats criteria as filters, keeps every
candidate visible, refuses to promote an `unknown` to a pass, runs favorites-search
first, and stops at a tradeoff only the user can decide. `scrapling-skill` verifies
the install, runs the smallest command, inspects the saved file, and escalates to a
browser-backed fetch only when static content is missing.

### Audio and video

`audio-router` chooses one audio specialist by the requested result and does not pick
StepFun merely because the user said transcribe. `asr-transcribe-to-text` treats the
transcript as the result rather than the run, labels speakers by default, chooses the
long local route or the short MLX route explicitly, keeps continuous-context ASR
before diarization, verifies the output, and does not paste a long copyrighted
transcript into chat. `stepfun-asr` must hit the SSE endpoint with the matching model,
because the wrong endpoint reports a model error, and it never omits a parameter
silently. `stepfun-tts` drives the bundled wrapper, reads the current API reference,
does not invent SSML, and checks listening quality rather than only synthesis success.

`meme-creator` binds identity before fetching an avatar, tracks only the chosen scene,
and verifies the encoded MP4 and GIF. `video-comparer` measures PSNR and SSIM and
builds an interactive HTML report. `youtube-downloader` decides file versus text
first, runs every command itself for a non-technical user, and follows the transcript
path before downloading audio. `bilibili-source` uses login-free APIs for real
engagement numbers, never estimates them, and does not bypass the login that subtitles
require. `douban-skill` exports through the Frodo API rather than scraping.
`twitter-reader` uses the fxtwitter mirror for post text and the article fetcher for
images. `download-gemini-images` opens the lightbox in the logged-in Chrome session
and never inspects cookies or session stores. `cli-demo-generator` records VHS tapes
and encodes complex commands instead of feeding raw special characters to the parser.

### UI and design quality

`data-visualization-discipline` is the judgment layer and loads before any chart is
drawn. Decide the conclusion the reader should reach, verify the statistic and the
denominator, choose the form that answers that question, keep one entity in one color
and one position across figures, and use a dual axis only when the relationship is
honest. `design-style-picker` generates comparable visual options when the user cannot
describe a style, then implements from the chosen references. `interaction-design-board`
freezes the product facts, generates isolated runnable interaction candidates, makes
the user operate them, and only then freezes approval. It never writes prototypes into
production directories and never lets a static image stand in for interaction.

`ui-designer` extracts a design system from reference images, writes the PRD, and
composes an implementation prompt. `frontend-visual-qa` is audit-only by default,
proves the target, state, and viewport, captures real rendered evidence, selects the
evidence level the claim requires, and never promotes a weaker level into a stronger
conclusion. `i18n-expert` configures the framework, removes hardcoded strings,
enforces en-US and zh-CN parity, localizes error codes, and never exposes a raw
`error.message` to the UI. `llm-icon-finder` resolves lobe-icons CDN URLs in SVG, PNG,
and WebP with light, dark, and color variants.

### Meetings, writing, and notifications

`meeting-minutes-taker` runs multiple complete passes and unions them, because a
single pass loses content. It never assumes a speaker identity, identifies decisions
by their elements rather than their phrasing, hit-tests each claim against the
retrievable layer, and runs a revocation scan before promoting a decision.
`transcript-fixer` completes Stage 1 deterministic fixes, then the native AI
correction, then compounds confirmed recurring fixes. It never rewrites speech for
fluency, reads the global and project rosters before correcting a name, and treats an
unfamiliar token as unknown rather than an error.

`teams-channel-post-writer` teaches with concrete examples and verifies release facts
against authoritative sources. `lark-cli-router` is the only Lark entry, loads the
smallest version-matched guide set, reads every required file, never bypasses the CLI
with curl or a browser, and does not treat an outer `ok` as proof that every item
succeeded. `notify-wecom` sends one message and respects the recipient scope, where
`self` may send directly and `others` needs the labeled confirmation gate.
`setup-notifications-via-wecom` leads with what happened, separates state from delta,
defines every number, omits hashes and paths, and ends with a next action.

### Evaluation and QA

`llm-eval-harness` measures availability, request fidelity, speed, concurrency,
protocol compliance, and blind-judged quality against a real endpoint. It never probes
a client-side bracket marker as a model id, never concludes from one run, and reports
`inconclusive` when the evidence does not separate the hypotheses.
`promptfoo-evaluation` configures prompts, providers, tests, assertions, Python
assertions, and `llm-rubric`, with concurrency under `commandLineOptions` rather than
at the top level. `qa-expert` sets up AAA test cases, Google testing standards,
P0 to P4 bug tracking, quality metrics, OWASP security coverage, and a third-party
handoff package.

### Infrastructure and app delivery

`terraform-skill` treats a valid-looking workflow as a way to publish unvalidated
bytes. Plan counts are not the outcome. It covers provisioner traps, staging and
production key parity, state lineage after a failed apply, and rollback through the
same CI. It never adds `-force`, never substitutes a local apply for the authorized
path, and stops after the requested result is verified. `developing-ios-apps` covers
XcodeGen projects, SwiftUI and SPM, device deployment, signing, notarization, and CI.
It handles `@rpath` crashes and code-signing errors, and it never clears the global SPM
cache.
