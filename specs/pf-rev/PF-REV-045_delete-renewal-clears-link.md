---
title: Deleting a renewal clears the original's link

mode: manual
oracle: intentional
status: active
priority: medium

tags: [regression, portfolio]
source: "Notion: Portfolio Review / Portfolio - Edit / Delete Portfolio (src 36)"
refs: []

---

## Objective

Prove deleting a renewal portfolio removes the original portfolio's link to it.

## Preconditions

- A portfolio exists; for the second scenario, a renewal portfolio linked to an original exists.

## Scenario: deleting a renewal clears the original's link

```gherkin
Given a renewal portfolio linked to an original
When the renewal portfolio is deleted
Then the original no longer links to it
```

## References

- Source manual case in Notion (see `source`).
