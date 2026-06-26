---
title: Deleting a policy updates aggregation

mode: manual
oracle: intentional
status: draft
priority: high

tags: [regression, portfolio, policy]
source: "Notion: Portfolio Review / Policies tab / Delete single policy (src 10, 52)"
refs: []

---

## Objective
Prove a policy can be deleted and that deleting a layer updates the aggregation that depended on it.

## Preconditions
- A portfolio with two policies exists: one XoL and one QS that benefits from the XoL.

## Scenario: delete a policy from the dustbin
```gherkin
Given a portfolio with a policy
When the user clicks the policy's dustbin button
Then the policy is deleted
```

## Scenario: deleting a layer updates the dependent aggregation
```gherkin
Given a portfolio with an XoL and a QS that benefits from it
And the aggregation has been noted
When the user deletes the XoL
Then the aggregation for the dependent QS changes
```

## References
- Source manual case in Notion (see `source`).
