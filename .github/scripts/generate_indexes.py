#!/usr/bin/env python3
"""Regenerate the spec index.md files from each spec's front-matter.

Every `specs/<area>/index.md` lists the area's specs (id, title, oracle), and the
root `specs/index.md` lists the areas with their spec counts. Those lines duplicate
data that lives in the spec front-matter, so they drift the moment a `title` or
`oracle` changes. This script is the single source that rebuilds them.

Usage:
    python .github/scripts/generate_indexes.py          # rewrite the index files
    python .github/scripts/generate_indexes.py --check   # exit 1 if any index is stale

The --check mode writes nothing; it is meant for a pre-commit hook or CI step
(not wired up yet). Run it from anywhere; paths are resolved relative to the repo.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SPECS = REPO / "specs"

ROOT_TITLE = "Allphins specs"
ROOT_INTRO = "Behaviour specifications grouped by area. Open an area to list its specs."


def parse_front_matter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    fm = text.split("---", 2)[1]
    out: dict[str, str] = {}
    for key in ("title", "oracle"):
        m = re.search(rf"^{key}:\s*(.*)$", fm, re.M)
        if m:
            v = m.group(1).strip()
            if len(v) >= 2 and v[0] == v[-1] and v[0] in ("'", '"'):
                v = v[1:-1]
            out[key] = v
    return out


def area_display_name(area: str) -> str:
    """Curated H1 from the existing area index, or a titlecased fallback."""
    idx = SPECS / area / "index.md"
    if idx.exists():
        for line in idx.read_text().splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    return area.replace("-", " ").title()


def existing_area_order() -> list[str]:
    """Area order curated in the current root index; unknown areas appended later."""
    root = SPECS / "index.md"
    if not root.exists():
        return []
    order = []
    for line in root.read_text().splitlines():
        m = re.match(r"\*\s*\[[^\]]+\]\(([^/]+)/\)", line)
        if m:
            order.append(m.group(1))
    return order


def collect() -> dict[str, list[tuple[str, str, str]]]:
    """area -> sorted list of (id, title, oracle)."""
    areas: dict[str, list[tuple[str, str, str]]] = {}
    for md in sorted(SPECS.glob("*/*.md")):
        if md.name == "index.md":
            continue
        fm = parse_front_matter(md.read_text())
        spec_id = md.stem
        areas.setdefault(md.parent.name, []).append(
            (spec_id, fm.get("title", ""), fm.get("oracle", ""))
        )
    for specs in areas.values():
        specs.sort(key=lambda s: s[0])
    return areas


def render_area_index(area: str, specs: list[tuple[str, str, str]]) -> str:
    lines = [f"# {area_display_name(area)}", ""]
    for spec_id, title, oracle in specs:
        lines.append(f"* [{spec_id}]({spec_id}.md) - {title}  `{oracle}`")
    return "\n".join(lines) + "\n"


def render_root_index(areas: dict[str, list[tuple[str, str, str]]]) -> str:
    curated = existing_area_order()
    ordered = [a for a in curated if a in areas]
    ordered += sorted(a for a in areas if a not in ordered)
    lines = [f"# {ROOT_TITLE}", "", ROOT_INTRO, ""]
    for area in ordered:
        n = len(areas[area])
        lines.append(f"* [{area_display_name(area)}]({area}/) - {n} specs")
    return "\n".join(lines) + "\n"


def main() -> int:
    check = "--check" in sys.argv[1:]
    areas = collect()
    if not areas:
        print("no specs found under", SPECS, file=sys.stderr)
        return 1

    targets: dict[Path, str] = {SPECS / "index.md": render_root_index(areas)}
    for area, specs in areas.items():
        targets[SPECS / area / "index.md"] = render_area_index(area, specs)

    stale = []
    for path, content in targets.items():
        current = path.read_text() if path.exists() else None
        if current != content:
            stale.append(path)
            if not check:
                path.write_text(content)

    rel = lambda p: p.relative_to(REPO)
    if check:
        if stale:
            print("Stale index files (run generate_indexes.py):", file=sys.stderr)
            for p in stale:
                print("  -", rel(p), file=sys.stderr)
            return 1
        print("All index files are up to date.")
        return 0

    if stale:
        for p in stale:
            print("updated", rel(p))
    else:
        print("All index files already up to date.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
