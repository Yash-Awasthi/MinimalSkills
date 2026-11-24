# Archive: cyber-masriyan

22 `cyber-masriyan-*` skill folders moved here after compaction into
`curated/cyber-security/cyber-masriyan/`. They span 2 subjects and remain 22
independent canonical skills in 5 groups, since each source had its own body rather
than a variant of one workflow.

Original relative path preserved: `catalog/<subject>/<folder>`.

Subject counts in this archive.

| Subject | Skills |
| --- | --- |
| cyber-security | 21 |
| compliance-audit | 1 |

Mapping to canonical skill and group: `curated/cyber-security/cyber-masriyan/SOURCES.md`.
Full bodies: `curated/cyber-security/cyber-masriyan/references/skills/`.
Long-form group prose: `curated/cyber-security/cyber-masriyan/references/GUIDE.md`.
Non-SKILL.md files: `curated/cyber-security/cyber-masriyan/references/assets/<skill>/`
at the same relative path as the source. 57 files totaling 471,443 bytes.

The numbered source folders map straight across. `cyber-masriyan-01-recon-osint`
becomes `01-recon-osint`, and so on through `22-purple-team`. Most assets are the
per-skill `scripts/` helpers and `examples/example_usage.md`.

`cyber-y2k` shares the prefix but is not in this pack. It is a visual design skill
nested inside `design-ux/sickn33-design-it/` and belongs to a different cluster.

Restore one top-level skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\cyber-masriyan\catalog\<subject>\<folder>" `
          -Destination "C:\github\skills\catalog\<subject>\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\cyber-masriyan\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
