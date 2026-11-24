# Archive: skill

20 `sickn33-skill-*` skill folders moved here after compaction into
`curated/ai-agents/skill/`. They span 7 subjects and remain 20 independent canonical
skills in 6 groups, since each source had its own body rather than a variant of one
workflow.

Original relative path preserved: `catalog/<subject>/<folder>`.

Subject counts in this archive.

| Subject | Skills |
| --- | --- |
| ai-agents | 14 |
| backend-api | 1 |
| code-quality | 1 |
| devops-cloud | 1 |
| hr-people | 1 |
| marketing-growth | 1 |
| writing-docs | 1 |

Mapping to canonical skill and group: `curated/ai-agents/skill/SOURCES.md`.
Full bodies: `curated/ai-agents/skill/references/skills/`.
Long-form group prose: `curated/ai-agents/skill/references/GUIDE.md`.
Non-SKILL.md files: `curated/ai-agents/skill/references/assets/<skill>/` at the same
relative path as the source. 66 files totaling 448,369 bytes.

The canonical name drops the `sickn33-skill-` prefix, so `sickn33-skill-skill` becomes
`skill` and `sickn33-skill-security-audit` becomes `security-audit`. The largest asset
trees are `skill-sentinel` with its analyzer package and `skill-writer` with its twelve
reference paths. `skill-creator` carries the init, validate, and package scripts.

Two members are not about authoring. `skill-gap-analysis` is an HR capability register
and `skill-rails-upgrade` is a Rails upgrade assessment. They keep their own group.

Restore one top-level skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\skill\catalog\<subject>\<folder>" `
          -Destination "C:\github\skills\catalog\<subject>\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\skill\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
