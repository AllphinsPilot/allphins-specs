---
title: Cedant aggregation shows data when considered for a scenario list

mode: manual
oracle: intentional
status: draft
priority: low

tags: [regression, portfolio, aggregation]
source: "Notion: Portfolio Review / Cedant aggregations / Display (src 53)"
refs: []

---

## Objective
Prove the Cedant agg shows data when the portfolio is considered for the chosen scenario list.

## Preconditions
- A portfolio that is considered for a chosen scenario list exists.

## Scenario: cedant agg has data
```gherkin
Given a portfolio considered for a chosen scenario list
When the user opens Cedant agg
Then it shows data
```

## References
- Source manual case in Notion (see `source`).
