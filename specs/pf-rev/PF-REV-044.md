---
title: Delete a portfolio

mode: manual
oracle: intentional
status: active
priority: medium

tags: [regression, portfolio]
source: "Notion: Portfolio Review / Portfolio - Edit / Delete Portfolio (src 36)"
refs: []

---

## Objective

Prove a portfolio can be deleted.

## Preconditions

- A portfolio exists; for the second scenario, a renewal portfolio linked to an original exists.

## Scenario: delete a portfolio

```gherkin
Given a portfolio
When the user deletes it
Then the portfolio is deleted
```

## References

- Source manual case in Notion (see `source`).
