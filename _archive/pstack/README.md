# Archive: pstack

129 `pstack*` top-level skill folders moved here after compaction into
`curated/ai-agents/pstack/`. They span 11 subjects and collapse into 72 canonical
skills in 13 groups.

The 129 folders form 57 `claude-` and plain pairs, 11 `claude-`-only skills, and 4
plain-only skills. 29 pairs were byte-identical after frontmatter and map once. The other
28 plain bodies differ and are preserved as
`curated/ai-agents/pstack/references/skills/<skill>--plain.md`.

Original relative path preserved: `catalog/<subject>/<folder>`.

Mapping to canonical skill, group, and role: `curated/ai-agents/pstack/SOURCES.md`.
Full bodies: `curated/ai-agents/pstack/references/skills/`.
Long-form workflow prose: `curated/ai-agents/pstack/references/GUIDE.md`.
Platform mappings, playbooks, and scripts:
`curated/ai-agents/pstack/references/assets/`.

Restore one top-level skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\pstack\catalog\<subject>\<folder>" `
          -Destination "C:\github\skills\catalog\<subject>\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\pstack\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
