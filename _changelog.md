## [2026-06-24] — TIER 1 — L&D (Em-Dash Unpacking, Article 01 line-wrap fix)
**Change:** Added text-wrap: balance to the .essay-body p.hook-line rule so the four emphasis lines stop orphaning a single word on the last line. Root cause was width-only wrapping against the 640px max-width with no break control, which dropped lone words like "infrastructure." onto their own line. Balance evens the line lengths and, for the origin line, lands the break at the sentence boundary ("It wasn't elegant. It wasn't literary." / "It was infrastructure.").
**Rationale:** Per Angie's note on odd wrapping. Balance is the responsive fix (no hard-coded breaks to maintain across viewports). For any line that needs a guaranteed break point regardless of screen width, a manual br is the deterministic option, same as the h1/h2 headings already use.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-24] — TIER 1 — L&D (Em-Dash Unpacking, Article 01 emphasis-line system)
**Change:** Unified all four section pull lines under one .hook-line treatment and dialed the size back from clamp(1.9rem, 5vw, 3rem) to clamp(1.5rem, 3vw, 1.9rem) with line-height 1.2. Converted the two remaining .verdict-line pulls (origin "It was infrastructure," adoption "Then GPT-4 showed up") to .hook-line so all four match in size and weight. Rosso stays on the opening line only ("That's not overuse. That's a hit job."); the other three are ecru.
**Rationale:** Per Angie. The 3rem hook read as way too big. The section-ending lines deserved more weight than the 1.35rem .verdict-line gave them, so they all share one moderate size now. Rosso is reserved for the single signature line so the red stays a punctuation mark, not the page's baseline.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-24] — TIER 1 — L&D (Em-Dash Unpacking, Article 01 hook fix)
**Change:** Fixed the .hook-line size that never took. The page-scoped .hook-line rule (specificity 0,1,0) was being overridden by styles.css .essay-body p (0,1,1), so both hook lines kept rendering at 1.05rem dim. Re-scoped the rule to .essay-body p.hook-line so it wins. Added an .is-rosso modifier and applied it to the opening line "That's not overuse. That's a hit job." so it renders in rosso. The closing bookend "Five hundred years of utility..." now renders at full size in ecru.
**Rationale:** Per Angie. The earlier enlarge attempts had no visible effect because of the specificity collision. Rosso on the short opening line gives it the headline's accent punch. Left the long closing line in ecru on purpose: at full size a paragraph-length line in solid rosso reads as a wall of red. Offered to recolor it if Angie wants the bookends to match.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-24] — TIER 2 — L&D (Em-Dash Unpacking, Article 01 copy + emphasis)
**Change:** Three edits to ld/em-dash-unpacking/assassination-of-the-em-dash.html. Promoted the closing verdict line "Five hundred years of utility. Assassinated by..." to .hook-line so it matches the opening hook in size and weight (two oversized beats now bookend the piece). Cut the redundant glossary intro sentence "You don't need this to read the piece. It's here if a term snags you." and moved the "Glossary" label below the "If a Term Snags You" heading so the section opens on the line, not the label. Deleted "I'm not psychic." from the Verdict section; the surrounding fragments carry the beat without it.
**Rationale:** Per Angie. The bookend emphasis gives the close the same landing as the open. The glossary heading already said "if a term snags you," so the sentence was a stutter. "I'm not psychic" was a throwaway that softened the line around it.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-24] — TIER 1 — L&D (Em-Dash Unpacking, Article 01 polish)
**Change:** Two cosmetic tweaks to ld/em-dash-unpacking/assassination-of-the-em-dash.html via a page-scoped style block. Promoted the hook line "That's not overuse. That's a hit job." from .verdict-line (1.35rem) to a new .hook-line at clamp(1.9rem, 5vw, 3rem) so the signature line reads as the dek. Gave inline body and glossary links an on-brand color (quetzal-bright #00A896 with a 1px underline, hover to ecru) to replace the default browser purple.
**Rationale:** The hit-job line is the strongest beat in the piece and was sized like an ordinary pull quote. The purple links clashed with the dark Brutalist palette. Scoped to this page rather than global styles.css, since a site-wide inline-link rule would also restyle every DRS and Verdict page in the same push and deserves its own decision.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-24] — TIER 3 — L&D (Em-Dash Unpacking, Article 01)
**Change:** Built and deployed the first Em-Dash Unpacking article, ld/em-dash-unpacking/assassination-of-the-em-dash.html (The Assassination of the Em-Dash), on the dark-variant doc/essay shell: 7-item nav, GA4 tag, five doc-sections with section-label + h2 + essay-body, verdict-line pull quotes, a four-term collapsible glossary and same-tab source links (no target=_blank). Wired its card on ld/infrastructure-of-a-life.html from a Coming placeholder div to a live anchor (.piece-card with .piece-status.live, "Read" arrow). Cards 2 through 4 stay Coming. Added the page to sitemap.xml and updated the Em-Dash Unpacking row in site-map.md.
**Rationale:** Article 1 of 4 is fact-checked and build-ready, so it ships solo while the other three finish their voice pass. The three in-body sibling cross-links (swastika, Confederate flag, Article 2) render as plain text, not hrefs, until those pages exist, which avoids live 404s. Pulled all four touched files live from GitHub before editing to protect yesterday's two-column restructure.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-24] — TIER 1 — R&D / DRS (Tactical Dignity)
**Change:** Reworded the Findings paragraph opener from "It doesn't look like resistance." to "What follows doesn't look like resistance." after the duplicate verdict-line was cut.
**Rationale:** With the verdict-line removed, the bare "It" sat right after a sentence whose "it" meant the tool, creating a dangling antecedent. "What follows" anchors to the heading.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-24] — TIER 2 — R&D / DRS (Tactical Dignity)
**Change:** Removed the duplicate verdict-line "The senior contributor stops contributing." from the Findings section of tactical-dignity.html. The H2 heading already states the same words one paragraph above, so the line read as a stutter rather than a callback.
**Rationale:** Heading and verdict-line were verbatim twins separated by a single setup paragraph. Kept the heading, cut the echo.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-24] — TIER 1 — SEO infra (short links)
**Change:** Minted evergreen root vanity `/last-50-feet` (→ /rd/dignity/last-50-feet.html, no campaign UTM) via the `path` override in _links.json + build_links.py. noindex stub, excluded from sitemap. Updated docs/analytics-runbook.md (live-slug snapshot, now two evergreen vanities) and site-map.md.
**Rationale:** A clean reusable pointer to the Last 50 Feet essay, since /go/drs-rock now sends Find the Rocks post traffic to the Rock Audit landing. Evergreen so essay traffic is not charged to a post campaign.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-23] — TIER 1 — R&D / DRS (Rock Audit body type)
**Change:** Aligned rock-audit.html body prose to the DRS .body-text spec: color to ecru-dim (60%, was 84% via --body), line-height to 1.8 on body / 1.7 on lede (were 1.6 to 1.7), and font-size to rem (1.05rem body, 1.15rem lede, was px). Base body line-height 1.55 to 1.6.
**Rationale:** The body read more solid and slightly cramped than the other DRS pages, which use a softer ecru-dim at airier 1.8 line-height. Now uniform with last-50-feet et al.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-23] — TIER 1 — R&D / DRS (Rock Audit heading treatment)
**Change:** Harmonized rock-audit.html headings with the DRS family while keeping Imbue at 700: page title and section heads now UPPERCASE, eyebrow/kicker mono labels bold (700), and the SHOW/STALL/SWAP question titles kept title-case but recolored to brand teal for dimension (the interactive layer, distinct from the uppercase ecru heads).
**Rationale:** Rock Audit read different from last-50-feet because its headings were title-case and its labels regular weight. Uppercase + bold labels close the gap without the 900 weight Angie rejected.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-23] — TIER 3 — L&D (two-column layout)
**Change:** Laid the two L&D collections side by side as columns on ld/infrastructure-of-a-life.html. Wrapped both in a .ld-collections two-column grid (page-scoped inline CSS), cards stack vertically within each column, capped column h2 size, and the grid collapses to one column at 900px. Anchors (#supply-closet-romance, #em-dash-unpacking) preserved on the column divs.
**Rationale:** Presents the two collections at a glance instead of one long scroll. Per Angie's direction.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-23] — TIER 3 — L&D (Infrastructure of A Life restructure)
**Change:** Split ld/infrastructure-of-a-life.html from one mixed "The Collection" block into two distinct collection sections with anchor IDs (#supply-closet-romance, #em-dash-unpacking), each with its own header and intro. Wrote descriptions for the four Em-Dash Unpacking cards (were empty). Dropped the conflating "no business in the same section" intro. Deep-linked the two homepage L&D cards to their matching collection anchors. Updated site-map.md.
**Rationale:** The page hosts two intentional collections now, not one jumbled pile. Each stands on its own and the index cards land readers on the exact collection they clicked. Piece cards stay Coming placeholders until the article pages are built.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-23] — TIER 1 — R&D / DRS (Rock Audit Imbue weight)
**Change:** Dropped Imbue display headings on rock-audit.html and rock-audit-worksheet.html from weight 900 to 700, matching the SOP Playbook Builder content-heading weight. (SOP reserves 900 for its single top hero only.)
**Rationale:** 900 read too heavy across the Rock Audit pages; 700 matches the lighter Imbue treatment Angie pointed to on the SOP Playbook Builder page.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-23] — TIER 2 — L&D (index cards)
**Change:** Removed the "Enter L&D" card-action label from both L&D cards (A Supply Closet Romance, Em-Dash Unpacking) on index.html. Cards remain fully clickable.
**Rationale:** Redundant CTA text; the cards are already links and the section header names L&D.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-23] — TIER 2 — Resources (Receipt Drawer)
**Change:** Added a Rock Audit card to the Tools category of /resources/ (links to rd/dignity/rock-audit.html), matching the Operational Telemetry printable pattern. Updated site-map.md Resources count (Tools 4 to 5, total 16 to 17).
**Rationale:** The Rock Audit is a printable field tool and belongs in the Receipt Drawer next to the other R&D printables. One card to the landing (the front door to the worksheet), not a duplicate Templates entry.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-23] — TIER 1 — R&D / DRS (Rock Audit nav)
**Change:** Replaced the landing's hand-styled inline nav with the exact site .nav-bar (fixed full-width, IBM Plex Mono links in ecru-dim at 0.85rem, quetzal mark, rosso hover underline, spine-left offset + responsive rules). Added a 7rem hero top offset to clear the fixed nav.
**Rationale:** The header menu on rock-audit.html was not uniform with the other DRS pages because it was built inline instead of mirroring /styles.css .nav-bar. Inlined the exact nav rules (no full stylesheet import, to avoid class collisions with the page's bespoke layout).
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-23] — TIER 1 — R&D / DRS (Rock Audit typography)
**Change:** Aligned rock-audit.html and rock-audit-worksheet.html typography to the site system: Imbue display headings now weight 900 (were 700) at responsive clamp() sizes (were fixed px), and the landing's body prose is the site's light Plex Sans 300. Loaded the matching Imbue 900 + Plex Sans 300 weights.
**Rationale:** The two pages were self-contained and had drifted from /styles.css typography (heading weight, heading size scale, body weight), so they read as a different font and incongruent header sizes next to the other DRS pages.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-23] — TIER 1 — SEO infra (sitemap.xml)
**Change:** Added rd/dignity/rock-audit.html (priority 0.7) and rd/dignity/rock-audit-worksheet.html (0.6) to sitemap.xml and bumped last-50-feet lastmod to 2026-06-23. The /go/drs-rock and /rock stubs stay excluded (noindex redirects).
**Rationale:** New indexable pages need to be in the sitemap so Search Console and Bing discover them on the next crawl. Worksheet included per the existing precedent that template/leaf tool pages are listed.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-23] — TIER 2 — R&D / DRS (Last 50 Feet)
**Change:** Added a Rock Audit launch CTA to the close of rd/dignity/last-50-feet.html (links to rock-audit.html), so the field tool launches from the essay it operationalizes. Clarified the close headline from "The Floor Was Never Asked" to "The People on the Floor Were Never Asked" so "the floor" reads as the people, not a place.
**Rationale:** Last 50 Feet is the strongest contextual entry point for the Rock Audit; readers finishing that essay should be handed the tool there. Headline clarity for the non-technical default audience.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-23] — TIER 3 — R&D / DRS (Rock Audit field tool)
**Change:** Added the Rock Audit field tool to the DRS series: landing (rd/dignity/rock-audit.html) and printable worksheet (rd/dignity/rock-audit-worksheet.html). Landing carries the 7-item nav, GA4 tag and dark-page html background; worksheet has a leaf nav, GA4 tag and a Print/Save button wired to the `template_download` event. Minted `/go/drs-rock` (→ rock-audit.html, utm_campaign=drs-rock) and an evergreen root vanity `/rock` (→ rock-audit.html, no UTM) via a new optional `path` override in scripts/build_links.py + _links.json. Surfaced the tool as a field-tool CTA on the DRS index. Updated site-map.md and docs/analytics-runbook.md.
**Rationale:** Companion to the "Find the Rocks" LinkedIn post (DRS Last 50 Feet territory). The post's first comment points at /go/drs-rock, which had to resolve before publish. Evergreen /rock keeps tool/worksheet traffic off the post campaign.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-18] — TIER 1 — Short links (/go/ drs-operator)
**Change:** Minted `/go/drs-operator` → `/rd/dignity/diagnostic-model.html?utm_source=linkedin&utm_medium=organic_social&utm_campaign=drs-operator`. Added to `_links.json`, regenerated stubs via `scripts/build_links.py`, refreshed the runbook live-slug snapshot.
**Rationale:** Fourth post in the DRS series (third /go/ link), pointed at the diagnostic model like Maverick and Detective. GA4 separates the three by utm_campaign and the short_link_click slug.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-18] — TIER 1 — Short links (/go/ drs-detective repoint)
**Change:** Repointed `/go/drs-detective` from `/rd/dignity/` to `/rd/dignity/diagnostic-model.html` (UTMs unchanged). Updated `_links.json`, regenerated the stub via `scripts/build_links.py`, refreshed the runbook live-slug snapshot.
**Rationale:** The post's first comment promises "the whole pattern" (the diagnostic model). Aligns Detective's destination with Maverick's; GA4 still separates them by utm_campaign and the short_link_click slug.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-18] — TIER 1 — Short links (/go/ drs-detective)
**Change:** Minted `/go/drs-detective` → `https://angieqbailey.com/rd/dignity/?utm_source=linkedin&utm_medium=organic_social&utm_campaign=drs-detective`. Added the slug to `_links.json` and regenerated stubs via `scripts/build_links.py`. Updated docs/analytics-runbook.md with the current live-slug snapshot.
**Rationale:** Clean tracked LinkedIn link for the drs-detective post, driving to the DRS hub. Second link in the /go/ system; links are minted per post, not batch-created.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-18] — TIER 1 — Docs (runbook maintenance rule)
**Change:** Added a "keep this current" rule to docs/analytics-runbook.md: any GA4 / Search Console / Bing / event-tracking / custom-dimension / key-event / /go/ change must update the runbook in the same task. Mirrored in Claude memory and the project config.
**Rationale:** "Is the repo current?" only checks commit state and won't catch a runbook that's drifted from the live external tools. A write-time rule prevents drift instead of relying on a check.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-18] — TIER 2 — Docs (analytics infrastructure runbook)
**Change:** Added `docs/analytics-runbook.md` — as-built record of the GA4 / Search Console / Bing stack, a break-fix playbook for each piece, and a step-by-step for standing the whole stack up on a new site. No secrets (deploy token stays in Claude memory).
**Rationale:** Removes single-operator dependency. Anyone can fix or recreate the analytics/search setup, including for additional URLs beyond the personal site.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-18] — TIER 1 — Debrief (contact link tracking)
**Change:** Added a GA4 `contact_click` event (method: email) to the Debrief mailto link on index.html, so clicks on angie@angieqbailey.com register as a tracked action. Guarded with if(window.gtag) so a missing tag can never break the link.
**Rationale:** Email contact is the site's real conversion. This makes "someone tried to reach me" measurable, to be marked a key event in GA4 once it surfaces.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-18] — TIER 1 — Site-wide (template & artifact Print buttons)
**Change:** Instrumented every "Print / Save as PDF" button across all template and artifact pages (31 pages: every post family plus hello-world and resources) to fire a GA4 custom event `template_download` with a `template_path` parameter (the page path), then print. Guarded with `if(window.gtag)` so a missing tag can never block printing. Inline-onclick buttons got the call inside the onclick; the interactive pages (interactive-channel-audit, safety-first-gate) got it inside their print handler.
**Rationale:** GA4's built-in file_download tracking can't see these because the templates are HTML pages saved via window.print(), not file links. The custom event gives a high-intent download signal, counted in GA4 and folded into the weekly report (new section A6). A Print/Save click is intent, not a confirmed save.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-18] — TIER 1 — R&D (DRS / diagnostic-model.html)
**Change:** Made the page-meta back-link obviously clickable. Changed `.page-meta a` from quetzal-bright/no-underline (which matched the surrounding meta text) to ecru with a persistent quetzal-bright underline; hover inverts the two. The link now stands apart from the "R&D //" prefix.
**Rationale:** The prior styling was indistinguishable from plain text, so the link read as static.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-18] — TIER 1 — R&D (DRS / diagnostic-model.html)
**Change:** Made the "The Dignity-Required System" text in the page-meta header a same-tab link to /rd/dignity/. Added a `.page-meta a` rule mirroring the existing `.back-link-row a` style (quetzal-bright, no underline, ecru on hover). No other content or layout change.
**Rationale:** Gives readers a top-of-page route back to the DRS hub, matching the existing bottom back-link.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-17] — TIER 3 — Warehouse (Post-Acquisition / Reframe to Own Framework)
**Change:** Reframed `posts/post-acquisition-integration-launch/post-acquisition-integration-launch.html` from a specific employer engagement to Angie's own repeatable post-acquisition e-commerce integration framework, and decoupled it from the (confidential, non-public) real acquisition. Main page: meta/og/twitter/schema descriptions reframed from "Architected the first e-commerce acquisition integration at a multi-billion-dollar company" to "A framework for standing up e-commerce after an acquisition"; the acquired company is no longer identified as "an industrial supply distributor/company" (lede, situation, pressure point all genericized to "a newly acquired business" / "the catalog"); "B2B industrial catalog" became "B2B catalog"; "Cloud Ops" became "cloud operations"; outcome narrative reframed from "the first... this organization had ever attempted" to "a repeatable... architecture"; two Oxford commas fixed in passing. The `assets/product-taxonomy-architecture.html` example catalog was rebuilt entirely from industrial-supply products (Tools, PPE, Fasteners, Abrasives, Material Handling) to illustrative outdoor and recreation gear (Camping, Climbing, Paddling, Apparel) across all 12 example rows, and its descriptions changed from "an industrial supply e-commerce catalog" to "an acquired B2B e-commerce catalog." Section structure, artifacts, metrics and the durability close are unchanged.
**Rationale:** The acquired company is a confidential, deliberately non-public acquisition. A case study depicting an industrial-supply acquisition plus its product catalog could corroborate or surface that deal, especially if it later goes public. Reframing to Angie's own framework with an illustrative (non-industrial) example catalog removes the corroborating detail while preserving the capability demonstration, and is the stronger IP-ownership posture.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-17] — TIER 2 — Warehouse (E-Commerce Summit / Dependency Map)
**Change:** Genericized one dependency-map cell in `posts/e-commerce-summit/assets/dependency-friction-map.html`: "Branch Sales Goals Set" became "Sales Team Goals Set." No other changes. A full comb-through of all 11 e-commerce summit files (case study, 5 artifacts, 5 blank templates) found no other EquipmentShare tells; the warehouse, distribution-center, fulfillment and procurement references are legitimate e-commerce operations.
**Rationale:** "Branch Sales Goals" competing with e-commerce reproduced the prior employer's branch-network-plus-online-channel structure. The generic label keeps the friction logic (a separate sales function with competing, unshared targets) without the branch-network implication.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-17] — TIER 3 — Warehouse (Crisis Communications / Reframe to Own Framework)
**Change:** Repositioned `posts/crisis-communications-architecture/crisis-communications-architecture.html` from an employer-engagement narrative to Angie's own framework, while keeping the case-study structure. Reframed the meta, og, twitter and schema descriptions from "for a large-scale company" to "for distributed, multi-site operations." The lede now opens on the general gap and states "So I built one from scratch" (self-initiated authorship) rather than "a large-scale company had no infrastructure." The situation reframes "The company had scaled fast" to a general operating condition. Softened two adoption-implying outcome stats to capability: "First crisis comms infrastructure ever built" became "From nothing to a complete system"; "Locations covered by the system" became "Locations the system is designed to cover." The outcome narrative now reads "The result is a complete crisis communication system, built from nothing and ready to deploy" instead of "The organization went from zero to a deployable system." Pressure-points diagnostic, artifacts, approach and section structure unchanged.
**Rationale:** The crisis system was a self-initiated project that was never adopted. Framing it as Angie's own framework rather than a delivered engagement is both more accurate and the stronger IP-ownership posture, and it removes adoption claims that overstated the work and undercut that posture.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-17] — TIER 2 — Warehouse (Web Experience Capacity / Metric)
**Change:** Genericized one outcome label in `posts/web-experience-capacity-build/web-experience-capacity-build.html`: "Rental Requests Completed Online" became "Requests Completed Online." No other content, layout or structural changes.
**Rationale:** "Rental Requests" referenced the prior employer's equipment-rental business. The generic label preserves the metric's meaning (online self-service completion) without the industry fingerprint.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-17] — TIER 2 — Warehouse (Homepage Cards Genericization)
**Change:** Genericized two Warehouse cards on `index.html` to match the already-scrubbed case studies. Crisis card: "A $1B+ industrial technology company had zero crisis communication infrastructure" became "A large-scale company had zero crisis communication infrastructure." Newsletter card: "80% of employees worked in the field" became "More than three-quarters of employees worked in the field." The MBR card's "$1B+ organization" was left as-is (generic scale indicator, no employer fingerprint). No structural, layout or CSS changes.
**Rationale:** The homepage cards still carried the "$1B+ industrial technology company" descriptor and the precise "80%" figure after the underlying case studies were genericized. This aligns the cards with the deployed case-study copy.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-17] — TIER 2 — Warehouse (Crisis Communications / Genericization)
**Change:** Genericized EquipmentShare fingerprints in `posts/crisis-communications-architecture/crisis-communications-architecture.html`. Removed "Significant field assets" from the lede and changed "Significant field assets exposed to weather" to "Field teams exposed to weather" in the situation (drops the heavy-equipment implication, centers the people). Changed "80% of the workforce operated in the field" to "More than three-quarters of the workforce operated in the field." Dumped the hurricane/meals narrative: removed the "Hurricane season alone put dozens of locations in direct threat paths annually" line, removed the "5,000 meals served during active hurricane activation" outcome stat (grid is now 5 stats), removed the "battle-tested during an active hurricane emergency..." sentence from the outcome, and softened "past weather events" to "past emergencies" in the volunteer-infrastructure finding. No structural, layout or CSS changes.
**Rationale:** Same anonymization pass applied to the other case studies. The field-assets-exposed-to-weather phrasing and the hurricane-plus-meals combination were the strongest triangulation points toward the prior employer's publicized disaster-relief work. Slack and the generic disaster-response framing stay. An alternative outcome-proof narrative is under discussion to fill the gap left by the removed hurricane proof.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-17] — TIER 2 — Warehouse (Enterprise Newsletter / Style Guide Rewrite)
**Change:** Rewrote the body copy and examples of `posts/enterprise-newsletter-architecture/assets/in-house-style-guide.html` so the expression is original rather than a verbatim lift of the prior employer's style guide. Section titles, purposes, logic and the rule set are unchanged; the prose in every section is reworded and every example is swapped: Voice & Tone, Style Standards, Capitalization (example name now "Operations Director Bobbi Baldwin"), Punctuation, Numbers, the No-Fly List intro and all 7 entries, the 8 Approval Process step labels, and the closing line. No structural, layout or CSS changes.
**Rationale:** The underlying rules are standard editorial conventions and not protectable, but verbatim wording and examples are. Rewriting the expression removes the copyright exposure while preserving the demonstrated capability.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-17] — TIER 2 — Warehouse (Enterprise Newsletter / Style Guide Title)
**Change:** Renamed the "The Voldemort List" section in `posts/enterprise-newsletter-architecture/assets/in-house-style-guide.html` to "The No-Fly List". Also renamed the underlying CSS classes `voldemort-list` to `banned-list` and `voldemort-item` to `banned-item` (style definitions and all entry divs), so no "Voldemort" reference remains anywhere in the source. List contents unchanged. No layout or structural changes.
**Rationale:** "Voldemort" is borrowed IP (Warner Bros / J.K. Rowling) and out of place on a commercial site being scrubbed for legal exposure. "The No-Fly List" preserves the forbidden-words meaning without borrowing anyone's IP.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-17] — TIER 2 — Warehouse (Enterprise Newsletter / Style Guide De-fingerprinting)
**Change:** Genericized the Voldemort List in `posts/enterprise-newsletter-architecture/assets/in-house-style-guide.html`. Item #1 reworded from telematics product-speak ("surveillance language... Instead use: 'asset visibility,' 'workforce management,' 'operational oversight'") to a neutral field-services note ("surveillance framing for operational tools... Instead use: plain descriptions of what the tool does for the team: 'shift scheduling,' 'dispatch coordination,' 'job status updates'"). Item #2 ("'sell' when describing technology adoption" reframed to "educate / enable / empower") removed entirely; the list goes from 8 entries to 7. The six generic brand-voice entries are unchanged. No structural, layout or CSS changes.
**Rationale:** "Asset visibility" is the prior employer's product euphemism, and the surveillance plus tech-adoption framing pointed at a GPS/telematics company. Removing both lines de-fingerprints the style guide while keeping the brand-voice lesson intact.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-17] — TIER 2 — Warehouse (Enterprise Newsletter / Workforce Genericization)
**Change:** Genericized the employer-identifying workforce descriptors in the Enterprise Newsletter case study, reframing the workforce as a generic field-services operation. (1) `posts/enterprise-newsletter-architecture/assets/internal-comms-channel-audit.html`: "Rental Coordinators" → "Service Coordinators"; the precise "80%" deskless figure → "more than three-quarters" in both spots. (2) `posts/enterprise-newsletter-architecture/enterprise-newsletter-architecture.html`: "yard workers" → "warehouse staff"; "80% of the workforce did not sit at desks" → "More than three-quarters of the workforce did not sit at desks". The deskless-field-workforce premise (branches, drivers, service technicians, regional and area management) is retained; it holds water for a field-services company and is not employer-identifying. No structural, layout or CSS changes.
**Rationale:** Remove the EquipmentShare rental/yard fingerprint and the specific internal headcount figure while keeping the diagnostic methodology and case structure intact. The mortgage filter was rejected for this case: a lender has no large deskless field workforce, which is the entire premise here. Field-services framing maps to the existing vocabulary with minimal change.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-17] — TIER 2 — Warehouse (Blank Template Ownership)
**Change:** Removed the personal authorship/ownership attribution block from all seven downloadable blank templates across three case studies, so the printable blanks make no ownership or authorship claim. Files: `posts/marketing-infrastructure-mbr/assets/templates/cross-functional-mbr-template-blank.html` and `reporting-governance-cadence-blank.html`; `posts/ecommerce-pl/assets/templates/pl-cutoff-definition-blank.html` and `pl-project-dossier-blank.html`; `posts/enterprise-newsletter-architecture/assets/templates/channel-mix-matrix-blank.html`, `ic-strategic-value-architecture-blank.html` and `internal-comms-channel-audit-blank.html`. Deleted the `<div class="attribution">...by Angie Bailey // angieqbailey.com</div>` footer from each. Unused `.attribution` CSS left in place (no visual effect). No other content, layout or structural changes.
**Rationale:** A downloaded blank carrying only "Framework / Methodology / Diagnostic Tool by Angie Bailey" can be misread as a sole-ownership claim over work product or as an official company artifact. Removing the attribution defuses both readings. No disclaimer added, per Principal's direction.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-18] — TIER 3 — Short Links (/go/)
**Change:** Stood up a self-hosted short-link system. New files: `_links.json` (slug registry, single source of truth), `scripts/build_links.py` (generator that writes one `go/[slug]/index.html` stub per registry entry), and the first stub `go/drs-maverick/index.html` → `rd/dignity/diagnostic-model.html?utm_source=linkedin&utm_medium=organic_social&utm_campaign=drs-maverick`. Each stub carries the GA4 tag, fires a `short_link_click` event (slug as parameter, beacon transport, event_callback redirect, 250ms timeout fallback, 2s meta-refresh fallback for no-JS), and is `noindex,nofollow`. Stubs are excluded from sitemap.xml. No change to index.html, nav, or any existing page; these are isolated leaf redirect pages following the existing drs-matrix pattern.
**Rationale:** Lets LinkedIn posts use clean `angieqbailey.com/go/[slug]` links that hide the long UTM string while still registering the campaign on the landing page, and gives per-slug click counts in GA4 (G-S0MXDDKP4E) independent of UTM noise. Path A (static stubs) chosen over a Cloudflare Worker to avoid a DNS migration; the domain serves directly from GitHub Pages.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-17] — TIER 2 — Warehouse (Marketing Infrastructure MBR Debt Clearance)
**Change:** Completed the anonymization pass on the MBR case study, removing residual prior-employer fingerprints from the live pages. (1) `posts/marketing-infrastructure-mbr/marketing-infrastructure-mbr.html`: smoothed the remaining inventory/P&L/Slack bottleneck line ("Moved inventory and P&L data... The Slack-interrupt-and-wait cycle ended" → "Moved operational and margin data... The request-and-wait cycle ended"), the layoff line ("terminated alongside more than 100 headquarters and executive employees" → "let go in a broader corporate restructure"), and the "scaling technology company" descriptor → "scaling company". (2) `posts/marketing-infrastructure-mbr/assets/cross-functional-mbr-template.html`: deleted the "Platform names retained to demonstrate technical breadth" line; renamed "Online Parts (DTC)" → "Online Storefront (DTC)" and "Promotional Merchandise / Swag Operations / Swag Store, Shopify Integration" → "Branded Merchandise / Brand Operations / Brand portal, print fulfillment"; swapped niche tools to known competitors (Klaviyo → Braze, CallRail → Invoca, Impact → Partnerize, Chatmeter → Sprout Social, Shopify → commerce platform); neutralized e-commerce-leaning metric and definition examples. (3) `posts/marketing-infrastructure-mbr/assets/reporting-governance-cadence.html`: smoothed the layoff line, the "scaling technology company" descriptor → "scaling organization", and the two Slack references → "team channel" / "team thread". Industry-neutral approach (no specific vertical), consistent with the prior live edits. Blank template unchanged. No structural, layout or CSS changes.
**Rationale:** Finish removing the prior-employer signature (equipment-rental/parts business model, P&L-via-request bottleneck, specific reported layoff) while keeping the operational structure intact. Niche SaaS tools swapped to credible competitors so the stack reads real without reproducing the original. Applied as targeted diffs against the live repo after pull-before-deploy revealed the local workspace copy was stale.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-17] - [TIER 1] - R&D (DRS / 902-meeting.html)
**Change:** Recast the character Jeremy in the 9:02 AM Meeting fable from a fast flaw-spotter into the Operator archetype. He now reads as someone with deep mastery asked to vouch for a system whose reasoning he can't see. Replaced his introduction block (now four paragraphs) and his "Thirty days later" beat. No other character or plot point changed.
**Rationale:** Aligns the fable's Operator stand-in with the de-IT-coded reader framing applied to diagnostic-model.html. Removes the developer-coded "spotted the flaw, built a workaround" framing in favor of the operations reality of signing off on what you can't inspect.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-17] - [TIER 1] - R&D (DRS / diagnostic-model.html)
**Change:** Rewrote the "You'll recognize them as" recognizer text in the Maverick (Surplus + Output) and Operator (Surplus + Mastery) quadrants of the Four States of Adoption Reality 2x2. Removed IT/developer framing (VP with the AI tool, CRM in Notion, reads documentation for fun, architect) and replaced with non-technical operations language. Topic stays AI-specific; reader is no longer coded as having a technical job.
**Rationale:** This page is the click-through destination from LinkedIn posts written for a non-technical HR, operations, marketing, comms and L&D audience. The technical framing lost that reader on arrival.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-17] — TIER 1 — R&D (Dignity-Required System / Four States of Adoption Reality)
**Change:** Mobile fix on `rd/dignity/diagnostic-model.html`. The 2x2 columns were rendering unequal on narrow screens (right column pinched) because the collapsed detail panels still fed their content width into the grid track sizing. Added `min-width: 0` to `.quadrant` so the two `1fr` columns split evenly regardless of hidden content, plus `overflow-wrap: break-word` so long strings wrap instead of widening a column. No content, color or layout-structure changes.
**Rationale:** Equal quadrants at every breakpoint. The left axis labels were a red herring (absolutely positioned, outside the grid); the real cause was grid items defaulting to a content-based minimum width.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-06-17] — TIER 2 — R&D (Dignity-Required System / Four States of Adoption Reality)
**Change:** Reworked `rd/dignity/diagnostic-model.html`. Renamed the page so the H1 reads "Four States of Adoption Reality"; removed "Operational Reality Assessment" from the H1, the page title, og:title, twitter:title and the JSON-LD headline. Retired the duplicate widget heading and promoted "DRS Framework / 2x2 Model" to the section H2. Brightened the instruction line ("Click a quadrant...") to ecru weight 500 so it sits above body copy. Restored the interactive 2x2 to its earlier full-glory build (recovered from the pre-redirect drs-matrix commit b828e0b3): solid Quetzal quadrants, ecru gridlines and frame, rosso center crosshair, framed axis-label cells, smooth-expanding detail panels. Adapted that light-page design to the dark canvas: active quadrant now signalled by a rosso inset frame (the old "turn black" cue is invisible on Nuit), detail panels render on Nuit with a rosso accent. Quadrant names set in Parisian Night, slightly enlarged, with a rosso accent bar (Valentino red failed contrast on the teal at ~1.7:1; Parisian Night reads ~2.6:1 plus bold weight). Fixed the left vertical axis labels (clipping/misaligning in the diminished build) via bordered vertical-cell layout with proper container padding. Tightened heading-to-grid and grid-to-thesis spacing. Split the closing verdict line ("If someone is a Fixer on Tuesday...") onto its own rosso line. Fixed a flex bug (min-height:0 on the detail panel) that left all four panels expanded at once. Body prose left at site-standard ecru-dim / weight 300 (consistent with sibling DRS pages; passes AA at ~6:1) pending a separate site-wide legibility review.
**Rationale:** The page now leads with the idea, not the assessment label. The matrix had been visually diminished when it moved off the 9:02 page onto its own page; this returns it to the richer, legible build and adapts it correctly to the dark variant. Contrast was checked numerically at each step rather than eyeballed.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-05-22] — TIER 2 — R&D (Dignity-Required System / Hub Page)
**Change:** Tightened the Sponge Leadership definition in the standalone element on `rd/dignity/index.html`. Replaced the previous 49-word paragraph ("The friction fronts diagnose organizational patterns. This diagnoses what those patterns cost the people absorbing them. Every system that ignores cognitive bandwidth, professional identity or organizational trust still needs someone to manage the fallout... and that someone has no circuit breakers, no rotation and no structural protection.") with the new 38-word version ("The friction fronts diagnose organizational patterns. This diagnoses what those patterns cost the managers absorbing on behalf of their team. Every system that ignores bandwidth, professional identity or organizational trust still needs someone to manage the fallout."). No structural, layout or CSS changes. No anchor or link changes. -75 bytes file size.
**Rationale:** Specificity over hedging. "People absorbing them" was vague; "managers absorbing on behalf of their team" names the role and the directionality. Drops "cognitive" before bandwidth (the friction fronts already define what kind of bandwidth) and drops the closing circuit-breaker / rotation / structural-protection clause (those details belong on the child page, not the hub teaser). Hub copy reads tighter and the click-through to `empathy-redlining.html` carries the structural-absence detail at full strength.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-05-22] — TIER 2 — R&D (Dignity-Required System / Section XX)
**Change:** Deployed Section XX of the Dignity-Required System: `rd/dignity/empathy-redlining.html` titled **Sponge Leadership** (unnumbered depth report on the human cost of emotional absorption work). Dark variant. Built against the seven-beat structure established by Sections 01-05 (header/friction front, the findings, why existing approaches fail, three-concept diagnostic vocabulary, what this means at rollout, the close, expandable inline glossary). New terms defined here as glossary cards: empathy redlining, the human sensor, circuit breaker (emotional). Crossover (Westman), surface acting / deep acting (Hochschild) and compassion fatigue (Figley) appear in body text only, not as glossary cards, per handoff brief registry. Page title / og:title / twitter:title / JSON-LD headline all lead with "Sponge Leadership" rather than the URL slug — Sponge Leadership is the page concept, empathy-redlining.html is the file path (Section XX nomenclature shift mid-build). Research citations hyperlinked inline (10 total): Bonnaire, Boudrias & Vandenberghe 2024 Frontiers (the anchor cascade — 62 managers / 74 teams / Canadian govt org, manager exhaustion → laissez-faire → psych safety drop → readiness drop), Figley 1995 (compassion fatigue clinical foundation, EMDR Israel open PDF), McCann & Pearlman 1990 (vicarious trauma clinical foundation, APSAC open PDF), Hochschild 1983 (emotional labor framework, UC Press), Iszatt-White 2013 (extends Hochschild to leadership specifically, ResearchGate open chapter), Üngüren, Tekin & Avsallı 2025 Frontiers (Cost of Smile — surface acting → burnout → work alienation, 85 hotels Turkey), Westman 2001 + Hartmann et al. 2025 cited together for crossover theory and team-level emotional contagion evidence (237 employees / 41 professional services teams), Maslach & Jackson 1981 (cited for CONTRAST — burnout syndrome vs absorption-specific mechanism), Bakker, van Emmerik & Westman 2011 (310 employees / 100 teams Dutch employment agency — crossover of emotional exhaustion ONLY in HIGH-cohesion teams, connection-as-conduit finding handled honestly in Beat 3), Waytz HBR March 2022 + Carnevale HBR April 2022 (practitioner framing for compassion fatigue applied to managers, marked as practitioner not empirical). All links verified no-login. No `target="_blank"`. The "weekly supervision reduces compassion fatigue by 40%" claim from the original brief was DROPPED at research phase as unsourced and contradicted by Linley & Joseph 2007 (no significant supervision effect on CF in psychologists); replaced with the alternative framing "evidence on whether protections reduce CF is mixed and depends on implementation quality, but absence of any structural protection produces measurably worse outcomes than partial protection." Section 4 (`rd/dignity/growth-collapse.html`) received a one-line edit: `id="human-shock-absorber"` added to the human shock absorber glossary card to enable cross-section anchor linking. Hub page NOT modified (already has Sponge Leadership element from 2026-05-22 hub restructure). Site-map updated: new R&D row, R&D pages 14 → 15, Total HTML 93 → 94.
**Rationale:** The depth report below the five friction fronts. Where Sections 01-05 answer "what breaks in the system," Sponge Leadership answers "what breaks in the person the system leans on." The single hardest constraint was the bridge reframe: the compassion fatigue label has stayed clinical in the peer-reviewed literature, so the page uses Figley / McCann & Pearlman / Maslach as the established clinical mechanism (what it IS) and Hochschild / Iszatt-White / Üngüren / Bonnaire / Westman / Bakker / Hartmann as the operational evidence (what it COSTS in non-clinical settings). No clinical study is cited as proof of operational impact. The research phase ran first as a separate session that answered three viability gate questions (gate passed with reframe — three of three glossary terms held from brief, mechanism evidence flagged as moderate vs strong), verified every stat against primary sources, dropped the 40% supervision claim as unverifiable, and pinned the Bakker crossover-only-in-cohesive-teams finding as the section's hardest honest move (connection is the conduit through which absorption operates, not a protective factor against it — team-building that thickens connection without adding circuit breakers makes the mechanism more efficient, not less costly). Prose draft went through V1 → V3 voice passes: V1 was flagged as too academic / too dense in research density / used "mechanism" too often, V2 cut roughly 25% of word count and front-loaded recognition before research in each beat, V3 (the deployed version) replaced "The Mechanism IS the Cost" with "Drained Manager, Drained Team" and rewrote the verdict line "The cost isn't the manager" to "She IS the cost. What she carries downward is the bill the team pays," extended the sponge metaphor to a sunlight verdict line ("she's a sponge nobody's left out in the sun"), softened three "load" instances to "weight she's carrying" / "what she's actually carrying" / "emotional weight" while keeping precision-load language in the staffing-constraint paragraph, replaced ambiguous "hard signal" diagnostic question with "what her team wasn't saying out loud," collapsed five citation paragraphs into three for breathing room, and linked the Beat 5 H2 "Circuit Breakers Are Structural, Not Cultural" directly to /verdict/structure-is-how-you-protect-people.html (Verdict #4). The "people-sensors" phrasing in the Beat 6 callout was Principal's specific rewrite to reinforce that these are people, not parts.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-05-22] — TIER 1 — R&D (DRS Section 04)
**Change:** Added `id="human-shock-absorber"` attribute to the human shock absorber `<details class="glossary-card">` element on `rd/dignity/growth-collapse.html`. Enables fragment-anchor linking from Section XX (Sponge Leadership) directly to the relevant card on Section 04 instead of dumping the reader at the top of the Growth Collapse page. Single attribute add. No content, structure, voice or CSS changes.
**Rationale:** Sponge Leadership opens with the link sentence "Section 4 named the role. This section diagnoses what the role costs." Linking to `growth-collapse.html` alone landed the reader at the page top with no path to the human shock absorber definition. The anchor makes the cross-reference functional rather than ceremonial.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-05-22] — TIER 3 — R&D (Dignity-Required System / Hub Page)
**Change:** Restructured DRS hub page (`rd/dignity/index.html`). Extracted interactive matrix widget (four quadrants: Operator, Detective, Maverick, Fixer with detail panels, axis labels, toggle JS) to new standalone page at `rd/dignity/diagnostic-model.html` titled "Operational Reality Assessment." Added Sponge Leadership standalone element between friction front cards and governors — not numbered, not a grid card, positioned as conclusion-weight content linking to `empathy-redlining.html`. Added routing CTA to diagnostic model page where matrix formerly sat. Removed all matrix-related CSS (~160 lines) and JS (~30 lines) from hub. Kept governors on hub. New page has full dark variant, 7-item nav, GA4, SEO stack (og:title, JSON-LD, canonical, Twitter Card). Hub scroll order: header/thesis → friction fronts (5 numbered + 9:02 AM) → Sponge Leadership → model CTA → governors → footer. Site-map updated: new R&D row, R&D pages 13 → 14, Total HTML 92 → 93.
**Rationale:** ICP cognitive journey analysis determined the matrix widget was third-visit analytical content competing for attention on a page whose primary job is first-visit recognition. Extracting it to its own page gives the model room to breathe and reduces hub scroll depth. Sponge Leadership element positions Section XX (the human cost report) as the bridge between "what breaks in the system" (friction fronts) and "what holds the system accountable" (governors). The hub now reads as a narrative path: here are the patterns → here's what they cost the person absorbing them → here's the deeper model → here are the governance requirements.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-05-22] — TIER 2 — R&D (Dignity-Required System / Section 05)
**Change:** Deployed Section 05 of the Dignity-Required System: `rd/dignity/signal-loss.html` — a findings report on signal loss between the floor and the boardroom. Dark variant. Built against the six-beat structure established by Section 04 (friction front, the findings, why existing approaches fail, three-concept diagnostic vocabulary, what this means at rollout, the close) with three expandable inline glossary terms using native `<details>` elements. New terms defined here: signal attenuation, proprioceptive drift (organizational), the mum effect. The deaf effect, the CEO bubble and the three governors appear in body text only, not as glossary cards (per handoff brief registry). Research citations hyperlinked inline (12 total): Lovich & Meier HBR Nov 2025 (executive AI perception gap, 45-point and 51-point), BCG AI at Work 2025 (10,600 employees / 11 countries — underlying data for Lovich & Meier), Smith & Keil 2003 ISJ (the mum effect named), Park, Im & Keil 2008 JAIS (mum effect experimental followup), Cuellar, Keil & Johnson 2006 (the deaf effect, receiving-side complement), Keil et al. MIT Sloan 2014 (operational synthesis from 14 IT project status reporting studies — pinned from "MIT Sloan unspecified" per research phase), Athanassiades 1973 AMJ via PMI library companion (foundational upward communication distortion paper — citation-chain treatment), Hofstede 1980 with 1967-1973 IBM survey data caveat acknowledged, GLOBE Project 2004 with corrected respondent count 17,300 (research phase caught the original brief's "17,000" miscount), Ashkenas HBR 2017 (executive isolation), Vistage 2017 (CEO bubble — practitioner attribution required, verbatim quote verified — research phase caught that the original brief's paraphrase wasn't in the source), Tsai CEIBS 2025 ("survival wisdom" — academic-adjacent), Botvinick & Cohen Nature 1998 via Carnegie Mellon mirror (rubber hand / proprioceptive drift neuroscience anchor), Parent & Reich California Management Review 2009 (three-layer IT governance + UK government project failure data), Wooldridge Schmid & Floyd Journal of Management 2008 (middle manager strategic translation layer), McKinsey Diversity Wins 2020 with triple correction (likelihood to outperform on profitability NOT "more profitable," ethnic and cultural diversity NOT "cognitive diversity," top-quartile vs fourth-quartile NOT raw claim — all three dimensions of the original brief's framing were factually wrong). All links verified no-login. No `target="_blank"`. Hub page `rd/dignity/index.html` updated: Section 05 card activated (removed `coming` class and "Coming" status div). This was the LAST coming card — all five friction fronts now active. Site-map updated: new R&D row added under DRS.
**Rationale:** Fifth and final child report under the DRS hub. The most politically charged section in the series, requiring the tightest ethical drift filter — every sentence had to describe a structural mechanism, never moralize about leadership behavior. Lead is the BCG/Columbia AI perception gap, chosen as the anchor over Hofstede/GLOBE structural research per the handoff rule (concrete first, then back with the research). The 45-point and 51-point gaps land the "executive sees one org, the floor sees another" claim viscerally before the IS research spine carries the weight. Research phase ran first as a separate session that verified every stat against primary sources, caught five issues in the original section brief (Stat 1b GLOBE respondent count off by 300, Stat 4 Vistage quote not verbatim, Stat 5 "Journal of Applied Psychology 2019 lonely CEOs" citation does not exist — replaced with Fracassi & Tate 2012 governance lens or Vistage practitioner observation, Stat 7 MIT Sloan pinned to Keil et al. 2014, Stat 8 McKinsey 36% wrong on three independent dimensions), and filled the load-bearing bridge gap (connecting signal loss to technology/transformation failure specifically, not just generic organizational communication) with the MUM/deaf effect IS research plus the 2025 Lovich & Meier perception gap. Prose draft went through V1 → V3 voice passes: V1 stripped 14 author names and 10 journal names from body text (citations demoted to parenthetical hyperlinks per Section 04 pattern), V2 cut the Hambrick & Mason upper echelons paragraph (the term didn't earn its rent — proprioceptive drift carries the same idea more viscerally) and tightened sentence length, V3 simplified the rubber hand metaphor twice (final version: "the brain can be tricked about where the body is. Stroke someone's hidden hand and a rubber hand in front of them at the same time. Within a couple of minutes they start to feel the brush on the rubber hand instead of their real one") and pulled out the agile/software vocabulary (ship/milestone/ticket/sprint → deliver/on schedule/problem/months) per Principal feedback that the tech-coded language was alienating to the ICP.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-05-22] — TIER 2 — R&D (Dignity-Required System / Section 02)
**Change:** Deployed Section 02 of the Dignity-Required System: `rd/dignity/last-50-feet.html` — a findings report on physical-digital friction at the last 50 feet of a rollout. Dark variant. Built against the seven-beat structure established by Sections 01, 03 and 04 (friction front, the findings, why existing approaches fail, three-concept diagnostic vocabulary, what this means at rollout, the close) with three expandable inline glossary terms using native `<details>` elements. New terms defined here: the last 50 feet, semantic compression, the rock in the door. Map vs. mud and the map trap appear in body text only, not as glossary cards (per handoff brief). Work-as-Imagined / Work-as-Done cited in body as Hollnagel's resilience engineering framework, not as a DRS-owned term. Research citations hyperlinked inline (12 total): Heartland Label Printers / HBS / Ericsson case (warehouse Wi-Fi defeated by metal racking), Sharma et al. 2023 in IJITM (Industry 4.0 last-mile barriers — physical infrastructure as biggest impediment), BCG 2020 Flipping the Odds (70% fall short — attribution corrected from "BCG/McKinsey" to BCG-only per research phase), Bain 2024 (88% of business transformations fail), TEKsystems 2024 State of Digital Transformation (32% complexity), Zebra Warehousing Vision Study (61% IT/tech utilization / 77% need to modernize but slow to implement), ScienceDirect ERP systematic mapping (shop-floor integration seam), PMC EHR scoping review 2024 (workflow mismatch), Hollnagel WAI/WAD via PA Patient Safety Authority, Buehler/Griffin/Ross 1994 JPSP (64% planning fallacy — replacement for unsupported "4x" multiplier per research phase), Kruger & Evans 2004 unpacking effect, Black 2024 System Dynamics Review abstraction gap, Gartner shadow IT via Auvik aggregator (provenance acknowledged per research phase). All links verified no-login. No `target="_blank"`. Hub page `rd/dignity/index.html` updated: Section 02 card activated (removed `coming` class and "Coming" status div). Site-map updated: new R&D row added, R&D pages count 12 → 13, Total HTML 91 → 92.
**Rationale:** Fourth child report under the DRS hub. Closes the friction-front quartet (Hardware, Last 50 Feet, Tactical Dignity, Growth Collapse) with the most operationally concrete section in the series. Lead is the Heartland Label Printers warehouse — physics defeating a digital plan that never walked the floor — chosen as the anchor over structural research per the handoff rule (concrete first, then back with the research). Voice calibrated per May 2026 refinements: no hyperbole, contractions mandatory, no first person, lowercase concept names, "architecture" defined inline at first use, em-dashes replaced with ellipses or sentence breaks. Research phase ran first as a separate session that verified every stat against primary sources, caught four issues in the original research map (Stat 1 attribution sloppy, Stat 4 "4x" unsupported, Stat 7 too vague, Stat 8 Gartner provenance), and added Hollnagel WAI/WAD as the published academic bridge for "semantic compression." Prose draft went through a V1 → V3 voice review pass to strip metaphor stacks (the "scanner that didn't fit the glove" / "process step compressed into a single verb" stack in the V1 lede was rebuilt for foothold-first reading) and replace one verdict line ("designed wrong" → "designed for the wrong reality") per Principal review.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-05-21] — TIER 1 — R&D (DRS Sections 1, 3, 4)
**Change:** Fixed citation link visibility on all three deployed DRS section pages (`rd/dignity/hardware-of-being-human.html`, `rd/dignity/tactical-dignity.html`, `rd/dignity/growth-collapse.html`). Bumped link color from `var(--quetzal-bright)` (`#00A896`) to literal `#00C4B4` for better contrast against `#121A28` dark background at font-weight 300. Increased underline opacity from 0.3 to 0.7. Added explicit `text-decoration-color` with hover transition to `var(--ecru)`. Standardized hover color to `var(--ecru)` across all pages (Section 4 previously used `--rosso`). Removed duplicate `.glossary-body a` rule from Section 1. Updated DRS-SECTION2-HANDOFF.md citation CSS block to match the new standard.
**Rationale:** `#00A896` at weight 300 on `#121A28` background produced insufficient contrast — links were visually indistinguishable from surrounding body copy. Underline at 30% opacity was invisible. Readers had no structural indicator that citations were clickable.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-05-21] — TIER 2 — R&D (Dignity-Required System / Section 01)
**Change:** Deployed Section 01 of the Dignity-Required System: `rd/dignity/hardware-of-being-human.html` — a findings report on cognitive bandwidth as the real constraint on technology adoption. Dark variant. Built against the 7-beat structure established by Sections 03 and 04 (friction front, the findings, why existing approaches fail, three-concept diagnostic vocabulary, what this means at rollout, the close) with three expandable inline glossary terms using native `<details>` elements. New terms defined here: mental rent, context-switching tax, cognitive redlining. Research citations hyperlinked inline (12 total): IT Revolution 2024 ($322B cognitive overload), Mark/Gonzalez/Harris CHI 2005 (23:15 recovery), HBR 2022 (1,200 toggles / 9% reorientation), APA on multitasking (40% task-switching), Altmann/Trafton/Hambrick JEP:General 2014 (4.4-second interruption → tripled errors — note: corrected from the original research map's "5 seconds"), Microsoft 2024 Work Trend Index (68% pace overwhelm / 46% burnout), Goldenberg & Oreg 2007 (Laggards in Disguise), Cronkite/ASAE 2017 (Rethinking the Change Adoption Curve), EJIS 2025 (acceptance/resistance as dynamic states), Wang et al. 2024 PMC (technostress suppresses adoption intention), Sustainability 2026 MDPI (cognitive strain blocks attitude→behavior transition), Hagger & Starr 2026 SDT meta-analysis (192 studies — note: corrected from original "2025"), Gagné et al. Nature Reviews Psychology 2022, Ouwehand/Lespiau/Tricot/Paas 2025 Education Sciences (CLT review — note: corrected from original map's "Hendrick" attribution; Hendrick wrote a blog about it, didn't author the paper). All links verified no-login. No `target="_blank"`. Hub page `rd/dignity/index.html` updated: Section 01 card activated (removed `coming` class and status label, href updated from placeholder `hardware.html` to `hardware-of-being-human.html`). Site-map updated.
**Rationale:** Third child report under the DRS hub. The foundational section: introduces biological throughput as the actual constraint on adoption, with the "laggard" label reframed as a misdiagnosis of throughput failure. Voice calibrated per May 2026 refinements: no hyperbole, contractions mandatory, no first person, lowercase concept names in body, "throughput" defined upfront, "load" instances aggressively pruned and replaced with bandwidth/capacity/ceiling/bill/pressure variants (per voice review feedback during build). Research phase ran first as a separate session that verified every stat against primary sources, caught three errors in the original research map (Stat 5 number, Stat 9 authorship, Stat 10 date), and added three bridge studies linking cognitive load specifically to technology adoption failure (filling the gap the research map had flagged).
**Operator:** Angie Bailey + Claude via Cowork

## [2026-05-21] — TIER 3 — R&D (DRS Hub Page)
**Change:** Restructured `rd/dignity/index.html` section order. Removed above-fold "Read the 9:02 AM Meeting" fable-link button (the fable remains accessible as a card in the friction fronts grid). Moved the Friction Fronts card grid to immediately follow the header/thesis. Moved the interactive 2x2 matrix widget below the friction fronts. Moved the human governance anchor (three governors) to the bottom of the page. New flow: thesis → friction fronts → matrix → governors.
**Rationale:** The previous order (thesis → matrix → governors → friction fronts) asked readers to engage with the analytical model before they'd seen the five failure patterns it maps to. The friction fronts are the hook — they're what the reader came for. The matrix and governors gain weight after the reader has context for what breaks and why.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-05-21] — TIER 1 — R&D (Section 03 — Tactical Dignity)
**Change:** Added research hyperlinks to all six inline citations on `rd/dignity/tactical-dignity.html`. Linked sources: AI & Society 2024 (Springer), 2024 Kahoot Workplace Culture Report, IMF global employment blog, Gartner 2025 press release, Deci and Ryan (selfdeterminationtheory.org), Gagné et al. 2022 (PMC open access). Added `.body-text a` link styles (quetzal bright, underline, hover to ecru). All links verified accessible without login credentials. No `target="_blank"`.
**Rationale:** Research citations existed as plain text — no way for readers to verify or follow up on the claims. Links now point to publicly accessible pages (press releases, open-access mirrors, journal abstracts).
**Operator:** Angie Bailey + Claude via Cowork

