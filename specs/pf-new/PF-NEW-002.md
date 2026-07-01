---
title: A portfolio can be renewed

mode: manual
oracle: intentional
status: active
priority: medium

tags: [regression, portfolio, renewal]
source: "Notion: New Portfolio / Portfolio renewal (src 24, src 26)"
refs: []

---

## Objective
Prove that renewing a portfolio produces a renewed portfolio whose policies are carried forward with the correct renewed values, from either entry point.

## Preconditions
- An existing portfolio eligible for renewal exists, with at least one policy.

## Scenario: renew a portfolio
```gherkin
Given an existing portfolio eligible for renewal
When the user triggers renewal from <entry_point>
Then a renewed portfolio is created
And its policies are carried forward with the renewed values
```

### Examples
| entry_point |
|-------------|
| the create-new-portfolio flow |
| the portfolio page |

## Assumptions
- Source says only "renew and double check the renewed values" without stating them. Inferred that renewal copies the portfolio's policies forward with inception and expiry shifted by the renewal term and other terms preserved. The exact set of carried-forward fields and the date-shift logic must be confirmed before this is trusted.

## References
- Source manual case in Notion (see `source`).
