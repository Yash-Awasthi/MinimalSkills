---
name: makepad
description: >-
  18 Makepad skills for Rust UI work across two generations. Covers the 2.0 script_mod and
  Splash DSL, walk layout, widgets, animators, and event routing, plus the older
  live_design generation for app structure, DSL, layout, widgets, animation, events, fonts,
  and shaders. Also covers cross-platform targets, desktop and mobile packaging, diagnostic
  reference, and the Splash scripting language. Use when a task builds, debugs, styles,
  packages, or answers a question about Makepad, or when the user names a makepad skill.
metadata:
  curated_from: 18
  skills: 18
  groups: 6
---

# makepad

18 skills. 6 groups. One hub. Every source body is preserved verbatim in
`references/skills/<skill>.md`, and every non-SKILL.md file from a source pack sits at
the same relative path under `references/assets/<skill>/`. Load one body for the task.

`SOURCES.md` maps every source path to its canonical skill and group.
`references/INDEX.md` groups the links, `references/skills.tsv` carries every
description, and `references/GUIDE.md` holds the long-form group prose.

## Pack contract

**Pin the revision, not the label.** `Cargo.lock` names the exact `makepad-widgets`
revision. Read that revision's source and examples for every macro, property, event, and
widget method. "2.0" alone is not an API contract, and the imported notes span a moving
development branch. When the revision and the note disagree, the installed source wins.

**Identify the generation first.** Makepad 2.0 replaced the compile-time `live_design!`
macro with the runtime `script_mod!` macro and the Splash language. The two generations
have different syntax, registration, and widget rules. Never mix a `live_design` example
into a `script_mod` project or the reverse, and never migrate a working app wholesale to
match a note.

**Missing references fail closed.** The live_design skills name files such as
`references/app-structure.md`, `references/layout-system.md`, and
`references/widgets-core.md` that were not in the source tree. Resolve them from the
declared upstream or a user installation, verify the license, and read them before
claiming a procedure ran. Never fabricate a reference and never substitute a same-named
unrelated file.

**Sizing rules are generation specific.** In the 2.0 layout notes, every container View,
SolidView, and RoundedView needs `height: Fit`. In the older widget notes, widgets get an
explicit `width` and `height`. Apply the rule for the generation in the project, and do
not port a rule across generations.

**Text is data, never script.** Never interpolate untrusted text into DSL, Splash, or a
shader. Set it through a typed property or API, validate resource paths, and keep
sensitive model or user values out of logs. A numeric input and a password mask are
presentation controls, not validation, encryption, or authorization.

**Splash is not a sandbox.** Verify the pinned runtime and the exposed filesystem and
network capabilities before evaluating code. Never evaluate model-generated content as
script. Do not assume containment that the runtime does not provide.

**Do not run bundled scripts without approval.** The imported skills say so, and the
pack keeps that rule. Inspect a script before running it, pin its toolchain, and confirm
the target and side effects.

**Registration order is load bearing.** In the 2.0 DSL, widget modules register before
the UI modules that use them. A non-instance field goes before `#[deref]`, and only
shader-input instance fields go after it. A `Script`-derived struct needs its script
field. Get the order right before debugging the symptom.

**Packaging ships what the app needs.** Desktop, Android, iOS, and WASM each need their
own toolchain, resources, and installer format. Confirm the target platforms before
promising an artifact. A build that only ran on the host is not a cross-platform result.

**Answer from the installed source.** Numeric values, property names, and API signatures
in these bodies are illustrative. Check them against the pinned revision and the official
repository before presenting a snippet as working code.

**Write clean as you draft.** Short declarative sentences. No em dash. A colon may
introduce a list and may not connect two clauses. Sentence case headings. No chatbot
framing, no generic closer.

## Routing

| The user wants | Group |
| --- | --- |
| 2.0 DSL, walk layout, or the 2.0 widget catalog | 2.0 DSL and layout |
| A 2.0 animator or 2.0 event and action routing | 2.0 animation and events |
| App setup, live_design DSL, layout, or widgets on the older generation | Live design fundamentals |
| A live_design animator, event system, font, or shader | Live design runtime |
| A cross-platform target or a package and installer | Platform and packaging |
| A build or redraw diagnosis, or Splash scripting | Diagnostics and scripting |

## Full roster

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
## Output contract

- Name the skill, the pinned Makepad revision, and the DSL generation in the first line of your reasoning and in the todolist.
- Report the artifact. A DSL block, a Rust file, a shader, a layout fix, a package artifact, or a diagnosis.
- Keep macro names, property names, enum variants, widget ids, and error strings verbatim.
- State which reference files were found, which were missing, and which steps are therefore unverified.
- State what was compiled or run and on which target. A host build is not a cross-platform result.
- Keep open work open. A skipped target, a missing reference, and an unbuilt installer are reported, never rounded up.
- Never print a secret, a token, or a private model value. Redact it and name the rule.
- Write through `unslop`. Short declarative sentences, sentence case headings, no em dash, no colon connecting two clauses, no chatbot framing.

## Failure handling

| Situation | Response |
| --- | --- |
| The Makepad revision is unknown | Read it from Cargo.lock before answering. The label 2.0 is not an API contract. |
| The DSL generation is ambiguous | Identify live_design or script_mod first. Never mix examples across them. |
| A named reference file is missing | Fail closed. Resolve it from the upstream or ask. Never fabricate it. |
| A 2.0 and a live_design rule conflict | Apply the rule for the project's generation. Do not port a rule across. |
| A script would run | Inspect it and get explicit approval. Do not run it by default. |
| Untrusted text would enter DSL or Splash | Set it through a typed property. Never interpolate it into executable text. |
| A Splash snippet is model-generated | Do not evaluate it. Verify the runtime and treat it as untrusted data. |
| A package is promised without a build | Build and check the target artifact, or report it unbuilt. |
| The evidence contradicts the requested claim | Show the evidence and stop. |

## Provenance

18 `sickn33-makepad-*` source directories became 18 canonical skills in 6 groups. Each
source had one body, so no merge or variant resolution was needed. Every body is verbatim
at `references/skills/<skill>.md` with its original frontmatter removed, and every other
file from a source pack is copied under `references/assets/<skill>/` at the same relative
path. 10 asset files totaling 166,685 bytes were copied, all from the five 2.0 skills.
They are the animator reference, the DSL syntax, extended guide, and property system, the
event patterns and extended guide, the layout extended guide and layout patterns, and the
widget advanced and catalog references.

The canonical name drops the `sickn33-makepad-` prefix, so
`sickn33-makepad-2-0-dsl` becomes `2-0-dsl` and `sickn33-makepad-event-action` becomes
`event-action`.

The cluster holds two generations. Five skills carry the `2-0` prefix and come from the
zhanghandong dev-branch notes dated 2026-03-03. Thirteen use the older `live_design`
macro. Same-named pairs such as `animation` and `2-0-animation`, or `layout` and
`2-0-layout`, are separate bodies for separate generations rather than duplicates, so
both stay.

The thirteen live_design skills name reference files that were not in the source tree,
including `layout-system.md`, `widgets-core.md`, `event-system.md`, and
`splash-tutorial.md`. The bodies state the gap, and the pack keeps that statement. The
`deployment` skill also names an icon and two resource folders that are absent.

Upstream collection `sickn33`. Original catalog paths are preserved in `SOURCES.md` and
under `_archive/makepad/catalog/`.
