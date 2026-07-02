#!/usr/bin/env python3
"""Show the source testcase(s) a spec was derived from.

Reads `testcase-classification.csv` (the system of record that maps every source
testcase to the spec it became) and prints, for each given spec ID, the matching
source rows with their steps and comments.

Usage:
    python .github/scripts/trace.py PORT-017
    python .github/scripts/trace.py DS-011 DS-010          # several at once

Exit code is 1 if any given ID matched no spec file.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

from _common import id_from_stem

REPO = Path(__file__).resolve().parents[2]
SPECS = REPO / "specs"
CSV = REPO / "testcase-classification.csv"

FIELDS = ("section", "topic_page", "functionality")


def spec_path(spec_id: str) -> Path | None:
    # File is `<area>/<ID>_<slug>.md` at any depth; also accept a legacy bare `<ID>.md`.
    hits = list(SPECS.rglob(f"{spec_id}_*.md")) + list(SPECS.rglob(f"{spec_id}.md"))
    return hits[0] if hits else None


def indent(text: str, pad: str = "    ") -> str:
    return "\n".join(pad + line for line in text.splitlines())


def main(argv: list[str]) -> int:
    if not argv:
        print("usage: trace.py <SPEC-ID> [SPEC-ID ...]", file=sys.stderr)
        return 2

    rows = list(csv.DictReader(CSV.open(encoding="utf-8")))
    by_spec: dict[str, list[dict]] = {}
    for r in rows:
        if r["spec_id"]:
            by_spec.setdefault(r["spec_id"], []).append(r)

    missing = 0
    for arg in argv:
        # Accept a bare ID, a full stem, or a filename; reduce to the ID.
        spec_id = id_from_stem(Path(arg).stem if arg.endswith(".md") else arg)
        path = spec_path(spec_id)
        loc = path.relative_to(REPO) if path else "(no spec file found)"
        if not path:
            missing += 1
        print("=" * 78)
        print(f"{spec_id} — {loc}")

        matches = by_spec.get(spec_id, [])
        if not matches:
            print("  No source testcase recorded (derived beyond the source set).")
            continue

        print(f"  Derived from {len(matches)} source testcase(s):")
        for r in matches:
            title = " / ".join(r[f] for f in FIELDS if r.get(f))
            print()
            print(f"  [src {r['src']}] {title}")
            meta = [f"oracle={r['oracle']}"]
            for k in ("type", "classes", "endpoint"):
                if r.get(k):
                    meta.append(f"{k}={r[k]}")
            print("    " + "   ".join(meta))
            if r.get("how_to_do_it"):
                print("    steps:")
                print(indent(r["how_to_do_it"], "      "))
            if r.get("comments"):
                print(f"    comments: {r['comments']}")

    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
