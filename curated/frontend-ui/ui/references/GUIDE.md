# ui guide

The long-form group prose and the full roster. `SKILL.md` is the loadable hub, and
`references/skills/<skill>.md` is the verbatim body to follow for one task.

### StyleSeed build

| Skill | What it does |
| --- | --- |
| [`component`](references/skills/component.md) | Generates a UI component that follows the StyleSeed conventions, accepts a className override, and states the execution boundary. |
| [`motion`](references/skills/motion.md) | Applies one of five StyleSeed motion seeds or a named keyword move, from the installed recipe rather than inline parameters. |
| [`page`](references/skills/page.md) | Scaffolds a mobile page or screen from the StyleSeed layout patterns, with the same conventions and execution boundary. |
| [`pattern`](references/skills/pattern.md) | Composes a card, list, form section, or grid from design system primitives instead of a one-off layout. |
| [`tokens`](references/skills/tokens.md) | Views, adds, or updates design tokens in the StyleSeed system, keeping the JSON and CSS sources in sync. |

### StyleSeed review

| Skill | What it does |
| --- | --- |
| [`lint`](references/skills/lint.md) | Runs a fast static lint for hardcoded colors, raw pixels, old size syntax, physical properties, forbidden colors, and missing slots. |
| [`review`](references/skills/review.md) | Reviews UI code for token compliance, component conventions, accessibility, mobile practice, performance, typography, spacing, and coherence. |
| [`score`](references/skills/score.md) | Scores a UI file from 0 to 100 with a per-category breakdown, worst offenders, and a prioritized fix list, optionally as a gate. |

### StyleSeed setup and update

| Skill | What it does |
| --- | --- |
| [`setup`](references/skills/setup.md) | Runs an interactive design system setup across app type, brand color, concept, font, app name, and first page, with verified sources. |
| [`update`](references/skills/update.md) | Detects the installed StyleSeed version, reports outdated pieces, and updates only after approval while preserving project files. |

### Accessibility and validation

| Skill | What it does |
| --- | --- |
| [`a11y`](references/skills/a11y.md) | Audits a component or page against WCAG 2.2 AA and fixes perceivable, operable, understandable, and robust defects. |
| [`visual-validator`](references/skills/visual-validator.md) | Verifies UI visual quality, design system compliance, and accessibility with concrete evidence rather than an opinion. |

### Screenshot and states

| Skill | What it does |
| --- | --- |
| [`from-screenshot`](references/skills/from-screenshot.md) | Reads a screenshot or mockup, measures it, builds with the project's own components, then compares side by side and fixes the gaps. |
| [`states`](references/skills/states.md) | Designs and builds the states agents forget: first use, empty, loading, error, offline, no results, long content, permission denied, and success. |

### UI guidance and routing

| Skill | What it does |
| --- | --- |
| [`skills`](references/skills/skills.md) | An entry point to an external opinionated UI guidance collection, selected against the project's design system and target devices. |
| [`skills-root`](references/skills/skills-root.md) | Routes UI work to the smallest useful UI Skills context through the CLI, with a cap of three selected skills. |

### Design practice

| Skill | What it does |
| --- | --- |
| [`ux-designer`](references/skills/ux-designer.md) | Creates interface designs, wireframes, and design systems with user research, accessibility, and modern design tools. |
| [`ux-pro-max`](references/skills/ux-pro-max.md) | A searchable design database of styles, palettes, font pairings, UX rules, charts, and 11 stack guides, with a design system generator. |
## Group notes

### StyleSeed build

`component` generates one component from the StyleSeed conventions. Support a
`className` prop for overrides, use the installed primitives and tokens, and state the
execution boundary. `page` scaffolds a mobile screen from the layout patterns. `pattern`
composes a card, list, form section, or grid from primitives rather than a one-off
layout.

`tokens` lists, adds, or updates tokens and keeps the JSON and CSS sources in sync. Check
both files after a change. `motion` applies a seed or a named move. It has five
personality seeds, Spring, Silk, Snap, Float, and Pulse, each across entrance, exit,
hover, press, and layout, plus named moves such as toggle-flip, toggle-curtain,
reveal-blur, pop-in, and shimmer. The recipe lives in one source and is spread into the
component. This tree does not bundle the motion engine, `DESIGN-LANGUAGE.md`, the preview
routes, or the calibrated recipes, so verify them in the target project or report the
prerequisite.

