#!/usr/bin/env python3
"""Scaffold a new spec with the correct format, then regenerate the indexes.

Computes the next free ID for the area, writes a templated spec file, and runs
generate_indexes.py so the index.md files stay in sync.

Usage:
    python .github/scripts/new_spec.py --area auth --title "A user can sign out"
    python .github/scripts/new_spec.py            # prompts for area and title

Optional: --oracle {intentional,characterization,exploratory} (default intentional)
          --priority {high,medium,low}                          (default medium)

A spec holds exactly one `## Scenario:` (parameterise with an `### Examples` table if
needed). For a behaviour that needs several scenarios, make each scenario its own spec in
the same area (run this once per scenario with the same `--area`).

Prints the path of the created spec on success.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
REPO = SCRIPTS.parents[1]
SPECS = REPO / "specs"

ORACLES = ("intentional", "characterization", "exploratory")
PRIORITIES = ("high", "medium", "low")


def yaml_scalar(s: str) -> str:
    """Emit a YAML-safe scalar, single-quoting only when necessary."""
    if s == "" or s != s.strip() or re.search(r"[:#]", s) or s[0] in "\"'>|@`&*!%{}[],?-":
        return "'" + s.replace("'", "''") + "'"
    return s


def next_id(area: str) -> str:
    prefix = area.upper()
    area_dir = SPECS / area
    highest = 0
    if area_dir.exists():
        for md in area_dir.glob("*.md"):
            if md.name == "index.md":
                continue
            m = re.match(rf"^{re.escape(prefix)}-(\d+)$", md.stem)
            if m:
                highest = max(highest, int(m.group(1)))
    return f"{prefix}-{highest + 1:03d}"


def template(title: str, oracle: str, priority: str) -> str:
    return f"""---
title: {yaml_scalar(title)}

mode: manual
oracle: {oracle}
status: draft
priority: {priority}

tags: []
source: ""
refs: []

---

## Objective
<What this behaviour proves and why it matters.>

## Preconditions
- <State required before the scenario runs.>

## Scenario: <name>
```gherkin
Given <a starting state>
When <an action occurs>
Then <the expected result>
```

## References
- Source manual case in Notion (see `source`).
"""


def regenerate_indexes() -> None:
    subprocess.run([sys.executable, str(SCRIPTS / "generate_indexes.py")], check=True)


def main() -> int:
    p = argparse.ArgumentParser(description="Create a new spec and regenerate indexes.")
    p.add_argument("--area", help="area slug, e.g. auth, book, agg, pf-rev")
    p.add_argument("--title", help="one-line human title")
    p.add_argument("--oracle", choices=ORACLES, default="intentional")
    p.add_argument("--priority", choices=PRIORITIES, default="medium")
    args = p.parse_args()

    area = args.area or input("Area (e.g. auth, book, agg, pf-rev): ").strip()
    title = args.title or input("Title: ").strip()

    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", area or ""):
        print(f"error: invalid area slug {area!r} (use lowercase, e.g. pf-rev)", file=sys.stderr)
        return 1
    if not title or len(title) < 3:
        print("error: title must be at least 3 characters", file=sys.stderr)
        return 1

    spec_id = next_id(area)
    area_dir = SPECS / area
    area_dir.mkdir(parents=True, exist_ok=True)
    path = area_dir / f"{spec_id}.md"
    if path.exists():
        print(f"error: {path} already exists", file=sys.stderr)
        return 1

    path.write_text(template(title, args.oracle, args.priority))
    regenerate_indexes()
    print(f"created {path.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
