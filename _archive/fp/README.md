# Archive: fp

15 `sickn33-fp-*` skill folders moved here after compaction into
`curated/code-quality/fp/`. They span 6 subjects and remain 15 independent canonical
skills in 6 groups, since each source had its own body rather than a variant of one
workflow.

Original relative path preserved: `catalog/<subject>/<folder>`.

Subject counts in this archive.

| Subject | Skills |
| --- | --- |
| code-quality | 5 |
| data-ml | 3 |
| backend-api | 2 |
| business-finance | 2 |
| frontend-ui | 2 |
| strategy-executive | 1 |

Mapping to canonical skill and group: `curated/code-quality/fp/SOURCES.md`.
Full bodies: `curated/code-quality/fp/references/skills/`.
Long-form group prose: `curated/code-quality/fp/references/GUIDE.md`.
Non-SKILL.md files: `curated/code-quality/fp/references/assets/<skill>/` at the same
relative path as the source. 10 files totaling 254,329 bytes, all detailed guides.

The canonical name drops the `sickn33-fp-` prefix, so `sickn33-fp-async` becomes `async`
and `sickn33-fp-data-transforms` becomes `data-transforms`.

Three pairs are near-duplicates under two names. `pragmatic` and `ts-pragmatic`, `errors`
and `ts-errors`, and `react` and `ts-react`. Each source stays as its own canonical skill
rather than merging, because the two entries carry separate names and descriptions. The
five short reference cards, `either-ref`, `option-ref`, `pipe-ref`, `taskeither-ref`, and
`types-ref`, ship no extra files.

Every body warns that the code is an excerpt or an integration sketch, not a compiled
package. Keep that statement. Where a detailed guide is named, it is bundled under the
skill's asset folder, and the body says its safety and validation rules are mandatory.

Restore one top-level skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\fp\catalog\<subject>\<folder>" `
          -Destination "C:\github\skills\catalog\<subject>\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\fp\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
