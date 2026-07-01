#!/usr/bin/env python3
"""One-time migration: rename bare `<ID>.md` specs to `<ID>_<slug>.md`.

Uses the curated ID -> slug map below (slugs are short, editorial capability names,
not mechanically derived from titles). Renames via `git mv` so history is preserved,
then regenerates the indexes. Idempotent: already-renamed specs are skipped.

Usage:
    python .github/scripts/rename_specs.py            # perform the rename
    python .github/scripts/rename_specs.py --dry-run  # print what would change
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
REPO = SCRIPTS.parents[1]
SPECS = REPO / "specs"

SLUGS = {
    "AGG-001": "create-aggregation-objects",
    "AGG-002": "scenario-updates-on-new-source",
    "AGG-003": "policy-selection-updates-exposure",
    "AGG-004": "exposure-views",
    "AGG-005": "date-shortcuts-set-both-dates",
    "AGG-006": "report-includes-metadata",
    "AGG-007": "view-scenario-read-only",
    "AGG-008": "casualty-loss-requires-insured-subclass",
    "AGG-009": "lod-considers-all-exposures",
    "AGG-010": "rad-considers-in-range-inceptions",
    "AGG-011": "policy-live-at-resets-run-off",
    "AGG-012": "run-off-date-recomputes",
    "AGG-013": "definition-panel-read-only",
    "AGG-014": "view-aggregation-opens-computation",
    "AGG-015": "only-agg-keys-filterable",
    "AGG-016": "geo-key-excludes-other-geos",
    "AGG-017": "single-value-no-location-filters",
    "AGG-018": "no-duplicate-attribute-in-group",
    "AGG-019": "combine-different-geo-attributes",
    "AGG-020": "values-combine-with-or",
    "AGG-021": "lakehouse-requires-peril",
    "AGG-022": "duplicate-is-filter-warns",
    "AGG-023": "top-zones-count-bounded",
    "AGG-024": "top-zones-radius-bounded",

    "AUTH-001": "sign-in-with-valid-credentials",
    "AUTH-002": "reject-wrong-password",
    "AUTH-003": "reset-forgotten-password",
    "AUTH-004": "sign-in-via-sso",

    "BOOK-001": "portfolio-list-baseline",
    "BOOK-002": "year-filter-membership",
    "BOOK-003": "policy-dates-move-portfolio",
    "BOOK-004": "expired-policy-stays-in-force",
    "BOOK-005": "open-import-modal",
    "BOOK-006": "download-import-templates",
    "BOOK-007": "preview-import-changes",
    "BOOK-008": "cancel-discards-import",
    "BOOK-009": "confirm-applies-import",

    "PF-NEW-001": "create-portfolio-and-policy",
    "PF-NEW-002": "renew-portfolio",
    "PF-NEW-003": "no-double-renewal",
    "PF-NEW-004": "create-policy",
    "PF-NEW-005": "create-policies-rapidly",

    "PF-REV-001": "special-conditions-in-aggregation",
    "PF-REV-002": "policy-popup-details",
    "PF-REV-003": "manage-policy-labels",
    "PF-REV-004": "no-benefit-from-cycles",
    "PF-REV-005": "zero-share-allowed",
    "PF-REV-006": "duplicate-policy",
    "PF-REV-007": "total-premium-formula",
    "PF-REV-008": "deployed-limit-updates",
    "PF-REV-009": "policy-dates-persist",
    "PF-REV-010": "policies-tab-baseline",
    "PF-REV-011": "create-risk",
    "PF-REV-012": "edit-risk",
    "PF-REV-013": "match-fills-meta-attributes",
    "PF-REV-014": "mute-excludes-risk",
    "PF-REV-015": "second-source-adds-risks",
    "PF-REV-016": "delete-risk-updates-aggregation",
    "PF-REV-017": "smart-algorithms-match-definitions",
    "PF-REV-018": "risk-actions",
    "PF-REV-019": "data-source-matching",
    "PF-REV-020": "risk-links-to-portfolio",
    "PF-REV-021": "edit-portfolio-details",
    "PF-REV-022": "portfolio-names-unique",
    "PF-REV-023": "upload-data-source",
    "PF-REV-024": "map-data-source",
    "PF-REV-025": "edit-mapping",
    "PF-REV-026": "delete-data-source",
    "PF-REV-027": "download-data-source",
    "PF-REV-028": "scenario-report-as-data-source",
    "PF-REV-029": "cedant-aggregation-has-data",
    "PF-REV-030": "pricing-evolution-baseline",
    "PF-REV-031": "scenario-selection-updates-view",
    "PF-REV-032": "compare-two-portfolios",
    "PF-REV-033": "analytics-tables-populate",
    "PF-REV-034": "delete-policy",
    "PF-REV-035": "delete-layer-updates-aggregation",
    "PF-REV-036": "test-structure-matches-deployed-limit",
    "PF-REV-037": "test-structure-consistency",
    "PF-REV-038": "columns-match-risk-class",
    "PF-REV-039": "no-terror-risks-from-edm",
    "PF-REV-040": "filter-risks-by-attribute",
    "PF-REV-041": "search-and-filter-compose",
    "PF-REV-042": "expand-energy-risk-map",
    "PF-REV-043": "expand-availability-by-source",
    "PF-REV-044": "delete-portfolio",
    "PF-REV-045": "delete-renewal-clears-link",
    "PF-REV-046": "generate-audit-history",
    "PF-REV-047": "download-audit-csv",
    "PF-REV-048": "audit-csv-columns",
    "PF-REV-049": "audit-action-adds-line",
}


def git_mv(src: Path, dst: Path) -> None:
    subprocess.run(["git", "-C", str(REPO), "mv", str(src), str(dst)], check=True)


def regenerate_indexes() -> None:
    subprocess.run([sys.executable, str(SCRIPTS / "generate_indexes.py")], check=True)


def main() -> int:
    dry = "--dry-run" in sys.argv[1:]

    renamed = skipped = 0
    problems: list[str] = []
    for spec_id, s in SLUGS.items():
        area = spec_id.rsplit("-", 1)[0].lower()
        old = SPECS / area / f"{spec_id}.md"
        new = SPECS / area / f"{spec_id}_{s}.md"
        if new.exists():
            skipped += 1
            continue
        if not old.exists():
            problems.append(f"{spec_id}: neither {old.name} nor {new.name} present")
            continue
        rel_old, rel_new = old.relative_to(REPO), new.relative_to(REPO)
        print(("would rename " if dry else "renaming ") + f"{rel_old} -> {rel_new}")
        if not dry:
            git_mv(old, new)
        renamed += 1

    # Any bare <ID>.md left behind that we don't have a slug for?
    # (bare IDs use hyphens only, so an underscore means already-renamed.)
    for md in sorted(SPECS.glob("*/*.md")):
        if md.name == "index.md" or "_" in md.stem:
            continue
        if md.stem not in SLUGS:
            problems.append(f"{md.relative_to(REPO)}: no slug mapping for {md.stem}")

    print(f"\nrenamed={renamed} skipped(already done)={skipped}")
    if problems:
        print("PROBLEMS:", file=sys.stderr)
        for p in problems:
            print("  -", p, file=sys.stderr)
        return 1

    if not dry and renamed:
        regenerate_indexes()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
