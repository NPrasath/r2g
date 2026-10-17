# Testing and the Tester in the SDLC

Testing begins during requirement collection. The Developer and Tester have different evidence responsibilities; BA UAT and technical review add separate decisions.

| Layer / activity | Owner | Evidence |
| --- | --- | --- |
| Testability and acceptance review | Tester + BA | Clear criteria, decisions, risks, blocked expectations |
| Unit and component tests | Developer | Relevant rules and boundary behavior; command and result |
| API / database integration tests | Developer, with Tester input | Actual server/database setup, fixtures, error/transaction cases |
| Functional and exploratory testing | Tester | Candidate commit, inputs, steps, expected/actual result, evidence |
| Regression and fix verification | Tester | Original failing case, fixing commit, retest and affected scenarios |
| Security, concurrency, failure behavior | Developer + Tester; TM reviews | Scope, threat/failure scenario, actual execution and limits |
| UAT | BA / process owner | Business scenarios, candidate, explicit acceptance or rejection |
| Release checks | Tester + Developer; TM decides | Exact candidate, evidence, open defects and decision |

## Day-one checks

The C# project includes two HTTP smoke cases through an in-process ASP.NET Core host. They cover startup and JSON responses from `/` and `/health`. They contain no RQC, database, end-to-end UI, authorization, or hardware assertions.

The Python training-content validator checks local documentation links, required agent/skill metadata, issue form structure, issue-backlog references, and synthetic fixture integrity. It does not compile C# or execute business scenarios.

CI is configured to run both. Treat the first successful run as evidence only after inspecting the actual run and logs.

## RQC risk-based test inventory

Draft test cases before coding. Link each to the final approved acceptance criterion.

| Scenario | What to establish | Initial execution state |
| --- | --- | --- |
| Initial batch | Expected initial state, total/pending counts | NotRun; expected outcome needs BA approval |
| Partial batch: 1 of 96 | Started/completed distinction and correct counts | NotRun |
| Boundary: 95 then final battery | Correct completion condition | NotRun |
| Mixed OK / NOTOK | Approved resolved vs accepted distinction | Blocked pending D02 |
| Hold and release | Completion and permissions | Blocked pending D03/D06 |
| Repeat same update | Idempotency and audit policy | Blocked pending D04 |
| Correct an existing result | Agreed correction and audit behavior | Blocked pending D04 |
| Invalid / foreign-batch IDs | Validation and batch isolation | Blocked pending D08 |
| Unauthenticated / wrong role | Denial and no mutation | Blocked pending D06 |
| Failed write / interrupted request | Atomicity, error feedback, retry outcome | Blocked pending D05 |
| Concurrent updates / stale state | Consistency and conflict policy | Blocked pending D07 |

In-memory tests cannot demonstrate SQL transaction correctness. Add real database fixtures and race/failure checks when persistence is introduced. A UI end-to-end test is needed when the UI exists.

## Execution record

For each run, record test-case ID, requirement/criterion, preconditions, test inputs/steps, expected result, actual result, environment, commit SHA, execution date/person, status, and evidence link. Use `NotRun`, `Blocked`, `Passed`, or `Failed`. Put planned cases in the catalogue and keep individual execution records so reruns do not erase failures.

## Defect and retest evidence

Use the defect issue form. Include reproducible steps, expected/actual result, severity, environment/commit, and a linked test case. The Developer links a fix and regression test. The Tester verifies on the fixing commit and reruns affected scenarios. Keep the issue open while verification is pending.

Never mark tests passed based on agent prose, compilation, syntax checks, or a generated test file alone. If a dependency prevents execution, record Blocked/NotRun with the dependency and owner.
