# expo guide

The long-form group prose and the full roster. `SKILL.md` is the loadable hub, and
`references/skills/<skill>.md` is the verbatim body to follow for one task.

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
