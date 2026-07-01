---
title: Filters take one value each and exclude location-style attributes

mode: manual
oracle: intentional
status: active
priority: medium

tags: [regression, aggregation]
source: "Notion: Aggregation / Scenario List Creation / Filtering & Aggregation keys selection (src 85, 110, 116, 117, 118, 119)"
refs: []

---

## Objective

Prove the filter builder allows only one value per attribute limitation and blocks location-style attributes (Location, Address, Address precision, BZ) from being used as filters.

## Preconditions

- The user is creating a scenario (Custom scenario, Per-attribute scenario list, TZ, or FG as noted) on the Aggregations page.

## Scenario: one value per attribute, and location-style attributes cannot be filtered

```gherkin
Given the scenario filter builder is open
When the user adds an attribute limitation
Then only one value per attribute limitation can be chosen
And Location, Address, Address precision, and BZ attributes cannot be used as filters
```

## References

- Source manual cases in Notion (see `source`).
