---
title: A single risk can be edited

mode: manual
oracle: intentional
status: draft
priority: low

tags: [regression, portfolio, risk]
source: "Notion: Portfolio Review / Risks / Edit single risk (src 23)"
refs: []

---

## Objective
Prove a risk's SOV, currencies, and attributes can be edited.

## Preconditions
- A portfolio with a risk exists.

## Scenario: edit a risk
```gherkin
Given a risk
When the user opens it and edits SOV, currency, and attributes
Then the changes are saved
```

## References
- Source manual case in Notion (see `source`).
