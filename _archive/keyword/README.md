# Archive: keyword

12 `sickn33-keyword-*` skill folders moved here after compaction into
`curated/marketing-growth/keyword/`. They span 3 subjects and remain 12 independent
canonical skills in 4 groups, since each source is a distinct tool rather than a variant
of one workflow.

Original relative path preserved: `catalog/<subject>/<folder>`.

Subject counts in this archive.

| Subject | Skills |
| --- | --- |
| marketing-growth | 10 |
| frontend-ui | 1 |
| strategy-executive | 1 |

Mapping to canonical skill and group: `curated/marketing-growth/keyword/SOURCES.md`.
Full bodies: `curated/marketing-growth/keyword/references/skills/`.
Long-form group prose: `curated/marketing-growth/keyword/references/GUIDE.md`.
Non-SKILL.md files: none. `references/assets/` is empty.

The canonical name drops the `sickn33-keyword-` prefix, so
`sickn33-keyword-clustering-tool` becomes `clustering-tool` and
`sickn33-keyword-roi-calculator` becomes `roi-calculator`.

The pack keeps the minimum-input rule, the untrusted-pasted-content rule, the density,
ROI, and share formulas, the no-comparability rule for provider scores, the strict
extractor output contract, the batch row-identity rule, and the authorization rule.
`share-estimator` lives under `frontend-ui` and `extractor` under `strategy-executive`
in the original catalog; both are preserved here.

Restore one top-level skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\keyword\catalog\<subject>\<folder>" `
          -Destination "C:\github\skills\catalog\<subject>\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\keyword\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
