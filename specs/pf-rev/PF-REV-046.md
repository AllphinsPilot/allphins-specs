---
title: Generate audit history

mode: manual
oracle: intentional
status: draft
priority: medium

tags: [regression, portfolio, policy, audit]
source: "Notion: Portfolio Review / Audit history (src 133-136 portfolio, 137-140 policy)"
refs: []

---

## Objective

Prove the audit-history export can be generated for both a portfolio and a policy, surfacing the "History Export is ready" pop-up.

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

## References

- Source manual case in Notion (see `source`).
