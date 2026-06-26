---
title: A portfolio can be deleted

mode: manual
oracle: intentional
status: draft
priority: medium

tags: [regression, portfolio]
source: "Notion: Portfolio Review / Portfolio - Edit / Delete Portfolio (src 36)"
refs: []

---

## Objective
Prove a portfolio is deleted and that deleting a renewal portfolio removes the original's link to it.

## Preconditions
- A portfolio exists; for the second scenario, a renewal portfolio linked to an original exists.

## Scenario: delete a portfolio
```gherkin
Given a portfolio
When the user deletes it
Then the portfolio is deleted
```

## Scenario: deleting a renewal clears the original's link
```gherkin
Given a renewal portfolio linked to an original
When the renewal portfolio is deleted
Then the original no longer links to it
```

## References
- Source manual case in Notion (see `source`).
