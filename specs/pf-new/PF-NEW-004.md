---
title: Create a single policy

mode: manual
oracle: intentional
status: active
priority: high

tags: [smoke, regression, portfolio]
source: "Notion: New Portfolio / Create a single policy (src 30); Create multiple policies (src 32)"
refs: []

---

## Objective

Prove a policy can be created and saved in a portfolio.

## Preconditions

- A portfolio is open.

## Scenario: create a single policy

```gherkin
Given a portfolio is open
When the user clicks "New policy"
Then the policy creation popup opens
When the user enters a policy and saves
Then the policy is saved and shown in the portfolio
```

## References

- Source manual case in Notion (see `source`).
