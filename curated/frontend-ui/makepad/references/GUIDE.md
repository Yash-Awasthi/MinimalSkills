# makepad guide

The long-form group prose and the full roster. `SKILL.md` is the loadable hub, and
`references/skills/<skill>.md` is the verbatim body to follow for one task.

### 2.0 DSL and layout

| Skill | What it does |
| --- | --- |
| [`2-0-dsl`](references/skills/2-0-dsl.md) | Covers the Makepad 2.0 script_mod and Splash DSL, property-as-colon syntax, the := and +: operators, let bindings, spreads, and module registration order. |
| [`2-0-layout`](references/skills/2-0-layout.md) | Covers the 2.0 walk model, Fit and Fill sizing, flow, spacing, padding, align, clipping, overlays, and scrollable containers. |
| [`2-0-widgets`](references/skills/2-0-widgets.md) | Chooses and composes 2.0 widgets, with the container rules, named children, list virtualization, dialogs, and custom drawing. |

### 2.0 animation and events

| Skill | What it does |
| --- | --- |
| [`2-0-animation`](references/skills/2-0-animation.md) | Builds 2.0 animators for hover, focus, pressed, and timeline states, with the widgets that support an animator and those that do not. |
| [`2-0-events`](references/skills/2-0-events.md) | Routes 2.0 events and actions across Splash inline handlers, Rust matching, widget actions, timers, and deferred work. |

### Live design fundamentals

| Skill | What it does |
| --- | --- |
| [`basics`](references/skills/basics.md) | Starts a Makepad app on the live_design generation: project structure, Cargo setup, app_main, button clicks, and widget access. |
| [`dsl`](references/skills/dsl.md) | Covers live_design DSL objects, prototypes, inheritance, widget instantiation, and the Rust struct link for the older generation. |
| [`layout`](references/skills/layout.md) | Covers the live_design layout properties, sizing, flow, alignment, centering, and the fixed plus flexible row pattern. |
| [`skills`](references/skills/skills.md) | An entry point to the Makepad skill collection, covering setup, patterns, shaders, packaging, and troubleshooting. |
| [`widgets`](references/skills/widgets.md) | Selects and styles live_design widgets, including View, Button, Label, Image, and TextInput, against the pinned version. |

### Live design runtime

| Skill | What it does |
| --- | --- |
| [`animation`](references/skills/animation.md) | Covers the live_design animator, hover and focus states, play and ease enums, and the Rust animator trait. |
| [`event-action`](references/skills/event-action.md) | Covers the live_design event enum, hit testing, action definition and emission, widget helpers, and timers. |
| [`font`](references/skills/font.md) | Covers Makepad text modules, font families and atlases, layout parameters, rasterizer settings, and DrawText. |
| [`shaders`](references/skills/shaders.md) | Covers Makepad draw_bg shaders, Sdf2d shapes, gradients, borders, built-in variables, and GLSL functions. |

### Platform and packaging

| Skill | What it does |
| --- | --- |
| [`deployment`](references/skills/deployment.md) | Packages and deploys Makepad apps for desktop, Android, iOS, and WASM, including resources, installers, and CI. |
| [`platform`](references/skills/platform.md) | Covers Makepad target platforms, OsType, conditional compilation, platform features, and entry points. |

### Diagnostics and scripting

| Skill | What it does |
| --- | --- |
| [`reference`](references/skills/reference.md) | A diagnostic entry point for Makepad build, widget, redraw, and layout issues against the exact runtime revision. |
| [`splash`](references/skills/splash.md) | Covers the Splash scripting language, script macro, functions, built-in objects, async work, and its unsandboxed execution boundary. |
## Group notes

### 2.0 DSL and layout

`2-0-dsl` covers the runtime `script_mod!` and Splash form. Properties use a colon, not
an equals sign. `:=` creates a named instance, `+:` merges, and `..` spreads. `let`
binds a local template. The module structure registers widget modules before the UI
modules that use them. The `Script` derive needs the script field, and non-instance
fields go before `#[deref]`. Three references back the body: `dsl-syntax-reference.md`,
`extended-guide.md`, and `property-system.md`.

`2-0-layout` covers the walk model. Width and height take Fit, Fill, or a size, and every
container View, SolidView, or RoundedView needs `height: Fit`. Flow sets the direction,
then spacing, padding, align, clip, and inset. An overlay uses `walk.abs_pos` or a margin,
and the coordinate space must be confirmed before converting a screen position. Scrollable
containers and filler spacers complete the page patterns.

