---
title: Muting a risk removes it from aggregation

mode: manual
oracle: intentional
status: draft
priority: medium

tags: [regression, portfolio, risk]
source: "Notion: Portfolio Review / Risks / Muting single risks (src 27)"
refs: []

---

## Objective
Prove a muted risk is no longer counted in the aggregation, from both the portfolio Risks tab and the Risks page.

## Preconditions
- A risk that contributes to an aggregation exists.

## Scenario: muting excludes the risk
```gherkin
Given a risk that contributes to an aggregation
When the user mutes it from the portfolio Risks tab
Then it is no longer considered in the aggregation
And the same holds when muting from the Risks page
```

## References
- Source manual case in Notion (see `source`).
