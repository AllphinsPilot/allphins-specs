---
title: Generating an aggregation report includes the scenario metadata

mode: manual
oracle: intentional
status: active
priority: medium

tags: [regression, aggregation, report]
source: "Notion: Aggregation / Agg export / Generate report (src 89), Scenario Metadata (src 90)"
refs: []

---

## Objective
Prove generating an aggregation report creates an activity, lands the report under Reports, and that the report contains the scenario metadata.

## Preconditions
- A computed scenario list exists.

## Scenario: generating a report produces a report with metadata
```gherkin
Given a computed scenario list with a selection of actions performed
When the user generates a report
Then an activity is recorded for the generation
And the report appears on the Reports page under Scenario lists
And the report contains the scenario metadata
```

## References
- Source manual cases in Notion (see `source`).
