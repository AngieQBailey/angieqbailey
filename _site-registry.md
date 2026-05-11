# AQB Site Registry
**Last updated:** May 2026
**Repo:** `AngieQBailey/angieqbailey` | **Branch:** `main` | **Host:** GitHub Pages — `angieqbailey.com`

This is the authoritative file inventory. Update this document any time a file is added, removed, renamed or promoted from placeholder to live. Do not let it drift.

---

## Site Architecture

The index.html homepage has **5 numbered sections** plus Resources and Debrief:

| # | Section | Anchor | Description |
|---|---------|--------|-------------|
| 01 | Investigation | `#investigation` | Hero + positioning statement |
| 02 | Warehouse | `#warehouse` | Client case study card grid (8 live + 1 TBA placeholder) |
| 03 | R&D | `#rnd` | Frameworks under construction (Hello World toolkit, DRS Matrix) |
| 04 | L&D | `#lnd` | Learning & Development collections |
| 05 | Verdict | `#verdict` | 5 operating principles with linked essay pages |
| — | Resources | `/resources/` | External link in nav to Resources landing page |
| — | Debrief | `#debrief` | Footer section with contact, headshot easter egg |

**Nav:** 7-item horizontal nav — Investigation, Warehouse, R&D, L&D, Verdict, Resources, Debrief

---

## Root Files

| File | Purpose | Notes |
|------|---------|-------|
| `index.html` | Main site — single file, all CSS/JS embedded | Contains Warehouse card grid, nav, hero, all 5 sections, Debrief, footer |
| `CNAME` | GitHub Pages custom domain config | Contains: `angieqbailey.com` |
| `README.md` | Minimal deployment notes | Not public-facing |
| `favicon.png` | AB monogram favicon, 192x192 | Parisian Night bg, ecru text, quetzal-bright accent bar |
| `favicon-32.png` | 32px favicon variant | Same design |
| `favicon.ico` | Multi-size .ico (16, 32, 48) | Linked via `<link rel="icon">` and `<link rel="apple-touch-icon">` |
| `headshot.png` | Angie's portrait, 128x128 | Footer easter egg — opacity:0 default, reveals on footer hover |
| `og-image.png` | Social sharing preview, 1200x630 | Blueprint-grid aesthetic, IBM Plex Mono, Parisian Night + quetzal grid + rosso accent |

---

## Warehouse Cards (index.html)

Current order and status. Live cards are `<a>` elements. Placeholders are `<div>` elements.

| # | Card Title | Category | Status | Link Target |
|---|------------|----------|--------|-------------|
| 1 | Marketing Infrastructure MBR Debt Clearance | Strategic Operations | **LIVE** | `posts/marketing-infrastructure-mbr/marketing-infrastructure-mbr.html` |
| 2 | The GEO/AEO Transition | Process Architecture // AI Search Readiness | **LIVE** | `posts/geo-aeo-transition/geo-aeo-transition.html` |
| 3 | Multi-Team Roadmap Summit | Strategic Operations | **LIVE** | `posts/e-commerce-summit/e-commerce-summit.html` |
| 4 | E-Commerce P&L Build | Decision Infrastructure | **LIVE** | `posts/ecommerce-pl/ecommerce-pl.html` |
| 5 | Web Experience Capacity Expansion | Delivery Governance | **LIVE** | `posts/web-experience-capacity-build/web-experience-capacity-build.html` |
| 6 | Post-Acquisition Integration Launch | Strategic Revenue Ops | **LIVE** | `posts/post-acquisition-integration-launch/post-acquisition-integration-launch.html` |
| 7 | Enterprise Newsletter Launch | Channel Strategy | **LIVE** | `posts/enterprise-newsletter-architecture/enterprise-newsletter-architecture.html` |
| 8 | Crisis Communications Architecture | Strategic Communications | **LIVE** | `posts/crisis-communications-architecture/crisis-communications-architecture.html` |

**Rule:** Card titles and case study page h1s do not need to match. The card is the fast read. The page h1 is the forensic record. Do not "fix" discrepancies.

---

## R&D Section (Section 03)

Below the client case study grid, a separate subsection with its own visual treatment.

| # | Card Title | Status | Link Target |
|---|------------|--------|-------------|
| R1 | Hello, World (...of AI chaos) | **LIVE** | `/hello-world/` |
| R2 | Hardwiring Dignity: Defensive Leadership in the Age of AI | **LIVE** | `/drs-matrix` |

