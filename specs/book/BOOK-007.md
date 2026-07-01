---
title: Uploading a filled template previews the changes with correct counts

mode: manual
oracle: intentional
status: active
priority: medium

tags: [regression, book, import]
source: "Notion: Book / Portfolio list / Import Portfolio & Policies (src 147-152)"
refs: []

---

## Objective

Prove uploading a filled template previews the resulting changes — the portfolios and policies to be created or edited, with correct unchanged/edited/created counts — before anything is applied.

## Preconditions

- The user is on the Book page.
- The active group has some existing portfolios and policies (needed for the template-with-data and the edit cases).

## Scenario: uploading a filled template previews the changes with correct counts

```gherkin
Given a filled template that creates new portfolios and policies, renames an existing portfolio and policy, and modifies coverage and reinstatement
When the user uploads it in the modal
Then an "Are you sure?" modal lists the portfolios and policies that will be created or edited
And the counts of unchanged, edited, and created items are correct
```

## References

- Source manual case in Notion (see `source`).
