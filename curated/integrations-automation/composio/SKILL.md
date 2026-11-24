---
name: composio
description: >-
  94 Composio skills in five groups: 62 per-app automation workflows for CRMs,
  recruiting, finance, SEO, scraping, messaging, scheduling, storage, data, and AI
  services, plus document and artifact production (docx, pdf, pptx, xlsx, canvas,
  themes, brand, HTML artifacts), research and growth writing, media and file
  utilities, and developer tooling (MCP servers, skills, LangSmith, Playwright,
  Rube connect). Use when a task names a SaaS app and an action, or needs one of
  the bundled document, research, media, or skill tools.
metadata:
  curated_from: 94
  skills: 94
  groups: 5
---

# composio

94 skills. 5 groups. One hub. Every source body is preserved verbatim in
`references/skills/<skill>.md`, and every non-SKILL.md file from a source pack sits at
the same relative path under `references/assets/<skill>/`. Load one body for the task.

`SOURCES.md` maps every source path to its canonical skill and group.
`references/INDEX.md` groups the links, `references/skills.tsv` carries every
description, and `references/GUIDE.md` holds the long-form group prose.

This pack is the remaining Composio source set after the 845-app Rube cluster became
`curated/integrations-automation/composio-rube/`. Both can be installed. This pack
carries the per-app deep workflows and the standalone tools that the Rube catalog did
not cover.

## Pack contract

**One task, one skill.** Pick the app or tool whose requested result matches, read
its body in full before acting, and follow it. Do not blend two app skills because
both are connected. A cross-app chain is stated first, then run in order.

**Connect before acting.** App automation goes through the Rube MCP endpoint at
`https://rube.app/mcp`. Add it, call the app's connection flow, and wait for `ACTIVE`
before any tool call. An auth link means stop and hand it to the user.

**Resolve parent ids first.** Most app workflows need an organization, workspace,
store, page, project, pipeline, or account id before the requested call. Discover it
with the body's list tool, cache it for the task, and never invent an id.

**Use the body's tool names and required fields.** These per-app bodies document
specific tool slugs and parameter names. Pass them exactly. When the server rejects a
schema, read the error and re-check the live schema instead of guessing a new field.

**Writes need a matching instruction.** A read, search, or connection does not
authorize create, update, delete, publish, send, invite, pay, or refund. Confirm the
target, scope, and count for a broadcast, bulk change, payment, or deletion before
executing. Verify a write by reading the object back or keeping the returned id.

**Pagination and time are part of correctness.** Follow cursor or page tokens to the
end for a complete answer, and say when a window was bounded. Use ISO 8601 strings and
the format the body names. Never present the first page as the whole dataset.

**Local and private data stays local.** API keys, tokens, cookies, transcripts,
resumes, invoices, and customer records never enter output, logs, or a public
artifact. Keep keys in the named environment variable or server-side store.

**A source is not an answer.** A successful tool call is evidence of acceptance.
The user's result still needs a readback, a rendered file, or an inspected artifact.
Report what was observed and label what was not verified.

**Write clean as you draft.** Short declarative sentences. No em dash. A colon may
introduce a list and may not connect two clauses. Sentence case headings. No chatbot
framing, no generic closer.

## Routing

| The user wants | Group |
| --- | --- |
| Read or write data in a connected SaaS app | App automation workflows |
| A Word file, deck, spreadsheet, PDF, poster, theme, or HTML artifact | Document and artifact production |
| A changelog, ad analysis, article, growth report, name ideas, comms, leads, meeting insight, resume, or post rewrite | Research, growth, and content |
| Local file cleanup, image sharpening, invoice sorting, a raffle draw, a Slack GIF, or a video download | Media and file utilities |
| An MCP server, a skill, a LangSmith trace, browser testing, or Rube connect | Developer and skill tooling |

## Full roster

### App automation workflows

