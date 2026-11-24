# Archive: composio-rube

845 source skills moved here after compaction into
`curated/integrations-automation/composio-rube/`.

Original relative path preserved: `catalog/<subject>/<folder>`.

Mapping to slug and mode: `curated/integrations-automation/composio-rube/SOURCES.md`.
Full bodies for 113 detailed skills: `curated/integrations-automation/composio-rube/references/workflows/`.

Restore one skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\composio-rube\catalog\integrations-automation\<folder>" `
          -Destination "C:\github\skills\catalog\integrations-automation\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\composio-rube\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
