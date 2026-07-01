---
title: Confirming applies and persists the import

mode: manual
oracle: intentional
status: active
priority: medium

tags: [regression, book, import]
source: "Notion: Book / Portfolio list / Import Portfolio & Policies (src 147-152)"
refs: []

---

## Objective

Prove confirming the import applies the previewed changes, so the created and edited portfolios and policies persist after the page reloads.

## Preconditions

- The user is on the Book page.
- The active group has some existing portfolios and policies (needed for the template-with-data and the edit cases).

## Scenario: confirming applies the import

```gherkin
Given the "Are you sure?" modal is shown
When the user confirms the import
Then the listed portfolios and policies are created or edited
And after reloading the page, their values match the uploaded template
```

## Assumptions

- Source row 152's steps say "click on cancel" but its check describes the applied (confirm) path; the confirm scenario follows the intended behaviour, not the literal step. Confirm this was a copy-paste slip in the source.

## References

- Source manual case in Notion (see `source`).
