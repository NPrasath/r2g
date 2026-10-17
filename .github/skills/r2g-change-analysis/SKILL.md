---
name: r2g-change-analysis
description: Plan a bounded R2G implementation from an approved issue and trace its impact on contracts, state, persistence, UI, and tests. Use before coding or fixing a defect.
---

1. Verify the linked requirement version, acceptance IDs, human decisions, task boundaries, and dependencies. Identify anything blocking implementation.
2. Inspect actual files. In the fresh starter there are no business modules or database yet; do not invent controllers, tables, procedures, or deployed behavior.
3. Trace the proposed input → validation/authorization → business rule → persistence/audit → response/UI path. List affected components and responsibilities.
4. For state changes, define allowed transitions, repeated requests, corrections, transaction boundaries, concurrency/conflict policy, and failure behavior. Return business choices to the BA; present technical options to the TM.
5. Propose a minimal file/change plan, relevant unit/integration/QA cases, fixtures, commands, environment needs, and deployment/rollback effects.
6. Produce a ready implementation issue only when its dependencies and human decisions are actually satisfied. Otherwise list blocked items with owners.

During fixes, first distinguish reproduced behavior from an inferred risk. In-memory behavior is not evidence of SQL atomicity or plant integration.
