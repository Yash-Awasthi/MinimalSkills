# Archive: code

20 `sickn33-code-*` skill folders moved here after compaction into
`curated/code-quality/code/`. They span 7 subjects and remain 20 independent canonical
skills in 7 groups, since each source had its own body rather than a variant of one
workflow.

Original relative path preserved: `catalog/<subject>/<folder>`.

Subject counts in this archive.

| Subject | Skills |
| --- | --- |
| code-quality | 13 |
| writing-docs | 2 |
| backend-api | 1 |
| cyber-security | 1 |
| frontend-ui | 1 |
| hr-people | 1 |
| testing-qa | 1 |

Mapping to canonical skill and group: `curated/code-quality/code/SOURCES.md`.
Full bodies: `curated/code-quality/code/references/skills/`.
Long-form group prose: `curated/code-quality/code/references/GUIDE.md`.
Non-SKILL.md files: `curated/code-quality/code/references/assets/<skill>/` at the same
relative path as the source. 6 files totaling 82,471 bytes.

The canonical name drops the `sickn33-code-` prefix. `sickn33-code-audit` becomes
`audit`, `sickn33-code-polish` becomes `polish`, and `sickn33-code-of-conduct` becomes
`conduct`, since `of-conduct` is not a usable skill name. Four assets are the
`resources/implementation-playbook.md` variants behind code explanation, doc generation,
clean refactoring, and review excellence. Two are the SAST review checklist and the
conduct common-pitfalls reference.

Two bodies name support files that were already absent before the move.
`code-review-ai-ai-review` names `<support-root>/scripts/ai_review.py`, and
`code-review-and-quality` names `security-checklist.md` and `performance-checklist.md`
from the addyosmani upstream. The bodies say so and point at the upstream. Keep those
statements and do not fabricate the files. `documentation-doc-generate` and
`refactoring-context-restore` are compatibility aliases, so keep their callable IDs.

Restore one top-level skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\code\catalog\<subject>\<folder>" `
          -Destination "C:\github\skills\catalog\<subject>\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\code\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
