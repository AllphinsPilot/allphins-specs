---
title: A data source can be downloaded

mode: manual
oracle: intentional
status: active
priority: low

tags: [regression, portfolio, datasource]
source: "Notion: Portfolio Review / Data Sources / Download DataSource (src 51)"
refs: []

---

## Objective
Prove a data source can be downloaded from the Actions menu.

## Preconditions
- A data source exists.

## Scenario: download a data source
```gherkin
Given a data source
When the user clicks Actions then Download
Then the data source file is downloaded
```

## Assumptions
- Source gives steps but no explicit outcome; inferred a file download.

## References
- Source manual case in Notion (see `source`).
