---
title: A user can reset a forgotten password and sign in with the new one

mode: manual
oracle: intentional
status: draft
priority: medium

tags: [regression, auth]
source: "Notion: Login / Password / Can I reset my password? (src 2)"
refs: []

---

## Objective
Prove the full forgotten-password recovery path works end to end: request, email link, set new password, sign in.

## Preconditions
- A registered user with a known email exists.
- The user is logged out.

## Scenario: reset a forgotten password
```gherkin
Given the login page is open
When the user clicks "Forgot password?" and submits their email
Then they receive an email containing a link to set a new password
When they open the link, set a new password, and validate
Then they are returned to the login page
And they can sign in with the new password
```

## References
- Depends on transactional email delivery; the test environment must be able to receive or intercept the reset email.
- Source manual case in Notion (see `source`).