### Hello, World Toolkit

3-step toolkit: Start-Here > Safety-First Gate > SOP Playbook Builder

| File | Type | Status | Display Name |
|------|------|--------|--------------|
| `hello-world/index.html` | Toolkit landing / Start-Here step | **LIVE** | Hello, World |
| `hello-world/safety-first-gate/index.html` | Interactive checklist — 6 sequential gates | **LIVE** | Safety-First Gate |
| `hello-world/sop-playbook-builder/index.html` | SOP builder tool | **LIVE** | SOP Playbook Builder |
| `hello-world/sop-playbook-builder/assets/plain-language-guide.html` | Artifact page | **LIVE** | Plain Language Guide |
| `hello-world/sop-playbook-builder/assets/pro-guide.html` | Artifact page | **LIVE** | Pro Guide |
| `hello-world/sop-playbook-builder/assets/templates/capture-template-blank.html` | Blank template | **LIVE** | Capture Template |

### DRS Framework: The Weight of Wired Dignity

| File | Type | Status | Display Name |
|------|------|--------|--------------|
| `drs-matrix/index.html` | Framework page (light/ecru) | **LIVE** | "The 9:02 AM Meeting" (fable) + interactive DRS 2x2 matrix widget |

**Notes:**
- This is NOT a case study — it lives in the R&D section, not the client evidence grid
- Single self-contained HTML file with embedded CSS/JS, Google Fonts, and Plausible analytics
- URL: `angieqbailey.com/drs-matrix`
- Features: Mini-fable ("The 9:02 AM Meeting"), interactive 2x2 matrix with click-to-expand detail panels, click-outside-to-close, scroll-reveal animation, Print/Save as PDF with dedicated print stylesheet
- Series card in Warehouse shows "Chunk 1 of 5" — update as chunks ship

---

## L&D Section (Section 04)

| File | Type | Status | Display Name |
|------|------|--------|--------------|
| `ld/infrastructure-of-a-life.html` | L&D landing page | **LIVE** | Infrastructure of a Life |

**Collections:**
- "Dots, Good Pens & a Commonplace Book: A Supply Closet Romance" — 4 pieces (reworking)
- "Em-Dash Unpacking: Thief by Mass Visual Weaponization" — 4 pieces (coming)

Card in L&D section links to individual collection pages as they ship.

---

## Verdict Section (Section 05)

5 operating principles, each linked from index.html to a standalone essay page (~400 words each).

| File | Type | Status | Display Name |
|------|------|--------|--------------|
| `verdict/add-value-not-noise.html` | Essay page | **LIVE** | Principle 01: Add Value, Not Noise |
| `verdict/vocabulary-is-the-barrier.html` | Essay page | **LIVE** | Principle 02: Vocabulary Is the Barrier |
| `verdict/reality-before-theory.html` | Essay page | **LIVE** | Principle 03: Reality Before Theory |
| `verdict/structure-is-how-you-protect-people.html` | Essay page | **LIVE** | Principle 04: Structure Is How You Protect People |
| `verdict/the-implementation-failed-not-the-people.html` | Essay page | **LIVE** | Principle 05: The Implementation Failed, Not the People |

**Voice calibration:** No em-dashes, no arrogance, short.

---

## Start-Here Page

| File | Type | Status | Display Name |
|------|------|--------|--------------|
| `start-here/index.html` | Interactive AI context builder (lead gen) | **LIVE** | Start Here |

**Notes:**
- Single self-contained file (62 KB)
- Four-card questionnaire that generates a personal AI profile users can paste into any AI tool
- GA4 tag injected
- All dependencies CDN or inline
- Deployed 2026-04-27

---

## Resources Section

| File | Type | Status | Display Name |
|------|------|--------|--------------|
| `resources/index.html` | Resources landing page | **LIVE** | Resources |
| `resources/digital-gratuity.html` | Digital Gratuity page | **LIVE** | Digital Gratuity |

**Notes:**
- Resources is linked from the main nav as an external link (`/resources/`), not an anchor scroll
- Added as part of the 7-item nav update (May 2026)

---

## R&D Section Landing

| File | Type | Status | Display Name |
|------|------|--------|--------------|
| `rd/index.html` | R&D section landing page | **LIVE** | R&D |

---

## Case Study: Marketing Infrastructure MBR Debt Clearance

