# Portfolio artifact catalog

Weekly titles follow [PORTFOLIO_PLAN.md](PORTFOLIO_PLAN.md). Paths in backticks may be **planned**, not existing files. Markdown is the source; reports, screenshots, PDFs, and traces are execution or release evidence only after review.

Current baseline: document scaffolding exists; no application executions are recorded. A document template does not complete its milestone. All weekly outcomes remain Planned or In progress until their acceptance evidence exists.

| Week | Milestone | Deliverables | Acceptance evidence | Outcome maturity |
| ---: | --- | --- | --- | --- |
| 1 | Week 01 - Risk Analysis and Priority Test Design | `docs/manual-testing/Test_Strategy_SauceDemo.md`; `docs/manual-testing/Test_Cases_Matrix.md`; dated execution records | Risk matrix, reviewed traceability table, and two manual execution records. | In progress — draft documents only |
| 2 | Week 02 - First Working Vertical Slice | `package.json`; lockfile; `playwright.config.js`; `tests/e2e/auth.spec.js`; `.github/workflows/playwright.yml` | Green workflow URL, local test output, and a short locator rationale in the pull request. | Planned |
| 3 | Week 03 - Exploratory Testing and Defect Evidence | `docs/manual-testing/Exploratory_Sessions.md`; `docs/manual-testing/Bug_Reports.md`; reviewed screenshots | Session records and reproducible defect reports reviewed for clarity. | In progress — draft documents only |
| 4 | Week 04 - Manual Execution and Release Recommendation | `docs/manual-testing/Test_Execution_Summary.md`; reviewed `QA_Test_Plan_SauceDemo.pdf` | Reviewed summary, result links, and versioned PDF artifact. | In progress — draft documents only |
| 5 | Week 05 - Page Object Model After Working Tests | `pages/LoginPage.js`; `pages/InventoryPage.js`; optional justified shared page object | Before/after review in the pull request and passing authentication tests. | Planned |
| 6 | Week 06 - Fixtures, Test Data, and Negative Authentication | `fixtures/test-fixtures.js`; `test-data/users.json`; expanded auth tests | Fixture review and passing authentication suite. | Planned |
| 7 | Week 07 - Inventory, Cart, and Checkout Journey | `pages/CartPage.js`; `pages/CheckoutPage.js`; `tests/e2e/purchase.spec.js`; case mappings | Green CI run and updated traceability links. | Planned |
| 8 | Week 08 - Resilience and Network Behavior | `tests/integration/network-resilience.spec.js`; resilience rationale | Repeated test output and repository search showing no fixed waits. | Planned |
| 9 | Week 09 - Cross-Browser Scope and Stability Review | `docs/automation/Stability_Report.md`; supported-browser configuration | Cross-browser run and stability report with limitations. | Planned |
| 10 | Week 10 - Repository Conventions and CI Hardening | `CONTRIBUTING.md`; lint/format configuration; hardened test workflow | One successful run and one deliberately captured failure artifact. | In progress — draft documents only |
| 11 | Week 11 - Test Reports, Traces, and Evidence Review | `docs/automation/TEST_EVIDENCE_GUIDE.md`; reviewed failure evidence | Artifact links and a documented trace walkthrough. | Planned |
| 12 | Week 12 - Public Report Publishing | `.github/workflows/deploy-report.yml`; verified public report link | Public URL and successful deployment run. | Planned |
| 13 | Week 13 - Reviewer-Friendly README | `README.md`; current setup and evidence links | Review by a mentor or another person unfamiliar with the project. | In progress — draft documents only |
| 14 | Week 14 - Documentation Audit and Release Candidate | `docs/architecture/pom-architecture.png`; release notes and attachments | Published release or pre-release and artifact file list. | Planned |
| 15 | Week 15 - CV and Professional Project Story | `docs/portfolio/CV_Project_Description.md`; `docs/portfolio/Project_Presentation.md`; optional LinkedIn draft | Mentor review and links from each claim to relevant evidence. | In progress — draft documents only |
| 16 | Week 16 - Practice Placement and Employer Outreach | `docs/outreach/Practice_Outreach_Message.md`; `docs/outreach/Outreach_Strategy.md`; private contact tracker | Redacted strategy, message samples, and privately maintained outreach log. | In progress — draft documents only |

## Reusable preparation material

- [Misa IT preparation](docs/portfolio/MISA_IT_PREPARATION.md)
- [Repository reuse and tracking guide](docs/REPOSITORY_TEMPLATE_GUIDE.md)
- [Execution record template](docs/manual-testing/Execution_Record_Template.md)
- [Evidence and release-decision rules](docs/manual-testing/EVIDENCE_STANDARD.md)

## Keep state and evidence separate

Outcome maturity: **Planned → In progress → Verified → Published**, as defined in the plan. A draft file can exist while execution is still Planned. Issue board state: **Todo / Doing / Review / Done / Blocked**. Done requires acceptance evidence and review; a closed issue alone is not proof.

Add a dated run or review link before upgrading maturity. Record the repository commit, browser/OS, command or manual procedure, result, and limitations. Review evidence before publication, and retain selected release evidence beyond temporary CI artifact expiry.
