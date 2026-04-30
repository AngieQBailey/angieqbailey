## [2026-04-27] — TIER 3 — Start Here (New Page)
**Change:** Deployed /start-here/index.html — interactive AI context builder. Single self-contained file (62 KB). Four-card questionnaire that generates a personal AI profile users can paste into any AI tool. GA4 tag injected. All dependencies CDN or inline.
**Rationale:** Lead-gen and value-delivery tool for LinkedIn Content Engine. Gives visitors an immediate, useful artifact while introducing Angie's methodology.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-04-26] — TIER 2 — Warehouse
**Change:** Added Marketing Infrastructure MBR Debt Clearance case study. 1 case study page (dark-variant), 2 branded artifact pages (Cross-Functional MBR Template, Reporting Governance Cadence), 2 blank downloadable templates, 1 companion .docx narrative. MBR Warehouse card added as first card in grid. TBA placeholder card added as last card. Warehouse card limit overridden from 8 to 10. Collapsed card padding tightened with hover transition.
**Rationale:** New case study showcasing unified reporting infrastructure build across 13 marketing functions and 10+ data platforms for a $1B+ organization. Demonstrates strategic operations and governance methodology capabilities.
**Operator:** Angie Bailey + Claude via Cowork

### 2026-04-25 — Site Architecture Overhaul + Verdict Essays + L&D Landing Page
- Restructured: index.html now has 5 numbered sections (Investigation, Warehouse, R&D, L&D, Verdict) + unnumbered Debrief
- Added: `ld/infrastructure-of-a-life.html` (L&D landing page with two collections)
- Added: `verdict/add-value-not-noise.html` (Verdict essay, Principle 01)
- Added: `verdict/vocabulary-is-the-barrier.html` (Verdict essay, Principle 02)
- Added: `verdict/reality-before-theory.html` (Verdict essay, Principle 03)
- Added: `verdict/structure-is-how-you-protect-people.html` (Verdict essay, Principle 04)
- Added: `verdict/the-implementation-failed-not-the-people.html` (Verdict essay, Principle 05)
- Changed: R&D and L&D broken out of Warehouse into own sections (03, 04)
- Changed: Verdict principles now clickable links to essay pages
- Changed: Warehouse cards collapse text/metric by default, unfurl on hover
- L&D Collections: "Dots, Good Pens & a Commonplace Book: A Supply Closet Romance" (4 reworking) + "Em-Dash Unpacking: Thief by Mass Visual Weaponization" (4 coming)

### 2026-04-24 — The GEO/AEO Transition
- Added: `posts/geo-aeo-transition/geo-aeo-transition.html` (case study page)
- Added: `posts/geo-aeo-transition/assets/ai-overview-monitoring-guide.html` (artifact page)
- Added: `posts/geo-aeo-transition/assets/content-prioritization-framework.html` (artifact page)
- Added: `posts/geo-aeo-transition/assets/geo-best-practices-guide.html` (artifact page)
- Added: `posts/geo-aeo-transition/assets/schema-markup-ai-content-guide.html` (artifact page)
- Added: `posts/geo-aeo-transition/assets/seo-ai-search-playbook.html` (artifact page)
- Added: `posts/geo-aeo-transition/assets/content-brief-template.html` (artifact page)
- Added: `posts/geo-aeo-transition/assets/templates/*-blank.html` (6 blank templates)
- Added: Warehouse card to `index.html` (position 2, top row)
- Moved: AI Implementation/Workforce AI Adoption card to position 1, top row
- Category: Process Architecture // AI Search Readiness
- Artifacts: 6 branded pages, 6 blank templates

# AQB Site Changelog
**Repo:** `AngieQBailey/angieqbailey`

Running record of what changed, when, and why. Git commits are terse. This document captures the reasoning. Add an entry any time content is added, updated, or removed. Most recent entries at top.

---

## March 2026

### Crisis Communications Architecture + Enterprise Newsletter Architecture deployed
**Commit:** Series of commits via GitHub API, March 29-30 2026
**What:** Two new case studies deployed: Crisis Communications Architecture (main page, warehouse card, blank holding statements template) and Enterprise Newsletter Architecture (main page with yellow flag CSS fix). Yellow flag color corrected from `var(--quetzal)` to `#D4A017` on Enterprise Newsletter page.

