---
title: Pricing and Evolution tabs render

mode: manual
oracle: characterization
status: active
priority: low

tags: [regression, portfolio, pricing, evolution]
source: "Notion: Portfolio Review / Pricing & Evolution / Display&Numbers (src 55, 61)"
refs: []

---

## Objective
Catch accidental breakage of the Pricing and Evolution tab layouts. Regression tripwire, not a correctness claim.

## Preconditions
- A portfolio with pricing and evolution data exists.

## Scenario: tab matches the accepted baseline
```gherkin
Given a portfolio open on the <tab> tab
When the tab is displayed
Then the rendered tab matches the accepted baseline
```

### Examples
| tab |
|------|
| Pricing |
| Evolution |

## Assumptions
- Source for both is subjective ("data present, display correct"); handled as characterization against an approved baseline.

## References
- Source manual case in Notion (see `source`).
