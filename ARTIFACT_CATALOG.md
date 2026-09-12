# Portfolio Artifact Catalog

This catalog is the traceability index for the 16-week SauceDemo QA portfolio. Markdown files are authoritative. PDFs, PNGs, screenshots, traces, videos, and HTML reports are generated evidence.

| Week | GitHub milestone | Artifact | Type | Evidence required | Status |
| ---: | --- | --- | --- | --- | --- |
| 1 | Week 01 - Test Strategy and Risk Analysis | `docs/manual-testing/Test_Strategy_SauceDemo.md` | Source document | Risk matrix, scope, entry/exit criteria | Planned |
| 2 | Week 02 - Test Case Design and Traceability | `docs/manual-testing/Test_Cases_Matrix.md` | Source document | Ten cases mapped to user stories and risks | Planned |
| 3 | Week 03 - Exploratory Testing and Defect Management | `docs/manual-testing/Bug_Reports.md` | Source document | Three reproducible reports and evidence references | Planned |
| 3 | Week 03 - Exploratory Testing and Defect Management | `docs/manual-testing/screenshots/` | Evidence directory | Redacted screenshots and console excerpts | Planned |
| 4 | Week 04 - Test Execution Summary and Release Recommendation | `docs/manual-testing/Test_Execution_Summary.md` | Source document | Ten execution statuses and release decision | Planned |
| 4 | Week 04 - Test Execution Summary and Release Recommendation | `docs/manual-testing/QA_Test_Plan_SauceDemo.pdf` | Generated artifact | PDF matches reviewed Markdown sources | Planned |
| 5 | Week 05 - Playwright Project Setup | `package.json` | Configuration | Clean install and dependency verification | Planned |
| 5 | Week 05 - Playwright Project Setup | `playwright.config.js` | Configuration | Four browser projects and reporting settings | Planned |
| 5 | Week 05 - Playwright Project Setup | `.eslintrc.json`, `.prettierrc` | Tooling | Lint and formatting checks | Planned |
| 6 | Week 06 - Locator Strategy and Authentication | `tests/e2e/auth.spec.js` | Automated test | Passing login test and locator review | Planned |
| 7 | Week 07 - Page Object Model | `pages/BasePage.js` | Source code | Shared navigation implementation | Planned |
| 7 | Week 07 - Page Object Model | `pages/LoginPage.js` | Source code | Encapsulated login interactions | Planned |
| 7 | Week 07 - Page Object Model | `pages/InventoryPage.js` | Source code | Encapsulated inventory interactions | Planned |
| 8 | Week 08 - Fixtures and Data-Driven Testing | `fixtures/test-fixtures.js` | Test infrastructure | Injected page objects | Planned |
| 8 | Week 08 - Fixtures and Data-Driven Testing | `test-data/users.json` | Test data | Standard and locked-user scenarios | Planned |
| 8 | Week 08 - Fixtures and Data-Driven Testing | `tests/e2e/inventory.spec.js` | Automated test | Product-to-cart verification | Planned |
| 9 | Week 09 - Assertion Hardening and Network Mocking | `tests/api-integration/network-mock.spec.js` | Automated test | Blocked image requests with stable UI assertions | Planned |
| 10 | Week 10 - Git Discipline and Repository Conventions | `.gitignore` | Repository configuration | No generated artifacts or dependencies tracked | Planned |
| 10 | Week 10 - Git Discipline and Repository Conventions | `CONTRIBUTING.md` | Process document | Branch, commit, PR, and evidence guidance | Planned |
| 11 | Week 11 - GitHub Actions Test Pipeline | `.github/workflows/playwright.yml` | CI workflow | Green run and failure artifact | Planned |
| 12 | Week 12 - GitHub Pages Reporting | `.github/workflows/deploy-report.yml` | Deployment workflow | Verified public HTML report URL | Planned |
| 13 | Week 13 - Portfolio README | `README.md` | Portfolio document | Link and clean-clone review | Planned |
| 14 | Week 14 - Documentation Polish and Release | `docs/architecture/pom-architecture.png` | Architecture diagram | Diagram matches source structure | Planned |
| 14 | Week 14 - Documentation Polish and Release | `v1.0.0` release package | Release artifact | Release notes and reviewed attachments | Planned |
| 15 | Week 15 - CV, LinkedIn, and Trace Evidence | `docs/portfolio/CV_Project_Description.md` | Portfolio copy | Technology and outcome review | Planned |
| 15 | Week 15 - CV, LinkedIn, and Trace Evidence | `docs/portfolio/LinkedIn_Post.md` | Portfolio copy | Evidence-backed public draft | Planned |
| 15 | Week 15 - CV, LinkedIn, and Trace Evidence | `docs/portfolio/trace-evidence/` | Evidence directory | Redacted trace screenshots or video | Planned |
| 16 | Week 16 - LIA Outreach | `docs/outreach/Employer_Contact_List.csv` | Outreach tracker | Fifteen employers and follow-up dates | Planned |
| 16 | Week 16 - LIA Outreach | `docs/outreach/LIA_Outreach_Message.md` | Outreach template | Personalized message samples | Planned |

## Status Rules

- **Planned:** Defined but not started.
- **In progress:** Work exists and is being developed.
- **Ready for review:** Acceptance evidence is attached and awaiting review.
- **Complete:** Reviewed, traceable, and linked to its closed milestone.
- **Blocked:** A dependency or environment issue prevents completion; the reason must be recorded in the related issue.

## Evidence Rules

- Redact credentials, personal contact details, access tokens, and private URLs.
- Link evidence from the related GitHub issue or pull request.
- Record the command, browser, operating system, and date for executable evidence.
- Keep generated reports out of source control unless they are intentionally attached to a release.
