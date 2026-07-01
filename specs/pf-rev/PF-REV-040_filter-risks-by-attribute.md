---
title: Filtering by an attribute shows only matching risks

mode: manual
oracle: intentional
status: active
priority: medium

tags: [regression, portfolio, risk]
source: "Notion: Portfolio Review / Risks / Filter, Search, Combine (src 16, 18, 20)"
refs: []

---

## Objective

Prove applying an attribute filter with an operator shows only the matching risks.

## Preconditions

- A portfolio with many risks across varied attributes exists.

## Scenario: filtering by an attribute shows only matching risks

```gherkin
Given the risk list
When the user applies a filter on an attribute with an operator
Then only risks matching that filter are shown
```

## Assumptions

- The original "nothing is missed" completeness check (src 16) stays a manual exploratory check; it is not asserted here.

## References

- Source manual case in Notion (see `source`).
