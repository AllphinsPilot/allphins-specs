---
title: Policy labels can be managed

mode: manual
oracle: intentional
status: active
priority: low

tags: [regression, portfolio, policy]
source: "Notion: Portfolio Review / Policies tab / Policy labels (src 44)"
refs: []

---

## Objective
Prove labels can be added, recoloured, unselected, and deleted, with changes persisting across reopening the policy drawer.

## Preconditions
- A portfolio with a policy exists.

## Scenario: manage labels
```gherkin
Given a policy drawer is open
When the user adds several labels and creates a new one
Then the new labels are saved
When the user changes a label's colour
Then the colour change is saved
When the user unselects a label and reopens the drawer
Then that label is absent
```

## References
- Source manual case in Notion (see `source`).
