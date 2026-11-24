# Archive: bug-hunting

141 `bug-hunter-*` and `sickn33-hunt-*` skills moved here after compaction into
`curated/cyber-security/bug-hunting/`.

Original relative path preserved: `catalog/<subject>/<folder>`.

Mapping to class, playbook, and reference: `curated/cyber-security/bug-hunting/SOURCES.md`.
Full bodies: `curated/cyber-security/bug-hunting/references/classes/` and `references/playbooks/`.

Restore one skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\bug-hunting\catalog\cyber-security\<folder>" `
          -Destination "C:\github\skills\catalog\cyber-security\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\bug-hunting\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
