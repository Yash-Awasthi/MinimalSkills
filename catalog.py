#!/usr/bin/env python3
"""Segregate skill folders into subject folders by reading every SKILL.md.

- reads frontmatter name/description of each skill (per file)
- scores against subject keyword rules, highest score wins (ties by rule order)
- --apply moves each pack folder into catalog/<subject>/ and writes indexes
- writes catalog/_classification.tsv for audit
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
PACKS = os.path.join(ROOT, "packs")
CATALOG = os.path.join(ROOT, "catalog")
MANIFEST = os.path.join(ROOT, "repos.manifest.tsv")
REPOS = os.path.join(ROOT, "repos")

RULES = [
 ("cyber-security", [
  "security", "penetration test", "pentest", "red team", "blue team", "purple team",
  "malware", "ransomware", "threat model", "threat intel", "threat hunting", "exploit",
  "vulnerability", "cve", "mitre", "attack surface", "siem", "soc analyst", "forensic",
  "incident response", "osint", "recon", "phishing", "privilege escalation",
  "lateral movement", "reverse engineering", "fuzzing", "hardening", "zero trust",
  "bug bounty", "appsec", "xss", "sql injection", "ssrf", "csrf", "firewall", "waf",
  "edr", "honeypot", "adversary", "secret scanning", "ctf", "security review",
  "security audit", "secure code", "supply chain security", "cryptography",
  "encryption", "password", "credential", "access control", "penetration", "cyber",
  "red-team", "redteam", "threat detection", "log analysis", "network security",
  "cloud security", "container security", "sast", "dast", "bug identification",
  "crash analysis", "idor", "sqli", "xxe", "rce", "open redirect",
  "parameter pollution", "race condition", "initial access", "windows mitigations",
  "offensive", "fast-checking", "penetration tester", "web2 recon",
  "model signature", "provenance", "tls", "ssl", "hsts", "cipher", "downgrade attack",
 ]),
 ("compliance-audit", [
  "gdpr", "iso 27001", "iso27001", "soc 2", "soc2", "hipaa", "pci dss", "pci-dss",
  "nist", "cmmc", "fedramp", "audit prep", "compliance", "regulatory", "data protection",
  "privacy", "ai act", "mdr", "fda", "iso 13485", "sox", "governance risk",
  "risk assessment", "policy", "certification", "iso 42001", "cra readiness",
  "audit readiness", "capa", "qms", "corrective action", "medical device qms", "42001",
  "iso 14971", "fmea", "hazard analysis", "ai management system", "gap analysis",
  "model signature", "provenance",
 ]),
 ("healthcare-medical", [
  "healthcare", "health care", "medical", "clinical", "patient", "hipaa", "fhir",
  "ehr", "emr", "medical device", "fda", "iso 13485", "mdr", "therapeutic",
  "diagnosis", "triage", "care plan", "telemedicine", "wearable health", "vitals",
  "ecg", "hrv", "sleep analysis", "nutrition", "fitness", "wellness", "health data",
 ]),
 ("frontend-ui", [
  "react", "next.js", "nextjs", "vue", "svelte", "angular", "solidjs", "tailwind", "css",
  "html", "accessibility", "a11y", "wcag", "design system", "component library", "shadcn",
  "storybook", "responsive", "animation", "framer", "three.js", "threejs", "webgl",
  "canvas", "frontend", "front-end", "state management", "redux", "zustand",
  "ui component", "landing page", "web design", "dom", "browser extension", "pwa",
  "web performance", "core web vitals", "svg", "layout",   "theme", "styling", "ui kit", "form validation", "routing", "hydration", "ssr", "client-side",
  "web app", "web ui", "interface", "aurora ui", "d3", "d3js", "data visualization",
  "makepad", "cross-platform ui",
 ]),
 ("backend-api", [
  "backend", "back-end", "api design", "rest api", "graphql", "grpc", "microservice",
  "database", "postgres", "postgresql", "mysql", "sqlite", "mongodb", "redis", "prisma",
  "orm", "authentication", "authorization", "oauth", "jwt", "session", "webhook",
  "message queue", "kafka", "rabbitmq", "payment", "stripe", "rate limit", "caching",
  "server", "django", "rails", "fastapi", "express", "nestjs", "node.js", "laravel",
  "php", "spring", "dotnet", ".net", "crud", "multitenant", "file upload", "cron",
  "background job", "api integration", "endpoint", "sql query", "data model",
  "schema design", "c++", "asio", "tcp", "udp", "networking code", "audit log",
  "audit trail", "job queue", "queue", "bullmq", "redis-backed",
 ]),
 ("mobile", [
  "ios", "android", "swift", "swiftui", "kotlin", "jetpack compose", "react native",
  "flutter", "expo", "mobile app", "app store", "play store", "xcode", "gradle",
  "push notification", "deep link", "mobile", "uikit", "android studio",
 ]),
 ("devops-cloud", [
  "docker", "kubernetes", "k8s", "helm", "terraform", "ansible", "pulumi", "ci/cd",
  "cicd", "github actions", "gitlab ci", "jenkins", "deployment", "aws", "azure", "gcp",
  "cloud", "serverless", "lambda", "s3", "ec2", "ecs", "eks", "cloudfront", "vercel",
  "netlify", "cloudflare", "nginx", "linux", "ubuntu", "bash script", "shell script",
  "networking", "dns", "vpn", "load balancer", "observability", "monitoring",
  "prometheus", "grafana", "datadog", "opentelemetry", "logging", "tracing", "sre",
  "uptime", "disaster recovery", "backup", "infrastructure as code", "iac", "vps", "ssh",
  "systemd", "finops", "cost optimization", "gitops", "container",
  "platform engineering", "release pipeline", "chaos engineering", "chaos experiment",
  "gameday", "fault injection", "feature flag", "kill switch", "ci cd", "build pipeline",
  "workflow file", "rhdh", "backstage",
 ]),
 ("blockchain-web3", [
  "solidity", "smart contract", "ethereum", "evm", "web3", "defi", "nft", "dao",
  "blockchain", "crypto wallet", "zk proof", "zero-knowledge", "layer 2", "rollup",
  "foundry", "hardhat", "solana", "bitcoin", "tokenomics", "on-chain", "wallet",
 ]),
 ("data-ml", [
  "machine learning", "deep learning", "pytorch", "tensorflow", "keras", "scikit",
  "fine-tun", "training data", "dataset", "feature engineering", "model training",
  "embeddings", "vector database", "rag", "retrieval augmented", "nlp",
  "natural language", "computer vision", "image classification", "object detection",
  "speech recognition", "statistics", "pandas", "numpy", "jupyter", "data pipeline",
  "etl", "data warehouse", "dbt", "spark", "airflow", "data quality", "data engineering",
  "analytics engineering", "recommendation", "time series", "mlops", "huggingface",
  "transformer", "model evaluation", "benchmark", "inference", "quantization",
  "machine-learning", "data science", "classifier",
 ]),
 ("integrations-automation", [
  "composio", "rube", "automate ", "task automation", "app automation",
  "integration platform", "ipaas", "zapier", "n8n", "make.com", "mcp server",
  "third-party integration", "api integration", "connector", "no-code", "low-code",
  "wecom", "group bot", "send a message", "notify", "apify", "connected apps",
 ]),
 ("ai-agents", [
  "agent", "subagent", "multi-agent", "prompt", "system prompt", "mcp",
  "model context protocol", "skill authoring", "agent skill", "claude code", "codex",
  "opencode", "cursor rules", "memory", "context engineering", "tool use",
  "function calling", "orchestration", "agentic", "autonomous", "planner",
  "eval harness", "agent evaluation", "langchain", "langgraph", "crewai", "autogen",
  "openai api", "anthropic api", "llm", "chatbot", "assistant", "copilot",
  "workflow agent", "human-in-the-loop", "ai coding", "vibe coding", "spec-driven",
  "ralph", "gstack", "pstack", "coach me", "using claude", "claude tricks",
  "context files", "company context",   "agenthub", "reusable skill", "goal prompt",
  "grading rubric", "agent grading", "delegating", "skill.md", "hub-init",
  "hub-run", "hub-status", "rank finished", "which agent won", "aas",
  "deliberation queue", "checkpointed", "development loop", "spec-build-review",
  "context management", "project guidelines", "router over the skills",
 ]),
 ("hardware-iot", [
  "embedded", "iot", "esp32", "stm32", "arduino", "firmware", "pcb", "microcontroller",
  "raspberry pi", "pico", "rtos", "sensor", "robotics", "can bus", "modbus",
  "plc", "industrial automation",
 ]),
 ("testing-qa", [
  "test", "testing", "qa", "e2e", "end-to-end", "playwright", "cypress", "selenium",
  "puppeteer", "jest", "vitest", "pytest", "unit test", "integration test", "tdd",
  "test-driven", "coverage", "mutation test", "load test", "k6", "locust", "smoke test",
  "regression", "test plan", "test automation", "flaky", "mocking", "fixture",
  "browser automation", "contract test", "snapshot test", "test suite",
  "testing library",
 ]),
 ("code-quality", [
  "code review", "pull request", "refactor", "refactoring", "debugging", "debug",
  "root cause", "cleanup", "lint", "static analysis", "codebase", "architecture",
  "design pattern", "solid principle", "technical debt", "legacy", "migration",
  "upgrade", "dependency", "performance", "profiling", "optimization", "git", "commit",
  "branching", "merge conflict", "monorepo", "complexity", "naming", "code smell",
  "best practice", "code tour", "dead code", "type safety", "typescript",
  "adversarial review", "hostile reviewer", "reviewer persona", "diff", "pr before merge",
  "focused fix", "make it work", "end to end", "engineering skill", "which engineering",
  "self-eval", "devil's-advocate", "merge-ready", "pr checks", "until green",
  "comment sicko", "verify a claim", "falsifiably", "implement a piece of work",
  "tracer-bullet", "to-tickets", "tickets", "language-specific", "composition patterns",
  "comprehensive review", "reversible work", "never block", "concise planning",
  "coding task", "type system", "function signature", "logic bug", "execution tracing",
  "logic review", "principle-",
 ]),
 ("design-ux", [
  "design", "ux", "ui/ux", "user experience", "wireframe", "prototype", "figma",
  "sketch", "adobe xd", "brand", "branding", "logo", "icon", "illustration",
  "color palette", "visual identity", "mockup", "usability", "user research", "persona",
  "journey map", "information architecture", "design critique", "aesthetic",
  "style guide", "typography", "graphic", "visual design", "ui design", "ux design",
  "product design", "human interface", "apple hig", "hig",
 ]),
 ("product-management", [
  "product manager", "product management", "prd", "product requirement", "roadmap",
  "backlog", "user story", "acceptance criteria", "sprint", "agile", "scrum", "kanban",
  "jira", "prioritization", "stakeholder", "okr", "discovery", "product strategy",
  "feature spec", "launch plan", "go-to-market", "competitor analysis",
  "market research", "product vision", "requirements", "epic", "milestone",
  "release planning", "product analytics", "product risk", "before you build",
  "alternatives", "demand",
 ]),
 ("strategy-executive", [
  "c-level", "c-suite", "board", "boardroom", "investor", "fundraising", "m&a",
  "merger", "acquisition", "reorg", "executive", "advisor", "qbr", "pre-mortem",
  "premortem", "decision", "strategy", "strategic", "okr", "operating cadence",
  "ceo", "cto", "cfo", "coo", "cmo", "ciso", "chro", "chief", "memo",
  "business model", "market entry", "competitive matrix", "challenge a plan",
  "challenge a roadmap", "challenge a forecast", "challenge the", "venture",
  "career bet", "commercial", "deal review", "pricing change", "board deck",
  "investor update", "change management", "channel economics", "hard call", "grill",
  "shared understanding", "term sheet", "layoff", "down round", "assumptions",
  "postmortem", "blameless", "5-whys", "missed quarter",
 ]),
 ("marketing-growth", [
  "seo", "search engine optimization", "marketing", "copywriting", "copy",
  "content marketing", "blog post", "social media", "instagram", "tiktok", "linkedin",
  "twitter", "thread", "ads", "google ads", "facebook ads", "ppc", "email campaign",
  "newsletter", "funnel", "conversion", "growth", "crm", "hubspot", "salesforce",
  "sales", "lead generation", "cold email", "outreach", "influencer", "affiliate",
  "brand awareness", "aeo", "landing", "campaign", "audience", "positioning",
  "demand gen", "webinar", "case study", "testimonial", "community", "waitlist",
  "alternative page", "comparison page", "competitive matrix", "sentiment", "trends",
  "what people are saying", "blog intro", "article angle", "schema markup", "anchor text",
  "backlink", "canonical url", "competitor gap", "analytics tracking", "tracking plan",
  "seo audit",
 ]),
 ("writing-docs", [
  "technical writing", "documentation", "docs", "readme", "api reference", "tutorial",
  "how-to", "editing", "proofread", "grammar", "translation", "localization", "summarize",
  "summary", "notes", "changelog", "release notes", "writing", "author", "editor",
  "grant", "presentation", "slides", "report", "white paper", "style", "rewrite",
  "tone of voice", "content", "docx", "markdown", "pdf", "communication style",
  "terse", "token-efficient", "reply style", "write like", "reply like", "terse mode",
  "direct and warm", "no lists", "human-sounding", "restate", "in your own words",
  "catch the user up", "explain a body of work", "teach the user", "re-pitch",
  "plain human language", "learning progress", "learning plan", "sycophantic",
  "agreement patterns",
 ]),
 ("business-finance", [
  "finance", "financial", "accounting", "bookkeeping", "invoice", "payroll", "budget",
  "forecasting", "revenue", "pricing", "unit economics", "investment", "portfolio",
  "stock", "trading", "valuation", "due diligence", "cfo", "business plan", "legal",
  "contract", "terms of service", "nda", "procurement", "operations", "supply chain",
  "ecommerce", "shopify", "customer support", "support ticket", "business", "company",
  "startup", "founder", "saas metrics", "arr", "churn", "change management",
  "rollout", "channel economics", "cost to serve", "channel roi", "retention",
  "customer success", "churn risk", "deal desk", "discount", "redline", "msa",
  "term sheet", "ip assignment", "health score", "expansion", "layoff", "down round",
  "legal research", "lawyer", "juridica", "minutas", "law firm",
 ]),
 ("media-creative", [
  "video", "youtube", "film", "ffmpeg", "audio", "podcast", "music", "voice", "tts",
  "image generation", "midjourney", "stable diffusion", "photo", "image editing",
  "thumbnail", "3d", "blender", "rendering", "storyboard", "cinematic", "animation",
  "sprite", "graphics", "media", "streaming",   "subtitle", "transcription", "screenshot", "image realism", "image model", "video editing",
 ]),
 ("game-dev", [
  "game", "unity", "unreal", "godot", "roblox", "minecraft", "game design",
  "level design", "gameplay", "multiplayer game", "game engine", "shader", "voxel",
  "physics engine", "game art", "game mechanic", "rpg", "quest",
 ]),
 ("office-productivity", [
  "meeting", "calendar", "email", "gmail", "outlook", "notion", "obsidian", "slack",
  "teams", "excel", "spreadsheet", "google sheets", "pdf", "powerpoint", "keynote",
  "task management", "todoist", "trello", "asana", "linear", "inbox", "time tracking",
  "personal", "resume", "cv", "travel", "health", "fitness", "habit", "journal",
  "recipe", "shopping",   "note-taking", "knowledge base", "second brain",
  "file organization", "productivity", "automation", "zapier", "n8n",
  "brain dump", "weekly review", "confluence", "inbox", "blueprint", "page layout",
  "atlassian", "capture this", "google workspace",   "health data", "wellness",
  "medical", "checkup", "健康", "health analysis",
 ]),
 ("research-academic", [
  "research", "paper", "literature review", "citation", "arxiv", "academic", "thesis",
  "dissertation", "experiment design", "scientific", "bioinformatics", "biology",
  "chemistry", "physics", "math", "proof", "peer review", "replication", "lab",
  "university", "scholar", "bibliography", "autoresearch", "experiment on a schedule",
  "experiment iteration", "deepread", "deep read", "document set", "lecun", "debate",
 ]),
 ("education-learning", [
  "edtech", "education", "school", "student", "teacher", "classroom", "curriculum",
  "lesson plan", "lesson", "course design", "course", "syllabus", "lms",
  "learning management", "moodle", "google classroom", "roster", "assessment",
  "quiz", "tutoring", "training program", "learning path",
 ]),
 ("hr-people", [
  "hiring", "recruiting", "interview", "candidate", "onboarding", "offboarding",
  "performance review", "people management", "team building", "culture", "hr",
  "compensation", "org design", "feedback", "coaching", "mentoring", "one-on-one",
  "employee", "talent", "job description",
 ]),
]


def clean(s):
    return s.replace("\r", "").strip()


def parse_skill(path, depth=0):
    try:
        with open(path, encoding="utf-8", errors="ignore") as fh:
            txt = fh.read(12000)
    except OSError:
        return "", ""
    name = desc = ""
    m = re.match(r"---\s*\n(.*?)\n---", txt, re.S)
    if m:
        fm = m.group(1)
        nm = re.search(r"^name:\s*(.+)$", fm, re.M)
        if nm:
            name = nm.group(1).strip().strip("\"'")
        dm = re.search(r"^description:\s*(.+?)(?=^[A-Za-z][\w-]*:\s|\Z)", fm, re.M | re.S)
        if dm:
            desc = " ".join(dm.group(1).split()).strip("\"'")
    if not desc:
        body = re.sub(r"^---.*?---", "", txt, flags=re.S)
        for line in body.splitlines():
            line = line.strip()
            if line and not line.startswith("#") and not line.startswith("```"):
                desc = line[:300]
                break
    if depth < 2 and re.match(r"^(?:\.{1,2}/|/).+\.md$", desc):
        target = os.path.normpath(os.path.join(os.path.dirname(path), desc))
        if not os.path.isfile(target):
            tail = desc
            while tail.startswith("../"):
                tail = tail[3:]
            if tail.startswith("./"):
                tail = tail[2:]
            if os.path.isdir(REPOS):
                for repo in sorted(os.listdir(REPOS)):
                    cand = os.path.join(REPOS, repo, tail)
                    if os.path.isfile(cand):
                        target = cand
                        break
        if os.path.isfile(target) and os.path.abspath(target) != os.path.abspath(path):
            n2, d2 = parse_skill(target, depth + 1)
            name = name or n2
            if d2:
                desc = d2
    return clean(name), clean(desc)[:400]


def classify(label, name, desc):
    text_name = (label + " " + name).lower().replace("-", " ").replace("_", " ")
    d = desc.lower()
    if "composio" in d or "rube mcp" in d or "via rube" in d:
        return "integrations-automation", 9
    best, best_s, second = "general", 0, 0
    for cat, kws in RULES:
        s = 0
        for kw in kws:
            k = kw.lower()
            if k in text_name:
                s += 4
            elif k in d:
                s += 1
        if s > best_s:
            second = best_s
            best, best_s = cat, s
        elif s > second:
            second = s
    if best_s < 1:
        return "general", 0
    return best, best_s - second


def skill_files(pack):
    out = []
    for base, dirs, files in os.walk(pack):
        dirs[:] = [x for x in dirs if x != ".git"]
        if "SKILL.md" in files:
            out.append(os.path.join(base, "SKILL.md"))
    return out


def topic_of(pack):
    root_skill = os.path.join(pack, "SKILL.md")
    if os.path.isfile(root_skill):
        n, d = parse_skill(root_skill)
        return classify(os.path.basename(pack), n, d)
    files = skill_files(pack)
    if files:
        n, d = parse_skill(files[0])
        return classify(os.path.basename(pack), n, d)
    return "general", 0


def move_packs():
    if not os.path.isdir(PACKS):
        return 0
    moved = 0
    for name in sorted(os.listdir(PACKS)):
        src = os.path.join(PACKS, name)
        if not os.path.isdir(src):
            continue
        cat, _margin = topic_of(src)
        destdir = os.path.join(CATALOG, cat)
        os.makedirs(destdir, exist_ok=True)
        dest = os.path.join(destdir, name)
        if os.path.exists(dest):
            print("CONFLICT", name)
            continue
        os.replace(src, dest)
        moved += 1
    return moved


def write_indexes():
    subjects = {}
    audit = []
    for cat in sorted(os.listdir(CATALOG)):
        cdir = os.path.join(CATALOG, cat)
        if not os.path.isdir(cdir) or cat.startswith("_"):
            continue
        entries = []
        for pack in sorted(os.listdir(cdir)):
            pdir = os.path.join(cdir, pack)
            if not os.path.isdir(pdir):
                continue
            for sf in skill_files(pdir):
                n, d = parse_skill(sf)
                if not n:
                    n = os.path.basename(os.path.dirname(sf))
                rel = os.path.relpath(os.path.dirname(sf), ROOT).replace("\\", "/")
                entries.append((n, d, rel))
                audit.append((cat, n, d, rel))
        entries.sort(key=lambda x: x[0].lower())
        subjects[cat] = entries
        with open(os.path.join(cdir, "INDEX.md"), "w", encoding="utf-8") as f:
            f.write(f"# {cat}\n\n{len(entries)} skills. Classified from each SKILL.md.\n\n")
            f.write("| Skill | What it is for | Path |\n| --- | --- | --- |\n")
            for n, d, rel in entries:
                d = " ".join(d.split()).replace("|", "\\|")[:260]
                f.write(f"| `{n}` | {d} | `{rel}` |\n")

    with open(os.path.join(CATALOG, "_classification.tsv"), "w", encoding="utf-8") as f:
        f.write("subject\tskill\tdescription\tpath\n")
        for row in audit:
            f.write("\t".join(x.replace("\t", " ") for x in row) + "\n")

    repo_rows = []
    if os.path.isfile(MANIFEST):
        with open(MANIFEST, encoding="utf-8") as f:
            next(f, None)
            for line in f:
                p = line.rstrip("\n").split("\t")
                if len(p) >= 7:
                    repo_rows.append(p)
    repo_rows.sort(key=lambda r: r[0].lower())

    with open(os.path.join(CATALOG, "REPOS.md"), "w", encoding="utf-8") as f:
        f.write("# Source repositories\n\n"
                "Shallow mirrors used as raw material; the skills above live in subject folders.\n\n"
                "| Repo | Skills | Commit | Source |\n| --- | --- | --- | --- |\n")
        for r in repo_rows:
            f.write(f"| `{r[0]}` | {r[5]} | `{r[3]}` | {r[1]} |\n")

    total = sum(len(v) for v in subjects.values())
    with open(os.path.join(ROOT, "INDEX.md"), "w", encoding="utf-8") as f:
        f.write("# Skills index\n\n")
        f.write(f"{total} skills across {len(subjects)} subject folders. "
                "Every row was classified by reading that skill's own SKILL.md.\n\n")
        f.write("| Subject | Skills | Index |\n| --- | --- | --- |\n")
        for cat in sorted(subjects, key=lambda c: (-len(subjects[c]), c)):
            f.write(f"| [{cat}](catalog/{cat}/INDEX.md) | {len(subjects[cat])} | `catalog/{cat}/` |\n")
        f.write(f"\nSource mirrors: {len(repo_rows)} repos - see [catalog/REPOS.md](catalog/REPOS.md) "
                "and `repos.manifest.tsv`.\n")
        f.write("\nMaintenance: `./update-repos.sh` refreshes mirrors and the manifest; "
                "`python catalog.py --apply` re-indexes after adding packs.\n")
    return subjects, total


if __name__ == "__main__":
    if "--apply" not in sys.argv:
        counts = {}
        for name in sorted(os.listdir(PACKS)):
            p = os.path.join(PACKS, name)
            if os.path.isdir(p):
                c, _m = topic_of(p)
                counts[c] = counts.get(c, 0) + 1
        for c, n in sorted(counts.items(), key=lambda x: -x[1]):
            print(f"{n:6d}  {c}")
        print("total", sum(counts.values()))
        sys.exit(0)
    moved = move_packs()
    subjects, total = write_indexes()
    print(f"moved {moved} pack folders")
    for c in sorted(subjects, key=lambda x: -len(subjects[x])):
        print(f"{len(subjects[c]):6d}  {c}/")
    print("indexed", total, "skills")
