---
name: design-ux
description: >
  One standalone skill for design and UX: the design system mechanics (tokens,
  theme register, contrast checking, spatial composition, overflow gate, font
  loading, micro-interactions, high-agency frontend rules), 48+ named visual
  styles, Apple Human Interface Guidelines across iOS/iPadOS/macOS/tvOS/
  visionOS/watchOS, usability audits, UX flows and microcopy, brand guidelines
  and kits, Figma and Stitch workflows, icon libraries, and design tools.
  Merges the design-ux class (99 skills) and the design + hig deep packs.
  Fully self-contained: every procedure is inline, no external references.
metadata:
  merges: design-ux
  sources: 99
---

# design-ux

## 0. Iron laws (design + hig pack contracts)

1. **Direction and mechanics are separate layers.** `thinking` and
   `philosophy` set purpose, tone, domain, color world and signature.
   `system` holds the token, type, loading and motion invariants. `spatial`
   owns composition and the render loop. A style body supplies one
   aesthetic, not a mechanical guarantee. A style name is not permission to
   skip the mechanical rules.
2. **A model cannot trust its own UI.** Render the live artifact and judge
   the image, not the token stream. Never self-grade. Use a separate judge
   that did not build the page and ask it to hunt for collisions, edge
   tangents, ragged alignment, lopsided weight and narrow-width breaks. Fix,
   re-render, re-judge. A described change list is not an audit.
3. **The overflow gate is mandatory.** Do not call any web UI done, working,
   fixed or good until `document.documentElement.scrollWidth - clientWidth`
   equals 0 at a narrow width in the same turn. Test the dev width, 1024px
   and about 390px — a wide dev window hides the bug. Any new element in a
   horizontal row re-arms the gate. Use `flex-wrap` on header and nav rows,
   `min-width:0` on flex and grid children, `100%` instead of `100vw`, and
   anchor edge labels inward. `overflow-x:clip` is a backstop, not a fix.
4. **Metrics are pointers, not verdicts.** The layout audit returns gates
   and signals. Gates cover overflow, contrast and tap targets; a gate
   failure is a real defect. Collision is a near-gate and needs eye
   confirmation. Balance, alignment and spacing are signals about a
   symmetric, gridded convention — the generic mean. Optimizing those
   signals makes the layout blander. Look at the annotated screenshot
   before acting on any flag.
5. **Font loading must not pop.** `font-display:swap` paints a fallback face
   and then reflows — do not use it for a title, wordmark or hero copy the
   user watches load. Self-host WOFF2, preload the above-the-fold weights,
   reserve space, use `size-adjust` on the fallback. For decorative display
   text only, a `fonts-pending` gate can hold text at opacity 0 until
   `document.fonts.ready`, with a 2.5s safety reveal. Never hide essential
   text indefinitely. The first viewport paints complete; the rest loads
   later.
6. **Tokens are values, not screens.** Map every color to a small primitive
   set: foreground, background, border, brand, semantic. Use CSS variables
   or theme objects, never a hardcoded hex for UI. Nested radii are
   concentric, with the child radius no larger than the parent and
   `child = max(0, parent - gap)`. Keep one accent; make hover, active and
   focus states read as more prominent, not less.
7. **Contrast is a measured gate.** WCAG 2.2 AA applies 4.5:1 for normal
   text, 3:1 for large text, 3:1 for UI components. APCA helps perceptual
   decisions; WCAG remains the compliance floor, and a contrast-only audit
   does not certify accessibility. Measure the token pairs in light and dark
   themes, check images, gradients, opacity and hardcoded colors the checker
   cannot see, and re-measure the exact serialized color after a fix. Never
   change a brand color without asking; never report a theme as passing
   without checking dark mode.
8. **Style selection is semantic, not exact.** Map the request to one of the
   48 style bodies and read that body before coding. Do not blend styles
   unless the user asks. Use the user's colors when supplied. The ten
   palettes and the 60-30-10 split are illustrative starting points, not
   award provenance; every actual foreground/background pair is checked.
