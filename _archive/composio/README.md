# Archive: composio

94 `composio-*` skill folders moved here after compaction into
`curated/integrations-automation/composio/`. They span 12 subjects and remain 94
independent canonical skills in 5 groups, since each source had its own body rather
than a variant of one workflow.

This is the remainder after the earlier 845-folder `composio-rube` archive. That pack
stays at `curated/integrations-automation/composio-rube/`. Both can be installed.

Original relative path preserved: `catalog/<subject>/<folder>`.

Subject counts in this archive.

| Subject | Skills |
| --- | --- |
| integrations-automation | 69 |
| office-productivity | 5 |
| writing-docs | 4 |
| frontend-ui | 3 |
| ai-agents | 2 |
| design-ux | 2 |
| devops-cloud | 2 |
| marketing-growth | 2 |
| media-creative | 2 |
| business-finance | 1 |
| hr-people | 1 |
| testing-qa | 1 |

Mapping to canonical skill and group: `curated/integrations-automation/composio/SOURCES.md`.
Full bodies: `curated/integrations-automation/composio/references/skills/`.
Long-form group prose: `curated/integrations-automation/composio/references/GUIDE.md`.
Non-SKILL.md files: `curated/integrations-automation/composio/references/assets/<skill>/`
at the same relative path as the source. 271 files totaling 8,651,193 bytes.

62 of the 94 are per-app automation workflows on `https://rube.app/mcp`. The other 32
are standalone document, research, media, and developer tools. `canvas-design` carries
80 bundled font files and dominates the asset bytes. `wave-accounting-automation` is
only a placeholder because Composio exposes no native Wave tools.

Restore one top-level skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\composio\catalog\<subject>\<folder>" `
          -Destination "C:\github\skills\catalog\<subject>\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\composio\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
