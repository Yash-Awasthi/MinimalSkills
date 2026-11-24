---
name: expo
description: >-
  13 Expo skills. Covers native UI with `@expo/ui` across universal, SwiftUI, and Jetpack
  Compose paths, an animation decision sequence, Expo Router API routes on EAS Hosting, a
  development client, EAS workflow YAML, release builds and store submission, brownfield
  integration into a native host, native modules and views, Tailwind v4 with NativeWind v5,
  the official `with-*` example catalog, and EAS Observe. Use when a task builds, animates,
  routes, builds, releases, embeds, extends, styles, or observes an Expo or React Native
  app, or when the user names an expo skill.
metadata:
  curated_from: 13
  skills: 13
  groups: 6
---

# expo

13 skills. 6 groups. One hub. Every source body is preserved verbatim in
`references/skills/<skill>.md`, and every non-SKILL.md file from a source pack sits at
the same relative path under `references/assets/<skill>/`. Load one body for the task.

`SOURCES.md` maps every source path to its canonical skill and group.
`references/INDEX.md` groups the links, `references/skills.tsv` carries every
description, and `references/GUIDE.md` holds the long-form group prose.

## Pack contract

**The SDK version is part of the API.** `@expo/ui` works in Expo Go on SDK 56 but needs a
development client on older SDKs, and the SwiftUI and Jetpack Compose skills apply to SDK
55 only. Read the installed SDK, the Expo version, and the package version before copying a
component or a flag. A body that names one SDK is not a promise about another.

**A build and a submission are separate authorized actions.** An EAS build consumes build
minutes and may cost money. A submit uploads a binary to App Store Connect or Google Play,
and a store version number cannot be reused. Confirm the profile, the platform, the version,
the credentials, and the target before either. Never submit, promote, or release because a
local build passed.

**A server route is the only place for a secret.** An API route keeps a key, a database
credential, or a third-party token out of the client bundle. Validate and sanitize every
input on the server, because a client check is not a control. Never bundle a secret into
client code, and never log a token or a request body that carries one.

**A header is not authentication.** A presence check, a nonempty password, or a decoded
token without a signature check authenticates nobody. Verify the token with the identity
provider, enforce per-user authorization, and fail closed until the check is implemented. A
CORS header does not replace authorization.

**Do not run `prebuild --clean` on a hand-maintained host.** A brownfield app has native
code the generator does not know about. Take a clean baseline, work on a topic branch, and
keep a separate generated workspace for isolated artifacts. A clean prebuild can delete
custom native code, and the deletion is not always recoverable.

**Module code crosses a native boundary.** A native module runs with the app's full
authority. Validate an input in TypeScript and again at the native edge, request the
narrowest platform permission, and handle a denial. A permission prompt is not a grant, and
a simulator result is not a device result.

**Telemetry carries personal data.** Observe sends device, session, route, and custom-event
data to a backend. Inspect the route parameters and event properties for a token, an
identifier, or personal data before collection, minimize or redact the payload, and get
consent where the regime requires it. A metric name or a route path stays verbatim.

**Animation needs a reason and an accessibility path.** Run the gate before writing code.
Do not animate something that should not animate, never start from `scale(0)`, never
animate a `BlurView` intensity on Android, and keep continuous or interruptible values off
the JS thread. Honor reduced motion, and use haptics only where they add meaning. A spinner
does not fix a slow operation.

**Examples are reference integrations, not apps.** The `with-*` projects are managed,
roughly one screen, and pinned to their own versions. In inspiration mode, study without
touching the user's project. In scaffold mode, create a new project. Adapt into an existing
app non-destructively, with a diff, and check the config plugin and the permission list.

**Local success is not a release.** A Metro build, a simulator run, and a preview URL do not
prove a store build, a native module on a device, or an API route under production secrets.
State the exact target that was built and tested.

**Write clean as you draft.** Short declarative sentences. No em dash. A colon may
introduce a list and may not connect two clauses. Sentence case headings. No chatbot
framing, no generic closer.

