---
title: Per-risk and bulk actions each have their expected effect

mode: manual
oracle: intentional
status: active
priority: medium

tags: [regression, portfolio, risk]
source: "Notion: Portfolio Review / Risks / Actions on risks (src 35)"
refs: []

---

## Objective
Prove the per-risk and multi-select actions each have their expected effect.

## Preconditions
- A portfolio with several risks exists.

## Scenario: each action has its effect
```gherkin
Given one or more selected risks
When the user performs <action>
Then <effect>
```

### Examples
| action | effect |
|--------|--------|
| Delete | the risks are removed |
| Edit an attribute | the attribute is updated on the risks |
| Mute | the risks are excluded from aggregation |
| Unmute | the risks are included again |

## References
- Source manual case in Notion (see `source`).
