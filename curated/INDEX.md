# Curated skills

Compacted replacements for the raw catalog. One skill per redundant cluster. Every source
workflow, rule, script, and asset preserved either inline or by reference. Sources are
archived, not deleted.

| Skill | Subject | Replaces | Deep refs | Status |
| --- | --- | --- | --- | --- |
| [composio-rube](integrations-automation/composio-rube/SKILL.md) | integrations-automation | 845 | 106 | done |
| [prodsec](cyber-security/prodsec/SKILL.md) | cyber-security | 145 | 145 | done |
| [bug-hunting](cyber-security/bug-hunting/SKILL.md) | cyber-security | 141 | 83 | done |
| [azure-sdk](devops-cloud/azure-sdk/SKILL.md) | devops-cloud | 127 | 127 | done |
| [red-team](cyber-security/red-team/SKILL.md) | cyber-security | 77 | 77 | done |
| [gstack](ai-agents/gstack/SKILL.md) | ai-agents | 77 | 71 | done |
| [rhdh](code-quality/rhdh/SKILL.md) | code-quality | 72 | 72 | done |
| [opencode-power](ai-agents/opencode-power/SKILL.md) | ai-agents | 57 | 57 | done |
| [ai-toolkit](ai-agents/ai-toolkit/SKILL.md) | ai-agents | 50 | 50 | done |
| [seo-toolkit](marketing-growth/seo-toolkit/SKILL.md) | marketing-growth | 41 | 41 | done |
| [alirez-claude-skills](general/alirez-claude-skills/SKILL.md) | general | 460 | 460 | done |
| [anthropic-skills](ai-agents/anthropic-skills/SKILL.md) | ai-agents | 279 | 279 | done |
| [pstack](ai-agents/pstack/SKILL.md) | ai-agents | 129 | 100 | done |
| [daymade](general/daymade/SKILL.md) | general | 121 | 121 | done |
| [cursor](ai-agents/cursor/SKILL.md) | ai-agents | 113 | 113 | done |
| [composio](integrations-automation/composio/SKILL.md) | integrations-automation | 94 | 94 | done |
| [mattpocock](general/mattpocock/SKILL.md) | general | 39 | 39 | done |
| [cyber-masriyan](cyber-security/cyber-masriyan/SKILL.md) | cyber-security | 22 | 22 | done |
| [caveman](ai-agents/caveman/SKILL.md) | ai-agents | 22 | 22 | done |
| [superpowers](ai-agents/superpowers/SKILL.md) | ai-agents | 15 | 15 | done |
| [aws](devops-cloud/aws/SKILL.md) | devops-cloud | 25 | 25 | done |
| [odoo](business-finance/odoo/SKILL.md) | business-finance | 24 | 24 | done |
| [agent](ai-agents/agent/SKILL.md) | ai-agents | 22 | 22 | done |
| [skill](ai-agents/skill/SKILL.md) | ai-agents | 20 | 20 | done |
| [api](backend-api/api/SKILL.md) | backend-api | 20 | 20 | done |
| [code](code-quality/code/SKILL.md) | code-quality | 20 | 20 | done |
| [apify](integrations-automation/apify/SKILL.md) | integrations-automation | 19 | 19 | done |
| [ui](frontend-ui/ui/SKILL.md) | frontend-ui | 18 | 18 | done |
| [makepad](frontend-ui/makepad/SKILL.md) | frontend-ui | 18 | 18 | done |
| [frontend](frontend-ui/frontend/SKILL.md) | frontend-ui | 17 | 17 | done |
| [geo](marketing-growth/geo/SKILL.md) | marketing-growth | 16 | 16 | done |
| [llm](ai-agents/llm/SKILL.md) | ai-agents | 16 | 16 | done |
| [fp](code-quality/fp/SKILL.md) | code-quality | 15 | 15 | done |
| [hig](design-ux/hig/SKILL.md) | design-ux | 14 | 14 | done |
| [n8n](integrations-automation/n8n/SKILL.md) | integrations-automation | 13 | 13 | done |
| [context](ai-agents/context/SKILL.md) | ai-agents | 13 | 13 | done |
| [hugging](data-ml/hugging/SKILL.md) | data-ml | 13 | 13 | done |
| [expo](mobile/expo/SKILL.md) | mobile | 13 | 13 | done |
| [security](cyber-security/security/SKILL.md) | cyber-security | 12 | 12 | done |
| [design](design-ux/design/SKILL.md) | design-ux | 12 | 12 | done |
| [claude](ai-agents/claude/SKILL.md) | ai-agents | 12 | 12 | done |
| [keyword](marketing-growth/keyword/SKILL.md) | marketing-growth | 12 | 12 | done |

Raw catalog after this pass: 2303 skills. Curated: 42 skills replacing 3290 source packs.
Archives: `../_archive/composio-rube/`, `../_archive/prodsec/`, `../_archive/bug-hunting/`,
`../_archive/azure-sdk/`, `../_archive/red-team/`, `../_archive/gstack/`,
`../_archive/rhdh/`, `../_archive/opencode-power/`, `../_archive/ai-toolkit/`,
`../_archive/seo-toolkit/`, `../_archive/alirez-claude-skills/`,
`../_archive/anthropic-skills/`, `../_archive/pstack/`, `../_archive/daymade/`,
`../_archive/cursor/`, `../_archive/composio/`, `../_archive/mattpocock/`,
`../_archive/cyber-masriyan/`, `../_archive/caveman/`,
`../_archive/superpowers/`, `../_archive/aws/`, `../_archive/odoo/`,
`../_archive/agent/`, `../_archive/skill/`, `../_archive/api/`,
`../_archive/code/`, `../_archive/apify/`, `../_archive/ui/`,
`../_archive/makepad/`, `../_archive/frontend/`, `../_archive/geo/`,
`../_archive/llm/`, `../_archive/fp/`, `../_archive/hig/`, `../_archive/n8n/`,
`../_archive/context/`, `../_archive/hugging/`, `../_archive/expo/`,
`../_archive/security/`, `../_archive/design/`, `../_archive/claude/`,
`../_archive/keyword/`.

## Rules for the next cluster

1. Pick the biggest coherent cluster, not the biggest subject.
2. Classify every source: identical template, or unique content.
3. Template sources collapse to one canonical workflow.
4. Unique bodies stay verbatim under `references/`.
5. Copy non-`SKILL.md` files under `references/assets/<source-path>/`.
6. Write `SOURCES.md`: every source path, mapped. No orphan.
7. Write `SKILL.md` in ultracave: fragments, one fact once, code/commands/paths verbatim,
   negations kept, no flavor.
8. Validate: source count = archived count; every body searchable in references;
   every name in the lookup table.
9. Move sources to `_archive/<cluster>/`, then run `python catalog.py --apply`.
10. Update this index and the root `INDEX.md`.
