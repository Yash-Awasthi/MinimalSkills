# Archive: mattpocock

39 `mattpocock-*` skill folders moved here after compaction into
`curated/general/mattpocock/`. They span 13 subjects and remain 39 independent
canonical skills in 7 groups, since each source had its own body rather than a variant
of one workflow.

Original relative path preserved: `catalog/<subject>/<folder>`.

Subject counts in this archive.

| Subject | Skills |
| --- | --- |
| code-quality | 8 |
| ai-agents | 6 |
| writing-docs | 6 |
| strategy-executive | 5 |
| backend-api | 3 |
| frontend-ui | 2 |
| product-management | 2 |
| testing-qa | 2 |
| data-ml | 1 |
| design-ux | 1 |
| education-learning | 1 |
| office-productivity | 1 |
| research-academic | 1 |

Mapping to canonical skill and group: `curated/general/mattpocock/SOURCES.md`.
Full bodies: `curated/general/mattpocock/references/skills/`.
Long-form group prose: `curated/general/mattpocock/references/GUIDE.md`.
Non-SKILL.md files: `curated/general/mattpocock/references/assets/<skill>/` at the same
relative path as the source. 70 files totaling 134,832 bytes.

Most assets are one `agents/openai.yaml` per skill. The rest are the format files the
bodies point at, such as `PHASE-BOUNDARIES.md`, `DEEPENING.md`, `DESIGN-IT-TWICE.md`,
`SKILL-MECHANICS.md`, `HTML-REPORT.md`, `template.sh`, and
`scripts/block-dangerous-git.sh`. Keep them with the body that references them.

Restore one top-level skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\mattpocock\catalog\<subject>\<folder>" `
          -Destination "C:\github\skills\catalog\<subject>\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\mattpocock\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
