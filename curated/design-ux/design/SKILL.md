---
name: design
description: >-
  12 design skills. Covers a router to 48 opinionated UI styles, a named visual philosophy,
  direction and cross-domain lens, a theme and token register, token contrast checking, a
  mechanical design system, spatial composition, a usability audit, a high-agency frontend
  rule set, scoped micro-interactions, a design orchestration gate, and Stitch DESIGN.md
  synthesis. Use when a task builds, reviews, documents, styles, or orchestrates frontend
  design, or when the user names a design skill.
metadata:
  curated_from: 12
  skills: 12
  groups: 6
---

# design

12 skills. 6 groups. One hub. Every source body is preserved verbatim in
`references/skills/<skill>.md`, and every non-SKILL.md file from a source pack sits at
the same relative path under `references/assets/<skill>/`. The `it` pack also carries the
48 style bodies inside its source tree. Load one body for the task.

`SOURCES.md` maps every source path to its canonical skill and group.
`references/INDEX.md` groups the links, `references/skills.tsv` carries every
description, and `references/GUIDE.md` holds the long-form group prose.

## Pack contract

**Direction and mechanics are separate layers.** `thinking` and `philosophy` set purpose,
tone, domain, color world, and signature. `system` holds the token, type, loading, and
motion invariants. `spatial` owns composition and the render loop. A style body supplies
one aesthetic, not a mechanical guarantee. Keep the layers distinct, and do not treat a
style name as permission to skip the mechanical rules.

**A model cannot trust its own UI.** Render the live artifact and judge the image, not the
token stream. Never self-grade. Use a separate judge that did not build the page, and ask
it to hunt for collisions, edge tangents, ragged alignment, lopsided weight, and narrow
width breaks. Fix, re-render, and re-judge. A described change list is not an audit.

**The overflow gate is mandatory.** Do not call any web UI done, working, fixed, or good
until `document.documentElement.scrollWidth - clientWidth` equals 0 at a narrow width in
the same turn. Test the dev width, 1024px and about 390px. A wide dev window hides the
bug. Any new element in a horizontal row re-arms the gate. Use `flex-wrap` on header and
nav rows, `min-width:0` on flex and grid children, `100%` instead of `100vw`, and anchor
edge labels inward. `overflow-x:clip` is a backstop, not a fix.

**Metrics are pointers, not verdicts.** The layout audit returns gates and signals. Gates
cover overflow, contrast, and tap targets, and a failure is a real defect. Collision is a
near-gate and needs eye confirmation. Balance, alignment, and spacing are signals about a
symmetric, gridded convention, which is the generic mean. Optimizing those signals makes
the layout blander. Look at the annotated screenshot before acting on any flag.

**Font loading must not pop.** `font-display:swap` paints a fallback face and then reflows.
Do not use it for a title, wordmark, or hero copy the user watches load. Self-host WOFF2,
preload the above-the-fold weights, reserve space, and use `size-adjust` on the fallback.
For decorative display text only, a `fonts-pending` gate can hold text at opacity 0 until
`document.fonts.ready`, with a 2.5s safety reveal. Never hide essential text indefinitely.
The first viewport paints complete, and the rest loads later.

**Tokens are values, not screens.** Map every color to a small primitive set: foreground,
background, border, brand, and semantic. Use CSS variables or theme objects, never a
hardcoded hex for UI. Nested radii are concentric, with the child radius no larger than the
parent and `child = max(0, parent - gap)`. Keep one accent, and make hover, active, and
focus states read as more prominent, not less.

**Contrast is a measured gate.** WCAG 2.2 AA applies 4.5:1 for normal text, 3:1 for large
text, and 3:1 for UI components. APCA is useful for perceptual decisions, but WCAG remains
the compliance floor, and a contrast-only audit does not certify accessibility. Measure the
token pairs in light and dark themes, check images, gradients, opacity, and hardcoded
colors the checker cannot see, and re-measure the exact serialized color after a fix.
Never change a brand color without asking, and never report a theme as passing without
checking dark mode.

**Style selection is semantic, not exact.** Map the request to one of the 48 style bodies
and read that body before coding. Do not blend styles unless the user asks. Use the user's
colors when supplied. The ten palettes and the 60-30-10 split are illustrative starting
points, not award provenance, and every actual foreground and background pair is checked.
A style is an aesthetic, not a mechanical license.