| Skill | What it does |
| --- | --- |
| [`ahrefs-automation`](references/skills/ahrefs-automation.md) | Ahrefs SEO metrics, backlinks, keyword research, and batch URL analysis |
| [`apify-automation`](references/skills/apify-automation.md) | Apify Actors, datasets, tasks, and crawl results |
| [`apollo-automation`](references/skills/apollo-automation.md) | Apollo lead search, enrichment, and pipeline stages |
| [`ashby-automation`](references/skills/ashby-automation.md) | Ashby candidates, jobs, applications, interviews, and notes |
| [`attio-automation`](references/skills/attio-automation.md) | Attio records, filters, notes, and attribute schemas |
| [`braintree-automation`](references/skills/braintree-automation.md) | Braintree customers, subscriptions, payment methods, and transactions |
| [`capsule-crm-automation`](references/skills/capsule-crm-automation.md) | Capsule contacts, filter queries, tasks, projects, and entries |
| [`clockify-automation`](references/skills/clockify-automation.md) | Clockify time entries, workspaces, users, and running timers |
| [`cloudinary-automation`](references/skills/cloudinary-automation.md) | Cloudinary folders, upload presets, assets, transformations, and usage |
| [`coinbase-automation`](references/skills/coinbase-automation.md) | Coinbase wallets, portfolio data, and paginated wallet audits |
| [`contentful-automation`](references/skills/contentful-automation.md) | Contentful spaces, metadata, and space configuration |
| [`customerio-automation`](references/skills/customerio-automation.md) | Customer.io broadcasts, delivery metrics, segments, and newsletters |
| [`docker-hub-automation`](references/skills/docker-hub-automation.md) | Docker Hub organizations, repositories, teams, members, and webhooks |
| [`dynamics365-automation`](references/skills/dynamics365-automation.md) | Dynamics 365 leads, accounts, contacts, opportunities, orders, invoices, and cases |
| [`elevenlabs-automation`](references/skills/elevenlabs-automation.md) | ElevenLabs speech generation, voices, models, credits, and history |
| [`eventbrite-automation`](references/skills/eventbrite-automation.md) | Eventbrite organizations, events, attendees, categories, and formats |
| [`excel-automation`](references/skills/excel-automation.md) | Excel workbooks, worksheets, cell data, upserts, and formatting through Microsoft or Sheets |
| [`facebook-automation`](references/skills/facebook-automation.md) | Facebook Pages, scheduled posts, video, Messenger, and engagement |
| [`firecrawl-automation`](references/skills/firecrawl-automation.md) | Firecrawl scrape, crawl, extract, batch scrape, map, and crawl jobs |
| [`freshbooks-automation`](references/skills/freshbooks-automation.md) | FreshBooks businesses, projects, time tracking, and billing |
| [`gong-automation`](references/skills/gong-automation.md) | Gong calls, transcripts, users, and revenue intelligence |
| [`gorgias-automation`](references/skills/gorgias-automation.md) | Gorgias tickets, customers, macros, and support operations |
| [`groqcloud-automation`](references/skills/groqcloud-automation.md) | GroqCloud models, chat completions, and transcription |
| [`gumroad-automation`](references/skills/gumroad-automation.md) | Gumroad products, sales, subscribers, and payouts |
| [`harvest-automation`](references/skills/harvest-automation.md) | Harvest projects, time entries, clients, and invoices |
| [`heygen-automation`](references/skills/heygen-automation.md) | HeyGen avatars, videos, templates, and rendering status |
| [`hunter-automation`](references/skills/hunter-automation.md) | Hunter domain search, email verification, and enrichment |
| [`instantly-automation`](references/skills/instantly-automation.md) | Instantly campaigns, sending accounts, lead lists, and analytics |
| [`jotform-automation`](references/skills/jotform-automation.md) | Jotform forms, submissions, folders, activity, and plan limits |
| [`kommo-automation`](references/skills/kommo-automation.md) | Kommo leads, pipelines, stages, tasks, and custom fields |
| [`launch-darkly-automation`](references/skills/launch-darkly-automation.md) | LaunchDarkly projects, environments, flag triggers, and code references |
| [`lemlist-automation`](references/skills/lemlist-automation.md) | Lemlist campaigns, lead enrollment, variables, exports, and unsubscribes |
| [`lemon-squeezy-automation`](references/skills/lemon-squeezy-automation.md) | Lemon Squeezy stores, products, orders, subscriptions, customers, and discounts |
| [`lever-automation`](references/skills/lever-automation.md) | Lever opportunities, postings, requisitions, stages, and tags |
| [`mailerlite-automation`](references/skills/mailerlite-automation.md) | MailerLite subscribers, campaigns, groups, segments, and account stats |
| [`microsoft-clarity-automation`](references/skills/microsoft-clarity-automation.md) | Microsoft Clarity heatmaps, sessions, traffic, geography, and campaigns |
| [`mistral-ai-automation`](references/skills/mistral-ai-automation.md) | Mistral files, libraries, fine-tuning jobs, batches, OCR, and RAG |
| [`neon-automation`](references/skills/neon-automation.md) | Neon projects, branches, databases, and connection details |
| [`netsuite-automation`](references/skills/netsuite-automation.md) | NetSuite records, suitescript, and ERP operations |
| [`new-relic-automation`](references/skills/new-relic-automation.md) | New Relic alerts, incidents, entities, and observability queries |
| [`omnisend-automation`](references/skills/omnisend-automation.md) | Omnisend contacts, campaigns, automations, and ecommerce events |
| [`openai-automation`](references/skills/openai-automation.md) | OpenAI models, chat, embeddings, images, and files |
| [`pandadoc-automation`](references/skills/pandadoc-automation.md) | PandaDoc documents, templates, recipients, and signing status |
| [`phantombuster-automation`](references/skills/phantombuster-automation.md) | PhantomBuster agents, scripts, quotas, containers, and exports |
| [`prismic-automation`](references/skills/prismic-automation.md) | Prismic documents, predicates, refs, custom types, and repository info |
| [`productboard-automation`](references/skills/productboard-automation.md) | Productboard notes, features, objectives, components, and releases |
| [`quickbooks-automation`](references/skills/quickbooks-automation.md) | QuickBooks invoices, customers, accounts, and payments |
| [`ramp-automation`](references/skills/ramp-automation.md) | Ramp transactions, reimbursements, users, cards, and accounting fields |
| [`replicate-automation`](references/skills/replicate-automation.md) | Replicate models, predictions, files, versions, and schemas |
| [`semrush-automation`](references/skills/semrush-automation.md) | SEMrush domain keywords, pages, backlinks, difficulty, and related terms |
| [`share-point-automation`](references/skills/share-point-automation.md) | SharePoint sites, lists, folders, files, search, delta queries, and pages |
| [`shortcut-automation`](references/skills/shortcut-automation.md) | Shortcut stories, tasks, epics, comments, workflows, and projects |
| [`snowflake-automation`](references/skills/snowflake-automation.md) | Snowflake databases, schemas, tables, and SQL execution |
| [`spotify-automation`](references/skills/spotify-automation.md) | Spotify profile, catalog search, playlists, tracks, and playback |
| [`survey-monkey-automation`](references/skills/survey-monkey-automation.md) | SurveyMonkey surveys, collectors, responses, and lifecycle |
| [`toggl-automation`](references/skills/toggl-automation.md) | Toggl time entries, projects, clients, tags, and workspaces |
| [`uploadcare-automation`](references/skills/uploadcare-automation.md) | Uploadcare files, storage, metadata, download URLs, and groups |
| [`wave-accounting-automation`](references/skills/wave-accounting-automation.md) | A placeholder. No native Wave tools exist in Composio. |
| [`webex-automation`](references/skills/webex-automation.md) | Webex messages, rooms, teams, webhooks, memberships, and people |
| [`workday-automation`](references/skills/workday-automation.md) | Workday workers, time off requests, balances, and employee data |
| [`xero-automation`](references/skills/xero-automation.md) | Xero invoices, contacts, payments, bank transactions, and accounts |
| [`zoho-books-automation`](references/skills/zoho-books-automation.md) | Zoho Books organizations, invoices, bills, contacts, and payments |

