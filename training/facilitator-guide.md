# Facilitator guide

## Prepare

Appoint four role owners, confirm GitHub/Copilot feature access, inspect the first actual CI run, and prepare an Excel workbook using the tracking tables. Use synthetic data throughout. A small team can rotate roles between increments; keep independent review visible.

The complete legacy application is not prebuilt into this repository. Learners start with a bootable scaffold and rebuild agreed behavior in increments. Do not distribute an answer implementation before the requirement and test-design exercises.

## Run the cohort

Allocate sessions around the eight labs. Estimate pacing from the team's familiarity and availability; there is no measured course duration yet.

In Lab 01, act as the process owner only if that role is explicitly assigned. Supply business decisions deliberately and record them as training decisions. Do not present invented decisions as actual plant requirements. Require the BA to resolve what counts as RQC completion before the Developer implements it.

In Labs 02–04, ensure the Tester can describe expected results independently of the implementation. Let the Developer use the agent, then ask them to explain the diff and show actual checks.

In Lab 05, inspect a real failure where available. If there is none, use a separately labeled hypothetical defect-report exercise or propose a controlled mutation on a disposable branch. Do not merge deliberately defective code into main or claim that a hypothetical defect was reproduced.

In Lab 06, ask each role to show their own evidence and identify the candidate commit. Stop the training release when required evidence is missing, or record the actual human decision accepting a limitation within the exercise's scope.

## Assess participants

| Area | Observable evidence |
| --- | --- |
| BA | Resolves ambiguity, records approval/version, makes UAT criteria observable |
| Developer | Keeps scope bounded, explains the code, adds relevant tests, reports execution honestly |
| Tester | Joins requirements, challenges expectations, reproduces failures, verifies fixes independently |
| Technical Manager | Grounds findings in evidence, understands limitations, records review/release decisions |
| Team | Can follow requirement → issue → PR → tests → UAT → release links |
| AI practice | Records human rework, spots unsupported claims, improves instructions using evidence |

## Repeat

Rotate roles and use receipt validation, trolley mapping, or another approved module. Compare requirement quality, review findings, defects, and measured human effort across increments. Do not rank participants only by speed or generated lines of code.
