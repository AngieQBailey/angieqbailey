# AQB Site Changelog
**Repo:** `AngieQBailey/angieqbailey`

Running record of what changed, when, and why. Git commits are terse. This document captures the reasoning. Add an entry any time content is added, updated, or removed. Most recent entries at top.

---

## March 2026

### Enterprise Newsletter Launch + Crisis Communications Architecture deployed
**Commit:** Series of commits via GitHub API, March 28 2026
**What:** Two full case studies deployed to the site. Enterprise Newsletter Launch includes the main case study page plus 6 artifact subpages (interactive-channel-audit, in-house-style-guide, channel-mix-matrix, ic-strategic-value-architecture, internal-comms-channel-audit) and 3 blank templates. Crisis Communications Architecture includes the main case study page plus 4 artifact subpages (crisis-holding-statements, interactive-crisis-assessment, crisis-response-team-architecture) and 6 additional assets. Warehouse cards added to index.html for both.

**Files added:**
- `posts/enterprise-newsletter-architecture/enterprise-newsletter-architecture.html`
- `posts/enterprise-newsletter-architecture/assets/*.html` (6 artifact pages)
- `posts/enterprise-newsletter-architecture/assets/templates/*.html` (3 blank templates)
- `posts/crisis-communications-architecture/crisis-communications-architecture.html`
- `posts/crisis-communications-architecture/assets/*.html` (4 artifact pages + 6 additional assets)

**Files modified:**
- `index.html` — Two new Warehouse cards added

**Why:** Expanding the portfolio with two new case studies demonstrating internal communications and crisis response architecture work.

### Warehouse card reorder + naming updates + nesting fix
**Commit:** Series of commits via GitHub API, March 28 2026
**What:** Moved Enterprise Newsletter and Crisis Communications cards out of the R&D section into the main Warehouse grid. Retitled "Enterprise Newsletter Architecture" to "Enterprise Newsletter Launch." Retitled "Web Experience Capacity Build" to "Web Experience Capacity Expansion" across index.html. Fixed a missing `</div>` on the Workforce AI Adoption card that was causing the comms cards to nest inside it (overlap/stacking bug). Reordered cards: Multi-Team Roadmap Summit, E-Commerce P&L Build, Web Experience Capacity Expansion, Post-Acquisition Integration, Enterprise Newsletter Launch, Crisis Communications Architecture, Workforce AI Adoption (last, since it is not yet built out).

**Files modified:**
- `index.html` — Card moves, renames, reorder, nesting fix

**Why:** The two comms case studies are complete work, not R&D. Workforce AI moved to last position since its case study page does not exist yet. The nesting bug was caused by the Workforce AI `<div class="evidence-card">` missing its closing `</div>`, which caused subsequent `<a>` cards to render inside it.

### DRS Matrix page deployed + R&D section added to Warehouse
**Commits:** `18f9e90` through `7e5a536` (series of commits, March 22 2026)
**What:** New page at `drs-matrix/index.html` combining "The 9:02 AM Meeting" mini-fable with the interactive DRS 2Ã2 matrix widget. Added "R&D // Frameworks Under Construction" subsection to Warehouse on index.html with a Quetzal-tinted card linking to the new page (opens in new tab). Headshot in footer now links to LinkedIn with hover CTA.

**Files added:**
- `drs-matrix/index.html` â Full page: fable narrative + interactive widget + print stylesheet

**Files modified:**
- `index.html` â Added R&D subsection CSS (lab-divider, lab-grid, lab-card, series-status), DRS card, headshot wrapped in LinkedIn link with hover CTA, footer overflow fixes

