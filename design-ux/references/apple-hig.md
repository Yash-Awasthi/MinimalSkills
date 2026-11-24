# apple-hig

Load for iOS, iPadOS, macOS, watchOS, tvOS or visionOS surfaces.

## platform fit

| platform | primary input | layout default |
| --- | --- | --- |
| iOS | touch, one hand | tab bar, stack navigation |
| iPadOS | touch, pointer, keyboard | sidebar plus detail |
| macOS | pointer, keyboard | toolbar, menu bar, resizable windows |
| watchOS | glance, crown | vertical pages, one action |
| tvOS | focus, remote | focus-driven grid |
| visionOS | gaze and hands | spatial windows, depth |

An iOS layout ported to macOS keeps 44pt targets and no menu bar, so the window resizes wrong and the commands a mac user expects are absent.

## navigation

- Tab bar 2-5 items, top level only.
- Stack navigation pushes detail. A modal is for a task with a clear start and end.
- Back must be predictable: one gesture, one button, same result.
- Deep links resolve to the same screen as the in-app path.

## controls

| control | use |
| --- | --- |
| button | one primary action per screen |
| segmented control | 2-5 mutually exclusive views |
| toggle | immediate effect, no save |
| stepper | small numeric adjustment |
| sheet | task with a clear end |

Minimum hit target 44x44 points on touch platforms.

## typography

- Use the system font (SF Pro) unless the brand font ships every weight and supports Dynamic Type; a partial family falls back to tofu at the accessibility sizes.
- Dynamic Type: support the accessibility sizes, test at 200%.
- Never set body text below 11pt.

## color and materials

- Semantic colors adapt to appearance and accessibility settings.
- Test both appearances, plus increased contrast.
- Materials convey hierarchy; a material on a material loses depth.

## motion

- Transitions explain a spatial change, not decorate it.
- Respect Reduce Motion: cross-fade instead of zoom.
- Fire haptics on a completed destructive action or a selection change, not on every tap; a tap that always buzzes reads as a bug.

## accessibility

- Every image has a label or is marked decorative.
- VoiceOver order matches the visual order.
- Support Switch Control and full keyboard access.
- Test with the accessibility inspector, not by reading the code.

## review

1. Run on the smallest and largest supported device.
2. Rotate, and check the layout at each orientation.
3. Turn on the largest text size and check truncation.
4. Check the empty, loading and error states.
