# review

Load when reviewing a diff, PR, patch or proposed change.

## order

1. Correctness: does it do what the request says.
2. Error paths: every failure branch has a defined outcome.
3. Concurrency: shared state, ordering, cancellation.
4. Resources: close, cancel, release on every path.
5. Tests: assert behavior, not implementation.
6. Naming and placement: last, and only if it costs nothing.

## severity

| level | meaning | merge effect |
| --- | --- | --- |
| Critical | data loss, auth bypass, secret leak, crash on main path | blocks |
| Required | wrong behavior, missing error path, uncovered branch | blocks |
| Optional | simpler shape, better name, missing comment | author decides |
| Nit | style the linter already allows | never blocks |

## finding shape

```
file:line  [severity]
input: <the call or data that triggers it>
result: <observed or predicted consequence>
fix: <smallest change>
```

No finding without a location. "This is wrong" is not a finding.

## diff reading

```bash
git fetch origin
git diff --stat $(git merge-base origin/main HEAD)...HEAD
git diff $(git merge-base origin/main HEAD)...HEAD -- src/
```

- Pin the range. A moving base makes the review unreproducible.
- Read deleted lines. A removed guard is a behavior change.
- Read the tests first. They state the intent the author believes.
- Check call sites of changed signatures: `rg "functionName\(" -t ts`.

## red flags

- fallback added instead of a cause found
- catch that swallows and logs
- retry without an idempotency key
- timeout raised to hide a slow call
- assertion weakened or deleted
- snapshot regenerated with no diff read
- generated file edited by hand

## scope honesty

State what you did not read: vendored code, generated clients, migrations, lockfiles, large data files. An unread file is unverified, not approved.

## output

- verdict: approve, approve with nits, request changes
- findings in severity order
- commands run, with exit status

## review index

| check | what to look for |
| --- | --- |
| IDOR | An id from the request used without an owner check; swap two users' ids and diff the response. |
| HTML injection | User input concatenated into markup; `dangerouslySetInnerHTML`, `v-html`, `innerHTML` in the diff. |
| WordPress pentest | Plugin versions in `readme.txt`, `/wp-json/wp/v2/users` enumeration, `xmlrpc.php` for brute force. |
| Wi-Fi/wireless | WPA2 handshake capture, rogue AP, captive portal bypass; authorized engagement only. |
| AccessLint | Runs axe on a PR preview; a new violation fails the check, a waived one needs a reason. |
| HTTP status tester | Every documented status is reachable by a test; a 500 path with no test is unhandled. |
| Robots validator | `robots.txt` and `sitemap.xml` parse, no `Disallow: /` on production, canonical host consistent. |
| Differential security review | Compare the changed handler against its sibling: the missing check is usually the one the sibling has. |