**Files added:**
- `posts/crisis-communications-architecture/crisis-communications-architecture.html` - Main case study page
- `posts/crisis-communications-architecture/warehouse-card.html` - Warehouse card
- `posts/crisis-communications-architecture/assets/templates/crisis-holding-statements-blank.html` - Blank template (15 holding statement types)
- `posts/enterprise-newsletter-architecture/enterprise-newsletter-architecture.html` - Main case study page

**Bug fix:**
- Yellow constraint flags on Enterprise Newsletter page were rendering green. `.constraint-flag.yellow` CSS rule was using `var(--quetzal)` for color and border. Fixed to hardcoded `#D4A017` (warm gold). The Analytical Palette has no yellow, so this is the one UI color that does not map to a CSS variable.

**Why:** These case studies extend the portfolio into communications architecture and crisis infrastructure. The crisis comms page includes a four-tier severity escalation system, three-tier response teams, 15 holding statements, deskless workforce channel protocols, and disaster response decision framework. The newsletter page documents a channel audit, business case ($12,506/employee), CEO pitch, HRIS subscriber infrastructure, and editorial governance system that drove open rates from 9% to 95%+.


### Post-Acquisition Integration Launch â full case study deployed
**Commit:** Series of commits via GitHub API, March 29â30 2026
**What:** Full case study deployed: main page, 4 branded artifact pages, 3 blank templates, and warehouse card. Warehouse card on index.html converted from placeholder to live link with forensic copy and Scope // Output metrics.

**Files added:**
- `posts/post-acquisition-integration-launch/post-acquisition-integration-launch.html` â Main case study page
- `posts/post-acquisition-integration-launch/warehouse-card.html` â Warehouse card
- `posts/post-acquisition-integration-launch/assets/vendor-governance-model.html` â Branded artifact
- `posts/post-acquisition-integration-launch/assets/product-taxonomy-architecture.html` â Branded artifact
- `posts/post-acquisition-integration-launch/assets/cross-functional-workback.html` â Branded artifact
- `posts/post-acquisition-integration-launch/assets/templates/system-integration-sequence-blank.html` â Blank template
- `posts/post-acquisition-integration-launch/assets/templates/vendor-governance-model-blank.html` â Blank template
- `posts/post-acquisition-integration-launch/assets/templates/product-taxonomy-architecture-blank.html` â Blank template

**Files modified:**
- `index.html` â Post-Acquisition warehouse card converted from `<div>` placeholder to live `<a>` with forensic copy, Scope // Output metrics, "Ops Management" tag

**Why:** Fifth client case study. Post-acquisition integration operations covering vendor governance, product taxonomy architecture, system integration sequencing and cross-functional workback for a multi-brand merger.

### Post-Acquisition Integration Launch â post-deployment refinements
**Commit:** Series of commits via GitHub API, March 30 2026
**What:** Multiple UX and cross-linking improvements across the case study and site-wide.

**Changes:**
- System Integration Sequence Map: "Break" button CTA changed to "What breaks?" for clearer intent. Button restyled â larger font (0.7rem to 0.85rem), ecru text on rosso-tinted background with visible border. Vertical text orientation removed (was `writing-mode: vertical-rl`).
- Cross-Functional Workback: Related Work section added linking to Summit's Dependency Friction Map and Pressure Points Register
- Vendor Governance Model: Related Work section added linking to Summit's Expectations SLA Stress Test
- White flash fix: `style="background-color: #121A28"` (dark pages) or `#F5F5DC` (ecru pages) added to `<html>` tag on all 50 HTML files site-wide. Eliminates white frame between page transitions.
- Same-tab navigation: `target="_blank"` removed from all internal links across index.html, 6 case study pages, and 15 artifact pages. Only external links (LinkedIn) retain new-tab behavior.

**Files modified:**
- All 50 HTML files (inline bg on `<html>` tag)
- `index.html` (warehouse card `target="_blank"` removal)
- 6 case study main pages (`target="_blank"` removal from artifact links)
- 15 artifact pages (`target="_blank"` removal from cross-links)
- `posts/post-acquisition-integration-launch/assets/system-integration-sequence.html` (CTA and button styling)
- `posts/post-acquisition-integration-launch/assets/cross-functional-workback.html` (Related Work section)
- `posts/post-acquisition-integration-launch/assets/vendor-governance-model.html` (Related Work section)