### Document and artifact production

| Skill | What it does |
| --- | --- |
| [`artifacts-builder`](references/skills/artifacts-builder.md) | Builds multi-component React, Tailwind, and shadcn/ui artifacts, then bundles them into one HTML file. |
| [`brand-guidelines`](references/skills/brand-guidelines.md) | Applies Anthropic's official colors and typography to an artifact that needs the company look. |
| [`canvas-design`](references/skills/canvas-design.md) | Creates original posters and static art as PNG or PDF from a generated visual philosophy, with 80 bundled fonts. |
| [`docx`](references/skills/docx.md) | Creates, edits, and analyzes Word documents with tracked changes, comments, formatting preservation, and text extraction. |
| [`pdf`](references/skills/pdf.md) | Extracts text and tables, creates and merges PDFs, rotates pages, and fills or annotates forms with the bundled scripts. |
| [`pptx`](references/skills/pptx.md) | Creates, edits, and analyzes PowerPoint decks with layouts, comments, speaker notes, and template-matched typography. |
| [`theme-factory`](references/skills/theme-factory.md) | Styles slides, docs, reports, and HTML with one of ten preset themes or a new theme built on the fly. |
| [`xlsx`](references/skills/xlsx.md) | Creates, edits, and analyzes spreadsheets with formulas, formatting, and charts, and requires zero formula errors. |

