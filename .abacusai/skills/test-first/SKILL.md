---
name: test-first
description: Define and validate expected behavior before implementation using acceptance criteria, meaningful tests, failing baselines, and evidence-based verification. Use when developing features, fixing defects, changing existing behavior, or establishing a reliable test strategy before or alongside implementation.
---

# Test First

## 1. Purpose

Test First establishes an evidence-driven development workflow in which expected behavior is made explicit and testable before implementation is considered complete.

It helps translate requirements into acceptance criteria, select appropriate tests, expose incorrect or missing behavior, guide implementation through feedback, and verify the resulting change.

The core principle is **Clarify, Don't Assume**. Tests should encode confirmed requirements and authorized decisions, not silently turn guesses into expected behavior.

Test First encourages a test-driven development cycle where appropriate, but it does not require every change to follow an identical sequence. The approach must fit the task, the available test environment, the project's existing practices, and the risks involved.

Test First does not independently authorize scope changes, guarantee correctness, or claim that tests passed without execution evidence.

## 2. Core Responsibilities

### 2.1 Establish expected behavior

Identify the requirements, intended behavior, constraints, and acceptance criteria relevant to the change.

Distinguish:

- Confirmed behavior from proposed behavior.
- Required behavior from optional improvements.
- Explicit requirements from assumptions.
- Observable outcomes from implementation details.
- Existing behavior that must be preserved from behavior intentionally being changed.

If a material ambiguity would change what a test should assert, ask a focused clarification question or define clearly separated conditional test cases.

### 2.2 Design useful tests

Select tests that provide meaningful evidence about the expected behavior.

Consider:

- Normal and successful cases.
- Boundary conditions and edge cases.
- Invalid inputs and failure behavior.
- Relevant regression cases.
- State transitions and interactions.
- Integration boundaries and external dependencies.
- Security, privacy, authorization, and data integrity where applicable.

Prioritize tests by risk and value rather than maximizing test count.

### 2.3 Establish a baseline

When practical, run relevant existing tests before changing behavior.

Record whether the baseline passes, fails, is incomplete, or cannot be executed.

For a test-driven workflow, create a test that expresses the desired behavior and demonstrate that it fails for the intended reason before implementing the change.

A failing baseline may be unavailable or inappropriate for some tasks. If so, explain why rather than fabricating a failure.

### 2.4 Guide implementation through feedback

Use test outcomes to identify the gap between expected and actual behavior.

Encourage the smallest implementation that satisfies the agreed behavior while preserving existing contracts and constraints.

Avoid changing production behavior, expected results, or requirements merely to make a test pass.

When a test reveals an incorrect assumption or an ambiguous requirement, resolve that issue explicitly before treating the test as authoritative.

### 2.5 Verify and report evidence

Distinguish tests that are:

- Planned.
- Specified but not written.
- Written but not executed.
- Executed and passed.
- Executed and failed.
- Blocked or skipped.
- Inconclusive due to environment or test limitations.

Report the relevant commands, outcomes, and limitations when that evidence is available.

Passing tests provide evidence for the behaviors they cover. They do not establish universal correctness, complete security, or the absence of defects.

### 2.6 Preserve existing behavior

Identify existing contracts and behaviors that could be affected by the change.

Use regression tests where practical to detect unintended changes.

Do not treat an existing implementation's behavior as a requirement merely because it exists. If current behavior conflicts with an established requirement, expose the conflict and follow the authorized decision.

## 3. When to Use Test First

Use Test First when:

- Implementing a new feature or behavior.
- Fixing a defect with a reproducible or specified expected outcome.
- Refactoring code while preserving behavior.
- Changing public interfaces, data formats, or integration contracts.
- Introducing validation, authorization, or security-sensitive behavior.
- Migrating data or modifying persistence logic.
- Investigating regressions or unexpected outcomes.
- Establishing acceptance criteria for work that needs reliable verification.

For low-risk documentation-only changes, exploratory research, or tasks without executable behavior, a lightweight review or explicit checklist may be more appropriate than creating automated tests.

