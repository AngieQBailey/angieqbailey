# Build Notes — angieqbailey.com

Reference for deployment patterns, troubleshooting and conventions discovered through production builds.

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

The Cowork VM sandbox CAN reach api.github.com via Node.js `https` module. Use the Node.js upload script pattern:

```javascript
// Install docx if needed: cd /tmp/docx-build && npm init -y && npm install docx
const https = require('https');
const fs = require('fs');
const path = require('path');

const PAT = '{current_pat}';  // Refresh from Angie each session
const REPO = 'AngieQBailey/angieqbailey';
const BASE = '/sessions/{session}/mnt/Website & Case Studies/Portfolio Work/{Case Name}';

// Upload function handles both new files and updates (checks SHA automatically)
async function uploadFile(localPath, remotePath) {
  const content = fs.readFileSync(path.join(BASE, localPath));
  const b64 = content.toString('base64');
  let sha = null;
  // Check for existing file
  try {
    const check = await apiCall('GET', `/repos/${REPO}/contents/${remotePath}`);
    if (check.status === 200 && check.data.sha) sha = check.data.sha;
  } catch(e) {}
  const body = { message: `Update ${remotePath}`, content: b64 };
  if (sha) body.sha = sha;
  const result = await apiCall('PUT', `/repos/${REPO}/contents/${remotePath}`, body);
  return { ok: result.status === 200 || result.status === 201 };
}
```

This replaces the Chrome JS chunking approach documented in the skill. Node.js is faster and more reliable.

## Numeric Language Rule

Use "more than" / "fewer than" / "less than" for numeric comparisons. Never use "under" or "over" for numeric references. "Under" and "over" are spatial only.

- Correct: "fewer than six months"
- Incorrect: "under six months"

## Troubleshooting

**White flash on dark pages:** Check link attributes first. If links use `target="_blank"`, remove it. Same-tab navigation is the fix, not CSS.

**Print margins bleeding:** Set `@page { margin: 0.5in; }` — this is the safe minimum for standard printers.

**Template downloads as HTML file:** The artifact page link should NOT have a `download` attribute. Use `View Blank Template` as link text with `&rarr;` arrow. The template page itself has the `Print / Save as PDF` button.

**GitHub Pages not updating:** Wait 1-2 minutes, then hard refresh (Cmd+Shift+R). Check the raw file via GitHub API to confirm the upload succeeded before debugging the live site.
