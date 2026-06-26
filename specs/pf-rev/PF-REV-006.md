---
title: A policy share of 0% is allowed

mode: manual
oracle: intentional
status: draft
priority: low

tags: [regression, portfolio, policy]
source: "Notion: Portfolio Review / Policies tab / Policy share of 0% (src 48)"
refs: []

---

## Objective
Prove that entering a 0% share on a policy is accepted.

## Preconditions
- A policy exists in a portfolio.

## Scenario: zero share is accepted
```gherkin
Given a policy
When the user sets its share to 0%
Then the value is accepted
```

## References
- Source manual case in Notion (see `source`).
