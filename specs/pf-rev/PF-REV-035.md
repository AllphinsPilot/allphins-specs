---
title: Deleting a layer updates the dependent aggregation

mode: manual
oracle: intentional
status: active
priority: high

tags: [regression, portfolio, policy]
source: "Notion: Portfolio Review / Policies tab / Delete single policy (src 10, 52)"
refs: []

---

## Objective

Prove deleting a layer (XoL) updates the aggregation of the QS that depended on it.

## Preconditions

- A portfolio with two policies exists: one XoL and one QS that benefits from the XoL.

## Scenario: deleting a layer updates the dependent aggregation

```gherkin
Given a portfolio with an XoL and a QS that benefits from it
And the aggregation has been noted
When the user deletes the XoL
Then the aggregation for the dependent QS changes
```

## References

- Source manual case in Notion (see `source`).
