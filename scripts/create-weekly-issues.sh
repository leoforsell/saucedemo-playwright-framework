#!/usr/bin/env bash
set -euo pipefail

repo="${GH_REPO:-}"
if [[ -z "$repo" ]]; then
  echo "Usage: GH_REPO=owner/repository $0" >&2
  exit 1
fi

if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI is required: https://cli.github.com/" >&2
  exit 1
fi

create_label() {
  local name="$1"
  local color="$2"
  local description="$3"
  gh label create "$name" --repo "$repo" --color "$color" --description "$description" --force >/dev/null
}

create_label planning 1D76DB "Portfolio planning and milestone work"
create_label manual-qa 0E8A16 "Manual QA and test documentation"
create_label automation B60205 "Playwright automation work"
create_label ci-cd 5319E7 "CI, reporting, and deployment work"
create_label documentation 0075CA "Documentation and portfolio packaging"
create_label outreach FBCA04 "LIA and professional outreach"

entries=(
  "01|Test Strategy and Risk Analysis|Define SauceDemo scope, business risks, entry criteria, exit criteria, and mitigation.|planning,manual-qa|docs/manual-testing/Test_Strategy_SauceDemo.md"
  "02|Test Case Design and Traceability|Produce ten traceable test cases using black-box techniques and Gherkin acceptance criteria.|planning,manual-qa|docs/manual-testing/Test_Cases_Matrix.md"
  "03|Exploratory Testing and Defect Management|Run exploratory sessions and document three reproducible defects with evidence.|manual-qa|docs/manual-testing/Bug_Reports.md"
  "04|Test Execution Summary and Release Recommendation|Execute the manual suite and produce a justified Go or No-Go recommendation.|manual-qa,documentation|docs/manual-testing/Test_Execution_Summary.md"
  "05|Playwright Project Setup|Configure the JavaScript Playwright project, browsers, reporters, and test artifacts.|planning,automation|package.json and playwright.config.js"
  "06|Locator Strategy and Authentication|Implement stable locator-based authentication coverage.|automation|tests/e2e/auth.spec.js"
  "07|Page Object Model|Introduce reusable page objects and refactor authentication tests.|automation|pages/"
  "08|Fixtures and Data-Driven Testing|Add custom fixtures, external test data, and inventory coverage.|automation|fixtures/ and test-data/"
  "09|Assertion Hardening and Network Mocking|Remove fixed waits and verify UI resilience with network interception.|automation|tests/api-integration/network-mock.spec.js"
  "10|Git Discipline and Repository Conventions|Establish repository hygiene, branching, commit, and review conventions.|planning,documentation|CONTRIBUTING.md and .gitignore"
  "11|GitHub Actions Test Pipeline|Run the test suite in CI and upload reports and failure evidence.|ci-cd|.github/workflows/playwright.yml"
  "12|GitHub Pages Reporting|Publish the latest HTML test report to a verified public URL.|ci-cd|.github/workflows/deploy-report.yml"
  "13|Portfolio README|Create a recruiter-focused README with accurate setup and evidence links.|documentation|README.md"
  "14|Documentation Polish and Release|Review artifacts, create the architecture diagram, and prepare v1.0.0.|documentation|docs/architecture/ and release package"
  "15|CV, LinkedIn, and Trace Evidence|Package the project for professional communication with trace evidence.|documentation|docs/portfolio/"
  "16|LIA Outreach|Research target employers and conduct evidence-based LIA outreach.|outreach|docs/outreach/"
)

for entry in "${entries[@]}"; do
  IFS='|' read -r week title objective labels artifact <<< "$entry"
  milestone="Week $week - $title"
  body=$(cat <<EOF
## Objective

$objective

## Milestone

\`$milestone\`

## Planned artifact

\`$artifact\`

## Acceptance criteria

- [ ] Complete the objective described in [PORTFOLIO_PLAN.md](https://github.com/$repo/blob/main/PORTFOLIO_PLAN.md).
- [ ] Update the artifact and evidence in [ARTIFACT_CATALOG.md](https://github.com/$repo/blob/main/ARTIFACT_CATALOG.md).
- [ ] Link validation results, screenshots, traces, reports, or review notes.
- [ ] Update the status and close only after review.
EOF
)
  gh issue create \
    --repo "$repo" \
    --title "Week $week: $title" \
    --body "$body" \
    --milestone "$milestone" \
    --label "$labels"
done
