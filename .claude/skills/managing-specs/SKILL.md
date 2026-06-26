---
name: managing-specs
description: >-
  Create, delete, and run Allphins behaviour specs in the allphins-specs repo.
  Use when adding or removing a spec under specs/, when a spec title changes,
  when regenerating the spec indexes, or when coordinating a manual spec-run /
  test execution pass.
---

# Managing Allphins specs

Specs live at `specs/<area>/<ID>.md` (e.g. `specs/auth/AUTH-001.md`). The path is the
identity: `<area>` is the lowercased ID prefix, `<ID>` is `PREFIX-NNN`. Use the scripts
below — never hand-create/rename/delete spec files, invent IDs, or edit any `index.md`
(they are generated).

## Create a spec

```bash
python .github/scripts/new_spec.py --area <area> --title "<title>"
```

Picks the next free ID, scaffolds front-matter + body, and regenerates the indexes.
Optional: `--oracle {intentional,characterization,exploratory}` (default `intentional`),
`--priority {high,medium,low}` (default `medium`).

Then edit the generated body: `Objective`, `Preconditions`, **exactly one**
`## Scenario:` block (fenced ```` ```gherkin ````), and `## References`. Add an
`## Assumptions` section only if you inferred an expected result a reviewer must confirm.

One scenario per spec — it must be atomic and independent. Parameterise a single scenario
with an `### Examples` table, but never add a second `## Scenario:`. For a behaviour that
needs several scenarios (e.g. an end-to-end flow), create a dedicated flow area and add one
spec per scenario, e.g. `--area book-003` → `BOOK-003-001`, `BOOK-003-002`, …

## Delete a spec

```bash
python .github/scripts/delete_spec.py <ID>
```

Removes the file, reconciles `testcase-classification.csv` (its source row flips back to
`deferred`), cleans up an emptied area folder, and regenerates the indexes.

## After editing a spec's title (or any spec set change)

Indexes are generated. Regenerate and verify:

```bash
python .github/scripts/generate_indexes.py          # rewrite indexes
python .github/scripts/generate_indexes.py --check   # must exit 0
```

## Run a manual spec pass

Only `reviewed`/`active` specs are included. Admit specs first:

- Per spec: confirm the behaviour, clear `## Assumptions`, set `status: reviewed`.
- All at once (local only, git-ignored): `./set-spec-status.local.sh reviewed`
  (use `draft` to remove them).

Then trigger the **Spec run** GitHub Action (`.github/workflows/spec-run.yml`,
`workflow_dispatch`) with a run label. It opens a `spec-run` issue listing eligible specs
grouped by area with pass/fail checkboxes, and hard-fails if none are eligible. Automated
(Playwright) results do not go in this issue.

## Validate

Front-matter must satisfy `spec.schema.json` (required: `title`, `mode`, `oracle`,
`status`, `priority`; no unknown keys; valid enums). New specs are `mode: manual`,
`status: draft`.

Structure lint (path == identity, unique IDs, exactly one scenario per spec):

```bash
python .github/scripts/validate_specs.py   # must exit 0
```