**Why:** Polish pass. The interactive sequence map's "Break" label was ambiguous and hard to read. Cross-links between case studies reinforce that the diagnostic methodology is a system, not one-off work. White flash and new-tab behavior were degrading the dark-theme experience.

### Case study page titles aligned with Warehouse card names
**Commit:** Series of commits via GitHub API, March 28 2026
**What:** Updated the Enterprise Newsletter case study page (title tag, h1, OG meta tags) from "Enterprise Newsletter Architecture" to "Enterprise Newsletter Launch." Updated the Web Experience case study page from "Web Experience Capacity Build" to "Web Experience Capacity Expansion." Folder paths and filenames unchanged to preserve existing URLs. Site registry updated with full enumerated file inventory for Crisis Communications (replaced generic "6 additional assets" with specific filenames). Handoff doc updated to reflect titles are now aligned.

**Files modified:**
- `posts/enterprise-newsletter-architecture/enterprise-newsletter-architecture.html` â Title, h1 accent word, OG tags
- `posts/web-experience-capacity-build/web-experience-capacity-build.html` â Title, h1 accent word, OG tags
- `_site-registry.md` â Full Crisis Comms file inventory, Newsletter section title
- `AQB Website â Session Handoff.md` â Updated card/title alignment rules

**Why:** Warehouse card titles and case study page h1s were out of sync after the earlier rename. Brought everything into alignment so users land on a page whose title matches what they clicked.

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
- `index.html` Ã¢ÂÂ Two new Warehouse cards added

**Why:** Expanding the portfolio with two new case studies demonstrating internal communications and crisis response architecture work.

### Warehouse card reorder + naming updates + nesting fix
**Commit:** Series of commits via GitHub API, March 28 2026
**What:** Moved Enterprise Newsletter and Crisis Communications cards out of the R&D section into the main Warehouse grid. Retitled "Enterprise Newsletter Architecture" to "Enterprise Newsletter Launch." Retitled "Web Experience Capacity Build" to "Web Experience Capacity Expansion" across index.html. Fixed a missing `</div>` on the Workforce AI Adoption card that was causing the comms cards to nest inside it (overlap/stacking bug). Reordered cards: Multi-Team Roadmap Summit, E-Commerce P&L Build, Web Experience Capacity Expansion, Post-Acquisition Integration, Enterprise Newsletter Launch, Crisis Communications Architecture, Workforce AI Adoption (last, since it is not yet built out).

**Files modified:**
- `index.html` Ã¢ÂÂ Card moves, renames, reorder, nesting fix

**Why:** The two comms case studies are complete work, not R&D. Workforce AI moved to last position since its case study page does not exist yet. The nesting bug was caused by the Workforce AI `<div class="evidence-card">` missing its closing `</div>`, which caused subsequent `<a>` cards to render inside it.

### DRS Matrix page deployed + R&D section added to Warehouse
**Commits:** `18f9e90` through `7e5a536` (series of commits, March 22 2026)
**What:** New page at `drs-matrix/index.html` combining "The 9:02 AM Meeting" mini-fable with the interactive DRS 2ÃÂÃÂ2 matrix widget. Added "R&D // Frameworks Under Construction" subsection to Warehouse on index.html with a Quetzal-tinted card linking to the new page (opens in new tab). Headshot in footer now links to LinkedIn with hover CTA.

**Files added:**
- `drs-matrix/index.html` ÃÂ¢ÃÂÃÂ Full page: fable narrative + interactive widget + print stylesheet

**Files modified:**
- `index.html` ÃÂ¢ÃÂÃÂ Added R&D subsection CSS (lab-divider, lab-grid, lab-card, series-status), DRS card, headshot wrapped in LinkedIn link with hover CTA, footer overflow fixes

