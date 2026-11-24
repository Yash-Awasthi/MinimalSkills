# Archive: n8n

13 `sickn33-n8n-*` skill folders moved here after compaction into
`curated/integrations-automation/n8n/`. They span 4 subjects and remain 13 independent
canonical skills in 5 groups, since each source had its own body rather than a variant of
one workflow.

Original relative path preserved: `catalog/<subject>/<folder>`.

Subject counts in this archive.

| Subject | Skills |
| --- | --- |
| integrations-automation | 10 |
| ai-agents | 1 |
| backend-api | 1 |
| office-productivity | 1 |

Mapping to canonical skill and group: `curated/integrations-automation/n8n/SOURCES.md`.
Full bodies: `curated/integrations-automation/n8n/references/skills/`.
Long-form group prose: `curated/integrations-automation/n8n/references/GUIDE.md`.
Non-SKILL.md files: `curated/integrations-automation/n8n/references/assets/<skill>/` at
the same relative path as the source. 28 files totaling 321,345 bytes.

The canonical name drops the `sickn33-n8n-` prefix, so `sickn33-n8n-agents` becomes
`agents` and `sickn33-n8n-code-javascript` becomes `code-javascript`.

The largest asset set belongs to `agents`, with nine references for chat patterns,
examples, human review, memory, RAG, structured output, sub-workflow as tool, system
prompt, and tools. `multi-instance` and `workflow-patterns` ship no non-SKILL.md files.

Every body states that its fragments are illustrative rather than certified live schemas,
and several add a version and safety boundary. Keep those statements. The
`expression-syntax` body also notes that its named `EXAMPLES.md` and `COMMON_MISTAKES.md`
were absent before the move, so the pack reports the gap rather than fabricating them.

Restore one top-level skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\n8n\catalog\<subject>\<folder>" `
          -Destination "C:\github\skills\catalog\<subject>\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\n8n\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
