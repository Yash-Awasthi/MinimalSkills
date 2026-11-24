# Archive: makepad

18 `sickn33-makepad-*` skill folders moved here after compaction into
`curated/frontend-ui/makepad/`. They span 2 subjects and remain 18 independent canonical
skills in 6 groups, since each source had its own body rather than a variant of one
workflow.

Original relative path preserved: `catalog/<subject>/<folder>`.

Subject counts in this archive.

| Subject | Skills |
| --- | --- |
| frontend-ui | 17 |
| devops-cloud | 1 |

Mapping to canonical skill and group: `curated/frontend-ui/makepad/SOURCES.md`.
Full bodies: `curated/frontend-ui/makepad/references/skills/`.
Long-form group prose: `curated/frontend-ui/makepad/references/GUIDE.md`.
Non-SKILL.md files: `curated/frontend-ui/makepad/references/assets/<skill>/` at the same
relative path as the source. 10 files totaling 166,685 bytes.

The canonical name drops the `sickn33-makepad-` prefix, so `sickn33-makepad-layout`
becomes `layout` and `sickn33-makepad-2-0-layout` becomes `2-0-layout`.

The cluster holds two generations. Five `2-0-*` skills come from zhanghandong's
dev-branch notes dated 2026-03-03 and carry the only bundled references. Thirteen use
the older `live_design!` macro. Same-named pairs such as `animation` and
`2-0-animation`, or `layout` and `2-0-layout`, are separate bodies for separate
generations, so both stay and neither replaces the other.

The thirteen live_design skills name reference files that were absent before the move,
including `layout-system.md`, `widgets-core.md`, `event-system.md`, and
`splash-tutorial.md`. The bodies state the gap, and the pack keeps that statement.
`deployment` also names an icon and two resource folders that are not present.

Restore one top-level skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\makepad\catalog\<subject>\<folder>" `
          -Destination "C:\github\skills\catalog\<subject>\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\makepad\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
