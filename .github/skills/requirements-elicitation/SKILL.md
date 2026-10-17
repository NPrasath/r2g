---
name: requirements-elicitation
description: Refine R2G requests into business decisions, testable criteria, and an issue-ready requirement. Use for BA interviews, ambiguous rules, exceptions, and requirement readiness checks.
---

1. Read the request, current requirement, and docs/sdlc-playbook.md. Record the requirement ID, revision, and actual sources.
2. Identify actor, goal, normal flow, data, business rules, exceptions, permissions/audit, and measurable constraints. Mark facts, proposals, and unknowns.
3. Build a decision table: ID, question, human owner, answer/source, effect on acceptance, and status. For RQC ask what started/completed means, which results resolve a battery, holds, repeats/corrections, failed writes, and concurrent updates.
4. Draft acceptance IDs with Given/When/Then or equivalent observable input/outcome. Ask QA to challenge boundary, invalid, failure, and access cases. Do not turn unresolved rules into expected results.
5. Produce an issue-ready draft with scope, out-of-scope items, decision table, criteria, dependencies, and blank human approval fields.
6. Report readiness and the exact remaining decisions. Only record approval when the human supplies it, including identity, date, and revision.

Example: “one result was saved” does not establish that a 96-item batch is complete. Ask which state the business intends before proposing a completion rule.