**Direction precedes code.** Define purpose, tone, domain, color world, signature, and the
review bar before building. Commit to one bold direction and reserve high-impact devices
for one or two punctuation moments. The style must belong to the product's world, not to
the model's first average. A subtle reference can reward those who know it without
excluding everyone else.

**Orchestration has gates.** Brainstorming artifacts, a risk classification, a required
review, and an execution readiness check come before implementation. Do not skip a required
substantive review, do not silently escalate or de-escalate, and do not merge design and
implementation. A multi-agent review needs explicit delegation authorization. The meta
skill exits only with an explicit next step and all prior steps complete.

**Tokens are documented and auditable.** A theme is a set of values, not screens. Use one
row per token with light and dark values, contrast ratio, WCAG level, and status. Unknown
values stay `Unknown` and are not zero. Do not invent a hex code, font, license, or ratio,
and do not mark a record `Done` when a required check fails. Build the artifact only when
asked, and route a Notion output through the named import skill. Never ask for a Notion
password or token.

**Micro-interactions are scoped.** Add a spell only when it serves the requested experience.
Respect existing design, accessibility, and performance constraints; ordinary clear behavior
is valid. Keep core actions usable without animation, hover, or an easter egg, support
keyboard and touch, respect reduced motion, and avoid layout shift. A broken spell is worse
than none, and frame-rate claims need profiling.

**High-agency frontend rules are mandatory when they apply.** Check `package.json` before
importing any third party library, and never assume it exists. Lock the Tailwind version
and use the matching syntax and PostCSS path. Ban emojis in code, markup, text, and alt
text. Do not use `h-screen` for a hero; use `100svh` or `100dvh` and test chrome changes.
Use CSS Grid instead of flex percentage math, and use the installed Radix or Phosphor icon
API. Keep one palette, avoid the purple-blue AI look, pure black, neon glows, and generic
cards, and fall back to a single column below 768px for asymmetric layouts. Never mix GSAP
or ThreeJS with Framer Motion in one component tree. Treat infinite loops as demos, not
status.

**DESIGN.md is a source of truth, not a substitute for the project.** Read a Stitch screen
through the MCP tools, capture the screenshot and HTML, and extract exact hex codes,
typography, geometry, depth, and layout. Use descriptive names plus exact values, and
explain the role of each element. The Stitch MCP server, a designed screen, and the
prompting guide are prerequisites, not bundled assets. Do not invent project metadata.

**A missing support file fails closed.** `theme-guide` says its shared execution runtime is
not bundled. `system` names external design siblings and layout-audit helpers as not
bundled in its tree, although the `spatial` skill carries `scripts/layout-audit.js` in this
pack. `token-contrast` ships its checker as source in `references/contraste-checker.md`,
not as a committed script, and expects Node 18+. Resolve a missing path from the declared
upstream or skip the dependent step. Never fabricate it.

**Write clean as you draft.** Short declarative sentences. No em dash. A colon may
introduce a list and may not connect two clauses. Sentence case headings. No chatbot
framing, no generic closer.

## Routing

| The user wants | Group |
| --- | --- |
| A specific UI style, a philosophy, or direction before coding | Direction and style |
| Tokens, a theme register, or contrast on color tokens | System mechanics |
| Layout composition, overflow, balance, or a usability audit | Spatial and usability |
| React or Next.js UI with anti-generic taste rules | High-agency frontend |
| A scoped micro-interaction or easter egg | Micro-interactions |
| A design workflow gate or a Stitch DESIGN.md | Orchestration and documentation |

## Full roster

### Direction and style

| Skill | What it does |
| --- | --- |
| [`it`](references/skills/it.md) | Routes a frontend request to one of 48 opinionated UI styles, with fuzzy matching, optional palettes, and the 60-30-10 rule. |
| [`philosophy`](references/skills/philosophy.md) | Builds a named visual movement for high-concept work, with a subtle reference and minimalist text. |
| [`thinking`](references/skills/thinking.md) | Sets purpose, tone, domain, color world, signature, review bar, and a cross-domain lens before coding. |

### System mechanics

| Skill | What it does |
| --- | --- |
| [`system`](references/skills/system.md) | Defines mechanical design invariants for tokens, typography, loading order, font stability, chrome, motion, radii, and color. |
| [`theme-guide`](references/skills/theme-guide.md) | Builds a design token register with light and dark values, contrast ratio, WCAG level, and CSV, SQL, JSON, or Notion output. |
| [`token-contrast`](references/skills/token-contrast.md) | Measures WCAG 2.2 contrast across color tokens and suggests the closest passing color while keeping hue. |

