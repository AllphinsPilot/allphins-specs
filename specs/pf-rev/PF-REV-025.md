---
title: Expand on a risk popup

mode: manual
oracle: intentional
status: draft
priority: low

tags: [regression, portfolio, risk, energy]
source: "Notion: Portfolio Review / Risks / Expand risk popup (src 41, 104)"
refs: []

---

## Objective
Prove Expand opens the risk as a full page with a map for geolocated Energy risks, and that Expand is available only for Excel risks, not EDM ones.

## Preconditions
- A portfolio with both Excel and EDM risks, including a geolocated Energy risk, exists.

## Scenario: expand opens a full page with a map for Energy
```gherkin
Given a geolocated Energy risk
When the user clicks Expand
Then the risk edit popup is shown as a page
And a map is shown
```

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