## [2026-05-21] — TIER 3 — R&D (Dignity-Required System / Section 04)
**Change:** Deployed Section 04 of the Dignity-Required System: `rd/dignity/growth-collapse.html` — a findings report on performative compliance, middle-manager shock-absorber dynamics and the architecture of unsurvivable refusal. Dark variant. Built against the 7-beat structure established by Section 03 (friction front, the findings, why existing approaches fail, six-concept diagnostic vocabulary, what this means at rollout, the close) with six expandable inline glossary terms using native `<details>` elements. New terms defined here: hufflepuff mask, survivable refusal, human shock absorber, growth collapse, efficiency squeeze, trust vs compliance. Research citations hyperlinked inline: Ipsos 2022, Detert and Edmondson 2011, Edmondson's Fearless Organization, Gallup 2024 disruptive change, Capterra 2023 middle manager burnout, McKinsey 2023 middle manager transformation admin load, Frontiers in Psychology 2025 on AI awareness and knowledge hoarding, GP Strategies and HRZone on performative AI adoption, Mauno et al. 2023 work intensification review. Shared DRS CSS components (verdict-line, glossary-grid, glossary-card, back-link-row) consumed from styles.css rather than redefined inline. Hub page `rd/dignity/index.html` updated: Section 04 card activated (removed `coming` class and status label). Site-map updated: new R&D row added, R&D pages count 11 → 12, Total HTML 90 → 91.
**Rationale:** Second child report under the DRS hub. The first three friction fronts (Hardware of Being Human, Last 50 Feet, Tactical Dignity) describe what fails. This section names how the failure stays invisible: refusal isn't safe, the dashboard fills with masks, the middle manager wears the load, the architecture mistakes compliance for adoption. Voice calibrated per the May 2026 refinements: no hyperbole, contractions mandatory, no first person, lowercase concept names in body, "architecture" defined on first use, the architecture-vs-people dichotomy refused.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-05-21] — TIER 3 — R&D (Dignity-Required System / Section 03)
**Change:** Deployed Section 03 of the Dignity-Required System: `rd/dignity/tactical-dignity.html` — a findings report on identity erasure in AI rollouts. Dark variant. Five-beat structure: friction front, the findings, why existing approaches fail, four-concept diagnostic vocabulary (identity anchor, mastery vs drudgery distinction, dignity circuit breaker, defensive knowledge hoarding), what this means at rollout, diagnostic close. Four expandable inline glossary terms using native `<details>` elements. Research citations: AI & Society 2024, Kahoot 2024, IMF, Gartner 2025, Deci and Ryan (SDT foundational), Gagné et al. Nature Reviews Psychology 2022. Working definition of "architecture" placed in the header to preempt the cognitive lift. Hub page `rd/dignity/index.html` updated: Section 03 card activated (removed `coming` class and status label) and card description softened from "committed professional erasure" to "taken away the work that made them visible" to match the report's calibrated voice. Site-map updated.
**Rationale:** First child report under the Dignity-Required System hub. Establishes the section-report template that the remaining four sections (Hardware of Being Human, Last 50 Feet, Growth Collapse, Trust/Power/Signal Loss) will inherit. Voice calibrated through a V1→V4 review pass to strip hyperbole, drop first-person framing, lowercase non-proprietary concept names, define ambiguous load-bearing terms upfront, and refuse the architecture-vs-people dichotomy that lets systems off the hook.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-05-19] — TIER 1 — SEO and meta tag infrastructure across all pages
**Change:** Created robots.txt (allow all, sitemap reference) and sitemap.xml (84 canonical URLs with priority tiers). Added og:image, canonical URL, Twitter Card, and favicon meta tags to 82 subpages that were missing them (only homepage and DRS Matrix had complete tags previously). Added JSON-LD Article structured data to 13 pages (8 case studies + 5 verdict essays). All pages now show proper preview cards when shared on LinkedIn/Slack and are correctly indexed by search engines.
**Rationale:** Site had no sitemap or robots.txt, subpages showed blank previews when shared (no og:image), no canonical tags meant UTM-tagged LinkedIn links could fragment search authority, and no structured data meant Google treated case studies as generic pages instead of portfolio content.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-05-19] — TIER 1 — Repo cleanup (legacy files, orphans, dead CSS)
**Change:** Deleted 6 files: 3 legacy duplicates under `Portfolio Work/` (MBR, GEO/AEO, Dots/Pens hub — all superseded by `posts/` or L&D hub equivalents), 3 orphaned `warehouse-card.html` pages (geo-aeo, crisis-comms, post-acquisition — not linked from any live page). Removed ~800 chars of dead CSS from `styles.css`: `.ld-divider`/`.ld-label`/`.ld-title` rules (replaced by standard `section-label` pattern) and `.principle-arrow` hover rule (no HTML element uses this class). Full `site-map.md` rewrite: all 95 canonical URLs documented with correct paths, Warehouse count corrected to 8, all 8 case study inventories added, Resources categories recounted, L&D status updated to "Coming."
**Rationale:** Maintenance audit found stale documentation, duplicate files, orphaned pages, and dead CSS accumulated across deployments. Cleaned to prevent confusion in future sessions.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-05-19] — TIER 2 — Nav standardization across all case study, R&D, and artifact pages
**Change:** Fixed nav menus on 21 HTML files across posts/, hello-world/, and drs-matrix/ directories. 11 main pages updated to correct 7-item nav (Investigation, Warehouse, R&D, L&D, Verdict, Resources, Debrief). 10 artifact leaf pages updated to correct single "Main Site" link pattern with back-link to parent case study. Issues found: some pages had 4-item navs with obsolete "Signal" link, some missing Resources, some with "The Debrief" instead of "Debrief", DRS Matrix had no standard nav, older artifact pages had non-standard nav structures.
**Rationale:** Nav menus had drifted across deployments. Case study pages linked from homepage had inconsistent, outdated navigation. Standardized to match L&D and index page patterns.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-05-19] — TIER 1/2 — Multi-page fixes (R&D, L&D, Resources, Homepage)
**Change:** R&D page: tag changed to "P&L Readiness" / meta to "R&D // Measurement Infrastructure". CSS fixes: working-def font 0.95→1.1rem, marker-name 1.15→1.4rem, triad-title 1.2→1.5rem, framework-lede paragraph spacing added, red on marker 04 removed, orphaned shift-grid CSS cleaned. Copy: "five years"→"2 years", CTA→"View the New Metrics Reference Card", back link→"Back to R&D". Reference card page: title/heading/subtitle/meta updated to "Metrics" framing, back link→"View Full R&D Page". Homepage: R&D card tag→"P&L Readiness", Em-Dash Unpacking card added to L&D section. L&D page: "Reworking"→"Coming" on Supply Closet cards, back link→"Back to business".
**Rationale:** QA pass after v3 copy deployment. Tag/H1 redundancy fixed. Font sizes were too small for readability. Em-Dash series needed homepage representation. L&D labels were inaccurate.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-05-19] — TIER 2 — R&D (Operational Telemetry)
**Change:** Full copy rewrite of rd/operational-telemetry/index.html to align with LinkedIn content series framing. Updated meta descriptions. Updated homepage R&D card (index.html Section 03) and Resources page card (resources/index.html) to match new framing.
**Rationale:** LinkedIn Ops Telemetry series reframed around "Should ops teams shift from budget thinking to P&L thinking?" The R&D page needed to match before Post 1 publishes. Register shifted from academic framework delivery to research-with-a-pulse. "Markers" reframed as "metrics." From/to shift-grid visual and drama-loop arrow list removed. Blur/laser paradox introduced as opening complication. All seven metrics kept, descriptions rewritten in plain observation voice. Accountability triad reframed as prerequisite test.
**Operator:** Angie Bailey + Claude via Cowork

