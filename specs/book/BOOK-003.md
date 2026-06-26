---
title: Portfolios and policies can be imported from a template

mode: manual
oracle: intentional
status: draft
priority: medium

tags: [regression, book, import]
source: "Notion: Book / Portfolio list / Import Portfolio & Policies (src 147-152)"
refs: []

---

## Objective
Prove the bulk import flow works end to end: opening the modal, downloading templates, previewing changes with correct counts, and applying or discarding them.

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

## Scenario: uploading a filled template previews the changes with correct counts
```gherkin
Given a filled template that creates new portfolios and policies, renames an existing portfolio and policy, and modifies coverage and reinstatement
When the user uploads it in the modal
Then an "Are you sure?" modal lists the portfolios and policies that will be created or edited
And the counts of unchanged, edited, and created items are correct
```

## Scenario: cancelling discards the import
```gherkin
Given the "Are you sure?" modal is shown
When the user clicks Cancel
Then the modal closes
And no portfolio or policy is created or edited
```

## Scenario: confirming applies the import
```gherkin
Given the "Are you sure?" modal is shown
When the user confirms the import
Then the listed portfolios and policies are created or edited
And after reloading the page, their values match the uploaded template
```

## Assumptions
- Source row 152's steps say "click on cancel" but its check describes the applied (confirm) path; the confirm scenario follows the intended behaviour, not the literal step. Confirm this was a copy-paste slip in the source.
- Exact template column set is defined by the downloaded template, not restated here.

## References
- Source manual case in Notion (see `source`).
