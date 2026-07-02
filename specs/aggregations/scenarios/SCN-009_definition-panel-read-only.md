---
title: The scenario definition panel shows metadata read-only

mode: manual
oracle: intentional
status: active
priority: low

tags: [regression, aggregation]
source: "Notion: Aggregation / Agg page / Scenario Definition (src 111, 113)"
refs: []

---

## Objective

Prove the "See scenario definition" panel shows coherent scenario metadata that cannot be edited.

## Preconditions

- A scenario list with at least one scenario exists.

## Scenario: definition metadata is shown read-only

```gherkin
Given a scenario list is open
When the user clicks "See scenario definition"
Then the left panel shows coherent scenario metadata (name, risk-group filters)
And none of the displayed metadata can be edited
```

## References

- Source manual cases in Notion (see `source`).
