# AQB Site Registry
**Last updated:** March 2026
**Repo:** `AngieQBailey/angieqbailey` | **Branch:** `main` | **Host:** GitHub Pages Ã¢ÂÂ `angieqbailey.com`

This is the authoritative file inventory. Update this document any time a file is added, removed, renamed or promoted from placeholder to live. Do not let it drift.

---

## Root Files

| File | Purpose | Notes |
|------|---------|-------|
| `index.html` | Main site Ã¢ÂÂ single file, all CSS/JS embedded | Contains Warehouse card grid, nav, hero, Debrief section, footer |
| `CNAME` | GitHub Pages custom domain config | Contains: `angieqbailey.com` |
| `README.md` | Minimal deployment notes | Not public-facing |
| `favicon.png` | AB monogram favicon, 192ÃÂ192 | Parisian Night bg, ecru text, quetzal-bright accent bar |
| `favicon-32.png` | 32px favicon variant | Same design |
| `favicon.ico` | Multi-size .ico (16, 32, 48) | Linked via `<link rel="icon">` and `<link rel="apple-touch-icon">` |
| `headshot.png` | Angie's portrait, 128ÃÂ128 | Footer easter egg Ã¢ÂÂ opacity:0 default, reveals on footer hover |
| `og-image.png` | Social sharing preview, 1200ÃÂ630 | Blueprint-grid aesthetic, IBM Plex Mono, Parisian Night + quetzal grid + rosso accent |

---

## Warehouse Cards (index.html)

Current order and status. Live cards are `<a>` elements. Placeholders are `<div>` elements.

| # | Card Title | Category | Status | Link Target |
|---|------------|----------|--------|-------------|
| 1 | Multi-Team Roadmap Summit | Strategic Operations | **LIVE** | `posts/e-commerce-summit/e-commerce-summit.html` |
| 2 | E-Commerce P&L Build | Decision Infrastructure | **LIVE** | `posts/ecommerce-pl/ecommerce-pl.html` |
| 3 | Web Experience Capacity Expansion | Delivery Governance | **LIVE** | `posts/web-experience-capacity-build/web-experience-capacity-build.html` |
| 4 | Post-Acquisition Integration | Ops Management | **PLACEHOLDER** | No case study page yet |
| 5 | Enterprise Newsletter Launch | Channel Strategy | **LIVE** | `posts/enterprise-newsletter-architecture/enterprise-newsletter-architecture.html` |
| 6 | Crisis Communications Architecture | Strategic Communications | **LIVE** | `posts/crisis-communications-architecture/crisis-communications-architecture.html` |
| 7 | Workforce AI Adoption | AI Implementation | **PLACEHOLDER** | No case study page yet |

### R&D Section (Frameworks Under Construction)

Below the client case study grid, a separate subsection with Quetzal-tinted cards and its own visual treatment. Cards open in new tabs.

| # | Card Title | Category | Status | Link Target |
|---|------------|----------|--------|-------------|
| R1 | The Weight of Wired Dignity | Workforce Psychographics | **LIVE** | `/drs-matrix` (new tab) |

**Rule:** Card titles and case study page h1s do not need to match. The card is the fast read. The page h1 is the forensic record. Do not "fix" discrepancies.

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
| `posts/e-commerce-summit/assets/templates/dependency-friction-map-blank.html` | Blank template (light/ecru) | **LIVE** | Ã¢ÂÂ |
| `posts/e-commerce-summit/assets/templates/expectations-sla-stress-test-blank.html` | Blank template (light/ecru) | **LIVE** | Ã¢ÂÂ |
| `posts/e-commerce-summit/assets/templates/expectations-stress-test-blank.html` | Blank template (light/ecru) | **LIVE** | Ã¢ÂÂ |
| `posts/e-commerce-summit/assets/templates/facilitation-mindsets-blank.html` | Blank template (light/ecru) | **LIVE** | Ã¢ÂÂ |
| `posts/e-commerce-summit/assets/templates/pressure-points-register-blank.html` | Blank template (light/ecru) | **LIVE** | Ã¢ÂÂ |

---

## Case Study: E-Commerce P&L Build

| File | Type | Status | Display Name |
|------|------|--------|--------------|
| `posts/ecommerce-pl/ecommerce-pl.html` | Case study page (dark) | **LIVE** | Ã¢ÂÂ |
| `posts/ecommerce-pl/assets/pl-project-dossier.html` | Branded artifact page (dark) | **LIVE** | "Project Brief" (not "Dossier" Ã¢ÂÂ file name uses dossier to preserve URL; all display text says Brief) |
| `posts/ecommerce-pl/assets/pl-cutoff-definition.html` | Branded artifact page (dark) | **LIVE** | Cutoff Definition |
| `posts/ecommerce-pl/assets/templates/pl-project-dossier-blank.html` | Blank template (light/ecru) | **LIVE** | "Project Brief" |
| `posts/ecommerce-pl/assets/templates/pl-cutoff-definition-blank.html` | Blank template (light/ecru) | **LIVE** | Ã¢ÂÂ |

---

## Case Study: Web Experience Capacity Expansion

