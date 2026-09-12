# Test Strategy and Risk Analysis: SauceDemo

## Document Control

| Field | Value |
| --- | --- |
| Document status | Draft |
| Owner | Portfolio author |
| System under test | SauceDemo e-commerce sandbox |
| Version | 0.1.0 |
| Last updated | 2026-09-12 |

## 1. Purpose

This strategy defines how the SauceDemo e-commerce flow will be evaluated during the portfolio project. It prioritizes customer-facing risks and establishes the evidence required before automation and release recommendations.

## 2. Scope

### In Scope

- Authentication, including valid and invalid login behavior
- Product inventory display and sorting
- Adding, viewing, and removing cart items
- Checkout form validation
- Order completion and confirmation
- Logout and session behavior
- Browser console and network observations during exploratory testing

### Out of Scope

- Extreme-load and endurance performance testing
- Security penetration testing
- Payment-provider integration testing beyond the simulated SauceDemo flow
- Production infrastructure availability
- Accessibility certification beyond basic locator and usability observations

## 3. Test Approach

Use a risk-based combination of:

- Manual happy-path and negative testing
- Exploratory testing with purpose-built user accounts
- Black-box test design using equivalence classes and boundary values
- Automated end-to-end regression tests with Playwright
- Network interception for selected frontend resilience scenarios
- CI execution across supported browser projects

## 4. Entry Criteria

- SauceDemo is reachable.
- Test credentials are available and approved for the sandbox.
- The test case matrix has been reviewed.
- The intended browser and operating system are recorded.
- A clean test session can be started.

## 5. Exit Criteria

- Ten planned test cases have an execution status.
- Critical and major defects are documented and triaged.
- Residual risk is summarized.
- Required evidence is linked from the execution summary.
- A Go, No-Go, or Conditional Release decision is justified.

## 6. Risk Scoring

Risk score = probability of failure (1-3) multiplied by business impact (1-3).

| Score | Interpretation | Suggested response |
| ---: | --- | --- |
| 1-2 | Low | Test during normal regression |
| 3-4 | Medium | Add focused coverage and monitor |
| 6-9 | High | Prioritize before release and require mitigation |

## 7. Risk Matrix

| ID | Module / Function | Potential failure | Probability (1-3) | Impact (1-3) | Score | Mitigation | Status |
| --- | --- | --- | ---: | ---: | ---: | --- | --- |
| R-01 | Authentication | Valid customers cannot sign in |  |  |  | Positive and negative login tests | Open |
| R-02 | Inventory | Products or prices are displayed incorrectly |  |  |  | Inventory content and sorting checks | Open |
| R-03 | Sorting | Products are ordered incorrectly |  |  |  | Verify all supported sort options | Open |
| R-04 | Cart | Items, quantities, or totals are incorrect |  |  |  | Add, remove, and total verification | Open |
| R-05 | Checkout | Required customer data is accepted incorrectly |  |  |  | Boundary and empty-field validation | Open |
| R-06 | Order confirmation | A completed order has no reliable confirmation |  |  |  | End-to-end confirmation test | Open |
| R-07 | Logout | Session remains active after logout |  |  |  | Logout and back-navigation checks | Open |

## 8. Assumptions and Constraints

- SauceDemo is a sandbox and may change independently of this portfolio.
- Test accounts and test data are non-production values.
- Browser and network conditions can affect exploratory observations.
- Real execution counts and defect IDs will be added only after testing.

## 9. Review Record

| Reviewer | Date | Outcome | Notes |
| --- | --- | --- | --- |
| Pending | Pending | Pending | Review after Week 1 execution |
