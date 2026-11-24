# Archive: odoo

24 `sickn33-odoo-*` skill folders moved here after compaction into
`curated/business-finance/odoo/`. They span 10 subjects and remain 24 independent
canonical skills in 6 groups, since each source had its own body rather than a variant
of one workflow.

Original relative path preserved: `catalog/<subject>/<folder>`.

Subject counts in this archive.

| Subject | Skills |
| --- | --- |
| business-finance | 6 |
| backend-api | 5 |
| cyber-security | 3 |
| code-quality | 2 |
| devops-cloud | 2 |
| strategy-executive | 2 |
| compliance-audit | 1 |
| marketing-growth | 1 |
| testing-qa | 1 |
| writing-docs | 1 |

Mapping to canonical skill and group: `curated/business-finance/odoo/SOURCES.md`.
Full bodies: `curated/business-finance/odoo/references/skills/`.
Long-form group prose: `curated/business-finance/odoo/references/GUIDE.md`.

The canonical name drops the `sickn33-odoo-` prefix, so `sickn33-odoo-orm-expert`
becomes `orm-expert`. These sources carry no non-SKILL.md files, so
`references/assets/` is empty and no asset bytes were copied.

The bodies target the Odoo 14 to 19 range. Version, edition, and installed module
availability decide most menu paths and API details, so verify the deployed system
before applying an example.

Restore one top-level skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\odoo\catalog\<subject>\<folder>" `
          -Destination "C:\github\skills\catalog\<subject>\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\odoo\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
