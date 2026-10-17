# Lab 03 · Test design before implementation

**Lead:** Tester / QA. **Partners:** BA and Developer.

1. Read [the test strategy](../../docs/testing-strategy.md), approved criteria, and accepted design.
2. Use QA Tester and the test-design skill to draft acceptance and regression cases. Review expected outcomes independently of the proposed code.
3. Include 0/1/95/96 progress boundaries, repeat/corrected updates, invalid/foreign IDs, mixed results/holds, permissions, failure, and concurrency where relevant to the accepted scope.
4. Use [synthetic fixture data](../data/rqc-batch.json). Add data only as the approved tests need it.
5. Give every case an ID and expected outcome/source. Separate automated developer checks, independent manual QA, database tests, and later UI/hardware checks.
6. Record initial cases as NotRun; mark unresolved expectations/dependencies Blocked. Submit the test-plan PR and ask the BA to confirm business expectations.

**Deliverables:** criterion-to-test mapping, case/data plan, blocked dependencies and owners.

**Exit:** the team knows what evidence would demonstrate the task. No pass is recorded before execution.
