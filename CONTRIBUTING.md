# Contributing and Working Agreements

This repository is a portfolio project, but it follows team-oriented engineering practices.

## Branches

- `main` contains reviewed, releasable work.
- Create short-lived branches directly from `main`; a separate `develop` branch is not required.
- Feature branches should use a short descriptive name, such as `feat/week-02-authentication` or `docs/week-01-test-cases`.

## Commits

Use [Conventional Commits](https://www.conventionalcommits.org/) with a focused scope:

```text
feat: add authentication page object
fix: correct checkout assertion
test: cover locked user login
docs: document checkout risk
refactor: extract cart fixture
ci: upload Playwright report
chore: update development tooling
```

Do not include credentials, tokens, personal contact data, or generated local reports in commits.

## Pull Requests

Every pull request should:

- Link to its GitHub issue and weekly milestone.
- Explain the change and the risk it addresses.
- Include the command used for validation and its result.
- Link screenshots, traces, reports, or other evidence when relevant.
- State known limitations or follow-up work.
- Receive review before merging to `main`. For solo work, record a self-review and its limitations; ask a mentor when available. Do not configure a required external approval until a reviewer is available.

Use the repository pull request template to keep the review record consistent.

## Definition of Done

A change is complete when:

- The intended behavior or document is implemented.
- Acceptance criteria are checked.
- Required validation has passed. If blocked, record the reason and keep the related outcome unverified; documenting a blocker does not satisfy an execution criterion.
- Evidence is linked from the issue or pull request.
- Documentation and traceability are updated.
- No secrets or unrelated generated artifacts are added.

## Before requesting review

Run `python3 scripts/portfolio_plan.py --check` after plan changes. Run `python3 scripts/portfolio_plan.py --write-manifest` when weekly titles or objectives change, and update the artifact catalog. For implemented automation, also run the relevant tests and record the exact command and outcome.

## Evidence Handling

Redact credentials, private URLs, tokens, and personal contact information from screenshots and reports. Store generated reports in CI or release artifacts unless they are explicitly part of a versioned release package.