**Key design decisions:**
- R&D section uses Quetzal-tinted card backgrounds (`rgba(0,104,94,0.12)`) and Quetzal-bright accent line on hover to visually distinguish from client case study cards (which use ecru-ghost backgrounds and rosso accent lines)
- R&D label matches `section-label` pattern (0.85rem, weight 700, letter-spacing 0.2em, Quetzal bright)
- Lab title at `clamp(1.4rem, 3vw, 2rem)` weight 900 ÃÂ¢ÃÂÃÂ sits between section h2 and card titles in the hierarchy
- DRS page is light/ecru variant (not dark Durable Births) ÃÂ¢ÃÂÃÂ appropriate for thought leadership content vs. client case studies
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
**What:** Restored Post-Acquisition Integration placeholder card (had been accidentally replaced). Reordered Warehouse grid to: Summit ÃÂ¢ÃÂÃÂ P&L Build ÃÂ¢ÃÂÃÂ Web Experience Capacity Build ÃÂ¢ÃÂÃÂ Post-Acquisition Integration ÃÂ¢ÃÂÃÂ Workforce AI Adoption. Renamed Summit card title from "E-Commerce Strategic Summit Cross-Functional Alignment" to "Multi-Team Roadmap Summit."
**Why:** Previous edit replaced the wrong card when adding Web Experience. Summit card title was too long and jammed ÃÂ¢ÃÂÃÂ two lines of text in a card label is not the pattern. Card title is a fast read; case study page h1 is the full forensic record. They are allowed to differ.

---

### Web Experience Capacity Build ÃÂ¢ÃÂÃÂ full case study launched
**Commit:** `c385711`
**What:** Added three new files:
- `posts/web-experience-capacity-build/web-experience-capacity-build.html` ÃÂ¢ÃÂÃÂ main case study page
- `posts/web-experience-capacity-build/assets/team-capacity-diagnostic.html` ÃÂ¢ÃÂÃÂ branded artifact page
- `posts/web-experience-capacity-build/assets/templates/team-capacity-diagnostic-blank.html` ÃÂ¢ÃÂÃÂ blank template
Converted Warehouse card #3 from placeholder `<div>` to live `<a>`.
**Why:** New case study covering web experience scrum master and team architecture work for a high-growth industrial technology company. Key framework: Role-Weighted Capacity Diagnostic ÃÂ¢ÃÂÃÂ maps capacity ratios for mixed-discipline teams where upstream roles (POs, designers) outnumber engineering bottlenecks. Artifact credits Nick Sonnenberg (*Come Up for Air*, 2023) for bandwidth calculation methodology and Eliyahu Goldratt for Theory of Constraints. Applied diagnostic (role-weighted mapping) is original.

**Design decisions made during build:**
- Stat box max-width bumped 500px ÃÂ¢ÃÂÃÂ 750px; padding 1.25rem ÃÂ¢ÃÂÃÂ 1.75rem 1.5rem; min-width 100px ÃÂ¢ÃÂÃÂ 140px (labels "Overproduction Ratio" and "What the Governance Produced" were overflowing)
- Artifact page "View Blank Template ÃÂ¢ÃÂÃÂ" (not "Download") confirmed as standard
- Blank template "Print / Save as PDF" button (not download)
- 20 instances of sub-0.85rem mono text corrected across all three files in a dedicated fix pass
- Director departure reframed: not "survived chaos" but "system was built well enough that leadership was planning to hand it off" ÃÂ¢ÃÂÃÂ more accurate and consistent with the "survives the exit" brand thesis
- Company never named in copy; senior engineer referred to by role only

---

### SEO round 2: Organization schema, content alignment, freshness dates
**Commit:** `1c41b61`
**What:** Added Organization schema to JSON-LD, aligned content signals, added freshness dates.
**Why:** Follow-up to initial SEO implementation. Structural improvements from an AIView audit ÃÂ¢ÃÂÃÂ visible text and voice left untouched per brand rules. (A prior audit had recommended keyword-stuffed titles and generic descriptions; those were rejected.)

---

### Headshot easter egg improvements
**Commit:** `3c185c4` / `6ca14c6` / multiple
**What:** Angie's portrait added to footer as hover reveal. 36px circle, grayscale filter, opacity:0 default, reveals on footer hover. Mobile: opacity:0.6 always (no hover on touch).
**Why:** Low-key human signal. Not prominently displayed ÃÂ¢ÃÂÃÂ intentional restraint.

---

### OG social sharing image
**Commit:** `2aed6f1` / `96a7f08` / `2068abb` / `cc09567`
**What:** Created og-image.png (1200ÃÂÃÂ630). Iterated: started basic, rebuilt with blueprint-grid aesthetic, rosso accent, IBM Plex Mono. Added og:image:width and og:image:height tags.
**Why:** LinkedIn requires explicit image dimensions for reliable detection. `og:image:width` and `og:image:height` are mandatory ÃÂ¢ÃÂÃÂ do not remove. LinkedIn post inspector was used to force re-scrape after deploy.

