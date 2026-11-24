---
name: mobile-apps
description: Use when building or shipping a mobile app: Expo SDK and React Native structure, navigation, native modules and permissions, SwiftUI and Jetpack Compose screens, offline storage, push, EAS build and store submission, device QA. Triggers: Expo, React Native, SwiftUI, Compose, TestFlight, EAS.
---

# mobile-apps

## use when

- Expo SDK, config plugin, dev client -> references/expo.md
- SwiftUI screen, Compose screen, native module -> references/native.md
- offline storage, sync, push notification
- EAS build, TestFlight, Play submission, crash on one os version

not for: web ui patterns (frontend-ui), server endpoints (backend-api)

## rules

- Conflict order: crash-free launch, then offline correctness, then animation.
- The SDK version is part of the API; `@expo/ui` needs a dev client below SDK 56, so read the version first.
- Build and submit are separate actions: EAS build spends minutes, submit uploads a binary whose version cannot be reused.
- A secret belongs in an API route, never in the bundle; a mobile binary is public.
- `prebuild --clean` deletes native code the generator does not know about; never on a brownfield app.
- A native module runs with the app's full authority: validate at the TypeScript edge and at the native edge.

## change

1. Locate: the screen, its navigator, and the native module or permission it calls.
2. Propose the change in one sentence, with the alternative you rejected.
3. Predict before building: cold start, offline path, the SDK versions affected.
4. Back up the original screen and native config in context, pinned to `git rev-parse HEAD`.
5. Apply one concern per edit; a UI change and a permission change are two builds.
6. Verify: a dev-client build on a mid-range device, network off, cold start under 2s.
7. Regress: every screen reaching the module, the deep link and one OS two versions back.
8. Compare the device run against the prediction; a crash on either OS stops the build.
9. Report the device, OS version and what ran only in a simulator, then continue.

## build

1. Read the versions before writing a component.

   ```bash
   npx expo --version && npx expo config --type public | head -30
   ```

2. Navigation: tabs top level, stack detail, modal for one task. One navigator owner, or deep links break.
3. Data: cache first, network second. An offline write is queued with a key the server can dedupe.

   ```ts
   async function saveInvoice(input: Invoice) {
     const key = crypto.randomUUID();          // stable across retries
     await db.queue.put({ key, input, tries: 0 });
     if (await online()) return flush();       // same key on replay, server dedupes
   }
   ```

4. Permissions at the point of use, narrowest scope, denial path rendered.
5. Animation: never from `scale(0)`, never animate `BlurView` intensity on Android, keep continuous values off the JS thread.
6. Run on a mid-range device, network off: cold start to first frame, 10 min background then return, rotate a form, low power, one OS two versions behind.
7. Build, then submit the same binary.

   ```bash
   eas build --profile production --platform all
   eas submit --platform ios --latest
   ```

   `eas.json` profile: `{"build":{"production":{"channel":"production","autoIncrement":true}}}`. `autoIncrement` prevents the version reuse that fails a submit.

## decide

| condition | action |
| --- | --- |
| screen needs a native api | config plugin or native module, never a hack |
| works in Expo Go but not a build | version mismatch, check the SDK matrix |
| list over 50 rows | `FlashList`, stable key, no inline render |
| offline write | queue with idempotency key, replay on reconnect |
| push needed | token lifecycle plus server-side dedupe |

## check

- [ ] cold start under 2s on a mid-range device
- [ ] every screen renders offline and empty
- [ ] permission denial path handled
- [ ] deep link resolves to the same screen as in-app
- [ ] no secret in the bundle: `rg -i "sk-|api_key" dist/`

## stop

| condition | action |
| --- | --- |
| store policy conflict | surface it before coding |
| native module needs a paid account | ask first |
| signing credentials missing | ask the owner |
| submit requested without a device test | refuse until installed |

## emit

- screens and modules changed, with SDK version
- device and os version tested, and what ran only in a simulator
