---
title: A data source mapping can be edited

mode: manual
oracle: intentional
status: draft
priority: low

tags: [regression, portfolio, datasource]
source: "Notion: Portfolio Review / Data Source / Edit a DataSource Mapping (src 47)"
refs: []

---

## Objective
Prove edits to an existing mapping are applied.

## Preconditions
- A mapped data source exists.

## Scenario: edit mapping
```gherkin
Given a mapped data source
When the user edits the mapping and clicks Finish
Then the changes are applied
```

## References
- Source manual case in Notion (see `source`).
