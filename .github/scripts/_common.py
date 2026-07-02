#!/usr/bin/env python3
"""Shared helpers for the spec scripts.

A spec file is named `<ID>_<slug>.md` and lives at `specs/<area>/<ID>_<slug>.md`,
where `<area>` is a (possibly nested) path such as `book/portfolios` or
`aggregations/scenarios`. The `<ID>` is `PREFIX-NNN` (the load-bearing identity, also
the e2e test tag, e.g. `@USER-001`); the `<slug>` is a short kebab-case capability name.

The area↔prefix relationship is an explicit registry (below) rather than "folder name ==
lowercased prefix", because areas nest and use readable folder names (`data-sources`)
while prefixes stay short (`DS`).
"""
from __future__ import annotations

import re

SEP = "_"
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ID_RE = re.compile(r"^(?P<prefix>[A-Z0-9]+)-(?P<num>\d{3})$")

# area path (relative to specs/) -> ID prefix. The single source of truth for
# which areas exist and what prefix each uses. Mirrors the Notion product menu.
AREA_PREFIX: dict[str, str] = {
    "home": "HOME",
    "book/portfolios": "PORT",
    "book/policies": "POL",
    "book/risks": "RISK",
    "book/data-sources": "DS",
    "book/claims": "CLM",
    "analytics": "ANLY",
    "aggregations": "AGG",
    "aggregations/scenarios": "SCN",
    "customer-database/asset-matching": "ASSET",
    "customer-database/entity-matching": "ENTITY",
    "databases/allphins-energy": "AEDB",
    "databases/gem": "GEM",
    "reports": "RPT",
    "user-management": "USER",
}
PREFIX_AREA: dict[str, str] = {v: k for k, v in AREA_PREFIX.items()}

# Display/ordering: parent group folders that hold sub-areas (no specs of their own).
GROUP_DIRS = ("book", "aggregations", "customer-database", "databases")

# Ordering for indexes (Notion menu order). Entries not listed sort last, alphabetically.
AREA_ORDER = [
    "home",
    "book", "book/portfolios", "book/policies", "book/risks", "book/data-sources", "book/claims",
    "analytics",
    "aggregations", "aggregations/scenarios",
    "customer-database", "customer-database/asset-matching", "customer-database/entity-matching",
    "databases", "databases/allphins-energy", "databases/gem",
    "reports",
    "user-management",
]

# Folder segment -> display name overrides (otherwise Title Case the kebab segment).
DISPLAY_OVERRIDES = {"gem": "GEM"}


def id_from_stem(stem: str) -> str:
    """The spec ID part of a file stem (`USER-001_foo` -> `USER-001`)."""
    return stem.split(SEP, 1)[0]


def slug_from_stem(stem: str) -> str:
    """The slug part of a file stem, or '' if the stem carries no slug."""
    return stem.split(SEP, 1)[1] if SEP in stem else ""


def prefix_from_id(spec_id: str) -> str:
    """`PORT-008` -> `PORT`."""
    return spec_id.rsplit("-", 1)[0]


def display_name(segment: str) -> str:
    """Human display name for a single folder segment."""
    return DISPLAY_OVERRIDES.get(segment, segment.replace("-", " ").title())


def order_key(area_path: str) -> tuple[int, str]:
    """Sort key placing known areas in Notion order, unknown ones last alphabetically."""
    try:
        return (AREA_ORDER.index(area_path), area_path)
    except ValueError:
        return (len(AREA_ORDER), area_path)


def slug(title: str) -> str:
    """Slugify a title into a kebab-case capability name (a default for new specs)."""
    t = title.lower().replace("'", "").replace("’", "")
    t = t.replace("%", " percent ").replace("&", " and ")
    t = re.sub(r"[^a-z0-9]+", "-", t)
    return t.strip("-")
