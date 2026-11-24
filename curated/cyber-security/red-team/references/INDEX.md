# Red-team tactic index

77 tactics in 9 groups. Load only the tactic for the current phase or surface.

| Group | Tactics |
| --- | --- |
| **Web & API** | 22 |
| **Windows & Active Directory** | 11 |
| **Exploit dev & research** | 9 |
| **Cloud & supply chain** | 7 |
| **Network & operations** | 6 |
| **Wireless / RF / hardware** | 15 |
| **OSINT / social / mobile** | 5 |
| **AI security** | 1 |
| **Reporting** | 1 |

## Web & API

| Tactic | Purpose |
| --- | --- |
| [`api-abuse`](tactics/api-abuse.md) | Advanced API exploitation methodology focused on business logic abuse and sophisticated attack patterns that bypass traditional security controls. Covers business logic bypass through API call chaining and workflow manipulation. Addresses GraphQL-specific a... |
| [`api-security`](tactics/api-security.md) | Comprehensive API security testing methodology covering REST, gRPC, and WebSocket attack surfaces. Addresses the full OWASP API Security Top 10 2023 including BOLA/IDOR, broken authentication, excessive data exposure, rate limiting bypass, BFLA, mass assign... |
| [`business-logic`](tactics/business-logic.md) | Business logic vulnerability testing for web/mobile/API engagements. Covers workflow bypass, state machine violations, multi-step process abuse, price/quantity/discount manipulation, currency confusion, coupon stacking, refund/chargeback abuse, race conditi... |
| [`crypto-attacks`](tactics/crypto-attacks.md) | Systematic methodology for identifying and exploiting cryptographic implementation weaknesses in real-world applications. Covers padding oracle attacks against CBC-mode ciphers with PKCS7 padding (Vaudenay's original attack through modern padbuster automati... |
| [`deserialization`](tactics/deserialization.md) | Insecure deserialization exploitation across Java, PHP, .NET, Python, Node.js, and Ruby. Covers gadget chain construction with ysoserial/phpggc/ysoserial.net, ObjectInputStream and BinaryFormatter sink identification, pickle __reduce__ RCE, phar:// wrapper... |
| [`fast-checking`](tactics/fast-checking.md) | Speed-optimized offensive checklist for rapid assessment: quick-win vulnerability patterns, fast recon shortcuts, automated scanner configurations, and triage shortcuts. Use for time-boxed assessments, CTF-speed engagements, or initial rapid surface mapping. |
| [`file-upload`](tactics/file-upload.md) | File upload vulnerability checklist: MIME type bypass, extension bypass, magic byte manipulation, path traversal in filenames, stored XSS via SVG/HTML upload, server-side processing attacks, and race conditions. Use for assessing file upload endpoints in we... |
| [`graphql`](tactics/graphql.md) | Offensive methodology for attacking GraphQL APIs during penetration tests and bug bounty engagements. Covers the full attack lifecycle: endpoint discovery, introspection abuse and blind schema reconstruction when introspection is disabled, authentication an... |
| [`idor`](tactics/idor.md) | IDOR (Insecure Direct Object Reference) testing checklist: object ID enumeration, horizontal/vertical privilege escalation, GUID predictability, indirect references via hashes, chained IDOR, and API endpoint IDOR. Use for web app pentests and bug bounty IDO... |
| [`jwt`](tactics/jwt.md) | JWT attack methodology for penetration testers. Covers algorithm confusion (alg:none, RS256→HS256), weak HMAC secret brute force, kid parameter injection (SQLi, path traversal), jku/x5u/jwk header injection, JWKS cache poisoning, JWS/JWE confusion, timing a... |
| [`oauth`](tactics/oauth.md) | OAuth 2.0 attack checklist: authorization code interception, redirect_uri bypass, CSRF on OAuth flow, state parameter abuse, open redirector chaining, token leakage via Referer, PKCE bypass, and scope escalation. Use when testing OAuth implementations in we... |
| [`open-redirect`](tactics/open-redirect.md) | Open redirect vulnerability checklist: parameter identification, bypass techniques (URL encoding, double slashes, CRLF injection, protocol handlers), chaining with OAuth/SSRF, and impact escalation paths. Use for web app testing and bug bounty open redirect... |
| [`parameter-pollution`](tactics/parameter-pollution.md) | HTTP parameter pollution (HPP) checklist: duplicate parameter injection, backend vs frontend parsing differences, WAF bypass via HPP, server-side vs client-side HPP, and practical exploitation patterns. Use when testing web applications for parameter handli... |
| [`race-condition`](tactics/race-condition.md) | Race condition (TOCTOU) testing checklist: identifying timing windows, Burp Suite Turbo Intruder, Last-Byte sync technique, rate limit bypass, double-spend attacks, and concurrent request exploitation. Use for web app race condition testing or bug bounty ti... |
| [`request-smuggling`](tactics/request-smuggling.md) | HTTP request smuggling checklist: CL.TE, TE.CL, TE.TE variants, detection with timing and differential responses, WAF bypass, cache poisoning, credential hijacking, and request smuggling via HTTP/2. Use when testing reverse proxy/load balancer configurations. |
| [`ssrf`](tactics/ssrf.md) | Server-Side Request Forgery testing checklist: SSRF discovery, blind SSRF with out-of-band, cloud metadata endpoints (AWS/GCP/Azure), SSRF filter bypass techniques (IP encoding, DNS rebinding, redirect chains), and SSRF to RCE escalation. Use for web app SS... |
| [`ssti`](tactics/ssti.md) | Dense description covering Server-Side Template Injection across Jinja2, Twig, Freemarker, Velocity, Pebble, Smarty, Mako, Handlebars, ERB, Thymeleaf, EJS, Pug. Engine fingerprinting, filter bypass, blind exploitation, WAF evasion, SSTI-to-RCE chains. Tools... |
| [`toctou`](tactics/toctou.md) | Time-of-Check / Time-of-Use (TOCTOU) race condition exploitation methodology across binary, kernel, filesystem, web, and container layers. Covers symbolic-link races (open/access/stat split), file-descriptor races, fopen/realpath traversal races, /proc and... |
| [`vuln-classes`](tactics/vuln-classes.md) | Exploit development curriculum covering core vulnerability classes with real-world CVE case studies: stack/heap buffer overflows, use-after-free, integer overflows, format strings, type confusion, and race conditions. Use when learning or teaching vuln clas... |
| [`waf-bypass`](tactics/waf-bypass.md) | WAF bypass techniques checklist: encoding bypass (URL/HTML/Unicode/double encoding), case variation, comment injection, HTTP header manipulation, chunked encoding, IP rotation, timing attacks, and payload obfuscation per WAF vendor. Use when WAF is blocking... |
| [`xss`](tactics/xss.md) | Cross-Site Scripting testing checklist: stored/reflected/DOM/blind XSS discovery, polyglot payloads, CSP bypass, XSS filter bypass, event handler injection, DOM clobbering, mutation XSS, and impact escalation (session hijack, phishing, keylogging). Use for... |
| [`xxe`](tactics/xxe.md) | XML External Entity injection testing checklist: classic XXE, blind XXE (out-of-band), XXE via file upload (SVG/docx), XXE in SOAP/REST, error-based XXE, XInclude attacks, and XXE filter bypass. Use for web app XXE testing and bug bounty. |


## Windows & Active Directory

| Tactic | Purpose |
| --- | --- |
| [`active-directory`](tactics/active-directory.md) | Active Directory attack methodology for internal network red team engagements. Covers reconnaissance (BloodHound, PowerView, ADExplorer), credential abuse (Kerberoasting, ASREProasting, NTLM relay, LLMNR/NBT-NS poisoning), privilege escalation (ACL abuse, G... |
| [`anti-forensics`](tactics/anti-forensics.md) | Anti-forensics and evidence destruction techniques for red team operators conducting authorized engagements. Covers log clearing on Windows (wevtutil, Clear-EventLog, ETW provider patching) and Linux (journal truncation, utmp/wtmp binary editing, syslog man... |
| [`edr-evasion`](tactics/edr-evasion.md) | EDR evasion offensive checklist: hook unhooking (user/kernel), direct syscalls, PPID spoofing, process injection variants, AMSI bypass, ETW patching, memory encryption, and behavior-based evasion. Use when planning EDR bypass during red team engagements or... |
| [`keylogger-arch`](tactics/keylogger-arch.md) | Low-level keylogger architecture design: kernel driver hooks (WH_KEYBOARD_LL, SetWindowsHookEx), ETW-based input capture, user-mode vs kernel-mode approaches, stealth techniques, and data exfiltration. Use for understanding input capture mechanisms, EDR eva... |
| [`lateral-movement`](tactics/lateral-movement.md) | Comprehensive lateral movement tradecraft for authorized red team engagements covering credential-based movement (pass-the-hash, pass-the-ticket, overpass-the-hash), NTLM relay attacks (ntlmrelayx with PetitPotam, DFSCoerce, PrinterBug coercion), remote exe... |
| [`netexec`](tactics/netexec.md) | Use this skill whenever the user asks about NetExec (nxc) — a network exploitation and post-exploitation tool for Active Directory environments. Triggers include: any mention of 'nxc', 'netexec', 'crackmapexec' successor questions, AD enumeration, SMB/LDAP/... |
| [`persistence`](tactics/persistence.md) | Comprehensive persistence tradecraft for authorized red team engagements covering Windows and Linux mechanisms. Windows techniques include registry Run/RunOnce keys, scheduled tasks, WMI event subscriptions, DLL search order hijacking, COM object hijacking,... |
| [`shellcode`](tactics/shellcode.md) | Shellcode development reference for offensive security engagements. Use when writing custom x86/x64 shellcode, implementing position-independent code (PIC), building shellcode loaders, evading AV/EDR detection, or converting PE files to shellcode. Covers nu... |
| [`windows-boundaries`](tactics/windows-boundaries.md) | Windows security boundary taxonomy and attack surface enumeration: kernel/user boundary, sandbox boundaries (LPAC, AppContainer), COM/RPC boundaries, hypervisor boundary, trust level transitions. Use when planning privilege escalation paths, sandbox escapes... |
| [`windows-mitigations`](tactics/windows-mitigations.md) | Deep-dive on Windows exploit mitigations: ASLR, DEP/NX, CFG, CET/Shadow Stack, SEHOP, Heap Guard, ACG, Arbitrary Code Guard. Covers both the protection mechanism and known bypass techniques. Use when researching Windows exploit mitigations, planning bypass... |
| [`windows-privesc`](tactics/windows-privesc.md) | Comprehensive Windows privilege escalation methodology for offensive security engagements. Covers the full attack surface from a standard user shell to NT AUTHORITY\\SYSTEM: token impersonation via SeImpersonate and SeAssignPrimaryToken privileges using Jui... |


## Exploit dev & research

| Tactic | Purpose |
| --- | --- |
| [`basic-exploitation`](tactics/basic-exploitation.md) | Week 5 exploit development curriculum. Foundational exploitation techniques: controlling EIP/RIP, ROP chain construction, ret2libc, shellcode injection, heap spraying, bypass techniques for ASLR/NX/stack canaries. Use when building initial PoCs or understan... |
| [`bug-identification`](tactics/bug-identification.md) | Systematic bug identification methodology: source code review patterns, black-box testing strategies, taint analysis, dangerous function hunting, data flow tracing, and automated scanning setup. Use for code audits, bug bounty triage, or building vulnerabil... |
| [`crash-analysis`](tactics/crash-analysis.md) | Week 4 exploit development curriculum. Crash triage and analysis methodology: WinDbg/GDB analysis, ASAN/MSAN output interpretation, exploitability assessment, register/stack trace reading, root cause identification. Use when analyzing crash dumps, assessing... |
| [`exploit-dev-course`](tactics/exploit-dev-course.md) | Full exploit development course roadmap and syllabus: weekly topics, recommended reading, lab setup, and learning path from vulnerability classes through advanced exploitation. Use to structure exploit dev training or onboard new researchers. |
| [`exploit-development`](tactics/exploit-development.md) | Exploit development operational guide: environment setup, debugging workflow, PoC development lifecycle, writing reliable exploits, using pwntools/pwndbg, heap exploitation techniques, and weaponization considerations. Use when actively developing exploits... |
| [`fuzzing`](tactics/fuzzing.md) | Practical offensive fuzzing methodology covering target identification, fuzzer selection (AFL++, libFuzzer, Honggfuzz, Boofuzz, syzkaller), harness writing, corpus curation, mutation strategies, coverage measurement, and crash triage. Use when setting up or... |
| [`fuzzing-course`](tactics/fuzzing-course.md) | Week 2 of the exploit development curriculum. Covers fuzzing methodology: target selection, corpus generation, coverage-guided fuzzing with AFL++/libFuzzer, structured fuzzing, and triage/deduplication. Use when setting up fuzz campaigns, selecting harness... |
| [`linux-privesc`](tactics/linux-privesc.md) | Comprehensive Linux privilege escalation methodology for offensive security engagements. Covers the full attack surface from a low-privilege shell to root: SUID/SGID binary abuse via GTFOBins, Linux capabilities exploitation (cap_setuid, cap_dac_override, c... |
| [`mitigations`](tactics/mitigations.md) | Security mitigation reference and bypass catalog: ASLR, DEP/NX, RELRO, stack canaries, CFI, sandboxing, seccomp. Covers both detection of enabled mitigations and known bypass techniques. Use when assessing target hardening or planning exploit mitigation byp... |


## Cloud & supply chain

| Tactic | Purpose |
| --- | --- |
| [`cicd-pipeline`](tactics/cicd-pipeline.md) | Comprehensive CI/CD pipeline exploitation methodology covering GitHub Actions injection vectors (expression injection via PR titles and issue bodies, workflow_run event abuse, GITHUB_TOKEN over-scoping, composite action supply chain compromise), Jenkins att... |
| [`cicd-secrets`](tactics/cicd-secrets.md) | Comprehensive secrets extraction methodology targeting CI/CD environments across all major platforms. Covers environment variable extraction from build contexts, exploitation of vault and secrets-manager misconfigurations (HashiCorp Vault, AWS Secrets Manag... |
| [`cloud`](tactics/cloud.md) | Cloud security attack methodology covering AWS, Azure, and GCP. Includes credential harvesting (IMDS, ~/.aws, env vars, leaked CI secrets, instance roles), enumeration with cloud-specific tools (pacu, ScoutSuite, Prowler, ROADtools, gcp_enum), privilege esc... |
| [`container-escape`](tactics/container-escape.md) | Container escape and breakout techniques targeting Docker, containerd, and Podman runtimes. Covers privileged container breakout via host filesystem mount and nsenter, Docker socket abuse through /var/run/docker.sock, Linux capability exploitation including... |
| [`dependency-confusion`](tactics/dependency-confusion.md) | Deep-dive offensive methodology for dependency confusion and namespace attacks across all major package ecosystems. Covers npm scope confusion exploiting the gap between public and private scoped packages and .npmrc misconfigurations where registry mappings... |
| [`k8s-attacks`](tactics/k8s-attacks.md) | Kubernetes cluster attack techniques covering the full attack lifecycle from initial foothold in a pod to cluster-wide compromise. Covers service account token theft and impersonation, RBAC misconfiguration exploitation including wildcard permissions and pr... |
| [`supply-chain`](tactics/supply-chain.md) | Comprehensive offensive methodology for software supply chain attacks covering the full kill chain from reconnaissance through exploitation. Addresses dependency confusion across npm, PyPI, and NuGet ecosystems where internal registry override allows an att... |


## Network & operations

| Tactic | Purpose |
| --- | --- |
| [`advanced-redteam`](tactics/advanced-redteam.md) | Comprehensive red team operations methodology covering full engagement lifecycle from planning through reporting. Addresses engagement scoping and rules of engagement negotiation, multi-tier C2 infrastructure design with redirectors and domain fronting, mal... |
| [`c2-frameworks`](tactics/c2-frameworks.md) | Command and Control framework deployment, configuration, and operational tradecraft for red team engagements. Covers Cobalt Strike (malleable C2 profiles, Beacon types HTTP/HTTPS/DNS/SMB, Beacon Object Files for in-memory execution, sleep and jitter tuning,... |
| [`data-exfiltration`](tactics/data-exfiltration.md) | Dense methodology covering DNS exfiltration (dnscat2, iodine, dns2tcp), HTTPS tunneling (domain fronting, CDN abuse, legitimate service channels), ICMP tunneling (icmpsh, ptunnel-ng), cloud storage dead drops (S3 presigned URLs, Azure Blob SAS tokens, GCS s... |
| [`initial-access`](tactics/initial-access.md) | Initial access techniques checklist: phishing (spear/smishing), credential stuffing, exposed service exploitation, supply chain attacks, watering hole, VPN/RDP brute force, public-facing application exploitation. Maps to MITRE ATT&CK TA0001. Use when planni... |
| [`network-attacks`](tactics/network-attacks.md) | Dense description covering ARP spoofing, LLMNR/NBT-NS/mDNS poisoning, DNS poisoning, MITM attacks, VLAN hopping, DHCP attacks, 802.1X/NAC bypass, IPv6 attacks. Tools: Bettercap, Responder, mitm6, Ettercap, Wireshark. MITRE T1557, T1040. Use when conducting... |
| [`tls-attacks`](tactics/tls-attacks.md) | Comprehensive methodology for auditing and exploiting TLS/SSL implementations and misconfigurations across network services and mobile applications. Covers protocol downgrade attacks including POODLE (CVE-2014-3566) against SSLv3 CBC padding, DROWN (CVE-201... |


## Wireless / RF / hardware

| Tactic | Purpose |
| --- | --- |
| [`bluetooth-ble`](tactics/bluetooth-ble.md) | Bluetooth Low Energy (BLE) attack methodology — GATT enumeration, characteristic read/write without auth, pairing downgrade (Just Works forced), LE Secure Connections bypass, MITM via active relay, sniffing with Sniffle (TI CC1352) / Ubertooth / Frontline,... |
| [`bluetooth-classic`](tactics/bluetooth-classic.md) | Bluetooth Classic (BR/EDR) attack methodology — device discovery, service enumeration via SDP, LMP/L2CAP layer attacks, legacy PIN cracking (BlueBorne / KNOB), Bluetooth file-transfer abuse (BlueSnarfing legacy), unauthenticated profile abuse (HSP, HFP, OPP... |
| [`deauth-disassoc`](tactics/deauth-disassoc.md) | Deauthentication and disassociation attacks against 802.11 networks — targeted single-client deauth for handshake capture, broadcast deauth for DoS (with authorization), action-frame attacks bypassing 802.11w (PMF), beacon flooding, mdk4 / aireplay-ng tooli... |
| [`evil-twin`](tactics/evil-twin.md) | Evil Twin / KARMA / Mana access point methodology — rogue AP construction with hostapd-mana / wifiphisher / airgeddon, KARMA universal probe response, Mana selective probe response, captive portal phishing, deauth-driven client coercion to attacker AP, MAC... |
| [`iot`](tactics/iot.md) | IoT and embedded device security testing methodology. Covers hardware reconnaissance (UART, JTAG, SWD, SPI flash, I2C EEPROM, eMMC chip-off), firmware acquisition (vendor portals, OTA capture, flash dump, binwalk extraction), firmware analysis (filesystem m... |
| [`krack-fragattacks`](tactics/krack-fragattacks.md) | KRACK (CVE-2017-13077..082) and FragAttacks (CVE-2020-24586..588 + 26139-26147) — key reinstallation, fragmentation, and aggregation attacks against WPA2 supplicants. Covers Vanhoef's test scripts, viability against modern patched stacks (mostly mitigated p... |
| [`lorawan-sub-ghz`](tactics/lorawan-sub-ghz.md) | LoRaWAN and sub-GHz (433 / 868 / 915 MHz) attack methodology — LoRaWAN ABP/OTAA join attack, network/session key reuse, frame counter replay, downlink injection on TTN/Helium-style networks, sub-GHz protocol replay (KeeLoq garage doors, fixed-code remotes,... |
| [`wifi`](tactics/wifi.md) | Wireless / 802.11 attack methodology for red team engagements and wireless security assessments. Covers monitor-mode setup, WPA/WPA2-PSK handshake capture and PMKID attacks, WPA3 SAE downgrade and Dragonblood, WPA-Enterprise (EAP) attacks (MSCHAPv2 cracking... |
| [`wifi-recon`](tactics/wifi-recon.md) | Wi-Fi reconnaissance methodology — adapter selection, monitor mode and packet injection setup, regulatory domain handling, multi-band airspace mapping, hidden SSID discovery, BSSID/ESSID/channel/PMF/encryption fingerprinting, client probe analysis, vendor O... |
| [`wpa-enterprise`](tactics/wpa-enterprise.md) | WPA/WPA2/WPA3-Enterprise (802.1X / EAP) attack methodology — EAP method identification (PEAP-MSCHAPv2, EAP-TTLS, EAP-TLS, EAP-GTC, EAP-PWD, EAP-FAST), evil-twin RADIUS attacks with eaphammer for credential capture, MSCHAPv2 challenge-response cracking, EAP-... |
| [`wpa2-psk`](tactics/wpa2-psk.md) | WPA/WPA2-PSK attack methodology — four-way handshake capture via targeted deauthentication, PMKID attacks (no client required), hcxdumptool / hcxpcapngtool conversion to hashcat hc22000 format, GPU-accelerated cracking with dictionary, mask, and rule-based... |
| [`wpa3-sae`](tactics/wpa3-sae.md) | WPA3 / SAE (Simultaneous Authentication of Equals) attack methodology — transition-mode (mixed WPA2/WPA3) downgrade, Dragonblood side-channel attacks (CVE-2019-9494, 9495, 13377, 13456), SAE auth flooding for AP CPU exhaustion, Hash-to-Element (H2E) timing... |
| [`wps`](tactics/wps.md) | WPS (Wi-Fi Protected Setup) PIN attack methodology — Pixie Dust offline attack against vulnerable chipsets (Ralink, Realtek, Broadcom, MediaTek), online PIN brute-force with reaver/bully, lockout handling, time-of-day evasion, WPS push-button vulnerability... |
| [`z-wave`](tactics/z-wave.md) | Z-Wave attack methodology — sniffing with Z-Force / EZ-Wave / RTL-SDR + ZniffMobile, S0 (legacy) network-key derivation flaw and key reuse, S2 (modern) ECDH commissioning analysis, replay/injection on unauthenticated nodes, default-key brute-force on test d... |
| [`zigbee-thread-matter`](tactics/zigbee-thread-matter.md) | Zigbee, Thread, and Matter mesh-protocol attack methodology — IEEE 802.15.4 sniffing with TI CC2531 / CC2540 / Sonoff Zigbee Dongle E, KillerBee toolkit, Touchlink commissioning abuse with the well-known transport key, replay/injection attacks, Zigbee Clust... |


## OSINT / social / mobile

| Tactic | Purpose |
| --- | --- |
| [`mobile`](tactics/mobile.md) | Mobile (Android + iOS) application penetration testing methodology. Covers static analysis (apktool/jadx for Android, class-dump/Hopper/IDA for iOS), dynamic instrumentation with Frida and Objection, SSL pinning bypass strategies, root/jailbreak detection b... |
| [`osint`](tactics/osint.md) | Comprehensive OSINT methodology skill for offensive security, red team intelligence gathering, and bug bounty reconnaissance. Covers domain recon, email harvesting, social media profiling, GitHub/code leaks, Shodan/Censys enumeration, breach data lookup, em... |
| [`osint-methodology`](tactics/osint-methodology.md) | Structured OSINT methodology framework: target definition, source selection, collection workflows, data correlation, timeline reconstruction, and reporting. Use to guide systematic OSINT campaigns or teach OSINT methodology. |
| [`phishing`](tactics/phishing.md) | Phishing campaign execution methodology for authorized red team engagements. Covers end-to-end campaign lifecycle: infrastructure provisioning (GoPhish, SMTP relay configuration, domain acquisition and aging, SPF/DKIM/DMARC alignment), payload delivery vect... |
| [`social-engineering`](tactics/social-engineering.md) | Social engineering attack techniques beyond email phishing for authorized red team and physical penetration testing engagements. Covers pretexting methodology (persona creation, authority and urgency psychological triggers, rapport building), vishing (voice... |


## AI security

| Tactic | Purpose |
| --- | --- |
| [`ai-security`](tactics/ai-security.md) | AI/LLM security offensive checklist: prompt injection, jailbreaking, model extraction, training data poisoning, adversarial inputs, LLM-assisted attack automation, and AI system reconnaissance. Use when assessing AI/ML systems, red-teaming LLMs, or research... |


## Reporting

| Tactic | Purpose |
| --- | --- |
| [`reporting`](tactics/reporting.md) | Penetration test and red team report writing methodology. Covers executive summary structuring (risk-led narrative for non-technical readers), technical finding format (title, severity, affected scope, narrative, reproduction steps, impact, remediation, ref... |

