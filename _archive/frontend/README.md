# Archive: frontend

17 `sickn33-frontend-*` skill folders moved here after compaction into
`curated/frontend-ui/frontend/`. They span 3 subjects and remain 17 independent
canonical skills in 7 groups, since each source had its own body rather than a variant
of one workflow.

Original relative path preserved: `catalog/<subject>/<folder>`.

Subject counts in this archive.

| Subject | Skills |
| --- | --- |
| frontend-ui | 14 |
| cyber-security | 2 |
| game-dev | 1 |

Mapping to canonical skill and group: `curated/frontend-ui/frontend/SOURCES.md`.
Full bodies: `curated/frontend-ui/frontend/references/skills/`.
Long-form group prose: `curated/frontend-ui/frontend/references/GUIDE.md`.
Non-SKILL.md files: `curated/frontend-ui/frontend/references/assets/<skill>/` at the same
relative path as the source. 24 files totaling 242,298 bytes.

The canonical name drops the `sickn33-frontend-` prefix, so
`sickn33-frontend-architecture` becomes `architecture` and
`sickn33-frontend-ui-dark-ts` becomes `ui-dark-ts`.

`slides` and `slides-frontend-slides` deliver the same kind of artifact with different
layout rules. One fits each slide to the viewport and the other fixes a 1920 by 1080
stage. Both stay, because the chosen body carries its own rule.

Three gaps were present before the move. `frontend-ui-engineering` names an
accessibility checklist from the addyosmani upstream, `dev-guidelines` names project
components such as `SuspenseLoader` and `apiClient`, and `mobile-security-xss-scan`
describes a scanner whose `xss-scanner.js` is not included. Keep the fail-closed
statements in those bodies.

Restore one top-level skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\frontend\catalog\<subject>\<folder>" `
          -Destination "C:\github\skills\catalog\<subject>\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\frontend\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
