---
title: Changing only the run-off date recomputes exposures

mode: manual
oracle: intentional
status: active
priority: high

tags: [regression, aggregation]
source: "Notion: Aggregation / Agg page / Policy live at/Exposure run off date (src 82)"
refs: []

---

## Objective

Prove that changing only "Exposure run off date" recomputes the scenario exposures to the new run-off date.

## Preconditions

- A portfolio with a computed scenario exists.

## Scenario: changing only the run-off date recomputes

```gherkin
Given a computed scenario
When the user changes only "Exposure run off date" and clicks Compute
Then the scenario exposures are adapted to the new run-off date
```

## References

- Source manual case in Notion (see `source`).
