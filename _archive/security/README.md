# Archive: security

12 `sickn33-security-*` skill folders moved here after compaction into
`curated/cyber-security/security/`. They span 2 subjects and remain 12 independent
canonical skills in 5 groups, since each source had its own body rather than a variant of
one workflow.

Original relative path preserved: `catalog/<subject>/<folder>`.

Subject counts in this archive.

| Subject | Skills |
| --- | --- |
| cyber-security | 11 |
| compliance-audit | 1 |

Mapping to canonical skill and group: `curated/cyber-security/security/SOURCES.md`.
Full bodies: `curated/cyber-security/security/references/skills/`.
Long-form group prose: `curated/cyber-security/security/references/GUIDE.md`.
Non-SKILL.md files: `curated/cyber-security/security/references/assets/<skill>/` at the
same relative path as the source. 6 files totaling 104,345 bytes.

The canonical name drops the `sickn33-security-` prefix, so
`sickn33-security-and-hardening` becomes `and-hardening` and
`sickn33-security-scanning-security-sast` becomes `scanning-security-sast`.

`arsenal` and `audit` are authorized-use only and carry the mandatory confirmation gate.
`auditor` and `scanning-security-hardening` forbid intrusive production testing without
written approval. `and-hardening` is the defensive counterpart and carries no such gate.
Keep the offensive and defensive roles separate.

`bluebook-builder` names `<support-root>/references/bluebook_template.md`, which was absent
before the move. The body says it is an external prerequisite. Keep that statement and do
not fabricate the template. The compliance and dependency playbooks are described as
conceptual scaffolding rather than certified control sets.

Restore one top-level skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\security\catalog\<subject>\<folder>" `
          -Destination "C:\github\skills\catalog\<subject>\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\security\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
