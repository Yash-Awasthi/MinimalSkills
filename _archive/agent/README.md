# Archive: agent

22 `sickn33-agent-*` skill folders moved here after compaction into
`curated/ai-agents/agent/`. They span 2 subjects and remain 22 independent canonical
skills in 6 groups, since each source had its own body rather than a variant of one
workflow.

Original relative path preserved: `catalog/<subject>/<folder>`.

Subject counts in this archive.

| Subject | Skills |
| --- | --- |
| ai-agents | 20 |
| devops-cloud | 2 |

Mapping to canonical skill and group: `curated/ai-agents/agent/SOURCES.md`.
Full bodies: `curated/ai-agents/agent/references/skills/`.
Long-form group prose: `curated/ai-agents/agent/references/GUIDE.md`.
Non-SKILL.md files: `curated/ai-agents/agent/references/assets/<skill>/` at the same
relative path as the source. 27 files totaling 271,332 bytes.

The canonical name drops the `sickn33-agent-` prefix. The prefix also matches
neighbours such as `sickn33-agentflow`, `sickn33-agentfolio`, `sickn33-agentic-*`,
`sickn33-agentmail`, `sickn33-agentphone`, `sickn33-agents-*`, and
`sickn33-agenttrace-session-audit`. Those are not part of this pack and stay in the
live catalog.

Two assets carry structure rather than a single file. `squad/` holds eight nested agent
files under `references/assets/squad/<name>/SKILL.md`, and `orchestrator/` holds the
Python registry and matching scripts behind the meta-skill. Keep each with its body.

Restore one top-level skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\agent\catalog\<subject>\<folder>" `
          -Destination "C:\github\skills\catalog\<subject>\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\agent\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