### Research, growth, and content

| Skill | What it does |
| --- | --- |
| [`changelog-generator`](references/skills/changelog-generator.md) | Turns git commits into user-facing release notes grouped into features, improvements, and fixes. |
| [`competitive-ads-extractor`](references/skills/competitive-ads-extractor.md) | Pulls competitor ads from Facebook and LinkedIn ad libraries and analyzes the messaging and creative choices. |
| [`content-research-writer`](references/skills/content-research-writer.md) | Researches a topic, adds citations, improves hooks, and iterates section by section with the writer. |
| [`developer-growth-analysis`](references/skills/developer-growth-analysis.md) | Reads recent Claude Code history, finds coding gaps, curates learning resources, and sends a growth report. |
| [`domain-name-brainstormer`](references/skills/domain-name-brainstormer.md) | Generates project name ideas and checks availability across .com, .io, .dev, .ai, and other TLDs. |
| [`internal-comms`](references/skills/internal-comms.md) | Writes status reports, leadership updates, newsletters, FAQs, and incident reports in the company's formats. |
| [`lead-research-assistant`](references/skills/lead-research-assistant.md) | Finds target companies for a product and returns actionable contact strategies for sales or business development. |
| [`meeting-insights-analyzer`](references/skills/meeting-insights-analyzer.md) | Reads meeting transcripts for behavioral patterns such as hedging, filler words, dominance, and missed listening. |
| [`tailored-resume-generator`](references/skills/tailored-resume-generator.md) | Maps a job description onto a resume and rewrites the summary, skills, and experience for that role. |
| [`twitter-algorithm-optimizer`](references/skills/twitter-algorithm-optimizer.md) | Rewrites a post for reach using the ranking signals in Twitter's open-source algorithm. |

### Media and file utilities

| Skill | What it does |
| --- | --- |
| [`file-organizer`](references/skills/file-organizer.md) | Finds duplicates and proposes a cleaner structure for local files, with confirmation before any deletion. |
| [`image-enhancer`](references/skills/image-enhancer.md) | Sharpens and upscales images, especially screenshots, while keeping the original files as backup. |
| [`invoice-organizer`](references/skills/invoice-organizer.md) | Reads invoices and receipts, extracts key fields, renames consistently, and sorts them for tax time. |
| [`raffle-winner-picker`](references/skills/raffle-winner-picker.md) | Picks random winners from a list, file, or Google Sheet with transparent fair-selection rules. |
| [`slack-gif-creator`](references/skills/slack-gif-creator.md) | Builds animated Slack GIFs from composable templates and validates Slack size and dimension limits. |
| [`video-downloader`](references/skills/video-downloader.md) | Downloads YouTube video or audio with a chosen quality and format through the bundled script. |

### Developer and skill tooling

| Skill | What it does |
| --- | --- |
| [`connect`](references/skills/connect.md) | Connects Claude to Gmail, Slack, GitHub, Notion, and 1000+ services through a Rube API key and auth link. |
| [`connect-apps`](references/skills/connect-apps.md) | Installs the connect plugin, runs setup, and verifies an external app action end to end. |
| [`langsmith-fetch`](references/skills/langsmith-fetch.md) | Fetches and analyzes recent LangSmith traces and threads to debug LangChain or LangGraph agent behavior. |
| [`mcp-builder`](references/skills/mcp-builder.md) | Guides a high-quality MCP server in Python or TypeScript through research, implementation, review, and evaluation. |
| [`skill-creator`](references/skills/skill-creator.md) | Creates or updates a skill with a required SKILL.md, progressive disclosure, and optional scripts, references, and assets. |
| [`skill-share`](references/skills/skill-share.md) | Creates and validates a skill, packages it, and shares it to Slack through Rube. |
| [`template-skill`](references/skills/template-skill.md) | A placeholder scaffold that shows the minimum skill shape and is meant to be replaced. |
| [`webapp-testing`](references/skills/webapp-testing.md) | Drives a local web app with Playwright to verify behavior, capture screenshots, and read browser logs. |

