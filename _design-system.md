# AQB Design System Reference
**Last updated:** March 2026
**System name:** Durable Births (Brutalist Industrial-Editorial)

This is the single source of truth for CSS variables, typography, spacing, components, and design rules. If something in this doc conflicts with a skill file, this doc reflects the most recent resolved decision. Update it when decisions change.

---

## Color Palette (CSS Variables)

All defined in `:root {}` at the top of each HTML file.

```css
--nuit: #121A28;          /* Parisian Night — dark page backgrounds */
--cacao: #2D1B14;         /* Deep cacao — alternative dark tone */
--quetzal: #00685E;       /* Base quetzal — borders, grid lines, structural accents on LIGHT backgrounds */
--quetzal-bright: #00A896;/* Readable green text on DARK backgrounds */
--ecru: #F5F5DC;          /* Primary light tone — templates, text on dark */
--rosso: #C41E3A;         /* Accent red — stats, h1 accent words, critical flags */
--ecru-dim: rgba(245, 245, 220, 0.6);   /* Dimmed ecru — body text on dark */
--ecru-ghost: rgba(245, 245, 220, 0.08);/* Very faint ecru — DO NOT use for card backgrounds (too faint) */
--quetzal-line: rgba(0, 104, 94, 0.3);  /* Transparent quetzal — horizontal rules, borders */
--spine-left: 22%;        /* Asymmetric grid left-spine position */
```

**NOT a CSS variable — hardcoded hex:**
- Yellow/amber flag color: `#D4A843` — added after the original design system, never got a variable. Use this hex directly in any new flag instances.

**Quetzal usage rule:**
- `--quetzal` (dark): borders, grid lines, structural accents on ecru/light backgrounds
- `--quetzal-bright`: readable text, links, labels on `--nuit` dark backgrounds

---

## Typography

Three-font system. All loaded via Google Fonts `<link>` tags.

| Font | Use | Import |
|------|-----|--------|
| **Imbue** | Headlines (h1, h2, section headers) | `family=Imbue:opsz,wght@10..20,300..900` |
| **IBM Plex Sans** | Body text, paragraph copy | `family=IBM+Plex+Sans:wght@300;400;500;600` |
| **IBM Plex Mono** | Labels, metadata, tags, nav, metrics, flags | `family=IBM+Plex+Mono:wght@400;500` |

### Font Size Floor: 0.85rem
**IBM Plex Mono minimum is 0.85rem everywhere.** At 0.6–0.75rem it becomes unreadable on mobile. This applies to:
- Section labels
- Card tags / artifact-type labels
- Metric labels / stat labels
- Nav links (exception: drops to 0.75rem only at the 500px mobile breakpoint)
- Footer text
- Constraint flags
- Approach-day / phase labels
- Download / template buttons
- Table headers (`th`)

This is the most frequently violated rule by new sessions. Run a grep for `font-size: 0\.[67]` before pushing any new page.

---

## Page Variants

### Dark Variant (Case Study Pages + Artifact Pages)
- Background: `--nuit` (`#121A28`)
- Body text: `--ecru-dim` (`rgba(245, 245, 220, 0.6)`)
- Headings: `--ecru` (`#F5F5DC`)
- Accent text: `--rosso` or `--quetzal-bright`
- Card/panel backgrounds: `rgba(245, 245, 220, 0.14)` — **not** `var(--ecru-ghost)` which is 0.08 opacity (too faint)

