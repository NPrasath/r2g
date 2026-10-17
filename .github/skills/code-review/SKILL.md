---
name: code-review
description: Review R2G PRs and designs for requirement alignment, correctness, authorization, data consistency, and credible test evidence. Use during technical review and regression assessment.
---

1. Read the approved requirement, task, complete diff, relevant surrounding code, and supplied evidence. Establish the candidate commit and acceptance IDs.
2. Trace behavior for normal input, invalid input, missing identity, wrong role, repeats, partial batches, errors, and concurrent requests. Inspect actual data writes and error paths where present.
3. Check authorization separately from antiforgery, identity separately from a supplied name, per-battery counts separately from request size, and atomicity separately from sequential happy-path success.
4. Assess tests against the business criteria and realistic failure modes. Note missing execution environments, fake/stale evidence, weak assertions, and checks that cannot establish the claimed result.
5. Report concrete findings first. For each include severity, file/location, trigger, observed or inferred consequence, and recommended fix/check. Label inference and uncertainty. Avoid invented findings to fill a quota.
6. Summarize technical readiness, residual gaps, and required human decisions. A review recommendation is not a human approval or release decision.

For instruction/agent/skill/workflow changes, also review scope, tool access, approval claims, check commands, and the effect on evidence quality.
