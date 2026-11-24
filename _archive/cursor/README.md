# Archive: cursor

113 `cursor-*` skill folders moved here after compaction into
`curated/ai-agents/cursor/`. They span 17 subjects and remain 113 independent
canonical skills in 11 groups, since each source had its own body rather than a
variant of one workflow.

Original relative path preserved: `catalog/<subject>/<folder>`.

Subject counts in this archive.

| Subject | Skills |
| --- | --- |
| code-quality | 31 |
| ai-agents | 24 |
| writing-docs | 16 |
| testing-qa | 8 |
| design-ux | 6 |
| backend-api | 5 |
| office-productivity | 4 |
| strategy-executive | 4 |
| cyber-security | 3 |
| frontend-ui | 3 |
| business-finance | 2 |
| media-creative | 2 |
| data-ml | 1 |
| devops-cloud | 1 |
| integrations-automation | 1 |
| marketing-growth | 1 |
| research-academic | 1 |

Mapping to canonical skill and group: `curated/ai-agents/cursor/SOURCES.md`.
Full bodies: `curated/ai-agents/cursor/references/skills/`.
Long-form group prose: `curated/ai-agents/cursor/references/GUIDE.md`.
Non-SKILL.md files: `curated/ai-agents/cursor/references/assets/<skill>/` at the
same relative path as the source. 565 files totaling 3,867,520 bytes.

The pack shares an author and a lineage with `curated/ai-agents/pstack/`, and many
style, review, and principle skills appear in both. Bodies are kept per pack so each
one stands alone.

Restore one top-level skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\cursor\catalog\<subject>\<folder>" `
          -Destination "C:\github\skills\catalog\<subject>\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\cursor\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
