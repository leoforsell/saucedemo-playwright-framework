# Reusing this QA repository template

This repository provides a reusable documentation scaffold. It is not yet a runnable Playwright starter. GitHub's “Template repository” setting is separate from these files; this change does not enable it or change repository visibility.

## Use it for this project

1. Keep the existing repository and issue history.
2. Use `PORTFOLIO_PLAN.md` for weekly objectives and acceptance criteria; use `ARTIFACT_CATALOG.md` to locate outputs.
3. Start one focused issue or subtask at a time. Use Todo → Doing → Review → Done, with a separate Blocked state and a written next action.
4. Use the PR template for every completed slice. A mentor review is useful; record self-review honestly when working alone.

## Reuse for another project

After reviewing and merging this scaffold, the repository owner can enable **Settings → General → Template repository**, then use GitHub's template creation flow. See [GitHub's template instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository).

In the new repository, replace the author, system under test, links, risk assumptions, test data, and case IDs. Reset all result and evidence fields. Choose a license deliberately if you intend others to reuse your original work; no license grant is added by this scaffold. Copy the workflow structure, not claims about completed testing.

## Tracking scripts

Requires Python 3.9+ for offline previews and a current authenticated GitHub CLI supporting `gh api --paginate --slurp` for creation. The [CLI documentation](https://cli.github.com/manual/gh_api) describes those options. No dependency installation is needed for the Python script. Run its offline safety checks with `python3 -m unittest discover -s scripts/tests -v`. Those mocked tests do not verify live GitHub writes.

```bash
# Offline checks and preview; no GitHub reads or writes
python3 scripts/portfolio_plan.py --check
bash scripts/create-github-milestones.sh
bash scripts/create-weekly-issues.sh

# Refresh the manifest after editing weekly titles/objectives
python3 scripts/portfolio_plan.py --write-manifest

# Explicit creation, only when setting up missing records in the intended repository
bash scripts/create-github-milestones.sh --repo OWNER/REPOSITORY --apply
bash scripts/create-weekly-issues.sh --repo OWNER/REPOSITORY --apply
```

Replace OWNER/REPOSITORY before use. Creation reads all open and closed records, matches by week number, and skips existing weeks. It does not overwrite descriptions, reopen issues, change due dates, or delete anything. Duplicate week records stop the operation. Run one setup process at a time; concurrent creation is not supported. A partial failure can be retried because already-created records are discovered on the next run. Week numbering should remain stable.

Existing records with old titles are reported for manual reconciliation; same-title body changes also require manual review. This preserves comments and user edits. To obtain current acceptance text, run the issues preview and copy the relevant week into the existing issue. This scaffold does not bulk-edit the live board.

## Existing issue migration after merging this plan

Issues #1–#16 were already present at review time. Keep their numbers, comments, assignees, and any work evidence. Update each title/objective/acceptance section to the current week below, and align its existing milestone. Do not create a second set. Check current state before editing because work may have progressed since this document was written.

| Existing issue | Current planned title |
| --- | --- |
| #1 | Week 01: Risk Analysis and Priority Test Design |
| #2 | Week 02: First Working Vertical Slice |
| #3 | Week 03: Exploratory Testing and Defect Evidence |
| #4 | Week 04: Manual Execution and Release Recommendation |
| #5 | Week 05: Page Object Model After Working Tests |
| #6 | Week 06: Fixtures, Test Data, and Negative Authentication |
| #7 | Week 07: Inventory, Cart, and Checkout Journey |
| #8 | Week 08: Resilience and Network Behavior |
| #9 | Week 09: Cross-Browser Scope and Stability Review |
| #10 | Week 10: Repository Conventions and CI Hardening |
| #11 | Week 11: Test Reports, Traces, and Evidence Review |
| #12 | Week 12: Public Report Publishing |
| #13 | Week 13: Reviewer-Friendly README |
| #14 | Week 14: Documentation Audit and Release Candidate |
| #15 | Week 15: CV and Professional Project Story |
| #16 | Week 16: Practice Placement and Employer Outreach |

## Repository settings checklist

- Add labels used by the issue templates if absent: `planning`, `manual-qa`, `automation`, `ci-cd`, `documentation`, `outreach`, `defect`, `testing`, `release`.
- Protect `main` against force pushes and deletion when repository settings permit it. Require actual available checks only after the corresponding workflow exists and has run.
- Avoid a required external reviewer until someone is available; keep a recorded solo review meanwhile.
- Configure test CI in Week 2 with read-only repository permissions, explicit Node/Playwright versions, the lockfile, and uploaded failure evidence. Use ordinary pull-request events, not privileged execution of untrusted code.
- Publishing reports is a later, separately reviewed step. A deployment must identify the test run and commit; it must not present stale results as the current run.

Reference pages checked 2026-09-20. This setup checklist records intended settings, not verified configuration of the live repository.
