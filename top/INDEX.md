# Top skills

The final merged set: 18 self-contained skills replacing 2,105 raw skills
across 22 subject classes. Each hub is **one standalone `SKILL.md`** — every
policy, rule, procedure, script contract and workflow is inlined in the file
itself. No hub references `catalog/`, `curated/`, `_archive/` or any other
external file; load one file and the whole domain playbook is present.

| # | Skill | Merges | Sources | Lines |
| --- | --- | --- | --- | --- |
| 1 | [engineering-craft](engineering-craft/SKILL.md) | code-quality + testing-qa | 362 | 845 |
| 2 | [ai-agents-orchestration](ai-agents-orchestration/SKILL.md) | ai-agents | 227 | 883 |
| 3 | [backend-api](backend-api/SKILL.md) | backend-api | 218 | 431 |
| 4 | [devops-cloud](devops-cloud/SKILL.md) | devops-cloud | 185 | 452 |
| 5 | [security-operations](security-operations/SKILL.md) | cyber-security + compliance-audit | 180 | 689 |
| 6 | [frontend-ui](frontend-ui/SKILL.md) | frontend-ui | 166 | 476 |
| 7 | [writing-docs](writing-docs/SKILL.md) | writing-docs | 124 | 214 |
| 8 | [business-finance](business-finance/SKILL.md) | business-finance | 109 | 311 |
| 9 | [design-ux](design-ux/SKILL.md) | design-ux | 99 | 294 |
| 10 | [strategy-product](strategy-product/SKILL.md) | strategy-executive + product-management | 87 | 176 |
| 11 | [data-ml](data-ml/SKILL.md) | data-ml | 68 | 222 |
| 12 | [media-creative](media-creative/SKILL.md) | media-creative | 64 | 169 |
| 13 | [office-productivity](office-productivity/SKILL.md) | office-productivity | 55 | 157 |
| 14 | [mobile-apps](mobile-apps/SKILL.md) | mobile | 40 | 189 |
| 15 | [research-education](research-education/SKILL.md) | research-academic | 34 | 154 |
| 16 | [game-dev](game-dev/SKILL.md) | game-dev | 39 | 141 |
| 17 | [platform-general](platform-general/SKILL.md) | general + integrations-automation | 29 | 307 |
| 18 | [web3-blockchain](web3-blockchain/SKILL.md) | blockchain-web3 | 19 | 166 |

Total: 18 skills covering 2,105 source skills. The marketing-growth,
hr-people, healthcare-medical, hardware-iot and education-learning classes
were deleted by the user (out of scope for a software-development-focused
library); their former hubs (marketing-growth, people-ops, healthcare) were
removed with them.

## Self-containment guarantees
1. **Zero external references** — verified: every hub's SKILL.md contains no
   `catalog/`, `curated/`, `_archive/` or `references/` path. Each file
   works alone.
2. **Policies inline** — authorization gates, budget and approval rules,
   consent boundaries, verification requirements, output contracts and
   failure-handling tables are restated inside each hub where they apply.
3. **Duplicates collapsed** — where many source skills said the same thing,
   one canonical statement carries it; nothing was dropped, only merged.
4. **Provenance per hub** — each file ends with a provenance section naming
   its merges, source counts and what was preserved.
5. **Fail-closed rules kept** — every "stop when evidence is missing" rule
   from the source packs is preserved verbatim in meaning.

## How to use
Load the hub matching the task domain. The hub's numbered sections carry the
full playbook; the output contract and failure table at the end govern
reporting. Cross-domain work is handled by the hub that owns the domain
(e.g. mobile app security testing lives in security-operations, referenced
from mobile-apps).

## Original sources
The raw material stays on disk until you delete it: `catalog/` (2,105
skills, 122 MB), `curated/` (42 deep packs with verbatim bodies, 249 MB) and
`_archive/` (281 MB). Recommended: back up or `git init` before removing
them.
