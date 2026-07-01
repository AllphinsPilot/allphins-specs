#!/usr/bin/env python3
"""One-time migration: renumber specs into the Notion-aligned nested taxonomy.

Moves every spec from its old flat area/ID to its new nested area/ID (keeping the same
capability slug), via `git mv` so history is preserved. Then remaps the `spec_id` column
in testcase-classification.csv, removes stale index.md files, prunes emptied old dirs,
and regenerates the index tree.

Usage:
    python .github/scripts/restructure_specs.py            # perform the migration
    python .github/scripts/restructure_specs.py --dry-run  # print what would change
"""
from __future__ import annotations

import csv
import subprocess
import sys
from pathlib import Path

from _common import PREFIX_AREA, id_from_stem, prefix_from_id, slug_from_stem

SCRIPTS = Path(__file__).resolve().parent
REPO = SCRIPTS.parents[1]
SPECS = REPO / "specs"
CLASSIFICATION = REPO / "testcase-classification.csv"

# old ID -> new ID. New area is derived from the new ID's prefix via PREFIX_AREA.
OLD_TO_NEW = {
    # book/portfolios
    "BOOK-001": "PORT-001", "BOOK-002": "PORT-002", "BOOK-003": "PORT-003", "BOOK-004": "PORT-004",
    "PF-NEW-001": "PORT-005", "PF-NEW-002": "PORT-006", "PF-NEW-003": "PORT-007",
    "PF-REV-021": "PORT-008", "PF-REV-022": "PORT-009", "PF-REV-044": "PORT-010",
    "PF-REV-045": "PORT-011", "PF-REV-030": "PORT-012", "PF-REV-031": "PORT-013",
    "PF-REV-032": "PORT-014", "PF-REV-036": "PORT-015", "PF-REV-037": "PORT-016",
    "PF-REV-046": "PORT-017", "PF-REV-047": "PORT-018", "PF-REV-048": "PORT-019",
    "PF-REV-049": "PORT-020",
    # book/policies
    "PF-NEW-004": "POL-001", "PF-NEW-005": "POL-002", "PF-REV-002": "POL-003",
    "PF-REV-003": "POL-004", "PF-REV-004": "POL-005", "PF-REV-005": "POL-006",
    "PF-REV-006": "POL-007", "PF-REV-007": "POL-008", "PF-REV-008": "POL-009",
    "PF-REV-009": "POL-010", "PF-REV-010": "POL-011", "PF-REV-001": "POL-012",
    "PF-REV-034": "POL-013", "PF-REV-035": "POL-014",
    # book/risks
    "PF-REV-011": "RISK-001", "PF-REV-012": "RISK-002", "PF-REV-013": "RISK-003",
    "PF-REV-014": "RISK-004", "PF-REV-015": "RISK-005", "PF-REV-016": "RISK-006",
    "PF-REV-017": "RISK-007", "PF-REV-018": "RISK-008", "PF-REV-019": "RISK-009",
    "PF-REV-020": "RISK-010", "PF-REV-038": "RISK-011", "PF-REV-039": "RISK-012",
    "PF-REV-040": "RISK-013", "PF-REV-041": "RISK-014", "PF-REV-042": "RISK-015",
    "PF-REV-043": "RISK-016",
    # book/data-sources
    "PF-REV-023": "DS-001", "PF-REV-024": "DS-002", "PF-REV-025": "DS-003",
    "PF-REV-026": "DS-004", "PF-REV-027": "DS-005", "PF-REV-028": "DS-006",
    "BOOK-005": "DS-007", "BOOK-006": "DS-008", "BOOK-007": "DS-009",
    "BOOK-008": "DS-010", "BOOK-009": "DS-011",
    # analytics
    "PF-REV-033": "ANLY-001",
    # aggregations
    "AGG-009": "AGG-001", "AGG-010": "AGG-002", "AGG-011": "AGG-003", "AGG-012": "AGG-004",
    "AGG-023": "AGG-005", "AGG-024": "AGG-006", "PF-REV-029": "AGG-007",
    # aggregations/scenarios
    "AGG-001": "SCN-001", "AGG-002": "SCN-002", "AGG-003": "SCN-003", "AGG-004": "SCN-004",
    "AGG-005": "SCN-005", "AGG-006": "SCN-006", "AGG-007": "SCN-007", "AGG-008": "SCN-008",
    "AGG-013": "SCN-009", "AGG-014": "SCN-010", "AGG-015": "SCN-011", "AGG-016": "SCN-012",
    "AGG-017": "SCN-013", "AGG-018": "SCN-014", "AGG-019": "SCN-015", "AGG-020": "SCN-016",
    "AGG-021": "SCN-017", "AGG-022": "SCN-018",
    # user-management
    "AUTH-001": "USER-001", "AUTH-002": "USER-002", "AUTH-003": "USER-003", "AUTH-004": "USER-004",
}


