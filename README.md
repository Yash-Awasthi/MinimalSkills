# Skills collection

Local mirror of public agent-skill repositories, segregated into subject folders with a master index.

## Layout

| Path | Purpose |
| --- | --- |
| `catalog/<subject>/` | Skill folders grouped by use case. Each contains real skill directories (frontmatter + instructions + assets), moved here from `packs/`. |
| `catalog/<subject>/INDEX.md` | Every skill in that subject with its own description and path. |
| `INDEX.md` | Master index: all 27 subjects with counts, plus the source mirror list. |
| `catalog/REPOS.md` | The 83 source mirrors with upstream URL, commit and skill count. |
| `catalog/_classification.tsv` | Audit trail: subject, skill, description, path for every indexed skill. |
| `curated/` | Compacted skills. One skill per redundant cluster, with merged workflows and provenance. |
| `_archive/` | Source skills replaced by a curated skill. Original paths kept for restore. |
| `repos/` | One shallow git clone per upstream repo, named `<owner>-<repo>`, kept as raw source material. |
| `catalog.py` | Per-file classifier: reads each `SKILL.md`, assigns a subject, moves folders, rebuilds indexes. |
| `repos.manifest.tsv` | Generated inventory of clones: URL, branch, commit, commit date, `SKILL.md` count, file count. |
| `update-repos.sh` | Refreshes all clones and regenerates the manifest. |

## Subjects

`cyber-security`, `compliance-audit`, `frontend-ui`, `backend-api`, `mobile`, `devops-cloud`,
`blockchain-web3`, `data-ml`, `integrations-automation`, `ai-agents`, `hardware-iot`, `testing-qa`,
`code-quality`, `design-ux`, `product-management`, `strategy-executive`, `marketing-growth`,
`writing-docs`, `business-finance`, `media-creative`, `game-dev`, `office-productivity`,
`research-academic`, `hr-people`, `general`.

Classification is per file: `catalog.py` reads the `SKILL.md` frontmatter `name` and `description`
(and follows pointer stubs into `repos/` when a pack only references another file), scores the text
against subject keyword rules, and assigns the highest-scoring subject. It writes
`catalog/_classification.tsv` so any assignment can be audited.

## Browsing

```bash
# master index
cat INDEX.md

# everything in one subject
cat catalog/cyber-security/INDEX.md

# search every skill description
grep -ril "kubernetes" catalog/*/INDEX.md
```

## Manual audit status

All 27 subject folders have been hand-audited row by row using each skill's name and description;
misfits were moved to their proper subject and every index was rebuilt afterwards. Remaining
placements are judgment calls, not automation output.

## Adding new skills

1. Drop skill folders into `packs/`, or clone a repo into `repos/` and copy its skill folders into `packs/`.
2. Run `python catalog.py` for a dry-run distribution.
3. Run `python catalog.py --apply` to move them into `catalog/<subject>/` and rebuild every index.

## Updating mirrors

```bash
./update-repos.sh
```

Fetches and fast-forwards each clone, prints `UPDATED`/`FAIL`/`SKIP` per repo, and rewrites
`repos.manifest.tsv`. Clean mirrors are hard-reset to the fetched tip (shallow clones have no shared
ancestry); any repo with local changes or untracked files is skipped untouched.

## Health check

```bash
# subjects and counts
awk -F'\\t' 'NR>1 && $6==0 {print $1}' repos.manifest.tsv   # repos with no SKILL.md
awk -F'\\t' 'NR>1 {n++; s+=$6} END {print n" repos, "s" SKILL.md"}' repos.manifest.tsv

# skills per subject
for d in catalog/*/; do printf "%5d %s\n" "$(find "$d" -name SKILL.md | wc -l)" "$(basename "$d")"; done | sort -rn
```
