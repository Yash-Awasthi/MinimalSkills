# Archive: ui

18 `sickn33-ui-*` skill folders moved here after compaction into
`curated/frontend-ui/ui/`. They span 5 subjects and remain 18 independent canonical
skills in 7 groups, since each source had its own body rather than a variant of one
workflow.

Original relative path preserved: `catalog/<subject>/<folder>`.

Subject counts in this archive.

| Subject | Skills |
| --- | --- |
| frontend-ui | 12 |
| design-ux | 3 |
| ai-agents | 1 |
| code-quality | 1 |
| writing-docs | 1 |

Mapping to canonical skill and group: `curated/frontend-ui/ui/SOURCES.md`.
Full bodies: `curated/frontend-ui/ui/references/skills/`.
Long-form group prose: `curated/frontend-ui/ui/references/GUIDE.md`.
Non-SKILL.md files: `curated/frontend-ui/ui/references/assets/<skill>/` at the same
relative path as the source. 26 files totaling 415,410 bytes, all from `ux-pro-max`.

The canonical name drops the `sickn33-ui-` prefix, so `sickn33-ui-a11y` becomes `a11y`
and `sickn33-ui-ux-pro-max` becomes `ux-pro-max`.

`ux-pro-max` carries 12 design data CSVs, 11 stack guides, and the `core.py`,
`design_system.py`, and `search.py` scripts. The remaining 17 sources ship no
non-SKILL.md files.

Ten skills belong to the StyleSeed design-system family. Their bodies name
`DESIGN-LANGUAGE.md`, `VISUAL-CRAFT.md`, and `engine/motion`, which were absent before
the move and are not bundled. Keep the statements that report the prerequisite. The
`from-screenshot` and `states` skills come from UXKIN, and the two UI Skills entries are
an external collection and its router.

Restore one top-level skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\ui\catalog\<subject>\<folder>" `
          -Destination "C:\github\skills\catalog\<subject>\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\ui\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
