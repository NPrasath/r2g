# Excel tracking templates

Create one workbook with the following six sheets by copying these tables into Excel. The rows below are templates and proposed examples; no approval, test pass, or time saving has been recorded.

Keep the shared workbook under the team's existing file-sharing arrangement. If a workbook is committed to GitHub, assign one editor at a time to avoid binary-file merge conflicts. Use GitHub issues for approved requirements and execution status; Excel retains capture, measurement, execution history, and links.

## 1. Workflow

| Stage | Primary owner | Supporting role | Input | Exit evidence | Link |
| --- | --- | --- | --- | --- | --- |
| Collect | BA | Tester | Interview | Rules and questions | Add link |
| Approve | BA | Tester / TM | Draft requirement | Human decision/version | Add link |
| Design | Developer | TM / Tester | Approved requirement | Accepted approach and ready issue | Add link |
| Build | Developer | Tester | Ready issue | PR and developer checks | Add link |
| Verify | Tester | Developer / TM | Candidate commit | QA, regression and retest evidence | Add link |
| Accept | BA | Tester | Tested candidate | Business acceptance | Add link |
| Release | TM | Developer / Tester | Candidate and approvals | Training release decision | Add link |
| Improve | TM | All roles | AI run and quality evidence | Process/skill changes | Add link |

## 2. Requirements

| Requirement ID | User / module | Problem / source | Proposed behavior | Acceptance IDs | Open decisions / owner | Approval person/date/version | GitHub issue |
| --- | --- | --- | --- | --- | --- | --- | --- |
| REQ-RQC-001 | Quality operator / RQC | Batch-progress clarity / training scenario | Draft; refine with BA | Proposed AC01–AC08 | D01–D08 / see requirement | Not recorded | Not created |

Add interview notes, priority, constraints, and normal/exception flows in adjacent columns as needed. After approval, place the authoritative version in the GitHub requirement issue. Do not maintain a separate implementation status backlog here.

## 3. Test Cases and Executions

Use one row per execution. Keep a catalogue row with NotRun until there is a candidate; append results instead of replacing a previous failure.

| Test ID | Requirement / AC | Preconditions / input | Steps | Expected result / decision source | Actual result | Status | Commit / environment | Person / date | Evidence / defect |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TC-RQC-001 | REQ-RQC-001 / AC02 | Synthetic 96-item batch | Check first item; inspect progress | Awaiting BA-approved D01/D02 | Not executed | Blocked | Not recorded | Not recorded | Not recorded |
| TC-RQC-002 | REQ-RQC-001 / AC03 | 95 items resolved by approved rule | Check final required item | Awaiting BA-approved D01–D03 | Not executed | Blocked | Not recorded | Not recorded | Not recorded |
| TC-RQC-003 | REQ-RQC-001 / AC04 | One prior result | Repeat identical update | Awaiting BA-approved D04 | Not executed | Blocked | Not recorded | Not recorded | Not recorded |

Allowed result states: NotRun, Blocked, Passed, Failed. Use real candidate and evidence links when executing. The Tester adds failure, authorization, concurrency, and regression cases.

## 4. Agents and Skills

| Item | Purpose | Human owner | Repository path | Version commit | Evaluation / change PR |
| --- | --- | --- | --- | --- | --- |
| Requirements Analyst | BA assistance | BA | .github/agents/requirements-analyst.agent.md | Record commit | Add evidence |
| Implementation Developer | Implementation assistance | Developer | .github/agents/implementation-developer.agent.md | Record commit | Add evidence |
| QA Tester | QA assistance | Tester | .github/agents/qa-tester.agent.md | Record commit | Add evidence |
| Technical Reviewer | Technical review assistance | TM | .github/agents/technical-reviewer.agent.md | Record commit | Add evidence |
| Five reusable skills | See Copilot guide | Assigned content owner | .github/skills | Record commit | Add evidence |

## 5. AI Runs

| Run ID | Task / issue / PR | Person / role | Agent / model if visible | Prompt link | Instruction / skill commit | Manual baseline min | Prompting min | Review min | Correction min | Verification min | Accepted / reworked / rejected | Quality evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Assign on execution | Add links | Record person/role | Record actual session | Add link | Record commit | Leave blank until measured | Record actual | Record actual | Record actual | Record actual | Record outcome | Tests / defects / limitations |

Do not enter estimated manual effort as a measured baseline. Do not use blank to mean zero minutes. See [AI evaluation](ai-evaluation.md) for comparisons and formula rules.

## 6. Decisions and UAT

| Decision ID / type | Requirement / candidate | Decision / scenario | Human owner | Date | Outcome | Evidence / remaining action |
| --- | --- | --- | --- | --- | --- | --- |
| D01 / business rule | REQ-RQC-001 / Draft | Meaning of RQC started/completed | BA / process owner | Not recorded | Unresolved | Interview required |
| UAT-001 | Candidate not recorded | Validate approved RQC workflow | BA | Not recorded | Not executed | Await tested candidate |

These templates cover the Excel requirement without requiring another planning application. A native workbook can be added later if the team prefers a preformatted file.
