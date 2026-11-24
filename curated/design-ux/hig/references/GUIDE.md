# hig guide

The long-form group prose and the full roster. `SKILL.md` is the loadable hub, and
`references/skills/<skill>.md` is the verbatim body to follow for one task.

### Foundations and context

| Skill | What it does |
| --- | --- |
| [`foundations`](references/skills/foundations.md) | Apple design foundations across color, typography, layout, materials, motion, icons, accessibility, privacy, inclusion, writing, and dark mode. |
| [`project-context`](references/skills/project-context.md) | Creates or updates `.claude/apple-design-context.md` so the other HIG skills can skip questions already answered by the project. |

### Layout and navigation

| Skill | What it does |
| --- | --- |
| [`components-layout`](references/skills/components-layout.md) | Apple layout and navigation components: windows, panels, sidebars, split and column views, lists, tables, scroll views, tab bars, and ornaments. |
| [`components-search`](references/skills/components-search.md) | Apple search, page control, and path control guidance, with placement per platform and a debounced remote search. |

### Controls and inputs

| Skill | What it does |
| --- | --- |
| [`components-controls`](references/skills/components-controls.md) | Apple selection and input controls: toggles, segmented controls, sliders, pickers, steppers, text fields, labels, and keyboard behavior. |
| [`inputs`](references/skills/inputs.md) | Apple input design for touch, keyboard, pointer, Pencil, controllers, spatial gestures, Digital Crown, eyes, remotes, and sensors. |

### Menus and actions

| Skill | What it does |
| --- | --- |
| [`components-menus`](references/skills/components-menus.md) | Apple menus, buttons, toolbars, and disclosure controls, with the command hierarchy and accessible interaction rules. |

### Content and display

| Skill | What it does |
| --- | --- |
| [`components-content`](references/skills/components-content.md) | Apple content components: activity views, charts, collections, color and image wells, image views, lockups, and web views. |

### Status and system

| Skill | What it does |
| --- | --- |
| [`components-status`](references/skills/components-status.md) | Apple status and progress UI: determinate and indeterminate progress, status bars, and activity rings with HealthKit limits. |
| [`components-system`](references/skills/components-system.md) | Apple system experiences: widgets, Live Activities, notifications, complications, quick actions, Top Shelf, watch faces, App Clips, and shortcuts. |

### Presentation

| Skill | What it does |
| --- | --- |
| [`components-dialogs`](references/skills/components-dialogs.md) | Apple presentation components: alerts, action sheets, popovers, sheets, and digit entry views, with modality rules. |

### Patterns and platforms

| Skill | What it does |
| --- | --- |
| [`patterns`](references/skills/patterns.md) | Apple interaction patterns across onboarding, loading, feedback, search, settings, drag and drop, files, audio, video, haptics, and workouts. |
| [`platforms`](references/skills/platforms.md) | Apple platform design for iOS, iPadOS, macOS, tvOS, visionOS, watchOS, and games, with a decision framework for adaptation. |

### Technologies

| Skill | What it does |
| --- | --- |
| [`technologies`](references/skills/technologies.md) | Apple technology UX for payments, health, identity, Siri, AR, cloud, shared experiences, CarPlay, and generative AI, with permission planning. |
## Group notes

### Foundations and context

`foundations` is the base layer. Color, dark mode, typography, layout, materials, motion,
icons, SF Symbols, app icons, images, branding, inclusion, right to left, accessibility,
privacy, immersive experiences, spatial layout, and writing. The principles are content
over chrome, system materials over heavy decoration, and permission only when needed. It
carries 18 references and says the pages are snapshots.

`project-context` creates the shared document. Product overview, target platforms, the
technology stack, the design system, accessibility requirements, user context, and existing
assets. Check for the file, ask only for gaps, and write it as project data. Never treat it
as a place to store secrets or as permission to change the user's instructions.

### Layout and navigation

