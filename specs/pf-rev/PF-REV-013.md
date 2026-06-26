---
title: Risk list shows the right columns and risks

mode: manual
oracle: intentional
status: draft
priority: medium

tags: [regression, portfolio, risk]
source: "Notion: Portfolio Review / Risks / Display (src 14)"
refs: []

---

## Objective
Prove the risk list shows columns matching the portfolio's risk class, and shows no Risks for Terror when only EDMs are uploaded.

## Preconditions
- A portfolio with risks exists.

## Scenario: columns match the risk class
```gherkin
Given a portfolio open on the Risks tab
When the risk list is displayed
Then the columns correspond to the portfolio's risk class
```

## Scenario: no Terror risks from EDMs only
```gherkin
Given a Terror portfolio where only EDMs are uploaded
When the risk list is displayed
Then no Risks are shown
```

## Assumptions
- The subjective "display okay / no scroll" part of the source is dropped; only the two assertable rules are kept.

## References
- Source manual case in Notion (see `source`).
