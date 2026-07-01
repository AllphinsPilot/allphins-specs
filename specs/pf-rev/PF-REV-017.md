---
title: Smart algos produce results matching their definitions

mode: manual
oracle: intentional
status: active
priority: high

tags: [regression, portfolio, risk, energy, cyber, casualty]
source: "Notion: Portfolio Review / Risks / Smart algos (src 33)"
refs: []

---

## Objective
Prove the smart algorithms produce results consistent with their definitions.

## Preconditions
- A portfolio with risks suitable for each algorithm exists.

## Scenario: algos match their definitions
```gherkin
Given a portfolio with applicable risks
When the user applies the <algo>
Then the result matches that algorithm's definition
```

### Examples
| algo |
|------|
| Double-counting (Energy) |
| De-duplication (Cyber/Casualty) |
| Simulating risks (Cyber/Casualty) |

## Assumptions
- The oracle is "matches the algo definition" but the definitions are not in the source. Each algorithm's expected behaviour must be supplied as a companion doc before this can be asserted. Link it in References.

## References
- Source manual case in Notion (see `source`).
