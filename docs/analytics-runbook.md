# Analytics & Search Infrastructure Runbook

**Site:** angieqbailey.com **Last updated:** 2026-06-18 **Owner:** Angie Bailey

This is the as-built record, the break-fix guide, and the new-site setup playbook for the analytics and search stack (GA4, Google Search Console, Bing Webmaster Tools, the weekly report, and the on-site tracking code). If something breaks, or you need to set the same stack up for a different site, everything is here. No prior context required.

Secrets are NOT in this file. The GitHub deploy token lives in Claude memory only. This doc is safe to keep in the repo.

**Keep this current:** any change to GA4, Search Console, Bing, the on-site event tracking, custom dimensions / key events, or the /go/ short-link system must update this file in the same task. If the stack changes and this file doesn't, this file is wrong.

---

## 1. As-built inventory (what currently exists)

**Hosting**
- Site: `angieqbailey.com`, served by GitHub Pages from repo `AngieQBailey/angieqbailey`, custom apex domain. GitHub Pages force-redirects http→https and www→apex, so `https://angieqbailey.com/` is the one canonical URL.
- Deploys happen via the GitHub Contents API (a deploy token in Claude memory), not local git. Always pull the live file before editing. The local Desktop folder is a working copy and can be stale.

**GA4**
- Measurement ID: `G-S0MXDDKP4E` (present in the `<head>` of every page; also auto-injected by `.github/workflows/ga4-inject.yml` if missing).
- Account ID `a389376845`, Property ID `p530624731`.
- Enhanced Measurement: ON. Data retention: **14 months** (event + user).
- Custom dimensions (event-scoped): **Template Path** → param `template_path`; **Short Link Slug** → param `slug`.
- Custom events: `template_download` (Print/Save buttons), `short_link_click` (/go/ stubs), `contact_click` (Debrief email link). Plus GA4 defaults (page_view, scroll, click, file_download, etc.).
- Key events: `purchase` (default, unused), `short_link_click` (live). `template_download` and `contact_click` are pending the star (they only appear in Admin > Events after firing + processing; the scheduled task `ga4-star-template-download-keyevent` stars them once available).

**Google Search Console**
- Property: URL-prefix `https://angieqbailey.com/`. Ownership auto-verified via the **Google Analytics** method (relies on the GA4 tag being present and you owning the GA property).
- Linked to GA4 (Admin > Product links > Search Console links → the Production web stream).
- Sitemap `https://angieqbailey.com/sitemap.xml` submitted (93 URLs). Email notifications: ON (all emails enabled).

**Bing Webmaster Tools**
- Property `angieqbailey.com` imported from Google Search Console (auto-verified, inherits GSC ownership). Signed in with Angie's Google account.
- Sitemap crawled, Status = Success, 93 URLs. "AI Performance (BETA)" section is relevant to GEO/AEO work.

**Reporting**
- Scheduled task `weekly-ga4-traffic-check` runs Sundays ~12:35 AM, writes one Google Doc to Drive `Performance Analytics / Weekly Reports` (folder ID `1jXFewzQd1UN0MvxglshLohQclj4h3KSD`), titled `GA4-LinkedIn-Weekly_YYYY-MM-DD_to_YYYY-MM-DD`. Covers Website (GA4 + Search Console section A7), LinkedIn, and Cross-Platform.

**On-site tracking code**
- `template_download`: inline on each Print/Save button — `onclick="if(window.gtag){gtag('event','template_download',{template_path:location.pathname});} window.print();"` (interactive pages fire it inside their print handler).
- `short_link_click`: emitted by the `/go/` stub template generated from `_links.json` via `scripts/build_links.py` (param `slug`, beacon transport). Live slugs as of 2026-06-18: `drs-maverick`, `drs-detective`, `drs-operator` (all → /rd/dignity/diagnostic-model.html, separated by utm_campaign + slug). `_links.json` is the authoritative registry; this list is a convenience snapshot.
- `contact_click`: inline on the Debrief mailto link in `index.html` (param `method:'email'`).

---

## 2. How ownership/verification actually works (so you can re-establish it)

The GA4 tag (`G-S0MXDDKP4E`) is the linchpin. Search Console ownership rides on it (Google Analytics verification method), and Bing rides on Search Console. **Do not remove or replace the GA4 tag** — doing so can silently de-verify Search Console.