Do not force unit tests where the relevant behavior can only be meaningfully evaluated through integration, system, usability, or other forms of verification.

## 4. Shared Standards

Follow the repository's shared standards:

- `standards/CORE-PRINCIPLES.md`
- `standards/HANDOFF-CONTRACT.md`
- `standards/SKILL-TEMPLATE.md`
- `standards/VERIFICATION.md`

Apply the shared principles:

1. Follow **Clarify, Don't Assume**.
2. Do not treat silence as approval.
3. Distinguish confirmed requirements from proposals and assumptions.
4. Preserve context and decision history across handoffs.
5. Do not claim tests ran, passed, or verified a behavior without evidence.
6. Make material uncertainty and environmental limitations visible.
7. Continue safe, independent work when a nonessential unknown remains unresolved.
8. Ask focused questions when ambiguity materially affects expected behavior, safety, authorization, or correctness.

Shared standards remain the canonical source for general rules. This skill defines their application to test design and test-driven development.

## 5. Operating Procedure

### Step 1: Establish the change and its objective

Identify the feature, defect, refactor, migration, or other change being evaluated.

Establish:

- Intended behavior or outcome.
- Relevant requirements and constraints.
- Existing behavior that must be preserved.
- Scope and exclusions.
- Acceptance criteria.
- Relevant risks and affected components.

Use the available project context and artifacts. Do not claim to have inspected source code, tests, build configuration, or execution environments unless they were actually available.

If the expected outcome is materially ambiguous, clarify it before writing assertions that would commit to one interpretation.

### Step 2: Identify observable behavior

Translate the objective into outcomes that can be observed or evaluated.

For each important behavior, identify:

- Preconditions.
- Input or triggering event.
- Expected result.
- Relevant state changes or side effects.
- Expected error or rejection behavior.
- Constraints that must remain true.

Prefer behavior-oriented assertions over tests that merely mirror internal implementation details.

Use implementation-specific assertions only when the internal contract itself is relevant, such as a required algorithmic complexity, resource constraint, or architectural boundary.

### Step 3: Assess testability and environment

Determine which testing approaches are available and appropriate.

Consider:

- Existing test frameworks and conventions.
- Unit, component, integration, contract, system, end-to-end, and manual testing.
- Required databases, services, credentials, fixtures, or test data.
- Determinism and reproducibility.
- Runtime, build, and environment limitations.
- Security and privacy constraints.
- Cleanup and isolation requirements.

Do not assume a test framework, dependency, service, or environment exists. Inspect the available project context when access permits.

If the environment is unavailable, identify what can still be specified or reviewed and what remains unverified.

### Step 4: Establish the baseline

When relevant, run the existing test suite or a focused subset before changing behavior.

Record:

- What was run.
- Whether it completed.
- The observed result.
- Any existing failures.
- Environmental warnings or limitations.
- Which tests were not run.

A baseline failure should not automatically be attributed to the proposed change. Separate pre-existing failures from new failures using available evidence.

If no execution environment is available, mark the baseline as unavailable rather than implying it passed.

### Step 5: Prioritize test scenarios

Select test scenarios based on risk, expected behavior, and likely failure modes.

Consider the following categories where relevant:

**Normal cases**

- Typical valid inputs.
- Expected successful outcomes.
- Common state transitions.

**Boundary cases**

- Minimum and maximum permitted values.
- Empty collections or strings.
- Missing optional values.
- Repeated or duplicate inputs.
- Off-by-one conditions.

**Invalid and failure cases**

- Malformed inputs.
- Unsupported operations.
- Dependency failures.
- Timeouts and interrupted operations.
- Rejected requests and invalid state transitions.

**Regression cases**

- Previously reported defects.
- Known fragile behavior.
- Existing contracts that the change could break.

**Security and integrity cases**

- Unauthorized access.
- Invalid trust boundaries.
- Sensitive data exposure.
- Injection and validation failures.
- Duplicate processing or inconsistent state, where applicable.

Do not mechanically include every category. Select those justified by the behavior and risk.

### Step 6: Write acceptance criteria and tests

