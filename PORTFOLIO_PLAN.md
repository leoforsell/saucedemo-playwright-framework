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

## How to Use the Reading Guides

Each week combines a small amount of reading with hands-on work. Read the suggested material before starting the week's implementation, apply the ideas to SauceDemo, and record a short reflection in the related artifact or issue. The goal is not to finish a large reading list; it is to explain which principle you applied and show evidence of the result.

For each week:

1. Read the primary source and skim the optional source if time permits.
2. Write down three principles, terms, or techniques in your own words.
3. Apply at least one principle to the week's SauceDemo task.
4. Check the learning outcome before marking the week complete.

Use stable, authoritative sources where possible: the [ISTQB glossary](https://glossary.istqb.org/), [ISTQB Foundation Level syllabus](https://istqb.org/certifications/certified-tester-foundation-level), [Test Automation University](https://testautomationu.applitools.com/), [MDN Web Docs](https://developer.mozilla.org/), [Playwright documentation](https://playwright.dev/docs/intro), and official GitHub documentation. Record the title, URL, and access date for sources that materially influenced a deliverable.

### Test Automation University Path

Test Automation University (TAU) is a free, course-based complement to the reference reading. Do not complete every TAU course before progressing. Select the course listed for the current milestone, complete only the modules needed for that week's work, and apply the result to SauceDemo. The suggested sequence is:

1. [Setting a Foundation for Successful Test Automation](https://testautomationu.applitools.com/setting-a-foundation-for-successful-test-automation/) - automation strategy, maintainability, and return on investment.
2. [Introduction to JavaScript](https://testautomationu.applitools.com/javascript-tutorial/) - the language fundamentals needed for the Playwright project.
3. [TAU course catalog](https://testautomationu.applitools.com/) - select the current Playwright, API, CI/CD, or supporting course when the relevant implementation week begins.

TAU course availability and URLs can change. If a course moves, use the catalog to locate its current page and record the actual course completed.

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

**Reading guide:**

- Primary: ISTQB Foundation Level syllabus sections on testing fundamentals, test activities, and risk-based testing.
- Reference: ISTQB glossary entries for *risk*, *risk-based testing*, *test strategy*, *entry criteria*, and *exit criteria*.
- TAU: Complete the relevant modules from [Setting a Foundation for Successful Test Automation](https://testautomationu.applitools.com/setting-a-foundation-for-successful-test-automation/) on automation strategy and ROI.
- Apply: Compare the business impact of a failed checkout with a failed product sort and use the comparison to justify the risk matrix.
- Learning check: Explain why probability and impact are scored separately and when testing may start or stop.

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

**Reading guide:**

- Primary: ISTQB Foundation Level syllabus sections on test techniques and test analysis.
- Reference: Martin Fowler's [Specification by Example](https://martinfowler.com/bliki/SpecificationByExample.html) overview and the [Cucumber Gherkin reference](https://cucumber.io/docs/gherkin/reference).
- Apply: Derive partitions and boundaries for login, cart quantity, and checkout fields before writing the ten cases.
- Learning check: Justify why every test case exists, which risk it covers, and which partition or boundary it represents.

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

**Reading guide:**

- Primary: ISTQB Foundation Level syllabus sections on defect management and experience-based testing.
- Reference: James Bach's [Exploratory Testing Explained](https://www.satisfice.com/articles/et-article) and Atlassian's [bug report guidance](https://www.atlassian.com/software/jira/guides/bug-reporting).
- Apply: Create a time-boxed charter for each exploratory session and separate observations from confirmed defects.
- Learning check: Explain the difference between severity and priority and reproduce one finding from a clean session record.

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

**Reading guide:**

- Primary: ISTQB Foundation Level syllabus sections on test monitoring, control, completion, and reporting.
- Reference: ISTQB glossary entries for *residual risk*, *release decision*, and *test summary report*.
- Apply: Use the ten execution results and unresolved risks to make a justified Go, No-Go, or Conditional Release recommendation.
- Learning check: Defend the release recommendation using evidence, coverage, known defects, and residual risk rather than intuition.

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

**Learning focus:** Node.js project structure, Playwright configuration, browser projects, reporters, and reproducible setup.

**Reading guide:**

- Primary: Playwright documentation on [installation](https://playwright.dev/docs/intro) and [test configuration](https://playwright.dev/docs/test-configuration).
- Reference: npm documentation on [package.json](https://docs.npmjs.com/cli/v10/configuring-npm/package-json) and Playwright's [reporters](https://playwright.dev/docs/test-reporters).
- TAU: Complete the relevant modules from [Introduction to JavaScript](https://testautomationu.applitools.com/javascript-tutorial/) on variables, functions, objects, arrays, modules, and asynchronous JavaScript.
- Apply: Explain what each configuration option protects against and verify the project from a clean install.
- Learning check: Describe the purpose of each browser project, reporter, and failure artifact setting.

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

**Learning focus:** Accessible locators, web-first assertions, actionability, and authentication flows.

**Reading guide:**

- Primary: Playwright documentation on [locators](https://playwright.dev/docs/locators), [writing tests](https://playwright.dev/docs/writing-tests), and [actionability](https://playwright.dev/docs/actionability).
- Reference: MDN guidance on [accessible names](https://developer.mozilla.org/en-US/docs/Glossary/Accessible_name) and [web forms](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms).
- TAU: Use the [TAU course catalog](https://testautomationu.applitools.com/) to select the current Playwright or browser-automation course, completing only the locator and first-test modules relevant to this milestone.
- Apply: Replace generated selectors with role- and label-based locators and assert observable page behavior.
- Learning check: Explain why a chosen locator is resilient and why a web-first assertion is preferable to a fixed delay.

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

**Learning focus:** Page Object Model design, cohesion, coupling, and separation of test intent from UI mechanics.

**Reading guide:**

- Primary: Playwright documentation on [page object models](https://playwright.dev/docs/pom).
- Reference: Martin Fowler's [PageObject](https://martinfowler.com/bliki/PageObject.html) and the [single-responsibility principle](https://www.oodesign.com/single-responsibility-principle).
- TAU: Use the [TAU course catalog](https://testautomationu.applitools.com/) to select the current Playwright or test-automation design course and compare its page-object examples with this project's structure.
- Apply: Move login and inventory interactions into page objects while keeping business assertions in the tests.
- Learning check: Identify which responsibility belongs in a page object, fixture, or test and explain why.

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

**Learning focus:** Fixtures, dependency injection, test-data design, and safe handling of credentials.

**Reading guide:**

- Primary: Playwright documentation on [fixtures](https://playwright.dev/docs/test-fixtures) and [parameterized tests](https://playwright.dev/docs/test-parameterize).
- Reference: OWASP [Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html).
- TAU: Use the [TAU course catalog](https://testautomationu.applitools.com/) to select the current course covering test data, fixtures, or data-driven automation.
- Apply: Inject page objects through a custom fixture and load non-secret user scenarios from test data.
- Learning check: Explain the fixture lifecycle and demonstrate that no secret or environment-specific credential is hard-coded in a test.

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

**Learning focus:** Assertion design, asynchronous behavior, network interception, and frontend resilience.

**Reading guide:**

- Primary: Playwright documentation on [network](https://playwright.dev/docs/network), [mock APIs](https://playwright.dev/docs/mock), and [auto-waiting](https://playwright.dev/docs/actionability).
- Reference: Martin Fowler's [Eradicating Non-Determinism in Tests](https://martinfowler.com/articles/nonDeterminism.html).
- TAU: Use the [TAU course catalog](https://testautomationu.applitools.com/) to select the current course covering API or network testing when this milestone is reached.
- Apply: Block product image requests and assert that inventory remains usable without using `waitForTimeout`.
- Learning check: Distinguish a deterministic synchronization point from a timing guess and explain what user-visible behavior the test protects.

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

**Learning focus:** Git history, branching strategy, Conventional Commits, pull request review, and repository hygiene.

**Reading guide:**

- Primary: [Pro Git](https://git-scm.com/book/en/v2) chapters on Git basics and branching.
- Reference: [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) and GitHub's [pull request review documentation](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests).
- Apply: Review the repository as a new contributor and verify that ignored files, branch names, commits, and PR evidence follow the documented conventions.
- Learning check: Explain what makes a commit reviewable and how a pull request connects code, risk, validation, and evidence.

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

**Learning focus:** CI workflow design, reproducible environments, artifact retention, and failure visibility.

**Reading guide:**

- Primary: GitHub Actions documentation on [workflow syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions) and [storing workflow data as artifacts](https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts).
- Reference: Playwright's [continuous integration guide](https://playwright.dev/docs/ci).
- TAU: Use the [TAU course catalog](https://testautomationu.applitools.com/) to select the current CI/CD course and map its pipeline concepts to this workflow.
- Apply: Trace every workflow step from checkout through browser installation, test execution, and artifact upload.
- Learning check: Explain why failures must fail the job while reports and failure evidence still upload with `if: always()`.

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

**Learning focus:** Static-site deployment, artifact publishing, permissions, and public report safety.

**Reading guide:**

- Primary: GitHub Pages documentation on [publishing with GitHub Actions](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).
- Reference: Playwright documentation on the [HTML report](https://playwright.dev/docs/test-reporters).
- Apply: Follow a report from test output to the deployed Pages URL and check it for secrets, private data, and broken links.
- Learning check: Explain the deployment trigger, required permissions, published artifact, and how you verified the public URL.

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

**Learning focus:** Technical communication, information architecture, concise documentation, and evidence-backed claims.

**Reading guide:**

- Primary: GitHub's [README guidance](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories) and documentation style recommendations.
- Reference: Write the Docs' [documentation guide](https://www.writethedocs.org/guide/).
- Apply: Ask whether a new reader can understand the purpose, setup, current status, architecture, and evidence within one minute.
- Learning check: Identify every externally verifiable claim in the README and point to its repository or CI evidence.

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

**Learning focus:** Documentation review, release management, reproducibility, and technical diagrams.

**Reading guide:**

- Primary: GitHub documentation on [release management](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases) and [semantic versioning](https://semver.org/).
- Reference: C4 model guidance on [software architecture diagrams](https://c4model.com/diagrams).
- Apply: Compare the architecture diagram, source tree, release notes, and generated artifacts for consistency.
- Learning check: Reproduce the release package from a clean checkout and explain what the version communicates.

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

**Learning focus:** Professional technical writing, portfolio storytelling, trace analysis, and responsible evidence sharing.

**Reading guide:**

- Primary: Playwright documentation on [Trace Viewer](https://playwright.dev/docs/trace-viewer).
- Reference: GitHub's [writing on GitHub](https://docs.github.com/en/get-started/writing-on-github) and OWASP guidance on [data protection](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html).
- Apply: Turn one verified trace and one repository outcome into concise CV and LinkedIn language without overstating coverage or reliability.
- Learning check: Distinguish a measurable project outcome from a claim that still needs evidence, and redact sensitive trace content.

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

**Learning focus:** Employer research, professional communication, data minimization, and follow-up planning.

**Reading guide:**

- Primary: Swedish Authority for Privacy Protection (IMY) guidance on [personal data](https://www.imy.se/en/organisations/data-protection/).
- Reference: Harvard Business Review's [networking message guidance](https://hbr.org/2016/11/how-to-write-a-networking-email-that-gets-a-response) and the target employers' own careers pages.
- Apply: Build a research-backed contact list and write messages that connect a specific employer need to verified portfolio evidence.
- Learning check: Explain why each target is relevant, what data-minimization considerations apply, and when to follow up.

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
