---
title: Analytics tables populate when a risk exists

mode: manual
oracle: intentional
status: draft
priority: low

tags: [regression, portfolio, analytics, casualty, cyber]
source: "Notion: Portfolio Review / Analytics / Display (src 64)"
refs: []

---

## Objective
Prove the Analytics tables are filled when the portfolio has at least one risk. Relevant only for Casualty and Cyber.

## Preconditions
- A Casualty or Cyber portfolio with at least one entered or uploaded risk exists.

## Scenario: tables fill with a risk
```gherkin
Given a Casualty or Cyber portfolio with at least one risk
When the Analytics tab is displayed
Then its tables are filled
```

## References
- Source manual case in Notion (see `source`).
