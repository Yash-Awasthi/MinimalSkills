# Archive: anthropic-skills

252 `anthropic-*` top-level skill folders moved here after compaction into
`curated/ai-agents/anthropic-skills/`. They contain 279 skill directories: 20
official Anthropic skills, 232 knowledge-work plugin skills, and 27 nested
platform skills inside `video-sdk`, `meeting-sdk`, `contact-center`,
`virtual-agent`, and `zoom-mcp`.

Original relative path preserved: `catalog/<subject>/<folder>`.

Mapping to skill and group: `curated/ai-agents/anthropic-skills/SOURCES.md`.
Full bodies: `curated/ai-agents/anthropic-skills/references/skills/`.
Language guides, MCP and SDK references, runbooks, office schemas, scripts,
examples, and templates:
`curated/ai-agents/anthropic-skills/references/assets/`.

Restore one top-level skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\anthropic-skills\catalog\<subject>\<folder>" `
          -Destination "C:\github\skills\catalog\<subject>\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\anthropic-skills\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