---

## [2026-05-14] — TIER 2 — Operational Telemetry Web Presence (R&D + Resources)
**Change:** Deployed 4 files for the Operational Telemetry content series:
1. `rd/operational-telemetry/index.html` — New dark-variant R&D framework page. Sections: structural problem (drama loop), functional-to-system shift grid, 7 telemetry marker cards, shared causal chains, accountability triad (control/signals/symmetry), economic systems architects conclusion with CTA. 24,916 bytes.
2. `resources/operational-telemetry-markers.html` — New ecru light-variant printable reference card. 7-marker table, self-assessment scoring, accountability check grid, print button (landscape). Back-link to framework page. 16,194 bytes.
3. `index.html` — Added Operational Telemetry card to R&D section `.lab-grid` (position 3, after DRS). Tag: "Operational Economics". +606 bytes.
4. `resources/index.html` — Added Operational Telemetry Markers card to Tools category (`#tools`). Tag: "Reference Card // Printable". +647 bytes.
**Rationale:** Web presence needed to support LinkedIn content series (9 atoms, 6 planned posts). Framework page earns trust in durability of social content. Reference card is the "receipt" — printable takeaway. Post 1 can ship without the framework page; Posts 2+ and all carousels need these pages live.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-05-11] — TIER 1 — Site Registry Full Refresh
**Change:** Complete rewrite of _site-registry.md. Updated from March 2026 to May 2026. Added: Site Architecture section (5 numbered sections + Resources + Debrief), MBR case study (Warehouse position 1), GEO/AEO case study reformatted into proper table (position 2), Hello World Toolkit (3 pages + 3 artifacts), Verdict essays (5 pages), Start-Here page, Resources section (2 pages), R&D landing, L&D section. Updated Warehouse card order to reflect all 8 live positions. Added URL Summary table (~90 total live URLs).
**Rationale:** Registry had drifted since March — did not reflect MBR, GEO/AEO, Hello World toolkit, verdict essays, start-here, resources, or R&D landing deployments. Single source of truth for file inventory must stay current.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-05-11] — TIER 3 — Performance Analytics Infrastructure
**Change:** Created Google Drive folder structure for marketing analytics under 2_AREAS/Work/Performance Analytics/ (PARA methodology). Subfolders: Weekly Reports, Page Performance, Reference. Updated weekly-ga4-traffic-check scheduled task to save Google Docs to Weekly Reports folder with expanded metrics (per-page performance data). Moved legacy GA4 reference docs to Reference subfolder. Archived EquipmentShare-era analytics PDFs to 4_ARCHIVES.
**Rationale:** Scheduled weekly reports were saving to ephemeral session outputs and getting lost. Needed persistent, organized storage following PARA methodology for recurring analytics work.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-05-05] â TIER 1 â Nav Bar (All Pages)
**Change:** Added Resources nav link to all subpages (verdict essays, L&D hub, case study hubs, 404); modernized old 4-item navs to full 7-item nav. Deleted orphan file changelog2_deploy.md.
**Rationale:** Consistency â Resources link was only on index.html and resources pages after initial deploy.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-05-05] â TIER 3 â Resources (New Section + New Page)
**Change:** Created /resources/index.html (The Receipt Drawer) â standalone resources landing page with 4 categories (Prompts, Templates, Playbooks, Tools) and 15 resource cards linking to existing site content. Created /resources/digital-gratuity.html â standalone prompt stack page with 3-step system (Capture, Prompt, Send), 8 capture questions, 2-turn copyable AI prompt, and 6-step LinkedIn send instructions. Added "Resources" to nav bar on index.html between Verdict and Debrief. All pages include GA4 tag, inline base CSS for local preview, and anchor IDs for deep-linking from LinkedIn posts.
**Rationale:** Needed a single URL to point LinkedIn and presentation audiences to when referencing templates, prompts, or tools. Eliminates the "go find it on my site" friction. Digital Gratuity prompt stack was the first resource seeded from an existing LinkedIn post (activity 7449837717149884417).
**Operator:** Angie Bailey + Claude via Cowork

