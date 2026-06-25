# _skills/ — version-controlled skill sources

The git repo is the durable source of truth. Some Claude skills bundle copies of
repo files (templates, build references). Those copies are **derived artifacts**,
not hand-maintained duplicates. This directory holds the version-controlled
source-of-record for the skills that bundle repo content, so a drift check can
guarantee the copies never silently diverge from their sources.

This directory is excluded from the published site: GitHub Pages runs Jekyll,
which does not copy `_`-prefixed paths into the built site (same as `_templates/`
and `_design-system.md`). Nothing here is reachable over HTTP.

## What's tracked

```
_skills/
  skill-pairs.json                         the pair manifest the check reads
  aqb-ld-article/
    SKILL.md                               source-of-record SKILL.md
    assets/ld-article-template.html        derived copy of _templates/ld-article-template.html
    references/conventions.md              derived copy of _templates/LD-ARTICLE-CONVENTIONS.md
  aqb-case-study/
    SKILL.md                               source-of-record SKILL.md
    references/design-system.md            conceptual copy, tracked against _design-system.md
```

Only the skills that bundle repo content live here today. Others can be added the
same way when they start bundling repo files.

## The two pair types

- **exact** — byte-identical to a repo file. The check byte-compares them and
  fails on any difference. Edit the canonical repo file, then re-sync the copy here.
- **conceptual** — intentionally not identical (the skill copy is richer or
  paraphrased). The check records the canonical's sha256 and flags when the
  canonical changes, so a human reconciles. It never rewrites the copy.

  The one conceptual pair today (aqb-case-study `design-system.md` vs repo
  `_design-system.md`) is settled detect-only by decision: the repo file is the
  portable token spec and the skill file is the full case-study build manual.
  They share tokens, not purpose, so they are kept distinct. The repo spec
  (ultimately `styles.css` `:root`) is canonical for the tokens. Do not merge or
  overwrite either doc; when the repo spec's tokens change, re-check the build
  manual by hand, then run `--update-hashes`.

## How to keep things in sync

When you edit a canonical repo source (e.g. `_templates/ld-article-template.html`
or `_design-system.md`):

1. Copy the change into the matching file under `_skills/`.
   - For a **conceptual** pair, reconcile by judgment, then run
     `python3 scripts/check_skill_drift.py --update-hashes` to acknowledge.
2. Run the check locally: `python3 scripts/check_skill_drift.py` (expect "in sync").
3. Rebuild the `.skill` package from the `_skills/` source and save it to
   `Updated Skills (Versioned)/`, then install it with "Save Skill".

## The honest limit

CI verifies **repo-internal consistency**: the canonical repo file against the
committed copy under `_skills/`. It does **not** reach the installed skill cache
or the `.skill` zips in `Updated Skills (Versioned)/` (those live outside the
repo, on disk). So the build can't reach in and install for you. What it can do,
and does, is make it impossible to silently ship a `_skills/` copy that no longer
matches its source: the check turns red and names the file. Building the `.skill`
from `_skills/` and clicking "Save Skill" stays a deliberate human step.
