---
title: Deleting a data source removes its risks

mode: manual
oracle: intentional
status: active
priority: medium

tags: [regression, portfolio, datasource]
source: "Notion: Portfolio Review / Data Sources / Delete DataSource (src 49)"
refs: []

---

## Objective
Prove deleting a data source removes it and its associated risks.

## Preconditions
- A data source with associated risks exists.

## Scenario: delete a data source
```gherkin
Given a data source with associated risks
When the user deletes it via the Actions menu
Then the data source and its associated risks are deleted
```

## References
- Source manual case in Notion (see `source`).
