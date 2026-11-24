# styles

Load when choosing or applying a visual direction.

## choose by product

| product | direction | avoid |
| --- | --- | --- |
| developer tool | dense, monospace accents, dark default | illustration-heavy hero |
| fintech dashboard | neutral, tabular numbers, calm accent | playful gradients on data |
| consumer app | warm, large type, one accent | dense tables |
| editorial | serif display, generous measure | card grids everywhere |
| internal admin | utility first, high density | brand expression |
| marketplace | photo-led, neutral chrome | strong brand color behind product images |
| onboarding flow | one idea per screen, large type | dense forms, competing CTAs |

## families

| family | markers | risk |
| --- | --- | --- |
| swiss | grid, sans, left align, one accent | bland without strong type |
| brutalist | raw borders, mono, high contrast | unreadable at scale |
| glass | blur, translucency, layered depth | contrast failures |
| neumorphic | soft shadows, low contrast | invisible controls |
| editorial | serif display, rules, drop caps | slow to scan in ui |
| retro terminal | mono, phosphor color, scanlines | accessibility |
| material | elevation, motion, ripple | generic feel |
| neo-brutal | thick borders, offset shadows, saturated | heavy at density |

Token starting points per family, so the first component does not invent its own:

```
swiss        radius 0-2px   shadow none        scale 1.25  accent 1 hue   weight 400/600
brutalist    radius 0       shadow 4px 4px #000 scale 1.333 accent 2 hues  weight 700/900
glass        radius 12-16px shadow 0 8px 32px   scale 1.2   accent 1 hue   blur 12px
neumorphic   radius 16-24px shadow in+out pair  scale 1.2   accent 0       contrast min 4.5:1
editorial    radius 0       shadow none        scale 1.333 serif display measure 60-75ch
terminal     radius 0       shadow none        scale 1.2   mono only     bg near-black
material     radius 4-28px  shadow elevation 1-5 scale 1.2  accent 1 hue   motion 200-300ms
neo-brutal   radius 0-4px   shadow 6px 6px      scale 1.25  accent 3 hues  border 2-3px
```

## apply one

1. Pick the family from the product table, not from taste.
2. Set the type pair, the accent, the radius family and the shadow scale.
3. Apply across ui, illustration and empty states. A mixed style reads as unfinished.
4. Check contrast and density before adding a second decorative idea.

Order the work: tokens, then one representative screen end to end, then the rest. Styling screen by screen before tokens exist produces five radii and three shadow recipes, and the cleanup costs more than the first pass.

## named directions

`swiss`, `editorial`, `brutalist`, `neo-brutal`, `glass`, `neumorphic`, `terminal`, `material`, `clay`, `paper`, `bauhaus`, `art-deco`, `memphis`, `vaporwave`, `corporate-memphis`, `scandinavian`, `japanese-minimal`, `cyberpunk`, `retro-70s`, `risograph`, `blueprint`, `isometric`, `collage`, `gradient-mesh`, `monochrome`, `high-contrast`, `organic`, `geometric`, `type-driven`, `photo-led`.

A style name is a starting point: fix the palette, type scale and radius in tokens before the first component, or each component invents its own.

## type

- Scale ratio 1.2 for dense product ui, 1.25 for marketing, 1.333 for editorial. More than five sizes in one product means the scale is decorative.
- Body 16px minimum, 18px for long reading. Line height 1.5 for body, 1.15-1.25 for display.
- Measure 45-75 characters. A full-width paragraph on a 1440px screen is 150 characters and unreadable.
- Weights: two per family. A third weight is emphasis that the layout should have carried.
- Tabular figures (`font-variant-numeric: tabular-nums`) in every column of numbers, or the digits jitter on update.

## color

- Roles, not colors: `bg`, `surface`, `border`, `text`, `text-muted`, `accent`, `danger`, `success`, `warning`. A component that names a hex value has no theme.
- One accent in use at a time. Two accents compete; three read as a bug.
- Text on background at 4.5:1 for body, 3:1 for large text and UI borders. Check the muted text too; it is the usual failure.
- Never encode state in hue alone. Pair with an icon, a label or a weight change for the 8% of men with a color vision deficiency.
- Dark mode is a second palette, not an inversion. Pure `#000` on pure `#fff` vibrates; use near-black and off-white.

## composition

- One focal point per viewport; two competing CTAs split the click and the eye has nowhere to land.
- Align to the 8px grid; break it once per screen, and only for the element the eye should land on.
- Whitespace groups; borders separate only when grouping fails.
- Hierarchy from size, then weight, then color, then position.
- Three levels of emphasis maximum. A fourth reads as noise.
- Spacing scale in steps of 4 or 8: 4, 8, 12, 16, 24, 32, 48, 64. A 13px gap is a typo with consequences.
- Vertical rhythm: one spacing value between sections, one inside them. Mixed gaps make unrelated blocks look related.

## motion

- 150-200ms for a state change on a control, 250-300ms for an element entering, 0 for anything the user repeats.
- Ease out on entry, ease in on exit. Linear motion on a large element reads as broken.
- Animate transform and opacity only; animating layout properties drops frames on mid-range phones.
- Respect `prefers-reduced-motion`: cut to a fade or nothing, never keep the movement.

## anti-patterns

- gradient on every card
- three accent colors
- centered body text past two lines
- icon set from three families
- shadows on flat surfaces
- placeholder copy in a delivered design
- a hero image that pushes the actual product below the fold on a laptop
- text over a photo without a scrim, at any contrast
