# expo

Load for Expo SDK work, config plugins, dev clients and EAS.

## version matrix

| package | behavior |
| --- | --- |
| `@expo/ui` | works in Expo Go on SDK 56, needs a dev client on older SDKs |
| SwiftUI and Compose paths | apply to SDK 55 only |
| `expo-router` | file routes, typed hrefs, modal presentation per route |
| `expo-updates` | runtime version must match the build or the update is rejected |

Read the installed SDK before copying a component or a flag. A body that names one SDK is not a promise about another.

```bash
npx expo config --type public
npx expo install --check
```

`expo install` picks the version matched to the SDK. `npm install` picks latest and breaks the matrix.

## go versus dev client

- Expo Go: no custom native code, fast iteration, one SDK at a time.
- Dev client: any native module, a build per platform, slower loop.
- Switch when a package has a config plugin or a native dependency. Check the package readme for the phrase "requires a development build".

## config plugins

```json
{
  "expo": {
    "plugins": [["expo-camera", { "cameraPermission": "Scan invoices" }]],
    "ios": { "infoPlist": { "NSCameraUsageDescription": "Scan invoices" } }
  }
}
```

- A plugin edits native files at prebuild. Two plugins touching one file can conflict.
- The permission string is what the store reviewer reads. Match it to the feature.
- After adding a plugin: `npx expo prebuild` then a new build. A JS reload does not apply it.

## prebuild safety

`prebuild --clean` regenerates the native folders and deletes hand edits. On a brownfield app: topic branch, a clean baseline commit, and a diff review after prebuild. Keep a generated workspace separate from the maintained one.

## eas

| profile | use |
| --- | --- |
| development | dev client, internal distribution |
| preview | internal testers, ad hoc |
| production | store binary, credentials from the store |

```bash
eas build:list --limit 5
eas build --profile preview --platform ios
eas update --branch production --message "fix invoice scan"
```

- `eas.json` holds the profiles, not the secrets. Credentials live in the EAS store.
- A build number must increase. Reusing a store version is rejected.
- An update ships JS only. A native change needs a new binary and a new runtime version.

## common failures

| error | cause |
| --- | --- |
| native module not found | Expo Go, no dev client |
| invariant violation, new arch | a package without new-architecture support |
| white screen after update | runtime version mismatch |
| android build fails on plugin | plugin expects a newer SDK |
| metro cannot resolve | cache: `npx expo start -c` |
