---
name: ui
description: >-
  18 UI skills for building and reviewing interfaces. Covers StyleSeed component, page,
  pattern, token, motion, setup, and update work, the lint, review, and 0 to 100 score
  passes, WCAG 2.2 AA accessibility, visual validation with evidence, screenshot to UI
  reconstruction, the states agents forget, UI Skills routing, and the broad ux-designer
  and ux-pro-max design practice. Use when a task builds, reviews, scores, updates, or
  audits a user interface or design system, or when the user names a ui skill.
metadata:
  curated_from: 18
  skills: 18
  groups: 7
---

# ui

18 skills. 7 groups. One hub. Every source body is preserved verbatim in
`references/skills/<skill>.md`, and every non-SKILL.md file from a source pack sits at
the same relative path under `references/assets/<skill>/`. Load one body for the task.

`SOURCES.md` maps every source path to its canonical skill and group.
`references/INDEX.md` groups the links, `references/skills.tsv` carries every
description, and `references/GUIDE.md` holds the long-form group prose.

## Pack contract

**The target project decides.** StyleSeed skills assume a project that actually follows
StyleSeed. Read the installed tokens, theme, component exports, and conventions before
writing a snippet. When the target uses a different system, map the pattern to its API
rather than installing a second system beside it.

**Named references are not bundled.** `DESIGN-LANGUAGE.md`, `VISUAL-CRAFT.md`,
`engine/motion`, the preview routes, and the calibrated recipe files live in the target
project or its upstream. Verify each path and export before copying a named snippet. If
a path is absent, report the prerequisite and label any dependent check unverified.
Never invent a seed, a token, or a rule number.

**Five motion seeds, one engine.** The seeds are exactly five. Do not invent another
name, edit the calibrated seed files, inline the spring parameters, or add a third-party
animation library. StyleSeed targets framer-motion. No scroll-linked, parallax, or
infinite animation. Motion is for affordance, never a delay before content.

**States are part of the screen.** A build is not done at the happy path. List first use,
empty, loading, error, offline, no results, long content, permission denied, and success
for each screen, then build and check each one. Never show a raw error code or stack
trace to a user. Every list needs an empty state.

**Accessibility is not a visual opinion.** Semantic structure, keyboard operation, focus,
labels, contrast, and target size are checked against WCAG 2.2 AA. Token use alone does
not prove contrast or labeling, and a screenshot cannot prove keyboard behavior. Report
what was tested and with which tool.

**Every visual claim needs evidence.** Compare the built result with the source image
side by side. Describe the remaining differences. Never call a build a match without the
comparison, and never copy a logo, brand name, illustration, or photo from a reference.
Take the pattern, not the identity.

**The update is a merge, not an overwrite.** Show what will change before changing it.
Never overwrite `theme.css`, a project-specific `CLAUDE.md`, or a component without
explicit approval. Merge the Golden Rules section only. Fetch, clone, copy, or modify
nothing without consent, and never treat a live upstream revision as reviewed.

**Tokens stay in sync.** A token change updates the JSON and the CSS source together.
A list command reports what is installed, not what a doc claims should be installed.

**A score is a rubric result, not a certification.** The 0 to 100 score comes from the
inline rubric against the real project system. Gate mode fixes and re-scores to the
stated floor, and it does not authorize edits beyond that scope. Do not chase 95 to 100
past the floor.

**Attribution is one removable comment.** The single "Scaffolded with StyleSeed" line
goes on the first scaffolded file only and is explicitly removable. Never watermark a
component the user builds.

**Datasets and external collections are references.** The ux-pro-max CSV data and the
external UI Skills collection are guidance, not a complete rule set or a verified
framework API. Framework snippets mix versions, so check the installed version before
copying an API or adding a dependency.

**Write clean as you draft.** Short declarative sentences. No em dash. A colon may
introduce a list and may not connect two clauses. Sentence case headings. No chatbot
framing, no generic closer.

## Routing

| The user wants | Group |
| --- | --- |
| A component, page, pattern, token, or motion recipe built in StyleSeed | StyleSeed build |
| A fast lint, a design review, or a 0 to 100 design score | StyleSeed review |
| The design system installed for the first time, or the engine updated | StyleSeed setup and update |
| A WCAG audit, or visual validation with evidence | Accessibility and validation |
| A screenshot turned into UI, or the missing screen states | Screenshot and states |
| The right UI guidance selected for a task | UI guidance and routing |
| Broad interface design, research, or a searchable design database | Design practice |

## Full roster

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
## Output contract

- Name the skill, the target project, and the screen or component in the first line of your reasoning and in the todolist.
- Report the artifact. A component file, a page, a token diff, a motion change, a lint result, a score, an audit, or a comparison.
- Keep token names, seed names, class names, WCAG criteria, file paths, and error strings verbatim.
- State which named references were found, which were missing, and which checks are therefore unverified.
- State what was visual, what was static, and what was tested with a tool.
- Keep open work open. An unchecked state, an unmatched difference, and an unverified contrast claim are reported, never rounded up.
- Never print a secret, a private screenshot, or user data. Redact it and name the rule.
- Write through `unslop`. Short declarative sentences, sentence case headings, no em dash, no colon connecting two clauses, no chatbot framing.

## Failure handling

| Situation | Response |
| --- | --- |
| The project does not use StyleSeed | Map the pattern to its actual system. Do not install a second one. |
| A named reference or motion engine is absent | Report the prerequisite and label dependent checks unverified. Never invent it. |
| A sixth motion seed is requested | Refuse. There are exactly five. Name the nearest existing seed. |
| A state was not designed | Return to the state list and build it. A happy path alone is incomplete. |
| A visual match is claimed without comparison | Run the side-by-side comparison and report the remaining differences. |
| A contrast or keyboard claim rests on tokens alone | Test it or label it unverified. |
| An update would overwrite theme.css or a project file | Stop. Show the diff and ask. Merge only the allowed section. |
| A screenshot carries a logo or brand asset | Take the pattern only. Never copy the identity. |
| A score is presented as a certification | Call it a rubric result and state the scope and floor. |
| The evidence contradicts the requested claim | Show the evidence and stop. |

## Provenance

18 `sickn33-ui-*` source directories became 18 canonical skills in 7 groups. Each source
had one body, so no merge or variant resolution was needed. Every body is verbatim at
`references/skills/<skill>.md` with its original frontmatter removed, and every other
file from a source pack is copied under `references/assets/<skill>/` at the same relative
path. 26 asset files totaling 415,410 bytes were copied, all from `ux-pro-max`. They are
12 design data CSVs, 11 stack guides, and the `core.py`, `design_system.py`, and
`search.py` scripts.

The canonical name drops the `sickn33-ui-` prefix, so `sickn33-ui-a11y` becomes `a11y`
and `sickn33-ui-ux-pro-max` becomes `ux-pro-max`.

Ten skills belong to the StyleSeed design-system family: component, page, pattern,
tokens, motion, lint, review, score, setup, and update. Their bodies name
`DESIGN-LANGUAGE.md`, `VISUAL-CRAFT.md`, and `engine/motion`, which were not in the
source tree and are not bundled here. The bodies say so, and the pack keeps that
statement rather than fabricating the files.

`from-screenshot` and `states` come from UXKIN and carry optional connectivity. The two
UI Skills entries are an external guidance collection and its routing layer.
`ux-designer` and `visual-validator` are broad role skills. `ux-pro-max` is the only
member with data assets.

Upstream collection `sickn33`. Original catalog paths are preserved in `SOURCES.md` and
under `_archive/ui/catalog/`.
