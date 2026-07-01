---
title: A data source can be uploaded

mode: manual
oracle: intentional
status: active
priority: medium

tags: [regression, portfolio, datasource]
source: "Notion: Portfolio Review / Data Sources / Upload a DataSource (src 43)"
refs: []

---

## Objective
Prove a data source can be uploaded from the drag-and-drop area and is processed.

## Preconditions
- A valid data source file is available.

## Scenario: upload a data source
```gherkin
Given the data-source drag-and-drop area on a page
When the user drops a valid file
Then the data source is uploaded and processed
```

## Assumptions
- Source step is truncated ("In the Drag&Drop area") with no outcome; inferred that a dropped file uploads and processes. Confirm the success indication.

## References
- Source manual case in Notion (see `source`).
