# SauceDemo QA Engineering Portfolio

A practical QA portfolio by Leo Forsell: use risk analysis, manual testing, and JavaScript/Playwright automation to explain whether an e-commerce journey works and what remains uncertain.

> **Current status: planning and document templates.** No executable Playwright suite, application test results, CI test run, or public report has been verified in this repository yet. A template is not execution evidence.

## Start here

1. Read the [Misa IT preparation checklist](docs/portfolio/MISA_IT_PREPARATION.md).
2. Follow [Week 1 of the plan](PORTFOLIO_PLAN.md#week-1---risk-analysis-and-priority-test-design): review risks and execute two priority cases.
3. In Week 2, implement successful and invalid login tests and the first Chromium CI run.
4. Use the [artifact catalog](ARTIFACT_CATALOG.md) to find deliverables and their evidence requirements.

## Intended skills and evidence

| Skill | Current material | What will demonstrate it |
| --- | --- | --- |
| Risk-based testing | [Draft strategy](docs/manual-testing/Test_Strategy_SauceDemo.md) | Justified risk priorities and test selection |
| Test design | [Case matrix](docs/manual-testing/Test_Cases_Matrix.md) | Repeatable cases, explicit expectations, and execution records |
| Exploratory testing | [Session template](docs/manual-testing/Exploratory_Sessions.md) | Dated observations and reproduced findings |
| Quality decisions | [Execution summary](docs/manual-testing/Test_Execution_Summary.md) | Results, limitations, and a reasoned release recommendation |
| Automation and CI | Week 2 onward in the plan | Working code, clean-install instructions, and run links |
| Collaboration | [Working agreement](CONTRIBUTING.md) and issue/PR templates | Reviewable changes and responses to feedback |

## Roadmap

- **Weeks 1–4:** Risk assessment, first automated tests and CI, manual evidence.
- **Weeks 5–9:** Page objects, fixtures, purchase journey, resilience, and stability review. Additional browsers are stretch work.
- **Weeks 10–12:** CI hardening, diagnostic evidence, and report publishing.
- **Weeks 13–16:** Portfolio review, release candidate, project story, and practice-placement preparation.

[PORTFOLIO_PLAN.md](PORTFOLIO_PLAN.md) is the source of truth for the 16-week sequence and acceptance criteria. Weeks are adjustable work blocks, not fixed deadlines.

## Repository map

- `docs/manual-testing/`: strategy, case definitions, execution and exploration templates.
- `docs/portfolio/`: preparation checklist, honest project descriptions, and presentation guide.
- `docs/outreach/`: message templates; keep actual contact records privately.
- `.github/`: issue/PR templates and generated milestone manifest.
- `scripts/`: planning tools; preview by default.
- Planned in Week 2: `package.json`, lockfile, `playwright.config.js`, `tests/e2e/auth.spec.js`, and `.github/workflows/playwright.yml`.
- Planned from Week 5: `pages/`, `fixtures/`, and `test-data/` as needed by implemented tests.

## Setup

This is currently a documentation scaffold; there is no runnable application test command yet. To inspect the plan with Python 3.9 or later:

```bash
python3 scripts/portfolio_plan.py --check
python3 scripts/portfolio_plan.py --kind issues
```

Once Week 2 delivers the framework, validate and document the intended clean-checkout workflow:

```bash
npm ci
npx playwright install chromium
npx playwright test --project=chromium
```

Do not treat those future commands as verified today. See the [reuse and GitHub setup guide](docs/REPOSITORY_TEMPLATE_GUIDE.md) for template setup, labels, and existing-issue handling.

## Evidence and limitations

Start with desktop Chromium. SauceDemo is an external demonstration site, so availability and behavior may change independently of this repository. A simulated release recommendation is a learning artifact, not authority to release SauceDemo. Reports and badges will be linked only after actual execution. See [evidence rules](docs/manual-testing/EVIDENCE_STANDARD.md).
