---
title: A Scenario List report can be mapped as a data source

mode: manual
oracle: intentional
status: active
priority: medium

tags: [regression, portfolio, datasource]
source: "Notion: Portfolio Review / Data Sources / Map a Scenario List report as DataSource (src 146)"
refs: []

---

## Objective
Prove a generated Scenario List report can be uploaded as a data source and is recognised as an Allphins aggregation with cedant agg.

## Preconditions
- A generated Scenario List report is available; a new portfolio exists to receive it.

## Scenario: map an SL report
```gherkin
Given a generated Scenario List report
When the user uploads it as the portfolio's data source
Then scenario id, scenario name, and exposure are listed in the mapping modal
And the data source is listed as an Aggregation with provider "Allphins"
And the cedant agg is filled
```

## References
- Source manual case in Notion (see `source`).
