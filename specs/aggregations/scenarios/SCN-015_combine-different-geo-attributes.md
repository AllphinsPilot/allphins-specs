---
title: Filters on different geo-attributes can be combined

mode: manual
oracle: intentional
status: active
priority: medium

tags: [regression, aggregation]
source: "Notion: Aggregation / Scenario List Creation / Filtering & Aggregation keys selection (src 85, 110, 116, 117, 118, 119)"
refs: []

---

## Objective

Prove two filters on different geo-attributes in the same risk group can be combined.

## Preconditions

- The user is creating a scenario (Custom scenario, Per-attribute scenario list, TZ, or FG as noted) on the Aggregations page.

## Scenario: different geo-attributes can be combined

```gherkin
Given a first filter on a geo-attribute exists in a risk group
When the user adds a second filter in the same risk group on a different geo-attribute
Then both geo-attribute filters can be selected and are combined
```

## References

- Source manual cases in Notion (see `source`).