### Light Variant (Blank Templates)
- Background: `--ecru` (`#F5F5DC`)
- Body text: `--nuit` (`#121A28`)
- Accent: `--quetzal` (not quetzal-bright — that's for dark backgrounds)
- Borders: `--quetzal`

---

## Spacing

| Element | Value | Notes |
|---------|-------|-------|
| Section padding (top/bottom) | `2.5rem` | Previously 5rem — halved to avoid dead zones |
| Card padding | `1.75rem 1.5rem` | Confirmed after stat box overflow fix |
| Stat box min-width | `140px` | Bumped from 100px to prevent text truncation |
| Stat row max-width | `750px` | Bumped from 500px to accommodate long labels |
| Left spine | `22%` | `--spine-left` variable |

---

## Constraint Flag System (Three Colors)

Flags appear in Pressure Points sections and diagnostic tables.

| Color | Meaning | CSS Value |
|-------|---------|-----------|
| Red | Critical constraint | `var(--rosso)` / `#C41E3A` |
| Yellow | Caution / advisory | `#D4A843` — **hardcoded, not a variable** |
| Green | Met / resolved | `var(--quetzal-bright)` / `#00A896` on dark; `var(--quetzal)` / `#00685E` on light templates |

History: Yellow flags previously rendered as quetzal-bright (green). Green flags previously rendered as ecru-dim (beige). Both were wrong. Current values are correct.

---

## Section Structure (Case Study Pages)

Standard section order: **Header → Evidence → Situation → Diagnostic/Pressure Points → Approach → Outcome**

Evidence (artifact cards) goes second, immediately after the header lede. This is intentional — deliverables above the fold signal tangible output before the narrative starts. Do not move it to the bottom.

---

## Scroll Animations

All case study and artifact pages use `IntersectionObserver` for `.reveal` class elements. Pattern:

```js
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.1 });
document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
```

CSS paired with this: `.reveal { opacity: 0; transform: translateY(20px); transition: opacity 0.6s ease, transform 0.6s ease; }` and `.reveal.visible { opacity: 1; transform: translateY(0); }`

---

## Navigation

Consistent nav across all pages:
- Main site: links to `#warehouse`, `#debrief`, `#connect`
- Case study pages: back-link to `../index.html` (or `../../index.html` from assets)
- All nav links: IBM Plex Mono, min 0.85rem, `--quetzal-bright` color on dark pages

**Section id:** The "Signal" section was renamed to "Debrief." The id is `#debrief`. All nav links and back-links updated. Do not re-introduce `#signal`.

---

## Template Button Pattern (Two-Step Flow)

All artifact pages use this exact two-button flow. Do not deviate.

1. **On the artifact page:** `"View Blank Template →"` — opens blank template in new tab (`target="_blank"`, no `download` attribute)
2. **On the blank template page:** `"Print / Save as PDF"` — `onclick="window.print()"`

The old `download` attribute on HTML files caused browsers to download raw HTML source instead of rendering the page. It was removed.

---

## Copy-Paste Component Patterns

### Warehouse Card (Live, clickable)
```html
<a href="posts/{slug}/{slug}.html" class="evidence-card" target="_blank" rel="noopener noreferrer" style="text-decoration: none; cursor: pointer;">
  <div class="card-tag">{Category Label}</div>
  <div class="card-title">{Card Title}</div>
  <div class="card-text">{2–3 sentence description. Forensic tone. Problem → intervention.}</div>
  <div class="card-metric">Scope: <span>{scope}</span> // Output: <span>{output}</span></div>
</a>
```

### Warehouse Card (Placeholder, not yet linked)
```html
<div class="evidence-card placeholder">
  <div class="card-tag">{Category Label}</div>
  <div class="card-title">{Card Title}</div>
  <div class="card-text">{Placeholder description}</div>
  <div class="card-metric">Coming soon</div>
</div>
```

### Constraint Flag (Pressure Points section)
```html
<!-- Red: critical -->
<span class="flag" style="background: var(--rosso);">CRITICAL</span>

<!-- Yellow: caution — hardcoded hex, not a variable -->
<span class="flag" style="background: #D4A843; color: #121A28;">CAUTION</span>

<!-- Green: resolved — quetzal-bright on dark pages -->
<span class="flag" style="background: var(--quetzal-bright); color: #121A28;">RESOLVED</span>
```

### Stat Box (Outcome section, dark page)
```html
<div class="stat-box">
  <div class="stat-number" style="color: var(--rosso);">115%</div>
  <div class="stat-label">Conversion lift</div>
</div>
```
Container: `.stat-row { max-width: 750px; }` / `.stat-box { min-width: 140px; padding: 1.75rem 1.5rem; background: rgba(245, 245, 220, 0.14); }`

---

## File Architecture Rules

- Every HTML file is **fully self-contained** — embedded CSS, embedded JS, no external stylesheets, no build tools
- Google Fonts are the **only external dependency** (loaded via `<link>` tags in `<head>`)
- No frameworks, no npm, no bundlers
- Back-links use **relative paths** (`../index.html`, `../../index.html`) not absolute URLs

---

## Responsive Breakpoints

| Breakpoint | What changes |
|-----------|-------------|
| `900px` | Grid collapses to single column, section padding reduces |
| `500px` | Nav links drop to 0.75rem (only exception to the 0.85rem floor), further layout compression |

---

## SEO / Meta Layer

- JSON-LD: `@graph` with Person, WebSite, ProfilePage on index.html; Article schema on case study pages
- Canonical URLs: `<link rel="canonical">` on all pages
- OG tags: title, description, type, url, image, image:width (1200), image:height (630), image:type, locale
- Twitter/X: summary_large_image format
- `jobTitle` in JSON-LD: "Operations Strategist" (crawler-only, not displayed)
- Page `<title>` and `og:title`: "Angie Bailey" — no subtitle

**Important:** `og:image:width` and `og:image:height` are required for reliable LinkedIn detection. Do not remove them.