**Key design decisions:**
- R&D section uses Quetzal-tinted card backgrounds (`rgba(0,104,94,0.12)`) and Quetzal-bright accent line on hover to visually distinguish from client case study cards (which use ecru-ghost backgrounds and rosso accent lines)
- R&D label matches `section-label` pattern (0.85rem, weight 700, letter-spacing 0.2em, Quetzal bright)
- Lab title at `clamp(1.4rem, 3vw, 2rem)` weight 900 â sits between section h2 and card titles in the hierarchy
- DRS page is light/ecru variant (not dark Durable Births) â appropriate for thought leadership content vs. client case studies
- Matrix widget: solid Quetzal quadrant backgrounds, Parisian Night on click, 2px borders on axis labels, click-outside-to-close
- "See where you sit" CTA button at top of page (jump to widget), "Print / Save as PDF" button under "Explore the model" label at bottom of fable
- Print stylesheet: portrait orientation, 1cm margins, hides fable/nav/footer, scales widget typography to fit one page, forces color printing
- Plausible analytics script in `<head>` (requires account setup to activate)
- Headshot: click goes to `linkedin.com/in/angie-bailey/`, hover scales to 2.8x with "Connect on LinkedIn" CTA text above image
- "Cognitive State (Bandwidth)" axis label sits above Surplus/Deficit (mirrors Identity Source placement on y-axis)

**LinkedIn strategy note:** The DRS page is the conversion destination for a LinkedIn test post (Chunk 2). URL should be shared in the first pinned comment with UTM parameters (`?utm_source=linkedin&utm_medium=social&utm_campaign=drs-chunk2`), NOT in the post body, to preserve embedding quality and on-platform engagement signals. See Trust Insights Q1 2026 LinkedIn Algorithm Guide analysis in the session handoff.

---

### Warehouse grid reorder + Summit card title fix
**Commit:** `831e0ed` / `7053125`
**What:** Restored Post-Acquisition Integration placeholder card (had been accidentally replaced). Reordered Warehouse grid to: Summit â P&L Build â Web Experience Capacity Build â Post-Acquisition Integration â Workforce AI Adoption. Renamed Summit card title from "E-Commerce Strategic Summit Cross-Functional Alignment" to "Multi-Team Roadmap Summit."
**Why:** Previous edit replaced the wrong card when adding Web Experience. Summit card title was too long and jammed â two lines of text in a card label is not the pattern. Card title is a fast read; case study page h1 is the full forensic record. They are allowed to differ.

---

### Web Experience Capacity Build â full case study launched
**Commit:** `c385711`
**What:** Added three new files:
- `posts/web-experience-capacity-build/web-experience-capacity-build.html` â main case study page
- `posts/web-experience-capacity-build/assets/team-capacity-diagnostic.html` â branded artifact page
- `posts/web-experience-capacity-build/assets/templates/team-capacity-diagnostic-blank.html` â blank template
Converted Warehouse card #3 from placeholder `<div>` to live `<a>`.
**Why:** New case study covering EquipmentShare web experience scrum master and team architecture work. Key framework: Role-Weighted Capacity Diagnostic â maps capacity ratios for mixed-discipline teams where upstream roles (POs, designers) outnumber engineering bottlenecks. Artifact credits Nick Sonnenberg (*Come Up for Air*, 2023) for bandwidth calculation methodology and Eliyahu Goldratt for Theory of Constraints. Applied diagnostic (role-weighted mapping) is original.

**Design decisions made during build:**
- Stat box max-width bumped 500px â 750px; padding 1.25rem â 1.75rem 1.5rem; min-width 100px â 140px (labels "Overproduction Ratio" and "What the Governance Produced" were overflowing)
- Artifact page "View Blank Template â" (not "Download") confirmed as standard
- Blank template "Print / Save as PDF" button (not download)
- 20 instances of sub-0.85rem mono text corrected across all three files in a dedicated fix pass
- Director departure reframed: not "survived chaos" but "system was built well enough that leadership was planning to hand it off" â more accurate and consistent with the "survives the exit" brand thesis
- Company never named in copy; senior engineer referred to by role only

---

### SEO round 2: Organization schema, content alignment, freshness dates
**Commit:** `1c41b61`
**What:** Added Organization schema to JSON-LD, aligned content signals, added freshness dates.
**Why:** Follow-up to initial SEO implementation. Structural improvements from an AIView audit â visible text and voice left untouched per brand rules. (A prior audit had recommended keyword-stuffed titles and generic descriptions; those were rejected.)

---

### Headshot easter egg improvements
**Commit:** `3c185c4` / `6ca14c6` / multiple
**What:** Angie's portrait added to footer as hover reveal. 36px circle, grayscale filter, opacity:0 default, reveals on footer hover. Mobile: opacity:0.6 always (no hover on touch).
**Why:** Low-key human signal. Not prominently displayed â intentional restraint.

