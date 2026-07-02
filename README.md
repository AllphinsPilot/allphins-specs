# allphins-specs

Behaviour specifications for the Allphins platform, derived from the product team's
manual test cases. These are the human-owned statements of intended behaviour. They are
the source the e2e tests (Cypress) are written against, joined by ID.

## Format

Each spec is one markdown file with YAML front-matter and a body.

```
specs/<area>/<ID>_<slug>.md
```

- **id** is the part of the file name before `_` (e.g. `RISK-002` in
  `RISK-002_edit-risk.md`). It is also the tag the e2e test carries (`@RISK-002`, Cypress)
  so the spec and its test are linked. There is no `id` field; the path is the id.
- **slug** is the part after `_`: a short, kebab-case *capability name* for the behaviour,
  so the file reads meaningfully to a human. It is editorial (derived from the title but
  deliberately terse) and may be shortened by hand; it is not required to round-trip the
  title. `new_spec.py` derives it from the title by default (override with `--slug`).
- **area** is the (possibly nested) folder path, e.g. `book/risks` or
  `aggregations/scenarios`. There is no `area` field; the path is the area. Each area maps
  to an ID prefix via the **registry** (`AREA_PREFIX` in `.github/scripts/_common.py`) —
  so `book/risks` ⇒ `RISK`, giving `book/risks/RISK-002_edit-risk.md`.
- A behaviour that needs several scenarios (e.g. importing data) is **not** one
  multi-scenario spec. It is several specs in the same area, one per scenario
  (e.g. `book/data-sources/DS-007_open-import-modal.md` … `DS-011_confirm-applies-import.md`).
  Each scenario stays atomic and independently runnable.

### Areas

Areas mirror the Allphins product menu (Notion "Global Product Features"). The folder tree
nests under parent groups (`book/`, `aggregations/`, …) for the same levels-of-detail
navigation the menu has. Each leaf area has a short ID prefix, set in the `AREA_PREFIX`
registry.

| group | area path | ID prefix | what it covers |
|-------|-----------|-----------|----------------|
| | `home` | `HOME` | Home page: book summary, activity, LOB selector. |
| Book | `book/portfolios` | `PORT` | Portfolio list, year/tabs, create/renew/edit/delete, pricing & evolution, test structure, audit history. |
| Book | `book/policies` | `POL` | Policy terms, labels, benefits/recoveries, premium & limits, delete. |
| Book | `book/risks` | `RISK` | Risk create/edit, matching, muting, filters, expand. |
| Book | `book/data-sources` | `DS` | Upload, mapping, download, delete, and bulk import. |
| Book | `book/claims` | `CLM` | Claims data and claim→event grouping (Energy). |
| | `analytics` | `ANLY` | Table/matrix splits, metrics, year-on-year. |
| Aggregations | `aggregations` | `AGG` | Computation, policy periods (LOD/RAD), cedant agg, Top Zones. |
| Aggregations | `aggregations/scenarios` | `SCN` | Scenario lists/scenarios, keys, filters, views, dates. |
| Customer Database | `customer-database/asset-matching` | `ASSET` | Asset matching / Allphins Energy DB. |
| Customer Database | `customer-database/entity-matching` | `ENTITY` | Entity resolution (D&B, GLEIF). |
| Databases | `databases/allphins-energy` | `AEDB` | Allphins Energy database. |
| Databases | `databases/gem` | `GEM` | GEM property database. |
| | `reports` | `RPT` | Loss Ladder, Top Zones / Fixed Grid, Excel export. |
| | `user-management` | `USER` | Authentication, profile, currency rates, team & permissions. |

New areas are added by registering them in `AREA_PREFIX` (path → prefix). Empty areas
(no specs yet) are not created as folders until their first spec lands.

### Front-matter fields

| field    | meaning |
|----------|---------|
| title    | one-line human name |
| mode     | `manual` or `automated`, how it is executed today. Everything starts `manual`; flip to `automated` when a Cypress test with the matching tag exists. |
| oracle   | `intentional` (asserts a specific expected result), `characterization` (asserts only "unchanged from an approved baseline"), or `exploratory` (a human judges; no automated assertion). |
| status   | `draft` (derived, not yet reviewed), `reviewed` (a human confirmed the behaviour), `active` (in use). All specs here are `draft`. |
| priority | high / medium / low |
| tags     | free tags; put the line of business here when a spec is LoB-specific (e.g. `energy`). |
| source   | where the spec was derived from (the Notion case and its source row). |
| refs     | optional bundle-relative links to related specs or companion docs. |

### Body sections

- **Objective**, what behaviour this proves and why it matters.
- **Preconditions**, state required before the scenario runs.
- **Scenario: \<name\>**, **exactly one per spec**. A spec describes a single, atomic,
  independent scenario. It may carry an `### Examples` table beneath the scenario to
  parameterise it, but it never contains a second `## Scenario:`. A behaviour that needs
  several scenarios is modelled as several specs in the same area, one per scenario.
- **Assumptions**, present only when an oracle was inferred during derivation. Each line is
  an inference a reviewer must confirm or correct. This is the review gate.
- **References**, companion docs, data-setup notes, the source case.

## Validation

`spec.schema.json` validates the front-matter (run in CI). It is strict: unknown keys and
bad enum values fail. `.github/scripts/validate_specs.py` is the structural lint: it
enforces that every spec lives at `specs/<area>/<ID>_<slug>.md`, that the file name carries
a kebab-case slug, that the area is registered and its ID prefix matches the `AREA_PREFIX`
registry, that IDs are unique, and that **each spec contains exactly one `## Scenario:`**.
`generate_indexes.py --check` separately verifies the index files are in sync.

## Status of this batch

Derived so far: **91 specs** from **93 of the 153 source cases**, across the areas
**book/portfolios**, **book/policies**, **book/risks**, **book/data-sources**,
**analytics**, **aggregations**, **aggregations/scenarios**, and **user-management**. Every
spec is `draft`/`active` and needs review, with special attention to the **Assumptions**
sections where an oracle was inferred. Notes:

- The Book "Filters&Search" case (source row 17) was intentionally **not** derived: it was
  classified no-oracle / do-not-concretize and stays a manual check outside this repo. It
  is one of 60 source cases left `deferred` (see the classification CSV for the per-row
  reason, most are whole sections not yet processed: Aggregation detail, Claims, Databases,
  Home page, Portfolio Optimisation, Scenario Cards).
- Behaviours that span several scenarios are modelled as several specs in the same area,
  one per scenario (e.g. the import flow is `book/data-sources/DS-007`…`DS-011`, audit
  history is `book/portfolios/PORT-017`…`PORT-020`); single parameterised cases use an
  `### Examples` table within their one scenario.
- Provenance for every spec is in its `source` field; the full classification of all 153
  source cases lives in [`testcase-classification.csv`](testcase-classification.csv), one
  row per source case with its `oracle` verdict, `disposition` (`derived`/`deferred`),
  `spec_id`, and the `reason`. This file is also the system of record for the original
  product-team export: it carries each case's `how_to_do_it` steps, `endpoint`, `type`,
  `classes`, `comments`, and per-release columns, so no upstream detail is lost.
- To see the source testcase(s) a given spec was derived from, run
  `python .github/scripts/trace.py <ID>` — it reverses the CSV mapping and prints the
  originating cases (steps and comments). This is authoritative; a spec's `source` field is
  prose provenance and may be coarser than the precise per-spec mapping in the CSV.
