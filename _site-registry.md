# AQB Site Registry
**Last updated:** March 2026
**Repo:** `AngieQBailey/angieqbailey` | **Branch:** `main` | **Host:** GitHub Pages → `angieqbailey.com`

This is the authoritative file inventory. Update this document any time a file is added, removed, renamed or promoted from placeholder to live. Do not let it drift.

---

## Root Files

| File | Purpose | Notes |
|------|---------|-------|
| `index.html` | Main site — single file, all CSS/JS embedded | Contains Warehouse card grid, nav, hero, Debrief section, footer |
| `CNAME` | GitHub Pages custom domain config | Contains: `angieqbailey.com` |
| `README.md` | Minimal deployment notes | Not public-facing |
| `favicon.png` | AB monogram favicon, 192×192 | Parisian Night bg, ecru text, quetzal-bright accent bar |
| `favicon-32.png` | 32px favicon variant | Same design |
| `favicon.ico` | Multi-size .ico (16, 32, 48) | Linked via `<link rel="icon">` and `<link rel="apple-touch-icon">` |
| `headshot.png` | Angie's portrait, 128×128 | Footer easter egg — opacity:0 default, reveals on footer hover |
| `og-image.png` | Social sharing preview, 1200×630 | Blueprint-grid aesthetic, IBM Plex Mono, Parisian Night + quetzal grid + rosso accent |

---

## Warehouse Cards (index.html)

Current order and status. Live cards are `<a>` elements. Placeholders are `<div>` elements.

| # | Card Title | Category | Status | Link Target |
|---|------------|----------|--------|-------------|
| 1 | Multi-Team Roadmap Summit | Strategic Operations | **LIVE** | `posts/e-commerce-summit/e-commerce-summit.html` |
| 2 | E-Commerce P&L Build | Decision Infrastructure | **LIVE** | `posts/ecommerce-pl/ecommerce-pl.html` |
| 3 | Web Experience Capacity Build | Delivery Governance | **LIVE** | `posts/web-experience-capacity-build/web-experience-capacity-build.html` |
| 4 | Post-Acquisition Integration | Ops Management | **PLACEHOLDER** | No case study page yet |
| 5 | Workforce AI Adoption | AI Implementation | **PLACEHOLDER** | No case study page yet |

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
| `posts/e-commerce-summit/assets/templates/dependency-friction-map-blank.html` | Blank template (light/ecru) | **LIVE** | — |
| `posts/e-commerce-summit/assets/templates/expectations-sla-stress-test-blank.html` | Blank template (light/ecru) | **LIVE** | — |
| `posts/e-commerce-summit/assets/templates/expectations-stress-test-blank.html` | Blank template (light/ecru) | **LIVE** | — |
| `posts/e-commerce-summit/assets/templates/facilitation-mindsets-blank.html` | Blank template (light/ecru) | **LIVE** | — |
| `posts/e-commerce-summit/assets/templates/pressure-points-register-blank.html` | Blank template (light/ecru) | **LIVE** | — |

---

## Case Study: E-Commerce P&L Build

| File | Type | Status | Display Name |
|------|------|--------|--------------|
| `posts/ecommerce-pl/ecommerce-pl.html` | Case study page (dark) | **LIVE** | — |
| `posts/ecommerce-pl/assets/pl-project-dossier.html` | Branded artifact page (dark) | **LIVE** | "Project Brief" (not "Dossier" — file name uses dossier to preserve URL; all display text says Brief) |
| `posts/ecommerce-pl/assets/pl-cutoff-definition.html` | Branded artifact page (dark) | **LIVE** | Cutoff Definition |
| `posts/ecommerce-pl/assets/templates/pl-project-dossier-blank.html` | Blank template (light/ecru) | **LIVE** | "Project Brief" |
| `posts/ecommerce-pl/assets/templates/pl-cutoff-definition-blank.html` | Blank template (light/ecru) | **LIVE** | — |

---

## Case Study: Web Experience Capacity Build

| File | Type | Status | Display Name |
|------|------|--------|--------------|
| `posts/web-experience-capacity-build/web-experience-capacity-build.html` | Case study page (dark) | **LIVE** | "Web Experience / Capacity / Build" |
| `posts/web-experience-capacity-build/assets/team-capacity-diagnostic.html` | Branded artifact page (dark) | **LIVE** | Team Capacity Diagnostic |
| `posts/web-experience-capacity-build/assets/templates/team-capacity-diagnostic-blank.html` | Blank template (light/ecru) | **LIVE** | — |

---

## Placeholder / Orphaned Files

| File | Notes |
|------|-------|
| `posts/my-first-post.md` | Orphan — not linked anywhere. Probably a GitHub default artifact. Do not delete without confirming with Angie. |

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