| File | Type | Status | Display Name |
|------|------|--------|--------------|
| `posts/web-experience-capacity-build/web-experience-capacity-build.html` | Case study page (dark) | **LIVE** | "Web Experience / Capacity / Build" |
| `posts/web-experience-capacity-build/assets/team-capacity-diagnostic.html` | Branded artifact page (dark) | **LIVE** | Team Capacity Diagnostic |
| `posts/web-experience-capacity-build/assets/templates/team-capacity-diagnostic-blank.html` | Blank template (light/ecru) | **LIVE** | Ã¢ÂÂ |

---

## DRS Framework: The Weight of Wired Dignity

| File | Type | Status | Display Name |
|------|------|--------|--------------|
| `drs-matrix/index.html` | Framework page (light/ecru) | **LIVE** | "The 9:02 AM Meeting" (fable) + interactive DRS 2ÃÂ2 matrix widget |

**Notes:**
- This is NOT a case study Ã¢ÂÂ it lives in the R&D section, not the client evidence grid
- Single self-contained HTML file with embedded CSS/JS, Google Fonts, and Plausible analytics
- URL: `angieqbailey.com/drs-matrix`
- Features: Mini-fable ("The 9:02 AM Meeting"), interactive 2ÃÂ2 matrix with click-to-expand detail panels, click-outside-to-close, scroll-reveal animation, Print/Save as PDF with dedicated print stylesheet
- Series card in Warehouse shows "Chunk 1 of 5" Ã¢ÂÂ update as chunks ship
- Plausible analytics embedded but requires paid account setup at plausible.io to activate tracking

---

## Case Study: Enterprise Newsletter Launch

| File | Type | Status | Display Name |
|------|------|--------|--------------|
| `posts/enterprise-newsletter-architecture/enterprise-newsletter-architecture.html` | Case study page (dark) | **LIVE** | â |
| `posts/enterprise-newsletter-architecture/assets/interactive-channel-audit.html` | Branded artifact page (dark) | **LIVE** | Interactive Channel Audit |
| `posts/enterprise-newsletter-architecture/assets/in-house-style-guide.html` | Branded artifact page (dark) | **LIVE** | In-House Style Guide |
| `posts/enterprise-newsletter-architecture/assets/channel-mix-matrix.html` | Branded artifact page (dark) | **LIVE** | Channel Mix Matrix |
| `posts/enterprise-newsletter-architecture/assets/ic-strategic-value-architecture.html` | Branded artifact page (dark) | **LIVE** | IC Strategic Value Architecture |
| `posts/enterprise-newsletter-architecture/assets/internal-comms-channel-audit.html` | Branded artifact page (dark) | **LIVE** | Internal Comms Channel Audit |
| `posts/enterprise-newsletter-architecture/assets/templates/*.html` | Blank templates (light/ecru) | **LIVE** | 3 blank templates |

---

## Case Study: Crisis Communications Architecture

| File | Type | Status | Display Name |
|------|------|--------|--------------|
| `posts/crisis-communications-architecture/crisis-communications-architecture.html` | Case study page (dark) | **LIVE** | — |
| `posts/crisis-communications-architecture/assets/crisis-holding-statements.html` | Branded artifact page (dark) | **LIVE** | Crisis Holding Statements |
| `posts/crisis-communications-architecture/assets/interactive-crisis-assessment.html` | Branded artifact page (dark) | **LIVE** | Interactive Crisis Assessment |
| `posts/crisis-communications-architecture/assets/crisis-response-team-architecture.html` | Branded artifact page (dark) | **LIVE** | Crisis Response Team Architecture |
| `posts/crisis-communications-architecture/assets/crisis-severity-framework.html` | Branded artifact page (dark) | **LIVE** | Crisis Severity Framework |
| `posts/crisis-communications-architecture/assets/disaster-response-decision-framework.html` | Branded artifact page (dark) | **LIVE** | Disaster Response Decision Framework |
| `posts/crisis-communications-architecture/assets/templates/crisis-holding-statements-blank.html` | Blank template (light/ecru) | **LIVE** | Crisis Holding Statements |
| `posts/crisis-communications-architecture/assets/templates/crisis-response-team-architecture-blank.html` | Blank template (light/ecru) | **LIVE** | Crisis Response Team Architecture |
| `posts/crisis-communications-architecture/assets/templates/crisis-severity-framework-blank.html` | Blank template (light/ecru) | **LIVE** | Crisis Severity Framework |
| `posts/crisis-communications-architecture/assets/templates/disaster-response-decision-framework-blank.html` | Blank template (light/ecru) | **LIVE** | Disaster Response Decision Framework |
---

## Placeholder / Orphaned Files

| File | Notes |
|------|-------|
| `posts/my-first-post.md` | Orphan Ã¢ÂÂ not linked anywhere. Probably a GitHub default artifact. Do not delete without confirming with Angie. |

---

## Adding a New Case Study Ã¢ÂÂ Checklist

When a new case study is ready to deploy:

1. Create folder: `posts/{slug}/`
2. Add case study page: `posts/{slug}/{slug}.html`
3. Add artifact pages (if applicable): `posts/{slug}/assets/{artifact-name}.html`
4. Add blank templates (if applicable): `posts/{slug}/assets/templates/{artifact-name}-blank.html`
5. Update `index.html` Ã¢ÂÂ convert the placeholder `<div>` Warehouse card to a clickable `<a>` tag
6. Update this registry Ã¢ÂÂ add new rows to the appropriate case study table, update Warehouse card status
7. Update `_changelog.md` with what changed and why
