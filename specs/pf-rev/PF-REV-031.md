---
title: Scenario selection updates Pricing and Evolution

mode: manual
oracle: intentional
status: draft
priority: low

tags: [regression, portfolio, pricing, evolution]
source: "Notion: Portfolio Review / Pricing & Evolution / Scenario dropdown (src 57, 62)"
refs: []

---

## Objective
Prove selecting a scenario from the dropdown updates the tab's figures.

## Preconditions
- A portfolio with multiple scenarios available exists.

## Scenario: scenario selection updates the view
```gherkin
Given a portfolio open on the <tab> tab
When the user selects a different scenario from the dropdown
Then the displayed figures update for that scenario
```

### Examples
| tab |
|------|
| Pricing |
| Evolution |

## Assumptions
- Source says only "the scenario choice works"; inferred that selecting a scenario updates the figures shown.

## References
- Source manual case in Notion (see `source`).
