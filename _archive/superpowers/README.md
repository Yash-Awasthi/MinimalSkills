# Archive: superpowers

15 `superpowers-*` skill folders moved here after compaction into
`curated/ai-agents/superpowers/`. They span 5 subjects and remain 15 independent
canonical skills in 7 groups, since each source had its own body rather than a variant
of one workflow.

Original relative path preserved: `catalog/<subject>/<folder>`.

Subject counts in this archive.

| Subject | Skills |
| --- | --- |
| code-quality | 5 |
| ai-agents | 4 |
| backend-api | 2 |
| testing-qa | 2 |
| writing-docs | 2 |

Mapping to canonical skill and group: `curated/ai-agents/superpowers/SOURCES.md`.
Full bodies: `curated/ai-agents/superpowers/references/skills/`.
Long-form group prose: `curated/ai-agents/superpowers/references/GUIDE.md`.
Non-SKILL.md files: `curated/ai-agents/superpowers/references/assets/<skill>/` at the
same relative path as the source. 65 files totaling 293,556 bytes.

The assets matter here. `brainstorming/scripts/` holds the visual companion server,
`subagent-driven-development/` holds the implementer, reviewer, and re-review prompts
plus the task and review scripts, `diagnosing-superpowers/` holds the analyst prompts,
report templates, and redaction policy, and `using-superpowers/references/` holds the
platform tool maps the entry skill names.

Restore one top-level skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\superpowers\catalog\<subject>\<folder>" `
          -Destination "C:\github\skills\catalog\<subject>\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\superpowers\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
