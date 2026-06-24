# Build Notes — angieqbailey.com

Reference for deployment patterns, troubleshooting and conventions discovered through production builds.

This is part of the durable repo layer: the portable record of how pages get built and deployed. The `aqb-case-study` skill and the `feedback_skill_overrides` memory mirror these conventions for operational use, but the repo is upstream. If a skill disagrees, reconcile to this doc and `styles.css`, then re-sync the skill.

## Dark-Variant Page Setup

Every dark-variant page (case study pages, branded artifact pages) requires three layers of background protection to prevent white flash on load:

```html
<html lang="en" style="background-color:#121A28;">
<head>
    <meta charset="UTF-8">
    <meta name="color-scheme" content="dark">
    ...
</head>
<body style="background-color: #121A28;">
```

The `color-scheme` meta tag tells the browser to default to a dark canvas before any CSS loads. The inline styles on `<html>` and `<body>` provide fallback.

**Critical:** Artifact card links on case study pages must NOT use `target="_blank"`. Same-tab navigation inherits the dark background during page transition. New-tab links flash white because the browser paints its default canvas before HTML loads. All existing deployed case studies use plain `<a>` links without target attributes.

## Link Conventions

| Context | Link Style | Reason |
|---|---|---|
| Artifact cards on case study pages | `<a href="assets/{slug}.html" class="artifact-card">` | Same-tab prevents white flash |
| "View Blank Template" button on artifact pages | `<a href="templates/{slug}-blank.html" class="download-btn">` | Opens template page for viewing/printing |
| Warehouse cards on index.html | `<a href="posts/{slug}/{slug}.html" class="evidence-card">` | Same-tab, consistent with site navigation |
| Back navigation on artifact pages | `<a href="../{case-slug}.html" class="nav-mark">` | Returns to parent case study |

## Blank Template Conventions

- Button text: `Print / Save as PDF` (not "Print Template" or "Download")
- Print margins: `@page { margin: 0.5in; }` (not 1.5cm)
- Table-based templates: `@page { size: landscape; }`
- Card-based templates (methodologies, playbooks): portrait, no `@page` size override
- Button hidden in print: `@media print { .print-btn { display: none; } }`

## Companion Documents

Each case study includes a companion .docx narrative document. These are rich prose versions of the case study, matching the section arc (Evidence, Situation, Pressure Points, Approach, Outcome) but with extended diagnostic narrative. Each companion doc should showcase different capabilities from other case studies.

| Case Study | Companion Focus |
|---|---|
| Web Experience Capacity Expansion | Delivery governance, capacity math, sprint architecture, hard performance metrics |
| GEO/AEO Transition | Research synthesis, subject matter expertise in emerging tech, documentation architecture at scale, self-initiated capability building |

## Deployment via GitHub API

The Cowork VM sandbox can reach api.github.com via the Node.js `https` module, so deploys run from the sandbox. The canonical tool is `deploy.js` in the repo root:

```
node deploy.js <local-file> <repo-path> "<commit message>"
```

It fetches the current file's SHA first (conflict-safe), then pushes the local content. Always pull the latest content of any file you will edit before editing it, since the repo can hold manual GitHub-side edits the local copy lacks. The deploy token (PAT) lives in Claude memory and the session env, never in the repo, and is rotated on expiry. The older Chrome-JS chunking approach in the case-study skill is superseded by `deploy.js`.

## Numeric Language Rule

Use "more than" / "fewer than" / "less than" for numeric comparisons. Never use "under" or "over" for numeric references. "Under" and "over" are spatial only.

- Correct: "fewer than six months"
- Incorrect: "under six months"

## Troubleshooting

**White flash on dark pages:** Check link attributes first. If links use `target="_blank"`, remove it. Same-tab navigation is the fix, not CSS.

**Print margins bleeding:** Set `@page { margin: 0.5in; }` — this is the safe minimum for standard printers.

**Template downloads as HTML file:** The artifact page link should NOT have a `download` attribute. Use `View Blank Template` as link text with `&rarr;` arrow. The template page itself has the `Print / Save as PDF` button.

**GitHub Pages not updating:** Wait 1-2 minutes, then hard refresh (Cmd+Shift+R). Check the raw file via GitHub API to confirm the upload succeeded before debugging the live site.
