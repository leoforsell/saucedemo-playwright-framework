# SauceDemo QA Engineering Portfolio Plan

## Purpose

This 16-week plan builds a practical, recruiter-ready portfolio for QA engineering and test automation roles. The system under test is the [SauceDemo e-commerce sandbox](https://www.saucedemo.com/). The plan assumes approximately 12 hours of focused work per week.

The portfolio combines manual QA, risk-based testing, JavaScript and Playwright automation, Page Object Model design, CI/CD, reporting, release evidence, and targeted LIA outreach in the Stockholm region.

## Working Principles

- Use risk to decide what to test and automate first.
- Keep exploratory findings separate from assumptions until they are reproduced.
- Prefer accessible, user-facing locators and web-first assertions.
- Keep test data, page objects, test logic, and reporting concerns separate.
- Treat Markdown as the source of truth and generated PDFs, screenshots, traces, and HTML reports as evidence.
- Do not claim a test result, defect, release, or live report until evidence exists in the repository or CI.

## Phase Overview

| Phase | Weeks | Focus | Primary outcome |
| --- | ---: | --- | --- |
| 1 | 1-4 | Manual QA foundation | Test strategy, traceable cases, defects, and release recommendation |
| 2 | 5-9 | Playwright automation | Maintainable JavaScript framework with POM, fixtures, and network testing |
| 3 | 10-12 | Git, CI/CD, and reporting | Reproducible workflows and published test evidence |
| 4 | 13-16 | Portfolio packaging and outreach | Recruiter-ready repository, release package, and LIA outreach |

## Weekly Milestones

### Phase 1: Manual QA Foundation

#### Week 1 - Test Strategy and Risk Analysis

**Objective:** Establish scope, business risks, test levels, and release criteria before writing automation.

**Learning focus:** Testing fundamentals, test activities, risk management, the test pyramid, and automation ROI.

**Work:**

- Execute a manual standard purchase with `standard_user` / `secret_sauce`.
- Identify at least six modules: authentication, inventory, sorting, cart, checkout, order confirmation, and logout.
- Score each risk as probability (1-3) multiplied by business impact (1-3).
- Define in-scope and out-of-scope areas, entry criteria, exit criteria, and assumptions.

**Deliverables:**

- `docs/manual-testing/Test_Strategy_SauceDemo.md`
- GitHub issue linked to `Week 01 - Test Strategy and Risk Analysis`

**Definition of Done:**

- [ ] At least six modules are risk assessed.
- [ ] Every risk has probability, impact, risk score, and mitigation.
- [ ] Entry and exit criteria are explicit.
- [ ] Scope and assumptions are reviewable by another person.

**Acceptance evidence:** Completed risk matrix and a recorded manual purchase flow.

#### Week 2 - Test Case Design and Traceability

**Objective:** Produce a compact, traceable regression set using black-box test design.

**Learning focus:** Equivalence partitioning, boundary value analysis, user stories, and Given/When/Then acceptance criteria.

**Work:**

- Write ten formal test cases with unique IDs.
- Cover login, inventory, sorting, cart additions/removals, checkout, and order completion.
- Include at least two negative or boundary cases.
- Map each case to a user story and risk area.

**Deliverables:**

- `docs/manual-testing/Test_Cases_Matrix.md`

**Definition of Done:**

- [ ] Ten complete test cases are documented.
- [ ] At least two negative or boundary cases are included.
- [ ] Preconditions, data, steps, and expected results are testable.
- [ ] Each case maps to a user story and risk area.

**Acceptance evidence:** Traceability table with no orphaned test cases or user stories.

#### Week 3 - Exploratory Testing and Defect Management

**Objective:** Investigate behavior beyond the happy path and report reproducible defects professionally.

**Learning focus:** Exploratory testing, defect lifecycle, severity versus priority, and evidence-based reporting.

**Work:**

- Run exploratory sessions with `problem_user` and `performance_glitch_user`.
- Monitor browser console and network activity.
- Capture reproducible observations, screenshots, and relevant console excerpts.
- Document three defects only after confirming their actual behavior.

**Deliverables:**

- `docs/manual-testing/Bug_Reports.md`
- `docs/manual-testing/screenshots/`

**Definition of Done:**

- [ ] Exploratory sessions have charters, notes, and time boxes.
- [ ] Three defects have clear reproduction steps.
- [ ] Severity and priority are justified independently.
- [ ] Each defect has expected and actual results plus evidence references.

**Acceptance evidence:** Reproducible defect reports reviewed for clarity and completeness.

#### Week 4 - Test Execution Summary and Release Recommendation

**Objective:** Turn the first three weeks of evidence into a formal release decision.

**Learning focus:** Test monitoring, test completion, reporting, and Go/No-Go decision-making.

**Work:**

- Execute the ten documented cases and record pass, fail, and blocked results.
- Summarize coverage, unresolved defects, residual risk, and limitations.
- Make a Go, No-Go, or Conditional Release recommendation.
- Generate a PDF package only from reviewed Markdown source.

**Deliverables:**

- `docs/manual-testing/Test_Execution_Summary.md`
- `docs/manual-testing/QA_Test_Plan_SauceDemo.pdf` (generated artifact)

**Definition of Done:**

- [ ] All ten cases have an execution status.
- [ ] Defect impact and residual risk are summarized.
- [ ] The release recommendation is explicitly justified.
- [ ] The generated PDF matches the reviewed source documents.

**Acceptance evidence:** Signed execution summary and versioned PDF package.

### Phase 2: Playwright Automation

#### Week 5 - Playwright Project Setup

**Objective:** Establish a reproducible JavaScript test project with cross-browser configuration.

**Work:**

- Initialize Node.js and Playwright.
- Configure Chromium, Firefox, WebKit, and mobile Chrome projects.
- Enable HTML and list reporters, trace-on-first-retry, failure screenshots, and failure video.
- Add formatting, linting, and repository ignore rules.

**Deliverables:** `package.json`, `playwright.config.js`, `.eslintrc.json`, `.prettierrc`

**Definition of Done:**

- [ ] Dependencies install with `npm ci`.
- [ ] All four browser profiles are configured.
- [ ] `npx playwright test` starts without configuration errors.
- [ ] Generated reports and test artifacts are ignored by Git.

**Acceptance evidence:** Clean install log and configuration review.

#### Week 6 - Locator Strategy and Authentication

**Objective:** Build the first stable end-to-end test using accessible locators.

**Work:**

- Use Playwright Codegen for an initial flow, then refactor it.
- Replace brittle generated selectors with `getByRole()` and `getByPlaceholder()`.
- Validate URL and product heading with web-first assertions.

**Deliverables:** `tests/e2e/auth.spec.js`

**Definition of Done:**

- [ ] The authentication test passes in the selected browser.
- [ ] No XPath or CSS-class selectors are needed for the login flow.
- [ ] Assertions wait for observable behavior rather than fixed time.

**Acceptance evidence:** Test output and a reviewed locator rationale.

#### Week 7 - Page Object Model

**Objective:** Separate page interaction details from test intent.

**Work:**

- Implement `BasePage`, `LoginPage`, and `InventoryPage`.
- Encapsulate locators and actions in page objects.
- Refactor authentication coverage to use the page objects.
- Keep business assertions in test files unless they are reusable page state checks.

**Deliverables:** `pages/BasePage.js`, `pages/LoginPage.js`, `pages/InventoryPage.js`

**Definition of Done:**

- [ ] Page objects expose meaningful actions.
- [ ] Tests no longer contain raw login interaction calls.
- [ ] Repeated locator definitions are not duplicated unnecessarily.

**Acceptance evidence:** POM architecture review and passing authentication test.

#### Week 8 - Fixtures and Data-Driven Testing

**Objective:** Remove manual page-object construction and externalize credentials.

**Work:**

- Create custom fixtures with `test.extend()`.
- Move user credentials to JSON test data.
- Add inventory coverage for adding a product to the cart.
- Keep secrets and environment-specific values out of source control.

**Deliverables:** `fixtures/test-fixtures.js`, `test-data/users.json`, `tests/e2e/inventory.spec.js`

**Definition of Done:**

- [ ] Tests consume injected page objects.
- [ ] Credentials are loaded from test data.
- [ ] Inventory coverage verifies the cart badge or cart contents.
- [ ] No test file manually constructs a page object.

**Acceptance evidence:** Fixture usage review and passing inventory test.

#### Week 9 - Assertion Hardening and Network Mocking

**Objective:** Test frontend resilience and remove timing-based flakiness.

**Work:**

- Remove every `waitForTimeout` from source code.
- Intercept product image requests with `page.route()`.
- Verify that the inventory interface remains usable when images fail.
- Review asynchronous assertions for deterministic behavior.

**Deliverables:** `tests/api-integration/network-mock.spec.js`

**Definition of Done:**

- [ ] No fixed waits remain in source code.
- [ ] The network-mocking test passes.
- [ ] The test asserts user-visible stability rather than implementation details.
- [ ] The selected suite passes repeatedly without unexplained variation.

**Acceptance evidence:** Search result showing no fixed waits and test output.

### Phase 3: Git, CI/CD, and Reporting

#### Week 10 - Git Discipline and Repository Conventions

**Objective:** Make project history and collaboration practices easy to understand.

**Work:**

- Add a complete `.gitignore`.
- Document branch naming, pull requests, review expectations, and Conventional Commits.
- Use `main` for releasable work and `develop` for integration.
- Keep commits small enough to review and trace to a milestone.

**Deliverables:** `.gitignore`, `CONTRIBUTING.md`

**Definition of Done:**

- [ ] Generated artifacts and dependencies are ignored.
- [ ] Branch and commit conventions are documented.
- [ ] Pull requests require tests, evidence, and risk notes.

**Acceptance evidence:** Repository hygiene check and sample commit history.

#### Week 11 - GitHub Actions Test Pipeline

**Objective:** Run the full suite automatically on pushes and pull requests.

**Work:**

- Configure an Ubuntu GitHub Actions runner.
- Install Node.js, dependencies, and Playwright browsers.
- Run the suite in headless mode.
- Upload the HTML report and failure artifacts even when tests fail.

**Deliverables:** `.github/workflows/playwright.yml`

**Definition of Done:**

- [ ] Workflow triggers on pushes and pull requests to `main` and `develop`.
- [ ] A failing test makes the workflow fail.
- [ ] Reports are uploaded with `if: always()`.
- [ ] The workflow is understandable without hidden local setup.

**Acceptance evidence:** Successful workflow run and a deliberately captured failure artifact.

#### Week 12 - GitHub Pages Reporting

**Objective:** Publish the latest Playwright HTML report for external review.

**Work:**

- Run tests and continue long enough to publish the report.
- Deploy `playwright-report/` to GitHub Pages.
- Document repository Pages settings and the expected URL.
- Link the report from the README only after it is publicly verified.

**Deliverables:** `.github/workflows/deploy-report.yml`

**Definition of Done:**

- [ ] Deployment runs from the intended branch.
- [ ] The published report loads from a public URL.
- [ ] README links to the verified report.
- [ ] The report does not expose secrets or private data.

**Acceptance evidence:** Public report URL and deployment run.

### Phase 4: Portfolio Packaging and Outreach

#### Week 13 - Portfolio README

**Objective:** Make the repository understandable within a one-minute scan.

**Work:**

- Add purpose, status badges, architecture, quality strategy, and quick start.
- Link to the manual QA package and live report when available.
- Explain what is implemented, what is planned, and where evidence lives.

**Deliverables:** `README.md`

**Definition of Done:**

- [ ] README explains the project and its business value.
- [ ] Setup commands are accurate on a clean clone.
- [ ] Links do not produce 404 responses.
- [ ] Claims are supported by repository or CI evidence.

**Acceptance evidence:** README review by someone unfamiliar with the project.

#### Week 14 - Documentation Polish and Release

**Objective:** Produce a coherent, versioned portfolio release.

**Work:**

- Review document consistency, spelling, structure, and traceability.
- Create the POM architecture diagram.
- Prepare release notes and attach reviewed PDF artifacts.
- Tag the first complete portfolio release as `v1.0.0`.

**Deliverables:** `docs/architecture/pom-architecture.png`, release notes, reviewed PDFs

**Definition of Done:**

- [ ] Architecture diagram matches the implemented structure.
- [ ] Release artifacts are generated from reviewed sources.
- [ ] Release notes identify known limitations and evidence.
- [ ] `v1.0.0` is reproducible from the repository.

**Acceptance evidence:** Published release and artifact checksum or file list.

#### Week 15 - CV, LinkedIn, and Trace Evidence

**Objective:** Turn technical work into concise professional evidence.

**Work:**

- Write a CV-ready project description using concrete outcomes.
- Draft a LinkedIn post explaining the testing approach.
- Capture a Playwright trace showing actions, network requests, and DOM snapshots.
- Avoid unsupported claims about coverage, reliability, or defects.

**Deliverables:** `docs/portfolio/CV_Project_Description.md`, `docs/portfolio/LinkedIn_Post.md`, `docs/portfolio/trace-evidence/`

**Definition of Done:**

- [ ] CV text names the technologies and engineering decisions.
- [ ] LinkedIn draft links to verified project evidence.
- [ ] Trace evidence is anonymized and reviewable.

**Acceptance evidence:** Final drafts and trace screenshots or video.

#### Week 16 - LIA Outreach

**Objective:** Contact relevant QA decision-makers with specific, evidence-based value.

**Work:**

- Research 15 relevant employers in Stockholm, Kista, and Liljeholmen.
- Identify QA Leads, Test Managers, Engineering Managers, and consultancy leads.
- Send at least ten personalized messages.
- Track contact route, date, response, and follow-up date.

**Deliverables:** `docs/outreach/Employer_Contact_List.csv`, `docs/outreach/LIA_Outreach_Message.md`

**Definition of Done:**

- [ ] Fifteen target employers are recorded.
- [ ] Ten messages are personalized and tracked.
- [ ] Follow-up dates are scheduled.
- [ ] No personal data is committed without a legitimate reason and appropriate handling.

**Acceptance evidence:** Redacted contact tracker and message samples.

## Completion Standard

The portfolio is complete when every weekly milestone is closed with its documented artifact, acceptance evidence, review record, and traceable Git history. A polished repository may still contain known limitations, but those limitations must be explicit and tied to a risk or future improvement.
