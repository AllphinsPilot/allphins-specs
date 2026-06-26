---
title: Pricing and Evolution can compare two portfolios

mode: manual
oracle: intentional
status: draft
priority: low

tags: [regression, portfolio, pricing, evolution]
source: "Notion: Portfolio Review / Pricing & Evolution / Comparison (src 59, 63)"
refs: []

---

## Objective
Prove the comparison view shows both portfolios side by side.

## Preconditions
- Two portfolios with pricing and evolution data exist.

## Scenario: compare two portfolios
```gherkin
Given the <tab> tab
When the user compares two portfolios
Then the tab shows both portfolios' figures together
```

### Examples
| tab |
|------|
| Pricing |
| Evolution |

## Assumptions
- Source says only "compare two portfolios" with no outcome; inferred a side-by-side comparison view.

## References
- Source manual case in Notion (see `source`).
