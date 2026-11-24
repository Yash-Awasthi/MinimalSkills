# frontend guide

The long-form group prose and the full roster. `SKILL.md` is the loadable hub, and
`references/skills/<skill>.md` is the verbatim body to follow for one task.

### Architecture and state

| Skill | What it does |
| --- | --- |
| [`architecture`](references/skills/architecture.md) | A portable React and React Native module structure with feature barrels, page directories, a strict server and UI state split, and promotion rules. |
| [`dev-guidelines`](references/skills/dev-guidelines.md) | React and TypeScript standards with Suspense as the default, lazy loading, feature organization, strict types, and required import aliases. |
| [`developer`](references/skills/developer.md) | Builds React 19 and Next.js 15 components, responsive layouts, client state, data fetching, and accessible interaction flows. |
| [`ui-engineering`](references/skills/ui-engineering.md) | Builds production-quality interfaces with component architecture, design system adherence, WCAG 2.1 AA, responsive layout, and real empty and error states. |

### Data and network

| Skill | What it does |
| --- | --- |
| [`api-integration-patterns`](references/skills/api-integration-patterns.md) | Covers race-safe fetching, AbortController cancellation, bounded retry, debounce, deduplication, and loading, error, and success states. |
| [`data-contracts`](references/skills/data-contracts.md) | Defines one typed fetch boundary with runtime parsing, one response envelope, branded ids, and one normalized error type before data enters the app. |
| [`observability`](references/skills/observability.md) | Defines a typed field event taxonomy, best-effort provider fan-out, consent gating, Core Web Vitals, and boundary error reporting. |
| [`optimistic-mutations`](references/skills/optimistic-mutations.md) | Codifies the optimistic write path: cancel, snapshot, patch, roll back verbatim, invalidate, and retry only when an idempotency key makes it safe. |

### Performance and SEO

| Skill | What it does |
| --- | --- |
| [`lighthouse`](references/skills/lighthouse.md) | Adds a portable Lighthouse CI gate on the production build with Core Web Vitals budgets, category floors, median runs, and artifacts. |
| [`seo`](references/skills/seo.md) | A portable SEO system for React and React Native web with metadata, rendering limits, and a detailed builder procedure. |

### Design and UI

| Skill | What it does |
| --- | --- |
| [`design`](references/skills/design.md) | Designs a distinctive interface inside the existing brand, accessibility, performance, and framework constraints, with an advisory DFII score. |
| [`ui-dark-ts`](references/skills/ui-dark-ts.md) | A dark React UI system with Tailwind CSS and Framer Motion for dashboards, admin panels, and data-rich applications. |

### Security

| Skill | What it does |
| --- | --- |
| [`mobile-security-xss-scan`](references/skills/mobile-security-xss-scan.md) | Inspects frontend code for XSS injection points, unsafe DOM manipulation, and missing sanitization across React, Vue, Angular, and vanilla JavaScript. |
| [`security-coder`](references/skills/security-coder.md) | Secure frontend coding for XSS prevention, output sanitization, CSP, input handling, clickjacking, sessions, and third-party scripts. |

### Component scaffolding

| Skill | What it does |
| --- | --- |
| [`mobile-development-component-scaffold`](references/skills/mobile-development-component-scaffold.md) | Scaffolds a React or React Native component with TypeScript types, accessibility, tests, styles, Storybook, and documentation. |

### Slides

| Skill | What it does |
| --- | --- |
| [`slides`](references/skills/slides.md) | Builds animation-rich HTML presentations or converts PowerPoint, with viewport-fitted slides and a five-phase discovery and delivery flow. |
| [`slides-frontend-slides`](references/skills/slides-frontend-slides.md) | The fixed 1920 by 1080 stage variant of the slides workflow, with bundled PDF export, extraction, and confined server helpers. |
## Group notes

### Architecture and state

`architecture` defines the portable module structure. Feature modules, a barrel as the
contract, page directories with a short README, co-located styles, naming rules, and
adapters for Next.js App Router, Vite, Remix, and Expo. Two kinds of state, two homes.
The split is mandatory and the libraries are your choice. A component starts in the
narrowest scope and is promoted only when a second consumer appears.

`dev-guidelines` is the React and TypeScript standard. Suspense is the default, heavy
code is lazy loaded, features are organized by folder, TypeScript is strict, and import
aliases are required. The FFCI feasibility score is an advisory heuristic. The named
components `SuspenseLoader`, `LoadingOverlay`, `useMuiSnackbar`, `useAuth`, and
`apiClient` are project examples rather than bundled implementations, so provide or
adapt them first.

`developer` is the broad React 19 and Next.js 15 role skill. Components, responsive
layouts, client state, data fetching, styling, performance, testing, accessibility, and
tooling. Its capability list is a map, not a claim that every tool is installed.