## Group notes

### App automation workflows

All 62 use the Rube MCP endpoint. Add `https://rube.app/mcp`, connect the named app,
and confirm the connection is active before the first call. Each body lists the app's
main workflows, the exact tool slugs, the required parameters, the known pitfalls, and
a quick reference table. Treat that body as the authority for its app.

The common failure is a missing parent id. Resolve it first with the body's discovery
tool. Eventbrite needs `organization_id`, Facebook needs `page_id`, Clockify and Toggl
need `workspace_id` plus `user_id`, FreshBooks needs `business_id`, Zoho Books needs
`organization_id`, Kommo needs `pipeline_id` and `status_id`, Prismic needs a `ref`,
and Lemon Squeezy needs `store_id`. Cache the value for the task and do not repeat the
discovery call.

Pagination is not optional on list endpoints. Coinbase, Ramp, Lemon Squeezy,
SurveyMonkey, MailerLite, and most CRM list tools return pages. Follow the cursor or
page parameters to the end, or state the bounded window. A first page is not a total.

Exact schema matters. Attio timestamps must be ISO 8601 strings and its name filters
must nest under `name`. Dynamics 365 entity ids are GUIDs without braces. Replicate
models each have their own input keys, so read the schema before a prediction.
Snowflake needs a running warehouse for compute and bindings for user values. Apify
Actors each have a unique input schema. Use the body's fields.

Write safety is per app. Braintree, Coinbase, QuickBooks, Xero, Ramp, Wave, and Zoho
Books move money. State the amount, account, and target before a payment or invoice
write, and verify the returned object. Broadcasts, bulk imports, scheduled posts,
invites, and deletions get the same preview. `wave-accounting-automation` is only a
placeholder because Composio exposes no Wave tools, so say that instead of pretending.

The families are straightforward to route. SEO is Ahrefs and SEMrush. Scraping is
Apify, Firecrawl, and PhantomBuster. CRM is Apollo, Attio, Capsule, Dynamics 365,
Kommo, and HubSpot-style pipelines. Recruiting is Ashby and Lever. Finance is
Braintree, Coinbase, FreshBooks, QuickBooks, Ramp, Wave, Xero, and Zoho Books.
Messaging and support are Customer.io, Facebook, Gorgias, MailerLite, Omnisend,
SurveyMonkey, Webex, and Zoho. Data and AI are GroqCloud, Mistral, Neon, New Relic,
OpenAI, Replicate, Snowflake, and ElevenLabs.

### Document and artifact production

`docx` handles professional Word documents, tracked changes, comments, and text
extraction. Before any OOXML work it requires reading `docx-js.md` and `ooxml.md` in
full, with no range limit. Tracked-change edits use the redlining workflow. Grep
`word/document.xml` immediately before writing a script because line numbers move.

`pptx` covers decks, layouts, comments, speaker notes, and template matching. It
requires reading `html2pptx.md` and `ooxml.md` in full before the matching workflow.
Analyze a reference deck's typography and colors first. Never stack charts or tables
below text in one column. `xlsx` requires zero formula errors, preserves an existing
template's conventions over the house style, uses the documented color and number
formats, and recalculates with LibreOffice through `recalc.py`.

`pdf` extracts text and tables, creates, merges, splits, rotates, and fills forms.
The form path uses `forms.md` and the bundled scripts to inspect fields, fill them,
and check bounding boxes. `canvas-design` generates an original visual philosophy and
a PNG or PDF, uses the 80 bundled fonts, keeps text minimal, and never copies an
existing artist. `brand-guidelines` applies Anthropic colors and typography with
system fonts. `theme-factory` offers ten themes and a showcase PDF to view, not edit.
`artifacts-builder` is for multi-component React, Tailwind, and shadcn/ui artifacts,
then bundles one HTML file. It is not for a simple single-file artifact.

### Research, growth, and content

`changelog-generator` reads git history, groups changes, and rewrites technical
commits as customer-facing notes. `competitive-ads-extractor` reads Facebook and
LinkedIn ad libraries and reports the messaging and creative patterns.
`content-research-writer` researches with citations, sharpens the hook, and works
section by section. `developer-growth-analysis` reads recent Claude Code history,
finds gaps, curates Hacker News resources, and sends a Slack DM. Treat the transcript
as private data.