### Spatial and usability

| Skill | What it does |
| --- | --- |
| [`spatial`](references/skills/spatial.md) | Composes layout by rendering and judging the page, measuring overflow and balance, and separating gates from signals. |
| [`ux`](references/skills/ux.md) | Scores a rendered interactive UI against Nielsen's 10 heuristics plus interaction add-ons, then fixes and re-scores. |

### High-agency frontend

| Skill | What it does |
| --- | --- |
| [`taste-frontend`](references/skills/taste-frontend.md) | Builds high-agency React and Next.js UI with anti-generic rules for typography, color, layout, states, motion, and dependencies. |

### Micro-interactions

| Skill | What it does |
| --- | --- |
| [`spells`](references/skills/spells.md) | Adds scoped micro-interactions and easter eggs that increase delight without breaking usability or accessibility. |

### Orchestration and documentation

| Skill | What it does |
| --- | --- |
| [`md`](references/skills/md.md) | Analyzes a Stitch project through MCP and synthesizes a semantic DESIGN.md with atmosphere, palette roles, typography, components, and layout. |
| [`orchestration`](references/skills/orchestration.md) | Routes design work through mandatory brainstorming, risk classification, review, and an execution readiness gate. |

## Group notes

### Direction and style

`it` is the style router. It maps a website, app screen, or UI component request to one of
48 opinionated style bodies, using fuzzy matching rather than an exact keyword. The styles
span modern UI, depth and 3D, typography, retro and historical, modern trends, futuristic,
and data and product categories. The body lists ten illustrative palettes, the 60-30-10
background, accent, and CTA split, and a table of color tokens. Read the chosen style's
`SKILL.md` before coding, use the user's colors when supplied, verify contrast for every
real pair, and do not blend styles unless requested. The 48 style bodies are preserved at
the same relative paths under `references/assets/it/`, so the router's file instruction
still resolves.

`philosophy` creates a named movement for high-concept or art-like work. Name it in one or
two words, then articulate space and form, color and material, scale and rhythm,
composition and balance, and visual hierarchy in four to six paragraphs, each aspect once.
Stress painstaking craft, keep text sparse, and leave room for interpretive choices. Find
one subtle conceptual reference in the request and weave it into form, color, and
composition. The bundled `reference.md` carries examples.

`thinking` sets direction before coding. Define purpose, tone, constraints, and one
differentiating element. Pick an extreme and execute it with intention. Reserve full-bleed
media, dramatic motion, oversized type, a saturated accent, and parallax for one or two
punctuation moments, not the default. Name five or more concepts from the product's
domain, five or more colors that belong in that world, and one signature element. The
review bar asks whether you would put your name on the work. No font pop-in and first seen
first loaded are non-negotiable. The cross-domain lens draws two or three principles from
cinema, architecture, marketing, UX, automotive, or industrial design, chosen for the
product.

### System mechanics

`system` holds the mechanical invariants. Colors map to foreground, background, border,
brand, and semantic tokens, and code uses variables rather than raw hex. Typography pairs
a display face with a body face and controls size, weight, and letter spacing; monospace
with `tabular-nums` is for real data, not decorative microtext. Loading order follows the
first viewport: self-host WOFF2, preload the above-the-fold weights and the hero image,
use `fetchpriority="high"` and a poster, lazy-load below the fold, reserve space, and
inline critical CSS. Slow content gets a styled placeholder, not the browser's partial
paint. Chrome holds a constant height and transient status text stays on one line. Motion
is purposeful, with restrained defaults and reduced-motion support. Scrollytelling suits
editorial narration, not dashboards or forms. Nested radii stay concentric. Color is
derived from the domain, carries meaning, and keeps hover and focus states more prominent.
The bundled `references/motion-choreography.md` carries the transition rules and duration
table. External design siblings and layout-audit helpers are not bundled in this source
tree; the `spatial` skill supplies its own audit script in this pack.

`theme-guide` builds a documented token register. Identify the intent first, ask only for
the missing facts, and record unknown values as `Unknown` rather than zero. The register
uses one row per token with value, light and dark variants, contrast ratio, WCAG level,
status, and review date, so the CSV, SQL, JSON, and Notion forms share one field source.
The default output is a short recommendation, and the full artifact is built only when
requested. A Notion output is routed to the named import skill, and no Notion password or
token is requested. Never invent a hex code, font name, license, or measured ratio.

