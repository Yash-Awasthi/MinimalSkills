# auth-secrets

Load for sessions, tokens, permissions and secret handling.

## session vs token

| need | choice |
| --- | --- |
| browser app, server rendered | http-only session cookie |
| mobile, first-party | short access token + refresh |
| third-party api access | oauth client credentials or scoped key |
| service to service | workload identity, not a shared key |

Cookie flags: `HttpOnly; Secure; SameSite=Lax; Path=/`. `SameSite=None` needs `Secure` and a csrf defense.

## tokens

- Access token 5-15 minutes. Refresh token 30 days, rotated on use.
- Store refresh tokens hashed. A plaintext token table is a breach waiting.
- Revoke on password change, role change and logout everywhere.
- Validate: signature, `exp`, `iss`, `aud`, `nbf`. Not just the signature.

## authorization

```ts
const invoice = await db.invoice.findUnique({ where: { id } });
if (!invoice || invoice.ownerId !== user.id) return err('not_found', 404);
```

- Check the record, not the route. Route-level checks miss the id swap.
- Deny by default. A new endpoint starts closed.
- Roles for coarse access, attributes for ownership.
- Tenant id in every query, from the session, never from the request body.

## secrets

| place | allowed |
| --- | --- |
| secret manager, injected at runtime | yes |
| environment variable from the manager | yes |
| repo, image layer, log, error message | never |
| client bundle | never |

- Rotate on exposure first, purge logs second.
- One secret per environment and per service; a shared key means one leak revokes every service at once.
- Prefix search before commit: `rg -i "sk-|ghp_|AKIA|BEGIN PRIVATE"`.

## password storage

argon2id with a per-user salt and a tuned cost, or bcrypt cost 12. Never sha256. Never a homemade scheme.

## failures

| case | response |
| --- | --- |
| unknown user | same timing and message as a wrong password |
| expired token | 401 with `token_expired`, client refreshes once |
| insufficient role | 403, no detail about the resource |
| rate limit hit | 429 with `Retry-After` |
| repeated failures | lockout with exponential delay, logged |

## review

- Every route has an auth check, listed in a table.
- No secret in a log line, including the error path.
- Permission tests exist for the deny case.
## auth index

| topic | the rule that matters |
| --- | --- |
| Broken authentication | Credential stuffing defense is rate limit plus lockout plus breached-password check; a 200 on a wrong password leaks enumeration. |
| Django access review | Audit every `permission_required`, `LoginRequiredMixin` and raw `request.user` check; a view with none is open. |
| VMware vCenter | Default `administrator@vsphere.local`, SSO token lifetime and the `/rest/com/vmware/cis/session` endpoint are the usual exposure. |
| security-best-practices | Deny by default, least privilege, fail closed; a catch-all `try/except: pass` around an auth check fails open. |
| security-testing | Test the negative path: no token, expired token, another user's token, a token for the wrong scope. |
| fuzzing | Fuzz the parser and the boundary, not the ORM; a crash and a 500 are different findings. |
