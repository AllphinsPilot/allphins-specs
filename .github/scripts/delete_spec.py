#!/usr/bin/env python3
"""Delete a spec by ID, then regenerate the indexes.

Resolves the file from the ID prefix via the AREA_PREFIX registry
(`RISK-002` -> `specs/book/risks/RISK-002_*.md`) and removes it. Empty area folders
(and their now-stale index.md) are cleaned up, walking up the tree. Then runs
generate_indexes.py so the index.md files stay in sync.

Usage:
    python .github/scripts/delete_spec.py USER-003
    python .github/scripts/delete_spec.py            # prompts for the ID

Any rows in testcase-classification.csv that pointed at the deleted spec are
reconciled back to `deferred` (spec_id cleared, reason updated).
"""
from __future__ import annotations

import csv
import re
import subprocess
import sys
from pathlib import Path

from _common import PREFIX_AREA, prefix_from_id

SCRIPTS = Path(__file__).resolve().parent
REPO = SCRIPTS.parents[1]
SPECS = REPO / "specs"
CLASSIFICATION = REPO / "testcase-classification.csv"


def regenerate_indexes() -> None:
    subprocess.run([sys.executable, str(SCRIPTS / "generate_indexes.py")], check=True)


def reconcile_classification(spec_id: str) -> int:
    """Flip any classification rows pointing at spec_id back to deferred."""
    if not CLASSIFICATION.exists():
        return 0
    with CLASSIFICATION.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames or []
        rows = list(reader)
    if "spec_id" not in fields:
        return 0
    changed = 0
    for r in rows:
        if r.get("spec_id") == spec_id:
            r["spec_id"] = ""
            if "disposition" in r:
                r["disposition"] = "deferred"
            if "reason" in r:
                r["reason"] = f"Spec {spec_id} deleted; needs reclassification"
            changed += 1
    if changed:
        with CLASSIFICATION.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)
    return changed


def prune_empty(area_dir: Path) -> None:
    """Remove empty area dirs (and stale index.md) upward, stopping at specs/."""
    d = area_dir
    while d != SPECS and d.is_dir():
        specs = [m for m in d.glob("*.md") if m.name != "index.md"]
        subdirs = [k for k in d.iterdir() if k.is_dir()]
        if specs or subdirs:
            break
        idx = d / "index.md"
        if idx.exists():
            idx.unlink()
        parent = d.parent
        try:
            d.rmdir()
            print(f"removed empty area {d.relative_to(REPO)}/")
        except OSError:
            break
        d = parent


def main() -> int:
    arg = sys.argv[1] if len(sys.argv) > 1 else input("Spec ID (e.g. USER-003): ").strip()
    spec_id = arg.strip().upper()

    if not re.fullmatch(r"[A-Z0-9]+-\d{3}", spec_id):
        print(f"error: {spec_id!r} is not a valid spec ID (e.g. USER-003)", file=sys.stderr)
        return 1

    area = PREFIX_AREA.get(prefix_from_id(spec_id))
    if area is None:
        print(f"error: unknown ID prefix {prefix_from_id(spec_id)!r}", file=sys.stderr)
        return 1

    area_dir = SPECS / area
    matches = sorted(area_dir.glob(f"{spec_id}_*.md")) + [
        p for p in [area_dir / f"{spec_id}.md"] if p.exists()
    ]
    if not matches:
        print(f"error: no spec file for {spec_id} under specs/{area}/", file=sys.stderr)
        return 1
    if len(matches) > 1:
        print(f"error: {spec_id} is ambiguous ({', '.join(m.name for m in matches)})", file=sys.stderr)
        return 1

    path = matches[0]
    path.unlink()
    print(f"deleted {path.relative_to(REPO)}")

    reconciled = reconcile_classification(spec_id)
    if reconciled:
        print(f"reconciled {reconciled} classification row(s) back to deferred")

    prune_empty(area_dir)
    regenerate_indexes()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
