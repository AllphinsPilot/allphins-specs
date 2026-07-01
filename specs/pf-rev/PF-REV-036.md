---
title: Test structure matches deployed limit for an XoL

mode: manual
oracle: intentional
status: active
priority: high

tags: [regression, portfolio, policy]
source: "Notion: Portfolio Review / Policies tab / Test Structure vs Deployed Limit (src 54)"
refs: []

---

## Objective

Prove Test Structure for an XoL-only portfolio returns a result equal to the Deployed Limit.

## Preconditions

- A portfolio with a single XoL policy exists.

## Scenario: test structure matches deployed limit for an XoL

```gherkin
Given a portfolio with only an XoL policy
When the user runs Test Structure with 100bn
Then the result equals the Deployed Limit
```

## References

- Source manual case in Notion (see `source`).
