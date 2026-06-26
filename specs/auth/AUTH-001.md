---
title: A user with valid credentials can sign in

mode: manual
oracle: intentional
status: draft
priority: high

tags: [smoke, regression, auth]
source: "Notion: Login / Password / Can I login? (src 0)"
refs: []

---

## Objective
Prove that a registered user with valid credentials can authenticate and reach the application. The most basic availability check for the product.

## Preconditions
- A registered user with a known password exists.

## Scenario: valid credentials grant access
```gherkin
Given the Allphins login page is open
When the user signs in with valid credentials
Then they are authenticated and reach the application
```

## Assumptions
- Source states only "log in to the tool"; the exact post-login landing view is not specified and is assumed to be the authenticated application home. Confirm the expected landing screen.

## References
- Source manual case in Notion (see `source`).
