# Archive: rhdh

72 `rhdh*` skills moved here after compaction into
`curated/code-quality/rhdh/`.

Original relative path preserved: `catalog/<subject>/<folder>`.

Mapping to skill and group: `curated/code-quality/rhdh/SOURCES.md`.
Full bodies: `curated/code-quality/rhdh/references/skills/`.
Bundled scripts, references, examples, schemas, and tests:
`curated/code-quality/rhdh/references/assets/`.

Restore one skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\rhdh\catalog\code-quality\<folder>" `
          -Destination "C:\github\skills\catalog\code-quality\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\rhdh\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
