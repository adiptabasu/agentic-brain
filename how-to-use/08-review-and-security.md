# Review a change for quality and security

Use this before accepting a consequential change, merging work, or preparing a release. Review is an assessment, not an instruction to modify the code.

## Request an independent review

Provide the relevant repo, branch or diff, requirements, and any checks already run. Then say:

> Read `skills/review/SKILL.md` and follow it. Independently review [commit, branch, PR diff, or paths] against these requirements: [requirements]. Check for correctness defects, regressions, maintainability issues, compatibility concerns, and missing tests. Do not make edits. Report actionable findings first with file and line references, or explicitly say if you found none within the review scope.

Do not tell the reviewer what conclusion to reach. Include build/test results as evidence, not as a substitute for reviewing the code.

## Add a security and safety assessment where appropriate

If the change affects authentication, authorization, input handling, secrets, sensitive data, network boundaries, execution, or other meaningful risk, invoke `shield` separately:

> Read `skills/shield/SKILL.md` and follow it for [change/system]. Identify assets, trust boundaries, plausible threats, existing controls, gaps, and proportionate mitigations. Distinguish observed controls from assumptions. Do not change the system.

For a change without meaningful security impact, do not run a security assessment just to add process overhead.

## Decide what to do with findings

Ask the reviewer to distinguish defects from suggestions and note the evidence or uncertainty for each. If you accept a finding, use the appropriate implementation or debug workflow; do not have the reviewer silently make the fix. Afterward, review and verify the new diff.

If no issues are reported, interpret that only within the stated scope. A review is not proof that the code has no bugs, a complete security audit, or test coverage. Use `verify` to check acceptance criteria and evidence independently.
