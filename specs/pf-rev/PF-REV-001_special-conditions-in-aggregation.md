---
title: Policy special conditions are reflected in aggregation

mode: manual
oracle: intentional
status: active
priority: medium

tags: [regression, portfolio, policy]
source: "Notion: Portfolio Review / Policies tab / Special conditions (src 12)"
refs: []

---

## Objective
Prove that sublimits, exclusions, and filters set on a policy are taken into account in both scenario-list and custom-scenario aggregation.

## Preconditions
- A policy exists in a portfolio that contributes to an aggregation.

## Scenario: special conditions affect the aggregation
```gherkin
Given a policy's expanded popup
When the user sets sublimits, an exclusion, and a filter
Then the special conditions are reflected in the scenario-list aggregation
And they are reflected in the custom-scenario aggregation
```

## References
- Source manual case in Notion (see `source`).
