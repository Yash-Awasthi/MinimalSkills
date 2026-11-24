# Archive: hugging

13 `sickn33-hugging-*` skill folders moved here after compaction into
`curated/data-ml/hugging/`. They span 6 subjects and remain 13 independent canonical
skills in 6 groups, since each source had its own body rather than a variant of one
workflow.

Original relative path preserved: `catalog/<subject>/<folder>`.

Subject counts in this archive.

| Subject | Skills |
| --- | --- |
| data-ml | 6 |
| marketing-growth | 2 |
| research-academic | 2 |
| business-finance | 1 |
| devops-cloud | 1 |
| frontend-ui | 1 |

Mapping to canonical skill and group: `curated/data-ml/hugging/SOURCES.md`.
Full bodies: `curated/data-ml/hugging/references/skills/`.
Long-form group prose: `curated/data-ml/hugging/references/GUIDE.md`.
Non-SKILL.md files: `curated/data-ml/hugging/references/assets/<skill>/` at the same
relative path as the source. 66 files totaling 496,691 bytes.

The canonical name drops the `sickn33-hugging-face-` prefix, so
`sickn33-hugging-face-jobs` becomes `jobs` and `sickn33-hugging-face-vision-trainer`
becomes `vision-trainer`. `sickn33-hugging-face-cli` becomes `hf-cli`, since a bare `cli`
is not a usable skill name.

The largest asset sets are the 20 `model-trainer` files and the 16 `vision-trainer` files.
`model-trainer` carries training, hardware, hub, trackio, GGUF, Unsloth, and
troubleshooting references plus example scripts. `vision-trainer` carries notebooks,
safety scripts, a license, and an upstream notice. `jobs` contributes 10 and
`paper-publisher` contributes 8. The CLI, viewer, papers, and tool-builder skills ship no
extra files.

Three gaps were present before the move. `tool-builder` names four shell helpers under
`<support-root>/references/`, `datasets` names SQL and dataset manager files, and
`community-evals` says its bundled lighteval wrapper is disabled pending a release-specific
migration. The bodies report all three. Keep those statements and do not fabricate the
targets.

The bodies treat submission, scheduling, publication, and a paid retry as separate
authorized actions. They also require a scoped token, private storage, and a held-out
evaluation. Keep those boundaries.

Restore one top-level skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\hugging\catalog\<subject>\<folder>" `
          -Destination "C:\github\skills\catalog\<subject>\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\hugging\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
