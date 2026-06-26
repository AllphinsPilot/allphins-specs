---
title: Portfolio Year filter shows the correct tab membership

mode: manual
oracle: intentional
status: draft
priority: medium

tags: [regression, book]
source: "Notion: Book / Portfolio list / Tabs (src 19)"
refs: []

---

## Objective
Prove that filtering the Book by Year shows exactly the portfolios that belong to that year under the platform's membership rules, including the in-force rule for risk-attaching policies.

## Preconditions
- Portfolios exist with a mix of Years of Account, policy periods, and coverage types (including at least one Risk Attaching policy).

## Scenario: year filter membership
```gherkin
Given the Book page is open
And the Year column is unfiltered by default
When the year <Y> is selected
Then portfolios whose Year of Account is <Y> are shown
And portfolios with policies active within <Y> are shown
And portfolios with no policies at all are shown
And portfolios qualifying under the in-force rule are shown
And no other portfolios are shown
```

### Examples
| Y |
|------|
| a year with matching and non-matching portfolios |

## Scenario: changing a policy's dates moves the portfolio between tabs
```gherkin
Given a portfolio currently visible under a year filter
When a policy's dates are changed so it no longer matches that year
Then the portfolio moves to the appropriate tab
```

## Scenario: a risk-attaching expired policy stays In force while a risk is live
```gherkin
Given a portfolio with an expired Year of Account
And exactly one policy whose Period of Coverage is Risk Attaching with expired dates
When at least one of that policy's Risks has dates valid on the current day
Then the portfolio appears in the "In force" tab
```

## Assumptions
- "Policies active within the chosen year" is read as the policy period overlapping that calendar year. Confirm the exact overlap definition.

## References
- Source manual case in Notion (see `source`).
