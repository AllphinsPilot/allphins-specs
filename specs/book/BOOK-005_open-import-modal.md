---
title: The import modal opens from the Book page

mode: manual
oracle: intentional
status: active
priority: medium

tags: [regression, book, import]
source: "Notion: Book / Portfolio list / Import Portfolio & Policies (src 147-152)"
refs: []

---

## Objective

Prove the user can open the bulk-import modal from the Book page, with its upload zone, two template-download CTAs, and FAQ link.

## Preconditions

- The user is on the Book page.
- The active group has some existing portfolios and policies (needed for the template-with-data and the edit cases).

## Scenario: open the import modal

```gherkin
Given the Book page is open
When the user opens the "Create Portfolio" menu and selects "Import Portfolio & Policies"
Then a modal opens with one upload zone and two template-download CTAs
And the FAQ link opens in a new tab
```

## References

- Source manual case in Notion (see `source`).
