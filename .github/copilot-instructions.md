# R2G training repository instructions

Read README.md, CONTRIBUTING.md, docs/sdlc-playbook.md, and the linked issue before changing files. This is a fresh training starter, not the existing plant application.

- Human roles are BA, Developer, Tester/QA, and Technical Manager; see TEAM.md. Never invent approval, UAT acceptance, a reviewer identity, or a test result.
- The approved GitHub requirement issue governs behavior. `docs/requirements/REQ-RQC-001.md` starts as Draft. Material unresolved business decisions block business-rule implementation; ask the BA and identify the dependency.
- Work on a small issue-linked branch/PR. State a short plan, the requirement version and acceptance IDs, affected files, scope boundaries, and validation before implementing.
- The initial API targets .NET 10 and has only `/` and `/health`. SQL persistence, identity, RQC, UI, and hardware integration have not been implemented. Do not claim those modules exist.
- Use clear C# with nullable references enabled. Keep business rules testable outside HTTP handling when they are introduced. Avoid unrelated refactors and invented architecture.
- Require actual authenticated identity and explicit authorization for future business mutations. Do not use a supplied username, nonempty password, or administrator fallback as authentication/audit evidence.
- Use synthetic training data. Do not copy legacy configuration, credentials, binaries, or plant data. Keep credentials in the appropriate secret store when a later task needs them.
- For data changes, explain validation, transaction boundaries, retries, concurrency, and rollback. Parameterize SQL if introduced. Do not present an in-memory test as proof of SQL behavior.
- Use relevant skills under `.github/skills/`. Read their SKILL.md instructions when applicable. Agents are configured under `.github/agents/`.
- Baseline commands: `dotnet restore R2G.Training.sln`; `dotnet build R2G.Training.sln --configuration Release --no-restore`; `dotnet test R2G.Training.sln --configuration Release --no-build --logger trx --results-directory TestResults`; `python3 scripts/validate_training_kit.py`.
- Choose meaningful tests for the change. Report the exact commands, environment, commit, results, evidence links, and checks not run with reasons. Generated tests and passing content validation do not establish application correctness.
- Preserve failed-test and defect evidence. QA verifies fixes independently; BA performs UAT; TM decides merge/release. Return new business questions to the BA.
- In the PR, summarize resulting behavior, linked issues, validation, residual limitations, and deployment/rollback implications. Use `Related to` rather than `Closes` if acceptance work remains.
- Record the agent/skill/instruction version and the human review/correction/verification effort in the AI run record. Do not fabricate savings or model information.

Changes to these instructions, profiles, skills, or workflows require the same human review as code changes.
