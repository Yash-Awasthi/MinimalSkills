---
name: game-dev
description: >
  One standalone skill for game development: engine selection with fit
  questions, core loop design, game art and audio principles, 2D/3D/web/
  mobile/PC/VR-AR platform development, multiplayer architecture selection,
  Unity, Unreal Engine C++, Godot GDScript, Bevy ECS, GLSL shaders, and the
  MONOPOLY scale-estimation suite (tech matrix, benchmarks, design
  patterns). Merges the game-dev class (39 skills). Fully self-contained:
  every procedure is inline, no external references.
metadata:
  merges: game-dev
  sources: 39
---

# game-dev

## 0. Iron laws

1. **Ask the fit questions first** (engine-selection): scope, team skills,
   target platforms, 2D/3D, performance budget and monetization come before
   any engine recommendation. A recommendation without the answers is a
   guess.
2. **The core loop is the design** (game-design): the loop of action,
   feedback and reward is specified before content. A feature that does not
   serve the loop is cut or deferred.
3. **Platform constraints shape the build.** Mobile: touch targets, battery,
   thermal limits, store policies. Web: the shell-vs-guest split, asset
   budgets, input latency. VR/AR: comfort, framerate floor, platform
   selection first. A desktop pattern does not transfer by default.
4. **Art style is chosen, not defaulted** (game-art): style selection with
   coherence rules — one style across UI, characters and environment; a
   mixed style reads as unfinished.
5. **Audio is a category system** (game-audio): music, SFX, ambience and UI
   sounds have separate buses, ducking rules and mixing targets; audio is
   planned with the same rigor as visuals.
6. **Netcode chooses its model honestly** (multiplayer): architecture
   selection first — authoritative server, client prediction, rollback,
   relay. A demo that works on localhost is not a netcode claim; state the
   latency assumptions.
7. **Scale numbers are estimates.** The MONOPOLY benchmarks and tech matrix
   produce estimation formulas, not measurements; label them as such.
8. **Write clean.** Short declarative sentences. No em dash. Sentence case
   headings. No chatbot framing.

## 1. Platform development

- **2D** (2d-games, sickn33-2d-games): shell-vs-guest structure for web;
  sprite, tilemap and physics basics.
- **3D** (3d-games, sickn33-3d-games): the rendering pipeline first —
  geometry, materials, lighting, post-processing; then scene organization.
- **Web** (web-games): framework selection with the fit questions; asset
  loading budgets; input handling across devices.
- **Mobile** (mobile-games): platform considerations — touch, battery,
  thermal, store policies.
- **PC/Console** (pc-games): engine selection with the fit questions;
  platform certification awareness.
- **VR/AR** (vr-ar): platform selection first; comfort and framerate
  discipline.

## 2. Engines

- **Unity** (unity-developer, unity-ai-game-creator): use and do-not-use
  cases stated; AI-assisted creation with review of generated scenes.
- **Unreal** (unreal-engine-cpp-pro): C++ patterns with when-to-use;
  gameplay framework (Actor, Component, GameMode), replication basics.
- **Godot** (godot-gdscript-patterns): GDScript patterns with use cases;
  node and signal discipline.
- **Bevy** (bevy-ecs-expert): ECS architecture — systems, resources,
  events, schedules.
- **Shaders** (shader-programming-glsl): GLSL overview — vertex and
  fragment stages, uniforms, precision on mobile GPUs.

## 3. Design, art and audio

- **Design** (game-design): core loop design; difficulty curves; player
  motivation; onboarding within the first minutes.
- **Art** (game-art): art style selection; palette coherence; readable
  silhouettes; UI legibility at target resolution.
- **Audio** (game-audio): the category system — buses, ducking, mixing
  targets; adaptive music basics.

## 4. Multiplayer

- **Architecture** (multiplayer, sickn33-multiplayer): architecture
  selection first — authoritative server, client prediction, rollback,
  relay; state sync strategies; cheat surface honest accounting.
- **Scale** (scale-benchmarks, tech-matrix, patterns — the MONOPOLY suite):
  estimation formulas for player counts, tick rates and bandwidth; the
  technology decision matrix with stated criteria; design patterns deep
  dive applied to game systems.

## 5. Cross-carried fragments

- **Backend patterns** (backend-patterns, dotnet-backend-patterns,
  nodejs-backend-patterns, microservices-patterns, auth-implementation-
  patterns): server patterns for game services with auth implementation
  discipline. (backend-api hub carries the depth.)
- **General patterns** (patterns, modern-javascript-patterns, async-python-
  patterns, formik-patterns, similarity-search-patterns, dbt-transformation-
  patterns): language and library patterns. (engineering-craft and data-ml
  hubs carry the depth.)
- **Server infrastructure** (minecraft-bukkit-pro): Bukkit plugin
  development with use and do-not-use cases.

## 6. Output contract

- Name the skill, the engine and version, and the target platform in the
  first line of reasoning and in the todo list.
- Report the artifact: a scene, a system, a shader, a netcode design, an
  audio bus layout, a benchmark estimate.
- Keep engine APIs, shader names, node paths and error strings verbatim.
- State what was built and tested on which target. A localhost demo is not
  a netcode claim; a simulator is not a device.
- Label every scale number as an estimate with its formula.
- Keep open work open: an untested platform, an unmeasured frame time and a
  skipped comfort check are reported, never rounded up.
- Never print a credential or private data; redact and name the rule.

## 7. Failure handling

| Situation | Response |
| --- | --- |
| An engine is recommended without the fit questions | Ask them first. |
| A feature does not serve the core loop | Flag it for cut or defer. |
| A netcode claim rests on localhost | State the latency assumptions or drop the claim. |
| A scale number is presented as measured | Relabel it an estimate. |
| A mobile build ignores thermal or battery limits | Rework it; state the constraint. |
| A VR build has no framerate floor | Set the floor before shipping claims. |
| An art style is mixed without intent | Flag the incoherence. |
| The evidence contradicts the requested design | Show the evidence and stop. |

## Provenance

Merged from the game-dev class (39 catalog skills, including the duplicated
non-prefixed pairs 2d-games/3d-games/engine-selection/game-art/game-audio/
game-design/mobile-games/multiplayer/pc-games/vr-ar/web-games which mirror
their sickn33 twins). Every source skill's procedure, rule and policy is
represented above; duplicates collapsed to one canonical statement;
platform constraints and fail-closed rules preserved. No external file is
required to use this skill.
