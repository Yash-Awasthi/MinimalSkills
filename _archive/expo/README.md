# Archive: expo

13 `sickn33-expo-*` skill folders moved here after compaction into `curated/mobile/expo/`.
They span 3 subjects and remain 13 independent canonical skills in 6 groups, since each
source had its own body rather than a variant of one workflow.

Original relative path preserved: `catalog/<subject>/<folder>`.

Subject counts in this archive.

| Subject | Skills |
| --- | --- |
| mobile | 10 |
| frontend-ui | 2 |
| devops-cloud | 1 |

Mapping to canonical skill and group: `curated/mobile/expo/SOURCES.md`.
Full bodies: `curated/mobile/expo/references/skills/`.
Long-form group prose: `curated/mobile/expo/references/GUIDE.md`.
Non-SKILL.md files: `curated/mobile/expo/references/assets/<skill>/` at the same relative
path as the source. 38 files totaling 197,657 bytes.

The canonical name drops the `sickn33-expo-` prefix, so `sickn33-expo-api-routes` becomes
`api-routes` and `sickn33-expo-ui-jetpack-compose` becomes `ui-jetpack-compose`.

The three UI skills overlap by design. `ui` is the universal layer, while
`ui-jetpack-compose` and `ui-swift-ui` are the SDK 55 platform paths with their own native
rebuild rules. All three stay, because each carries a different version and component
contract. `ui-jetpack-compose` and `ui-swift-ui` ship no non-SKILL.md files.

The API route body says that fragments are incomplete demos and that a header or a
nonempty password does not authenticate. The brownfield body bans `prebuild --clean` on a
hand-maintained host. The observe body requires payload inspection and redaction. Keep all
three boundaries.

Restore one top-level skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\expo\catalog\<subject>\<folder>" `
          -Destination "C:\github\skills\catalog\<subject>\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\expo\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
