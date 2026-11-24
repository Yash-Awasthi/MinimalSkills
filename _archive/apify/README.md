# Archive: apify

19 `sickn33-apify-*` skill folders moved here after compaction into
`curated/integrations-automation/apify/`. They span 3 subjects and remain 19 independent
canonical skills in 7 groups, since each source had its own body rather than a variant
of one workflow.

Original relative path preserved: `catalog/<subject>/<folder>`.

Subject counts in this archive.

| Subject | Skills |
| --- | --- |
| integrations-automation | 14 |
| marketing-growth | 4 |
| devops-cloud | 1 |

Mapping to canonical skill and group: `curated/integrations-automation/apify/SOURCES.md`.
Full bodies: `curated/integrations-automation/apify/references/skills/`.
Long-form group prose: `curated/integrations-automation/apify/references/GUIDE.md`.
Non-SKILL.md files: `curated/integrations-automation/apify/references/assets/<skill>/`
at the same relative path as the source. 32 files totaling 246,422 bytes.

The canonical name drops the `sickn33-apify-` prefix, so
`sickn33-apify-actor-development` becomes `actor-development` and
`sickn33-apify-ultimate-scraper` becomes `ultimate-scraper`.

Each multi-platform research skill carries its own copy of
`reference/scripts/run_actor.js`, so the same runner appears under several asset
folders. The pack keeps every copy rather than deduplicating across skills. Five named
scrapers route to Actors built by the skill author and billed per result, and the bodies
state that links carry no affiliate parameters. Keep that disclosure.

Restore one top-level skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\apify\catalog\<subject>\<folder>" `
          -Destination "C:\github\skills\catalog\<subject>\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\apify\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