`domain-name-brainstormer` generates names and checks TLD availability.
`internal-comms` follows the company's own formats for status, leadership, newsletter,
FAQ, and incident writing. `lead-research-assistant` identifies target companies and
contact strategies. `meeting-insights-analyzer` reads transcripts for behavioral
patterns. `tailored-resume-generator` maps a job description onto a resume and asks the
user to review the personal output before sending. `twitter-algorithm-optimizer`
rewrites a post against the ranking signals in Twitter's published algorithm.

### Media and file utilities

`file-organizer` proposes a structure and duplicate cleanup, and always asks before
deleting. `invoice-organizer` extracts invoice fields, renames consistently, and sorts
for tax time. `image-enhancer` sharpens and upscales while keeping originals.
`raffle-winner-picker` draws from a list, file, or Sheet with a transparent method and
optional exclusions. `slack-gif-creator` composes frames from templates and validates
Slack's size and dimension limits. `video-downloader` wraps `yt-dlp` with quality,
format, and audio-only options through its script.

### Developer and skill tooling

`connect` and `connect-apps` set up Rube access to external apps. `connect` uses a
Rube API key in an environment variable and an auth link. `connect-apps` installs the
plugin, runs setup, and verifies an action. `langsmith-fetch` requires the CLI and
environment variables, then pulls recent traces and threads for debugging.
`webapp-testing` drives a local app with Playwright, starts with `--help` on the
bundled scripts, launches headless Chromium, and always closes the browser.

`mcp-builder` runs research, implementation, review, and evaluation for a Python or
TypeScript MCP server, with read-only tools as the baseline. `skill-creator` requires
a `SKILL.md` with name and description, uses progressive disclosure, and ships init,
package, and validate scripts. `skill-share` creates, validates, and packages a skill,
then posts it to Slack through Rube. `template-skill` is a placeholder to replace.

## Output contract

- Name the skill and the app or tool in the first line of your reasoning and in the
  todolist.
- Report the actual result. A created file, a readback object, a rendered page, a
  stored id, or a tool response with its key fields. A 2xx or a green check is not
  the user's outcome.
- Keep ids, timestamps, currency, and error strings verbatim. Do not rename a field
  or round a number on the way out.
- State the window, the page count, and any skipped source. A bounded read is not a
  complete dataset.
- Keep open work open. A blocked write, a missing connection, and an unverified
  artifact are reported, never rounded up to done.
- Write through `unslop`. Short declarative sentences, sentence case headings, no em
  dash, no colon connecting two clauses, no chatbot framing.
- Sanitize keys, tokens, customer data, transcripts, resumes, and invoice details
  before any public output.

## Failure handling

| Situation | Response |
| --- | --- |
| The app is not connected, or the connection is not `ACTIVE` | Return the auth link and stop. No tool call. |
| A required parent id cannot be resolved | Fail closed. Name the discovery tool and the missing id. |
| The live schema rejects a documented field | Read the error, re-check the live schema, and correct the call. Never invent a replacement field. |
| A tool returns a partial page | Follow the cursor or state the bounded window. Never present the page as the total. |
| A write would move money, broadcast, bulk change, or delete | Preview the target and count, get the matching approval, then execute once and verify. |
| A document, deck, or spreadsheet has a validation error | Keep the failure, fix the source, and re-run the validator. Never ship a file with a known error. |
| A source file or script is missing | Fail closed. Name the missing path. |
| The user asks for Wave Accounting | Say the integration is a placeholder and offer the native Wave UI or API instead. |

## Provenance

94 `composio-*` source directories became 94 canonical skills in 5 groups. Each source
had one body, so no merge or variant resolution was needed. Every body is verbatim at
`references/skills/<skill>.md` with its original frontmatter removed, and every other
file from a source pack is copied under `references/assets/<skill>/` at the same
relative path. 271 asset files totaling 8,651,193 bytes were copied.

These sources are the remainder after the 845-app Rube cluster became
`curated/integrations-automation/composio-rube/`. That pack covers broad app access
through a search-first canonical workflow. This pack keeps the per-app deep workflows
and the standalone document, research, media, and developer tools. `composio-rube`
remains the authority for an app it catalogs and this pack does not.

Upstream author `composio`. Original catalog paths are preserved in `SOURCES.md` and
under `_archive/composio/catalog/`.
