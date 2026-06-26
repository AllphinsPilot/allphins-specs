---
title: Audit history generates, downloads, and records changes

mode: manual
oracle: intentional
status: draft
priority: medium

tags: [regression, portfolio, policy, audit]
source: "Notion: Portfolio Review / Audit history (src 133-136 portfolio, 137-140 policy)"
refs: []

---

## Objective
Prove audit history can be generated and downloaded for a portfolio and a policy, that the CSV has the expected columns, and that an action adds a correctly-populated line.

## Preconditions
- A portfolio and a policy with recorded actions exist.

## Scenario: generate audit history
```gherkin
Given a <entity>
When the user clicks its history control (<control>)
Then a "History Export is ready" pop-up appears at the bottom right
```

### Examples
| entity | control |
|--------|---------|
| portfolio | the History button in the portfolio header |
| policy | the clock button in the policy actions column |

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

## Scenario: CSV content columns
```gherkin
Given a downloaded audit history CSV
When it is opened
Then its first columns are: Object type, Object ID, Object name, Date, User, Action, Subject type, Subject ID, Subject name, Changed attribute, Old value, New value
And if no actions have occurred, only the header row is present
```

## Scenario: an action adds a correct line
```gherkin
Given a downloaded audit history
When the user performs <trigger> and regenerates the history
Then a new line appears with Date, User, Action, Subject type, Subject ID, Subject name, Changed attribute, Old value, and New value set correctly
```

### Examples
| entity | trigger |
|--------|---------|
| portfolio | uploading a new data source |
| policy | modifying the policy share |

## References
- Source manual case in Notion (see `source`).
