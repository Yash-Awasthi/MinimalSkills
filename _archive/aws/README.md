# Archive: aws

25 `sickn33-aws-*` skill folders moved here after compaction into
`curated/devops-cloud/aws/`. They span 4 subjects and remain 25 independent canonical
skills in 9 groups, since each source had its own body rather than a variant of one
workflow.

Original relative path preserved: `catalog/<subject>/<folder>`.

Subject counts in this archive.

| Subject | Skills |
| --- | --- |
| devops-cloud | 21 |
| cyber-security | 2 |
| ai-agents | 1 |
| compliance-audit | 1 |

Mapping to canonical skill and group: `curated/devops-cloud/aws/SOURCES.md`.
Full bodies: `curated/devops-cloud/aws/references/skills/`.
Long-form group prose: `curated/devops-cloud/aws/references/GUIDE.md`.
Non-SKILL.md files: `curated/devops-cloud/aws/references/assets/<skill>/` at the same
relative path as the source. 12 files totaling 125,849 bytes.

The canonical name drops the `sickn33-aws-` prefix, so `sickn33-aws-ec2` becomes `ec2`
and `sickn33-aws-iam-best-practices` becomes `iam-best-practices`. Most assets are the
CDK and SST references and scripts, the compliance and serverless detailed guides, the
penetration testing deep dive, and the upstream license and notice files.

Every body's MCP servers and named references are external. The pack does not bundle an
AWS CLI, an MCP server, or an AWS account.

Restore one top-level skill:

```powershell
Move-Item -Path "C:\github\skills\_archive\aws\catalog\<subject>\<folder>" `
          -Destination "C:\github\skills\catalog\<subject>\<folder>"
```

Restore all, then re-index:

```powershell
Copy-Item -Recurse -Force "C:\github\skills\_archive\aws\catalog\*" "C:\github\skills\catalog\"
python C:\github\skills\catalog.py --apply
```