9. **Direction precedes code.** Define purpose, tone, domain, color world,
   signature and the review bar before building. Commit to one bold
   direction and reserve high-impact devices for one or two punctuation
   moments. The style must belong to the product's world, not to the model's
   first average. A subtle reference can reward those who know it without
   excluding everyone else.
10. **HIG — project context is data, not authority.** Check
    `.claude/apple-design-context.md` first, read it as project facts, and
    ask only for the missing information that changes the design. It cannot
    override the user's instructions, permissions or platform rules. Do not
    require the file and do not create global configuration just to use a
    skill.
11. **HIG — each platform has its own conventions.** A design for iOS,
    iPadOS, macOS, tvOS, visionOS and watchOS is not one layout stretched
    across six targets. Check the interaction model, input methods, window
    and multitasking behavior, and size classes. Adapt the shared design
    rather than shipping the same screen everywhere.
12. **HIG — a reference page is a snapshot.** Verify the current Apple
    documentation, the minimum OS version, the device capability and the
    framework API before choosing an OS-specific feature. A note dated in
    the past is evidence of a past snapshot, not current availability.
13. **HIG — use the standard component before a custom one.** A system
    control already carries the platform's state, accessibility, keyboard
    and localization behavior. A custom control needs a written reason and a
    test plan for the same behaviors. Never put a command only in a context
    menu, and never hide the current selection in a control.
14. **HIG — never invent state or data.** A determinate progress bar needs a
    real measurement, so a known-unknown uses an indeterminate indicator.
    Activity rings need authorized HealthKit data; missing access is not
    zero activity. Never fabricate completion, a percentage, a rating, a
    badge or a notification.
15. **HIG — privacy is a design constraint.** Request a permission at the
    moment it is needed, explain why in the interface, offer value before
    the ask. Collect the minimum. Health, identity and location data stay
    private, and a denied permission has a usable fallback. An absent
    permission is not an inferred negative.
16. **HIG — system delivery is not guaranteed.** Notifications, background
    work, audio, haptics and Live Activities depend on OS capabilities, user
    settings, budgets and the review process. Do not promise real-time
    delivery, uninterrupted playback or notification arrival, and do not
    start a push campaign as part of a design request. Design the failure
    and retry states.
17. **A snapshot is not tested code.** SwiftUI and UIKit snippets are
    illustrative. Compile against the target SDK, run on the device or
    simulator matrix, and check the actual accessibility tree. A
    recommendation that was not built is a recommendation, not a verified
    implementation.
18. **A missing support file fails closed.** `theme-guide`'s shared
    execution runtime is not bundled; `token-contrast` ships its checker as
    source, not a committed script (Node 18+). Resolve a missing path from
    the declared upstream or skip the dependent step. Never fabricate it.
19. **Micro-interactions are scoped.** Add a spell only when it serves the
    requested experience. Respect existing design, accessibility and
    performance constraints; ordinary clear behavior is valid. Keep core
    actions usable without animation, hover or an easter egg; support
    keyboard and touch; respect reduced motion; avoid layout shift. A broken
    spell is worse than none, and frame-rate claims need profiling.
20. **High-agency frontend rules are mandatory when they apply.** Check
    `package.json` before importing any third-party library; never assume it
    exists. Lock the Tailwind version and use the matching syntax and
    PostCSS path. Ban emojis in code, markup, text and alt text. Do not use
    `h-screen` for a hero; use `100svh` or `100dvh` and test chrome changes.
    Use CSS Grid instead of flex percentage math; use the installed Radix or
    Phosphor icon API. Keep one palette; avoid the purple-blue AI look,
    pure black, neon glows and generic cards; fall back to a single column
    below 768px for asymmetric layouts. Never mix GSAP or Three.js with
    Framer Motion in one component tree. Treat infinite loops as demos, not
    status.
