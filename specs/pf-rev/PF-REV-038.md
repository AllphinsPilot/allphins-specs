---
title: Columns match the risk class

mode: manual
oracle: intentional
status: active
priority: medium

tags: [regression, portfolio, risk]
source: "Notion: Portfolio Review / Risks / Display (src 14)"
refs: []

---

## Objective

Prove the risk list shows columns matching the portfolio's risk class.

## Preconditions

- A portfolio with risks exists.

## Scenario: columns match the risk class

```gherkin
Given a portfolio open on the Risks tab
When the risk list is displayed
Then the columns correspond to the portfolio's risk class
```

## Assumptions

- The subjective "display okay / no scroll" part of the source is dropped; only the assertable column rule is kept.

## References

- Source manual case in Notion (see `source`).