`ui-engineering` targets production quality rather than an AI look. Component
architecture, file structure, state, design system adherence, spacing, typography,
color, WCAG 2.1 AA, keyboard navigation, ARIA, focus management, empty and error states,
responsive layout, and loading transitions. It names an accessibility checklist from the
addyosmani upstream that is not bundled.

### Data and network

`api-integration-patterns` covers the async failure modes. An API layer, race-safe state,
AbortController cancellation, bounded retry with exponential backoff, debounce, request
deduplication, and loading, error, and success states. The default is one attempt.
Retry only explicitly replay-safe operations and classified transient failures, honor
`Retry-After`, and keep a total deadline. Never expose a privileged key in frontend code.

`data-contracts` puts type safety at the network edge. One client as the only fetch
boundary, parse don't validate, one response envelope, branded identifiers, and one
normalized error with a code. Side effects live outside the parser. Per-field errors map
to form fields. Never throw a bare string, and never render a server message directly.

`optimistic-mutations` is the write path. Be optimistic only when the UI can recover.
Cancel in-flight queries, snapshot every affected cache, patch instantly, roll back
verbatim on error, then invalidate. For a create with server-owned fields, wait for the
server. Cache coherence keeps detail and lists in lock step. Retry only with an
idempotency key, and never auto-retry a non-idempotent write.

`observability` is the field side. A typed event taxonomy, best-effort fan-out with
bounded adapter work, a provider and SSR-safe hook, real-user Core Web Vitals, consent
gating, and boundary error reporting. Lighthouse is the lab gate and this is the field
signal. A consent boolean does not stop SDK auto-collection, so configure collection
disabled before startup and clear queued sends. Verify Firebase event name and parameter
restrictions for the pinned SDK.

### Performance and SEO

`lighthouse` adds the CI gate. `lighthouserc.cjs`, budget severity, the npm script, the
GitHub Actions workflow, framework adapters, and flaky-run debugging. Gate the production
build, take the median of several runs, keep `onlyCategories` to what you gate, and
upload the HTML and JSON reports. A workflow does not block until it is a required check
in branch protection. INP is a field metric with no direct lab audit, so do not configure
a nonexistent audit.

`seo` is the portable builder-based SEO system. The body defers to
`references/detailed-guide.md`, which is bundled, and that guide holds the complete
procedure and references. Rendering and metadata limits are real. A client-rendered page
cannot promise what a crawler will see, so verify with the built output.

### Design and UI

`design` is the designer-engineer mandate. Work inside the product's brand,
accessibility, performance, and framework constraints. The Design Feasibility and Impact
Index scores five dimensions on a 1 to 5 scale for an arithmetic range of -1 to +19, and
it is an advisory heuristic, not a certification or a release gate. Choose one dominant
tone and blend no more than two. Framer Motion only when justified.

`ui-dark-ts` is the dark dashboard system with Tailwind CSS and Framer Motion. Glass
effects, tasteful animation, and data-rich layouts. The detailed guide is bundled and
carries the full procedure, so read it before executing. Verify contrast and focus
states rather than trusting the dark palette.

### Security

`mobile-security-xss-scan` inspects React, Vue, Angular, and vanilla JavaScript for
injection points, unsafe DOM writes, and missing sanitization. The scanner classes are
illustrative pseudocode and `xss-scanner.js` is not bundled, so string matches are
review candidates, not confirmed findings. Confirm the data path and the framework's
escaping before reporting. Never put user input in `innerHTML`.

`security-coder` is the secure coding standard. Output handling, CSP, input validation,
CSS handling, clickjacking, redirects, session management, browser features, third-party
integration, PWA, and mobile. Prefer `textContent` over `innerHTML`. The implementation
playbook is bundled. This is the coding side, not a replacement for an independent
security audit.

### Component scaffolding

`mobile-development-component-scaffold` generates a React or React Native component with
TypeScript props, accessibility, tests, styles, Storybook stories, and documentation. It
handles required and optional props explicitly and produces mocks for the tests. Map the
generated output to the project's own test runner and styling system, and review the
generated types rather than accepting the template.

### Slides

`slides` builds animation-rich HTML presentations from scratch or from a PowerPoint. It
detects the mode, discovers content, evaluates images, offers style previews, generates
the deck, converts PPT, then delivers. Every slide fits within 100vh with no internal
scroll, and overflow splits into another slide. Breakpoints are required at 700, 600, and
500 pixels of height. Never negate a CSS function directly.

`slides-frontend-slides` is the fixed-stage variant. Every deck uses a 1920 by 1080
canvas scaled as a whole, and it stays 16:9 on phones rather than reflowing. Slide
visibility uses `.active` and `.visible` with `visibility`, `opacity`, and
`pointer-events`, not `display`. It bundles the upstream license and notice, a PDF
export script, the PPTX extractor, and a loopback-only confined server. Playwright and
Chromium must already be installed, and remote style files are untrusted reference data.

The two slide skills have incompatible layout rules. Pick the one that matches the
deliverable and follow only its body. Never mix the viewport rule with the fixed stage.
