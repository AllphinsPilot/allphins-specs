---
title: An action adds a correct line

mode: manual
oracle: intentional
status: draft
priority: medium

tags: [regression, portfolio, policy, audit]
source: "Notion: Portfolio Review / Audit history (src 133-136 portfolio, 137-140 policy)"
refs: []

---

## Objective

Prove performing an auditable action adds a correctly-populated line to the regenerated audit history.

## Preconditions

- A portfolio and a policy with recorded actions exist.

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
