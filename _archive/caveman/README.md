# Archive: caveman

22 `caveman-*` skill folders moved here after compaction into
`curated/ai-agents/caveman/`. They span 7 subjects and remain 22 independent canonical
skills in 6 groups, since each source had its own body rather than a variant of one
workflow.

Original relative path preserved: `catalog/<subject>/<folder>`.

Subject counts in this archive.

| Subject | Skills |
| --- | --- |
| code-quality | 7 |
| backend-api | 6 |
| ai-agents | 2 |
| devops-cloud | 3 |
| design-ux | 1 |
| frontend-ui | 1 |
| marketing-growth | 1 |
| testing-qa | 1 |

Mapping to canonical skill and group: `curated/ai-agents/caveman/SOURCES.md`.
Full bodies: `curated/ai-agents/caveman/references/skills/`.
Long-form group prose: `curated/ai-agents/caveman/references/GUIDE.md`.
Non-SKILL.md files: `curated/ai-agents/caveman/references/assets/<skill>/` at the same
relative path as the source. 26 files totaling 104,862 bytes.

Most assets are small: the `caveman-compress` Python package, the `caveman-explore`
reader tests, the two SVG marks, and the per-skill `README.md` and `agents/openai.yaml`.
Keep `scripts/compress.py` with its sibling modules, since the body calls the package
entry point.

Restore one top-level skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\caveman\catalog\<subject>\<folder>" `
          -Destination "C:\github\skills\catalog\<subject>\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\caveman\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
