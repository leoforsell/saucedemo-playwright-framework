# SauceDemo QA Engineering Portfolio Plan

## Purpose

This 16-week plan builds an evidence-based portfolio for entry-level QA, software testing, and test automation opportunities. The system under test is the [SauceDemo e-commerce sandbox](https://www.saucedemo.com/). The plan assumes approximately 12 focused hours per week and is designed to be reviewed with an IT mentor, including at Misa IT.

The plan deliberately produces a small working vertical slice early. By the end of Week 2, the repository should contain:

- a prioritized risk assessment;
- at least two executed manual test cases;
- automated successful and unsuccessful login tests;
- a reproducible Playwright setup; and
- a successful GitHub Actions run.

Everything after that point expands, hardens, and explains working evidence. The goal is not to appear finished early; it is to demonstrate steady, traceable progress from risk to test evidence.

## Portfolio Outcomes

By Week 16, a reviewer should be able to verify:

1. **QA analysis:** risks, scope, test strategy, designed cases, exploratory sessions, and a release recommendation.
2. **Automation:** maintainable Playwright tests for authentication, inventory, cart, and checkout behavior.
3. **Engineering workflow:** focused issues, short-lived branches, complete pull requests, reviewable commits, and automated checks.
4. **Test evidence:** CI runs, reports, traces, screenshots, and documented limitations.
5. **Professional communication:** a clear README, an honest project description, a versioned release, and a targeted practice-placement plan.

## Scope and Capacity

Use the following weekly time box as a guide:

| Activity | Target time |
| --- | ---: |
| Plan and focused reading | 1 hour |
| Testing or implementation | 7 hours |
| Documentation and evidence | 2 hours |
| Review, feedback, and buffer | 2 hours |

If work exceeds the weekly time box, finish the core Definition of Done and move stretch work to the backlog. Do not reduce evidence quality to preserve the calendar.

### Core scope

- Desktop Chromium as the first supported browser.
- Authentication, inventory, cart, and checkout as the main user journey.
- Manual QA documentation plus focused Playwright UI automation.
- GitHub Actions and a public, privacy-reviewed report.

### Stretch scope

- Firefox, WebKit, and mobile projects after Chromium is stable.
- Broader accessibility checks.
- API testing with Playwright or Python/`pytest` if mentor support and time allow.
- TypeScript migration after the JavaScript suite is stable.

Stretch work must not block the core portfolio.

## Evidence and Status Rules

Use these labels consistently in the README, issues, and portfolio documents:

| Status | Meaning |
| --- | --- |
| Planned | No implementation or verified artifact exists yet. |
| In progress | Work exists but the Definition of Done is not complete. |
| Verified | The work has been executed, reviewed, and linked to evidence. |
| Published | Verified evidence is available at a stable public URL or release. |

- Do not claim a test result, defect, release, coverage level, framework feature, or live report until the evidence exists.
- Use `Built`, `Implemented`, or `Achieved` only for verified work. Use `Planned`, `Designing`, or `Currently implementing` for future work.
- Keep Markdown source files as the source of truth. Treat PDFs, screenshots, traces, videos, and HTML reports as generated evidence.
- Record limitations and failed experiments; they demonstrate engineering judgment when explained clearly.
- Review screenshots, traces, reports, and logs for credentials or personal data before publishing them.

## GitHub Working Method

Use one lightweight workflow throughout the project:

1. Create or update one focused GitHub issue with acceptance criteria.
2. Create a short-lived branch from `main`, such as `docs/week-01-risk-analysis` or `feat/week-02-auth-tests`.
3. Make small Conventional Commits that describe completed changes.
4. Open a pull request to `main` and complete its checklist.
5. Link validation output and relevant evidence in the pull request.
6. Use `Relates to #N` for partial work. Use `Closes #N` only when the complete issue Definition of Done is satisfied.
7. Merge only after the change is reviewable and required checks pass.

A separate `develop` branch is not required for this solo portfolio. The `main` branch should remain demonstrable, and unfinished work should live on short-lived branches.

## Learning Method

Use just-in-time reading instead of treating reading as a separate course:

1. Read one primary source relevant to the current task.
2. Record up to three ideas in your own words.
3. Apply at least one idea to a SauceDemo artifact or test.
4. Explain the decision in the issue or pull request.

Prefer stable, authoritative sources:

- [ISTQB Foundation Level syllabus](https://istqb.org/certifications/certified-tester-foundation-level) and [ISTQB glossary](https://glossary.istqb.org/)
- [Playwright documentation](https://playwright.dev/docs/intro)
- [MDN Web Docs](https://developer.mozilla.org/)
- [GitHub documentation](https://docs.github.com/)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)

Record the title, URL, and access date only when a source materially influences a deliverable.

## Phase Overview

| Phase | Weeks | Focus | Primary outcome |
| --- | ---: | --- | --- |
| 1 | 1-4 | Risk, first tests, and manual evidence | An early working slice plus a defensible release recommendation |
| 2 | 5-9 | Automation growth and reliability | A maintainable core suite with stable test architecture |
| 3 | 10-12 | Repository quality, CI, and reporting | Reproducible checks and reviewable published evidence |
| 4 | 13-16 | Portfolio packaging and practice outreach | An honest, reviewer-friendly portfolio and targeted next step |

## Weekly Milestones

### Phase 1: Risk, First Tests, and Manual Evidence

#### Week 1 - Risk Analysis and Priority Test Design

**Objective:** Decide what matters most before expanding documentation or automation.

**Learning focus:** Risk-based testing, scope, entry and exit criteria, equivalence partitioning, and boundary value analysis.

**Core work:**

- Execute one standard purchase manually to understand the product.
- Complete the existing risk matrix for authentication, inventory, sorting, cart, checkout, confirmation, and logout.
- Score probability and impact separately on a documented 1-3 scale.
- Review the existing ten test cases and correct their technique labels.
- Ensure at least two cases are genuine negative or boundary scenarios.
- Execute and record the two highest-priority cases.

**Required deliverables:**

- `docs/manual-testing/Test_Strategy_SauceDemo.md`
- `docs/manual-testing/Test_Cases_Matrix.md`

**Definition of Done:**

- [ ] At least six risk areas have probability, impact, score, and mitigation.
- [ ] Scope, assumptions, entry criteria, and exit criteria are explicit.
- [ ] Every test case maps to a risk or user story.
- [ ] Two priority cases have dated execution results and evidence references.
- [ ] Test technique labels match the actual test design.

**Acceptance evidence:** Risk matrix, reviewed traceability table, and two manual execution records.

#### Week 2 - First Working Vertical Slice

**Objective:** Turn the plan into running code and visible CI evidence as early as possible.

**Learning focus:** Node.js project setup, Playwright fundamentals, accessible locators, web-first assertions, and basic CI.

**Core work:**

- Initialize Node.js and Playwright in JavaScript.
- Configure Chromium, the HTML reporter, traces on first retry, and screenshots on failure.
- Automate successful login and rejected invalid login.
- Prefer `getByRole()`, `getByLabel()`, or `getByPlaceholder()` over brittle selectors.
- Add a minimal GitHub Actions workflow using `npm ci` and Chromium.
- Verify the project from a clean install.

**Required deliverables:**

- `package.json` and lockfile
- `playwright.config.js`
- `tests/e2e/auth.spec.js`
- `.github/workflows/playwright.yml`
- `.gitignore`

**Definition of Done:**

- [ ] `npm ci` succeeds from a clean checkout.
- [ ] Both authentication tests pass locally in Chromium.
- [ ] No fixed waits, XPath, or CSS-class selectors are used in the login tests.
- [ ] GitHub Actions completes successfully on the pull request.
- [ ] Reports, dependencies, and generated artifacts are ignored by Git.

**Acceptance evidence:** Green workflow URL, local test output, and a short locator rationale in the pull request.

#### Week 3 - Exploratory Testing and Defect Evidence

**Objective:** Investigate behavior beyond scripted happy paths and produce reproducible findings.

**Learning focus:** Session-based exploratory testing, defect lifecycle, severity versus priority, and evidence quality.

**Core work:**

- Run two time-boxed exploratory sessions using `problem_user` and `performance_glitch_user`.
- Give each session a charter, notes, start/end time, and observed risks.
- Inspect relevant browser console and network behavior.
- Reproduce candidate defects in a clean session before classifying them as defects.
- Document up to three verified defects; keep unconfirmed observations separate.

**Required deliverables:**

- `docs/manual-testing/Exploratory_Sessions.md`
- `docs/manual-testing/Bug_Reports.md`
- `docs/manual-testing/screenshots/`

**Definition of Done:**

- [ ] Two sessions have a charter, time box, notes, and conclusion.
- [ ] Every reported defect has reproducible steps, expected and actual results, environment, severity, priority, and evidence.
- [ ] Severity and priority are justified independently.
- [ ] Observations that cannot be reproduced are not presented as confirmed defects.

**Acceptance evidence:** Session records and reproducible defect reports reviewed for clarity.

#### Week 4 - Manual Execution and Release Recommendation

**Objective:** Use accumulated evidence to make a defensible release decision.

**Learning focus:** Test execution, test completion, residual risk, and Go/No-Go decision-making.

**Core work:**

- Execute all ten documented cases and record pass, fail, or blocked status.
- Link failed cases to verified defect reports.
- Summarize coverage, limitations, unresolved defects, and residual risks.
- Make a Go, No-Go, or Conditional Release recommendation.
- Generate a PDF only after the Markdown sources are reviewed.

**Required deliverables:**

- `docs/manual-testing/Test_Execution_Summary.md`
- `docs/manual-testing/QA_Test_Plan_SauceDemo.pdf`

**Definition of Done:**

- [ ] All ten cases have a dated status and environment.
- [ ] Results can be traced to cases, risks, and defects.
- [ ] The recommendation follows from the evidence and stated exit criteria.
- [ ] The PDF matches the reviewed Markdown source.

**Acceptance evidence:** Reviewed summary, result links, and versioned PDF artifact.

### Phase 2: Automation Growth and Reliability

#### Week 5 - Page Object Model After Working Tests

**Objective:** Improve maintainability without hiding test intent or over-engineering the first suite.

**Learning focus:** Cohesion, coupling, Page Object Model design, and separation of concerns.

**Core work:**

- Review the Week 2 tests and identify actual duplication.
- Implement `LoginPage` and `InventoryPage`; add `BasePage` only if it contains proven shared behavior.
- Move reusable interactions and locators into page objects.
- Keep business assertions visible in test files unless a reusable page-state assertion is justified.
- Refactor both authentication tests without changing their behavior.

**Required deliverables:**

- `pages/LoginPage.js`
- `pages/InventoryPage.js`
- Optional `pages/BasePage.js` with documented justification

**Definition of Done:**

- [ ] Both Week 2 tests still pass locally and in CI.
- [ ] Page-object methods describe user actions rather than low-level clicks.
- [ ] Test intent remains understandable from the spec file.
- [ ] No abstraction exists solely for a hypothetical future need.

**Acceptance evidence:** Before/after review in the pull request and passing authentication tests.

#### Week 6 - Fixtures, Test Data, and Negative Authentication

**Objective:** Make setup reusable and expand meaningful authentication coverage.

**Learning focus:** Fixtures, dependency injection, parameterized tests, and responsible test-data handling.

**Core work:**

- Inject page objects using `test.extend()`.
- Store public SauceDemo user scenarios as clearly documented test data.
- Add coverage for `locked_out_user` and one additional relevant authentication scenario.
- Keep environment-specific secrets out of source control.

**Required deliverables:**

- `fixtures/test-fixtures.js`
- `test-data/users.json`
- Expanded `tests/e2e/auth.spec.js`

**Definition of Done:**

- [ ] Tests consume injected page objects.
- [ ] Test data distinguishes public demo credentials from real secrets.
- [ ] Each negative test asserts the user-visible error or outcome.
- [ ] No test file manually constructs page objects.

**Acceptance evidence:** Fixture review and passing authentication suite.

#### Week 7 - Inventory, Cart, and Checkout Journey

**Objective:** Automate the highest-value e-commerce flow without duplicating every manual case.

**Learning focus:** End-to-end scenario design, state transitions, data selection, and assertion quality.

**Core work:**

- Add page objects only for pages used by implemented tests.
- Automate adding a product, verifying the cart, and completing checkout.
- Add one focused removal or validation scenario.
- Map each automated test to a risk and manual test case.

**Required deliverables:**

- `pages/CartPage.js`
- `pages/CheckoutPage.js`
- `tests/e2e/purchase.spec.js`
- Updated traceability matrix

**Definition of Done:**

- [ ] The purchase journey passes in Chromium locally and in CI.
- [ ] Assertions verify observable outcomes at important state transitions.
- [ ] Automated tests are mapped to risks and manual cases.
- [ ] The suite avoids unnecessary test interdependence.

**Acceptance evidence:** Green CI run and updated traceability links.

#### Week 8 - Resilience and Network Behavior

**Objective:** Demonstrate testing beyond straightforward UI success paths.

**Learning focus:** Network interception, asynchronous behavior, deterministic synchronization, and frontend resilience.

**Core work:**

- Intercept selected product image requests with `page.route()`.
- Verify that core inventory behavior remains usable when images fail.
- Review the suite for fixed waits and timing assumptions.
- Document what the resilience test proves and what it does not prove.

**Required deliverables:**

- `tests/integration/network-resilience.spec.js`
- Short resilience rationale in the relevant issue or documentation

**Definition of Done:**

- [ ] No `waitForTimeout` remains in project test code.
- [ ] The test uses a deterministic route condition.
- [ ] Assertions focus on user-visible behavior.
- [ ] The test passes repeatedly without unexplained variation.

**Acceptance evidence:** Repeated test output and repository search showing no fixed waits.

#### Week 9 - Cross-Browser Scope and Stability Review

**Objective:** Expand browser coverage only after the core Chromium suite is reliable.

**Learning focus:** Browser projects, test isolation, retries, flakiness analysis, and appropriate coverage.

**Core work:**

- Run the core suite in Firefox and WebKit.
- Add mobile Chrome only if the desktop projects are stable within the time box.
- Run the selected suite repeatedly and investigate every inconsistent result.
- Record browser-specific limitations instead of concealing them with retries.

**Required deliverables:**

- Updated `playwright.config.js`
- `docs/automation/Stability_Report.md`

**Definition of Done:**

- [ ] Supported browser projects are documented and justified.
- [ ] Core tests pass in the browsers claimed as verified.
- [ ] Retries do not conceal a known deterministic failure.
- [ ] Any unstable or unsupported project is clearly labeled.

**Acceptance evidence:** Cross-browser run and stability report with limitations.

### Phase 3: Repository Quality, CI, and Reporting

#### Week 10 - Repository Conventions and CI Hardening

**Objective:** Turn the early workflow into a clear, repeatable engineering process.

**Learning focus:** Reviewable Git history, branch strategy, pull request quality, CI design, and artifact retention.

**Core work:**

- Document the `main` plus short-lived branch workflow and Conventional Commits.
- Add or refine linting and formatting scripts.
- Expand CI from the Week 2 baseline to the supported browser scope.
- Upload HTML reports and failure artifacts with `if: always()`.
- Confirm that a failing test fails the workflow.

**Required deliverables:**

- `CONTRIBUTING.md`
- Updated `.github/workflows/playwright.yml`
- Linting and formatting configuration

**Definition of Done:**

- [ ] Branch, commit, PR, and evidence conventions are documented.
- [ ] The PR checklist is completed on the Week 10 pull request.
- [ ] CI fails when tests fail but still uploads diagnostic evidence.
- [ ] A clean checkout can reproduce the documented commands.

**Acceptance evidence:** One successful run and one deliberately captured failure artifact.

#### Week 11 - Test Reports, Traces, and Evidence Review

**Objective:** Make failures understandable to someone who did not run the tests locally.

**Learning focus:** Playwright reporting, Trace Viewer, evidence selection, and privacy review.

**Core work:**

- Verify HTML report generation and CI retention.
- Capture and inspect a trace for a controlled failing test.
- Document how to retrieve and review CI artifacts.
- Remove the controlled failure after preserving safe example evidence.

**Required deliverables:**

- `docs/automation/TEST_EVIDENCE_GUIDE.md`
- Privacy-reviewed trace screenshots or a safe trace artifact

**Definition of Done:**

- [ ] A reviewer can find the relevant run, report, and trace from the guide.
- [ ] The evidence explains the failure without exposing sensitive data.
- [ ] The default branch is green after the controlled exercise.

**Acceptance evidence:** Artifact links and a documented trace walkthrough.

#### Week 12 - Public Report Publishing

**Objective:** Publish verified Playwright results for external review.

**Learning focus:** GitHub Pages, deployment permissions, static artifacts, and public-report safety.

**Core work:**

- Deploy `playwright-report/` through a dedicated GitHub Actions workflow.
- Publish only from the intended branch and event.
- Review the report for credentials, personal data, and broken assets.
- Add the public link only after verifying it in a private browser session.

**Required deliverables:**

- `.github/workflows/deploy-report.yml`
- Verified report link in `README.md`

**Definition of Done:**

- [ ] The deployment succeeds from the documented source.
- [ ] The public URL loads without GitHub authentication.
- [ ] The report contains no secrets or unnecessary personal data.
- [ ] README status accurately distinguishes current results from historical evidence.

**Acceptance evidence:** Public URL and successful deployment run.

### Phase 4: Portfolio Packaging and Practice Outreach

#### Week 13 - Reviewer-Friendly README

**Objective:** Make the repository understandable and honest within a one-minute scan.

**Learning focus:** Technical communication, information architecture, and evidence-backed claims.

**Core work:**

- Explain the business risk, test approach, implemented scope, and current status.
- Add accurate quick-start commands and a concise repository map.
- Link manual evidence, CI, the public report, and known limitations.
- Label planned work separately from verified work.

**Required deliverable:** `README.md`

**Definition of Done:**

- [ ] A new reader can identify purpose, status, tools, and evidence within one minute.
- [ ] Setup commands work from a clean checkout.
- [ ] All links resolve correctly.
- [ ] Every outcome claim points to repository, CI, or release evidence.

**Acceptance evidence:** Review by a mentor or another person unfamiliar with the project.

#### Week 14 - Documentation Audit and Release Candidate

**Objective:** Produce a coherent, reproducible portfolio release candidate.

**Learning focus:** Documentation consistency, release management, semantic versioning, and architecture communication.

**Core work:**

- Audit traceability across risks, cases, defects, automated tests, and results.
- Create an architecture diagram that matches implemented code.
- Review wording for unsupported or outdated claims.
- Prepare release notes with scope, evidence, known limitations, and next steps.
- Create `v1.0.0` only if the core completion standard is met; otherwise use a truthful pre-release such as `v0.9.0`.

**Required deliverables:**

- `docs/architecture/pom-architecture.png`
- Release notes and reviewed generated artifacts

**Definition of Done:**

- [ ] Architecture documentation matches the repository structure.
- [ ] Traceability links have no unexplained gaps.
- [ ] The version accurately reflects project maturity.
- [ ] Release artifacts can be reproduced from a clean checkout.

**Acceptance evidence:** Published release or pre-release and artifact file list.

#### Week 15 - CV and Professional Project Story

**Objective:** Convert verified engineering work into concise, accurate professional evidence.

**Learning focus:** Outcome writing, responsible metrics, portfolio storytelling, and audience adaptation.

**Core work:**

- Rewrite the CV description using only verified technologies and outcomes.
- Draft a short project explanation for interviews and Misa IT discussions.
- Draft an optional LinkedIn post that links to the strongest evidence.
- Remove or qualify unsupported claims about coverage, reliability, defects, or framework completeness.

**Required deliverables:**

- `docs/portfolio/CV_Project_Description.md`
- `docs/portfolio/Project_Presentation.md`
- Optional `docs/portfolio/LinkedIn_Post.md`

**Definition of Done:**

- [ ] Every achievement statement is supported by evidence.
- [ ] Planned improvements are clearly separated from completed outcomes.
- [ ] The spoken project explanation takes approximately 60-90 seconds.
- [ ] The explanation identifies both a strength and a known limitation.

**Acceptance evidence:** Mentor review and links from each claim to relevant evidence.

#### Week 16 - Practice Placement and Employer Outreach

**Objective:** Use the portfolio in a focused search for a practice placement (`praktik`) or supported route toward work.

**Learning focus:** Employer research, professional communication, data minimization, and follow-up planning.

**Core work:**

- Agree with the Misa IT work consultant or mentor on target roles and a realistic outreach method.
- Research 8-12 relevant employers or consultancies in the Stockholm region.
- Prioritize targets that can provide QA, software testing, or test automation tasks and supervision.
- Prepare and send 5-8 personalized messages through appropriate channels.
- Track contact method, date, response, and follow-up without committing unnecessary personal data publicly.

**Required deliverables:**

- A private or access-controlled contact tracker
- `docs/outreach/Practice_Outreach_Message.md`
- Redacted `docs/outreach/Outreach_Strategy.md`

**Definition of Done:**

- [ ] Target roles and employer criteria are agreed with the relevant support person.
- [ ] Each employer has a documented reason for inclusion.
- [ ] Messages connect an employer need to specific verified portfolio evidence.
- [ ] Follow-up dates and ownership are clear.
- [ ] Personal contact data is not committed to the public repository.

**Acceptance evidence:** Redacted strategy, message samples, and privately maintained outreach log.

## Misa IT Review Checkpoints

Use the project to ask for specific support rather than a general review.

| Checkpoint | What to show | What to ask for |
| --- | --- | --- |
| Study visit | This plan, risk matrix, test cases, and current repository status | Whether the project can form part of the individual plan; available Playwright/JavaScript support; use of own laptop and GitHub account |
| End of Week 2 | Two automated login tests and first green CI run | Locator, assertion, and workflow review |
| End of Week 4 | Manual execution summary and release recommendation | Feedback on defect quality, traceability, and QA reasoning |
| End of Week 9 | Core automated journey and stability report | Architecture and reliability review; whether Python/API testing adds useful breadth |
| End of Week 13 | Reviewer-ready README and evidence links | Portfolio gap analysis and practice-placement readiness |
| Week 16 | Release and targeted employer criteria | Coordinated practice outreach and follow-up ownership |

Recommended recurring request:

> Could we do one short weekly review of a specific artifact or pull request, with one or two concrete improvements for the next week?

## Scope-Control Rules

- Prefer one complete, evidenced user journey over many shallow tests.
- Do not automate a scenario solely to increase the test count.
- Do not introduce a page object, fixture, helper, or new tool until current code creates a clear need.
- Keep unsuccessful experiments on a branch or document the lesson; do not leave the default branch broken.
- If a core milestone slips, move stretch work rather than compressing review and evidence.
- Treat mentor feedback as input to the backlog, not an obligation to redesign everything immediately.

## Completion Standard

The core portfolio is complete when:

- the highest-priority manual risks and cases have traceable execution evidence;
- verified defects and the release recommendation are evidence-based;
- the core Playwright journey runs locally and in CI;
- supported browser claims match actual runs;
- reports and failure evidence are reviewable and privacy-checked;
- the README, CV description, architecture documentation, and release describe only implemented work;
- each completed milestone has a linked issue, pull request, validation record, and relevant artifact; and
- known limitations and next steps are explicit.

A polished portfolio does not need to be large or flawless. It needs to make engineering decisions, results, and limitations easy for another person to verify.
