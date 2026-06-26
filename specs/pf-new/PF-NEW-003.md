---
title: Already-renewed portfolios cannot be renewed again

mode: manual
oracle: intentional
status: draft
priority: medium

tags: [regression, portfolio, renewal]
source: "Notion: New Portfolio / No Renewal button for already renewed portfolios (src 28)"
refs: []

---

## Objective
Prove that a portfolio which has already been renewed cannot be renewed a second time, preventing duplicate renewals.

## Preconditions
- A portfolio that has already been renewed exists.

## Scenario: the renewal action is blocked
```gherkin
Given a portfolio that has already been renewed
When the user opens its overview page
Then the renewal action is blocked
```

## References
- Source manual case in Notion (see `source`).