| File | Type | Status | Display Name |
|------|------|--------|--------------|
| `posts/marketing-infrastructure-mbr/marketing-infrastructure-mbr.html` | Case study page (dark) | **LIVE** | — |
| `posts/marketing-infrastructure-mbr/marketing-infrastructure-mbr-companion.docx` | Companion narrative doc | **LIVE** | — |
| `posts/marketing-infrastructure-mbr/assets/cross-functional-mbr-template.html` | Branded artifact page (dark) | **LIVE** | Cross-Functional MBR Template |
| `posts/marketing-infrastructure-mbr/assets/reporting-governance-cadence.html` | Branded artifact page (dark) | **LIVE** | Reporting Governance Cadence |
| `posts/marketing-infrastructure-mbr/assets/templates/cross-functional-mbr-template-blank.html` | Blank template (light/ecru) | **LIVE** | — |
| `posts/marketing-infrastructure-mbr/assets/templates/reporting-governance-cadence-blank.html` | Blank template (light/ecru) | **LIVE** | — |

**Date Added:** 2026-04-26 | **Warehouse Position:** 1

---

## Case Study: The GEO/AEO Transition

| File | Type | Status | Display Name |
|------|------|--------|--------------|
| `posts/geo-aeo-transition/geo-aeo-transition.html` | Case study page (dark) | **LIVE** | — |
| `posts/geo-aeo-transition/warehouse-card.html` | Warehouse card | **LIVE** | — |
| `posts/geo-aeo-transition/assets/ai-overview-monitoring-guide.html` | Branded artifact page (dark) | **LIVE** | AI Overview Monitoring Guide |
| `posts/geo-aeo-transition/assets/content-brief-template.html` | Branded artifact page (dark) | **LIVE** | Content Brief Template |
| `posts/geo-aeo-transition/assets/content-prioritization-framework.html` | Branded artifact page (dark) | **LIVE** | Content Prioritization Framework |
| `posts/geo-aeo-transition/assets/geo-best-practices-guide.html` | Branded artifact page (dark) | **LIVE** | GEO Best Practices Guide |
| `posts/geo-aeo-transition/assets/schema-markup-ai-content-guide.html` | Branded artifact page (dark) | **LIVE** | Schema Markup AI Content Guide |
| `posts/geo-aeo-transition/assets/seo-ai-search-playbook.html` | Branded artifact page (dark) | **LIVE** | SEO AI Search Playbook |
| `posts/geo-aeo-transition/assets/templates/ai-overview-monitoring-guide-blank.html` | Blank template (light/ecru) | **LIVE** | — |
| `posts/geo-aeo-transition/assets/templates/content-brief-template-blank.html` | Blank template (light/ecru) | **LIVE** | — |
| `posts/geo-aeo-transition/assets/templates/content-prioritization-framework-blank.html` | Blank template (light/ecru) | **LIVE** | — |
| `posts/geo-aeo-transition/assets/templates/geo-best-practices-guide-blank.html` | Blank template (light/ecru) | **LIVE** | — |
| `posts/geo-aeo-transition/assets/templates/schema-markup-ai-content-guide-blank.html` | Blank template (light/ecru) | **LIVE** | — |
| `posts/geo-aeo-transition/assets/templates/seo-ai-search-playbook-blank.html` | Blank template (light/ecru) | **LIVE** | — |

**Date Added:** 2026-04-24 | **Warehouse Position:** 2

---

## Case Study: Multi-Team Roadmap Summit

| File | Type | Status | Display Name |
|------|------|--------|--------------|
| `posts/e-commerce-summit/e-commerce-summit.html` | Case study page (dark) | **LIVE** | "E-Commerce Strategic Summit" (page h1) |
| `posts/e-commerce-summit/assets/dependency-friction-map.html` | Branded artifact page (dark) | **LIVE** | Dependency Friction Map |
| `posts/e-commerce-summit/assets/expectations-sla-stress-test.html` | Branded artifact page (dark) | **LIVE** | Expectations SLA Stress Test |
| `posts/e-commerce-summit/assets/expectations-stress-test-framework.html` | Branded artifact page (dark) | **LIVE** | Expectations Stress Test Framework |
| `posts/e-commerce-summit/assets/facilitation-mindsets-summary.html` | Branded artifact page (dark) | **LIVE** | Facilitation Mindsets Summary |
| `posts/e-commerce-summit/assets/pressure-points-register.html` | Branded artifact page (dark) | **LIVE** | Pressure Points Register |
| `posts/e-commerce-summit/assets/templates/dependency-friction-map-blank.html` | Blank template (light/ecru) | **LIVE** | — |
| `posts/e-commerce-summit/assets/templates/expectations-sla-stress-test-blank.html` | Blank template (light/ecru) | **LIVE** | — |
| `posts/e-commerce-summit/assets/templates/expectations-stress-test-blank.html` | Blank template (light/ecru) | **LIVE** | — |
| `posts/e-commerce-summit/assets/templates/facilitation-mindsets-blank.html` | Blank template (light/ecru) | **LIVE** | — |
| `posts/e-commerce-summit/assets/templates/pressure-points-register-blank.html` | Blank template (light/ecru) | **LIVE** | — |

