---
name: define-testcases
description: Turn a completed plan into clear, reviewable eval scenarios before implementation. Use when a planned phase needs its acceptance criteria mapped to manual skill evaluations or executable tests.
---

# Define test cases

Use this skill after the plan for a phase is complete and before implementation starts. It turns agreed requirements into cases that can show whether the planned work behaves as intended.

## Perspectives

- Use the Requirements Analyst viewpoint to map confirmed outcomes, constraints, and open questions.
- Use the Code Reviewer and Test Strategist viewpoint to make cases observable, appropriately scoped, and useful for checking regressions and failure modes.

## Workflow

1. **Check readiness.** Read the completed plan, applicable `AGENTS.md`, relevant source and project instructions, and the existing evaluation and test conventions. Confirm the planned phase and its acceptance criteria. If the plan is unfinished or a material requirement is unclear, ask one focused question or mark that item open; do not invent an expectation.
2. **Map requirements to evidence.** For each acceptance criterion, identify a scenario and the response, file, behavior, or command result a reviewer can observe. Call out any criterion that has no meaningful check and explain why.
3. **Define skill eval scenarios.** For each in-scope skill, write realistic positive triggers, negative triggers that belong to neighboring skills where possible, and at least one behavioral evaluation. Keep prompts natural rather than copying the skill description. Make behavioral pass criteria observable and tied to the agreed requirements.
4. **Write unit tests for code.** Whenever the plan includes production code, scripts, or other executable behavior, define and write runnable unit tests before implementation, using the project's existing test framework and conventions. Cover each applicable functional acceptance criterion and the meaningful branches, boundaries, invalid inputs, and failure paths; use configured coverage reports where available to find gaps. Do not invent a percentage threshold when the project has none. Do not implement production behavior while defining tests.
5. **Use representative fixtures.** Add only the smallest sanitized fixtures needed to exercise the case. Never place secrets, credentials, client data, or unrelated project content in fixtures.
6. **Save in the project convention.** For manual Agentic Brain skill evaluations, add one JSON case per skill under `evaluations/cases/` with `subject`, `positive_triggers`, `negative_triggers`, and `behavioral_evaluation` fields. Match the existing case format. Update `evaluations/README.md` so reviewers can find the cases. For executable tests, use the repository's established test directories and naming.
7. **Review coverage and boundaries.** Check that cases cover activation, appropriate non-activation, and required behavior. Include edge and failure scenarios where they matter. Check neighboring skills for trigger overlap and keep ownership clear. Do not add a separate skill's workflow to a case unless the scenario tests their handoff.
8. **Validate the artifacts.** Check case syntax, test syntax, and links. Confirm each pass criterion can be assessed from observable evidence. Report that cases and tests are defined, not passed; they have not been executed merely because they were written or validated.

## Case changes

If a case appears inaccurate or the agreed requirements change, cite the conflict, document the reason for the change, preserve the original requirement coverage, and review the revised case. Never change expected behavior just to make implementation pass. The later implementation workflow must rerun a corrected case.

## Common shortcuts to avoid

| Shortcut | Why to avoid it |
|---|---|
| “We can add evals after implementation.” | This project requires eval scenarios to be reviewed before each phase starts. |
| “The positive example is enough.” | Negative triggers expose when a neighboring skill should own the request. |
| “The case passed because it looks complete.” | A case is only passed after its expected behavior is observed and evidence is recorded. |

## Completion

The case files are saved and indexed; each in-scope acceptance criterion maps to an observable check or an explicit open item; relevant positive, negative, and behavioral scenarios are present; and runnable unit tests covering applicable requirements and meaningful edge/failure cases are written whenever code is in scope. Report any unrun checks as incomplete. Do not implement production behavior or claim any eval or test passed from case creation alone. The development phase cannot succeed until all defined evals and applicable unit tests pass.
