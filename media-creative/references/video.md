# video

Load for programmatic video, ffmpeg work and audio delivery.

## remotion

```tsx
export const Clip: React.FC<{ title: string }> = ({ title }) => (
  <AbsoluteFill style={{ backgroundColor: '#0b0b0c' }}>
    <Sequence from={0} durationInFrames={90}>
      <Title text={title} />
    </Sequence>
  </AbsoluteFill>
);
```

- Duration in frames at a fixed fps. `useVideoConfig()` is the only source of truth.
- Deterministic: no `Math.random()` without a seed, no `Date.now()` in a frame.
- `interpolate` with `extrapolateLeft/Right: 'clamp'`, or values overshoot at the edges.
- Render on a server with a pinned Chromium: `npx remotion render Clip out.mp4`.
- Audio: one `<Audio>` per track, volume in `interpolate`, no clipping above 0 dB.

## hyperframes

Runtime media: the composition is code, the player renders it. Suits captions, data-driven scenes and interactive overlays. Same rule as Remotion: fixed fps, deterministic frame, no wall clock.

## ffmpeg

| task | command |
| --- | --- |
| trim without re-encode | `ffmpeg -ss 00:00:12 -to 00:00:30 -i in.mp4 -c copy out.mp4` |
| transcode | `ffmpeg -i in.mp4 -c:v libx264 -crf 20 -preset slow -c:a aac -b:a 128k out.mp4` |
| extract frames | `ffmpeg -i in.mp4 -vf fps=1 frames/%04d.png` |
| contact sheet | `ffmpeg -i in.mp4 -vf "fps=1/10,scale=320:-1,tile=4x4" sheet.png` |
| loudness | `ffmpeg -i in.mp4 -af ebur128 -f null -` |
| normalize | `ffmpeg -i in.mp4 -af loudnorm=I=-14:TP=-1.5:LRA=11 out.mp4` |

- `-c copy` only at a keyframe boundary; otherwise the cut is off by up to the GOP length.
- `-crf` 18 to 23 for delivery. Below 18 the size doubles for no visible gain.
- `-movflags +faststart` for web playback before the full download.

## delivery

| slot | spec |
| --- | --- |
| web hero | 1920x1080, h264, under 8mb |
| social vertical | 1080x1920, under 30s, captions burned |
| thumbnail | 1280x720, under 2mb, text legible at 320px |
| podcast | mp3 128k or opus, -16 LUFS |

## captions

- Generate with a model, then read every line. Names and numbers are the usual errors.
- Two lines maximum, 42 characters per line, 1-6 seconds per cue.
- Burned captions for social, a sidecar track for players.

## check

- [ ] duration and fps match the spec
- [ ] audio peaks under -1 dB, loudness target hit
- [ ] captions present and readable at phone size
- [ ] file size inside the slot
- [ ] the render command is in the repo

## delivery slots

| slot | size | note |
| --- | --- | --- |
| 16:9 web | 1920x1080, 8-12 Mbps | crf 20, aac 128k |
| 9:16 short | 1080x1920 | safe area 250px top, 400px bottom |
| 1:1 feed | 1080x1080 | crop from the master, not a re-render |
| thumbnail | 1280x720, under 2MB | text at 80px minimum |

## render determinism

- Remotion renders per frame from `useCurrentFrame()`. Any `Date.now()`, `Math.random()` or network read inside a frame breaks the render.
- Pass data as props and seed randomness. A render that differs twice is a defect.
- Render in CI at the delivery fps, then compare frame count to duration times fps.
- HyperFrames builds the timeline from data, so the scene reads only its props: no `Date.now()`, no unseeded random, no fetch mid-render.
- Long renders: split into segments and concat, so a failure costs one segment.
