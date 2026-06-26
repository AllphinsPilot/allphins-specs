---
title: Create several policies in quick succession

mode: manual
oracle: intentional
status: draft
priority: high

tags: [smoke, regression, portfolio]
source: "Notion: New Portfolio / Create a single policy (src 30); Create multiple policies (src 32)"
refs: []

---

## Objective

Prove creating several policies in quick succession persists all of them.

## Preconditions

- A portfolio is open.

## Scenario: create several policies in quick succession

```gherkin
Given a portfolio is open
When the user creates several policies in quick succession
Then all of them are saved
```

## References

- Source manual case in Notion (see `source`).
