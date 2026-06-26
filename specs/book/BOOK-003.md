---
title: Changing a policy's dates moves the portfolio between tabs

mode: manual
oracle: intentional
status: draft
priority: medium

tags: [regression, book]
source: "Notion: Book / Portfolio list / Tabs (src 19)"
refs: []

---

## Objective

Prove that changing a policy's dates so it no longer matches a year moves its portfolio to the appropriate tab.

## Preconditions

- Portfolios exist with a mix of Years of Account, policy periods, and coverage types (including at least one Risk Attaching policy).

## Scenario: changing a policy's dates moves the portfolio between tabs

```gherkin
Given a portfolio currently visible under a year filter
When a policy's dates are changed so it no longer matches that year
Then the portfolio moves to the appropriate tab
```

## References

- Source manual case in Notion (see `source`).
