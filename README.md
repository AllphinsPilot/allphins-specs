# allphins-specs

Behaviour specifications for the Allphins platform, derived from the product team's
manual test cases. These are the human-owned statements of intended behaviour. They are
the source the e2e Playwright tests are written against, joined by ID.

## Format

Each spec is one markdown file with YAML front-matter and a body.

```
specs/<area>/<ID>.md
```

- **id** is the file name without `.md` (e.g. `AUTH-001`). It is also the tag a Playwright
  test carries (`@AUTH-001`) so the spec and its test are linked. There is no `id` field;
  the path is the id.
- **area** is the folder (e.g. `auth`). There is no `area` field; the folder is the area.
  The folder name is the lowercased ID prefix, so `pf-new/PF-NEW-002.md`.

### Front-matter fields

| field    | meaning |
|----------|---------|
| title    | one-line human name |
| mode     | `manual` or `automated`, how it is executed today. Everything starts `manual`; flip to `automated` when a Playwright test with the matching tag exists. |
| oracle   | `intentional` (asserts a specific expected result), `characterization` (asserts only "unchanged from an approved baseline"), or `exploratory` (a human judges; no automated assertion). |
| status   | `draft` (derived, not yet reviewed), `reviewed` (a human confirmed the behaviour), `active` (in use). All specs here are `draft`. |
| priority | high / medium / low |
| tags     | free tags; put the line of business here when a spec is LoB-specific (e.g. `energy`). |
| source   | where the spec was derived from (the Notion case and its source row). |
| refs     | optional bundle-relative links to related specs or companion docs. |

### Body sections

- **Objective**, what behaviour this proves and why it matters.
- **Preconditions**, state required before the scenario runs.
- **Scenario: \<name\>**, one or more, each a fenced ```gherkin``` block. Families use an
  `### Examples` table beneath the scenario.
- **Assumptions**, present only when an oracle was inferred during derivation. Each line is
  an inference a reviewer must confirm or correct. This is the review gate.
- **References**, companion docs, data-setup notes, the source case.

## Validation

`spec.schema.json` validates the front-matter (run in CI). It is strict: unknown keys and
bad enum values fail. A separate path lint enforces that every spec lives at
`specs/<area>/<ID>.md`, that the folder matches the ID prefix, and that IDs are unique.

## Status of this batch

Derived so far: areas **auth**, **book**, **pf-new**, **pf-rev**, and **agg**, 65 specs
from 85 of the 153 source cases. Every spec is `draft` and needs review, with special
attention to the **Assumptions** sections where an oracle was inferred. Notes:

- `book` case "Filters&Search" (source row 17) was intentionally **not** derived: it was
  classified no-oracle / do-not-concretize and stays a manual check outside this repo. It
  is one of 68 source cases left `deferred` (see the classification CSV for the per-row
  reason, most are whole sections not yet processed: Aggregation detail, Risks, Policies,
  Databases, Home page, Portfolio Optimisation, Scenario Cards).
- Several families were folded: the import flow is one spec with multiple scenarios, the
  template download and the two renewal entry points use `Examples` tables, and the
  aggregation filter rules are grouped into a few specs.
- Provenance for every spec is in its `source` field; the full classification of all 153
  source cases lives in [`testcase-classification.csv`](testcase-classification.csv), one
  row per source case with its `oracle` verdict, `disposition` (`derived`/`deferred`),
  `spec_id`, and the `reason`. This file is also the system of record for the original
  product-team export: it carries each case's `how_to_do_it` steps, `endpoint`, `type`,
  `classes`, `comments`, and per-release columns, so no upstream detail is lost.
