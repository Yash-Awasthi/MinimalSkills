---
name: media-creative
description: Use when producing images, video or audio: generation prompts and providers, Remotion and HyperFrames renders, ffmpeg capture and transcode, thumbnails and covers, captions and loudness, delivery specs. Triggers: image gen, Remotion, HyperFrames, ffmpeg, video, thumbnail.
---

# media-creative

## use when

- generate or edit a still image -> references/images.md
- Remotion or HyperFrames composition -> references/video.md
- ffmpeg trim, transcode, extract frames -> references/video.md
- thumbnail, cover, social crop -> references/images.md
- captions, loudness, audio bed

not for: ui visual system (design-ux), copy (writing-docs)

## rules

- Conflict order: rights, then delivery spec, then style; an unlicensed asset blocks the render.
- Fix the delivery spec before the tool: size, aspect, format, duration, loudness.
- Prompt for the frame, not the idea: subject, action, setting, light, lens, palette.
- Generated text inside an image is unreliable; set type in code over the asset.
- Keep the source asset and the render command. A result without a recipe cannot be revised.
- Record the license of every source asset before it ships.
- Simulated or stock media is labeled, never presented as a capture.

## change

1. Locate: the asset, its delivery slot, and every crop or composition that consumes it.
2. Propose the asset or timing change in one sentence, with the alternative you rejected.
3. Predict before rendering: dimensions, duration, file size and loudness.
4. Back up the source asset and the render command in context, pinned to `git rev-parse HEAD`.
5. Apply one concern per edit; a re-cut and a re-grade are two renders.
6. Verify: re-render at the delivery spec and check size, duration and `-14 LUFS`.
7. Regress: every crop from the master and every scene using the clip.
8. Compare the render against the prediction; a wrong duration stops the export.
9. Report dimensions, format and file size, then take the next item.

## image

1. Fix the slot: aspect, pixel size, safe area for the overlay.
2. Write one paragraph: subject, action, environment, light, style, palette.
3. Generate, then judge at the delivery size, not at 100%.
4. Inspect hands, text, symmetry, edge artifacts, repeated faces.
5. Export in the target format at the target quality.

## video

```bash
ffmpeg -i in.mp4 -vf "scale=1080:-2,fps=30" -c:v libx264 -crf 20 -c:a aac -b:a 128k out.mp4
ffmpeg -i in.mp4 -vf "fps=1" frames/%04d.png
ffmpeg -i in.mp4 -af ebur128=peak=true -f null - 2>&1 | tail -12
```

- Frame rate fixed at the source. Mixed rates stutter on every player.
- Loudness: -14 LUFS for web, -16 for podcast, true peak under -1 dBTP.
- Captions burned in or as a track. Not optional for accessibility.

## compose

```tsx
const frame = useCurrentFrame();                       // the only clock
const opacity = interpolate(frame, [0, 15], [0, 1]);   // deterministic
return <AbsoluteFill style={{ opacity }}><Title /></AbsoluteFill>;
```

- `Date.now()`, `Math.random()` or a fetch inside a frame breaks the render. Seed randomness, pass data as props.
- Render in CI at the delivery fps, then compare frame count to duration times fps.
- HyperFrames builds the timeline from data, so the scene must be pure.
- Provider call with size and quality params, and the audio mix chain: references/images.md, references/video.md.

## decide

| condition | action |
| --- | --- |
| text must appear in the image | render type over it, never generate it |
| one master, many slots | crop per slot from the master |
| web asset over 5mb | recompress, cap the long edge |
| exact timing or data-driven scene | programmatic render, not a manual edit |
| audio matters | normalize loudness, check on phone speakers |

## check

- [ ] exact pixel dimensions at delivery size
- [ ] safe area clear of platform chrome
- [ ] captions present for any speech
- [ ] render reproducible from the command

## stop

| condition | action |
| --- | --- |
| no rights to a source asset | refuse, ask for a licensed one |
| request to imitate a living person | refuse |
| brand kit missing | ask for the kit |

## emit

- assets with dimensions, format, file size
- the command or prompt used
- what was not reviewed at delivery size
