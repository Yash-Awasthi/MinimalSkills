---
name: game-dev
description: Use when building a game: engine choice, core loop and progression, 2D and 3D rendering with GLSL shaders, Bevy ECS, art and audio direction, multiplayer netcode, target platforms, performance budgets, scope estimation. Triggers: Unity, Unreal, Godot, shader, netcode, game loop.
---

# game-dev

## use when

- choose an engine or a framework
- design the core loop, difficulty, progression
- 2D, 3D, rendering, shader work -> references/rendering.md
- art, audio, animation pipeline
- multiplayer architecture and state sync
- platform build: web, mobile, pc, console, vr

not for: general app ui (frontend-ui), server endpoints (backend-api)

## rules

- Conflict order: frame budget, then scope, then polish; a cut feature outranks a dropped frame.
- Engine choice follows answers, not a demo: scope, shipped engine, platforms, frame budget, monetization.
- Every feature names the loop step it serves; one that serves none is cut before production art.
- Platform limits are budgets: 44px touch targets, 3-5 minute mobile sessions, 90fps on vr, certification before content lock.
- One art style governs ui, characters and environment; a second is a scope decision with its own cost.
- A netcode claim states tick rate, latency and loss; a localhost demo states neither.

## change

1. Locate: the system, its update order in the frame, and every scene or prefab that uses it.
2. Propose the gameplay or render change in one sentence, with the alternative you rejected.
3. Predict before running: frame time delta, draw calls, which loop step improves.
4. Back up the original system file in context, pinned to `git rev-parse HEAD`.
5. Apply one concern per edit; a balance tweak and a shader change are two edits.
6. Verify: frame time on the target device, then one playthrough of the affected loop.
7. Regress: every scene using the system, the platform build and the netcode latency test.
8. Compare the profile against the prediction; an unplanned frame cost stops the change.
9. Report frame time and the device measured on, then take the next item.

## loop

1. Define the loop in one sentence: action, feedback, reward.
2. Set the session length: 3-5 minutes on mobile, 20-40 on pc, and the first 30 seconds.
3. Prototype with placeholder art; watch 5 people play the first minute, note where they stop.
4. Add difficulty curve and progression only after the loop holds.
5. Budget the frame: draw calls, triangles, texture memory, gc.

```bash
Unity -quit -batchmode -projectPath . -executeMethod Build.Perf
godot --headless --export-release "Linux/X11" build/game
```

## decide

| condition | action |
| --- | --- |
| team knows one engine | use it unless it blocks a platform |
| web target | check the shell, asset budget and input latency first |
| mobile target | thermal and battery budget before visual ambition |
| vr target | 90fps floor and comfort rules before content |
| multiplayer needed | authoritative server or lockstep, chosen explicitly |
| scope over 6 months | cut a mode, not the polish |

## render

1. Budget the frame first: 16.6ms at 60, 33.3ms at 30, 11.1ms at 90 for vr.
2. Profile before shader work: RenderDoc for a GPU-bound frame, the engine profiler for a CPU-bound one.
3. One vertex and one fragment shader per material, uniforms batched per pass, precision set for mobile.
4. Batch before shader tricks: under 100 draw calls per frame on mobile, 1000 on desktop.

```glsl
precision mediump float;              // mobile: no default precision in fragment shaders
varying vec2 vUv;
uniform sampler2D uTex;
void main() { gl_FragColor = texture2D(uTex, vUv); }
```

A shader that compiles on desktop and fails on mobile is almost always missing that precision line.
Netcode: authoritative tick, prediction, 100-150ms interpolation, bandwidth budget -> references/rendering.md.

## check

- [ ] frame time measured on the target device
- [ ] netcode tested with 150ms latency and 2% loss
- [ ] first minute playable without a tutorial wall

## stop

| condition | action |
| --- | --- |
| engine recommended without fit answers | ask them first |
| netcode claim from a localhost test | state the assumption or drop it |
| store policy conflict | surface it before the build |

## emit

- engine, version, target platform
- frame time and the device it was measured on
- what is estimated versus measured
