# AQB Site Changelog
**Repo:** `AngieQBailey/angieqbailey`

Running record of what changed, when, and why. Git commits are terse. This document captures the reasoning. Add an entry any time content is added, updated, or removed. Most recent entries at top.

---

## March 2026

### Warehouse grid reorder + Summit card title fix
**Commit:** `831e0ed` / `7053125`
**What:** Restored Post-Acquisition Integration placeholder card (had been accidentally replaced). Reordered Warehouse grid to: Summit → P&L Build → Web Experience Capacity Build → Post-Acquisition Integration → Workforce AI Adoption. Renamed Summit card title from "E-Commerce Strategic Summit Cross-Functional Alignment" to "Multi-Team Roadmap Summit."
**Why:** Previous edit replaced the wrong card when adding Web Experience. Summit card title was too long and jammed — two lines of text in a card label is not the pattern. Card title is a fast read; case study page h1 is the full forensic record. They are allowed to differ.

---

### Web Experience Capacity Build — full case study launched
**Commit:** `c385711`
**What:** Added three new files:
- `posts/web-experience-capacity-build/web-experience-capacity-build.html` — main case study page
- `posts/web-experience-capacity-build/assets/team-capacity-diagnostic.html` — branded artifact page
- `posts/web-experience-capacity-build/assets/templates/team-capacity-diagnostic-blank.html` — blank template
Converted Warehouse card #3 from placeholder `<div>` to live `<a>`.
**Why:** New case study covering EquipmentShare web experience scrum master and team architecture work. Key framework: Role-Weighted Capacity Diagnostic — maps capacity ratios for mixed-discipline teams where upstream roles (POs, designers) outnumber engineering bottlenecks. Artifact credits Nick Sonnenberg (*Come Up for Air*, 2023) for bandwidth calculation methodology and Eliyahu Goldratt for Theory of Constraints. Applied diagnostic (role-weighted mapping) is original.

**Design decisions made during build:**
- Stat box max-width bumped 500px → 750px; padding 1.25rem → 1.75rem 1.5rem; min-width 100px → 140px (labels "Overproduction Ratio" and "What the Governance Produced" were overflowing)
- Artifact page "View Blank Template →" (not "Download") confirmed as standard
- Blank template "Print / Save as PDF" button (not download)
- 20 instances of sub-0.85rem mono text corrected across all three files in a dedicated fix pass
- Director departure reframed: not "survived chaos" but "system was built well enough that leadership was planning to hand it off" — more accurate and consistent with the "survives the exit" brand thesis
- Company never named in copy; senior engineer referred to by role only

---

### SEO round 2: Organization schema, content alignment, freshness dates
**Commit:** `1c41b61`
**What:** Added Organization schema to JSON-LD, aligned content signals, added freshness dates.
**Why:** Follow-up to initial SEO implementation. Structural improvements from an AIView audit — visible text and voice left untouched per brand rules. (A prior audit had recommended keyword-stuffed titles and generic descriptions; those were rejected.)

---

### Headshot easter egg improvements
**Commit:** `3c185c4` / `6ca14c6` / multiple
**What:** Angie's portrait added to footer as hover reveal. 36px circle, grayscale filter, opacity:0 default, reveals on footer hover. Mobile: opacity:0.6 always (no hover on touch).
**Why:** Low-key human signal. Not prominently displayed — intentional restraint.

---

### OG social sharing image
**Commit:** `2aed6f1` / `96a7f08` / `2068abb` / `cc09567`
**What:** Created og-image.png (1200×630). Iterated: started basic, rebuilt with blueprint-grid aesthetic, rosso accent, IBM Plex Mono. Added og:image:width and og:image:height tags.
**Why:** LinkedIn requires explicit image dimensions for reliable detection. `og:image:width` and `og:image:height` are mandatory — do not remove. LinkedIn post inspector was used to force re-scrape after deploy.

---

### Page title simplification
**Commit:** `b202962`
**What:** `<title>`, `og:title`, `twitter:title` all set to just "Angie Bailey." `jobTitle` in JSON-LD set to "Operations Strategist."
**Why:** Angie rejected "Operations Architecture and AI Implementation" (too narrow) and "Transformation Architect" (identity-first, cognitive load). Decision: let the work speak. Visible title is name only. Job title is crawler-only.

---

### Signal → Debrief rename
**Commit:** `413963d`
**What:** Section 04 on index.html renamed from "The Signal" to "The Debrief." Section id changed from `#signal` to `#debrief`. All nav links and back-links across case study pages and artifact pages updated.
**Why:** "Signal" read as AI jargon. "Debrief" won from five alternatives in a live session. All cross-links updated simultaneously — do not re-introduce `#signal`.

---

### Template button standardization
**Commit:** `413963d` (same commit as Signal → Debrief)
**What:** All artifact pages updated to use "View Blank Template →" (not "Download"). `download` attribute removed from all template links.
**Why:** `download` attribute on HTML files caused browsers to download raw HTML source instead of rendering the page. The correct pattern is `target="_blank"` with no `download` attribute. Blank templates themselves use "Print / Save as PDF" (`onclick="window.print()"`).

---

### Yellow flag color fix
**Commit:** `234b57e`
**What:** Yellow constraint flags across all artifact pages corrected to `#D4A843`.
**Why:** Yellow flags were rendering as quetzal-bright (green) — the wrong color. Green flags were rendering as ecru-dim (beige) — also wrong. Both fixed. Yellow is hardcoded `#D4A843` because it was added after the original CSS variable set and never got a variable.

---

### E-Commerce P&L Build — case study launched
**Commit:** `b5c0669`
**What:** Added case study page and artifact pages for E-Commerce P&L Build.
**Why:** Second case study. Decision infrastructure framing. Covers building the first e-commerce P&L for a company that tracked revenue but not profitability by channel.

---

### Dossier → Brief rename
**Commit:** `06278b7`
**What:** All user-facing display text changed from "Dossier" to "Project Brief" or "Brief." File names preserved (renaming would break existing URLs).
**Why:** Angie didn't want the word "dossier" in any visible copy. File paths still say `dossier` — this is intentional to preserve URLs. Do not rename the files.

---

### Cross-links between artifacts
**Commit:** `06278b7` (same commit as Dossier → Brief)
**What:** Related Work sections added to bottom of artifact pages where methodology overlaps (P&L and Summit case studies).
**Why:** Users landing on one artifact may have arrived from the other case study's ecosystem. Cross-links increase discovery without requiring a nav overhaul.

---

### Summit artifact back-link fix
**Commit:** (part of early summit iteration commits)
**What:** Summit artifact back-links corrected from `/cases/e-commerce-summit.html` to `../e-commerce-summit.html`.
**Why:** Path was wrong — linked to a non-existent `/cases/` directory. Relative paths are required.

---

### Multi-Team Roadmap Summit — case study launched
**Commit:** Early commits (`07a6c6a`, `3c215c4`, `624c100`)
**What:** First case study added. Five artifact pages, five blank templates.
**Why:** Summit case study was the first production build of the Durable Births design system.

---

## Format for New Entries

Copy this block and fill in:

```
### {Short title of change}
**Commit:** `{hash}` (or "no commit — edit in progress")
**What:** One paragraph description of what was changed, what files were touched.
**Why:** The reasoning. What decision was made and why. If overriding a previous decision, note what changed.
```
