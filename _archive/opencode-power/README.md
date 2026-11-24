# Archive: opencode-power

57 `opencode*` skills moved here after compaction into
`curated/ai-agents/opencode-power/`.

Original relative path preserved: `catalog/<subject>/<folder>`.

Mapping to skill and group: `curated/ai-agents/opencode-power/SOURCES.md`.
Full bodies: `curated/ai-agents/opencode-power/references/skills/`.
Bundled references, scripts, templates, workflows, and configs:
`curated/ai-agents/opencode-power/references/assets/`.

Restore one skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\opencode-power\catalog\ai-agents\<folder>" `
          -Destination "C:\github\skills\catalog\ai-agents\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\opencode-power\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
