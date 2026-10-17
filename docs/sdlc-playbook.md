# AI-assisted SDLC playbook

Use this lifecycle for every R2G increment. The first cohort practices it with RQC.

## Records and traceability

Excel captures interview notes, open questions, test execution, and AI effort. After approval, the GitHub requirement issue is the authoritative business record. GitHub holds execution status; Excel keeps IDs and links.

Use the chain `REQ-RQC-001 → implementation issue → PR → TC-RQC-* → QA/UAT evidence → training release`. Create actual links as records are created; proposed backlog keys are not issue numbers.

## Roles and handoffs

| Stage | Business Analyst | Developer | Tester / QA | Technical Manager | Exit evidence |
| --- | --- | --- | --- | --- | --- |
| Collect | Interview users; capture goals, rules, exceptions | Identify technical questions | Identify testability gaps and edge cases | Confirm scope and ownership | Notes and decision questions |
| Approve | Own business rules and acceptance criteria | Estimate bounded work | Review measurable expected outcomes | Confirm priorities and constraints | Human business approval and version |
| Design | Resolve new business questions | Propose design and tasks | Draft risk-based test plan | Accept architecture and approach | Ready implementation issue |
| Build | Answer scope questions | Use Copilot; inspect code; add developer tests | Refine tests alongside implementation | Review significant design changes | Branch, draft PR, honest check results |
| Verify | Clarify expected outcomes | Run tests; fix defects | Execute independent functional/regression tests; report defects; retest fixes | Review diff and validation gaps | Commit-specific automated and QA evidence |
| Accept | Perform UAT and record business acceptance | Prepare candidate and explain behavior | Confirm tested candidate and residual defects | Assess release readiness | BA acceptance and QA assessment |
| Release | Confirm business communication | Supply deployment and rollback steps | Run agreed candidate/release checks | Own merge and training release decision | Approved release record and commit |
| Improve | Review requirement quality | Record AI effort and corrections | Review escaped defects and test gaps | Compare quality and effort; improve process | Measured retrospective and skill PR |

Tester/QA participates from requirement collection. The Tester supplies evidence and a quality recommendation. The Technical Manager owns the final release decision; the BA owns business acceptance.

## Issue workflow

Use these status values in the issue body, or create an optional GitHub Project with the same values:

| Status | Move here when | Responsible role |
| --- | --- | --- |
| Needs clarification | Material business questions remain | BA |
| Ready | All Ready conditions in CONTRIBUTING are met | Developer, with BA/QA/TM input |
| In progress | A person is actively implementing the task | Developer |
| In review | A PR and developer evidence are available | Developer / Technical Manager |
| In QA | Candidate and review feedback are ready for independent verification | Tester / QA |
| UAT | QA evidence is adequate for business validation | BA |
| Ready for release | Business and technical evidence is recorded | Technical Manager |
| Done | Acceptance and release/completion conditions are met | Technical Manager / issue owner |
| Blocked | A named dependency prevents progress | Current owner |

GitHub's basic issue state remains open/closed. These richer statuses are a team convention until a Project field or labels are actually configured. Keep Ready/Done distinct from AI suggestions.

## Requirement collection

The BA captures users, business problem, process steps, inputs/outputs, rules, errors, permissions, audit needs, performance needs, priority, and questions. Ask the Tester to identify cases whose expected outcome cannot yet be stated.

Use [the draft requirement](requirements/REQ-RQC-001.md) as the interview starting point. Turn uncertain rules into decisions with an owner. Record approval in GitHub and link the Excel row. Keep an approval date/version and change history.

## Issues and PRs

- **Requirement issue:** user need, business rules, acceptance criteria, open decisions, human approval.
- **Implementation issue:** linked requirement, exact scope, dependencies, accepted approach, tests, completion conditions.
- **Defect issue:** tested commit/environment, reproduction steps, expected/actual result, severity, evidence, linked requirement/test/PR, retest outcome.
- **PR:** problem and final behavior, linked issues, meaningful tests, unavailable checks, QA/UAT evidence, database and rollback implications.

Only put `Closes #...` on a PR when merging really completes that issue. Use `Related to #...` for a requirement still waiting on QA, UAT, or other tasks. Do not let a merge automatically close unfinished business acceptance.

## AI task contract

Give the agent a linked issue, approved requirement version, acceptance IDs, scope boundaries, relevant files, applicable skill, check commands, and desired evidence. Ask it to flag missing decisions before editing code. Review the result, not just its explanation.

The human initiating the session records the agent profile, skill/instruction commit, model if visible, prompt, human effort, corrections, test results, and final outcome. See [Copilot usage](copilot-guide.md) and [AI evaluation](ai-evaluation.md).

## Defect cycle

The Tester creates a reproducible defect tied to a candidate commit. The BA confirms any disputed business expectation; the Technical Manager helps prioritize. The Developer adds a regression test when useful and supplies the fixing PR. The Tester repeats the failed scenario and relevant regression checks on the fixing commit before recording Verified/Closed. Keep failures and retest evidence, rather than rewriting a failed run as passed.

## Change and release decisions

Reopen requirement decisions when behavior changes. Update implementation scope and test expectations together. Release evidence must identify one candidate commit; do not combine results from different revisions without showing which checks were repeated. Use the [release checklist](release-checklist.md).
