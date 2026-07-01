#!/usr/bin/env python3
"""Structural lint for specs.

Enforces, for every `specs/<area>/<ID>_<slug>.md`:
  - the file name is `<ID>_<slug>.md` (ID + a kebab-case capability slug);
  - `<area>` is a known area and its ID prefix matches the registry (AREA_PREFIX);
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

from _common import (
    AREA_PREFIX,
    ID_RE,
    SEP,
    SLUG_RE,
    id_from_stem,
    prefix_from_id,
    slug_from_stem,
)

REPO = Path(__file__).resolve().parents[2]
SPECS = REPO / "specs"


def main() -> int:
    errors: list[str] = []
    seen: dict[str, Path] = {}

    for md in sorted(SPECS.rglob("*.md")):
        if md.name == "index.md":
            continue
        rel = md.relative_to(REPO)
        stem = md.stem
        area = md.parent.relative_to(SPECS).as_posix()

        if SEP not in stem:
            errors.append(f"{rel}: name must be '<ID>{SEP}<slug>.md' (missing '{SEP}<slug>')")
            continue
        spec_id = id_from_stem(stem)
        spec_slug = slug_from_stem(stem)
        if not SLUG_RE.match(spec_slug):
            errors.append(f"{rel}: slug {spec_slug!r} is not kebab-case [a-z0-9-]")

        m = ID_RE.match(spec_id)
        if not m:
            errors.append(f"{rel}: id {spec_id!r} is not PREFIX-NNN")
            continue

        expected_prefix = AREA_PREFIX.get(area)
        if expected_prefix is None:
            errors.append(f"{rel}: unknown area {area!r} (not in AREA_PREFIX registry)")
        elif prefix_from_id(spec_id) != expected_prefix:
            errors.append(
                f"{rel}: ID prefix {prefix_from_id(spec_id)!r} != area prefix "
                f"{expected_prefix!r} for area {area!r}"
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
