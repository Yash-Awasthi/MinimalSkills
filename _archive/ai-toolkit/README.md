# Archive: ai-toolkit

50 `sickn33-ai*` skills moved here after compaction into
`curated/ai-agents/ai-toolkit/`.

Original relative path preserved: `catalog/<subject>/<folder>`.

Mapping to skill and group: `curated/ai-agents/ai-toolkit/SOURCES.md`.
Full bodies: `curated/ai-agents/ai-toolkit/references/skills/`.
Bundled guides, references, evals, scripts, and playbooks:
`curated/ai-agents/ai-toolkit/references/assets/`.

Restore one skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\ai-toolkit\catalog\ai-agents\<folder>" `
          -Destination "C:\github\skills\catalog\ai-agents\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\ai-toolkit\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
