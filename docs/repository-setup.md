# Repository setup and first run

## Technical Manager: configure the cohort

1. Use a private training repository. Invite the actual participants through GitHub Settings and assign their roles in TEAM.md. Do not put guessed usernames into CODEOWNERS.
2. Confirm Issues are enabled. The forms appear under **Issues → New issue** after they are on the default branch.
3. Open **Actions → CI** and inspect the first run. Record its URL, commit SHA, SDK version, restore/build/test results, and missing checks in the foundation issue.
4. Confirm Copilot and the intended agent features are available under your account/organization policy. Never assume cloud execution, review, or usage capacity from this repository's files.
5. Where the GitHub plan permits, protect `main`: use PRs, independent human review, and successful CI checks (`Training content` and `.NET build and smoke tests`). Configure these after a real run registers the checks. Restrict bypass and direct pushes as appropriate.
6. If those controls are unavailable for this private repository, retain privacy and use the same review checklist manually. Record that the checks are a team procedure rather than an enforced branch rule.
7. Optional: create a GitHub Project using the statuses in the playbook. Otherwise record `Status` in issue bodies. Additional labels are optional; forms work without custom labels.
8. Appoint the four role owners. Add real CODEOWNERS entries later if desired; a person cannot independently approve their own PR.

## Working with Excel and GitHub in the browser

- Copy the tables in [Excel tracking](excel-tracking.md) into Excel sheets.
- Create requirement, implementation, and defect issues with the provided forms.
- Use GitHub's file editor to propose documentation changes on a branch and open a PR.
- If cloud-agent execution is enabled, select the relevant custom agent in the available Copilot task/issue interface, give it a bounded issue, and inspect its branch/PR and evidence. See [the prompt guide](copilot-guide.md).
- GitHub Actions provides a hosted build/test environment. Inspect results in the Actions and PR checks views.
- If executable agent access is unavailable, the team can practice BA/QA/review work in GitHub and Excel. A Developer needs a .NET 10 development environment to perform the coding labs; arrange that before promising a browser-only implementation session. A chat answer alone does not execute tests.

No external application AI API key is required. This course uses AI to assist engineering; adding an AI feature to the R2G product is a separate requirement.

## Starter verification

The initial application has no database or business modules. Expected CI sequence:

1. Validate training links, forms, profiles, skills, and synthetic fixture.
2. Install a released .NET 10 SDK.
3. Restore and build the solution.
4. Run the two HTTP integration smoke cases.
5. Retain the TRX result artifact when available.

The initial dependency versions are explicit; a generated NuGet lock file has not been fabricated. Once a real restore succeeds, the Developer can add and review package lock files and enable locked restore as a foundation improvement. Runtime, database, and end-to-end evidence must be collected from actual executions.

## Decisions to make before later modules

Agree UI requirements, identity/roles, audit identity, persistence/SQL schema, migrations, test database lifecycle, concurrent update strategy, deployment target, and plant integration boundaries. Keep the first application small while these decisions are made.

## Official references

- [Copilot agent configuration](https://docs.github.com/en/copilot/reference/custom-agents-configuration)
- [Copilot skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)
- [Repository instructions](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions)
- [Protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- [.NET setup action](https://github.com/actions/setup-dotnet)
