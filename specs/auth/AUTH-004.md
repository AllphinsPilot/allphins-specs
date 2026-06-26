---
title: A user can sign in via SAML SSO

mode: manual
oracle: intentional
status: draft
priority: high

tags: [smoke, regression, auth]
source: "Notion: Login / SSO / Can I login using SSO? (src 103)"
refs: []

---

## Objective
Prove that SSO authentication grants access, since SSO is the primary sign-in path for federated users.

## Preconditions
- A user provisioned for SAML SSO exists.

## Scenario: SSO grants access
```gherkin
Given the Allphins login page is open
When the user authenticates through SAML SSO
Then they are authenticated and reach the application
```

## Assumptions
- Source states only "log in with SAML SSO"; the post-login landing view is assumed to match password sign-in. Confirm the expected landing screen.

## References
- Source manual case in Notion (see `source`).
