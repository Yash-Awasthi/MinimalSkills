# design-system

Load for tokens, type, spacing, motion and contrast.

## token layers

| layer | example | rule |
| --- | --- | --- |
| primitive | `--gray-900` | raw value, never used in a component |
| semantic | `--fg`, `--bg`, `--border` | what a component uses |
| component | `--card-bg` | only when a semantic token is not enough |

Two layers, primitive and semantic, cover most products; a third needs a consumer shipping in the same release, or it drifts from both.

## color roles

foreground, background, border, brand, semantic (danger, success, warning, info). Five to seven roles. Every color in the ui maps to one.

## type scale

```
12 / 14 / 16 / 20 / 24 / 32 / 48
line-height 1.5 body, 1.2 display
measure 60-75 characters
```

- One family for ui, one for display if needed. Four weights maximum.
- Body 16px minimum on the web. 14px only for dense tables.
- Tabular numbers for anything that aligns in a column.

## spacing

One base unit, usually 4px or 8px. Steps: 4, 8, 12, 16, 24, 32, 48, 64. An arbitrary value in a component is a token gap.

## radius and elevation

- `child = max(0, parent - gap)` for nested corners.
- Elevation from one shadow scale, three levels maximum.
- A border and a shadow together read as a mistake.

## motion

| use | duration |
| --- | --- |
| hover, press feedback | 100-150ms |
| enter, exit | 150-250ms |
| layout change | 200-300ms |

Ease out for entry, ease in for exit. Animate opacity and transform only. Honor `prefers-reduced-motion`.

## contrast

```js
// relative luminance, then (l1 + 0.05) / (l2 + 0.05)
```

- 4.5:1 body, 3:1 large text, 3:1 ui component boundaries.
- A brand color usually fails as text. Use it as a fill.
- Placeholder text is text. 4.5:1 applies.
- Disabled controls are exempt from the ratio but must still be distinguishable.

## states

Every interactive element: default, hover, focus-visible, active, disabled, loading, error. A missing state is an incomplete component.

## delivery

- Tokens in one file, exported to css variables and to the design tool.
- A token renamed in code and not in the tool drifts within a week.
- Document the scale in one page; a gallery that lists every token value goes stale within a release.
## practice index

| topic | the rule that matters |
| --- | --- |
| UX practice | Task, friction, fix: name the step where the user stops, not the screen that looks wrong. |
| Behavioral lenses | Hick (choices slow), Fitts (target size and distance), Miller (7 plus or minus 2 chunks), Jakob (familiar patterns win). |
| Figma | Components with variants, tokens as variables, auto-layout for every frame; a detached instance is a fork nobody tracks. |
| Stitch | Generates UI from a prompt: treat output as a wireframe, re-token it, never ship its colors. |
| Free resources | Icons (Lucide), fonts (Google Fonts with `display=swap`), illustrations (unDraw); check the license per asset. |
| Radix | Primitives for behaviour (dialog, popover, tooltip); style them with tokens, keep the accessibility wiring. |
