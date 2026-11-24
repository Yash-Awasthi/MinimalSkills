# Skills

A curated library of **18 self-contained skills** for AI coding agents,
distilled from 2,105 source skills across 22 subject classes. Each skill is
**one standalone `SKILL.md`** — every policy, rule, procedure, script
contract and workflow is inlined in the file itself. No external references:
load one file and the whole domain playbook is present.

Focused on software development. Marketing, HR, healthcare, hardware/IoT and
general-education classes were dropped as out of scope.

## The skills

| # | Skill | Merges | Sources |
| --- | --- | --- | --- |
| 1 | [engineering-craft](top/engineering-craft/SKILL.md) | code-quality + testing-qa | 362 |
| 2 | [ai-agents-orchestration](top/ai-agents-orchestration/SKILL.md) | ai-agents | 227 |
| 3 | [backend-api](top/backend-api/SKILL.md) | backend-api | 218 |
| 4 | [devops-cloud](top/devops-cloud/SKILL.md) | devops-cloud | 185 |
| 5 | [security-operations](top/security-operations/SKILL.md) | cyber-security + compliance-audit | 180 |
| 6 | [frontend-ui](top/frontend-ui/SKILL.md) | frontend-ui | 166 |
| 7 | [writing-docs](top/writing-docs/SKILL.md) | writing-docs | 124 |
| 8 | [business-finance](top/business-finance/SKILL.md) | business-finance | 109 |
| 9 | [design-ux](top/design-ux/SKILL.md) | design-ux | 99 |
| 10 | [strategy-product](top/strategy-product/SKILL.md) | strategy-executive + product-management | 87 |
| 11 | [data-ml](top/data-ml/SKILL.md) | data-ml | 68 |
| 12 | [media-creative](top/media-creative/SKILL.md) | media-creative | 64 |
| 13 | [office-productivity](top/office-productivity/SKILL.md) | office-productivity | 55 |
| 14 | [mobile-apps](top/mobile-apps/SKILL.md) | mobile | 40 |
| 15 | [game-dev](top/game-dev/SKILL.md) | game-dev | 39 |
| 16 | [research-education](top/research-education/SKILL.md) | research-academic | 34 |
| 17 | [platform-general](top/platform-general/SKILL.md) | general + integrations-automation | 29 |
| 18 | [web3-blockchain](top/web3-blockchain/SKILL.md) | blockchain-web3 | 19 |

Full details and per-hub line counts: [top/INDEX.md](top/INDEX.md).

## Format

Each `SKILL.md` carries:

- **Frontmatter** — name, description, merge provenance and source count.
- **Iron laws** — the binding contracts distilled from the source packs
  (authorization gates, version discipline, fail-closed rules, style rules).
- **Numbered sections** — the full domain playbook, all procedures inline.
- **Output contract** — what a completed task must report.
- **Failure handling** — what to do when evidence is missing or contradicts
  the request.
- **Provenance** — merges, source counts, preservation notes.

## Guarantees

1. **Zero external references** — verified: no hub points at `catalog/`,
   `curated/`, `_archive/` or any `references/` directory.
2. **Duplicates collapsed, nothing dropped** — where many sources said the
   same thing, one canonical statement carries it.
3. **Fail-closed rules kept** — every "stop when evidence is missing" rule
   from the sources is preserved.
4. **History preserved** — the pre-cleanup snapshot (raw `catalog/`,
   `curated/` and `_archive/` trees, 38,495 files) lives in the git history
   (commit `020b5425`).

## Install

Copy the hub directories you need into your agent's skills directory, or
clone the repo and symlink `top/<skill>` entries.