## [2026-05-05] â TIER 1 â R&D (Hello, World / Safety-First Gate)
**Change:** Updated Safety-First Gate interactive checklist so all six gate sections can be expanded and previewed by clicking their headers, regardless of completion state. Checkboxes remain sequentially locked (must complete prior gate to answer). Locked gates show a hint explaining why checkboxes are disabled. `toggleGate()` now functional. Removed blanket `pointer-events: none` and `opacity: 0.5` from locked gates.
**Rationale:** Users should be able to read ahead and understand all gate questions before committing answers. Preview access improves transparency without breaking the sequential integrity of the assessment.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-04-27] â TIER 3 â Start Here (New Page)
**Change:** Deployed /start-here/index.html â interactive AI context builder. Single self-contained file (62 KB). Four-card questionnaire that generates a personal AI profile users can paste into any AI tool. GA4 tag injected. All dependencies CDN or inline.
**Rationale:** Lead-gen and value-delivery tool for LinkedIn Content Engine. Gives visitors an immediate, useful artifact while introducing Angie's methodology.
**Operator:** Angie Bailey + Claude via Cowork

## [2026-04-26] â TIER 2 â Warehouse
**Change:** Added Marketing Infrastructure MBR Debt Clearance case study. 1 case study page (dark-variant), 2 branded artifact pages (Cross-Functional MBR Template, Reporting Governance Cadence), 2 blank downloadable templates, 1 companion .docx narrative. MBR Warehouse card added as first card in grid. TBA placeholder card added as last card. Warehouse card limit overridden from 8 to 10. Collapsed card padding tightened with hover transition.
**Rationale:** New case study showcasing unified reporting infrastructure build across 13 marketing functions and 10+ data platforms for a $1B+ organization. Demonstrates strategic operations and governance methodology capabilities.
**Operator:** Angie Bailey + Claude via Cowork

