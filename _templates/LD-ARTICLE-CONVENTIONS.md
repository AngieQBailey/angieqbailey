# L&D Article Conventions

Doctrine for Infrastructure of A Life leaf articles (`ld/<collection>/<slug>.html`).
Converged across the four Em-Dash Unpacking articles, 2026-06-24. Start from
`_templates/ld-article-template.html`.

## Build shell

- Dark-variant: `html`, `body`, and `theme-color` all `#121A28`; `color-scheme: dark`.
- GA4 tag `G-S0MXDDKP4E` on every page. Never remove or duplicate.
- 7-item nav: Investigation, Warehouse, R&D, L&D, Verdict, Resources, Debrief.
- Page-scoped `<style>` block carries `.essay-body p.hook-line`, the inline-link
  color, and `.scale-note`. The hook-line selector must be `.essay-body p.hook-line`
  (specificity 0,2,1) so it beats the global `.essay-body p` rule. Plain `.hook-line`
  silently loses and renders small and dim. (Planned: move this block into global
  `styles.css` and delete it from each page.)

## Voice and typography

- No em-dash characters in body. Exception: verbatim quoted source titles only.
- No Oxford commas. Use `that` for restrictive, `which` for non-restrictive.
- `more than` / `fewer than` / `less than` for quantities, never `under`/`over`.
- Curly punctuation via entities: `&rsquo;`, `&ldquo;`, `&rdquo;`.
- Demonstrative ellipses as `&hellip;` (the glyph), not three spaced periods.
- Plain language over academic phrasing. Define obscure terms in the glossary.

## Emphasis pulls (`.hook-line`)

- One pull per section, including the dek. Not zero, not three.
- Pick the single best beat in the section, not the longest sentence. Chop a long
  line so the pull is short and the remainder drops to body weight beneath it.
- Ecru by default. Reserve rosso (`.is-rosso`) for at most ONE signature line in the
  whole collection, and never on a heavy-subject article (the red reads as
  sensationalizing on grave material).
- Size is `clamp(1.5rem, 3vw, 1.9rem)` with `text-wrap: balance` to kill orphans.

## Cross-links

- Inline source links: live, same-tab, NO `target="_blank"` (white-flash on dark).
- Sibling article references: render as PLAIN TEXT until that sibling page ships.
  When a sibling ships, wire it in both directions in the same pass (grep the
  collection for the new article's plain-text name and link every hit; link the new
  article's references back to the existing pages).
- The cross-case synthesis lands ONCE, in the collection's capstone (last article),
  not restated in every piece.

## Page furniture

- Bottom nav is a single `Back to L&D`. Drop the `Back to <Collection>` link.
- Keep the inline "one of N pieces" collection link only inside a `.scale-note`.
- `.scale-note` (rosso left border) for heavy-subject articles only: name the stakes
  gap plainly up front.
- Glossary: `<h2>If a Term<br>Snags You</h2>`, then a `Glossary` section-label below
  the heading, then the `details.glossary-card` grid. No redundant intro sentence.

## Landing cards (`ld/infrastructure-of-a-life.html`)

- A live card is `<a class="piece-card">` wrapping name + desc, with NO status label.
- A not-yet-built card is `<div class="piece-card placeholder">` with
  `<div class="piece-status">Coming &rarr;</div>`.
- Card descriptions already live on the landing page; reuse them, don't rewrite.

## Deploy ritual (per article)

1. Pull every file you will touch from GitHub first (edit-side freshness).
2. Build/edit. QA grep: 0 em-dashes, GA4 present, no `target=_blank`, sibling links
   correct, one pull per section.
3. Wire the landing card live and wire sibling cross-links both directions.
4. Add the page to `sitemap.xml`; update `site-map.md`.
5. Add a `_changelog.md` entry (date, tier, section, change, rationale, operator).
6. Deploy via `deploy.js`; verify the live URL returns 200 (new paths lag ~30-60s).

---

## PASTE INTO PROJECT INSTRUCTIONS

> ### L&D Articles (Infrastructure of A Life leaf pages)
> Build all L&D articles from `_templates/ld-article-template.html` and follow
> `_templates/LD-ARTICLE-CONVENTIONS.md`. Non-negotiables: dark-variant shell + GA4
> tag + 7-item nav; no em-dash characters, no Oxford commas, ellipses as `&hellip;`;
> one `.hook-line` emphasis pull per section (selector `.essay-body p.hook-line`),
> ecru by default with rosso reserved for a single collection signature and never on
> heavy-subject articles; sibling cross-links render as plain text until the sibling
> ships, then wired both directions; single `Back to L&D` at the bottom; live landing
> cards are anchor-wrapped with no status label, "Coming" only on placeholders; add a
> `.scale-note` caveat for heavy subjects; the cross-case synthesis lands once in the
> collection capstone, not per article.
