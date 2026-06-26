---
title: Cancelling discards the import

mode: manual
oracle: intentional
status: draft
priority: medium

tags: [regression, book, import]
source: "Notion: Book / Portfolio list / Import Portfolio & Policies (src 147-152)"
refs: []

---

## Objective

Prove cancelling at the confirmation step discards the import, creating or editing nothing.

## Preconditions

- The user is on the Book page.
- The active group has some existing portfolios and policies (needed for the template-with-data and the edit cases).

## Scenario: cancelling discards the import

```gherkin
Given the "Are you sure?" modal is shown
When the user clicks Cancel
Then the modal closes
And no portfolio or policy is created or edited
```

## References

- Source manual case in Notion (see `source`).
