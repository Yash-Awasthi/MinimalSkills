# Archive: seo-toolkit

41 `sickn33-seo*` skills moved here after compaction into
`curated/marketing-growth/seo-toolkit/`.

Original relative path preserved: `catalog/<subject>/<folder>`.

Mapping to skill and group: `curated/marketing-growth/seo-toolkit/SOURCES.md`.
Full bodies: `curated/marketing-growth/seo-toolkit/references/skills/`.
Bundled references, schema templates, playbooks, script, and plan templates:
`curated/marketing-growth/seo-toolkit/references/assets/`.

Restore one skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\seo-toolkit\catalog\marketing-growth\<folder>" `
          -Destination "C:\github\skills\catalog\marketing-growth\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\seo-toolkit\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
