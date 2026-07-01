---
title: No Terror risks from EDMs only

mode: manual
oracle: intentional
status: active
priority: medium

tags: [regression, portfolio, risk]
source: "Notion: Portfolio Review / Risks / Display (src 14)"
refs: []

---

## Objective

Prove a Terror portfolio with only EDMs uploaded shows no risks.

## Preconditions

- A portfolio with risks exists.

## Scenario: no Terror risks from EDMs only

```gherkin
Given a Terror portfolio where only EDMs are uploaded
When the risk list is displayed
Then no Risks are shown
```

## References

- Source manual case in Notion (see `source`).
