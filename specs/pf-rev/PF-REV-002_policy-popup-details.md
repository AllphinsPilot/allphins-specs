---
title: Opening a policy shows its details in a popup

mode: manual
oracle: intentional
status: active
priority: low

tags: [regression, portfolio, policy]
source: "Notion: Portfolio Review / Policies tab / Policy pop-up (src 42)"
refs: []

---

## Objective
Prove that opening a policy shows the correct popup with the same information as its row.

## Preconditions
- A portfolio with at least one policy exists.

## Scenario: opening a policy shows its details
```gherkin
Given a portfolio with a policy
When the user clicks the policy
Then the correct policy popup opens
And it shows the same information as the policy line
```

## References
- Source manual case in Notion (see `source`).
