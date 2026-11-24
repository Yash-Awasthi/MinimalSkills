---
name: writing-docs
description: >
  One standalone skill for writing, documentation and content: technical
  documentation (README, ADRs, API docs, templates), the unslop anti-AI-writing
  discipline and de-AI/humanize passes, proofreading and voice matching, blog
  and DevRel content, changelogs and release notes, wiki building, tutorials,
  scientific writing and report writing, presentations (PPTX, decks,
  slideshows), diagrams (Mermaid), localization (i18n), meeting and standup
  notes, plan writing, and web scraping/extraction helpers for content work.
  Merges the writing-docs class (124 skills). Fully self-contained: every
  procedure is inline, no external references.
metadata:
  merges: writing-docs
  sources: 124
---

# writing-docs

## 0. Iron laws

1. **Strip the AI smell (unslop).** Short declarative sentences. No em dash.
   A colon may introduce a list and may not connect two clauses. Sentence
   case headings. No chatbot framing, no generic closer, no "delve",
   "leverage", "tapestry", "it's important to note". The unslop CLI audits
   and rewrites; the audit lists the pattern, the rewrite fixes it. Avoid
   AI-writing passes run the same discipline as an audit-and-rewrite cycle;
   the Chinese de-AI writer (de-ai-writer) and humanize-chinese apply the
   equivalent rules for Chinese text.
2. **Anti-sycophancy.** Never open with praise of the request. State the
   assessment first. Disagree when the evidence disagrees; a yes-man draft
   is a defect.
3. **Report writing's most important rule:** report what was found, not what
   was hoped for. Triage & validation's 7-question gate applies to any claim
   written down: can it be demonstrated, is it in scope, is it proven beyond
   "technically possible"?
4. **Scientific writing integrity:** state research-integrity and tool
   limits; never fabricate a citation, a result, or a method. A tool limit
   is stated, not hidden.
5. **Documentation is code-adjacent.** Docs live beside the code they
   describe, update in the same change, and fail the review when stale.
   Docs Guard enforces this; changelog entries ride the same PR.
6. **Write in the user's voice when asked** (write-in-my-voice): sample
   first, match structure and vocabulary, never invent opinions the person
   does not hold.
7. **Show the change** (show-the-change): diffs over descriptions; the
   reader sees what moved, not a prose summary of it.
8. **Full-output enforcement:** when a deliverable is requested in full,
   deliver it in full — no "and so on", no truncation without saying so.

## 1. Technical documentation

- **Docs architect** (docs-architect): when to use and when not — scope
  stated before writing. Structure: overview → quickstart → concepts →
  how-to → reference.
- **README** (readme): what it is, install, quickstart, configuration,
  contributing, license — in that order; badges only when true.
- **Templates** (documentation-templates): README structure plus API docs,
  CONTRIBUTING, CODE_OF_CONDUCT, CHANGELOG skeletons.
- **ADRs** (documentation-and-adrs): decision records with context,
  decision, consequences; numbered, immutable once accepted, superseded by
  a new ADR rather than edited.
- **Generators** (docs-generator, documentation-generation-doc-generate,
  blockvectra-docs): automated documentation from code with compatibility
  and maintenance notes; bundled upstream support declared when absent.
- **Doc workflows** (documentation, brain-to-docs, interview-style-doc-
  building): bundle routing; interview-style building asks questions before
  drafting instead of guessing.
- **Wiki** (wiki-builder, wiki-page-writer, wiki-changelog, wiki-yylo,
  obsidian-markdown): purpose stated before building; page writer with
  frontmatter and cross-links; changelog pages; record selection rules;
  Obsidian-flavored markdown (callouts, wikilinks, embeds).
- **Diagrams** (mermaid-expert, diagram-generator): Mermaid syntax with
  stated do-not-use cases; diagram generation with bundled upstream support
  declared.
- **Changelogs** (changelog-automation, changelog-entry, changelog-updates,
  app-store-changelog): entries written for humans — what changed, why, and
  what to do; automation hooked to conventional commits; app-store release
  notes with character limits respected.

## 2. Editing, proofreading, voice

- **Proofreading** (professional-proofreader, tech-writing-proofread):
  grammar, consistency, terminology; technical proofreading preserves code
  identifiers and never "corrects" an API name.
- **Voice** (beautiful-prose, better-writing, bluebook-writing, cockney,
  faber-language, short, write-in-my-voice, crossframe-dialogue,
  crossframe-notebook): each style carries its own when-to-use and safety
  boundaries; Bluebook for legal citation; Faber for literary register.
- **Detection** (detect-ai-text): detection flags candidates; it never
  asserts authorship as fact.
- **re-create** (re-create): controlled erasure and rebuild protocol —
  strip to the skeleton, rebuild section by section, keep the facts.

## 3. Content and blog

- **Blog** (blog-writing-guide, blog-title-generator, devrel-content,
  content-creator, content-marketer, content-strategy, social-content,
  docs-as-marketing): Sentry-style blog discipline — a specific claim, a
  working example, an honest limitation. DevRel content targets the
  developer reader: runnable code first, marketing second. Documentation as
  marketing: docs that answer real questions rank and convert.