`token-contrast` measures the tokens rather than the screens. It runs the shipped checker
source at `references/contraste-checker.md` with Node 18+, reads `--color-*` variables in
hex, `rgb()`, `hsl()`, or `oklch()`, separates light and dark themes, and pairs text tokens
with background tokens. Every failing pair gets a same-hue suggestion with the nearest
passing lightness, and one value per token can pass all its backgrounds. The body names
WCAG 2.2 minimums of 4.5:1, 3:1 for large text, and 3:1 for UI components. Images,
gradients, opacity, and hardcoded colors need a visual check. The parser is a regular
expression heuristic, not a CSS validator, and transparent backgrounds are refused until
their composite is known. Re-measure the serialized color after a fix.

### Spatial and usability

`spatial` starts from two failures: a model cannot see its own UI, and its first idea is
the mean. Render the page and have a fresh judge critique the image. Do not prescribe a
fixed style, because a fixed rule becomes the next average. The overflow gate is explicit:
measure `scrollWidth - clientWidth` at narrow widths before calling the page done,
`flex-wrap` header rows, add `min-width:0`, use `100%`, anchor edge labels inward, and use
`overflow-x:clip` only as a backstop. Lay out in task order so the confirm action sits where
the work ends. Balance is measured as an ink-weighted centroid against optical center,
with an independent pixel oracle, not a VLM opinion. The audit script reports collision,
contrast, tap size, overflow, alignment, spacing, and balance, and overlays findings on the
screenshot. Gates are correctness and signals are convention; obeying a signal can make the
layout blander. The bundled `scripts/layout-audit.js` is the dependency-free audit pass.

`ux` audits interactive usability, not visual polish. Name the primary task, render the
default first-load state wide and narrow, trace the task step by step, and have a separate
judge score Nielsen's ten heuristics: system status, real-world match, user control,
consistency, error prevention, recognition over recall, flexibility, aesthetic minimalism,
error recovery, and help. Interaction add-ons cover self-evident affordances, Fitts transit,
gesture discoverability, visual-weight match, progressive disclosure, tooltip timing,
scroll-position restore, and idempotent submit. The output is a located finding per
heuristic with severity and a prioritized fix list, then a re-render and re-score. An
instruction wall is an affordance debt, not documentation.

### High-agency frontend

`taste-frontend` sets an active baseline of `DESIGN_VARIANCE` 8, `MOTION_INTENSITY` 6, and
`VISUAL_DENSITY` 4, then adapts to the user. It checks dependencies in `package.json`,
locks the Tailwind version, and isolates client interactivity. It bans emojis, `h-screen`,
flex percentage math, and the purple-blue AI look. It uses one accent, one palette, CSS
Grid, Radix or Phosphor icons, and a single column below 768px for asymmetric layouts. It
requires loading, empty, error, and tactile states. It bans pure black, neon glows, gradient
text, custom cursors, Inter, generic cards, generic names, fake numbers, and startup slop.
Inside the creative arsenal it names Liquid Glass, magnetic micro-physics, spring physics,
layout transitions, and staggered reveals. It warns never to mix GSAP or ThreeJS with
Framer Motion in one tree, and to treat infinite loops as demos.

### Micro-interactions

`spells` adds a detail that makes a finished interface memorable. Identify a standard or
boring element, study a creative pattern, adapt it to the brand, and implement it with CSS,
Anime.js, or Framer Motion. The strict rules are scoped enhancement, delight without
distraction, and high-performance execution that supports keyboard and touch, avoids layout
shift, and respects reduced motion. Core actions stay usable without the spell, and
reference designs are inspiration rather than permission to copy assets or add packages.

### Orchestration and documentation

`orchestration` is a routing and enforcement skill, not a creative one. If no validated
design exists, brainstorming must produce an Understanding Lock, an initial design, and a
started Decision Log. Then classify risk by user impact, irreversibility, cost, complexity,
uncertainty, and novelty. Low risk proceeds to planning; moderate risk recommends a
multi-agent review; high risk requires a substantive review, with multi-agent work only
under explicit delegation authorization. A multi-agent review only critiques, revises, and
resolves decisions, and cannot expand scope or reopen the problem. Execution waits for an
approved design, a complete Decision Log, documented assumptions, and acknowledged risks.
The skill exits only with an explicit next step and all prior steps complete.

