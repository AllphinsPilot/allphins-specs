---
title: Expand availability by source

mode: manual
oracle: intentional
status: active
priority: low

tags: [regression, portfolio, risk, energy]
source: "Notion: Portfolio Review / Risks / Expand risk popup (src 41, 104)"
refs: []

---

## Objective

Prove Expand is available for Excel-sourced risks and unavailable for EDM-sourced risks.

## Preconditions

- A portfolio with both Excel and EDM risks, including a geolocated Energy risk, exists.

## Scenario: expand availability by source

```gherkin
Given a risk
When the user opens it
Then the Expand option is <state>
```

### Examples
| risk source | state |
|-------------|-------|
| EDM | not present |
| Excel | present |

## References

- Source manual case in Notion (see `source`).
