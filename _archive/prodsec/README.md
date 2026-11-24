# Archive: prodsec

145 `redhat-prodsec-*` skills moved here after compaction into
`curated/cyber-security/prodsec/`.

Original relative path preserved: `catalog/<subject>/<folder>`.

Mapping to control name and category: `curated/cyber-security/prodsec/SOURCES.md`.
Full bodies: `curated/cyber-security/prodsec/references/controls/`.

Restore one skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\prodsec\catalog\cyber-security\<folder>" `
          -Destination "C:\github\skills\catalog\cyber-security\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\prodsec\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
