---
title: Consistency holds across policy configurations

mode: manual
oracle: intentional
status: active
priority: high

tags: [regression, portfolio, policy]
source: "Notion: Portfolio Review / Policies tab / Test Structure vs Deployed Limit (src 54)"
refs: []

---

## Objective

Prove the Test Structure result stays consistent with the Deployed Limit as the portfolio's policy configuration changes.

## Preconditions

- A portfolio with a single XoL policy exists.

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
