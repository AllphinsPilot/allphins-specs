---
title: A manually created risk is saved and findable

mode: manual
oracle: intentional
status: active
priority: medium

tags: [regression, portfolio, risk]
source: "Notion: Portfolio Review / Risks / Create single risk (src 21)"
refs: []

---

## Objective
Prove a manually created risk is saved and findable.

## Preconditions
- A portfolio is open on the Risks tab.

## Scenario: create and find a risk
```gherkin
Given the Risks tab
When the user clicks Add then Single Risk and creates it
Then the risk is found when searched
```

## References
- Source manual case in Notion (see `source`).
