# Starter architecture and rebuild scope

## What exists on day one

| Area | Initial state |
| --- | --- |
| Runtime | C# / ASP.NET Core targeting .NET 10 |
| API | Root training metadata and a process health endpoint |
| Automated tests | ASP.NET Core in-process HTTP integration smoke cases |
| Persistence | Not implemented |
| Identity and business endpoints | Not implemented |
| User interface | Not implemented |
| Plant integrations | Not implemented |

The source application used ASP.NET Core MVC/C# and SQL Server. This training project retains the .NET language/ecosystem and starts with a small supported runtime scaffold. It does not copy the old implementation or assume its state transitions are correct. .NET 10 is an LTS release; see [Microsoft's overview](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-10/overview).

`src/R2G.Training.Api` is the initial executable. `tests/R2G.Training.Api.Tests` starts that executable in a test host. The application requires no secret or database to boot. The initial endpoints perform no business data mutation.

## RQC pilot design task

After the BA approves REQ-RQC-001, propose the smallest design that supports its transitions and tests. Separate business rules from HTTP handling. Define the input/result contract, validation, errors, and audit expectations explicitly.

An in-memory first increment may be useful for training; record its restart and concurrency limits. Do not present it as SQL integration or persistent production storage. Introduce a real SQL test database, schema, transaction boundaries, fixtures, and isolation tests in a separately agreed persistence increment.

Security and audit requirements must be addressed before adding mutable business endpoints. Decide how authenticated identity reaches the application, which roles may change quality status, and how retries and failures preserve consistency. A supplied username or default administrator is not authentication.

## Architecture decision record

Create `docs/decisions/ADR-001-rqc-design.md` in Lab 02 with:

- Context, linked requirement version, and constraints.
- Options considered and selected approach.
- State/data model and HTTP/validation contract.
- Authorization, audit, transaction, and concurrency decisions.
- Test strategy, limitations, and deployment/rollback implications.
- Technical Manager's actual decision, date, and version.

The ADR does not exist yet because the team has not made those decisions. An agent may propose alternatives; the named people accept them.

## Later increments

Receipt parsing and duplicate policy, trolley granularity, FIFO rules, hold/release behavior, charging measurements, reports, and hardware connections each need their own requirement and verification scope. Automatic charging is outside the initial pilot until explicitly approved.
