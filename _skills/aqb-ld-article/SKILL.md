---
name: aqb-ld-article
description: "Build L&D leaf articles (Infrastructure of A Life essays) for angieqbailey.com. Use whenever Angie wants to create or edit a personal essay-style L&D article in a collection like Em-Dash Unpacking or A Supply Closet Romance, turn a researched long-form draft into a deployed dark-variant page, wire an article into the L&D hub, or cross-link a collection. Trigger on 'L&D article,' 'Infrastructure of a Life,' 'em-dash unpacking,' 'supply closet romance,' 'love letter piece,' 'leaf article,' 'essay page,' or any request to turn an L&D markdown draft into a web-ready page. This is the personal-essay shell, distinct from aqb-case-study (forensic case studies). Depends on angie-bailey-brand (voice, palette, banned words) and aqb-case-study (deploy mechanics, changelog, GitHub upload). Read those first if unfamiliar."
metadata:
  version: "1.2"
  last_updated: "2026-06-25"
---

# AQB L&D Article Builder

Builds the personal-essay leaf pages that live under `ld/<collection>/` on angieqbailey.com (the Infrastructure of A Life collections). These are not case studies. They are first-person essays, love letters to objects and ideas, forensic threads pulled until they connect to three other things. The shell, voice, and structure were proven across the four Em-Dash Unpacking articles and are captured here so the next collection is assembly, not reinvention.

This skill owns the HOW of an L&D article: the shell, the emphasis system, the cross-link rules, the landing-card states. It leans on `angie-bailey-brand` for voice and visual identity, and on `aqb-case-study` for the deploy mechanics (pull-before-deploy, the Node GitHub upload pattern, the changelog format). Read those if you don't know them.

## When to use

- Angie hands you a build-ready L&D markdown draft (a collection piece) and wants it on the site.
- She wants to edit, re-pull, or re-deploy an existing L&D article.
- She wants to wire a new article's card live on the L&D hub, or cross-link a collection.
- Any task naming an L&D collection: "Em-Dash Unpacking," "A Supply Closet Romance," "Infrastructure of a Life."

If the work is a forensic case study, an artifact page, a Warehouse card, or a downloadable template, use `aqb-case-study` instead.

## Files in this skill

- `assets/ld-article-template.html` — the proven shell with `[[PLACEHOLDERS]]` and the hard rules as inline comments. Copy it to start a new article.
- `references/conventions.md` — the full doctrine (build shell, voice, emphasis pulls, cross-links, landing cards, deploy ritual) plus a paste-ready block for the project instructions.

The canonical source lives in the repo at `_templates/ld-article-template.html` and `_templates/LD-ARTICLE-CONVENTIONS.md`. The copies this skill bundles are derived from those files: the repo is upstream, the skill is downstream. If they ever diverge, the repo wins and the skill copies are re-synced from it. A drift check (`scripts/check_skill_drift.py`, run in CI) fails the build if a bundled copy stops matching its repo source, so this can't drift silently.

## Build workflow

1. **Read first.** `site-map.md` (what exists, which cards are live), `angie-bailey-brand` SKILL.md, and the `feedback_skill_overrides.md` memory. State the change tier (a new article page is Tier 3; copy edits are Tier 2) and affected section at the top of the response.

2. **Content before code.** For Tier 2/3, the draft is usually Angie's own build-ready markdown. Scan it for banned words and brand-rule violations (no em-dash characters, no Oxford commas, no hedging) and fix or flag before building. Do not silently rewrite voice.

3. **Build from the template.** Copy `assets/ld-article-template.html` to `ld/<collection-slug>/<article-slug>.html`. Fill the placeholders. Match the slug to the cross-reference URLs the other articles already use.

4. **Apply the emphasis system.** One `.hook-line` pull per section, including the dek. Pick the single best beat, not the longest sentence; chop a long line so the pull is short and the rest drops to body weight. Ecru by default. Rosso (`.is-rosso`) only for a single collection signature, never on a heavy-subject article. The selector must be `.essay-body p.hook-line` so it beats the global `.essay-body p` rule.

5. **Handle cross-links.** Inline source links go live, same-tab, no `target="_blank"`. Sibling article references render as PLAIN TEXT until that sibling page exists. When a sibling ships, wire it in both directions in one pass. The cross-case synthesis lands once, in the collection capstone, not in every piece. Add a `.scale-note` (rosso left border) only for heavy subjects.

6. **QA (grep the file).** Zero em-dash characters. GA4 tag `G-S0MXDDKP4E` present. No `target=_blank`. One pull per section. Demonstrative ellipses as `&hellip;`. Glossary uses the "If a Term Snags You" + "Glossary" label + `details.glossary-card` pattern. Live links resolve; sibling links inert until shipped.

7. **Wire the hub + docs.** Flip the article's landing card from a `placeholder` div to a live `<a class="piece-card">` with NO status label ("Coming" stays only on unbuilt cards). Add the page to `sitemap.xml`. Update `site-map.md`. Add a `_changelog.md` entry.

8. **Deploy.** Pull every touched file from GitHub first (edit-side freshness), then push via `deploy.js`. Verify the live URL returns 200 (new paths lag 30-60s on GitHub Pages).

## Non-negotiables (full list in references/conventions.md)

- Dark-variant shell: `html` + `body` + `theme-color` all `#121A28`; `color-scheme: dark`.
- 7-item nav; single `Back to L&D` at the bottom (drop the collection back-link).
- No em-dash characters, no Oxford commas, curly quotes via entities, ellipses as `&hellip;`.
- One ecru emphasis pull per section; rosso reserved for one collection signature; never rosso on heavy subjects.
- Sibling cross-links plain text until shipped, then wired both directions.
- Live landing cards are anchor-wrapped with no status label.
- `.scale-note` caveat for heavy subjects; synthesis lands once in the capstone.
- Do not "improve" the brutalist design. Targeted edits only.

## Dependencies

- `angie-bailey-brand` — voice, banned words, palette, typography (upstream, read first).
- `aqb-case-study` — deploy mechanics, GitHub upload pattern, changelog process (shared infrastructure).