def git(*args: str) -> None:
    subprocess.run(["git", "-C", str(REPO), *args], check=True)


def find_old(old_id: str) -> Path | None:
    hits = list(SPECS.rglob(f"{old_id}_*.md"))
    return hits[0] if hits else None


def remap_csv(dry: bool) -> int:
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
        new = OLD_TO_NEW.get(r.get("spec_id", ""))
        if new:
            r["spec_id"] = new
            changed += 1
    if changed and not dry:
        with CLASSIFICATION.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(rows)
    return changed


def main() -> int:
    dry = "--dry-run" in sys.argv[1:]

    # Verify the mapping is well-formed before touching anything.
    news = list(OLD_TO_NEW.values())
    if len(set(news)) != len(news):
        dupes = sorted({n for n in news if news.count(n) > 1})
        print(f"error: duplicate new IDs: {dupes}", file=sys.stderr)
        return 1
    for new_id in news:
        if prefix_from_id(new_id) not in PREFIX_AREA:
            print(f"error: new ID {new_id} has no area in the registry", file=sys.stderr)
            return 1

    moved = 0
    problems: list[str] = []
    for old_id, new_id in OLD_TO_NEW.items():
        src = find_old(old_id)
        if src is None:
            problems.append(f"{old_id}: source file not found")
            continue
        slug = slug_from_stem(src.stem)
        dst = SPECS / PREFIX_AREA[prefix_from_id(new_id)] / f"{new_id}_{slug}.md"
        if dst.exists():
            problems.append(f"{new_id}: destination already exists ({dst.relative_to(REPO)})")
            continue
        print(("would move " if dry else "moving ") +
              f"{src.relative_to(SPECS)} -> {dst.relative_to(SPECS)}")
        if not dry:
            dst.parent.mkdir(parents=True, exist_ok=True)
            git("mv", str(src), str(dst))
        moved += 1

    # Specs left behind that the map didn't cover?
    for md in sorted(SPECS.rglob("*.md")):
        if md.name == "index.md":
            continue
        if id_from_stem(md.stem) not in OLD_TO_NEW and id_from_stem(md.stem) not in OLD_TO_NEW.values():
            problems.append(f"{md.relative_to(SPECS)}: not covered by the mapping")

    csv_changed = remap_csv(dry)
    print(f"\nmoved={moved} csv_rows_remapped={csv_changed}"
          f"{' (dry-run)' if dry else ''}")
    if problems:
        print("PROBLEMS:", file=sys.stderr)
        for p in problems:
            print("  -", p, file=sys.stderr)
        return 1

    if not dry:
        # Drop stale index.md files, prune emptied old dirs, regenerate the tree.
        for idx in list(SPECS.rglob("index.md")):
            git("rm", "-q", "--", str(idx))
        for d in sorted((p for p in SPECS.rglob("*") if p.is_dir()), reverse=True):
            if not any(d.iterdir()):
                d.rmdir()
        subprocess.run([sys.executable, str(SCRIPTS / "generate_indexes.py")], check=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
