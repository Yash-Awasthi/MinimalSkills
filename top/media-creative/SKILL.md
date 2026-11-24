---
name: media-creative
description: >
  One standalone skill for media and creative production: AI image, video,
  music and voice generation (Fal, Stability AI, Suno, Beatra, voice cloning,
  lipsync, talking avatars), Remotion programmatic video (create, render,
  captions, interactivity, Stitch walkthroughs), HyperFrames runtime media,
  YouTube ingestion and transcripts, podcast generation, screen recording,
  product photography and ecommerce listings, QR art with validation, cover
  makers, video editing and routing, and web media extraction. Merges the
  media-creative class (64 skills). Fully self-contained: every procedure is
  inline, no external references.
metadata:
  merges: media-creative
  sources: 64
---

# media-creative

## 0. Iron laws

1. **A generation is a side effect.** Image, video, audio and voice
   generation calls paid APIs and publishes artifacts. Confirm the target,
   the cost and the authorization before the call. Installing a CLI or
   downloading a model is also a side effect: download, review, run the
   reviewed file.
2. **Keys are narrow and secret.** Each provider skill requires its own API
   key setup first. Use a key scoped to the one provider; never print it,
   embed it in a script or commit it. A missing key stops the task with the
   setup step, not a guessed key.
3. **A missing bundled runtime fails closed.** md2video-audio stops before
   execution when its runtime is absent; podcast generation, Monte Carlo
   helpers and other bundled-upstream skills declare what is not bundled.
   Never fabricate a runtime or run a same-named file from an unrelated
   directory.
4. **Rights and likeness are the user's to confirm.** Voice cloning,
   talking avatars, viral-video remakes and riffing existing TikToks need
   the rights holder's consent. State the boundary; do not clone a voice or
   remake a video without it.
5. **Validate generated media before use.** QRX art QR codes are validated
   by scan test before use; lookdev-auto runs a visual eval loop because
   only an eye can judge it; a generated image with text needs the text
   checked. A render that completed is not a render that is correct.
6. **Version and scope discipline.** Remotion skills declare version and
   snippet scope; HyperFrames skills carry operational boundaries; provider
   CLIs pin their version. Read the installed version's behavior, not the
   memory of it.
7. **Attribution and licensing.** Unsplash integration follows its license
   terms; stock and fetched media keep their provenance; never pass off a
   fetched asset as original work.
8. **Write clean.** Short declarative sentences. No em dash. Sentence case
   headings. No chatbot framing.

## 1. Generation providers

- **Fal family** (fal-generate, fal-audio, fal-upscale, fal-workflow):
  image generation, audio, upscaling and workflow composition, each with
  its own overview and model list.
- **Stability AI** (stability-ai): professional image generation
  (Portuguese-canonical).
- **Beatra** (beatra, beatra-ai-video-studio): AI media generation and the
  video studio.
- **Music** (music-generation-studio, suno-lyrics-to-song, music-for-
  robots): AI music generation; lyrics-to-song; multimodal music discovery
  and creative exercise.
- **Voice** (voice-cloning-studio, sync-lipsync, talking-avatar-video,
  voice-ai-development, voice-ai-engine-development, podcast-generation):
  cloning with consent; lipsync; avatar video; voice AI development and
  engine building; podcast generation with GPT Realtime Mini and bundled
  upstream support declared.
- **Video platforms** (mmx-cli, runapi-cli, muapi-media, imagera-media,
  modellix, atlas-cloud-media): provider CLIs and media APIs, each with
  when-to-use and key setup.

## 2. Programmatic video (Remotion)

- **Create** (remotion-create): scaffold a project with the standard
  template; when-to-use stated.
- **Render** (remotion-render): general rendering strategy — concurrency,
  output formats, deterministic frames.
- **Captions** (remotion-captions): caption generation and timing.
- **Interactivity** (remotion-interactivity): version and snippet scope
  declared.
- **Best practices** (remotion-best-practices): when-to-use and how-to-use
  stated; composition and performance rules.