### 2026-04-25 â Site Architecture Overhaul + Verdict Essays + L&D Landing Page
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

### 2026-04-24 â The GEO/AEO Transition
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


### Post-Acquisition Integration Launch Ã¢ÂÂ full case study deployed
**Commit:** Series of commits via GitHub API, March 29Ã¢ÂÂ30 2026
**What:** Full case study deployed: main page, 4 branded artifact pages, 3 blank templates, and warehouse card. Warehouse card on index.html converted from placeholder to live link with forensic copy and Scope // Output metrics.

**Files added:**
- `posts/post-acquisition-integration-launch/post-acquisition-integration-launch.html` Ã¢ÂÂ Main case study page
- `posts/post-acquisition-integration-launch/warehouse-card.html` Ã¢ÂÂ Warehouse card
- `posts/post-acquisition-integration-launch/assets/vendor-governance-model.html` Ã¢ÂÂ Branded artifact
- `posts/post-acquisition-integration-launch/assets/product-taxonomy-architecture.html` Ã¢ÂÂ Branded artifact
- `posts/post-acquisition-integration-launch/assets/cross-functional-workback.html` Ã¢ÂÂ Branded artifact
- `posts/post-acquisition-integration-launch/assets/templates/system-integration-sequence-blank.html` Ã¢ÂÂ Blank template
- `posts/post-acquisition-integration-launch/assets/templates/vendor-governance-model-blank.html` Ã¢ÂÂ Blank template
- `posts/post-acquisition-integration-launch/assets/templates/product-taxonomy-architecture-blank.html` Ã¢ÂÂ Blank template

