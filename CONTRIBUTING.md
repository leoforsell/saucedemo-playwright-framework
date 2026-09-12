# Contributing and Working Agreements

This repository is a portfolio project, but it follows team-oriented engineering practices.

## Branches

- `main` contains reviewed, releasable work.
- `develop` is used for integration before release.
- Feature branches should use a short descriptive name, such as `feat/week-06-authentication` or `docs/week-02-test-cases`.

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
- Receive review before merging to `main`.

Use the repository pull request template to keep the review record consistent.

## Definition of Done

A change is complete when:

- The intended behavior or document is implemented.
- Acceptance criteria are checked.
- Focused validation has been run, or the reason it could not run is recorded.
- Evidence is linked from the issue or pull request.
- Documentation and traceability are updated.
- No secrets or unrelated generated artifacts are added.

## Evidence Handling

Redact credentials, private URLs, tokens, and personal contact information from screenshots and reports. Store generated reports in CI or release artifacts unless they are explicitly part of a versioned release package.
