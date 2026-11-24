# images

Load for generation, editing and delivery of stills.

## prompt

```
subject:     what, doing what
setting:     where, time of day, weather
light:       direction, quality, color temperature
lens:        wide, normal, macro, depth of field
palette:     three colors, contrast level
composition: rule of thirds, negative space for type
```

One paragraph, in that order. A list of adjectives produces a generic image.

## provider behavior

| behavior | consequence |
| --- | --- |
| text rendering | unreliable, set type in code |
| hands and faces | check at delivery size, not at 100% |
| aspect ratio | native ratio beats cropping a square |
| seed | store it, or the next render differs |
| upscale | do it in one pass, not chained |

## editing

- Change one attribute per pass. "Make it darker and remove the chair" usually does both badly.
- Keep the original. An edit chain loses the ability to go back.
- Inpainting for a small object, a new render for a layout change.

## delivery

| slot | size | format |
| --- | --- | --- |
| hero | 1600x900 or 2400x1350 | avif, webp fallback |
| card | 800x600 | webp |
| avatar | 512x512 | webp, square crop |
| og image | 1200x630 | png |
| thumbnail | 1280x720 | webp, under 2mb |

- Export at 2x the css size for retina, cap the long edge.
- Check the file size at the target quality, not at the default.
- Alt text names the function ("invoice total panel"), not the pixels ("blue rectangle"); a pixel description tells a screen reader nothing.

## accessibility

- Contrast of any text over an image: 4.5:1 at the worst part of the image, not the average.
- A gradient scrim is a fix, a low-contrast overlay is not.
- Motion: no autoplay loop above 5 seconds without a pause control.

## provenance

- Record the prompt, provider, model version and seed with the asset.
- A generated asset with no record cannot be regenerated or audited.
- License of any source image checked before it enters the render.

## provider call

```bash
curl -s https://api.openai.com/v1/images/generations \
  -H "authorization: Bearer $KEY" -H 'content-type: application/json' \
  -d '{"model":"gpt-image-1","prompt":"a matte ceramic mug on a linen cloth, soft window light, 50mm","size":"1024x1536","quality":"high","n":1}'
```

- `size` must match the slot: 1024x1024, 1024x1536, 1536x1024. Anything else is rejected, not resized.
- `n` above 1 is variants and costs n times. Generate one, judge it, then iterate on the prompt.
- The response returns base64 or a temporary url. Download and store the file; a hotlinked url expires.
- A 400 with `invalid_prompt` is a policy refusal, not a syntax error. Rewrite the subject, do not retry the same prompt.

## audio

```bash
ffmpeg -i voice.wav -af "loudnorm=I=-16:TP=-1.5:LRA=11" -ar 48000 voice_norm.wav
ffmpeg -i music.mp3 -i voice.wav -filter_complex \
  "[1:a]asplit=2[v1][v2];[0:a][v2]sidechaincompress=threshold=0.05:ratio=8[m];[m][v1]amix=inputs=2" mix.wav
```

- Normalize speech to -16 LUFS for podcast, -14 for web. A bed mixed by ear buries consonants on phone speakers.
- Sidechain ducking keeps music 8-10 dB under speech; a static volume cut fails on a loud master.
- True peak under -1 dBTP, or the encoder clips after loudness normalization.
## provider index

| provider | the rule that matters |
| --- | --- |
| Stability AI | `POST /v2beta/stable-image/generate/core` with `aspect_ratio` and `output_format`; a 429 is a queue, not an error, retry with backoff. |
| Create | Image-to-image and upscale: `strength` under 0.4 keeps composition, above 0.7 redraws it. |
| Interactivity | A generated interactive asset (hover, parallax) ships as two frames plus a mask, not a video. |
| Core | The base model pass: generate at 1024, judge, then upscale; generating at 2048 first wastes credits on rejects. |
| Ingestion | Ingest at the source resolution and keep the original; a re-encode before edit is a generation loss. |
| Extraction | Extract frames at the edit rate, not 1fps, when a cut lands mid-second; `-vf fps=source_fps`. |
| Analysis | Scene detection with `ffmpeg -vf "select='gt(scene,0.3)'"`; a fixed 10s cut misses every fast cut. |
| Best practices | One variable per iteration: prompt, then seed, then size; changing two makes the result unattributable. |
| Product photography | 45-degree key light, white sweep, `f/8`; a generated product shot must match the real product's proportions or it misleads. |
| Stills, product and covers | Cover art is judged at 200px wide; a detail that only reads at full size is lost in the feed. |
