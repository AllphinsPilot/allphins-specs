#!/usr/bin/env python3
"""Regenerate the spec index.md files from the folder tree and front-matter.

Every directory under `specs/` gets an `index.md`:
  - a leaf area (holds specs) lists its specs (id, title, oracle);
  - a group directory (holds sub-areas) lists its sub-areas with spec counts;
  - the root lists the top-level entries.
These duplicate data that lives in the tree/front-matter, so this script is the single
source that rebuilds them.

Usage:
    python .github/scripts/generate_indexes.py          # rewrite the index files
    python .github/scripts/generate_indexes.py --check   # exit 1 if any index is stale

The --check mode writes nothing; it is meant for a pre-commit hook or CI step.
Run it from anywhere; paths resolve relative to the repo.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from _common import display_name, id_from_stem, order_key

REPO = Path(__file__).resolve().parents[2]
SPECS = REPO / "specs"

ROOT_TITLE = "Allphins specs"
ROOT_INTRO = "Behaviour specifications grouped by product area. Open an area to list its specs."


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


def curated_title(d: Path) -> str:
    """Keep a curated H1 from an existing index.md, else derive from the folder name."""
    idx = d / "index.md"
    if idx.exists():
        for line in idx.read_text().splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    return ROOT_TITLE if d == SPECS else display_name(d.name)


def spec_count(d: Path) -> int:
    return sum(1 for md in d.rglob("*.md") if md.name != "index.md")


def subdirs(d: Path) -> list[Path]:
    kids = [k for k in d.iterdir() if k.is_dir()]
    kids.sort(key=lambda k: order_key(k.relative_to(SPECS).as_posix()))
    return kids


def specs_in(d: Path) -> list[Path]:
    return sorted((f for f in d.glob("*.md") if f.name != "index.md"), key=lambda f: f.stem)


def render(d: Path) -> str:
    title = ROOT_TITLE if d == SPECS else curated_title(d)
    lines = [f"# {title}", ""]
    if d == SPECS:
        lines += [ROOT_INTRO, ""]
    for sub in subdirs(d):
        n = spec_count(sub)
        lines.append(f"* [{display_name(sub.name)}]({sub.name}/) - {n} spec{'' if n == 1 else 's'}")
    for md in specs_in(d):
        fm = parse_front_matter(md.read_text())
        lines.append(f"* [{id_from_stem(md.stem)}]({md.name}) - {fm.get('title','')}  `{fm.get('oracle','')}`")
    return "\n".join(lines) + "\n"


def all_dirs() -> list[Path]:
    dirs = [SPECS]
    dirs += [d for d in SPECS.rglob("*") if d.is_dir()]
    return dirs


def main() -> int:
    check = "--check" in sys.argv[1:]
    if not any(SPECS.rglob("*.md")):
        print("no specs found under", SPECS, file=sys.stderr)
        return 1

    targets = {d / "index.md": render(d) for d in all_dirs()}

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
