---
name: frontend-ui
description: Use when building or fixing web UI: React and Next.js layout, state and fetching, forms with Zod, typed procedures with tRPC, Core Web Vitals, SEO, 3D and canvas, Avalonia and Makepad shells. Triggers: React, Next.js, hydration, CLS, bundle, Zod, tRPC.
---

# frontend-ui

## use when

- component structure, routing, React or Next.js -> references/react-next.md
- fetching, cache, forms, optimistic updates -> references/state-data.md
- bundle size, LCP, CLS, SEO, metadata -> references/perf-seo.md
- tokens, theming, layout mechanics -> references/design-tokens.md
- static, SPA, SSR, desktop shell -> references/platforms.md

not for: visual direction and design tokens (design-ux), server endpoints (backend-api)

## rules

- Conflict order: state correctness, then accessibility, then bundle size; a fast page with stale data is a defect.
- Server state and client state are separate; one owner per piece of state, never a cache mirrored into a store.
- `use client` at the leaf that needs it: a client page ships the whole tree and loses streaming.
- Never render `error.message` or raw server text: resolve an i18n key and log the code; user input goes through `textContent` or an allowlist sanitizer, never `innerHTML`.
- No layout shift: explicit `width` and `height` on every image, reserved space for async blocks.
- A privileged key never reaches the browser. A `NEXT_PUBLIC_` variable is public.
- Overflow gate: `scrollWidth - clientWidth` is 0 at 390px and 1024px on the built page, never on source, so every performance or SEO claim comes from the build.

## change

1. Locate: the component, its data source and the loading, empty and error branches it owns.
2. Propose the UI change in one sentence, with the alternative layout you rejected.
3. Predict before building: bundle delta, hydration path, LCP element, which state changes.
4. Back up the original component and its props in context, pinned to `git rev-parse HEAD`.
5. Apply one concern per edit; a state change and a style change are two edits.
6. Verify: `pnpm build`, then the built page at 390px and 1024px, console clean.
7. Regress: every route rendering the component and the e2e covering its states.
8. Compare the screenshots against the prediction; an unplanned shift stops the edit.
9. Report build result, bundle delta and what was not opened in a browser, then continue.

## build

1. Read the versions and the existing state library.

```bash
cat package.json
find app src -maxdepth 2 -name "*.tsx" | head -20
```

2. Match the folder shape that exists: route file under `app/<segment>/page.tsx`, shared parts in `components/`, pure logic in `lib/`. A second state library is a defect, not a preference.
3. Server component by default in Next.js 15 and React 19. `use client` only where hooks or events are needed.
4. Parse the boundary: `Schema.safeParse(json)`, never `as T`. The parsed type is the only shape downstream.
5. Cover loading, empty, error and success. A view with three states is incomplete.
6. Build and open the built page, not the dev server.

## component

```tsx
// app/invoices/page.tsx  (server, no "use client")
export default async function Page() {
  const invoices = await listInvoices();          // direct db or fetch, runs on the server
  return <InvoiceTable rows={invoices} />;        // client island only where it needs interactivity
}
```

- A client boundary is a prop serialization boundary: pass plain data, never functions or class instances.
- A `"use client"` file imports the whole subtree into the bundle. Put it around the button, not the page.
- Keys are stable ids, never the array index. Index keys reorder state on sort.
- A list over 100 rows virtualizes; below that, render plainly and measure before optimizing.

## form

```tsx
const Form = z.object({ email: z.string().email(), amount: z.coerce.number().int().positive() });

const { register, handleSubmit, formState } = useForm<z.infer<typeof Form>>({
  resolver: zodResolver(Form),
});
```

- One schema for the client and the server. A second hand-written validator drifts.
- Validate on submit, re-validate on change after the first submit. Never validate on every keystroke.
- Show the error next to the field, keyed by `errors.email.message`, and focus the first invalid field.
- Disable the submit button during the request and keep the values; a cleared form after a network error loses work.
- `z.coerce.number()` for inputs: a form value is always a string until parsed.

## errors

- A route-level `error.tsx` catches render errors; it does not catch async event handlers.
- An event handler error needs a try/catch and a toast; an unhandled rejection disappears.
- Retry the query, not the page. A full reload loses form state.
- A 401 sends to login with `?next=<path>`; a 403 renders a permission message, never a login redirect loop.

## data

- Query key is cache identity: `['invoice', id]`, every parameter that changes the result.
- `staleTime` 30s for stable reads, `gcTime` for retention. No refetch on every mount.
- Optimistic update: cancel queries, snapshot, patch, roll back verbatim on error, then invalidate.
- Cancel on unmount with `AbortSignal`. A response after unmount is a state write to nothing.
- Non-idempotent write: never auto-retry. Idempotency key or nothing.

## decide

| condition | action |
| --- | --- |
| data from a server | server component or query cache |
| interaction-local state | `useState` in the nearest parent |
| shared across routes | URL state, then a store |
| list over 100 rows | virtualize with a stable key |
| image above the fold | `priority`, dimensions set, preloaded |
| client bundle grows over 30kb | justify or split |
| three-state view | add the missing state before shipping |
| deck or fixed canvas | 1920x1080 stage scaled as a whole, never mixed with viewport units |

## budgets

| metric | target |
| --- | --- |
| LCP on 4G | under 2.5s |
| CLS | under 0.1 |
| INP | under 200ms |
| first-load js | under 200kb gzip |
| images | explicit width and height |
| font | two families, four weights |

## check

- [ ] `pnpm build` passes, no hydration warning in the console
- [ ] overflow 0 at 390px and 1024px
- [ ] LCP image preloaded, CLS under 0.1
- [ ] keyboard path works: tab order, focus visible, escape closes
- [ ] no secret in the client bundle: `rg "sk-|api_key" .next/static`
- [ ] loading, empty, error states rendered

## stop

| condition | action |
| --- | --- |
| design tokens missing | ask for the token set or reuse existing |
| API contract unclear | ask for the schema |
| a11y conflict with the design | surface the conflict, do not drop the label |

## emit

- components added or changed
- build result and bundle delta
- what was not tested in a browser
