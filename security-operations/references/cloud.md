# cloud

Load for authorized cloud, container and cluster posture work.

## identity first

| check | command |
| --- | --- |
| who am i | `aws sts get-caller-identity` |
| key age | `aws iam list-access-keys` |
| unused roles | `aws iam get-credential-report` |
| role trust | `aws iam get-role --role-name X` |
| root usage | `aws cloudtrail lookup-events --lookup-attributes AttributeKey=Username,AttributeValue=root` |

Long-lived keys are the finding. Prefer OIDC federation, instance roles and short sessions.

## storage

```bash
aws s3api get-bucket-acl --bucket b
aws s3api get-bucket-policy --bucket b
aws s3api get-public-access-block --bucket b
```

- Public read on a bucket with objects is a finding. An empty public bucket is informational.
- Check versioning and object lock for destructive-action resistance.
- Enumerate snapshots and AMIs: a public snapshot leaks the disk.

## network

- Security group open to `0.0.0.0/0` on a non-public port.
- Public load balancer to a private subnet with no auth.
- Metadata service reachable from a workload that fetches user URLs.
- Egress allowlist absent: exfiltration path.

## containers

```bash
trivy image --severity HIGH,CRITICAL app:latest
docker run --rm -v /var/run/docker.sock:/sock app  # privileged mount test
kubectl get pods -A -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.spec.securityContext}{"\n"}{end}'
```

| issue | signal |
| --- | --- |
| privileged pod | `securityContext.privileged: true` |
| host path mount | `hostPath` volume |
| root user | `runAsUser: 0` or absent |
| no limits | no `resources.limits` |
| cluster admin binding | rolebinding to `cluster-admin` |

## kubernetes posture

- Network policies present per namespace.
- Service account tokens not automounted where unused.
- Secrets in etcd encrypted at rest, or in an external store.
- Admission control: no `:latest`, no privileged, signed images.

## audit

- CloudTrail or equivalent enabled in every region, log integrity validation on.
- GuardDuty or equivalent with findings routed to a human.
- Baseline the account for 7 days before calling a resource anomalous.

## scope

Testing a cloud account requires authorization for that account id, not just the company name. A shared or partner account is out of scope until named.
