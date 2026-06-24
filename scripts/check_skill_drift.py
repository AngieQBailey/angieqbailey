#!/usr/bin/env python3
"""
check_skill_drift.py — enforce repo-as-source-of-truth for skill-bundled files.

The git repo is upstream. Some Claude skills bundle copies of repo files
(templates, build references). This check fails when a bundled copy diverges
from its canonical repo source, so the two cannot silently drift.

It reads _skills/skill-pairs.json and, for each declared pair:

  exact       byte-compares the bundled copy against the canonical repo file.
              Any difference is a failure.

  conceptual  the bundled copy is intentionally not identical (it paraphrases
              or extends a repo doc). The check records the canonical's sha256
              in skill-pairs.json and fails when the canonical changes since
              that hash, flagging it for human reconciliation. It never
              rewrites anything.

Scope and limit (read this): CI verifies repo-internal consistency, i.e. the
canonical repo file against the committed copy under _skills/. It does NOT
reach the installed skill cache or the .skill packages in
"Updated Skills (Versioned)/". The intended workflow is: edit the canonical,
re-sync the _skills/ copy, rebuild the .skill from _skills/, click "Save Skill"
to install. This check guarantees the repo halves stay in lock-step and tells
you exactly what to repackage. The install click stays human and deliberate.

Usage:
  python3 scripts/check_skill_drift.py            # check, exit 1 on drift
  python3 scripts/check_skill_drift.py --list     # list pairs, no pass/fail
  python3 scripts/check_skill_drift.py --update-hashes
                                                   # re-record conceptual
                                                   # canonical hashes (ack a
                                                   # reviewed change), then exit 0

Exit codes: 0 = in sync, 1 = drift detected, 2 = configuration error.
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFEST = REPO_ROOT / "_skills" / "skill-pairs.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_manifest() -> dict:
    if not MANIFEST.exists():
        print(f"ERROR: manifest not found: {MANIFEST.relative_to(REPO_ROOT)}", file=sys.stderr)
        sys.exit(2)
    try:
        return json.loads(MANIFEST.read_text())
    except json.JSONDecodeError as e:
        print(f"ERROR: {MANIFEST.name} is not valid JSON: {e}", file=sys.stderr)
        sys.exit(2)


def main() -> int:
    ap = argparse.ArgumentParser(description="Fail on drift between skill-bundled copies and their repo sources.")
    ap.add_argument("--list", action="store_true", help="list declared pairs and exit 0")
    ap.add_argument("--update-hashes", action="store_true",
                    help="re-record conceptual canonical hashes (acknowledge a reviewed change)")
    args = ap.parse_args()

    manifest = load_manifest()
    pairs = manifest.get("pairs", [])
    if not pairs:
        print("No pairs declared in _skills/skill-pairs.json. Nothing to check.")
        return 0

    if args.list:
        for p in pairs:
            print(f"[{p['type']:10}] {p['skill']:16} {p['bundled']}  <=  {p['canonical']}")
        return 0

    failures = []   # exact-copy mismatches
    flags = []      # conceptual canonical changes
    updated = 0

    for p in pairs:
        bundled = REPO_ROOT / p["bundled"]
        canonical = REPO_ROOT / p["canonical"]

        if not canonical.exists():
            failures.append(f"{p['skill']}: canonical source missing: {p['canonical']}")
            continue
        if not bundled.exists():
            failures.append(f"{p['skill']}: bundled copy missing: {p['bundled']}")
            continue

        if p["type"] == "exact":
            if bundled.read_bytes() != canonical.read_bytes():
                failures.append(
                    f"{p['skill']}: EXACT-COPY DRIFT\n"
                    f"      bundled:   {p['bundled']}\n"
                    f"      canonical: {p['canonical']}\n"
                    f"      fix: copy the canonical over the bundled copy, then repackage the skill."
                )
        elif p["type"] == "conceptual":
            current = sha256(canonical)
            recorded = p.get("canonical_sha256")
            if args.update_hashes:
                if recorded != current:
                    p["canonical_sha256"] = current
                    updated += 1
                continue
            if recorded is None:
                failures.append(f"{p['skill']}: conceptual pair missing canonical_sha256 in manifest.")
            elif current != recorded:
                flags.append(
                    f"{p['skill']}: CONCEPTUAL SOURCE CHANGED\n"
                    f"      canonical: {p['canonical']} changed since last reconcile\n"
                    f"      recorded:  {recorded[:12]}...\n"
                    f"      current:   {current[:12]}...\n"
                    f"      bundled:   {p['bundled']}\n"
                    f"      fix: reconcile the bundled copy to the canonical (or confirm no change is needed),\n"
                    f"           then run --update-hashes to acknowledge and repackage the skill."
                )
        else:
            failures.append(f"{p['skill']}: unknown pair type '{p['type']}' (expected exact|conceptual).")

    if args.update_hashes:
        if updated:
            MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")
            print(f"Updated {updated} conceptual hash(es) in {MANIFEST.name}.")
        else:
            print("No conceptual hashes needed updating.")
        return 0

    print("=== Skill drift check ===")
    print(f"Pairs checked: {len(pairs)}")
    if not failures and not flags:
        print("RESULT: in sync. No drift.")
        return 0

    if failures:
        print(f"\nEXACT-COPY DRIFT ({len(failures)}):")
        for f in failures:
            print(f"  - {f}")
    if flags:
        print(f"\nCONCEPTUAL SOURCES CHANGED ({len(flags)}):")
        for f in flags:
            print(f"  - {f}")
    print("\nRESULT: drift detected. Re-sync the offending copies and repackage the affected skills.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
