---
title: A data source can be mapped

mode: manual
oracle: intentional
status: draft
priority: medium

tags: [regression, portfolio, datasource]
source: "Notion: Portfolio Review / Data Sources / Map a DataSource (src 45)"
refs: []

---

## Objective
Prove the mapping modal works for each data source type.

## Preconditions
- An uploaded data source of the given type is available.

## Scenario: map a data source by type
```gherkin
Given an uploaded <type> data source
When the user opens its mapping modal and completes the mapping
Then the mapping is saved
```

### Examples
| type |
|------|
| Excel |
| EDM |
| CEDE |
| Cedant agg |

## Assumptions
- Source lists the four mapping modals with no per-type outcome; inferred each mapping completes and saves. Confirm any type-specific differences.

## References
- Source manual case in Notion (see `source`).
