---
title: A new portfolio can be created and a policy added to it

mode: manual
oracle: intentional
status: active
priority: high

tags: [smoke, regression, portfolio]
source: "Notion: New Portfolio / Create a Portfolio (src 22)"
refs: []

---

## Objective
Prove a user can create an empty portfolio and that a policy added to it propagates to the places that should reflect it.

## Preconditions
- The user is on the Book page.

## Scenario: create an empty portfolio then add a policy
```gherkin
Given the Book page is open
When the user creates a new portfolio with a name and a client
Then a new portfolio is created with no policies and no SOV
When the user creates a policy in that portfolio
Then the policy is present in the portfolio
And it appears in the Book list, the aggregation filters, and the risk-page filter
```

## References
- Source manual case in Notion (see `source`).
