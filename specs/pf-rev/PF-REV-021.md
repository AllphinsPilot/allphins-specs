---
title: Portfolio attributes can be edited

mode: manual
oracle: intentional
status: active
priority: low

tags: [regression, portfolio]
source: "Notion: Portfolio Review / Portfolio - Edit / Edit Portfolio Attributes (src 34)"
refs: []

---

## Objective
Prove a portfolio's name and client can be edited and persist.

## Preconditions
- A portfolio exists.

## Scenario: edit name and client
```gherkin
Given a portfolio
When the user edits its name and client
Then the changes are saved
```

## Assumptions
- Source lists the edits but no outcome; inferred that the edits persist.

## References
- Source manual case in Notion (see `source`).
