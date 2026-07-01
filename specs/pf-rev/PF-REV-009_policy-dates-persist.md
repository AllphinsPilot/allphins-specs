---
title: Policy dates persist after editing and duplication

mode: manual
oracle: intentional
status: active
priority: low

tags: [regression, portfolio, policy]
source: "Notion: Portfolio Review / Policies tab / Edit policy dates (src 60)"
refs: []

---

## Objective
Prove edited policy dates are kept after save and after copy/paste.

## Preconditions
- A policy exists in a portfolio.

## Scenario: dates persist
```gherkin
Given a policy popup
When the user changes the dates and saves
Then the same dates are displayed
When the policy is copied and pasted
Then the same dates are displayed on the copy
```

## References
- Source manual case in Notion (see `source`).
