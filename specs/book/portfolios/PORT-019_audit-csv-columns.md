---
title: The audit history CSV has the expected columns

mode: manual
oracle: intentional
status: active
priority: medium

tags: [regression, portfolio, policy, audit]
source: "Notion: Portfolio Review / Audit history (src 133-136 portfolio, 137-140 policy)"
refs: []

---

## Objective

Prove a downloaded audit-history CSV has the expected columns, with only a header row when no actions have occurred.

## Preconditions

- A portfolio and a policy with recorded actions exist.

## Scenario: CSV content columns

```gherkin
Given a downloaded audit history CSV
When it is opened
Then its first columns are: Object type, Object ID, Object name, Date, User, Action, Subject type, Subject ID, Subject name, Changed attribute, Old value, New value
And if no actions have occurred, only the header row is present
```

## References

- Source manual case in Notion (see `source`).
