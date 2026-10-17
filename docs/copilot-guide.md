# Copilot agents and skills: how the team uses them

Repository instructions provide common conventions. Custom agents provide a task focus and tool set. Skills provide reusable procedures selected when relevant. These files do not enable a paid feature, enforce every instruction, or replace human review.

## Agent selection

| Human | Agent | Allowed tools | Review the output for |
| --- | --- | --- | --- |
| BA | Requirements Analyst | Read, search, edit, GitHub read context | Assumptions, unanswered questions, measurable criteria |
| Developer | Implementation Developer | Read, search, edit, execute, GitHub read context | Correctness, scope, actual tests, unintended changes |
| Tester / QA | QA Tester | Read, search, edit, execute, GitHub read context | Expected outcomes, reproducibility, evidence, coverage gaps |
| Technical Manager | Technical Reviewer | Read, search, GitHub read context | Source-grounded findings, missing checks, residual risk |

`github/*` provides the cloud agent's available GitHub context tools; it is not a grant to bypass GitHub permissions. The QA agent's edit scope is an instruction and must be checked in review. The reviewer has no execution tool and must say so when assessing supplied test evidence.

## Skills

| Skill | Use it for | Human content owner |
| --- | --- | --- |
| [Requirements elicitation](../.github/skills/requirements-elicitation/SKILL.md) | Questions, rules, acceptance criteria | BA |
| [R2G change analysis](../.github/skills/r2g-change-analysis/SKILL.md) | Scope, contracts, state/data impact, test approach | Developer + TM |
| [Test design and verification](../.github/skills/test-design-and-verification/SKILL.md) | Testability, scenarios, execution, defects, retests | Tester / QA |
| [Code review](../.github/skills/code-review/SKILL.md) | Independent technical findings | Technical Manager |
| [Release readiness](../.github/skills/release-readiness/SKILL.md) | Candidate-specific gates and release evidence | Technical Manager + BA/QA |

Select the custom agent using the interface available to your account. Include the exact skill path in your task when you want its procedure followed. Repository files alone do not prove that a session loaded them; inspect the output and record the relevant commit.

## Copy-and-adapt task prompts

Replace bracketed values with real issue links and versions. These are starting prompts, not completed execution records.

**BA**

> Use `.github/skills/requirements-elicitation/SKILL.md` to refine [requirement issue]. Read `docs/requirements/REQ-RQC-001.md`. Identify facts, proposals, and open decisions; ask focused interview questions; draft acceptance IDs and exception scenarios. Keep approvals unrecorded. Do not implement code. Return the remaining readiness blockers for the BA and Tester.

**Developer planning**

> Use `.github/skills/r2g-change-analysis/SKILL.md` for [implementation issue] against [approved requirement version]. Confirm its decisions and scope. Propose the smallest design, affected files, validation, authorization/audit, failure/concurrency behavior, tests, and rollback. Identify missing inputs for the Technical Manager before implementation.

**Developer implementation**

> Implement only [ready issue] against [approved version and acceptance IDs]. Follow the accepted approach at [decision link] and the repository instructions. Include meaningful developer tests. Run available baseline and task checks. Prepare a draft PR with commands/results, unavailable checks, and remaining human QA/UAT/review work. Return any new business decision to the BA.

**Tester**

> Use `.github/skills/test-design-and-verification/SKILL.md` for [requirement/PR] on [candidate SHA]. Draft or execute the agreed cases for partial/final batches, repeats, invalid IDs, permissions, failures, and concurrency as relevant. Flag unknown expected outcomes. Record actual environment, commands, results, and evidence. Produce reproducible defect drafts and a retest plan. Do not silently change application behavior.

**Technical Manager**

> Review [PR] against [requirement version] using `.github/skills/code-review/SKILL.md`. Inspect the diff and surrounding code independently. Lead with actionable findings, trigger, file/location, consequence, and suggested fix/check. Separate confirmed issues from inference and missing evidence. State the limits of this read-only review and list the human decisions still needed.

**Training release**

> Use `.github/skills/release-readiness/SKILL.md` for [candidate SHA]. Check developer evidence, QA/regression/retest results, BA acceptance, open defects, and rollback. Draft release notes and identify blockers and their owners. Leave missing approvals unrecorded. Do not merge or release.

## Close the loop

The initiating human reviews the output, records corrections, verifies evidence, and updates the issue/PR. Record AI effort with [the evaluation method](ai-evaluation.md). Improve skills using a small PR that includes the failure pattern, revised instruction, and a fresh task to evaluate it.

If a feature is unavailable, use these prompts for assisted drafting where supported and record the limitation. Do not represent chat suggestions as cloud execution or a completed test run.

Configuration references: [GitHub agents](https://docs.github.com/en/copilot/reference/custom-agents-configuration) and [GitHub skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills).
