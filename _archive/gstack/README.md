# Archive: gstack

77 `gstack*` skill packs moved here after compaction into
`curated/ai-agents/gstack/`.

Original relative path preserved: `catalog/<subject>/<folder>`.

Six packs were nested inside `gstack-garrytan-gstack`. They moved with that repository
snapshot and keep their original paths:

- `catalog/ai-agents/gstack-garrytan-gstack/capy/skill/gstack`
- `catalog/ai-agents/gstack-garrytan-gstack/gstack-upgrade`
- `catalog/ai-agents/gstack-garrytan-gstack/openclaw/skills/gstack-openclaw-ceo-review`
- `catalog/ai-agents/gstack-garrytan-gstack/openclaw/skills/gstack-openclaw-office-hours`
- `catalog/ai-agents/gstack-garrytan-gstack/openclaw/skills/gstack-openclaw-retro`
- `catalog/ai-agents/gstack-garrytan-gstack/qm/sandbox/skills/gstack-plan`

The repository snapshot also contains 64 additional `SKILL.md` files that the pack
inventory never counted as separate catalog rows. They are preserved here and copied under
`curated/ai-agents/gstack/references/assets/`. Total `SKILL.md` files in this archive: 141.

Mapping to command, group, and reference: `curated/ai-agents/gstack/SOURCES.md`.
Full bodies: `curated/ai-agents/gstack/references/commands/`.

Restore one pack:

```powershell
Move-Item -Path "C:\github\skills\_archive\gstack\catalog\ai-agents\<folder>" `
          -Destination "C:\github\skills\catalog\ai-agents\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\gstack\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
