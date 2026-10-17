---
name: test-design-and-verification
description: Design R2G acceptance and regression tests, execute candidate checks honestly, report defects, and verify fixes. Use for QA planning, testability review, test execution, and retesting.
---

1. Read approved criteria, docs/testing-strategy.md, candidate commit/environment if available, and existing evidence. Flag missing business expectations.
2. Map each acceptance ID to normal, boundary, invalid, repeated, partial-batch, authorization, failure, and concurrency cases as relevant. Assign the right test layer and owner.
3. Specify test ID, requirement/criterion, preconditions, synthetic inputs, steps, expected result, and dependencies. Mark unresolved expectations Blocked. Planned cases are NotRun, never Passed.
4. Execute only the checks supported by the available environment. Record command or manual steps, timestamp/person, exact commit, expected/actual result, and evidence. Distinguish content checks, compilation, unit tests, integration tests, UI checks, SQL checks, and hardware validation.
5. Draft defects with reliable reproduction, expected/actual result, severity, evidence, and linked requirement/test/candidate. Do not infer a reproduced defect from code inspection alone.
6. On the fixing commit, repeat the failing case and affected regression scenarios. Keep the original failure and append the new execution. Produce a QA assessment with open defects and missing checks.

For the first RQC lab cover 0, 1, 95, and 96 checked items, mixed outcomes, holds, repeats/corrections, wrong-batch IDs, authorization, failed writes, and simultaneous updates. Expected outcomes depend on BA-approved rules. Use synthetic data and an isolated database when database checks become applicable.
