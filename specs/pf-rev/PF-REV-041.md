---
title: Search and filter compose

mode: manual
oracle: intentional
status: active
priority: medium

tags: [regression, portfolio, risk]
source: "Notion: Portfolio Review / Risks / Filter, Search, Combine (src 16, 18, 20)"
refs: []

---

## Objective

Prove search and attribute filters compose (order-independent) and the result holds across pagination.

## Preconditions

- A portfolio with many risks across varied attributes exists.

## Scenario: search and filter compose

```gherkin
Given the risk list
When the user applies a search and then a filter
Then the shown risks satisfy both
And applying them in the other order yields the same set
And the result holds when changing pages
```

## References

- Source manual case in Notion (see `source`).