## Routing

| The user wants | Group |
| --- | --- |
| A native or universal control, or an animation decision and implementation | UI and animation |
| A server endpoint, a secret, a database call, or an API proxy | Routing and backend |
| A development client, an EAS workflow, or a store release | Build and release |
| Expo embedded in a native app, or a native module and view | Native integration |
| Tailwind v4 with NativeWind v5 | Styling |
| A `with-*` integration example, or EAS Observe telemetry | Examples and diagnostics |

## Full roster

### UI and animation

| Skill | What it does |
| --- | --- |
| [`animation`](references/skills/animation.md) | Builds Expo animations with a gate before any code, the cheapest tool that works, off-thread properties, haptics, and reduced motion. |
| [`ui`](references/skills/ui.md) | Builds native UI with `@expo/ui`: universal Host, Column, Row, Button, Text, and List components, with SwiftUI and Jetpack Compose drop-ins. |
| [`ui-jetpack-compose`](references/skills/ui-jetpack-compose.md) | Builds Android-native Expo SDK 55 UI with Jetpack Compose views and modifiers, Host sizing, and the native rebuild prerequisite. |
| [`ui-swift-ui`](references/skills/ui-swift-ui.md) | Builds iOS-native Expo SDK 55 UI with SwiftUI views and modifiers, Host and RNHostView embedding, and the native rebuild prerequisite. |

### Routing and backend

| Skill | What it does |
| --- | --- |
| [`api-routes`](references/skills/api-routes.md) | Creates Expo Router API routes on EAS Hosting for server secrets, database work, third-party proxies, and server-side validation. |

### Build and release

| Skill | What it does |
| --- | --- |
| [`cicd-workflows`](references/skills/cicd-workflows.md) | Writes and validates EAS workflow YAML under `.eas/workflows/`, with job types, triggers, expressions, and the fetch and validate helpers. |
| [`deployment`](references/skills/deployment.md) | Builds and submits iOS and Android releases with EAS, manages versions and store metadata, and deploys web bundles and API routes. |
| [`dev-client`](references/skills/dev-client.md) | Builds an EAS development client for testing native changes on a device, with distribution, local build, install, and status steps. |

### Native integration

| Skill | What it does |
| --- | --- |
| [`brownfield`](references/skills/brownfield.md) | Integrates Expo and React Native into an existing native iOS or Android app through the isolated or the integrated approach. |
| [`module`](references/skills/module.md) | Creates Expo native modules and views with the Expo Modules API across Swift, Kotlin, and TypeScript, including config and lifecycle. |

### Styling

| Skill | What it does |
| --- | --- |
| [`tailwind-setup`](references/skills/tailwind-setup.md) | Sets up Tailwind CSS v4 in Expo with react-native-css and NativeWind v5 for iOS, Android, and web. |

### Examples and diagnostics

| Skill | What it does |
| --- | --- |
| [`examples`](references/skills/examples.md) | Finds, studies, and adapts one of the roughly 70 `with-*` integrations in the expo/examples repository without touching the host project. |
| [`observe`](references/skills/observe.md) | Adds and queries EAS Observe for startup, navigation, custom-event, trace, and log performance data, with payload redaction. |

## Group notes

### UI and animation

`ui` is the universal entry. `Host`, `Column`, `Row`, `Button`, `Text`, `List`, and the
other cross-platform components, then the drop-in replacements for migrating off a React
Native community UI library. Start universal, and drop to SwiftUI or Jetpack Compose only
when the universal layer falls short. On SDK 56 it runs in Expo Go. On an older SDK, build
a development client first.

`ui-jetpack-compose` is the Android-native path for SDK 55. Choose a Compose view or
modifier, size it inside `Host`, and rebuild natively with `npx expo run:android`. The
reference set in `ui` includes the Compose guide. The skill applies to SDK 55 only.

