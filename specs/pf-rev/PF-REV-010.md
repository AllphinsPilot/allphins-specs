---
title: Deployed Limit updates when a policy changes

mode: manual
oracle: intentional
status: draft
priority: medium

tags: [regression, portfolio, policy]
source: "Notion: Portfolio Review / Policies tab / Deployed Limit (src 58)"
refs: []

---

## Objective
Prove the portfolio's Deployed Limit adapts when a policy's share, limit, or excess changes.

## Preconditions
- A portfolio with at least one policy exists.

## Scenario: deployed limit adapts
```gherkin
Given a portfolio with a known Deployed Limit
When a policy's share, limit, or excess is changed
Then the Deployed Limit on the portfolio page adapts accordingly
```

## References
- Source manual case in Notion (see `source`).
