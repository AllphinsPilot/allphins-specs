---
title: Risk list search and filtering

mode: manual
oracle: intentional
status: draft
priority: medium

tags: [regression, portfolio, risk]
source: "Notion: Portfolio Review / Risks / Filter, Search, Combine (src 16, 18, 20)"
refs: []

---

## Objective
Prove attribute filters and search narrow the risk list correctly and compose, including across pagination.

## Preconditions
- A portfolio with many risks across varied attributes exists.

## Scenario: filtering by an attribute shows only matching risks
```gherkin
Given the risk list
When the user applies a filter on an attribute with an operator
Then only risks matching that filter are shown
```

## Scenario: search and filter compose
```gherkin
Given the risk list
When the user applies a search and then a filter
Then the shown risks satisfy both
And applying them in the other order yields the same set
And the result holds when changing pages
```

## Assumptions
- The original "nothing is missed" completeness check (src 16) stays a manual exploratory check; it is not asserted here.

## References
- Source manual case in Notion (see `source`).