---

### Page title simplification
**Commit:** `b202962`
**What:** `<title>`, `og:title`, `twitter:title` all set to just "Angie Bailey." `jobTitle` in JSON-LD set to "Operations Strategist."
**Why:** Angie rejected "Operations Architecture and AI Implementation" (too narrow) and "Transformation Architect" (identity-first, cognitive load). Decision: let the work speak. Visible title is name only. Job title is crawler-only.

---

### Signal ÃÂ¢ÃÂÃÂ Debrief rename
**Commit:** `413963d`
**What:** Section 04 on index.html renamed from "The Signal" to "The Debrief." Section id changed from `#signal` to `#debrief`. All nav links and back-links across case study pages and artifact pages updated.
**Why:** "Signal" read as AI jargon. "Debrief" won from five alternatives in a live session. All cross-links updated simultaneously ÃÂ¢ÃÂÃÂ do not re-introduce `#signal`.

---

### Template button standardization
**Commit:** `413963d` (same commit as Signal ÃÂ¢ÃÂÃÂ Debrief)
**What:** All artifact pages updated to use "View Blank Template ÃÂ¢ÃÂÃÂ" (not "Download"). `download` attribute removed from all template links.
**Why:** `download` attribute on HTML files caused browsers to download raw HTML source instead of rendering the page. The correct pattern is `target="_blank"` with no `download` attribute. Blank templates themselves use "Print / Save as PDF" (`onclick="window.print()"`).

---

### Yellow flag color fix
**Commit:** `234b57e`
**What:** Yellow constraint flags across all artifact pages corrected to `#D4A843`.
**Why:** Yellow flags were rendering as quetzal-bright (green) ÃÂ¢ÃÂÃÂ the wrong color. Green flags were rendering as ecru-dim (beige) ÃÂ¢ÃÂÃÂ also wrong. Both fixed. Yellow is hardcoded `#D4A843` because it was added after the original CSS variable set and never got a variable.

---

### E-Commerce P&L Build ÃÂ¢ÃÂÃÂ case study launched
**Commit:** `b5c0669`
**What:** Added case study page and artifact pages for E-Commerce P&L Build.
**Why:** Second case study. Decision infrastructure framing. Covers building the first e-commerce P&L for a company that tracked revenue but not profitability by channel.

---

### Dossier ÃÂ¢ÃÂÃÂ Brief rename
**Commit:** `06278b7`
**What:** All user-facing display text changed from "Dossier" to "Project Brief" or "Brief." File names preserved (renaming would break existing URLs).
**Why:** Angie didn't want the word "dossier" in any visible copy. File paths still say `dossier` ÃÂ¢ÃÂÃÂ this is intentional to preserve URLs. Do not rename the files.

---

### Cross-links between artifacts
**Commit:** `06278b7` (same commit as Dossier ÃÂ¢ÃÂÃÂ Brief)
**What:** Related Work sections added to bottom of artifact pages where methodology overlaps (P&L and Summit case studies).
**Why:** Users landing on one artifact may have arrived from the other case study's ecosystem. Cross-links increase discovery without requiring a nav overhaul.

---

### Summit artifact back-link fix
**Commit:** (part of early summit iteration commits)
**What:** Summit artifact back-links corrected from `/cases/e-commerce-summit.html` to `../e-commerce-summit.html`.
**Why:** Path was wrong ÃÂ¢ÃÂÃÂ linked to a non-existent `/cases/` directory. Relative paths are required.

---

### Multi-Team Roadmap Summit ÃÂ¢ÃÂÃÂ case study launched
**Commit:** Early commits (`07a6c6a`, `3c215c4`, `624c100`)
**What:** First case study added. Five artifact pages, five blank templates.
**Why:** Summit case study was the first production build of the Durable Births design system.

---

## Format for New Entries

Copy this block and fill in:

```
### {Short title of change}
**Commit:** `{hash}` (or "no commit ÃÂ¢ÃÂÃÂ edit in progress")
**What:** One paragraph description of what was changed, what files were touched.
**Why:** The reasoning. What decision was made and why. If overriding a previous decision, note what changed.
```
