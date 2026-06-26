---
title: Meta-attributes fill on match and clear on unmatch

mode: manual
oracle: intentional
status: draft
priority: medium

tags: [regression, portfolio, risk, cyber, casualty, pr]
source: "Notion: Portfolio Review / Risks / Meta-attributes on match (src 25)"
refs: []

---

## Objective
Prove matching an Asset, Insured, or Obligor fills the derived meta-attributes, and removing the match clears them.

## Preconditions
- A risk that can be matched to an Asset, Insured, or Obligor exists.

## Scenario: match fills meta-attributes, unmatch clears them
```gherkin
Given a risk
When the user matches its <entity>
Then the derived meta-attributes are filled accordingly
When the user removes the match and saves
Then the <entity> is unmatched
```

### Examples
| entity |
|--------|
| Asset |
| Insured (Cyber/Casualty/PR) |
| Obligor (PR) |

## Assumptions
- For Asset, the derived fields confirmed in source are Asset group and Country. The exact derived fields for Insured and Obligor are not stated; confirm them.

## References
- Source manual case in Notion (see `source`).
