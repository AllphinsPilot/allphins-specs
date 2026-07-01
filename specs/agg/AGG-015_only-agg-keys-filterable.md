---
title: Only aggregation keys can be used as filters

mode: manual
oracle: intentional
status: active
priority: medium

tags: [regression, aggregation]
source: "Notion: Aggregation / Scenario List Creation / Filtering & Aggregation keys selection (src 85, 110, 116, 117, 118, 119)"
refs: []

---

## Objective

Prove the scenario filter builder offers only aggregation keys as filterable attributes.

## Preconditions

- The user is creating a scenario (Custom scenario, Per-attribute scenario list, TZ, or FG as noted) on the Aggregations page.

## Scenario: only aggregation keys are filterable

```gherkin
Given the scenario filter builder is open
When the user adds a filter
Then only aggregation keys are offered as filterable attributes
```

## References

- Source manual cases in Notion (see `source`).
