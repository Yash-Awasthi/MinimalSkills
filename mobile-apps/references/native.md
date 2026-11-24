# native

Load for SwiftUI, Jetpack Compose, native modules and device behavior.

## swiftui

- `@State` for view-local, `@Observable` for a model, `@Environment` for injection. A view model per screen, not per view.
- `NavigationStack` with a typed path. A boolean `isPresented` does not survive a deep link.
- `task` for async work tied to the view lifetime. Cancel on disappear.
- `List` with `id` from the model, never the index.
- Dynamic Type: test at the largest accessibility size; truncation is the usual break.

## compose

- State hoisting: the screen owns state, the component receives values and lambdas.
- `rememberSaveable` for values that survive rotation, `remember` for the rest.
- `LazyColumn` with a stable `key`. An inline lambda per row recomposes the list.
- `collectAsStateWithLifecycle`, not `collectAsState`, or work continues in the background.
- Edge to edge: handle insets, or the last row hides under the nav bar.

## native module boundary

```
TypeScript -> bridge -> native
```

- Validate in TypeScript, then again in native. The bridge does not enforce the type.
- One module, one responsibility. A module that fetches and renders is two modules.
- Errors cross the bridge as codes, not strings. A rejected promise without a code loses the cause.
- A permission prompt is not a grant. Handle denial, and handle "denied permanently" with a settings deep link.

## storage

| need | choice |
| --- | --- |
| small key-value, sync read | MMKV |
| relational, queryable | SQLite via `expo-sqlite` or Room |
| secrets | Keychain / Keystore, never AsyncStorage |
| files | app documents dir, backed up only if the user expects it |

AsyncStorage is unencrypted and slow for large values. Never a token store.

## push

1. Request permission at a point of value, not at launch.
2. Register, send the token to the server, store it per device and per user.
3. Dedupe on the server: the same token can arrive twice.
4. Handle foreground, background and cold start. A notification tap is a deep link.
5. Unregister on logout, or the next user receives the previous user's messages.

## device test

- Cold start with the network off.
- Background for 10 minutes, then return: state and timers.
- Rotate on every screen with a form.
- Low power mode: animations and background work.
- One device two OS versions behind the minimum.

## native module workflow (expo)

1. Scaffold: `npx create-expo-module@latest --local my-module`. `--local` keeps it in the repo, which a config plugin alone cannot do.
2. Implement the module per platform.
3. Register it in `expo-module.config.json`: `{"platforms":["ios","android"],"ios":{"modules":["MyModule"]}}`.
4. Call it from TypeScript and handle absence: `MyModule?.getBatteryLevel() ?? Promise.resolve(null)`.
5. Rebuild the dev client: `npx expo run:ios` or `run:android`. Expo Go cannot load a local module.
6. Test the failure path: a build without the module must degrade, not crash.

```swift
@objc(MyModule) public class MyModule: Module {
  public func definition() -> ModuleDefinition {
    Name("MyModule")
    AsyncFunction("getBatteryLevel") { () -> Int in 87 }
  }
}
```

```kotlin
class MyModule : Module() {
  override fun definition() = ModuleDefinition {
    Name("MyModule")
    AsyncFunction("getBatteryLevel") { 87 }
  }
}
```

A module that throws on the missing-permission path crashes the app instead of returning a value; wrap the platform call and return a typed error.
## platform index

| topic | the rule that matters |
| --- | --- |
| Flutter | `const` widgets, `ListView.builder` for long lists, `ValueNotifier` over `setState` for a single field; `flutter build appbundle` for Play. |
| Design system | One token file shared by Swift, Kotlin and RN; a colour defined in three places drifts on the first theme change. |
| ASO | Title carries the keyword, subtitle the benefit, screenshots show the first 3 seconds of value; a screenshot with a caption only is unreadable at thumbnail size. |
| Reverse engineering | `apktool d app.apk`, `jadx-gui` for decompilation, `frida` for runtime hooks; authorized targets only. |
