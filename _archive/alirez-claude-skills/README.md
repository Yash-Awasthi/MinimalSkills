# Archive: alirez-claude-skills

460 `alirez-*` skills moved here after compaction into
`curated/general/alirez-claude-skills/`.

Original relative path preserved: `catalog/<subject>/<folder>`.

Mapping to skill and group: `curated/general/alirez-claude-skills/SOURCES.md`.
Full bodies: `curated/general/alirez-claude-skills/references/skills/`.
References, scripts, assets, templates, fixtures, and plugin metadata:
`curated/general/alirez-claude-skills/references/assets/`.

One nested sample, `testing-qa/alirez-skill-tester/assets/sample-skill/`, was a
bundled test fixture that `catalog.py` used to count as a separate skill. It moved
with its parent and remains available at
`_archive/alirez-claude-skills/catalog/testing-qa/alirez-skill-tester/assets/sample-skill/`
and in the curated assets. That explains the catalog drop of 461 for 460 sources.

67 of the archived entries are one-line alias pointers to `commands/` and
`agents/` paths that were never in the catalog. Their targets are not here.

Restore one skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\alirez-claude-skills\catalog\<subject>\<folder>" `
          -Destination "C:\github\skills\catalog\<subject>\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\alirez-claude-skills\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
