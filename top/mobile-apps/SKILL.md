---
name: mobile-apps
description: >
  One standalone skill for mobile development: Expo end to end (native UI
  with @expo/ui, animation decision sequence, Expo Router API routes on EAS
  Hosting, development client, EAS workflow YAML, release builds and store
  submission, brownfield integration, native modules and views, Tailwind v4
  with NativeWind v5, the with-* example catalog, EAS Observe), Swift and
  SwiftUI (concurrency, liquid glass, performance audit, refactoring), Kotlin
  and Jetpack Compose (coroutines, idiomatic efficiency), Flutter, iOS and
  Android platform work, app clips, ASO, Appium automation, and mobile
  reverse engineering. Merges the mobile class (40 skills) and the expo deep
  pack (13). Fully self-contained: every procedure is inline, no external
  references.
metadata:
  merges: mobile
  sources: 40
---

# mobile-apps

## 0. Iron laws (expo pack contract — bind everything below)

1. **The SDK version is part of the API.** `@expo/ui` works in Expo Go on
   SDK 56 but needs a development client on older SDKs, and the SwiftUI and
   Jetpack Compose skills apply to SDK 55 only. Read the installed SDK, the
   Expo version and the package version before copying a component or a
   flag. A body that names one SDK is not a promise about another.
2. **A build and a submission are separate authorized actions.** An EAS
   build consumes build minutes and may cost money. A submit uploads a
   binary to App Store Connect or Google Play, and a store version number
   cannot be reused. Confirm the profile, platform, version, credentials
   and target before either. Never submit, promote or release because a
   local build passed.
3. **A server route is the only place for a secret.** An API route keeps a
   key, a database credential or a third-party token out of the client
   bundle. Validate and sanitize every input on the server — a client check
   is not a control. Never bundle a secret into client code, and never log
   a token or a request body that carries one.
4. **A header is not authentication.** A presence check, a nonempty
   password or a decoded token without a signature check authenticates
   nobody. Verify the token with the identity provider, enforce per-user
   authorization, and fail closed until the check is implemented. A CORS
   header does not replace authorization.
5. **Do not run `prebuild --clean` on a hand-maintained host.** A brownfield
   app has native code the generator does not know about. Take a clean
   baseline, work on a topic branch, and keep a separate generated
   workspace for isolated artifacts. A clean prebuild can delete custom
   native code, and the deletion is not always recoverable.
6. **Module code crosses a native boundary.** A native module runs with the
   app's full authority. Validate an input in TypeScript and again at the
   native edge, request the narrowest platform permission, and handle a
   denial. A permission prompt is not a grant, and a simulator result is
   not a device result.
7. **Telemetry carries personal data.** Observe sends device, session,
   route and custom-event data to a backend. Inspect the route parameters
   and event properties for a token, an identifier or personal data before
   collection; minimize or redact the payload; get consent where the regime
   requires it. A metric name or a route path stays verbatim.
8. **Animation needs a reason and an accessibility path.** Run the gate
   before writing code. Do not animate something that should not animate,
   never start from `scale(0)`, never animate a `BlurView` intensity on
   Android, and keep continuous or interruptible values off the JS thread.
   Honor reduced motion; use haptics only where they add meaning. A spinner
   does not fix a slow operation.
9. **Examples are reference integrations, not apps.** The `with-*` projects
   are managed, roughly one screen, and pinned to their own versions. In
   inspiration mode, study without touching the user's project. In scaffold
   mode, create a new project. Adapt into an existing app non-destructively,
   with a diff, and check the config plugin and the permission list.
10. **Local success is not a release.** A Metro build, a simulator run and
    a preview URL do not prove a store build, a native module on a device
    or an API route under production secrets. State the exact target that
    was built and tested.

## 1. Expo (13 skills, 6 groups)

- **UI and animation** (expo-ui, animate-expo): native and universal
  controls across the universal, SwiftUI and Jetpack Compose paths; the
  animation decision sequence with the gate of law 8.
- **Routing and backend** (expo-router-api-routes, eas-hosting): API routes
  on EAS Hosting with the secret rule of law 3.
- **Build and release** (development-client, eas-workflows, eas-app-stores,
  eas-simulator): workflow YAML; release builds; store submission with the
  law-2 authorization split; simulator runs.
- **Native integration** (brownfield, native-modules, native-views):
  brownfield embedding with the prebuild rule of law 5; modules and views
  with the boundary rule of law 6.
- **Styling** (nativewind): Tailwind v4 with NativeWind v5, version-locked.
- **Examples and diagnostics** (with-* catalog, eas-observe,
  eas-update-insights, upgrading-expo): the example catalog in inspiration
  or scaffold mode; telemetry with the law-7 privacy rule; update insights;
  upgrade guides with references.

