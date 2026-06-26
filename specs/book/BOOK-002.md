---
title: Year filter membership

mode: manual
oracle: intentional
status: draft
priority: medium

tags: [regression, book]
source: "Notion: Book / Portfolio list / Tabs (src 19)"
refs: []

---

## Objective

Prove the Book Year filter shows exactly the portfolios belonging to the selected year under the platform's membership rules, including the in-force rule for risk-attaching policies.

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

## Assumptions

- "Policies active within the chosen year" is read as the policy period overlapping that calendar year. Confirm the exact overlap definition.

## References

- Source manual case in Notion (see `source`).