**Files modified:**
- `index.html` Ã¢ÂÂ Post-Acquisition warehouse card converted from `<div>` placeholder to live `<a>` with forensic copy, Scope // Output metrics, "Ops Management" tag

**Why:** Fifth client case study. Post-acquisition integration operations covering vendor governance, product taxonomy architecture, system integration sequencing and cross-functional workback for a multi-brand merger.

### Post-Acquisition Integration Launch Ã¢ÂÂ post-deployment refinements
**Commit:** Series of commits via GitHub API, March 30 2026
**What:** Multiple UX and cross-linking improvements across the case study and site-wide.

**Changes:**
- System Integration Sequence Map: "Break" button CTA changed to "What breaks?" for clearer intent. Button restyled Ã¢ÂÂ larger font (0.7rem to 0.85rem), ecru text on rosso-tinted background with visible border. Vertical text orientation removed (was `writing-mode: vertical-rl`).
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
- `posts/enterprise-newsletter-architecture/enterprise-newsletter-architecture.html` Ã¢ÂÂ Title, h1 accent word, OG tags
- `posts/web-experience-capacity-build/web-experience-capacity-build.html` Ã¢ÂÂ Title, h1 accent word, OG tags
- `_site-registry.md` Ã¢ÂÂ Full Crisis Comms file inventory, Newsletter section title
- `AQB Website Ã¢ÂÂ Session Handoff.md` Ã¢ÂÂ Updated card/title alignment rules

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
- `index.html` ÃÂ¢ÃÂÃÂ Two new Warehouse cards added

