#!/usr/bin/env python3
"""Shared helpers for the spec scripts.

A spec file is named `<ID>_<slug>.md` (e.g. `AUTH-001_sign-in-with-valid-credentials.md`).
The `<ID>` is the load-bearing identity (it is also the Playwright tag, e.g. `@AUTH-001`);
the `<slug>` is a short, human-readable capability name derived from the title. The `_`
separator is unambiguous because neither the ID (only hyphens/digits) nor the slug
(kebab-case, underscores forbidden) can contain an underscore.
"""
from __future__ import annotations

import re

SEP = "_"
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def id_from_stem(stem: str) -> str:
    """The spec ID part of a file stem (`AUTH-001_foo` -> `AUTH-001`)."""
    return stem.split(SEP, 1)[0]


def slug_from_stem(stem: str) -> str:
    """The slug part of a file stem, or '' if the stem carries no slug."""
    return stem.split(SEP, 1)[1] if SEP in stem else ""


def slug(title: str) -> str:
    """Slugify a title into a kebab-case capability name.

    A reasonable default for new specs; slugs are editorial and may be shortened
    by hand afterwards. Not required to round-trip the title.
    """
    t = title.lower().replace("'", "").replace("’", "")
    t = t.replace("%", " percent ").replace("&", " and ")
    t = re.sub(r"[^a-z0-9]+", "-", t)
    return t.strip("-")
