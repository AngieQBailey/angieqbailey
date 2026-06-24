#!/usr/bin/env python3
"""
build_links.py — generate /go/[slug]/index.html short-link redirect stubs.

Source of truth: _links.json (repo root).
Run from repo root:  python3 scripts/build_links.py

Each stub fires a GA4 'short_link_click' event (slug as parameter) using a
beacon transport, then redirects. A 250ms timeout and a <meta refresh> fallback
guarantee the visitor lands even if the beacon is slow or JS is disabled.
Stubs are noindex so short links never compete with real pages in search.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "_links.json"
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

STUB = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="robots" content="noindex,nofollow">
    <meta http-equiv="refresh" content="2;url={dest}">
    <link rel="canonical" href="{dest}">
    <title>Redirecting...</title>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={ga4}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', '{ga4}');
    </script>
</head>
<body>
    <p>Sending you along... <a href="{dest}">continue</a> if this does not redirect.</p>
    <script>
      (function(){{
        var dest = "{dest}";
        var done = false;
        function go(){{ if (done) return; done = true; window.location.replace(dest); }}
        gtag('event', 'short_link_click', {{
          'slug': '{slug}',
          'transport_type': 'beacon',
          'event_callback': go
        }});
        setTimeout(go, 250);
      }})();
    </script>
</body>
</html>
"""


def main():
    data = json.loads(REGISTRY.read_text())
    prefix = data.get("prefix", "go")
    ga4 = data.get("ga4_id", "")
    links = data.get("links", [])

    out_root = ROOT / prefix
    seen = {}
    written = []
    errors = []

    for entry in links:
        slug = entry.get("slug", "").strip()
        dest = entry.get("destination", "").strip()
        rel = entry.get("path", "").strip()
        if not SLUG_RE.match(slug):
            errors.append(f"invalid slug (must be lowercase kebab-case): {slug!r}")
            continue
        if not dest.startswith(("http://", "https://", "/")):
            errors.append(f"{slug}: destination must be an absolute URL or root path")
            continue
        if slug in seen:
            errors.append(f"duplicate slug: {slug!r}")
            continue
        if rel and not re.match(r"^[a-z0-9]+(?:-[a-z0-9]+)*(?:/[a-z0-9]+(?:-[a-z0-9]+)*)*$", rel):
            errors.append(f"{slug}: invalid path override: {rel!r}")
            continue
        seen[slug] = dest

        target = (ROOT / rel / "index.html") if rel else (out_root / slug / "index.html")
        # Flag a slug that already points somewhere different.
        if target.exists():
            current = target.read_text()
            if dest not in current:
                print(f"  ! {slug}: destination changed, overwriting")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(STUB.format(dest=dest, ga4=ga4, slug=slug))
        written.append(slug)

    for w in written:
        print(f"  + /{prefix}/{w}/ -> {seen[w]}")
    if errors:
        print("\nERRORS:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    print(f"\n{len(written)} stub(s) written under /{prefix}/")


if __name__ == "__main__":
    main()
