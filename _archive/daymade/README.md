# Archive: daymade

121 `daymade-*` skill folders moved here after compaction into
`curated/general/daymade/`. They span 18 subjects and remain 121 independent
canonical skills in 15 groups, since each source had its own body rather than a
variant of one workflow.

Original relative path preserved: `catalog/<subject>/<folder>`.

Subject counts in this archive.

| Subject | Skills |
| --- | --- |
| ai-agents | 33 |
| writing-docs | 17 |
| media-creative | 10 |
| code-quality | 8 |
| office-productivity | 8 |
| frontend-ui | 7 |
| strategy-executive | 7 |
| backend-api | 5 |
| business-finance | 5 |
| design-ux | 5 |
| devops-cloud | 3 |
| cyber-security | 2 |
| general | 2 |
| integrations-automation | 2 |
| marketing-growth | 2 |
| research-academic | 2 |
| testing-qa | 2 |
| mobile | 1 |

Mapping to canonical skill and group: `curated/general/daymade/SOURCES.md`.
Full bodies: `curated/general/daymade/references/skills/`.
Long-form group prose: `curated/general/daymade/references/GUIDE.md`.
Non-SKILL.md files: `curated/general/daymade/references/assets/<skill>/` at the
same relative path as the source. 1,566 files totaling 20,683,924 bytes.

`ppt-creator` and `slides-creator` are retirement notices, kept because installed
plugins still reference their names. Neither generates a deck.

Restore one top-level skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\daymade\catalog\<subject>\<folder>" `
          -Destination "C:\github\skills\catalog\<subject>\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\daymade\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
