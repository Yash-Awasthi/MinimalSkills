# rendering

Load for frame budget, batching, shaders and ECS structure.

## frame budget

| target | total | cpu | gpu |
| --- | --- | --- | --- |
| 60 fps | 16.6ms | 6ms | 10ms |
| 30 fps | 33.3ms | 12ms | 20ms |
| vr 90 fps | 11.1ms | 4ms | 7ms |

Budget per system, not per frame: physics 2ms, animation 1ms, ui 1ms, render submission 3ms. A system that exceeds its slice is the bug.

## draw calls

- Target under 2000 per frame on desktop, under 200 on mobile.
- Static geometry: merge by material, then instance.
- Dynamic: instanced draws with a per-instance buffer, not one mesh per object.
- Sort by state: material, then texture, then depth. A state change costs more than a triangle.
- Atlas small textures. A 4k atlas beats 40 swaps.

## culling and lod

1. Frustum cull per object, then per batch.
2. Occlusion for indoor scenes, portals or a depth prepass.
3. LOD by screen-space size, not distance: a huge object needs its LOD far away.
4. Impostors past the last LOD for foliage and crowds.

## glsl

```glsl
precision mediump float;              // mobile default, highp only where needed
uniform mat4 uViewProj;
attribute vec3 aPosition;
varying vec2 vUv;
```

- One vertex and one fragment shader per material. A permutation per feature multiplies compile time.
- Varyings are interpolators: pack a float4 instead of four floats.
- Branching on a uniform is cheap; branching on a varying diverges the warp.
- Sample textures with mipmaps on; `textureLod` in a loop kills the cache.
- Premultiplied alpha, or every blend is a halo.
- Precision: `highp` on world position, `mediump` on color and uv.

## bevy ecs

```rust
fn move_player(time: Res<Time>, mut q: Query<(&mut Transform, &Speed)>) {
    for (mut t, s) in &mut q {
        t.translation.x += s.0 * time.delta_secs();
    }
}
```

- Systems in a schedule: `Startup`, `Update`, `FixedUpdate`, `PostUpdate`.
- Physics and deterministic logic in `FixedUpdate` at a fixed rate, render interpolation after.
- Resources for global state, components for per-entity, events between systems.
- Query as narrowly as possible; a query over every entity is the usual frame cost.
- `Changed<T>` and `Added<T>` filters beat polling every frame.

## art pipeline

- One texel density across the scene. A prop with 4x the texels reads as imported.
- Normal maps in tangent space, one convention across the pipeline.
- Author LODs for hero assets; a generated LOD drops the silhouette the player reads at distance.
- Sprite atlases: padding to prevent bleed, power-of-two for compression.

## netcode: state sync

- Authoritative server ticks at 20-30 Hz. The client sends input with a sequence number; the server acknowledges the last one applied.
- Client-side prediction: apply the input locally, then reconcile against the server snapshot for that sequence.
- Remote entities interpolate 100-150ms in the past, between two snapshots, never snap to the newest.

```ts
const t = (now - snapA.t) / (snapB.t - snapA.t);
entity.pos = lerp(snapA.pos, snapB.pos, clamp(t, 0, 1));   // one frame of buffer, no teleport
```

- Send deltas: a 60-entity room at 20 Hz with full state is about 30 KB/s per client; changed fields only is 10-20 KB/s down, 2-5 KB/s up.
- Lag compensation: rewind hitboxes by the shooter's RTT, capped at 200ms. Uncapped rewind lets a high-ping player hit behind cover.
- Rollback for fighting games: keep 8-12 frames of input, resimulate from the late input, compare against the last confirmed frame.

Detection: rubber-banding after a loss burst means reconciliation without smoothing; entities teleporting means the interpolation buffer is missing or too short.
## scale

Content hours = finished assets per week times weeks. One artist finishes about 3 environment assets or 1 character per week; a 6-month scope with 3 artists is roughly 70 assets, not 300. Estimate the loop, the content and the polish separately; polish is 30-40% of the schedule and is always the line that gets cut.