`md` analyzes a Stitch project and writes a `DESIGN.md` source of truth. Use the Stitch MCP
prefix from `list_tools`, list projects and screens, fetch the screen metadata and the
HTML download URL, and read the project `designTheme`. Then describe the atmosphere, map
each color to a descriptive name, exact hex, and functional role, translate radii and shapes
into physical descriptions, and describe depth and elevation. The output follows five
sections: visual theme and atmosphere, color palette and roles, typography rules, component
stylings, and layout principles. Access to the MCP server, a designed screen, and the
prompting guide are prerequisites, not bundled assets.
## Output contract

- Name the skill, the artifact, and the framework or theme version in the first line of your reasoning and in the todolist.
- Report the artifact. A style, a philosophy, a design direction, a token register, a contrast report, a layout audit, a usability scorecard, a component, a micro-interaction, a DESIGN.md, or a workflow decision.
- Keep token names, hex codes, font names, ratios, WCAG levels, style names, selectors, and error text verbatim.
- State which rendered artifact was judged, at which widths, and whether the overflow check measured 0.
- State the light and dark theme, the contrast basis, and the exact token value behind a color decision.
- Keep open work open. An unmeasured gate, an unverified token, a missing helper, and an unaudited UI are reported, never rounded up.
- Never print a secret, a token, a credential, or private project data. Redact it and name the rule.
- Write through `unslop`. Short declarative sentences, sentence case headings, no em dash, no colon connecting two clauses, no chatbot framing.

## Failure handling

| Situation | Response |
| --- | --- |
| The page was called done without a narrow overflow measurement | Measure `scrollWidth - clientWidth` at narrow widths and report the number. |
| A style would be blended without a request | Use one style body, or ask before mixing. |
| A token or font value was invented | Mark it `Unknown` and ask for the real value. |
| A contrast claim comes from an unmeasured token | Run the checker or mark the ratio unverified. |
| A theme is called passing without dark mode | Measure both themes before reporting. |
| A design was self-graded by its builder | Use a separate judge and re-render the artifact. |
| A signal metric is treated as a defect | Look at the screenshot and keep the deliberate choice when it is intentional. |
| A font would pop in essential text | Use self-hosted WOFF2, a matched fallback, and a bounded reveal. |
| A frontend dependency is assumed | Check `package.json` and output the install command when it is missing. |
| A required design review is skipped | Block implementation and run the required brainstorming or review. |
| A missing support file is fabricated | Resolve it from the declared upstream or skip the dependent step. |
| The evidence contradicts the requested claim | Show the evidence and stop. |

## Provenance

12 `sickn33-design-*` source directories became 12 canonical skills in 6 groups. Each
source had one body, so no merge or variant resolution was needed. Every body is verbatim
at `references/skills/<skill>.md` with its original frontmatter removed. 52 asset files
totaling 551,061 bytes were copied under `references/assets/<skill>/` at the same relative
path. The largest set is `it`, which contains 48 nested style `SKILL.md` bodies plus its
router body. The rest are single files: `philosophy` ships `reference.md`, `spatial` ships
`scripts/layout-audit.js`, `system` ships `references/motion-choreography.md`, and
`token-contrast` ships `references/contraste-checker.md`.

The canonical name drops the `sickn33-design-` prefix, so `sickn33-design-taste-frontend`
becomes `taste-frontend` and `sickn33-design-token-contrast` becomes `token-contrast`.

`it` is the only source with nested skill folders. The 48 style bodies are preserved at
the same relative paths under `references/assets/it/<style>/SKILL.md`, so the router's
instruction to read `<style-folder>/SKILL.md` relative to its own directory still resolves.
The archive therefore removes 12 top-level folders and 60 skill directories in total,
because `catalog.py` also counts the nested style bodies.

The pack keeps the overflow gate as mandatory, separates gates from signals, keeps the
font-loading rules, and rejects self-graded design. `theme-guide` says its shared execution
runtime is not bundled, and `system` names external design siblings and audit helpers as
not bundled in its source tree; the `spatial` asset supplies `layout-audit.js` in this
pack. `token-contrast` ships its checker as source rather than a committed script, and it
requires Node 18+. The Stitch MCP server and prompting guide are prerequisites for `md`.
Keep those gaps and never fabricate a missing target.

Upstream collection `sickn33`. Original catalog paths are preserved in `SOURCES.md` and
under `_archive/design/catalog/`.