**Why:** Expanding the portfolio with two new case studies demonstrating internal communications and crisis response architecture work.

### Warehouse card reorder + naming updates + nesting fix
**Commit:** Series of commits via GitHub API, March 28 2026
**What:** Moved Enterprise Newsletter and Crisis Communications cards out of the R&D section into the main Warehouse grid. Retitled "Enterprise Newsletter Architecture" to "Enterprise Newsletter Launch." Retitled "Web Experience Capacity Build" to "Web Experience Capacity Expansion" across index.html. Fixed a missing `</div>` on the Workforce AI Adoption card that was causing the comms cards to nest inside it (overlap/stacking bug). Reordered cards: Multi-Team Roadmap Summit, E-Commerce P&L Build, Web Experience Capacity Expansion, Post-Acquisition Integration, Enterprise Newsletter Launch, Crisis Communications Architecture, Workforce AI Adoption (last, since it is not yet built out).

**Files modified:**
- `index.html` ÃÂ¢ÃÂÃÂ Card moves, renames, reorder, nesting fix

**Why:** The two comms case studies are complete work, not R&D. Workforce AI moved to last position since its case study page does not exist yet. The nesting bug was caused by the Workforce AI `<div class="evidence-card">` missing its closing `</div>`, which caused subsequent `<a>` cards to render inside it.

