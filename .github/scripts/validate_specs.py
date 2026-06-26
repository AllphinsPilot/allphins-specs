#!/usr/bin/env python3
"""Structural lint for specs.

Enforces, for every `specs/<area>/<ID>.md`:
  - the folder name equals the lowercased ID prefix (path == identity);
  - the ID is `PREFIX-NNN` and unique across the repo;
  - the file contains exactly one `## Scenario:` (a spec is a single, atomic scenario;
    parameterise with an `### Examples` table, never a second scenario).

Usage:
    python .github/scripts/validate_specs.py        # exit 1 on any violation

Run from anywhere; paths resolve relative to the repo.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SPECS = REPO / "specs"

ID_RE = re.compile(r"^(?P<prefix>[A-Z0-9]+(?:-[A-Z0-9]+)*)-(?P<num>\d{3})$")


def main() -> int:
    errors: list[str] = []
    seen: dict[str, Path] = {}

    for md in sorted(SPECS.glob("*/*.md")):
        if md.name == "index.md":
            continue
        rel = md.relative_to(REPO)
        spec_id = md.stem
        area = md.parent.name

        m = ID_RE.match(spec_id)
        if not m:
            errors.append(f"{rel}: id {spec_id!r} is not PREFIX-NNN")
            continue

        if m.group("prefix").lower() != area:
            errors.append(
                f"{rel}: folder {area!r} != lowercased ID prefix {m.group('prefix').lower()!r}"
            )

        if spec_id in seen:
            errors.append(f"{rel}: duplicate id, also at {seen[spec_id].relative_to(REPO)}")
        seen[spec_id] = md

        n = len(re.findall(r"(?m)^## Scenario:", md.read_text()))
        if n != 1:
            errors.append(f"{rel}: {n} '## Scenario:' blocks (a spec must have exactly one)")

    if errors:
        print("Spec validation failed:", file=sys.stderr)
        for e in errors:
            print("  -", e, file=sys.stderr)
        return 1
    print(f"All {len(seen)} specs valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
