---
title: Expand opens an Energy risk as a full page with a map

mode: manual
oracle: intentional
status: active
priority: low

tags: [regression, portfolio, risk, energy]
source: "Notion: Portfolio Review / Risks / Expand risk popup (src 41, 104)"
refs: []

---

## Objective

Prove Expand opens a geolocated Energy risk as a full page with a map.

## Preconditions

- A portfolio with both Excel and EDM risks, including a geolocated Energy risk, exists.

## Scenario: expand opens a full page with a map for Energy

```gherkin
Given a geolocated Energy risk
When the user clicks Expand
Then the risk edit popup is shown as a page
And a map is shown
```

## References

- Source manual case in Notion (see `source`).
