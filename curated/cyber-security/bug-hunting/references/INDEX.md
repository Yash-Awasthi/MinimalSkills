# Bug-hunting index

57 vulnerability classes and 26 playbooks. Load only the class or playbook for the target.

## Classes

| Group | Classes |
| --- | --- |
| **Injection & execution** | [`sqli`](classes/sqli.md), [`nosqli`](classes/nosqli.md), [`ldap`](classes/ldap.md), [`ssti`](classes/ssti.md), [`xxe`](classes/xxe.md), [`deserialization`](classes/deserialization.md), [`rce`](classes/rce.md), [`lfi`](classes/lfi.md), [`html-injection`](classes/html-injection.md) |
| **Client-side** | [`xss`](classes/xss.md), [`dom`](classes/dom.md), [`csrf`](classes/csrf.md), [`clickjacking`](classes/clickjacking.md), [`cors`](classes/cors.md), [`open-redirect`](classes/open-redirect.md) |
| **Auth & session** | [`auth-bypass`](classes/auth-bypass.md), [`ato`](classes/ato.md), [`brute-force`](classes/brute-force.md), [`forgot-password`](classes/forgot-password.md), [`mfa-bypass`](classes/mfa-bypass.md), [`oauth`](classes/oauth.md), [`saml`](classes/saml.md), [`jwt-crypto`](classes/jwt-crypto.md), [`session`](classes/session.md), [`ntlm-info`](classes/ntlm-info.md) |
| **Access & logic** | [`idor`](classes/idor.md), [`business-logic`](classes/business-logic.md), [`race-condition`](classes/race-condition.md), [`captcha-bypass`](classes/captcha-bypass.md) |
| **Request & transport** | [`http-smuggling`](classes/http-smuggling.md), [`host-header`](classes/host-header.md), [`cache-poison`](classes/cache-poison.md), [`ssrf`](classes/ssrf.md), [`tls-network`](classes/tls-network.md), [`websocket`](classes/websocket.md), [`grpc`](classes/grpc.md) |
| **API & protocol** | [`api-misconfig`](classes/api-misconfig.md), [`graphql`](classes/graphql.md), [`fintech-graphql`](classes/fintech-graphql.md), [`shadow-api`](classes/shadow-api.md), [`spa-api`](classes/spa-api.md) |
| **Files & disclosure** | [`file-upload`](classes/file-upload.md), [`source-leak`](classes/source-leak.md), [`exceptional-conditions`](classes/exceptional-conditions.md) |
| **Framework & stack** | [`aspnet`](classes/aspnet.md), [`laravel`](classes/laravel.md), [`nextjs`](classes/nextjs.md), [`nodejs`](classes/nodejs.md), [`springboot`](classes/springboot.md), [`sharepoint`](classes/sharepoint.md) |
| **Cloud & CI** | [`cloud-misconfig`](classes/cloud-misconfig.md), [`k8s`](classes/k8s.md), [`cicd`](classes/cicd.md), [`subdomain`](classes/subdomain.md) |
| **AI systems** | [`llm-ai`](classes/llm-ai.md), [`rag-vector`](classes/rag-vector.md) |
| **Misc** | [`misc`](classes/misc.md) |

## Playbooks

| Group | Playbooks |
| --- | --- |
| **Engagement** | [`bug-bounty`](playbooks/bug-bounty.md), [`bb-methodology`](playbooks/bb-methodology.md), [`bb-local-toolkit`](playbooks/bb-local-toolkit.md), [`recon-scope-triage`](playbooks/recon-scope-triage.md), [`security-arsenal`](playbooks/security-arsenal.md), [`web2-recon`](playbooks/web2-recon.md), [`supply-chain-attack-recon`](playbooks/supply-chain-attack-recon.md), [`cloud-iam-deep`](playbooks/cloud-iam-deep.md) |
| **Reporting** | [`report-writing`](playbooks/report-writing.md), [`bugcrowd-reporting`](playbooks/bugcrowd-reporting.md), [`redteam-report-template`](playbooks/redteam-report-template.md), [`triage-validation`](playbooks/triage-validation.md), [`evidence-hygiene`](playbooks/evidence-hygiene.md) |
| **Red team** | [`redteam-mindset`](playbooks/redteam-mindset.md), [`mid-engagement-ir-detection`](playbooks/mid-engagement-ir-detection.md), [`enterprise-vpn-attack`](playbooks/enterprise-vpn-attack.md), [`m365-entra-attack`](playbooks/m365-entra-attack.md), [`okta-attack`](playbooks/okta-attack.md), [`vmware-vcenter-attack`](playbooks/vmware-vcenter-attack.md), [`apk-redteam-pipeline`](playbooks/apk-redteam-pipeline.md), [`ios-redteam-pipeline`](playbooks/ios-redteam-pipeline.md) |
| **OSINT** | [`offensive-osint`](playbooks/offensive-osint.md), [`osint-methodology`](playbooks/osint-methodology.md) |
| **Web3** | [`web3-audit`](playbooks/web3-audit.md), [`meme-coin-audit`](playbooks/meme-coin-audit.md) |
| **Routing** | [`hunt-dispatch`](playbooks/hunt-dispatch.md) |
