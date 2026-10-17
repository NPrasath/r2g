---
name: release-readiness
description: Prepare a traceable R2G training release assessment from one candidate and its QA, UAT, technical, and rollback evidence. Use before merge/release or when summarizing remaining gates.
---

1. Identify the exact candidate SHA, linked requirements/tasks/PRs, and intended training release scope.
2. Read docs/release-checklist.md and check developer build/test evidence, independent QA/regression/retest evidence, BA UAT decision, and Technical Manager review. Verify which commit each result applies to.
3. List open defects, unavailable checks, environment limits, and accepted risks with their actual human owner/decision. Keep unrecorded fields unrecorded.
4. Check deployment steps, data/schema effects, rollback and post-release checks; mark not applicable only with a reason supported by the scope.
5. Draft release notes and a readiness assessment with blockers and next owners. Separate training demonstration from production and plant readiness.
6. Request the human TM's release decision through the team's process. Do not invent signoff, merge, publish a release, or close unfinished acceptance tasks yourself.
