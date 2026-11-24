# react-next

Load for component structure, routing and rendering mode.

## structure

```
app/
  (marketing)/page.tsx
  dashboard/
    layout.tsx
    page.tsx
    loading.tsx
    error.tsx
  api/health/route.ts
src/
  features/invoices/{components,hooks,api,schema.ts}
  components/ui/        # shared primitives
  lib/                  # adapters, no JSX
```

- Feature folders own their components, hooks and types.
- A barrel file is the public contract. Deep imports across features are a defect.
- Shared primitives live in one place. A second copy of a button is a review finding.

## server and client

| need | placement |
| --- | --- |
| data fetch, secrets, db | server component or route handler |
| hooks, events, browser api | client component |
| shared layout | server, with client leaves |
| context provider | client, mounted low |

`use client` at the leaf, not at the page. A client page ships the whole tree.

## data

```tsx
// server component
const invoices = await db.invoice.findMany({ where: { userId } });

// client mutation
const [pending, start] = useTransition();
```

- Server components cannot use hooks. Client components cannot read the database.
- Serialize only what the client renders. A full row with secrets is a leak.
- `cache()` for request-scoped dedupe.

## rendering modes

| mode | when | cost |
| --- | --- | --- |
| static | content same for everyone | build time |
| ISR | content changes on a schedule | revalidate window |
| dynamic | per-user, per-request | latency, no cdn |
| client | heavy interactivity after load | empty first paint |

Choose per route, not per app.

## hydration

| warning | cause | fix |
| --- | --- | --- |
| text mismatch | `Date.now()`, `Math.random()`, locale | render on client or pass a stable value |
| invalid nesting | `div` inside `p` | fix the element |
| style mismatch | media query in the first render | `useEffect` or CSS |
| id mismatch | `useId` missing | use `useId` |

## forms

- Server action or route handler. One path, not both.
- Validate on the server. Client validation is a convenience.
- Return field errors keyed by name, render next to the field.
- Disable submit while pending, keep the input values on error.

## accessibility floor

- One `h1` per page, headings in order.
- Every input has a label, not a placeholder.
- Focus visible. Escape closes overlays. Tab order follows reading order.
- `aria-live` for async status, `aria-busy` while pending.

## review

```bash
pnpm build
pnpm lint
npx tsc --noEmit
```
## framework index

| stack | the rule that matters |
| --- | --- |
| Angular | Signals or `OnPush`; `takeUntilDestroyed` on every subscription; `trackBy` on `*ngFor` or the list re-renders whole. |
| SvelteKit | `+page.server.ts` for load, `+page.ts` for universal; a store written during SSR leaks between requests. |
| Vue | `ref` for primitives, `reactive` for objects; `v-html` is an XSS sink; `watchEffect` re-runs on any read, prefer `watch`. |
| Markstream | Streams markdown into the DOM incrementally; a partial code fence must not render as HTML mid-stream. |
| Haskell/Scala | Frontend compiles to JS (GHCJS, Scala.js); bundle size is the first constraint, not the type system. |
| API integration patterns | One client module per API, typed responses, retry only idempotent calls, abort on unmount. |
| Observability | Web vitals to a real endpoint, errors with a release id, a session id in every report; console-only logging is not observability. |
| Animation craft | Animate transform and opacity; 150-250ms for UI, 300-400ms for a sheet; honor `prefers-reduced-motion`. |
| Three.js suite | One renderer per canvas, dispose geometries and textures on unmount, `renderer.setPixelRatio(Math.min(devicePixelRatio, 2))`. |
| 2.0 DSL | Makepad 2.0 uses runtime `script_mod!` and Splash; never mix a `live_design!` example into a `script_mod` project. |
| Live design generation | Generate the component from tokens, then diff against the design; a generated file that is hand-edited drifts on the next run. |
| XSS scanning | Crawl with a payload set, check reflection and storage; a CSP report-only header is a scan, not a fix. |
| PWAs | Service worker caches the shell, never the API by default; a stale cache needs a versioned cache name and `skipWaiting`. |
| Slides | Reveal or Slidev: one idea per slide, 24pt floor, a deck that needs a script is a document. |
| WordPress | Theme over plugin for layout, escape on output, `wp_enqueue_script` with a version for cache busting. |
| Analytics and SEO tools | One analytics tag, consent-gated; `robots.txt` plus a sitemap; a canonical tag on every variant. |
