# platforms

Load when choosing a delivery mode or targeting a non-browser surface.

## choose

| target | stack | trade |
| --- | --- | --- |
| content site, SEO matters | static or ISR | no per-user personalization at the edge |
| dashboard, auth | SSR plus client islands | server cost, session handling |
| internal tool | SPA | empty first paint, simpler deploy |
| desktop shell | Electron, Tauri | size, update channel, native apis |
| mobile shell | Expo, Capacitor | store review, native modules |

## static and SPA

- SPA fallback rewrites every path to `index.html`, except assets.
- Cache `index.html` briefly, hashed assets forever.
- Base path: set `base` in the bundler, not by string replace.

## ssr

- Sessions in http-only cookies, not localStorage.
- Stream the shell, hydrate below the fold.
- Set cache headers per route: `private, no-store` for personalized.

## edge

- No node built-ins unless the runtime provides them.
- Bundle size limit per function is real; check the build output.
- Cold start dominates a route called twice an hour: keep the bundle small, or keep one instance warm.

## desktop shells

- Avalonia for a XAML desktop shell over a shared .NET core: MVVM, one view model per view, no logic in code-behind.
- Makepad for a Rust UI shell: a single render loop, shader-based widgets, no webview. Choose it when the binary must stay small and native.
- Both need a real window chrome and a native file dialog. A webview app is a different trade.

## desktop

| concern | rule |
| --- | --- |
| updates | signed, staged, rollback path |
| filesystem | scoped to user-chosen paths |
| permissions | request at use, not at install |
| secrets | os keychain, never the app bundle |

## mobile shell

- Safe areas: `env(safe-area-inset-*)`.
- Touch targets and scroll physics differ from desktop.
- Test on a device, not only a resized window.

## headers

```
content-security-policy: default-src 'self'; img-src 'self' data:; frame-ancestors 'none'
strict-transport-security: max-age=31536000; includeSubDomains
x-content-type-options: nosniff
referrer-policy: strict-origin-when-cross-origin
```

CSP with `unsafe-inline` is a placeholder. Move to nonces or hashes.

## deploy check

```bash
curl -sI https://example.com | grep -iE "content-type|cache-control|csp"
```

- Html returns `text/html`, js returns `application/javascript`.
- A 200 on `/` does not prove the app rendered.
