#!/usr/bin/env bash
# Update all skill repo clones in repos/ and regenerate repos.manifest.tsv
# Usage: ./update-repos.sh
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPOS="$ROOT/repos"
MANIFEST="$ROOT/repos.manifest.tsv"

cd "$REPOS" || { echo "repos/ not found"; exit 1; }

updated=0
current=0
failed=0

for dir in */; do
  dir="${dir%/}"
  [ -d "$dir/.git" ] || continue

  # Never touch a mirror that has local edits or untracked files.
  if [ -n "$(git -C "$dir" status --porcelain 2>/dev/null)" ]; then
    echo "SKIP    $dir (local changes)"
    failed=$((failed + 1))
    continue
  fi

  before="$(git -C "$dir" rev-parse HEAD 2>/dev/null || echo '')"
  if ! git -C "$dir" fetch --depth 1 --quiet origin 2>/dev/null; then
    echo "FAIL    $dir (fetch failed)"
    failed=$((failed + 1))
    continue
  fi

  # Shallow clones have no shared ancestry, so move the branch to the fetched tip.
  if ! git -C "$dir" reset --hard --quiet FETCH_HEAD 2>/dev/null; then
    echo "FAIL    $dir (reset failed)"
    failed=$((failed + 1))
    continue
  fi

  after="$(git -C "$dir" rev-parse HEAD 2>/dev/null || echo '')"
  if [ "$before" = "$after" ]; then
    current=$((current + 1))
  else
    echo "UPDATED $dir"
    updated=$((updated + 1))
  fi
done

echo "---"
echo "updated=$updated current=$current failed=$failed"

# Regenerate manifest: name, url, branch, commit, commit date, skills (SKILL.md count), files
printf 'repo\turl\tbranch\tcommit\tcommit_date\tskills\tfiles\n' > "$MANIFEST"
for dir in */; do
  dir="${dir%/}"
  [ -d "$dir/.git" ] || continue
  url="$(git -C "$dir" remote get-url origin 2>/dev/null)"
  branch="$(git -C "$dir" rev-parse --abbrev-ref HEAD 2>/dev/null)"
  commit="$(git -C "$dir" rev-parse --short HEAD 2>/dev/null)"
  date="$(git -C "$dir" log -1 --format=%cs 2>/dev/null)"
  skills="$(find "$dir" -name SKILL.md 2>/dev/null | wc -l | tr -d ' ')"
  files="$(find "$dir" -path "$dir/.git" -prune -o -type f -print 2>/dev/null | wc -l | tr -d ' ')"
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$dir" "$url" "$branch" "$commit" "$date" "$skills" "$files" >> "$MANIFEST"
done

total="$(grep -c . "$MANIFEST")"
echo "manifest: $MANIFEST (${total} lines incl. header)"

[ "$failed" -eq 0 ]
