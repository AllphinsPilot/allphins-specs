---
title: Portfolio names must be unique

mode: manual
oracle: intentional
status: active
priority: low

tags: [regression, portfolio]
source: "Notion: Portfolio Review / Portfolio - Edit / Name cannot be reused (src 38)"
refs: []

---

## Objective
Prove a portfolio cannot be renamed to an already-existing name.

## Preconditions
- Two portfolios exist.

## Scenario: duplicate name refused
```gherkin
Given an existing portfolio name
When the user renames another portfolio to that name
Then the change is refused
```

## References
- Source manual case in Notion (see `source`).