`2-0-widgets` is the catalog. Containers, text, buttons, toggles, inputs, media, helpers,
lists, navigation, and the dock system. Named children use `:=`. A colored container that
holds text uses `new_batch`. List virtualization and dialogs have their own patterns. A
`MapView` needs a fixed height. Widget ids are stable, so keep them when editing.

### 2.0 animation and events

`2-0-animation` builds animators for hover, focus, pressed, and timeline states. It names
the widgets that support an animator and those that do not, and that support list is the
first check. A group holds a `from` block, a play type, an ease function, and an `apply`
block. A timeline uses keyframes. A loading spinner has its own pattern. The animator and
a vector tween are different tools, so pick deliberately.

`2-0-events` routes events and actions. Splash inline handlers cover `on_click`,
`on_render`, `on_return`, and `on_startup`. Rust handlers use the `MatchEvent` trait and
the standard app boilerplate. Widget actions differ per widget, so use the action the
installed widget actually emits. For a debounced search field, keep pending input,
cancel superseded timers, tag responses to reject stale updates, and test typing, empty
input, cancellation, focus changes, and teardown.

### Live design fundamentals

`basics` starts a live_design app. Project structure, `Cargo.toml`, `app_main!`, a button
click, and widget access. It names `references/app-structure.md` and
`references/event-handling.md`, which are not bundled, so resolve them before a step that
depends on them. Always include `use makepad_widgets::*;`.

`dsl` covers live_design objects. An anonymous object, a named prototype, inheritance
with an override, a widget instantiation, and the Rust struct link with `[derive(Live,
LiveHook, Widget)]`. It names `dsl-syntax.md` and `inheritance.md`, which are not
bundled. `layout` covers the older layout properties and patterns, including the basic
container, centering, a horizontal row, and a fixed plus flexible split. It names
`layout-system.md` and `core-types.md`. `widgets` covers View variants, Button variants,
Label, Image with its fit values, TextInput, and the full built-in list. It names three
widget references that are not bundled.

`skills` is the collection entry point over setup, patterns, shaders, packaging, and
troubleshooting. Use it to route, then open the specific skill. It does not replace the
specific body.

### Live design runtime

`animation` covers the live_design animator. Set `default:` for the initial state, then a
hover, multi-state, focus, or disabled pattern. It names `references/animation-system.md`,
which is not bundled. The Rust side uses the `AnimatorImpl` trait.

`event-action` covers the event enum, `handle_event`, hit testing, the action trait,
emission, handling, widget action helpers, the event flow, and timers. It names
`event-system.md` and `action-system.md`, which are not bundled.

`font` covers the text module, DSL font use, text style, theme fonts, the layouter API,
rasterizer settings, and DrawText properties. It names `font-system.md`, which is not
bundled.

`shaders` covers `draw_bg`, Sdf2d, rounded rectangles, borders, gradients, circles,
built-in variables, and GLSL functions. Set `show_bg: true` to enable the background
shader. It names `shader-basics.md` and `sdf2d-reference.md`, which are not bundled.

### Platform and packaging

`platform` covers macOS, Windows, Linux, Android, iOS, and WebGL2. It shows `OsType`,
platform detection, `cfg` attributes per target, platform-specific features, and the
entry point. It names `platform-support.md`, which is not bundled. Confirm the target
before promising a build.

`deployment` covers packaging. GitHub Actions, cargo-packager, `robius-packaging-commands`,
Cargo metadata, a pre-packaging resource copy, and the installer formats for Debian,
Windows NSIS, and macOS. It names a packaging action, an icon, and two widget resource
folders that are not bundled. `long_description` is limited to 80 characters per line.
Do not promise an IPA, APK, or installer that was not built and checked.

### Diagnostics and scripting

`reference` is the diagnostic entry point for build errors, widget behavior, redraw
issues, and layout problems. Run with line information for better messages, then open
the subsystem skill. It is a router, not a fix.

`splash` covers the Splash scripting language, the script macro, variables, functions,
control flow, console, http, and timer objects, widget interaction, and async work. It
names `splash-tutorial.md`, which is not bundled, and its API names are historical
dev-branch illustrations rather than compiled examples. Scripts are not assumed to be
sandboxed, so verify the runtime capabilities before evaluating reviewed code, and never
evaluate model-generated content.
