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
