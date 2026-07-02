---
title: The Policies tab matches its accepted baseline

mode: manual
oracle: characterization
status: active
priority: low

tags: [regression, portfolio, policy]
source: "Notion: Portfolio Review / Policies tab / Display (src 40)"
refs: []

---

## Objective
Catch accidental breakage of the policies-tab layout. Regression tripwire, not a correctness claim.

## Preconditions
- A portfolio with policies exists.

## Scenario: policies tab matches the accepted baseline
```gherkin
Given a portfolio is open on the Policies tab
When the tab is displayed
Then the rendered tab matches the accepted baseline
```

## Assumptions
- No correctness oracle in source ("good display, no scroll"). Handled as characterization against an approved baseline.

## References
- Source manual case in Notion (see `source`).
