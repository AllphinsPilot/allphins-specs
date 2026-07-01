---
title: The portfolio list renders

mode: manual
oracle: characterization
status: active
priority: low

tags: [regression, book]
source: "Notion: Book / Portfolio list / Display (src 15)"
refs: []

---

## Objective
Catch accidental breakage of the portfolio-list layout. This is a regression tripwire, not a correctness claim: the original check was a human judging that the display looked right, so there is no asserted expected value.

## Preconditions
- At least one portfolio exists for the active group.

## Scenario: portfolio list matches the accepted baseline
```gherkin
Given the Book page is open
When the portfolio list is displayed
Then the rendered list matches the accepted visual/structural baseline
```

## Assumptions
- No correctness oracle exists in the source ("no scrolling bar, display nice"). Handled as characterization: the test asserts only that the output has not changed from an approved baseline, and a human re-approves the baseline when a change is intended.

## References
- Source manual case in Notion (see `source`).