### DRS Matrix page deployed + R&D section added to Warehouse
**Commits:** `18f9e90` through `7e5a536` (series of commits, March 22 2026)
**What:** New page at `drs-matrix/index.html` combining "The 9:02 AM Meeting" mini-fable with the interactive DRS 2ÃÂÃÂÃÂÃÂ2 matrix widget. Added "R&D // Frameworks Under Construction" subsection to Warehouse on index.html with a Quetzal-tinted card linking to the new page (opens in new tab). Headshot in footer now links to LinkedIn with hover CTA.

**Files added:**
- `drs-matrix/index.html` ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ Full page: fable narrative + interactive widget + print stylesheet

**Files modified:**
- `index.html` ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ Added R&D subsection CSS (lab-divider, lab-grid, lab-card, series-status), DRS card, headshot wrapped in LinkedIn link with hover CTA, footer overflow fixes

**Key design decisions:**
- R&D section uses Quetzal-tinted card backgrounds (`rgba(0,104,94,0.12)`) and Quetzal-bright accent line on hover to visually distinguish from client case study cards (which use ecru-ghost backgrounds and rosso accent lines)
- R&D label matches `section-label` pattern (0.85rem, weight 700, letter-spacing 0.2em, Quetzal bright)
- Lab title at `clamp(1.4rem, 3vw, 2rem)` weight 900 ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ sits between section h2 and card titles in the hierarchy
- DRS page is light/ecru variant (not dark Durable Births) ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ appropriate for thought leadership content vs. client case studies
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
**What:** Restored Post-Acquisition Integration placeholder card (had been accidentally replaced). Reordered Warehouse grid to: Summit ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ P&L Build ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ Web Experience Capacity Build ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ Post-Acquisition Integration ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ Workforce AI Adoption. Renamed Summit card title from "E-Commerce Strategic Summit Cross-Functional Alignment" to "Multi-Team Roadmap Summit."
**Why:** Previous edit replaced the wrong card when adding Web Experience. Summit card title was too long and jammed ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ two lines of text in a card label is not the pattern. Card title is a fast read; case study page h1 is the full forensic record. They are allowed to differ.

---

### Web Experience Capacity Build ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ full case study launched
**Commit:** `c385711`
**What:** Added three new files:
- `posts/web-experience-capacity-build/web-experience-capacity-build.html` ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ main case study page
- `posts/web-experience-capacity-build/assets/team-capacity-diagnostic.html` ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ branded artifact page
- `posts/web-experience-capacity-build/assets/templates/team-capacity-diagnostic-blank.html` ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ blank template
Converted Warehouse card #3 from placeholder `<div>` to live `<a>`.
**Why:** New case study covering EquipmentShare web experience scrum master and team architecture work. Key framework: Role-Weighted Capacity Diagnostic ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ maps capacity ratios for mixed-discipline teams where upstream roles (POs, designers) outnumber engineering bottlenecks. Artifact credits Nick Sonnenberg (*Come Up for Air*, 2023) for bandwidth calculation methodology and Eliyahu Goldratt for Theory of Constraints. Applied diagnostic (role-weighted mapping) is original.

**Design decisions made during build:**
- Stat box max-width bumped 500px ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ 750px; padding 1.25rem ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ 1.75rem 1.5rem; min-width 100px ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ 140px (labels "Overproduction Ratio" and "What the Governance Produced" were overflowing)
- Artifact page "View Blank Template ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ" (not "Download") confirmed as standard
- Blank template "Print / Save as PDF" button (not download)
- 20 instances of sub-0.85rem mono text corrected across all three files in a dedicated fix pass
- Director departure reframed: not "survived chaos" but "system was built well enough that leadership was planning to hand it off" ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ more accurate and consistent with the "survives the exit" brand thesis
- Company never named in copy; senior engineer referred to by role only

---

### SEO round 2: Organization schema, content alignment, freshness dates
**Commit:** `1c41b61`
**What:** Added Organization schema to JSON-LD, aligned content signals, added freshness dates.
**Why:** Follow-up to initial SEO implementation. Structural improvements from an AIView audit ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ visible text and voice left untouched per brand rules. (A prior audit had recommended keyword-stuffed titles and generic descriptions; those were rejected.)

---

### Headshot easter egg improvements
**Commit:** `3c185c4` / `6ca14c6` / multiple
**What:** Angie's portrait added to footer as hover reveal. 36px circle, grayscale filter, opacity:0 default, reveals on footer hover. Mobile: opacity:0.6 always (no hover on touch).
**Why:** Low-key human signal. Not prominently displayed ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ intentional restraint.

---

### OG social sharing image
**Commit:** `2aed6f1` / `96a7f08` / `2068abb` / `cc09567`
**What:** Created og-image.png (1200ÃÂÃÂÃÂÃÂ630). Iterated: started basic, rebuilt with blueprint-grid aesthetic, rosso accent, IBM Plex Mono. Added og:image:width and og:image:height tags.
**Why:** LinkedIn requires explicit image dimensions for reliable detection. `og:image:width` and `og:image:height` are mandatory ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ do not remove. LinkedIn post inspector was used to force re-scrape after deploy.

---

### Page title simplification
**Commit:** `b202962`
**What:** `<title>`, `og:title`, `twitter:title` all set to just "Angie Bailey." `jobTitle` in JSON-LD set to "Operations Strategist."
**Why:** Angie rejected "Operations Architecture and AI Implementation" (too narrow) and "Transformation Architect" (identity-first, cognitive load). Decision: let the work speak. Visible title is name only. Job title is crawler-only.

---

### Signal ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ Debrief rename
**Commit:** `413963d`
**What:** Section 04 on index.html renamed from "The Signal" to "The Debrief." Section id changed from `#signal` to `#debrief`. All nav links and back-links across case study pages and artifact pages updated.
**Why:** "Signal" read as AI jargon. "Debrief" won from five alternatives in a live session. All cross-links updated simultaneously ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ do not re-introduce `#signal`.

---

### Template button standardization
**Commit:** `413963d` (same commit as Signal ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ Debrief)
**What:** All artifact pages updated to use "View Blank Template ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ" (not "Download"). `download` attribute removed from all template links.
**Why:** `download` attribute on HTML files caused browsers to download raw HTML source instead of rendering the page. The correct pattern is `target="_blank"` with no `download` attribute. Blank templates themselves use "Print / Save as PDF" (`onclick="window.print()"`).

---

### Yellow flag color fix
**Commit:** `234b57e`
**What:** Yellow constraint flags across all artifact pages corrected to `#D4A843`.
**Why:** Yellow flags were rendering as quetzal-bright (green) ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ the wrong color. Green flags were rendering as ecru-dim (beige) ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ also wrong. Both fixed. Yellow is hardcoded `#D4A843` because it was added after the original CSS variable set and never got a variable.

---

### E-Commerce P&L Build ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ case study launched
**Commit:** `b5c0669`
**What:** Added case study page and artifact pages for E-Commerce P&L Build.
**Why:** Second case study. Decision infrastructure framing. Covers building the first e-commerce P&L for a company that tracked revenue but not profitability by channel.

---

### Dossier ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ Brief rename
**Commit:** `06278b7`
**What:** All user-facing display text changed from "Dossier" to "Project Brief" or "Brief." File names preserved (renaming would break existing URLs).
**Why:** Angie didn't want the word "dossier" in any visible copy. File paths still say `dossier` ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ this is intentional to preserve URLs. Do not rename the files.

---

### Cross-links between artifacts
**Commit:** `06278b7` (same commit as Dossier ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ Brief)
**What:** Related Work sections added to bottom of artifact pages where methodology overlaps (P&L and Summit case studies).
**Why:** Users landing on one artifact may have arrived from the other case study's ecosystem. Cross-links increase discovery without requiring a nav overhaul.

---

### Summit artifact back-link fix
**Commit:** (part of early summit iteration commits)
**What:** Summit artifact back-links corrected from `/cases/e-commerce-summit.html` to `../e-commerce-summit.html`.
**Why:** Path was wrong ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ linked to a non-existent `/cases/` directory. Relative paths are required.

---

### Multi-Team Roadmap Summit ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ case study launched
**Commit:** Early commits (`07a6c6a`, `3c215c4`, `624c100`)
**What:** First case study added. Five artifact pages, five blank templates.
**Why:** Summit case study was the first production build of the Durable Births design system.

---

## Format for New Entries

Copy this block and fill in:

```
### {Short title of change}
**Commit:** `{hash}` (or "no commit ÃÂÃÂ¢ÃÂÃÂÃÂÃÂ edit in progress")
**What:** One paragraph description of what was changed, what files were touched.
**Why:** The reasoning. What decision was made and why. If overriding a previous decision, note what changed.
```