---

### OG social sharing image
**Commit:** `2aed6f1` / `96a7f08` / `2068abb` / `cc09567`
**What:** Created og-image.png (1200Ã630). Iterated: started basic, rebuilt with blueprint-grid aesthetic, rosso accent, IBM Plex Mono. Added og:image:width and og:image:height tags.
**Why:** LinkedIn requires explicit image dimensions for reliable detection. `og:image:width` and `og:image:height` are mandatory â do not remove. LinkedIn post inspector was used to force re-scrape after deploy.

---

### Page title simplification
**Commit:** `b202962`
**What:** `<title>`, `og:title`, `twitter:title` all set to just "Angie Bailey." `jobTitle` in JSON-LD set to "Operations Strategist."
**Why:** Angie rejected "Operations Architecture and AI Implementation" (too narrow) and "Transformation Architect" (identity-first, cognitive load). Decision: let the work speak. Visible title is name only. Job title is crawler-only.

---

### Signal â Debrief rename
**Commit:** `413963d`
**What:** Section 04 on index.html renamed from "The Signal" to "The Debrief." Section id changed from `#signal` to `#debrief`. All nav links and back-links across case study pages and artifact pages updated.
**Why:** "Signal" read as AI jargon. "Debrief" won from five alternatives in a live session. All cross-links updated simultaneously â do not re-introduce `#signal`.

---

### Template button standardization
**Commit:** `413963d` (same commit as Signal â Debrief)
**What:** All artifact pages updated to use "View Blank Template â" (not "Download"). `download` attribute removed from all template links.
**Why:** `download` attribute on HTML files caused browsers to download raw HTML source instead of rendering the page. The correct pattern is `target="_blank"` with no `download` attribute. Blank templates themselves use "Print / Save as PDF" (`onclick="window.print()"`).

---

### Yellow flag color fix
**Commit:** `234b57e`
**What:** Yellow constraint flags across all artifact pages corrected to `#D4A843`.
**Why:** Yellow flags were rendering as quetzal-bright (green) â the wrong color. Green flags were rendering as ecru-dim (beige) â also wrong. Both fixed. Yellow is hardcoded `#D4A843` because it was added after the original CSS variable set and never got a variable.

---

### E-Commerce P&L Build â case study launched
**Commit:** `b5c0669`
**What:** Added case study page and artifact pages for E-Commerce P&L Build.
**Why:** Second case study. Decision infrastructure framing. Covers building the first e-commerce P&L for a company that tracked revenue but not profitability by channel.

---

### Dossier â Brief rename
**Commit:** `06278b7`
**What:** All user-facing display text changed from "Dossier" to "Project Brief" or "Brief." File names preserved (renaming would break existing URLs).
**Why:** Angie didn't want the word "dossier" in any visible copy. File paths still say `dossier` â this is intentional to preserve URLs. Do not rename the files.

---

### Cross-links between artifacts
**Commit:** `06278b7` (same commit as Dossier â Brief)
**What:** Related Work sections added to bottom of artifact pages where methodology overlaps (P&L and Summit case studies).
**Why:** Users landing on one artifact may have arrived from the other case study's ecosystem. Cross-links increase discovery without requiring a nav overhaul.

---

### Summit artifact back-link fix
**Commit:** (part of early summit iteration commits)
**What:** Summit artifact back-links corrected from `/cases/e-commerce-summit.html` to `../e-commerce-summit.html`.
**Why:** Path was wrong â linked to a non-existent `/cases/` directory. Relative paths are required.

---

### Multi-Team Roadmap Summit â case study launched
**Commit:** Early commits (`07a6c6a`, `3c215c4`, `624c100`)
**What:** First case study added. Five artifact pages, five blank templates.
**Why:** Summit case study was the first production build of the Durable Births design system.

---

## Format for New Entries

Copy this block and fill in:

```
### {Short title of change}
**Commit:** `{hash}` (or "no commit â edit in progress")
**What:** One paragraph description of what was changed, what files were touched.
**Why:** The reasoning. What decision was made and why. If overriding a previous decision, note what changed.
```