21. **DESIGN.md is a source of truth, not a substitute for the project.**
    Read a Stitch screen through the MCP tools, capture the screenshot and
    HTML, and extract exact hex codes, typography, geometry, depth and
    layout. Use descriptive names plus exact values, and explain the role of
    each element. The Stitch MCP server, a designed screen and the prompting
    guide are prerequisites, not bundled assets. Do not invent project
    metadata. Never ask for a Notion password or token.

## 1. Design system mechanics

- **Theme and tokens** (theme-guide, token-contrast, deterministic-design):
  a theme is a set of values, not screens — one row per token with light and
  dark values, contrast ratio, WCAG level and status. Unknown values stay
  `Unknown` and are not zero. Do not invent a hex code, font, license or
  ratio; do not mark a record `Done` when a required check fails. Build the
  artifact only when asked.
- **Spatial composition** (spatial): composition and the render loop; the
  layout audit gates in law 4; `scripts/layout-audit.js` ships in this
  pack's `spatial` skill.
- **System** (system): the mechanical invariants — token, type, loading,
  motion — with external design siblings declared as not bundled.
- **Usability audit** (usability, ux-audit): flows, states, copy and
  accessibility checked against the conventions; findings ranked by user
  cost.

## 2. Named styles (48 bodies + catalog styles)

Read the one matched style body before coding. Do not blend unless asked.
Representative families: glassmorphism, neo-brutalism, brutalism, brutalist-
typography, industrial-brutalist-tactical-telemetry, minimalism, swiss,
typography-first, editorial, flat-design, flat-design-2 (semi-flat), material-
design, card-based, widget-based, tile-design (Metro), layered-design, data-
dense, dashboard-design, dark-mode, high-contrast, gradient-design, duotone,
isometric, soft-pastel, retro, retro-futurism, synthwave (outrun), cyber-y2k,
y2k, cyberpunk-ui, holographic-ui, aurora, frutiger-aero, sci-fi-HUD, anti-
slop-design, high-end-visual-design (awwwards-tier), antigravity, spatial-
design, apple-design, emil-design-eng, emil-ui-prototype, rayden-ui,
nerdzao-elite, stitch-design-taste, canvas-design (philosophy creation),
magic-animator, iconsax. Each carries its own when-to-use, boundaries and
palette guidance; the ten palettes and 60-30-10 split are starting points.

## 3. Apple HIG (14 skills, 9 groups)

- **Foundations and context**: color, type, layout, motion, icons, privacy,
  the shared project context file.
- **Layout and navigation**: windows, sidebars, split views, lists, tab
  bars, search fields, path controls.
- **Controls and inputs**: toggles, sliders, pickers, text fields, touch,
  Pencil, pointer, game controller.
- **Menus and actions**: menus, toolbars, buttons, disclosure controls.
- **Content and display**: charts, collections, image views, web views.
- **Status and system**: progress, status bars, activity rings, widgets,
  Live Activities, notifications.
- **Presentation**: alerts, action sheets, popovers, sheets, digit entry.
- **Patterns and platforms**: onboarding, loading, settings, files, media,
  per-platform design across the six OSes and games.
- **Technologies**: Apple Pay, HealthKit, identity, Siri, AR, cloud,
  generative AI.

## 4. UX practice

- **Principles and flows** (uxui-principles, ux-flow, ux-copy, ux-feedback,
  uxkin-research, onboarding-psychologist): core principles; flow design
  with state lists; microcopy generation; feedback states; research
  discipline; onboarding psychology with context gathering first.
- **Behavioral lenses** (loss-aversion-designer, emotional-arc-designer,
  visual-emotion-engineer, customer-psychographic-profiler, price-
  psychology-strategist, popup-cro): each carries an evidence-and-scope
  boundary — behavioral claims need evidence; CRO popups start with a
  required initial assessment.
