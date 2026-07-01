---
title: Download a template

mode: manual
oracle: intentional
status: active
priority: medium

tags: [regression, book, import]
source: "Notion: Book / Portfolio list / Import Portfolio & Policies (src 147-152)"
refs: []

---

## Objective

Prove the import modal offers downloadable xlsx templates — empty and pre-filled with the group's data — each with the expected columns.

## Preconditions

- The user is on the Book page.
- The active group has some existing portfolios and policies (needed for the template-with-data and the edit cases).

## Scenario: download a template

```gherkin
Given the import modal is open
When the user clicks "<cta>"
Then an xlsx template with the expected columns is downloaded
And <rows>
```

### Examples
| cta | rows |
|-----|------|
| Download empty template | the rows are empty |
| Download template with data | each row is a unique portfolio x policy couple |

## Assumptions

- Exact template column set is defined by the downloaded template, not restated here.

## References

- Source manual case in Notion (see `source`).