Backup verification (do this once so you're not single-threaded on the GA tag): in Search Console → Settings → Ownership verification, add a second method:
- **HTML tag** — add the provided `<meta name="google-site-verification" content="...">` to the `<head>` of `index.html` and deploy. (Survives even if the GA tag changes.)
- **DNS TXT** — add the TXT record at the domain registrar. (Requires registrar access.)

---

## 3. Break-fix playbook (symptom → cause → fix)

- **GA4 shows no data / traffic lands in "(Other)" channel.** Tag missing on a page, or `utm_medium` is wrong. Fix: confirm `G-S0MXDDKP4E` is in the page `<head>`; confirm post links use `utm_medium=organic_social` (never `organic`). Check GA4 Realtime to confirm hits arrive.
- **A custom event isn't counting (e.g. template_download).** The button's onclick lost the gtag call, or the event hasn't fired yet. Fix: view-source the page, confirm the guarded gtag line is on the button; click it and watch GA4 Realtime → Event count.
- **Custom event won't appear to be marked a Key Event.** GA4 only lists events in Admin > Events after they've fired AND been processed (lags Realtime up to ~24h). Fix: wait, then star it in Admin > Events > Recent events.
- **Data retention reverted to 2 months.** Fix: Admin > Data collection and modification > Data retention → set Event data to 14 months → Save. (Not retroactive.)
- **Search Console sitemap "Couldn't fetch."** Usually transient right after submitting (Last read blank). Real failure only if the sitemap doesn't return HTTP 200 + valid XML, or robots.txt blocks it. Fix: confirm `curl -I https://[domain]/sitemap.xml` is 200, valid XML, and `robots.txt` has a `Sitemap:` line; then resubmit in Sitemaps.
- **Search Console ownership lost.** Fix: Settings > Ownership verification → re-verify via Google Analytics (needs the GA tag) or the HTML-tag backup from section 2.
- **GA4 ↔ Search Console link missing / SC reports empty in GA4.** Fix: Admin > Product links > Search Console links → Link → pick the property + web stream. Note: SC data is forward-only from verification + a 2-3 day processing delay, so it's sparse for ~2 weeks regardless.
- **Bing sitemap error or stale.** Fix: Bing Webmaster Tools > Sitemaps > Submit sitemap → `https://[domain]/sitemap.xml`.
- **Weekly report shows empty Search Console section.** Expected while SC data is still populating; the task writes a "populating" line by design. No action.
- **Weekly report didn't run.** Scheduled tasks only run while the Claude app is open; if closed at the scheduled time it runs on next launch. Confirm in the Scheduled panel that it's enabled.

---

## 4. New-site setup playbook (onboarding a brand-new URL)

Use this to stand up the full stack for any new site. Order matters. Anything marked **[human]** requires account creation, sign-in, an OAuth grant, terms acceptance, or DNS — Claude cannot do those and will hand them to you.

**A. GA4**
1. Create a GA4 property (or a new data stream in an existing property). Note the new measurement ID (`G-XXXXXXXX`).
2. Put the gtag snippet in the `<head>` of every page. (For a GitHub Pages site, mirror the `ga4-inject.yml` action so new pages can't ship untagged.)
3. Admin > Data retention → set Event data to **14 months**.
4. Register the custom dimensions you'll use: e.g. Template Path → `template_path`, Short Link Slug → `slug` (Admin > Custom definitions). Only needed if the site uses those events.
5. Instrument events the site actually has (templates with Print/Save → `template_download`; short links → `short_link_click`; contact link → `contact_click`). Reuse the exact snippets from section 1.

**B. Google Search Console** **[human for sign-in/consent]**
6. Add a property. Prefer **URL-prefix** (`https://[domain]/`) — it supports Google Analytics verification with no DNS. Use **Domain** only if you have registrar/DNS access and want subdomain coverage.
7. Verify ownership. Easiest: Google Analytics method (works once the GA tag is live and you own the GA property). Add an HTML-tag backup (section 2).
8. Submit the sitemap (`/sitemap.xml`). Confirm robots.txt references it.
9. Settings → confirm email notifications are on.

**C. Link GA4 ↔ Search Console**
10. GA4 Admin > Product links > Search Console links > Link → choose the SC property → choose the web stream → Submit. (The SC property may take a few minutes to appear in GA4's picker after verification.)

**D. Bing Webmaster Tools** **[human for sign-in/consent]**
11. bing.com/webmasters → sign in (Google account is fine) → **Import from Google Search Console** (auto-verifies, no DNS/file). Select the site → Import. Confirm the sitemap shows Status = Success.

**E. Reporting + key events**
12. Mark the real conversions as Key Events in GA4 (Admin > Events, star them once they've fired).
13. If you want a weekly report, clone the `weekly-ga4-traffic-check` task and swap the property ID, stream name, and Drive folder for the new site.

**Pre-flight checklist for the new site's repo:** `sitemap.xml` exists and is valid; `robots.txt` exists and has a `Sitemap:` line; GA4 tag on every page.

---

## 5. Quick reference (deep links — swap in the new site's IDs)

- GA4 Admin: `analytics.google.com` → gear (bottom-left). Deep links to admin sub-pages often bounce to Home; navigate via the gear.
- Search Console: `search.google.com/search-console`
- Bing Webmaster Tools: `bing.com/webmasters`
- This site's GA4: account `a389376845`, property `p530624731`, measurement ID `G-S0MXDDKP4E`.
- Drive Weekly Reports folder ID: `1jXFewzQd1UN0MvxglshLohQclj4h3KSD`.
- Related Claude memory: `reference_performance_analytics.md` (full infra), `project_go_short_links.md` (/go/ system), `feedback_utm_convention.md` (UTM rules), `reference_github_pat.md` (deploy token — secret).

---

## 6. What always needs a human (Claude cannot do these)

Creating accounts; signing in / entering passwords; granting OAuth/SSO permissions; accepting terms of service; changing DNS records; modifying access controls or permissions. Claude can drive everything up to these points and resume right after you complete them.
