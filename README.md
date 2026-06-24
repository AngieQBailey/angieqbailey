# angieqbailey.com

Personal site for Angie Bailey — The Warehouse. Pure HTML/CSS/JS, no framework, hosted on GitHub Pages (serves from the repo root on `main`).

**Design System: The Warehouse.** Palette: Nuit de Chine, Bitter Cacao, Quetzal Green, Ecru Wool, Valentino Rosso. Type: Imbue (headlines) + IBM Plex Sans/Mono (body/code). Constraint: no italics, no border-radius, certainty over suggestion.

## How the documentation is organized

The git repo is the durable backbone. Everything foundational has its record here, in plain text, so the site is rebuildable even if the tooling changes. The Claude skills are a derived convenience layer for generating on-brand content; they mirror the repo and are re-synced from it. The repo is always upstream.

### Where each thing lives (the durable repo layer)

| Concern | Canonical home |
|---|---|
| What pages and files exist | `site-map.md` |
| Design system spec (colors, type, spacing, components) | `_design-system.md` (values render from `styles.css` `:root {}`) |
| Build, link and deploy conventions; troubleshooting | `_build-notes.md` |
| L&D article shell + doctrine | `_templates/ld-article-template.html`, `_templates/LD-ARTICLE-CONVENTIONS.md` |
| Analytics & SEO infrastructure (GA4, Search Console, Bing, /go/) | `docs/analytics-runbook.md` |
| Project operating instructions | `docs/PROJECT-INSTRUCTIONS.md` (mirrors the live project settings) |
| Change history | `_changelog.md` |
| Short-link source + generator | `_links.json`, `scripts/build_links.py` |
| Deploy tool | `deploy.js` |
| Skill sources + no-drift check | `_skills/` (version-controlled copies + `skill-pairs.json`), `scripts/check_skill_drift.py`, `.github/workflows/skill-drift.yml` |

### Derived layer (Claude skills, re-synced from the repo)

- `angie-bailey-brand` — voice, banned words, visual identity, numeric-language rule.
- `aqb-case-study` — case-study pages, artifacts, templates, deploy mechanics.
- `aqb-ld-article` — L&D leaf articles (bundles the template + conventions above).

If a skill ever disagrees with the repo, the repo wins and the skill gets re-synced. Skill packages are versioned in `Updated Skills (Versioned)/` and tracked by the `skill-version-manifest`.

This relationship is enforced, not trusted. Skills that bundle repo files keep version-controlled copies under `_skills/`, declared in `_skills/skill-pairs.json`. `scripts/check_skill_drift.py` byte-compares each exact copy against its repo source and flags conceptual sources that have changed; a standalone GitHub Action (`.github/workflows/skill-drift.yml`) runs it on every push and fails when a copy has drifted. That check is report-only and independent of the Pages deploy, so a drift failure never blocks the site. See `_skills/README.md` for the sync workflow and its limits.

## Deployment

Pull the latest of any file before editing it, then `node deploy.js <local-file> <repo-path> "<message>"`. Every deploy gets a `_changelog.md` entry. New paths can lag 30–60s on GitHub Pages.
