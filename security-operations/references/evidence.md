# evidence

Load when writing a finding or handling artifacts from a test.

## confidence

| label | meaning | allowed claim |
| --- | --- | --- |
| observed | reproduced with a recorded request | present as fact |
| inferred | code path read, not executed | state the inference and the missing step |
| unverified | tool output only | candidate, no severity |

Extraction confidence is not impact confidence: a confirmed version with unknown reachability stays Unknown, not High.

## record per action

```
utc:        2026-03-04T11:22:31Z
source:     203.0.113.9
target:     https://app.example.com/api/v1/users/42
action:     GET with user B token
result:     200, body contains user A email
hash:       sha256 of the response body
```

A finding without a timestamp, a target and a hash cannot be replayed, and gets disputed at the first pushback.

## finding shape

```
title:      IDOR on GET /api/v1/users/{id}
severity:   high
impact:     any authenticated user reads any user record
repro:      1. login as B  2. GET /api/v1/users/42  3. observe A's email
evidence:   request.txt, response.txt, sha256
fix:        authorize the record against the caller, not the route
```

Severity from impact and reachability, not from the tool's label.

## redaction

- Credentials become placeholders: `<REDACTED-PASSWORD>`, `<TOKEN-A1>`.
- PII is hashed or replaced, never screenshotted raw.
- Crop screenshots. Check browser tabs and autocomplete for session tokens.
- Strip metadata: `exiftool -all= shot.png`.
- Remove internal hostnames, client names and debug toolbars from images.
- Keep the original in the secure store, share the redacted copy.

## reporting

- Executive summary: what an attacker gains, in one paragraph.
- Findings sorted by severity, each with repro and fix.
- Coverage: what was tested, what was not, what blocked testing.
- Negative results carry scope: "no injection found in 14 parameters across 3 endpoints".

## handoff

Destroy beacons and test accounts at the end. Confirm the kill date executed. A forgotten callback is legal liability.
