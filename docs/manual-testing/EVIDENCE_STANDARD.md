# Evidence and decision standard

## Traceability

Use `risk → user story → test case → execution record → defect (if observed) → summary`. Add a spec path and exact test title when automation exists. A planned path is not a result. User stories in this portfolio are proposed test oracles, not an official SauceDemo specification; resolve uncertain expectations before classifying a defect.

## Record each execution

- Unique run ID, date/time with timezone, tester, repository commit, target URL.
- Browser/version, OS, account scenario, and relevant network conditions. Record the application version if visible; otherwise say “not exposed”.
- Preconditions and clean-session/reset method.
- Case ID, actual result, Pass / Fail / Blocked / Not run, and evidence path or run URL.
- Link a reproduced failure to a defect; distinguish an application failure from an environment or automation failure.
- Keep prior runs immutable and append retests. The summary identifies the selected cycle and latest applicable result per case.

`Pass` means all expected checks were observed. `Fail` means a check was performed and differed from the expected result. `Blocked` means execution could not reach a meaningful verdict. `Not run` means no attempt. Blocked and Not run are never passes.

## Useful calculations

- Total selected = Passed + Failed + Blocked + Not run.
- Execution completion = (Passed + Failed) / Total selected × 100.
- Pass rate among conclusive results = Passed / (Passed + Failed) × 100; use N/A for a zero denominator.
- Risk coverage = risks with at least one executed mapped case / in-scope risks. This is not code coverage or proof that all behavior is covered.
- Report counts with percentages; separate manual cases, automated tests, browser runs, and retries.

## Severity and priority

| Severity | Meaning in this simulated shop |
| --- | --- |
| Blocker | Core journey cannot be evaluated at all |
| Critical | Core purchase/session behavior is unusable with no viable workaround |
| Major | Important behavior is wrong but a workaround exists |
| Minor | Limited usability or presentation impact |

Priority is a separate decision: P1 before the next release recommendation; P2 next planned iteration; P3 backlog. Explain why, including which demo account is affected. Purpose-built problem accounts may exhibit intentional faults: report them as sandbox observations, not production incidents.

## Release recommendation

This is a simulated QA decision. **Go:** all selected P1 cases passed, every high risk has executed coverage, and no open Blocker/Critical finding affects the standard-user core journey. **Conditional:** those gates pass but explicitly accepted lower risks remain; name the decision owner, mitigation, and follow-up. **No-Go:** a gate fails or evidence is insufficient. Until execution begins, use “Pending execution”, not Go. Record all unexecuted cases and reasons even if outside the release gate.

## Evidence storage

Use synthetic customer data. Public demo credentials may be named as test inputs; never include real credentials, session tokens, or private contact data. Review screenshots, logs, and traces before sharing. Keep raw generated reports in CI artifacts, and copy only selected, reviewed evidence into versioned documentation. Record artifact expiry; preserve selected release evidence with a commit and run ID so a temporary artifact link is not the sole proof. Do not publish raw traces automatically.

## Automation reliability

Proposed Week 9 baseline: repeat the chosen Chromium suite five times, with retries disabled, and report first-attempt pass/fail counts. Investigate inconsistent results rather than erasing them with retries. Additional browsers remain stretch work. A small repeated run is a useful observation, not a guarantee of reliability.
