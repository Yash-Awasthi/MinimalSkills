# redteam

Load for authorized adversary simulation and detection engineering.

## plan

1. Objective: data, access, or a specific business process.
2. Entry assumption: external, assumed breach, insider, or supply chain.
3. Rules of engagement: techniques allowed, prohibited targets, notification threshold, kill date.
4. Detection goal: what the blue team should have seen and when.
5. Stop condition written before the first action.

An engagement without a stop condition becomes an incident.

## kill chain, mapped

| phase | technique class | typical control |
| --- | --- | --- |
| recon | passive dns, certs, public repos | asset inventory |
| initial access | phishing, exposed service, valid account | mfa, patching |
| execution | signed binary, script host, container exec | app allowlist, edr |
| persistence | scheduled task, service, token | baseline diffing |
| privilege escalation | misconfig, token, kernel | least privilege |
| credential access | lsass, keychain, cloud metadata | edr, secret store |
| lateral movement | smb, winrm, ssh, cloud role | segmentation |
| collection | archive, db dump | dlp, egress control |
| exfiltration | dns, https, cloud storage | egress allowlist |

Map every action to a technique id. Unmapped action, unwritten report.

## c2 hygiene

- Redirector in front of the team server. Never expose the team server directly.
- Domain age and category checked before use.
- Beacons have a kill date and a single owner.
- Payloads stored encrypted at rest, destroyed at closeout.
- No real user credentials in test payloads.

## phishing, when allowed

- Written approval for named targets. Executives and legal counsel excluded unless explicitly listed.
- Landing page hosts no real credential capture. Use a token or a form that discards input.
- Report template pre-agreed with the client so a report does not look like a real phish.

## detection engineering

| signal | source | rule shape |
| --- | --- | --- |
| new service installed | windows event 7045 | service name not in baseline |
| lsass access | edr telemetry | handle request with read memory |
| metadata api call | vpc flow, cloudtrail | 169.254.169.254 from a workload |
| mass file rename | filesystem audit | rate over threshold |
| token reuse | idp logs | same token, two geos, 5 min |

Ship the rule with a test case that fires and one that stays quiet.

## closeout

- Every beacon killed, verified by callback log.
- Credentials used are rotated.
- Timeline delivered with timestamps and technique ids.
- Blue team gets the detection gaps, not just the successes.
