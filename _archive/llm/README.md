# Archive: llm

16 `sickn33-llm-*` skill folders moved here after compaction into
`curated/ai-agents/llm/`. They span 3 subjects and remain 16 independent canonical skills
in 6 groups, since each source had its own body rather than a variant of one workflow.

Original relative path preserved: `catalog/<subject>/<folder>`.

Subject counts in this archive.

| Subject | Skills |
| --- | --- |
| ai-agents | 14 |
| cyber-security | 1 |
| data-ml | 1 |

Mapping to canonical skill and group: `curated/ai-agents/llm/SOURCES.md`.
Full bodies: `curated/ai-agents/llm/references/skills/`.
Long-form group prose: `curated/ai-agents/llm/references/GUIDE.md`.
Non-SKILL.md files: `curated/ai-agents/llm/references/assets/<skill>/` at the same
relative path as the source. 11 files totaling 149,578 bytes.

The canonical name drops the `sickn33-llm-` prefix, so `sickn33-llm-app-patterns`
becomes `app-patterns` and `sickn33-llm-structured-output` becomes `structured-output`.

Bundled assets are the `app-patterns` detailed guide, the `app-security` details
reference, the two `application-dev` playbooks, the council detailed guide and
`.env.example`, the evaluation benchmarking reference, and the four `security`
references covering agent obedience engineering, agent security testing, the OWASP LLM
Top 10 map, and prompt injection methodology.

Four skills are `application-dev` scaffolding, and `ops` is a Portuguese-language
overview. Their bodies say the code is conceptual rather than a runnable project. Keep
that statement. `evaluation` carries a deliberate
`NotImplementedError("A verified fact-checking adapter is required")` and a
two-observation guard, both of which stay. `fine-tuning` states that publishing weights
is a separate authorized action after a license and privacy review. `security` is
authorized-use only with a mandatory confirmation gate, and `app-security` is the
defensive counterpart.

Restore one top-level skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\llm\catalog\<subject>\<folder>" `
          -Destination "C:\github\skills\catalog\<subject>\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\llm\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