`ui-swift-ui` is the iOS-native path for SDK 55. Choose a SwiftUI view or modifier, wrap the
tree in `Host`, embed React Native with `RNHostView`, and rebuild with
`npx expo run:ios`. A missing view or modifier can be added through a local Expo module,
and the body says to confirm that extension with the user first.

`animation` is the decision sequence from Emil Kowalski. Ask whether the element should
animate at all, what the purpose is, and which tool is the cheapest that works. A screen
transition uses the native stack options in Expo Router. Pull to refresh uses
`RefreshControl` unless the interaction is a signature. A press scale is a transition, a
drag is a shared value. Bounce only when the gesture carried momentum. Never `scale(0)`,
never animate `BlurView` intensity on Android, keep work off the JS thread, respect reduced
motion, and use haptics sparingly. Recipes, a license, and an agent manifest are bundled.

### Routing and backend

`api-routes` creates an Expo Router route on EAS Hosting. Use one for a server secret, a
database operation, a third-party proxy, or server-side validation. Do not use one for
static data or a client-safe operation. The body covers the file structure, HTTP methods,
dynamic routes, query parameters, headers, JSON bodies, environment variables, CORS, error
handling, local testing, and deployment. Header presence and a nonempty password field do
not authenticate. Implement token verification and per-user authorization, and fail closed
until they exist. The agent manifest is bundled.

### Build and release

`dev-client` builds a development client with EAS. Use one when a native library or a
native change cannot run in Expo Go, and prefer it for a real app. The body covers the EAS
configuration, distribution choice, a local iOS or Android build, installing the artifact,
the platform filter, build status, starting Metro, and troubleshooting. `xcodebuild` and
`ideviceinstaller` are local paths with their own prerequisites.

`cicd-workflows` writes EAS workflow YAML under `.eas/workflows/`. The top-level `on` and
`jobs` keys, job types and their required and optional parameters, expressions, generation,
and validation. The fetch and validation helpers are bundled. Do not rely on memorized
values, because the job schema evolves. A workflow that deploys is a deployment, so confirm
its trigger and its target.

`deployment` covers the release. Install and initialize the EAS CLI, configure `eas.json`
build and submit profiles, build for iOS and Android, submit to App Store Connect and Google
Play, use the TestFlight shortcut, and deploy a web bundle or an API route. It also covers
versions, build numbers, store metadata, and ASO. The iOS, Play Store, TestFlight, metadata,
and workflow references are bundled. A submission is irreversible at the version level, so
confirm the binary and the version first.

### Native integration

`brownfield` embeds React Native in an existing native app. Choose the isolated approach,
which builds an AAR or XCFramework in a separate workspace, or the integrated approach,
which adds the React Native dependencies to the host build. The two approach references,
the comparison, and the troubleshooting guide are bundled. Take a baseline, work on a topic
branch, and never run `prebuild --clean` on hand-maintained host projects. Preserve the
native host and its custom code.

`module` writes an Expo native module or view in Swift, Kotlin, and TypeScript. The module
DSL, native views, shared objects, config plugins, lifecycle hooks, autolinking, and the
type system. Seven references are bundled, from create and config to native module, native
view, and lifecycle. Scaffold with the official tool, keep the config in
`expo-module.config.json`, and validate on a device. The skill states the native
integration limits.

### Styling

`tailwind-setup` installs Tailwind CSS v4 with `react-native-css` and NativeWind v5 for
iOS, Android, and web. The dependencies, the Metro, PostCSS, and global CSS configuration,
the CSS component wrappers for view, text, image, and animated components, custom theme
variables, platform-specific styles, Apple system colors, and the differences from
NativeWind v4 and Tailwind v3. No Babel config is needed. Rebuild and check each platform,
because a web-only pass does not prove the native path.

### Examples and diagnostics

`examples` works from the expo/examples repository of roughly 70 `with-*` integrations. Use
inspiration mode to study without touching the project, or scaffold mode to create a new
one. Find the example, read `README.md`, `package.json`, `app.json`, the integration code,
and `.env` in that order. Adapt into the user's app non-destructively. The example catalog
and the alias and deprecation notes are bundled. The projects are single-screen references,
not full apps.