### StyleSeed review

`lint` is the fast static pass. Eight checks cover hardcoded colors, raw pixel values in
Tailwind, old width and height syntax, physical properties that assume left to right,
forbidden colors, a missing `data-slot`, ambiguous font-size arbitrary values, and a
`className` built without `cn()`. It is a quick check, not a full review.

`review` is the full checklist across token compliance, component conventions,
accessibility, mobile practice, performance, typography, spacing, and coherence. The
coherence section points at `VISUAL-CRAFT.md` C0, which is not bundled, so label those
checks unverified unless the file exists.

`score` turns the review into a number from 0 to 100 with a category breakdown, the worst
offenders, and a prioritized fix list. In gate mode it fixes and re-scores to the floor
of 80 before showing the user. It does not authorize edits beyond that gate, and the
reference files it names are not bundled. Use the inline rubric and label unsupported
checks unverified.

### StyleSeed setup and update

`setup` runs six steps: app type, brand color, design concept from awesome-design-md,
font, app name and first page, then a summary. Verify the awesome-design-md URL before
applying it, and fall back to manual color selection if the fetch fails. The attribution
comment appears on the first scaffolded file only and is removable. Never add a
watermark to user-built components.

`update` detects the current setup, compares the local marker against a reviewed
upstream revision, reports the gaps, asks, then executes. It never overwrites
`theme.css`, never overwrites a project `CLAUDE.md` and only merges the Golden Rules
section, and never overwrites a component without approval. Show the change before the
change, and fetch nothing without consent. Legacy `ui-*` and `ux-*` names migrate to
`ss-*`.

### Accessibility and validation

`a11y` audits against WCAG 2.2 AA across the four principles. Perceivable, operable,
understandable, and robust, then fixes the defects it finds. It includes a design token
reference, and its output names each issue with its criterion. A token audit alone does
not prove contrast, labeling, focus order, or keyboard operation.

`visual-validator` is the evidence discipline. It covers visual analysis, design system
validation, accessibility verification, cross-platform consistency, and automated visual
testing. Never declare success without concrete visual evidence. It runs the mandatory
verification checklist and states which checks were manual and which were tooled.

### Screenshot and states

`from-screenshot` measures the image first, reads spacing, type, and color, builds with
the project's own components, then compares the result side by side and fixes the
remaining differences. Optional UXKIN connectivity is not required. Copy the pattern,
never the logo, brand name, illustrations, photos, or copy. Never describe a build as
matching without the comparison, and hand off the differences that remain.

`states` lists the states per screen, builds each one properly, then checks each. The set
is first use, empty, loading, error, offline, no results, long content, permission denied,
and success. Error copy says what happened and what to do next, never a raw code or stack
trace. Empty states explain the next action rather than only saying there is no data.

### UI guidance and routing

`skills` is an entry point to an external opinionated UI guidance collection. It does not
contain the complete upstream rules. Inspect the requested interface, the existing design
system, the target devices, and the accessibility requirements, then select the relevant
guidance.

`skills-root` is the routing layer. It uses the `ui-skills` CLI to select the smallest
useful context, prefers one skill, allows two only for two clear angles, and never uses
more than three. A route is a starting point, so verify the selected skill exists before
relying on it.

### Design practice

`ux-designer` covers interface design, wireframes, design systems, user research,
information architecture, visual and brand systems, prototyping, cross-platform design,
and design system implementation. For a flow change, identify the user task and the
existing completion or drop-off evidence, sketch the smallest flow, and define default,
loading, error, and success states. Use approved copy or label a placeholder.

`ux-pro-max` is the searchable design database. 50 or more styles, 96 palettes, 57 font
pairings, 99 UX guidelines, 25 chart types, and 11 stack guides, with a design system
generator and search scripts. Start with `--design-system` for reasoned
recommendations, then search for the detail. The CSVs are guidance, not a live
compatibility table, and the framework snippets mix versions. Verify the installed
version before copying an API or deploying a dataset recommendation.