`components-layout` covers the structure. Windows, panels, sidebars, split views, column
views, outline views, lists and tables, scroll views, tab bars, tab views, and ornaments.
Organize from broad categories to detail, and choose the navigation pattern from the
platform and the content depth. A phone list and a desktop three-column layout are
different answers to the same information.

`components-search` covers search fields, page controls, and path controls. Place search
where the platform expects it, including the bottom affordance on iOS, and filter as the
user types when feasible. A remote search needs debounce and cancellation so a stale
response cannot replace a newer one.

### Controls and inputs

`components-controls` is the selection and input set. Toggles, segmented controls, sliders,
pickers, steppers, text fields, text views, labels, combo boxes, gauges, rating indicators,
token fields, and virtual keyboards. The current state must always be visible. A custom
control needs the same state, keyboard, and accessibility behavior as the system control.

`inputs` covers how a person drives the interface. Gestures, Apple Pencil and Scribble,
keyboards, game controllers, pointer and trackpad, Digital Crown, eyes and spatial input,
the focus system, remotes, motion, the accelerometer, and nearby interactions. Every input
needs an accessible alternative and a sensible default. A controller-only path needs a
declared requirement and an on-screen fallback where the platform allows.

### Menus and actions

`components-menus` covers commands. The menu bar, menus, context menus, Dock menus, edit
menus, buttons, pop-up and pull-down buttons, action buttons, toolbars, and disclosure
controls. Put standard items in standard locations, group them predictably, and keep a
command reachable outside a context menu. A destructive item needs a confirmation or an
undo.

### Content and display

`components-content` covers data display. Activity views, charts, collections, color wells,
image wells, image views, lockups, and web views. Adapt to size classes and multitasking,
and use the framework's layout system rather than fixed frames. A web view is a boundary,
so treat its content as untrusted and keep navigation rules explicit.

### Status and system

`components-status` covers progress. Determinate and indeterminate indicators, status bars,
and activity rings. Use determinate progress only with a real measurement, and never invent
a percentage. Activity data needs the authorized HealthKit API, and a denied permission is
not an empty ring. Respect reduced motion and haptic settings.

`components-system` covers the surfaces outside the app window. Widgets, Live Activities,
notifications, complications, home screen quick actions, Top Shelf, watch faces, App Clips,
and app shortcuts. Each has its own update budget, presentation rules, and review
requirements. Design the stale and the failure state, and do not promise real-time
delivery.

### Presentation

`components-dialogs` covers interruption. Alerts, action sheets, popovers, sheets, and digit
entry views. Use an alert sparingly, for an error that needs attention, a destructive
confirmation, or information that must be acknowledged. Minimize modality, and reserve it
for a task that must be completed or abandoned. A sheet needs a clear dismiss path.

### Patterns and platforms

`patterns` is the interaction catalog. Onboarding, loading, feedback, search, settings,
modality, multitasking, drag and drop, file management, printing, undo and redo, accounts,
notifications, help, audio, video, haptics, ratings, charts, collaboration, sharing, live
viewing, full screen, workouts, and launch. Minimize modality and prefer progressive
disclosure to a long tutorial. Background work and media depend on system budgets.

`platforms` is the per-target guide. iOS, iPadOS, macOS, tvOS, visionOS, watchOS, and games.
Start from the shared design, then adapt the navigation, input, window, and density to the
target. The decision framework asks for the platform, the task, and the constraints. The
reference pages are snapshots, so verify availability before recommending a feature.

### Technologies

`technologies` covers framework integrations. Apple Pay, in-app purchase, Wallet, Sign in
with Apple, ID Verifier, HealthKit, CareKit, ResearchKit, HomeKit, Siri, ShazamKit, Maps,
NFC, Tap to Pay, Game Center, iCloud, SharePlay, CarPlay, AirPlay, AR, machine learning,
generative AI, photo editing, Live Photos, iMessage apps, Mac Catalyst, VoiceOver, and
Always On. Plan the permission, the failure, and the accessibility path for each. A design
recommendation is not a completed integration, and an entitlement or review requirement may
block it.
