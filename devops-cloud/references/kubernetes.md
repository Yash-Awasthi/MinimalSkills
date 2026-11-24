# kubernetes

Load for container images and cluster workloads.

## image

```dockerfile
FROM node:22-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:22-alpine
USER node
COPY --from=build /app/dist ./dist
CMD ["node", "dist/main.js"]
```

- Multi-stage. No build tools in the runtime image.
- Non-root user. Read-only root filesystem where possible.
- Pin by digest in production: `image: app@sha256:...`.
- One process per container. Logs to stdout, not a file.

## workload

```yaml
resources:
  requests: { cpu: 100m, memory: 128Mi }
  limits:   { memory: 256Mi }
readinessProbe:
  httpGet: { path: /healthz, port: 8080 }
livenessProbe:
  httpGet: { path: /livez, port: 8080 }
  initialDelaySeconds: 10
```

- Requests drive scheduling, limits drive throttling and OOM. Set both.
- Readiness gates traffic. Liveness restarts. Never point liveness at a dependency.
- `PodDisruptionBudget` for anything with a replica count above one.
- `topologySpreadConstraints` across zones for real availability.

## rollout

```bash
kubectl rollout status deploy/app -n prod
kubectl rollout undo deploy/app -n prod
kubectl diff -f k8s/
```

- `maxSurge: 1`, `maxUnavailable: 0` for zero-downtime.
- Migrations run as a job, before the rollout, and must tolerate the old version still running.

## debug

| symptom | first command |
| --- | --- |
| crash loop | `kubectl logs pod --previous` |
| pending | `kubectl describe pod` for the scheduler reason |
| oomkilled | `kubectl get pod -o jsonpath='{.status.containerStatuses[*].lastState}'` |
| no traffic | `kubectl get endpoints svc` |
| dns failure | `kubectl run -it --rm dbg --image=busybox -- nslookup svc` |

## hygiene

- Namespace per environment or per team, with resource quotas.
- Network policy default deny, then allow.
- Secrets from an external store, not base64 in git.
- No `:latest`. No `privileged: true`. No hostPath for app data.
## kubernetes tooling

| tool | the rule that matters |
| --- | --- |
| Podman | Rootless by default; `podman generate systemd` for a host service; a `:Z` volume label on SELinux or the mount is denied. |
| Hardening and scanning | `trivy image`, non-root `securityContext`, `readOnlyRootFilesystem`, no `:latest`, no cluster-admin binding. |
| Helm | `helm upgrade --install --atomic --timeout 5m`; `--reuse-values` silently drops new chart defaults, pass a values file instead. |
| Kustomize | Overlays per environment, a base never patched in place; `kubectl kustomize` prints the rendered manifest for review. |
| ArgoCD GitOps | Sync policy `automated` with `selfHeal`; a manual `kubectl edit` is reverted on the next sync, which is the point. |
| mirrord | Runs a local process against the cluster: `mirrord exec --target deployment/api -- npm run dev`; file and network are remote, so a local write is not persisted. |
