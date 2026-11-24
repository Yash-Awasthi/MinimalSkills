# Archive: context

13 `sickn33-context-*` skill folders moved here after compaction into
`curated/ai-agents/context/`. They span 7 subjects and remain 13 independent canonical
skills in 6 groups, since each source had its own body rather than a variant of one
workflow.

Original relative path preserved: `catalog/<subject>/<folder>`.

Subject counts in this archive.

| Subject | Skills |
| --- | --- |
| ai-agents | 6 |
| backend-api | 2 |
| business-finance | 1 |
| code-quality | 1 |
| design-ux | 1 |
| frontend-ui | 1 |
| writing-docs | 1 |

Mapping to canonical skill and group: `curated/ai-agents/context/SOURCES.md`.
Full bodies: `curated/ai-agents/context/references/skills/`.
Long-form group prose: `curated/ai-agents/context/references/GUIDE.md`.
Non-SKILL.md files: `curated/ai-agents/context/references/assets/<skill>/` at the same
relative path as the source. 16 files totaling 84,016 bytes.

The canonical name drops the `sickn33-context-` prefix, so `sickn33-context-agent` becomes
`agent` and `sickn33-context-management-context-restore` becomes
`management-context-restore`.

`agent` carries 13 assets: the compression rules and context format references plus 12
Python scripts and `requirements.txt`. `guardian` carries three: the extraction protocol,
the verification checklist, and `context_snapshot.py`. The other 11 sources ship no
non-SKILL.md files.

`agent` and `guardian` are written in Brazilian Portuguese, with the `When to Use` and
`Limitations` headings kept in English for catalog compatibility. `agent` writes a SQLite
database and `MEMORY.md`, and `guardian` creates and prunes snapshots. Keep their
confirmation and retention warnings.

`kit` names `<support-root>/scripts/install.sh`, which was absent before the move. The body
says it is an external prerequisite from the declared upstream. Keep that statement and do
not fabricate the script.

Restore one top-level skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\context\catalog\<subject>\<folder>" `
          -Destination "C:\github\skills\catalog\<subject>\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\context\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