## 2. iOS and Swift

- **Swift language** (swift, write-swift, swift-concurrency-expert):
  idiomatic efficiency reference; initial-response discipline; structured
  concurrency with actors, tasks and cancellation.
- **SwiftUI** (swiftui-expert-skill, swiftui-ui-patterns, swiftui-liquid-
  glass, swiftui-performance-audit, swiftui-view-refactor, update-swiftui-
  apis): patterns with quick starts; the Liquid Glass design language;
  performance audits; view refactoring; API updates with version checks.
- **iOS platform** (ios-developer, ios-debugger-agent, add-app-clip): do-
  not-use cases stated; debugging workflows; App Clips with when-to-use.
- **iOS design** (ios-flows, ios-screens, ios-review): UXKIN-derived flows,
  screens and reviews with stated boundaries.

## 3. Android and Kotlin

- **Kotlin** (kotlin, kotlin-coroutines-expert): idiomatic efficiency;
  coroutines with structured concurrency and flow.
- **Compose** (android-jetpack-compose-expert): composable design, state
  hoisting, recomposition discipline.
- **Platform** (android-dev, android-cli, android_ui_verification,
  diagnose-android-overheating): detailed-guide development; CLI
  specialization; UI verification with when-to-use; thermal diagnosis with
  measurement first.

## 4. Cross-platform and QA

- **Flutter** (flutter-expert): use and do-not-use cases stated.
- **React Native** (vercel-react-native-skills, mobile-developer): when to
  apply; general mobile development with do-not-use cases.
- **Design system** (mobile-design): scope and risk stated first.
- **Mobile games** (mobile-games): platform considerations — touch targets,
  battery, thermal, store policies. (game-dev hub carries the depth.)
- **Testing** (appium-skill): automation with device matrix and desired
  capabilities discipline.
- **ASO** (app-store-optimization): scope, evidence and safe use stated —
  keyword and metadata advice based on observable store data, not
  guaranteed rankings.

## 5. Security boundary

- **Reverse engineering** (mobile-reverse): analyze only apps you own or
  are authorized to test; jailbroken-device techniques carry their own
  legal boundaries; findings feed the security-operations hub.
- **Secrets and auth**: laws 3 and 4 apply to every mobile backend call;
  the mobile-security-xss-scan discipline lives in the frontend hub.

## 6. Cross-carried fragments

- **Desktop Apple** (macos-menubar-tuist-app, macos-spm-app-packaging):
  Tuist menubar apps; SwiftPM packaging without Xcode — prerequisites
  stated.
- **Design** (mobile UI styles): the named styles live in the design-ux
  hub §2; spatial computing UI in the writing-docs fragments.
- **Backend** (API routes): server-side patterns live in the backend-api
  hub.

## 7. Output contract

- Name the skill, the platform and SDK version, and the app target in the
  first line of reasoning and in the todo list.
- Report the artifact: a build profile result, a submitted version, an API
  route, a native module, a component, a test run.
- Keep SDK versions, package versions, permission names, route paths and
  error strings verbatim.
- State what was built and on which target. A simulator result is not a
  device result; a local build is not a release.
- State the animation gate decision and the accessibility path.
- Keep open work open: an unverified device behavior, a missing permission
  denial path and an untested route are reported, never rounded up.
- Never print a token, secret or personal data; redact and name the rule.

## 8. Failure handling

| Situation | Response |
| --- | --- |
| The SDK or package version is unknown | Read it first; never copy across versions. |
| A submission is proposed after a local build | It is a separate authorized action; confirm the target. |
| A secret would enter client code | Move it to a server route; never bundle it. |
| Auth rests on a header or a decoded token | Verify the signature and enforce authorization; fail closed. |
| `prebuild --clean` on a brownfield host | Refuse; use the baseline and topic-branch procedure. |
| A native module input is unvalidated | Validate in TypeScript and at the native edge. |
| A permission prompt is treated as a grant | It is not; handle the denial. |
| Telemetry would carry a token or personal data | Minimize or redact before collection. |
| An animation has no reason or accessibility path | Run the gate first; do not animate. |
| A `with-*` example is adapted destructively | Adapt non-destructively with a diff. |
| The evidence contradicts the requested release | Show the evidence and stop. |

## Provenance

Merged from the mobile class (40 catalog skills) and the expo curated pack
(13 sources, 6 groups). Every source skill's procedure, rule and policy is
represented above; duplicates collapsed to one canonical statement;
authorization splits, native-boundary and fail-closed rules preserved. No
external file is required to use this skill.
