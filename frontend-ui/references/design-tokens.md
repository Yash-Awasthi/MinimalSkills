# design-tokens

Load for tokens, theming, layout mechanics and the overflow gate.

## tokens

```css
:root {
  --fg: oklch(0.2 0 0);
  --bg: oklch(0.99 0 0);
  --border: oklch(0.9 0 0);
  --brand: oklch(0.55 0.18 260);
  --radius: 0.5rem;
  --space: 0.25rem;
}
```

- One primitive set: foreground, background, border, brand, semantic (danger, success, warning).
- No hardcoded hex in a component. A second source of color is a defect.
- Radius nesting: `child = max(0, parent - gap)`.
- Spacing comes from one base unit (4px or 8px); a raw `padding: 13px` in a component is a token gap, not a one-off.
- One accent. Hover, active and focus read as more prominent, not less.

## themes

- Theme by swapping token values under a selector, not by branching in components.
- Test both themes for contrast, not just the default.
- `color-scheme` set so form controls follow.

## contrast

- 4.5:1 for body text, 3:1 for large text and ui borders.
- Check computed values, not the design file.
- A brand color used as text usually fails. Use it for fill, not text.

## layout

| need | tool |
| --- | --- |
| one axis | flex |
| two axes | grid |
| page frame | grid with named areas |
| sticky element | `position: sticky` with a scroll container |
| aspect lock | `aspect-ratio` |

## overflow gate

```js
const over = document.documentElement.scrollWidth - document.documentElement.clientWidth;
// must be 0 at 390px, 768px, 1024px, and the dev width
```

- `flex-wrap` on header and nav rows.
- `min-width: 0` on flex and grid children, or long text forces overflow.
- `100%` instead of `100vw` where a scrollbar exists.
- `overflow-x: clip` is a backstop, not a fix.
- Long words: `overflow-wrap: anywhere` on user content.

## interaction

- Every interactive element has hover, focus-visible, active and disabled states.
- Focus ring never removed without a replacement.
- Tap target 44x44 minimum.
- Motion under 200ms for feedback, and honor `prefers-reduced-motion`.

## review

- Render the page and read the screenshot. A token stream is not a rendered result.
- Check 390px, 768px, 1024px.
- Check the empty state and the long-text state.
