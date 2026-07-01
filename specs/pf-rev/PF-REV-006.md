---
title: A policy can be duplicated

mode: manual
oracle: intentional
status: active
priority: low

tags: [regression, portfolio, policy]
source: "Notion: Portfolio Review / Policies tab / Duplicate a policy (src 50)"
refs: []

---

## Objective
Prove copy/paste creates a new policy with the same parameters.

## Preconditions
- A policy exists in a portfolio.

## Scenario: duplicate keeps parameters
```gherkin
Given a policy
When the user clicks the copy/paste button
Then a new policy is created with the same parameters
```

## References
- Source manual case in Notion (see `source`).
