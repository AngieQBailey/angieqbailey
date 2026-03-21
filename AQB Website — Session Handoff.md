# AQB Website — Session Handoff
**Last updated:** March 2026

This is the briefing for any new Cowork session working on angieqbailey.com. It covers deployment mechanics, working rules, and contextual knowledge that took multiple sessions to accumulate.

For design rules and CSS values: read `_design-system.md`
For file inventory and Warehouse card status: read `_site-registry.md`
For history of what changed and why: read `_changelog.md`

---

## Required Skills

These three skills must be installed. Read them before touching any code.

- **angie-bailey-brand** — Full visual identity, voice modes (AS Angie vs. FOR Clients), banned words, punctuation rules, messaging framework. Start here.
- **aqb-case-study** — Complete deliverable chain: case study pages, artifact pages, blank templates, Warehouse cards. Includes the Durable Births design system and a 13-point quality checklist.
- **angie-social-voice** — LinkedIn voice, Tequila Test methodology, iteration protocol. Used when case study content gets repurposed for social.

The skills contain their own reference files. Read them. Don't skip.

---

## Repository & Deployment

**GitHub repo:** `AngieQBailey/angieqbailey`
**Branch:** `main` (single branch)
**Hosting:** GitHub Pages → `angieqbailey.com`
**Deploy method:** `git push origin main` — Pages rebuilds automatically within 1-2 minutes

**Authentication:** Angie generates a fine-grained GitHub PAT (Contents: Read and Write on `angieqbailey` repo). Paste into remote URL:
```
git remote set-url origin https://x-access-token:{PAT}@github.com/AngieQBailey/angieqbailey.git
```
Tokens expire between sessions. Ask Angie for a fresh one before pushing.

**Git config (per repo, not global):**
```
git config user.email "angiebaileycomo@gmail.com"
git config user.name "Angie Bailey"
```

**Always pull before committing.** Angie sometimes edits files directly on GitHub between sessions:
```
git pull --rebase origin main
```

---

## What a New Session Needs to Do First

1. Clone the repo: `git clone https://x-access-token:{PAT}@github.com/AngieQBailey/angieqbailey.git`
2. Read the installed skills (angie-bailey-brand, aqb-case-study, angie-social-voice) including their reference files
3. Read this handoff document
4. Read `_site-registry.md` — current file inventory and Warehouse card status
5. Read `_design-system.md` — CSS variables, typography rules, component patterns
6. Ask Angie for a fresh GitHub PAT if pushing is needed

---

## Anonymization Rules

All live case studies are from EquipmentShare. The case study pages don't name the company.

- **Personal names → role/function titles.** No exceptions.
- **System and platform names are kept.** Shopify, Looker, eBay, Amazon, Webflow, Figma, etc. They add credibility.
- **Department and team names are kept.** E-Commerce, Finance, Marketing, Supply Chain, etc.
- **Quantitative data is preserved.** Dollar amounts, percentages, timelines, stakeholder counts. The numbers are the proof.

---

## Source Material Patterns

Angie stores engagement artifacts in Google Drive and in the `Claude Co-Work/Rental Experience/` folder on her Desktop.

1. Search Drive for a folder named after the engagement
2. Check Desktop `Claude Co-Work/` subfolders for pre-organized material
3. Look for: SMART goal trackers, project dossiers, meeting transcripts, self-reviews, follow-up items, announcements, performance review excerpts
4. **SMART goal trackers may show items as "In Progress" even when completed.** Angie doesn't always update the tracker after delivery. Cross-reference with launch announcements or mid-year reviews to confirm status.

---

## Artifact Philosophy

Not every engagement produces artifacts worth their own standalone page. Before building artifact pages, ask:

1. **Is this unique IP?** Sprint templates and retro agendas are not. The diagnostic logic behind why a specific governance model was needed — is.
2. **Is it reusable?** If someone else could apply this to their own team or org, it earns a blank template. If it's specific to one engagement, it's supporting narrative, not a standalone artifact.
3. **Credit your influences.** If the framework builds on existing methodology (Sonnenberg, Goldratt, Trust Insights 5Ps, etc.), attribute it explicitly. More credible than claiming everything is original.

---

## Narrative Arc Preference

Angie wants case studies to show the full arc: mess to delivery. Not just the clean "after" shot.

- The messy middle is LinkedIn-content gold — recognition moment for target connections ("I've lived this problem too")
- Showing diagnostic honesty (what was actually broken) differentiates from portfolios that only show polished outcomes
- The forensic tone requires showing what was found, not just what was fixed

The Pressure Points / Diagnostic section exists specifically for this. Don't skip it or soften it.

---

## Positioning Notes

**"Transformation Architect"** is identity-first language that increases cognitive load. As of March 2026, it is de-emphasized in favor of intervention-first framing ("I find where the process broke before the people get blamed for it"). Do not add it to visible site copy.

**"Operational OS Builder"** is still valid. "OS" is structural (it runs without you). "Builder" is a verb-person.

---

## Things That Have Bitten Us

- **Only touch what's in scope.** Do not edit existing Warehouse cards, artifact pages or case study copy unless Angie has explicitly requested it in the current session. If building a new case study, that does not grant license to touch the other three.
- **Warehouse card titles ≠ case study page h1s.** The card is the fast read. The page h1 is the forensic record. They can differ. Do not normalize them.
- **Mono font size floor is 0.85rem everywhere.** Agents frequently set section labels, table headers and footer text to 0.6–0.75rem. Grep for `font-size: 0\.[67]` before pushing any new file.
- **Yellow flag color isn't a CSS variable.** Use `#D4A843` directly. Not quetzal, not quetzal-bright.
- **Card backgrounds: 0.14 opacity, not 0.08.** `rgba(245, 245, 220, 0.14)` — not `var(--ecru-ghost)` which is 0.08 and too faint.
- **PAT expiration.** Tokens from prior sessions will be expired. Test a push before doing extensive work that depends on deployment.
- **Remote edits.** Always pull before committing.
- **Read-only skill files.** Skills in `/mnt/.skills/skills/` are read-only. To edit: copy directory to `/tmp/`, `chmod -R u+w`, edit, package with `python -m scripts.package_skill /tmp/{skill-name} /path/to/output`.
- **Dossier file names vs. display names.** File paths say `dossier` (preserving URLs). All user-facing text says "Brief" or "Project Brief." Do not rename the files.
- **Summit artifact back-links.** Use relative paths (`../e-commerce-summit.html`) not absolute URLs.
- **WebFetch blocked for angieqbailey.com.** Verify changes by reading source files, not by fetching the live URL.
- **LinkedIn OG caching.** Use [LinkedIn Post Inspector](https://www.linkedin.com/post-inspector/) to force re-scrape after OG changes. `og:image:width` and `og:image:height` tags are required — do not remove.
- **package_skill.py syntax.** Correct: `python -m scripts.package_skill {skill-dir} {output-dir}` — output directory is a positional argument, not a flag.
- **TodoWrite schema.** The `todos` parameter requires objects with `content`, `status` and `activeForm` fields.
