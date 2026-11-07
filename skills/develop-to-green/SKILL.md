---
name: develop-to-green
description: Implement an approved, evaluated software plan and iterate until its skill evals and applicable unit tests pass. Use after the phase plan and pre-development checks are complete.
---

# Develop to green

Use this skill to carry an authorized development phase from its reviewed plan through verified completion. Keep implementation tied to the plan and acceptance criteria.

## Perspectives

- Use the Implementation Engineer viewpoint to make focused, maintainable changes that fit existing project conventions.
- Use the Code Reviewer and Test Strategist viewpoint to inspect failures, verify evidence, and protect requirement coverage.

## Workflow

1. **Check the gate.** Read the approved plan, applicable `AGENTS.md`, repository instructions, and relevant implementation and evaluation conventions. Confirm that the current phase's skill eval scenarios are defined and reviewed before implementation. If code is in scope, confirm runnable unit tests were written before production implementation and cover applicable acceptance criteria, meaningful branches, boundaries, invalid input, and failure paths. If any gate is missing or unclear, stop before implementation, report the gap, and return to `define-testcases` or the plan owner.
2. **Establish the baseline.** Inspect current repository status, relevant files, and any existing eval/test results. Preserve unrelated work. Run the relevant baseline checks when safe and useful, and record what fails before the change.
3. **Implement in scope.** Make the smallest coherent change that satisfies the approved acceptance criteria. Follow project conventions and avoid unrelated cleanup or opportunistic changes.
4. **Run and inspect checks.** Run the applicable skill evals and, whenever code is involved, the defined unit tests. Review actual output and coverage reports when the project configures them. Connect each result to its acceptance criterion. Do not infer success from test names, exit status without output review, or a green subset.
5. **Iterate on failures.** Diagnose each failed or incomplete check, make a focused change, then rerun the affected checks and any regression checks needed. Repeat until every defined case and applicable unit test passes. If a check cannot be run, report it as incomplete and explain the blocker; do not claim the phase is complete.
6. **Review case accuracy.** If a case appears inconsistent with an agreed requirement, identify the exact conflict and determine whether the implementation or case is wrong. Change a case only when evidence shows it is inaccurate or the requirement changed. Document the reason, preserve the original coverage, and rerun the corrected case. Never weaken or remove a valid expectation just to get a pass.
7. **Review the final change.** Inspect the final diff for scope, correctness, regressions, and preserved user work. Summarize changed files, acceptance-criteria evidence, eval and test outcomes, and any remaining limitations. Follow repository-specific approval rules for commits or pushes; this skill does not authorize either operation by itself.

## Completion

Report the phase complete only after every defined skill eval and applicable unit test has passed and the results have been reviewed against the acceptance criteria. For code, report coverage evidence when configured and identify any untested areas. If any check is failing, blocked, or unrun, report the phase as incomplete with the exact remaining work.

## Iteration and handoff

Keep a concise durable handoff in the active session or project record when the work spans chats. Record the current phase, completed changes, failing or pending checks, relevant evidence, and next action. Resume by rechecking repository status and the recorded gate rather than assuming prior state.
