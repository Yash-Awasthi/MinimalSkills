# Archive: claude

12 `sickn33-claude-*` skill folders moved here after compaction into
`curated/ai-agents/claude/`. They span 7 subjects and remain 12 independent canonical
skills in 6 groups, since each source had its own body rather than a variant of one
workflow.

Original relative path preserved: `catalog/<subject>/<folder>`.

Subject counts in this archive.

| Subject | Skills |
| --- | --- |
| ai-agents | 4 |
| backend-api | 2 |
| code-quality | 1 |
| design-ux | 1 |
| frontend-ui | 1 |
| healthcare-medical | 1 |
| research-academic | 1 |
| strategy-executive | 1 |

Mapping to canonical skill and group: `curated/ai-agents/claude/SOURCES.md`.
Full bodies: `curated/ai-agents/claude/references/skills/`.
Long-form group prose: `curated/ai-agents/claude/references/GUIDE.md`.
Non-SKILL.md files: `curated/ai-agents/claude/references/assets/<skill>/` at the same
relative path as the source. 42 files totaling 353,754 bytes.

The canonical name drops the `sickn33-claude-` prefix, so
`sickn33-claude-api` becomes `api` and
`sickn33-claude-win11-speckit-update-skill` becomes `win11-speckit-update-skill`.

The pack keeps the API trigger scope, user-owned model choice, authorization checks,
pinned SDKs, bounded requests, the settings-audit read-only warning, explicit delegation
and orchestrator landing, the monitor permission rule, the macOS-only Chrome repair
with restart ordering, the SpecKit no-force rule, and the medical, scientific, and
reading boundaries. `delegate` is documentation only and `scripts/relay.mjs` is absent.
The Chrome paths are historical observations. `scientific-skills` is a discovery guide,
not a bundled library. `speed-reader` requires an installed upstream reader.

Restore one top-level skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\claude\catalog\<subject>\<folder>" `
          -Destination "C:\github\skills\catalog\<subject>\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\claude\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
