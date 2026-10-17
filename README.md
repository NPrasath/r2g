# R2G · AI-assisted SDLC training

Learn to rebuild R2G in small, reviewed increments using **Excel, GitHub, and GitHub Copilot where available**. Start with requirements and finish with verified release evidence.

This is a fresh training starter. The initial application contains only HTTP startup/health endpoints. Receipt, RQC, trolley mapping, charging, and reporting are exercises to implement as the team progresses. Existing R2G source, credentials, and plant data are not included.

## Start your first cohort

1. The Technical Manager completes [repository setup](docs/repository-setup.md) and names the four role owners in [TEAM.md](TEAM.md).
2. Everyone reads the [working agreement](CONTRIBUTING.md) and [SDLC playbook](docs/sdlc-playbook.md).
3. Run [Lab 00](training/labs/00-foundation.md), then the [training sequence](training/README.md).
4. The BA begins with the [draft RQC requirement](docs/requirements/REQ-RQC-001.md). The Tester joins this workshop.
5. Open real issues with the supplied forms. Submit changes through PRs using the supplied template.

## People, AI, and evidence

| Human role | Main responsibility | Copilot profile |
| --- | --- | --- |
| Business Analyst | Requirements, business decisions, acceptance criteria, UAT | [Requirements Analyst](.github/agents/requirements-analyst.agent.md) |
| Developer | Implementation, developer tests, fixes, PR evidence | [Implementation Developer](.github/agents/implementation-developer.agent.md) |
| Tester / QA | Testability, test cases, independent verification, regression, defects | [QA Tester](.github/agents/qa-tester.agent.md) |
| Technical Manager | Architecture, technical review, merge and release decisions | [Technical Reviewer](.github/agents/technical-reviewer.agent.md) |

AI drafts and investigates. Humans approve the relevant decisions. Selecting an agent does not assign a human, approve an issue, or grant release authority.

## What is included

- Eight guided labs, a facilitator guide, role ownership, a release checklist, and an AI evaluation method.
- Requirement, implementation, and defect issue forms, plus a PR template.
- Four Copilot agent profiles and five reusable skills, with [usage prompts](docs/copilot-guide.md).
- [Excel tracking tables](docs/excel-tracking.md) to copy into a workbook; no additional planning system is required.
- A .NET 10 ASP.NET Core starter, HTTP integration smoke tests, and GitHub Actions CI.
- Synthetic 96-battery training data and a [proposed issue backlog](training/backlog.json).

## Application and checks

The initial API exposes `GET /` and `GET /health`. Business endpoints and a SQL database have not been implemented. See [architecture and scope](docs/architecture.md).

GitHub Actions can build and test the starter without installing the SDK on each participant's computer. Development inside GitHub depends on the Copilot features enabled for your account. The [setup guide](docs/repository-setup.md) describes the browser workflow and fallback.

For a local development environment with the .NET 10 SDK:

```sh
dotnet restore R2G.Training.sln
dotnet build R2G.Training.sln --configuration Release --no-restore
dotnet test R2G.Training.sln --configuration Release --no-build --logger trx --results-directory TestResults
dotnet run --project src/R2G.Training.Api --urls http://localhost:5096
```

The optional training-content check uses Python 3, also supplied by the CI runner:

```sh
python3 scripts/validate_training_kit.py
```

Two passing HTTP smoke cases show that the starter boots and responds. They do not establish RQC behavior, SQL consistency, security, or plant readiness. Record those separately using [the test strategy](docs/testing-strategy.md).

## Rebuild roadmap

| Increment | Team delivers | Completion evidence |
| --- | --- | --- |
| Foundation | Named roles, working CI, approved tool access | Setup issue and successful build/test run |
| RQC pilot | Agreed state rules, implementation, regression and UAT | Linked requirement → issue → PR → tests → acceptance |
| Battery receipt | Approved scan format, duplicate rules, batch creation | Automated and independent QA evidence |
| Trolley mapping | Per-battery/per-batch contract and FIFO decisions | Transaction and concurrency tests |
| Manual charging | Authorized workflow, measurements, audited transitions | Failure, authorization, and integration tests |
| Hold/release and reports | Agreed business rules and access restrictions | Regression and business acceptance |
| Plant integration | Database, scanners, RFID, printers, SAP where needed | Separately planned integration and hardware validation |

The roadmap describes future work. It does not assume the legacy behavior is the approved specification. Automatic charging requires a separate scope decision.

Start with one RQC change and complete the full lifecycle before expanding.
