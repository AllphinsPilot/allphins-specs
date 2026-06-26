---
title: Matching risks from a data source

mode: manual
oracle: intentional
status: draft
priority: medium

tags: [regression, portfolio, risk, datasource]
source: "Notion: Portfolio Review / Risks / Matching (src 37)"
refs: []

---

## Objective
Prove that uploading a data source produces correct matching results for its risks.

## Preconditions
- A data source whose risks should match known assets/insureds/obligors is available.

## Scenario: matching results are correct
```gherkin
Given a data source is uploaded
When matching runs
Then the risks are matched to the correct entities
And their derived meta-attributes are filled
```

## Assumptions
- Source says only "validate matching results" with no criteria. Inferred that correct matching links each risk to its expected entity and fills the derived fields. Confirm what "correct" means per LoB.

## References
- Source manual case in Notion (see `source`).
