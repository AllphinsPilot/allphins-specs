---
title: A risk-attaching expired policy stays In force while a risk is live

mode: manual
oracle: intentional
status: active
priority: medium

tags: [regression, book]
source: "Notion: Book / Portfolio list / Tabs (src 19)"
refs: []

---

## Objective

Prove a portfolio with an expired risk-attaching policy stays in the "In force" tab while at least one of its risks is live.

## Preconditions

- Portfolios exist with a mix of Years of Account, policy periods, and coverage types (including at least one Risk Attaching policy).

## Scenario: a risk-attaching expired policy stays In force while a risk is live

```gherkin
Given a portfolio with an expired Year of Account
And exactly one policy whose Period of Coverage is Risk Attaching with expired dates
When at least one of that policy's Risks has dates valid on the current day
Then the portfolio appears in the "In force" tab
```

## References

- Source manual case in Notion (see `source`).