- **SEO helpers** (meta-description-optimizer, meta-description-writer,
  headline-analyzer, content-freshness-checker, content-gap-finder,
  duplicate-content-checker, content-length-comparator, competitor-summary-
  report-creator, site-comparison-report-generator, location-based-content-
  idea-generator): optimizers and checkers report measurements; gaps and
  duplicates are candidates for review, not verdicts.
- **Social repurposing** (postel, adhx, xiaohongshu-content-strategist,
  make-ugc, longbridge-content): turn viral posts into your own with
  attribution discipline; X/Twitter post reading; Xiaohongshu strategy
  (Chinese-canonical); UGC video briefs.
- **Regional formats** (humanize-chinese, de-ai-writer): Chinese-language
  register fixes.

## 4. Presentations and slides

- **PPTX generation** (python-pptx-generator, 2slides-ppt-generator,
  nanobanana-ppt-skills): python-pptx layouts with consistent masters;
  detailed guides read before executing.
- **Decks** (presentation-deck, slideshow, mdpr-skill): deck structure —
  one idea per slide, title as the takeaway; HyperFrames slideshow with
  operational boundaries stated.
- **Office apps** (google-docs-automation, google-slides-automation,
  writer, impress, draw): Google Workspace automation via APIs;
  LibreOffice Writer/Impress/Draw basics (office hub carries the depth).

## 5. Plans, notes, learning

- **Plans** (plan-writing, writing-plans, i-have-adhd): plan format with
  verifiable steps and a definition of done per step; persistence rules for
  multi-session work.
- **Meeting and standup** (meeting-notes, team-collaboration-standup-
  notes): decisions and owners over transcripts; standup format — done /
  doing / blocked.
- **Teaching** (teach, explain-like-socrates, tutorial-engineer,
  technical-tutorials): teaching workspace with stated invocation; Socratic
  questioning over answer-dumping; tutorial engineering with runnable
  checkpoints.
- **Skills writing** (writing-great-skills, writing-skills, writing-
  guidelines, vercel-writing-guidelines, reference-builder): how to write a
  skill — invocation contract, when-to-use, procedures; Vercel's guidelines
  as the house style reference.
- **Learning support** (i-have-adhd persistence rules): externalize state,
  small steps, resume from a written anchor.

## 6. Extraction and conversion helpers

- **Web to text** (url-to-markdown, defuddle, firecrawl-scraper,
  scrapingbee-cli, mock-hunter, curlshot): URL to markdown with declared
  when-to-use; content extraction; scraping CLIs with rate limits honored;
  live-page reality checks; screenshot capture.
- **Conversion** (hugo-to-markdown, pdf-conversion-router, markdown-
  rendering, text-translator, i18n-localization): Hugo content to
  markdown; PDF conversion routed by input type; markdown rendering
  contexts; translation with locale notes; i18n core concepts — externalize
  strings, never concatenate translated fragments, plural forms per locale.
- **Data fetchers** (weather-observation-fetching, tune-monitor,
  traderspy-position-check, fal-image-edit, imagen, video-content-
  extractor, unpaid-intern): niche fetchers and media helpers with
  supporting-material availability declared where absent.
- **Filing** (file-organizer, template-library): file organization rules;
  reusable templates.

## 7. Cross-carried fragments

- **Security reports** (bugcrowd-reporting, triage-validation): program-
  specific reporting tactics with VRT category selection and fallback.
  (security-operations hub carries the depth.)
- **Astro** (astro): content-site framework basics. (frontend hub carries
  the framework depth.)
- **Remotion docs** (remotion-docs): docs search discipline for the Remotion
  video library. (media hub carries the depth.)
- **Spatial UI** (spatial-computing-ui): visionOS-style spatial layouts.
  (mobile hub carries the depth.)
- **Media fragments** (maximalism, daily-news-report, reports-analytics):
  controlled maximalism as an editorial style; news report architecture;
  analytics reporting. (media-creative hub carries the depth.)
- **Leave management** (leave-management): HR register fragment retained
  for completeness; the people-ops hub was retired with its class.

## 8. Output contract

- Name the skill, the document, and the audience in the first line of
  reasoning and in the todo list.
- Report the artifact: a document path, a section, a diff, a slide deck, a
  changelog entry.
- Keep code identifiers, API names, file paths, and quoted strings verbatim.
- State what was drafted, what was reviewed, and what stayed unverified.
- Keep open work open: a missing source, an unverified claim, and a skipped
  section are reported, never rounded up.
- Never print a credential, private payload, or personal data; redact and
  name the rule.

## 9. Failure handling

| Situation | Response |
| --- | --- |
| The draft reads like AI output | Run the unslop pass: patterns listed, rewrite applied. |
| A claim cannot be demonstrated | Cut it or label it unverified. |
| A citation cannot be verified | Do not fabricate; state the limit. |
| Docs drift from the code | Update in the same change or flag the drift. |
| A scraped page fails or is paywalled | Report the failure; never invent the content. |
| A translation loses technical meaning | Keep the English term inline with the translation. |
| A voice sample is too thin to match | Ask for more samples; do not guess the voice. |
| The evidence contradicts the requested claim | Show the evidence and stop. |

## Provenance

Merged from the writing-docs class (124 catalog skills). Every source
skill's procedure, rule and policy is represented above; duplicates
collapsed to one canonical statement; anti-slop discipline, integrity rules
and fail-closed behavior preserved. No external file is required to use
this skill.
