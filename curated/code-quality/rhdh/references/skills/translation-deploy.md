<!-- source: catalog/code-quality/rhdh-rhdh-translation-deploy -->
<!-- source-name: rhdh-rhdh-translation-deploy -->

# RHDH Translation Deploy

Download translated files from TMS, merge into the right targets, and prepare
PRs.

## What goes where

| Source repo in TMS | Deploy target |
|--------------------|---------------|
| rhdh-plugins | In-place `.ts` merge in rhdh-plugins + changesets + PR |
| community-plugins | In-place `.ts` merge in community-plugins + changesets + PR; also JSON merge into `rhdh/translations/` |
| backstage | JSON merge into `rhdh/translations/backstage-{locale}.json` only — **no upstream backstage PR** |
| rhdh | JSON merge into `rhdh/translations/rhdh-{locale}.json` |

## Merge rules for `.ts` files

Do **not** use `translations-cli i18n deploy` — it rewrites files and removes
unchanged keys.

1. Load downloaded JSON for a plugin + locale.
2. Open the existing locale file (e.g. `de.ts`).
3. For each downloaded key: if it exists in the file → update the value; if
   not → skip.
4. Never remove keys. Never change imports/exports.
5. Strings containing an apostrophe use double quotes (`"..."`).
6. Run Prettier on changed files before commit.

No delta comparison and no `ref.ts` gate during merge. Keys developers add
after upload stay untouched.

## Subcommands

| Command | Description |
|---------|-------------|
| `preflight` | Check repos, tools, TMS credentials |
| `download` | Download completed jobs via translations-cli |
| `validate` | Basic JSON / structure checks on downloads |
| `update-translated-sot --sprint S` | Fix TMS `en` → real locale, merge into `rhdh/translations/`, PR on rhdh |
| `deploy` | In-place `.ts` merge for rhdh-plugins and community-plugins |
| `pr --sprint S` | Write changesets with real package names; report repos ready for `/mutation-gate` |

## Route

Load `workflows/download-and-deploy.md`.

## Boundary

- Extracting strings and uploading to TMS is `/rhdh-translation-upload`.
- Repository locations and branch context are `/rhdh-context`.
- External writes (creating PRs, pushing branches) go through `/mutation-gate`.

## Completion

Report per-repo: files changed, keys updated/skipped, changesets, and PR URLs
when created. Note that backstage has no upstream PR.