Create testable acceptance criteria before implementation is treated as complete.

Where useful, express a criterion as:

- Given a known starting condition.
- When an action or event occurs.
- Then an observable outcome must hold.

Each important criterion should have a corresponding test or an explicit explanation of how it will be verified.

Tests should be:

- Focused on a defined behavior.
- Deterministic where practical.
- Independent of unrelated test execution order.
- Clear about inputs and expected outcomes.
- Maintainable as requirements evolve.
- Proportionate to the risk and complexity of the change.

Avoid tests that pass regardless of the result, assert irrelevant details, duplicate coverage without benefit, or depend on undocumented environmental state.

### Step 7: Demonstrate a failing test when appropriate

In a test-driven development cycle:

1. Write the smallest meaningful test for the desired behavior.
2. Run it against the current implementation.
3. Confirm that it fails for the expected reason.
4. Investigate unexpected failures before proceeding.

The intended red state is evidence that the test can detect the missing or incorrect behavior.

A failure caused by a syntax error, broken test setup, missing dependency, or unrelated environment problem does not demonstrate that the behavioral test is effective.

Do not deliberately break unrelated functionality merely to produce a failing test.

If a failing baseline cannot reasonably be demonstrated, document the limitation and proceed using another suitable verification strategy.

### Step 8: Implement the minimum necessary behavior

Implement the change needed to satisfy the established criteria.

Preserve:

- Existing contracts not authorized to change.
- Agreed interfaces and design decisions.
- Security and data integrity requirements.
- Relevant error-handling behavior.
- Explicit scope boundaries.

Avoid unnecessary production changes or test-only shortcuts that conceal defects.

Do not weaken assertions, remove meaningful tests, hardcode test-specific outcomes, or change expected behavior solely to achieve a green result.

If implementation reveals a genuine ambiguity or missing requirement, pause the affected decision and clarify it.

### Step 9: Run focused tests and observe the result

Run the relevant test or smallest useful test group after implementation.

Compare actual results with expected results.

For failures:

1. Capture the observed failure.
2. Determine whether it reflects the implementation, test, setup, environment, or requirement.
3. Gather evidence before choosing a cause.
4. Correct the appropriate issue.
5. Rerun the affected test.

Do not repeatedly modify code without a testable hypothesis about the failure.

### Step 10: Run regression and broader verification

Once focused tests pass, run additional relevant tests based on the scope and risk of the change.

Consider:

- Related unit tests.
- Integration and contract tests.
- Regression suites.
- Static analysis and type checking.
- Build and packaging checks.
- Security checks.
- Migration or compatibility tests.
- Manual verification for behavior that automated tests cannot adequately assess.

Choose a suitable verification scope rather than assuming that every task requires the entire test suite.

Record any skipped tests and explain their relevance.

### Step 11: Review test quality

Evaluate whether the tests provide meaningful evidence.

Check that:

- Assertions correspond to confirmed requirements.
- Failure cases test the intended behavior.
- Tests can detect plausible defects.
- Fixtures and mocks do not conceal the behavior under test.
- Tests do not depend unnecessarily on execution order or external state.
- Regression coverage addresses the affected behavior.
- Test names and structure make failures understandable.
- Security-sensitive paths receive appropriate coverage.
- Test setup and cleanup are reliable.

Passing tests alone do not establish that the tests themselves are sufficient or correct.

### Step 12: Reconcile results with acceptance criteria

For each acceptance criterion, record its status and supporting evidence.

Distinguish:

- Satisfied by observed evidence.
- Failed by observed evidence.
- Not tested.
- Blocked.
- Inconclusive.
- No longer applicable following an authorized requirement change.

If a criterion is not satisfied, explain the gap and identify the next action.

Do not mark the overall change as verified if material acceptance criteria remain unresolved.

### Step 13: Report the outcome

Provide a concise evidence-based summary containing, as appropriate:

- The intended behavior.
- Tests added or updated.
- Implementation changes made.
- Commands or procedures executed.
- Actual test results.
- Existing or newly discovered failures.
- Verification not performed.
- Environmental limitations.
- Remaining risks or acceptance gaps.
- Recommended next action.

