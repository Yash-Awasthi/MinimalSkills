# Archive: azure-sdk

127 `sickn33-azure-*` skills moved here after compaction into
`curated/devops-cloud/azure-sdk/`.

Original relative path preserved: `catalog/<subject>/<folder>`.

Mapping to SDK, family, and language: `curated/devops-cloud/azure-sdk/SOURCES.md`.
Full bodies: `curated/devops-cloud/azure-sdk/references/sdks/`.

Restore one skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\azure-sdk\catalog\devops-cloud\<folder>" `
          -Destination "C:\github\skills\catalog\devops-cloud\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\azure-sdk\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