`observe` adds EAS Observe. The `AppMetricsRoot` or `ObserveRoot` wrapper, `markInteractive`,
the `useObserve` hook, and the Expo Router and React Navigation integrations for per-route
metrics. Query with the CLI summary, traces, and logs. The setup, metrics, and query
references are bundled. Collection sends device and event data to the configured backend,
so inspect the route parameters and event properties for personal data and redact before
enabling it.
## Output contract

- Name the skill, the Expo SDK and package version, and the target platform in the first line of your reasoning and in the todolist.
- Report the artifact. A component, an animation, a route, a workflow file, a build, a submit, a module, a style config, or a trace.
- Keep package names, SDK versions, config keys, route paths, and error text verbatim.
- State which platform and which build target were actually run, and which remain unbuilt.
- State the credentials scope and the store or hosting target behind a deploy or submit.
- Keep open work open. An unbuilt platform, an unauthenticated route, and an unredacted event are reported, never rounded up.
- Never print a token, a signing key, a private env value, or personal telemetry. Redact it and name the rule.
- Write through `unslop`. Short declarative sentences, sentence case headings, no em dash, no colon connecting two clauses, no chatbot framing.

## Failure handling

| Situation | Response |
| --- | --- |
| The SDK version is unknown | Read it before copying a component or a flag. `@expo/ui` behavior differs by SDK. |
| A build or submit was not authorized | Stop. Confirm the profile, platform, version, credentials, and target. |
| A secret would reach client code | Move it to an API route and keep it out of the bundle. |
| A route checks a header but verifies nothing | Implement token verification and per-user authorization, and fail closed. |
| A brownfield host would get `prebuild --clean` | Do not run it. Use a separate workspace and a topic branch. |
| A native module trusts client input | Validate again at the native edge and scope the permission. |
| Telemetry would collect a token or personal data | Redact or minimize before enabling collection. |
| An animation starts from `scale(0)` | Start from 0.9 to 0.97 with opacity 0 and respect reduced motion. |
| A `with-*` example would overwrite the host app | Adapt non-destructively and show the diff. |
| A simulator pass is called a release | Name the exact target that was built and tested. |
| The evidence contradicts the requested claim | Show the evidence and stop. |

## Provenance

13 `sickn33-expo-*` source directories became 13 canonical skills in 6 groups. Each source
had one body, so no merge or variant resolution was needed. Every body is verbatim at
`references/skills/<skill>.md` with its original frontmatter removed, and every other file
from a source pack is copied under `references/assets/<skill>/` at the same relative path.
38 asset files totaling 197,657 bytes were copied. The largest sets are the seven `module`
references, the six `deployment` store and workflow references, the six `ui` guides and
the component list script, and the five `brownfield` approach and troubleshooting
references. The two SDK 55 platform skills, `ui-jetpack-compose` and `ui-swift-ui`, ship no
extra files.

The canonical name drops the `sickn33-expo-` prefix, so `sickn33-expo-api-routes` becomes
`api-routes` and `sickn33-expo-ui-jetpack-compose` becomes `ui-jetpack-compose`.

The three UI skills overlap by design. `ui` is the current universal layer, while
`ui-jetpack-compose` and `ui-swift-ui` are the SDK 55 platform paths. All three stay,
because each carries a different version and component rule. `animation` keeps the gate,
the `scale(0)` ban, the Android `BlurView` rule, and the reduced-motion requirement.

The API route body says that fragments are incomplete demos and that a header or a nonempty
password does not authenticate. The brownfield body bans `prebuild --clean` on a
hand-maintained host. The observe body requires payload inspection and redaction. The pack
keeps all three boundaries.

Upstream collection `sickn33`. Original catalog paths are preserved in `SOURCES.md` and
under `_archive/expo/catalog/`.