**Warehouse Position:** 3

---

## Case Study: E-Commerce P&L Build

| File | Type | Status | Display Name |
|------|------|--------|--------------|
| `posts/ecommerce-pl/ecommerce-pl.html` | Case study page (dark) | **LIVE** | — |
| `posts/ecommerce-pl/assets/pl-project-dossier.html` | Branded artifact page (dark) | **LIVE** | "Project Brief" (not "Dossier" — file name uses dossier to preserve URL; all display text says Brief) |
| `posts/ecommerce-pl/assets/pl-cutoff-definition.html` | Branded artifact page (dark) | **LIVE** | Cutoff Definition |
| `posts/ecommerce-pl/assets/templates/pl-project-dossier-blank.html` | Blank template (light/ecru) | **LIVE** | "Project Brief" |
| `posts/ecommerce-pl/assets/templates/pl-cutoff-definition-blank.html` | Blank template (light/ecru) | **LIVE** | — |

**Warehouse Position:** 4

---

## Case Study: Web Experience Capacity Expansion

| File | Type | Status | Display Name |
|------|------|--------|--------------|
| `posts/web-experience-capacity-build/web-experience-capacity-build.html` | Case study page (dark) | **LIVE** | "Web Experience / Capacity / Build" |
| `posts/web-experience-capacity-build/assets/team-capacity-diagnostic.html` | Branded artifact page (dark) | **LIVE** | Team Capacity Diagnostic |
| `posts/web-experience-capacity-build/assets/templates/team-capacity-diagnostic-blank.html` | Blank template (light/ecru) | **LIVE** | — |

**Warehouse Position:** 5

---

## Case Study: Post-Acquisition Integration Launch

| File | Type | Status | Display Name |
|------|------|--------|--------------|
| `posts/post-acquisition-integration-launch/post-acquisition-integration-launch.html` | Case study page (dark) | **LIVE** | — |
| `posts/post-acquisition-integration-launch/warehouse-card.html` | Warehouse card | **LIVE** | — |
| `posts/post-acquisition-integration-launch/assets/vendor-governance-model.html` | Branded artifact page (dark) | **LIVE** | Vendor Governance Model |
| `posts/post-acquisition-integration-launch/assets/product-taxonomy-architecture.html` | Branded artifact page (dark) | **LIVE** | Product Taxonomy Architecture |
| `posts/post-acquisition-integration-launch/assets/cross-functional-workback.html` | Branded artifact page (dark) | **LIVE** | Cross-Functional Workback |
| `posts/post-acquisition-integration-launch/assets/system-integration-sequence.html` | Branded artifact page (dark) | **LIVE** | System Integration Sequence (interactive map) |
| `posts/post-acquisition-integration-launch/assets/templates/system-integration-sequence-blank.html` | Blank template (light/ecru) | **LIVE** | — |
| `posts/post-acquisition-integration-launch/assets/templates/vendor-governance-model-blank.html` | Blank template (light/ecru) | **LIVE** | — |
| `posts/post-acquisition-integration-launch/assets/templates/product-taxonomy-architecture-blank.html` | Blank template (light/ecru) | **LIVE** | — |

**Warehouse Position:** 6

---

## Case Study: Enterprise Newsletter Architecture

