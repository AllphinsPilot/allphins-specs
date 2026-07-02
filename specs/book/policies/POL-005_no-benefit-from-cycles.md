---
title: Benefit-from loops between layers are forbidden

mode: manual
oracle: intentional
status: active
priority: medium

tags: [regression, portfolio, policy]
source: "Notion: Portfolio Review / Policies tab / Forbid loops with Benefit from (src 46)"
refs: []

---

## Objective
Prove the platform prevents a circular benefit-from relationship between two layers.

## Preconditions
- A portfolio with two layers A and B exists.

## Scenario: a benefit-from cycle is prevented
```gherkin
Given a portfolio with layers A and B
When A is set to benefit from B
And the user tries to set B to benefit from A
Then the action is prevented
```

## References
- Source manual case in Notion (see `source`).
