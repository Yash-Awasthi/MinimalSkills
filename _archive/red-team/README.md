# Archive: red-team

77 `claude-red-offensive-*` skills moved here after compaction into
`curated/cyber-security/red-team/`.

Original relative path preserved: `catalog/<subject>/<folder>`.

Mapping to tactic and group: `curated/cyber-security/red-team/SOURCES.md`.
Full bodies: `curated/cyber-security/red-team/references/tactics/`.

Restore one skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\red-team\catalog\cyber-security\<folder>" `
          -Destination "C:\github\skills\catalog\cyber-security\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\red-team\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
