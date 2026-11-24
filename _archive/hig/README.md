# Archive: hig

14 `sickn33-hig-*` skill folders moved here after compaction into
`curated/design-ux/hig/`. They span 2 subjects and remain 14 independent canonical skills
in 9 groups, since each source had its own body rather than a variant of one workflow.

Original relative path preserved: `catalog/<subject>/<folder>`.

Subject counts in this archive.

| Subject | Skills |
| --- | --- |
| design-ux | 13 |
| frontend-ui | 1 |

Mapping to canonical skill and group: `curated/design-ux/hig/SOURCES.md`.
Full bodies: `curated/design-ux/hig/references/skills/`.
Long-form group prose: `curated/design-ux/hig/references/GUIDE.md`.
Non-SKILL.md files: `curated/design-ux/hig/references/assets/<skill>/` at the same
relative path as the source. 156 files totaling 2,385,323 bytes, all HIG reference pages.

The canonical name drops the `sickn33-hig-` prefix, so `sickn33-hig-components-layout`
becomes `components-layout` and `sickn33-hig-foundations` becomes `foundations`.

`project-context` is the only skill with no extra files. The rest carry between 3 and 28
HIG reference pages each, from `components-search` and `components-status` at 3 to
`technologies` at 28 and `patterns` at 25.

Every body checks for `.claude/apple-design-context.md` and treats it as project data
rather than authority. The bodies call their reference pages snapshots and warn that OS
availability, hardware, and input methods vary by release. `components-status` and
`technologies` add the HealthKit authorization rule, and `components-system` and
`patterns` add the delivery and system-budget limits. Keep those statements.

Restore one top-level skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\hig\catalog\<subject>\<folder>" `
          -Destination "C:\github\skills\catalog\<subject>\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\hig\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
