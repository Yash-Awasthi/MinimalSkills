# perf-seo

Load for Core Web Vitals, bundle size and crawlable output.

## vitals

| metric | good | fix |
| --- | --- | --- |
| LCP | under 2.5s | preload the hero image, cut render-blocking css |
| INP | under 200ms | split long tasks, defer hydration |
| CLS | under 0.1 | reserve space, `font-display`, fixed dimensions |

Measure the built site, on a throttled profile, on the URL that matters. Lighthouse lab numbers are a gate, field data is the truth.

## images

```html
<img src="/hero.avif" width="1200" height="630" fetchpriority="high" alt="" />
```

- Modern format, explicit dimensions, `srcset` per breakpoint.
- Below the fold: `loading="lazy"`.
- Above the fold: never lazy, preload the LCP candidate.
- A css background hero cannot be preloaded as an image. Use `<img>`.

## fonts

- Self-host woff2, subset to the used ranges.
- `preload` the weights used above the fold.
- `font-display: swap` causes a reflow. For a wordmark, use a size-adjusted fallback or a pending gate with a 2.5s reveal.
- Two families maximum, four weights maximum.

## bundle

```bash
pnpm build
npx source-map-explorer '.next/static/chunks/*.js'
```

- Route-level split by default. Dynamic import for modals, editors, charts.
- A date library is 20kb. Check before adding.
- Tree-shake: named imports, no barrel re-export of a whole library.
- Budget: first-load js under 200kb gzip for a content page.

## seo

| item | rule |
| --- | --- |
| title | unique per page, under 60 chars |
| description | unique, 120-160 chars |
| canonical | absolute, one per page |
| robots | noindex on staging and on filtered duplicates |
| sitemap | generated from routes, includes lastmod |
| headings | one h1, ordered h2 |
| structured data | json-ld matching visible content |
| social | og:title, og:image with absolute url |

A client-rendered page cannot promise what a crawler sees. Check the built html.

```bash
curl -s https://example.com/pricing | grep -E "<title>|<h1|canonical"
```

## gates

- Lighthouse CI on the production build, median of 3 runs.
- Budgets as errors, not warnings.
- A required check in branch protection, or the gate does not block.
