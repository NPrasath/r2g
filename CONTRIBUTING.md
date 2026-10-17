# Working agreement

1. Link every change to a requirement or training issue. Before implementation, record the BA's business decisions and the Technical Manager's accepted approach.
2. Use branches such as `feature/req-rqc-001-progress`, `test/req-rqc-001-cases`, or `docs/cohort-01-roles`.
3. Use a draft PR for work in progress. Keep it small enough for another person to explain and verify.
4. The Developer supplies automated evidence; the Tester supplies independent test and defect evidence; the BA supplies business acceptance; the Technical Manager records merge/release decisions.
5. Record approvals with the human's name, date, requirement version or commit SHA, and decision. AI-generated approval text is a draft until the human explicitly confirms it.
6. Report commands, results, environment, and checks not run. Keep training examples, proposed test cases, and executed evidence distinguishable.
7. Keep secrets out of the repository. Use synthetic IDs and isolated training environments. Never use a fallback administrator identity for auditing.
8. Record business-rule changes in the requirement issue and update the linked tests and task before proceeding.
9. Review changes to instructions, agents, skills, workflows, and dependencies through PRs, just as application changes are reviewed.
10. Complete the [release checklist](docs/release-checklist.md) for a training release. Production or plant deployment requires separate requirements and authorization.

## Ready and done

**Ready for implementation:** approved business rules; linked acceptance criteria; QA review of testability; accepted technical approach; bounded scope; available dependencies; clear test and rollback plan. An unresolved material business question blocks Ready.

**Done:** reviewed implementation; meaningful automated tests; independent QA evidence; verified fixes; BA acceptance; Technical Manager decision; linked issue/PR/test records; updated documentation and AI run record. Mark unavailable checks and accepted limitations explicitly.

Passing CI alone does not complete the human acceptance steps. See the [playbook](docs/sdlc-playbook.md) for the exact handoffs.
