---
title: A risk's portfolio value links to that portfolio

mode: manual
oracle: intentional
status: active
priority: low

tags: [regression, portfolio, risk]
source: "Notion: Portfolio Review / Risks / Portfolio link (src 39)"
refs: []

---

## Objective
Prove the portfolio value in a risk popup navigates to that portfolio.

## Preconditions
- A risk belonging to a portfolio exists.

## Scenario: portfolio link navigates
```gherkin
Given a risk popup
When the user clicks the Portfolio value
Then they land on that portfolio's page
```

## References
- Source manual case in Notion (see `source`).
