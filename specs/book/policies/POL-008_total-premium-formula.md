---
title: Total Premium equals the sum of premium times share

mode: manual
oracle: intentional
status: active
priority: medium

tags: [regression, portfolio, policy]
source: "Notion: Portfolio Review / Policies tab / Total Premium (src 56)"
refs: []

---

## Objective
Prove Total Premium is the sum over policies of displayed premium multiplied by share.

## Preconditions
- A portfolio with several policies and known premiums and shares exists.

## Scenario: total premium formula
```gherkin
Given a portfolio with policies
When Total Premium is displayed
Then it equals the sum over policies of premium multiplied by share
```

## References
- Source manual case in Notion (see `source`).
