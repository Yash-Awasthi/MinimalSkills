# Archive: geo

16 `sickn33-geo-*` skill folders moved here after compaction into
`curated/marketing-growth/geo/`. They span 7 subjects and remain 16 independent
canonical skills in 7 groups, since each source had its own body rather than a variant
of one workflow.

Original relative path preserved: `catalog/<subject>/<folder>`.

Subject counts in this archive.

| Subject | Skills |
| --- | --- |
| marketing-growth | 6 |
| writing-docs | 4 |
| ai-agents | 2 |
| backend-api | 1 |
| business-finance | 1 |
| code-quality | 1 |
| design-ux | 1 |

Mapping to canonical skill and group: `curated/marketing-growth/geo/SOURCES.md`.
Full bodies: `curated/marketing-growth/geo/references/skills/`.
Long-form group prose: `curated/marketing-growth/geo/references/GUIDE.md`.
Non-SKILL.md files: `curated/marketing-growth/geo/references/assets/<skill>/` at the same
relative path as the source. 3 files totaling 57,420 bytes.

The canonical name drops the `sickn33-geo-` prefix, so `sickn33-geo-audit` becomes
`audit` and `sickn33-geo-keyword-expansion-tool` becomes `keyword-expansion-tool`.

The three assets are the `geo_checker.py` script behind `fundamentals`, plus the details
references behind `brand-mentions` and `technical`. The remaining 13 sources ship no
non-SKILL.md files.

Most bodies state their own evidence limits. GEO scores are heuristics, citations need a
dated sample, llms.txt is a proposal, and platform mechanisms need primary
documentation. Keep those limits. `report-pdf` needs pandoc and a local Chrome, and
`prospect` writes a local JSON register under `~/.geo-prospects/`.

Restore one top-level skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\geo\catalog\<subject>\<folder>" `
          -Destination "C:\github\skills\catalog\<subject>\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\geo\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
