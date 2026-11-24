# Archive: api

20 `sickn33-api-*` skill folders moved here after compaction into
`curated/backend-api/api/`. They span 8 subjects and remain 20 independent canonical
skills in 5 groups, since each source had its own body rather than a variant of one
workflow.

Original relative path preserved: `catalog/<subject>/<folder>`.

Subject counts in this archive.

| Subject | Skills |
| --- | --- |
| backend-api | 8 |
| testing-qa | 3 |
| writing-docs | 3 |
| cyber-security | 2 |
| code-quality | 1 |
| frontend-ui | 1 |
| game-dev | 1 |
| strategy-executive | 1 |

Mapping to canonical skill and group: `curated/backend-api/api/SOURCES.md`.
Full bodies: `curated/backend-api/api/references/skills/`.
Long-form group prose: `curated/backend-api/api/references/GUIDE.md`.
Non-SKILL.md files: `curated/backend-api/api/references/assets/<skill>/` at the same
relative path as the source. 21 files totaling 115,832 bytes.

The canonical name drops the `sickn33-api-` prefix, so `sickn33-api-patterns` becomes
`patterns` and `sickn33-api-and-interface-design` becomes `and-interface-design`.
`api-patterns` owns the largest asset set, ten decision files plus `api_validator.py`.
`api-design-principles` carries the checklist, REST template, GraphQL reference, and
playbook.

`api-designer` names two support paths that are not in the source tree,
`references/domains.md` and `references/testmu_example.md`. They were already missing
before the move, and the body points at the LambdaTest upstream. Three security skills
carry an authorized-use and confirmation gate. Keep both statements.

Restore one top-level skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\api\catalog\<subject>\<folder>" `
          -Destination "C:\github\skills\catalog\<subject>\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\api\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