Use exact results from available evidence. Do not invent test counts, pass rates, coverage percentages, or execution details.

### Step 14: Hand off unresolved work

If another person, agent, or workflow must continue, provide:

- The objective and relevant context.
- Confirmed acceptance criteria.
- Tests written and their current status.
- Commands already executed.
- Actual outcomes and failure details.
- Unresolved questions and blockers.
- Required environment or dependencies.
- The next recommended action.

Follow the shared handoff contract and preserve the distinction between planned and completed work.

## 6. Test Design and Deliverable Structure

Adapt the deliverable to the task. A small defect may require a few focused tests, while a high-risk change may need a formal test plan and traceability matrix.

### 6.1 Behavior specification

Describe the expected outcome and relevant preconditions, inputs, state changes, side effects, and failure behavior.

### 6.2 Acceptance criteria

List observable criteria that define the required behavior.

Assign stable identifiers when several criteria need traceability.

### 6.3 Test scenario matrix

Use a table when it improves clarity.

| Field | Meaning |
|---|---|
| Test ID | Stable scenario reference |
| Criterion | Acceptance criterion covered |
| Scenario | Behavior being evaluated |
| Preconditions | Required starting state |
| Action or input | Event or input under test |
| Expected result | Observable required outcome |
| Test level | Unit, integration, contract, system, or manual |
| Status | Planned, written, passed, failed, blocked, or not run, as supported by evidence |
| Notes | Limitations, dependencies, or relevant observations |

Do not require every column for every task.

### 6.4 Baseline and execution record

Record relevant commands, test scope, environment, outcome, and limitations.

Distinguish the original baseline from results after the change.

### 6.5 Failure analysis

For material failures, record:

- Observed behavior.
- Expected behavior.
- Reproduction steps where available.
- Relevant logs or error details.
- Confirmed cause, if established.
- Competing hypotheses when the cause remains unknown.
- Proposed corrective action.

Do not present a hypothesis as a confirmed root cause.

### 6.6 Verification summary

Summarize which criteria are satisfied, which remain unresolved, and what evidence supports each conclusion.

### 6.7 Handoff

Provide the next action and preserve the test context, limitations, and outstanding work.

## 7. Decision and Authorization Rules

### 7.1 Requirements determine expected behavior

Tests must reflect established requirements or explicitly authorized decisions.

When the implementation and a test disagree, investigate the source of the disagreement rather than automatically changing either one.

### 7.2 A passing test is not blanket approval

A passing test establishes only that the test passed under the observed conditions.

It does not automatically authorize a release, approve a design, establish compliance, or prove that all relevant behaviors are correct.

### 7.3 Do not hide failures

Do not delete, skip, weaken, or rewrite a failing test merely to produce a passing suite.

A test may legitimately change when the requirement changes or the test is shown to be incorrect. Explain the reason and preserve the relevant decision history.

### 7.4 Preserve safety and authorization boundaries

Tests must not bypass required authorization, expose sensitive information, or create unsafe side effects.

Use controlled test data and environments appropriate to the risk.

Do not perform destructive tests against production or other sensitive systems without explicit authorization and suitable safeguards.

### 7.5 Distinguish planned and executed verification

A test plan is not evidence of execution.

A test file is not evidence that its tests passed.

A successful test run is not proof of universal correctness.

Report only the strongest conclusion supported by the available evidence.

### 7.6 Handle requirement changes explicitly

When a requirement changes, identify the affected acceptance criteria and tests.

Update them only after the change is sufficiently established or authorized. Do not quietly redefine the expected outcome to fit the current implementation.

## 8. Failure Handling

### Ambiguous expected behavior

Identify the competing interpretations and ask a focused question when the difference materially affects correctness.

Where useful, specify separate candidate scenarios without pretending one has been approved.

### Test fails before implementation

Determine whether the failure is caused by the intended missing behavior, a faulty test, setup, or environment.

Do not assume that any red test demonstrates the intended defect.

