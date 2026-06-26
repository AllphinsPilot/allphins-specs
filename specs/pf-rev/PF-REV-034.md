---
title: Delete a policy from the dustbin

mode: manual
oracle: intentional
status: draft
priority: high

tags: [regression, portfolio, policy]
source: "Notion: Portfolio Review / Policies tab / Delete single policy (src 10, 52)"
refs: []

---

## Objective

Prove a policy can be deleted from a portfolio via its dustbin control.

## Preconditions

- A portfolio with two policies exists: one XoL and one QS that benefits from the XoL.

## Scenario: delete a policy from the dustbin

```gherkin
Given a portfolio with a policy
When the user clicks the policy's dustbin button
Then the policy is deleted
```

## References

- Source manual case in Notion (see `source`).
