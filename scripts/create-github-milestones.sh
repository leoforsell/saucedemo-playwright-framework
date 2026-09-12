#!/usr/bin/env bash
set -euo pipefail

if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI is required: https://cli.github.com/" >&2
  exit 1
fi

if [[ -z "${GH_REPO:-}" ]]; then
  echo "Usage: GH_REPO=owner/saucedemo-playwright-framework $0" >&2
  exit 1
fi

milestones=(
  "Week 01|Test Strategy and Risk Analysis|Define SauceDemo scope, business risks, entry criteria, exit criteria, and mitigation."
  "Week 02|Test Case Design and Traceability|Produce ten traceable test cases using black-box techniques and Gherkin acceptance criteria."
  "Week 03|Exploratory Testing and Defect Management|Run exploratory sessions and document three reproducible defects with evidence."
  "Week 04|Test Execution Summary and Release Recommendation|Execute the manual suite and produce a justified Go/No-Go recommendation."
  "Week 05|Playwright Project Setup|Configure the JavaScript Playwright project, browsers, reporters, and test artifacts."
  "Week 06|Locator Strategy and Authentication|Implement stable locator-based authentication coverage."
  "Week 07|Page Object Model|Introduce reusable page objects and refactor authentication tests."
  "Week 08|Fixtures and Data-Driven Testing|Add custom fixtures, external test data, and inventory coverage."
  "Week 09|Assertion Hardening and Network Mocking|Remove fixed waits and verify UI resilience with network interception."
  "Week 10|Git Discipline and Repository Conventions|Establish repository hygiene, branching, commit, and review conventions."
  "Week 11|GitHub Actions Test Pipeline|Run the test suite in CI and upload reports and failure evidence."
  "Week 12|GitHub Pages Reporting|Publish the latest HTML test report to a verified public URL."
  "Week 13|Portfolio README|Create a recruiter-focused README with accurate setup and evidence links."
  "Week 14|Documentation Polish and Release|Review artifacts, create the architecture diagram, and prepare v1.0.0."
  "Week 15|CV, LinkedIn, and Trace Evidence|Package the project for professional communication with trace evidence."
  "Week 16|LIA Outreach|Research target employers and conduct evidence-based LIA outreach."
)

for entry in "${milestones[@]}"; do
  IFS='|' read -r week title description <<< "$entry"
  full_title="$week - $title"
  echo "Creating: $full_title"
  gh api "repos/$GH_REPO/milestones" \
    --method POST \
    --field title="$full_title" \
    --field description="$description" \
    >/dev/null
done

echo "Created ${#milestones[@]} milestones in $GH_REPO"