| File | Type | Status | Display Name |
|------|------|--------|--------------|
| `posts/enterprise-newsletter-architecture/enterprise-newsletter-architecture.html` | Case study page (dark) | **LIVE** | — |
| `posts/enterprise-newsletter-architecture/warehouse-card.html` | Warehouse card | **LIVE** | — |
| `posts/enterprise-newsletter-architecture/assets/interactive-channel-audit.html` | Branded artifact page (dark) | **LIVE** | Interactive Channel Audit |
| `posts/enterprise-newsletter-architecture/assets/in-house-style-guide.html` | Branded artifact page (dark) | **LIVE** | In-House Style Guide |
| `posts/enterprise-newsletter-architecture/assets/channel-mix-matrix.html` | Branded artifact page (dark) | **LIVE** | Channel Mix Matrix |
| `posts/enterprise-newsletter-architecture/assets/ic-strategic-value-architecture.html` | Branded artifact page (dark) | **LIVE** | IC Strategic Value Architecture |
| `posts/enterprise-newsletter-architecture/assets/internal-comms-channel-audit.html` | Branded artifact page (dark) | **LIVE** | Internal Comms Channel Audit |
| `posts/enterprise-newsletter-architecture/assets/templates/channel-mix-matrix-blank.html` | Blank template (light/ecru) | **LIVE** | — |
| `posts/enterprise-newsletter-architecture/assets/templates/ic-strategic-value-architecture-blank.html` | Blank template (light/ecru) | **LIVE** | — |
| `posts/enterprise-newsletter-architecture/assets/templates/internal-comms-channel-audit-blank.html` | Blank template (light/ecru) | **LIVE** | — |

**Warehouse Position:** 7

---

## Case Study: Crisis Communications Architecture

| File | Type | Status | Display Name |
|------|------|--------|--------------|
| `posts/crisis-communications-architecture/crisis-communications-architecture.html` | Case study page (dark) | **LIVE** | — |
| `posts/crisis-communications-architecture/warehouse-card.html` | Warehouse card | **LIVE** | — |
| `posts/crisis-communications-architecture/assets/crisis-holding-statements.html` | Branded artifact page (dark) | **LIVE** | Crisis Holding Statements |
| `posts/crisis-communications-architecture/assets/interactive-crisis-assessment.html` | Branded artifact page (dark) | **LIVE** | Interactive Crisis Assessment |
| `posts/crisis-communications-architecture/assets/crisis-response-team-architecture.html` | Branded artifact page (dark) | **LIVE** | Crisis Response Team Architecture |
| `posts/crisis-communications-architecture/assets/crisis-severity-framework.html` | Branded artifact page (dark) | **LIVE** | Crisis Severity Framework |
| `posts/crisis-communications-architecture/assets/disaster-response-decision-framework.html` | Branded artifact page (dark) | **LIVE** | Disaster Response Decision Framework |
| `posts/crisis-communications-architecture/assets/templates/crisis-holding-statements-blank.html` | Blank template (light/ecru) | **LIVE** | — |
| `posts/crisis-communications-architecture/assets/templates/crisis-response-team-architecture-blank.html` | Blank template (light/ecru) | **LIVE** | — |
| `posts/crisis-communications-architecture/assets/templates/crisis-severity-framework-blank.html` | Blank template (light/ecru) | **LIVE** | — |
| `posts/crisis-communications-architecture/assets/templates/disaster-response-decision-framework-blank.html` | Blank template (light/ecru) | **LIVE** | — |

**Warehouse Position:** 8

---

## 404 Page

| File | Type | Status |
|------|------|--------|
| `404.html` | Custom 404 error page | **LIVE** |

---

## Placeholder / Orphaned Files

| File | Notes |
|------|-------|
| `posts/my-first-post.md` | Orphan — not linked anywhere. Probably a GitHub default artifact. Do not delete without confirming with Angie. |

---

## URL Summary

| Category | Count |
|----------|-------|
| Root/nav pages | 5 (index, start-here, resources index, resources/digital-gratuity, 404) |
| R&D pages | 8 (rd landing, drs-matrix, hello-world x3, sop-playbook assets x2, template x1) |
| L&D pages | 1 |
| Verdict essays | 5 |
| Case study pages | 8 |
| Branded artifact pages | 33 |
| Blank templates | 30 |
| **Total live URLs** | **~90** |

---

## Adding a New Case Study — Checklist

When a new case study is ready to deploy:

1. Create folder: `posts/{slug}/`
2. Add case study page: `posts/{slug}/{slug}.html`
3. Add artifact pages (if applicable): `posts/{slug}/assets/{artifact-name}.html`
4. Add blank templates (if applicable): `posts/{slug}/assets/templates/{artifact-name}-blank.html`
5. Update `index.html` — convert the placeholder `<div>` Warehouse card to a clickable `<a>` tag
6. Update this registry — add new rows to the appropriate case study table, update Warehouse card status
7. Update `_changelog.md` with what changed and why
