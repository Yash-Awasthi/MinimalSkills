---
name: design-ux
description: Use when setting visual direction or auditing a UI: design tokens, type and spacing scale, contrast, named visual styles, Apple HIG surfaces, UX flows, microcopy, icon and brand kits. Triggers: design system, style, HIG, contrast, audit.
---

# design-ux

## use when

- tokens, type scale, spacing, motion, contrast -> references/design-system.md
- choose or apply a visual style -> references/styles.md
- Apple platform surface or pattern -> references/apple-hig.md

not for: React components and fetching (frontend-ui), brand strategy (strategy-product)

## rules

- Conflict order: accessibility, then brand, then density; a branded page that fails contrast is not shipped.
- Direction and mechanics are separate: a style name never waives the token, contrast or overflow gate.
- Judge the rendered image, not the token stream; never self-grade your own page.
- Overflow gate: `scrollWidth - clientWidth` is 0 at 390px, 768px and 1024px in the same turn.
- Contrast is measured on computed values: 4.5:1 body, 3:1 large text and ui borders.
- Nested radii are concentric: `child = max(0, parent - gap)`; keep one accent, one type pair and one radius family, and review a second.
- Font loading must not reflow the first viewport: self-host woff2, preload the above-the-fold weight, `size-adjust` the fallback.

## change

1. Locate: the token, its consumers, and the rendered states at 390px, 768px and 1024px.
2. Propose the visual change in one sentence, with the direction you rejected.
3. Predict before rendering: contrast ratio, overflow, tap targets and which screen moves.
4. Back up the original token block in context, pinned to `git rev-parse HEAD`.
5. Apply one concern per edit; a colour change and a spacing change are two edits.
6. Verify: contrast on computed values, the overflow gate and tap targets at 44x44.
7. Regress: every component reading the token, plus both themes.
8. Compare the screenshots against the prediction; an unplanned overflow stops the edit.
9. Report screenshots and gate values, then take the next item.

## audit

1. Render at 390px, 768px, 1024px. Screenshot each.
2. Run the gate in the console.

```js
const de = document.documentElement;
({ overflow: de.scrollWidth - de.clientWidth, width: de.clientWidth });
```

3. Check contrast on the computed color of every text and border token.
4. Check tap targets at 44x44.
5. Read the screenshots: collisions, ragged alignment, cramped rows, orphaned labels.
6. Fix, re-render, re-check. A described fix list is not an audit.

## choose

1. Pick the family from the product table, not from taste.
2. Set the type pair, the accent, the radius family, the shadow scale.
3. Apply across ui, illustration and empty states. A mixed style reads as unfinished.
4. Check contrast and density before adding a second decorative idea.

| product | direction | avoid |
| --- | --- | --- |
| developer tool | dense, mono accents, dark default | illustration-heavy hero |
| fintech dashboard | neutral, tabular numbers, calm accent | gradients on data |
| consumer app | warm, large type, one accent | dense tables |
| editorial | serif display, generous measure | card grids everywhere |
| internal admin | utility first, high density | brand expression |

## tokens

```css
:root {
  --color-bg: #0b0d10;  --color-fg: #e7e9ee;  --color-accent: #4f7cff;
  --color-muted: #8a90a2;  --color-border: #23262f;
  --space-1: 4px; --space-2: 8px; --space-3: 12px; --space-4: 16px;
  --radius-sm: 6px; --radius-md: 10px;
  --font-sans: "Inter", system-ui, sans-serif;
}
```

- A component reads the variable, never a hex; one hardcoded color breaks the dark theme.
- Five color roles are enough: bg, fg, accent, muted, border.
- Name the role, not the value: `--color-danger`, never `--color-red`.

## numbers

| item | value |
| --- | --- |
| body contrast | 4.5:1 |
| large text and borders | 3:1 |
| tap target | 44x44 |
| type scale | 12, 14, 16, 20, 24, 32, 48 |
| spacing base | 4px, steps to 64 |
| motion | 150-250ms, opacity and transform only |
| measure | 60-75 characters per line |

## decide

| condition | action |
| --- | --- |
| client has a brand system | extend it, do not replace it |
| no system exists | define 5 color roles, 1 type pair, 1 spacing base |
| dense data surface | compact spacing, 12px floor, tabular numbers |
| style conflicts with contrast | keep contrast, adjust the style |
| dark mode requested | token swap, test both for contrast |
| motion requested | under 250ms, honor reduced motion |
| display text above the fold | preload, or hold at opacity 0 with a 2.5s reveal |

## check

- [ ] overflow 0 at three widths
- [ ] contrast passes on computed values, both themes
- [ ] tap targets 44x44
- [ ] focus visible on every interactive element
- [ ] first viewport paints complete, no font reflow
- [ ] one accent, one radius family, one spacing base

## stop

| condition | action |
| --- | --- |
| no brand assets and no direction | ask for one reference |
| a11y conflicts with the chosen style | surface it, do not drop the label |
| the request is a copy of a living product | refuse the clone, offer the direction |

## emit

- screenshots at the three widths
- gates: overflow, contrast, tap targets, with values
- what was not checked
