# ship

Load when branching, committing, opening a PR, merging or reverting.

## branch

```bash
git switch -c fix/parser-trailing-comma
git fetch origin && git rebase origin/main
```

One concern per branch. A branch that fixes a bug and renames a module cannot be reverted cleanly.

## commit

Subject: imperative, under 72 chars, states why.

```
reject trailing comma in invoice parser

The parser accepted "1,2," and produced a phantom line item.
Guard the token loop and add the regression case.
```

- Body wraps at 72.
- One logical change per commit.
- Never commit a secret, a build artifact or a lockfile churn from a different tool.
- Check before committing: `git diff --cached` and `git status --porcelain`.

## pr

```bash
gh pr create --title "reject trailing comma in invoice parser" --body-file pr.md
```

Body sections: what changed, why, how it was verified, what is not covered.

- Link the issue.
- Paste the command and exit status of the verification.
- Screenshots for UI changes, before and after.
- State the rollback path for a migration.

## review loop

1. Push, wait for CI. Read the failing job log, not the summary.
2. Address findings with a commit each, or a stated reason to decline.
3. Re-request review after the last change. Do not merge past an open Required.
4. Resolve threads only when the code changed or the reason is written.

## merge

| strategy | use when |
| --- | --- |
| squash | feature branch, history noise |
| rebase | linear history is a project rule |
| merge commit | the branch history itself is the record |

Delete the branch after merge.

## revert

```bash
git revert --no-edit <sha>
```

Revert first, diagnose second, when main is broken. A forward fix under pressure adds a second defect.

## release

- Tag after CI is green on the merge commit.
- Changelog from merged PR titles, grouped by type.
- Publish from the tag, never from a laptop working tree.
