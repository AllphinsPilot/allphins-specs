---
title: Duplicate IS filters warn while IS and IS-NOT together do not

mode: manual
oracle: intentional
status: active
priority: medium

tags: [regression, aggregation]
source: "Notion: Aggregation / Scenario List Creation / Filtering (src 114, 115)"
refs: []

---

## Objective

Prove duplicate "IS" filters on the same attribute show a non-blocking warning that clears once one operator is changed to "IS NOT".

## Preconditions

- The user is creating a scenario list on the Aggregations page.

## Scenario: duplicate IS filters on one attribute warn, IS/IS-NOT does not

```gherkin
Given two filters use the same attribute with the "IS" operator
When the scenario list is being built
Then a warning is displayed but the scenario list can still be created
And when one filter's operator is changed to "IS NOT" on the same attribute
Then the warning is no longer displayed
```

## Assumptions

- Source row 115 is truncated around whether the warning blocks creation; this spec assumes the warning is non-blocking (creation still allowed). Confirm.

## References

- Source manual cases in Notion (see `source`).
