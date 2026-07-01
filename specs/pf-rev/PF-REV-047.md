---
title: Download the audit CSV

mode: manual
oracle: intentional
status: active
priority: medium

tags: [regression, portfolio, policy, audit]
source: "Notion: Portfolio Review / Audit history (src 133-136 portfolio, 137-140 policy)"
refs: []

---

## Objective

Prove the generated audit history downloads as a CSV whose file name follows the expected pattern for both a portfolio and a policy.

## Preconditions

- A portfolio and a policy with recorded actions exist.

## Scenario: download the audit CSV

```gherkin
Given the "History Export is ready" pop-up
When the user clicks Save
Then a CSV downloads named like "<pattern>"
```

### Examples
| entity | pattern |
|--------|---------|
| portfolio | allphins_export_history_portfolio_<portfolio_uuid>_<group_id>_<YYYY>-<MM>-<DD>.csv |
| policy | allphins_export_history_policy_<policy_id>_<group_id>_<YYYY>-<MM>-<DD>.csv |

## References

- Source manual case in Notion (see `source`).