- **Stitch walkthroughs** (remotion): Stitch-to-Remotion walkthrough videos.

## 3. HyperFrames runtime

- **Core** (hyperframes, hyperframes-cli, hyperframes-registry, media-use):
  the HyperFrames runtime, its CLI and registry, and media handling inside
  it — each with operational boundaries (AAS adaptation) stated. Slideshow
  and Figma pipelines live in the frontend and design hubs' slide rules.

## 4. Video editing, capture and analysis

- **Routing and editing** (video-router, minicut-film-studio, reverse-any-
  video, viral-video-teardown-remake, riffkit): route a video task to the
  right tool; film-studio editing; reversal; teardown-remake with rights
  discipline; riffing winning TikToks into your own.
- **Capture** (macos-screen-recorder, screenstudio-alt): screen recording
  with permissions and when-to-use stated.
- **Analysis** (seek-and-analyze-video, videodb, videodb-skills): seek and
  analyze with stated purpose; VideoDB indexing and retrieval.
- **Ingestion** (ingest-youtube, youtube-full, youtube-transcript,
  youtube-transcript-skills, youtube-summarizer, youtube-notetaker):
  YouTube-to-vault connectors; transcripts via TranscriptAPI or DeepAPI
  with yt-dlp fallback; summarizers with source and summary limits stated —
  a summary never invents a claim the transcript does not carry.
- **Extraction** (web-media-getter, audio-transcriber): web media
  extraction; transcription with detailed guide.

## 5. Stills, product and covers

- **Product photography** (product-photo-studio, ecommerce-listing-image-
  set): AI product photography; full listing image sets with consistent
  lighting and angle plans.
- **Covers and art** (wechat-cover-maker, zhongcao-cover-maker, claymor-
  phism style carried by design hub, qrx): WeChat article covers; Xiaohongshu
  covers (Chinese-canonical); art QR codes validated before use.
- **Creative** (daily-gift, pro-motion, film-crew, lanshu-create-ai-
  presenter-video): daily creative prompts; MG film/audio-first production
  for launch, brand, TVC and promo; film-crew role routing; AI presenter
  videos (Chinese-canonical).

## 6. Cross-carried fragments

- **Slides** (remotion family interplay): slide-fit rules live in the
  frontend hub §4.
- **Design styles** (claymorphism): named style bodies live in the
  design-ux hub §2.
- **NSFW boundary** (nsfw-ai-spicyapi): supporting-material availability
  declared; adult-content skills run only within the user's stated legal
  and platform boundaries and never generate content involving real people
  without consent.

## 7. Output contract

- Name the skill, the provider, and the artifact in the first line of
  reasoning and in the todo list.
- Report the artifact: a file path, a render output, a transcript, a
  generated asset, a validation result.
- Keep model names, parameter names, version numbers and error strings
  verbatim.
- State what was generated, what was validated, and by which check.
- State cost and rights status for every generation.
- Keep open work open: a missing runtime, an unverified scan test and a
  skipped validation are reported, never rounded up.
- Never print a key, token or personal data; redact and name the rule.

## 8. Failure handling

| Situation | Response |
| --- | --- |
| An API key is missing | Stop at the setup step; never guess a key. |
| A bundled runtime is absent | Fail closed; never fabricate it. |
| A voice clone or remake lacks consent | Refuse until the rights holder consents. |
| A generated asset was not validated | Run the validation (scan test, visual eval) first. |
| A summary adds a claim the transcript lacks | Cut the claim or quote the source. |
| A render finished but was not reviewed | Render is not correctness; review the output. |
| A provider version differs from the guide | Read the installed version's behavior. |
| The evidence contradicts the requested output | Show the evidence and stop. |

## Provenance

Merged from the media-creative class (64 catalog skills). Every source
skill's procedure, rule and policy is represented above; duplicates
collapsed to one canonical statement; consent, key and fail-closed rules
preserved. No external file is required to use this skill.
