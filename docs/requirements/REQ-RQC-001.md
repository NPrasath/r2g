# REQ-RQC-001 · Explain RQC batch progress correctly

**Status:** Draft — Needs clarification

**Business approval:** Not recorded

**Implementation readiness:** Blocked pending business decisions

**Source:** R2G battery quality workflow; this is a training requirement draft

## Problem and goal

An operator needs to understand whether quality checking has started and whether the whole batch has reached its agreed completion condition. Partial updates must not misrepresent overall completion.

The training scenario uses a synthetic batch of 96 unique battery IDs. This fixture size supports the exercise; the BA must confirm actual product rules and whether different sizes are allowed.

## Interview the process owner

| Decision | Question | Decision owner | Current answer |
| --- | --- | --- | --- |
| D01 | Does the batch status mean RQC has started or RQC has completed? Are these separate states? | BA / process owner | Unresolved |
| D02 | Which individual results count as resolved? Does NOTOK finish a check without approving it? | BA / process owner | Unresolved |
| D03 | Do held batteries prevent completion? Who may release them? | BA / process owner | Unresolved |
| D04 | Are repeat identical updates idempotent? How are changed results handled and audited? | BA / process owner | Unresolved |
| D05 | Must individual and batch updates be atomic? What should the operator see on failure? | BA, Developer, TM | Unresolved |
| D06 | Which roles may view and change quality results? What identifies the acting person? | BA / process owner | Unresolved |
| D07 | What should simultaneous updates do? Is stale data rejected or retried? | BA, Developer, TM | Unresolved |
| D08 | How are invalid, duplicate, missing, or foreign-batch battery IDs handled? | BA / process owner | Unresolved |

## Proposed acceptance criteria — awaiting approval

These are interview proposals, not approved product behavior.

| ID | Proposed criterion | Decision dependency |
| --- | --- | --- |
| AC01 | A newly received batch has a defined, visible initial quality state and truthful counts. | D01, D02 |
| AC02 | Checking one battery in a 96-battery batch cannot imply that all 96 have completed checking. | D01, D02 |
| AC03 | A final valid update changes batch completion only when the approved resolved-state rule holds for every required battery. | D01–D03 |
| AC04 | Repeating an identical update does not double-count; changing an outcome follows the agreed correction/audit rule. | D04 |
| AC05 | A failed operation leaves an agreed consistent state and reports failure rather than success. | D05 |
| AC06 | Unauthorized changes are denied and an allowed change records the actual authenticated identity. | D06 |
| AC07 | Simultaneous updates preserve counts and apply the approved conflict/retry policy. | D07 |
| AC08 | Invalid IDs cannot affect another batch or inflate progress. | D08 |

The Tester drafts boundary, invalid, repeat, failure, authorization, and concurrency cases before implementation. Expected outcomes must follow the approved decisions; unresolved expectations are Blocked, not Passed.

## Scope for the first implementation

Define one bounded task after approving the rules. The UI, SQL persistence, and hardware integration can be later tasks with explicit dependencies and tests. State which parts of this requirement the first task can actually satisfy.

## Human decision record

| Record | Value |
| --- | --- |
| BA / process owner | Not recorded |
| Approved requirement version and date | Not recorded |
| Accepted decisions D01–D08 | Not recorded |
| QA testability assessment | Not recorded |
| Technical approach approval | Not recorded |
| Requirement issue URL | Not created |
| Implementation / test / PR links | Not created |

When approved, publish the decisions in the GitHub requirement issue, link this document, and keep revisions traceable. Do not use the draft text to bypass clarification.