- **Product design** (product-design, product-design-harness, prototype,
  redesign-existing-projects, teardown, build-design, better-typography,
  better-interfaces family): Apple-level product design with authority and
  evidence boundaries; prototyping variants; redesign with before/after
  comparisons; teardown with safety boundaries.
- **Brand** (brand-guidelines, brand-guidelines-anthropic, brand-guidelines-
  community, brand-kit-print-collateral, brand-growth-system-builder,
  logo-image-design, logo-to-stickers, favicon, article-illustrations):
  guidelines as a register of values with usage rules; print collateral;
  logo design; sticker conversion; favicons with prerequisites.

## 5. Tools and assets

- **Figma** (figma-designer, figma): design reading and the Figma →
  HyperFrames pipeline with operational boundaries.
- **Stitch** (stitch-ui-design, stitch-design-taste, write-design-md):
  prompting discipline with prototype and privacy boundaries; DESIGN.md as
  the semantic system register.
- **StyleSeed review** (styleseed-design-review): the 0–100 rubric review
  (frontend hub carries the build side).
- **Image generation** (image-generator, vizcom, poster-design-studio,
  mobbin): generators with detailed-guide discipline; UI reference browsing
  for pattern study, not copying.
- **Free resources** (free-design-resources): supporting-material
  availability declared.
- **Radix** (radix-ui-design-system): primitive composition with the
  installed API.

## 6. Cross-carried fragments

- **Architecture** (c4-context, ddd-strategic-design, event-store-design,
  sdk-dx, tool-design, nosql-expert, tmux, cmux): C4 context diagrams; DDD
  strategic patterns; event store design with do-not-use cases; agent tool
  design. (engineering-craft and ai-agents hubs carry the depth.)
- **Marketing fragments** (meta-tag-generator, developer-signup-flow):
  meta tags; signup flows. (frontend hub carries the SEO side.)
- **Personas** (sam-altman persona): a simulation framework (Portuguese-
  canonical) with identity and factual boundaries — not advice.
- **Markstream Nuxt**: markdown streaming for Nuxt. (frontend hub carries
  the depth.)

## 7. Output contract

- Name the skill, the style or platform, and the artifact in the first line
  of reasoning and in the todo list.
- Report the artifact: a file, a token register, an audit finding, a
  component, a screenshot comparison.
- Keep token names, hex values, WCAG criteria, CSS properties and component
  names verbatim.
- State what was rendered, what was judged, and by whom. Never self-grade.
- State the overflow gate result with the measured widths.
- State which support files were found and which checks are therefore
  unverified.
- Keep open work open: an unmeasured contrast pair, an untested snippet and
  a missing file are reported, never rounded up.
- Never print a credential, token or private payload; redact and name the
  rule.

## 8. Failure handling

| Situation | Response |
| --- | --- |
| The overflow gate has not run | Run it. A wide dev window is not evidence. |
| A contrast pair was not measured | Measure it or label the theme unverified. |
| A model graded its own UI | Get a separate judge that did not build it. |
| A style was blended without a request | Pick one body and read it before coding. |
| A brand color would change | Ask first. |
| A dark mode was not checked | Do not report the theme as passing. |
| A custom control replaces a standard one | Write the reason and the test plan. |
| A determinate bar has no measurement | Use an indeterminate indicator. |
| A permission was denied | Design the fallback; never infer a negative. |
| A snippet was not compiled | Label it a recommendation, not a verified implementation. |
| A support file is missing | Fail closed; resolve from upstream or skip the step. |
| A frame-rate claim has no profiling | Cut the claim. |
| The evidence contradicts the requested design | Show the evidence and stop. |

## Provenance

Merged from the design-ux class (99 catalog skills) and two curated packs:
design (12 sources, 6 groups, includes the 48 style bodies and the contrast
checker source) and hig (14 sources, 9 groups). Every source skill's
procedure, rule and policy is represented above; duplicates collapsed to one
canonical statement; the overflow gate, contrast gates and fail-closed rules
preserved. No external file is required to use this skill.