### Test fails after implementation

Compare actual and expected outcomes, investigate the cause, and correct the appropriate layer.

Avoid weakening the requirement or assertion without evidence.

### Existing baseline failures

Record pre-existing failures separately. Use focused execution or other evidence to determine whether the change introduced additional failures.

Do not attribute causality without supporting evidence.

### Flaky or nondeterministic tests

Investigate shared state, timing, concurrency, external dependencies, and environmental variation.

Record reproducibility and limitations. Do not treat a single successful rerun as proof that the underlying instability is resolved.

### Unavailable test environment

Specify which tests cannot run and why. Identify alternative evidence where appropriate and leave the affected criteria unverified.

### Missing test coverage

Identify the behavior or risk not covered, its significance, and the recommended next step.

Do not imply complete coverage from a green test suite.

### Conflicting tests and requirements

Identify the contradiction and the source of each expectation. Seek an authorized decision or correction rather than choosing whichever result is easiest to satisfy.

### Security-sensitive behavior

Use controlled test environments and appropriate safeguards. Do not create unsafe real-world side effects merely to demonstrate a test case.

## 9. Output Expectations

A useful Test First result is:

- **Behavior-focused:** tests correspond to observable expected outcomes.
- **Requirement-aligned:** assertions do not silently invent requirements.
- **Risk-aware:** edge cases and failure modes are selected according to relevance.
- **Reproducible:** execution conditions and outcomes are recorded where possible.
- **Diagnostic:** failures provide useful information about the violated expectation.
- **Proportionate:** test effort matches the complexity and risk of the change.
- **Regression-conscious:** relevant existing behavior is protected.
- **Evidence-based:** execution and verification claims match actual results.
- **Portable:** guidance does not depend on a particular model provider or test framework.
- **Honest:** skipped tests, environment limitations, and unresolved criteria remain visible.

The objective is not merely to achieve a green test suite. It is to obtain credible evidence that the intended behavior is implemented and that important unintended changes have been considered.

## 10. Acceptance Criteria for the Test First Skill

The skill is behaving as intended when it can:

1. Translate established requirements into observable acceptance criteria.
2. Identify material ambiguity before embedding an unsupported interpretation in tests.
3. Select meaningful test scenarios based on behavior and risk.
4. Establish a baseline when practical and report its actual outcome.
5. Demonstrate a meaningful failing test when appropriate.
6. Distinguish behavioral failures from test setup and environment failures.
7. Guide implementation without weakening requirements to make tests pass.
8. Recommend regression and broader verification proportionate to the change.
9. Identify gaps between acceptance criteria and available test coverage.
10. Distinguish planned, written, executed, passed, failed, blocked, and unrun tests.
11. Avoid unsupported claims about coverage, correctness, or compatibility.
12. Preserve authorization and safety boundaries during testing.
13. Provide a context-preserving handoff for unresolved work.
14. Follow shared standards without silently changing their meaning.
15. Adapt to different languages, frameworks, and test environments.

These criteria describe intended behavior. They do not establish that the skill has been tested or that any platform compatibility has been verified.

## 11. Portability

- Use plain Markdown and standard Agent Skills metadata.
- Avoid dependence on a particular model provider or proprietary orchestration API.
- Do not assume that a specific test framework, language, build system, or environment is available.
- Do not assume access to source files, execution tools, credentials, test data, or external services unless the runtime establishes their availability.
- Use explicit handoffs when direct skill invocation is unsupported.
- Treat compatibility with individual agent platforms as unverified until tested.
- Prefer test concepts that can be adapted to the project's established conventions.

## 12. Maintenance

When updating Test First:

1. Preserve alignment with the shared core principles and handoff contract.
2. Keep test design and verification distinct from implementation and authorization.
3. Prefer meaningful, maintainable tests over unnecessary test volume.
4. Remove duplicated rules when a shared standard already defines them.
5. Validate metadata, Markdown structure, whitespace, and internal references after edits.
6. Test representative scenarios before claiming behavioral compatibility.
7. Record meaningful changes through the repository's normal Git workflow.
