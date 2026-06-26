---
title: Uploading a second data source adds its risks

mode: manual
oracle: intentional
status: draft
priority: low

tags: [regression, portfolio, risk, datasource]
source: "Notion: Portfolio Review / Risks / Uploading multiple data sources (src 29)"
refs: []

---

## Objective
Prove that uploading an additional data source brings its data into the portfolio.

## Preconditions
- A portfolio with one data source already uploaded exists.

## Scenario: second upload adds data
```gherkin
Given a portfolio with one data source
When the user uploads a second file
Then a data record from the second file is present
```

## References
- Source manual case in Notion (see `source`).
