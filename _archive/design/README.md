# Archive: design

12 `sickn33-design-*` skill folders moved here after compaction into
`curated/design-ux/design/`. They span 3 subjects and remain 12 independent canonical
skills in 6 groups, since each source had its own body rather than a variant of one
workflow.

Original relative path preserved: `catalog/<subject>/<folder>`.

Subject counts in this archive.

| Subject | Skills |
| --- | --- |
| design-ux | 8 |
| frontend-ui | 3 |
| ai-agents | 1 |

Mapping to canonical skill and group: `curated/design-ux/design/SOURCES.md`.
Full bodies: `curated/design-ux/design/references/skills/`.
Long-form group prose: `curated/design-ux/design/references/GUIDE.md`.
Non-SKILL.md files: `curated/design-ux/design/references/assets/<skill>/` at the same
relative path as the source. 52 files totaling 551,061 bytes.

The canonical name drops the `sickn33-design-` prefix, so
`sickn33-design-taste-frontend` becomes `taste-frontend` and
`sickn33-design-token-contrast` becomes `token-contrast`.

`sickn33-design-it` is the only source with nested skill folders. Its 48 style bodies are
preserved at the same relative paths under `references/assets/it/<style>/SKILL.md`, so the
router's instruction to read `<style-folder>/SKILL.md` relative to its own directory still
resolves. The archive removes 12 top-level folders and 60 skill directories in total,
because `catalog.py` also counts the nested style bodies.

The pack keeps the overflow gate as mandatory, separates gates from signals, keeps the
font-loading rules, and rejects self-graded design. `theme-guide` says its shared execution
runtime is not bundled. `system` names external design siblings and audit helpers as not
bundled in its source tree, while the `spatial` asset supplies `layout-audit.js` in this
pack. `token-contrast` ships its checker as source rather than a committed script and
requires Node 18+. The Stitch MCP server and prompting guide are prerequisites for `md`.
Keep those gaps and never fabricate a missing target.

Restore one top-level skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\design\catalog\<subject>\<folder>" `
          -Destination "C:\github\skills\catalog\<subject>\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\design\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
