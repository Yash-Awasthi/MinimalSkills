# design guide

The long-form group prose and the full roster. `SKILL.md` is the loadable hub, and
`references/skills/<skill>.md` is the verbatim body to follow for one task.

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
