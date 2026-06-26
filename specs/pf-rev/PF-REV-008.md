---
title: Test Structure result equals Deployed Limit

mode: manual
oracle: intentional
status: draft
priority: high

tags: [regression, portfolio, policy]
source: "Notion: Portfolio Review / Policies tab / Test Structure vs Deployed Limit (src 54)"
refs: []

---

## Objective
Prove the Test Structure result is consistent with Deployed Limit across policy configurations.

## Preconditions
- A portfolio with a single XoL policy exists.

## Scenario: test structure matches deployed limit for an XoL
```gherkin
Given a portfolio with only an XoL policy
When the user runs Test Structure with 100bn
Then the result equals the Deployed Limit
```

## Scenario: consistency holds across policy configurations
```gherkin
Given the portfolio's policies are changed to <config>
When the user runs Test Structure again
Then the result stays consistent with Deployed Limit
```

### Examples
| config |
|--------|
| a QS with a limit |
| a QS without a limit |
| an XoL with excess and limit |
| QS benefits-from cases |

## References
- Source manual case in Notion (see `source`).
