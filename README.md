# SauceDemo QA Engineering Portfolio

A 16-week portfolio project for demonstrating practical quality assurance and test automation skills with the SauceDemo e-commerce sandbox.

> **Status:** Planning and repository setup in progress

## What This Portfolio Demonstrates

- Risk-based manual test strategy and release decision-making
- Traceable test case design and exploratory defect reporting
- JavaScript and Playwright end-to-end automation
- Page Object Model and custom fixtures
- Data-driven testing and network interception
- GitHub Actions CI and Playwright reporting
- Evidence-based documentation and professional LIA outreach

## Project Structure

```text
.
|-- .github/                 # Milestones, issue templates, PR process, workflows
|-- docs/
|   |-- architecture/        # POM diagrams and architecture notes
|   |-- manual-testing/      # Test strategy, cases, defects, and summaries
|   |-- outreach/            # LIA contact tracking and message templates
|   `-- portfolio/           # CV, LinkedIn, and trace evidence
|-- pages/                   # Playwright Page Object Model classes
|-- fixtures/                # Custom Playwright fixtures
|-- test-data/               # Non-secret test data
|-- tests/                   # E2E and integration tests
|-- ARTIFACT_CATALOG.md      # Week-to-artifact traceability index
`-- PORTFOLIO_PLAN.md        # Complete English 16-week plan
```

## Roadmap

The work is divided into four phases:

1. **Weeks 1-4:** Manual QA foundation
2. **Weeks 5-9:** Playwright automation
3. **Weeks 10-12:** Git, CI/CD, and reporting
4. **Weeks 13-16:** Portfolio packaging and LIA outreach

See [PORTFOLIO_PLAN.md](PORTFOLIO_PLAN.md) for weekly objectives, acceptance criteria, and evidence requirements. See [ARTIFACT_CATALOG.md](ARTIFACT_CATALOG.md) for the traceability index.

## Local Setup

The executable Playwright framework is introduced during Week 5. Once `package.json` exists, the intended clean-clone workflow is:

```bash
npm ci
npx playwright install
npx playwright test
```

The commands above are intentionally documented as the target workflow until the implementation milestone is complete.

## Reports and Releases

- **CI status:** To be added after Week 11.
- **Live Playwright report:** To be added after Week 12 and verified before publication.
- **Release package:** Planned for `v1.0.0` during Week 14.
- **Manual QA documents:** See [`docs/manual-testing/`](docs/manual-testing/).

No test result, defect, release, or public report is claimed until the corresponding evidence is committed or linked from CI.

## Quality and Collaboration

Contributions follow the guidance in [CONTRIBUTING.md](CONTRIBUTING.md). Work is organized through the 16 weekly milestones listed in [.github/milestones.md](.github/milestones.md), with issue templates for recurring QA, automation, CI/CD, documentation, and outreach work.
