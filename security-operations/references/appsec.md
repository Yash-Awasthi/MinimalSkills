# appsec

Load for authorized web, API and identity testing.

## web checks

| class | probe | signal |
| --- | --- | --- |
| injection | `' OR 1=1--`, `;id`, `${7*7}` | error text, 49 in output, time delta |
| xss | `<img src=x onerror=alert(1)>` | reflected unencoded, stored |
| ssrf | `http://169.254.169.254/latest/meta-data/` | metadata body |
| path traversal | `../../etc/passwd`, `%2e%2e%2f` | file content |
| idor | swap an id for another user's | foreign object returned |
| open redirect | `?next=https://evil.test` | 302 to foreign host |
| deserialization | crafted cookie or body | gadget execution |
| template injection | `{{7*7}}` in every rendered field | 49 rendered |

Test one parameter at a time. Two variables per request produces unreadable evidence.

## auth

- Enumerate the auth path: login, refresh, reset, invite, oauth callback, logout.
- Check token storage, lifetime, rotation, revocation.
- Confirm access control server side: replay the request with a lower-privilege token.
- Test password reset for user enumeration and token reuse.
- MFA bypass classes: response manipulation, code reuse, backup code brute force, session fixation.

## api

```bash
curl -s -X POST https://api.example.com/v1/users \
  -H "authorization: Bearer $TOKEN" \
  -H "content-type: application/json" \
  -d '{"role":"admin"}' -i
```

- Mass assignment: add fields the UI does not send.
- Verb tampering: `GET` vs `POST` vs `PUT` on the same route.
- Rate limits: measure the window and the key. Per-IP only is bypassable.
- GraphQL: introspection, depth limit, batched queries, field-level authorization.
- Versioning: old versions keep old auth bugs.

## triage

| question | if no |
| --- | --- |
| is the code path reachable in production | downgrade to informational |
| is the version affected per the advisory | not a finding |
| does the payload survive the framework's encoding | not a finding |
| is the data real or a fixture | state which |

A reflected payload that the framework escapes on output is not xss.

## evidence

Per finding: request line, full headers, body, response status and body, timestamp, account role used. Reproduce twice. Attach the smallest payload that works.

## stop

- Third-party host in scope by accident: stop, notify.
- Real user data reached: capture three records, stop, report.
- Destructive proof required: report the theory, ask before acting.
