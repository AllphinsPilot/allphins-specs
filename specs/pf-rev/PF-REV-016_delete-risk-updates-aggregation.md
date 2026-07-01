---
title: Deleting a risk removes it and updates aggregation

mode: manual
oracle: intentional
status: active
priority: medium

tags: [regression, portfolio, risk]
source: "Notion: Portfolio Review / Risks / Deleting single risks (src 31)"
refs: []

---

## Objective
Prove a deleted risk disappears and the aggregation changes.

## Preconditions
- A portfolio with a risk contributing to an aggregation exists.

## Scenario: delete a risk
```gherkin
Given a risk
When the user clicks its dustbin button
Then the risk disappears
And the aggregation changes
```

## References
- Source manual case in Notion (see `source`).
