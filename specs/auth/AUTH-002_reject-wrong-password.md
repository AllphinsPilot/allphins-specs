---
title: Sign-in is refused with an incorrect password

mode: manual
oracle: intentional
status: active
priority: medium

tags: [regression, auth]
source: "Notion: Login / Password / Can I login if I forgot my password? (src 1)"
refs: []

---

## Objective
Prove that an incorrect password does not grant access. Guards against authentication being bypassed. Not a test of the reset-password feature.

## Preconditions
- A registered user exists.

## Scenario: an incorrect password is rejected
```gherkin
Given the Allphins login page is open
When the user submits a valid email with an incorrect password
Then sign-in is refused
And the user remains unauthenticated on the login page
```

## Assumptions
- Source describes the action but not the expected outcome. Inferred that an incorrect password is rejected and the user is kept out. Whether a specific error message is shown is unspecified; confirm expected messaging.

## References
- Source manual case in Notion (see `source`).
