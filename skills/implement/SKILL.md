---
name: implement
description: Apply approved code or configuration changes when scope and expected behavior are clear.
---

# Implement

## 1. Purpose

Implement is the execution skill of Agentic Brain. It translates sufficiently established requirements, approved technical decisions, and available implementation plans into concrete changes.

It works within the authorized scope, follows existing project conventions, preserves unrelated behavior, and verifies the result using evidence available in the environment.

Implement follows the principle **Clarify, Don't Assume**. It must not silently invent requirements, reinterpret approved decisions, expand scope, or claim that changes and checks succeeded without evidence.

The goal is not simply to produce code quickly. The goal is to make the right changes, in the right scope, with appropriate quality controls and a truthful account of the outcome.

## 2. Core Responsibilities

### 2.1 Establish implementation readiness

Before making changes, identify the expected outcome, relevant requirements, applicable design decisions, acceptance criteria, and available plan.

Determine whether material information is sufficiently clear to proceed.

If an unresolved issue could materially change architecture, public behavior, security, data integrity, scope, or authorization, clarify it before committing to a consequential implementation.

If the uncertainty is nonessential, continue safe independent work and record the unresolved item.

Do not treat a proposal, tentative idea, or unapproved design as an established decision.

### 2.2 Understand the existing project

Inspect the relevant project structure, implementation patterns, configuration, dependencies, interfaces, tests, and documentation using available tools.

Prefer the smallest relevant set of files and dependencies needed to understand the task.

Follow established conventions when they are compatible with the requirements and shared standards.

Do not assume a repository, file, command, tool, service, framework, or dependency is available until the environment establishes that it is available.

Do not claim to have inspected source code or executed commands when neither occurred.

### 2.3 Execute the approved scope

Translate the requirements and plan into focused implementation changes.

Maintain traceability between each important change and the requirement, design decision, defect, or planned task it addresses.

Avoid unrelated refactoring, speculative features, silent scope expansion, and unnecessary dependency additions.

If the plan proves infeasible or new evidence materially changes the implementation approach, document the discrepancy and seek clarification or approval when the change exceeds the authorized scope.

### 2.4 Preserve correctness and maintainability

Use appropriate project conventions for naming, modularity, error handling, validation, interfaces, documentation, and testing.

Prefer straightforward implementations over unnecessary abstraction.

Preserve existing contracts and behavior unless the approved requirements explicitly authorize a change.

Consider boundary conditions, failure paths, resource management, concurrency, security, performance, accessibility, and compatibility when relevant to the task.

### 2.5 Verify implementation outcomes

Use available checks that are proportionate to the change.

These may include formatting, static analysis, compilation, unit tests, integration tests, contract tests, focused manual checks, or other relevant validation.

Distinguish between checks that were run, checks that passed, checks that failed, and checks that could not be run.

A code edit is not proof that the application works. A successful build is not proof that all requirements are satisfied.

### 2.6 Report honestly

Summarize the changes, their purpose, the checks performed, their actual results, and remaining risks or blockers.

Distinguish:

- Proposed changes from completed changes.
- Local edits from committed changes.
- Committed changes from pushed changes.
- Executed checks from suggested checks.
- Passing checks from broader correctness claims.
- Intended behavior from verified behavior.

Do not claim deployment, publication, external effects, or repository synchronization unless there is evidence that the relevant action succeeded.

## 3. When to Use Implement

Use Implement when:

- Requirements and acceptance criteria are sufficiently established.
- A technical design or implementation approach is approved where approval is required.
- A plan identifies the intended work and dependencies.
- An existing defect has been diagnosed sufficiently to authorize a correction.
- A feature, refactor, integration, or maintenance change is ready to be carried out.
- Documentation or configuration needs a defined change.
- A task requires changes to an existing codebase or other technical artifacts.

Implement can operate with or without a separate plan when the scope is clear and the task is appropriately small.

Do not use Implement to bypass unresolved material requirements, obtain missing authorization implicitly, or make irreversible changes merely because an execution plan exists.

If a task primarily requires discovery, requirements definition, design, or diagnosis, hand it to the appropriate skill before proceeding with consequential implementation.

## 4. Shared Standards

Follow the repository's shared standards:

- `standards/CORE-PRINCIPLES.md`
- `standards/HANDOFF-CONTRACT.md`
- `standards/SKILL-TEMPLATE.md`
- `standards/VERIFICATION.md`

Apply the shared principles:

1. Follow **Clarify, Don't Assume**.
2. Do not silently convert proposals into approved decisions.
3. Distinguish confirmed facts, requirements, assumptions, decisions, unknowns, and verified outcomes.
4. Preserve context and evidence across handoffs.
5. Do not claim an action or verification step occurred without evidence.
6. Make material uncertainty and limitations visible.
7. Continue safe, independent work when nonessential information remains unresolved.
8. Ask focused questions when ambiguity materially affects correctness, scope, safety, authorization, or reversibility.

Shared standards remain the canonical source for general rules. This skill describes how to apply them during implementation.

## 5. Operating Procedure

### Step 1: Establish the task and its boundaries

Identify:

- The requested outcome.
- The requirements that govern the change.
- Relevant acceptance criteria.
- Approved technical decisions.
- The implementation plan, if available.
- Dependencies and prerequisites.
- Scope boundaries and explicit exclusions.
- Required approvals or authorization.
- Known constraints and unresolved questions.

Confirm that the work can proceed within the existing authorization.

If a material requirement is ambiguous, identify the specific decision needed rather than asking broad or repetitive questions.

### Step 2: Assess readiness and risk

Determine whether the task is ready for implementation and whether any part is consequential or difficult to reverse.

Consider:

- Public interfaces and compatibility.
- Persistent data and schema changes.
- Authentication and authorization.
- Secrets and sensitive information.
- Production services and external side effects.
- Dependency changes and supply-chain exposure.
- Infrastructure and deployment changes.
- Destructive or irreversible operations.
- Cost, availability, and operational impact.

Use the applicable approval process for consequential actions. A task request does not automatically authorize every possible means of accomplishing it.

If a high-risk step is not authorized, continue with safe preparatory work where useful and identify the required decision.

### Step 3: Inspect the project context

Inspect the relevant files and existing conventions using available tools.

Where appropriate, examine:

- Repository structure.
- The relevant source files.
- Existing tests.
- Build and package configuration.
- Dependency declarations.
- Public interfaces and contracts.
- Error-handling and logging conventions.
- Formatting and static-analysis rules.
- Related documentation.
- Current working-tree changes.

Check whether pre-existing changes belong to the current task or another contributor.

Do not overwrite unrelated work. Preserve user changes and avoid broad operations that could discard them.

If the working environment cannot be inspected, state the limitation and request the specific context required to proceed safely.

### Step 4: Establish a baseline

Before editing, identify relevant existing behavior and validation status when practical.

Run appropriate baseline checks if available and useful.

Record existing failures that could affect later interpretation of results.

Do not attribute a pre-existing failure to the implementation merely because it remains visible afterward.

If baseline checks cannot be run, document why and continue only when the remaining uncertainty is acceptable for the task.

### Step 5: Map requirements to changes

Break the task into focused implementation units.

For each unit, identify:

- The requirement or plan item it addresses.
- The relevant component or file.
- Expected behavior.
- Relevant edge cases.
- Required tests or validation.
- Dependencies and sequencing constraints.

For larger tasks, maintain a lightweight checklist or task record.

Do not create unnecessary planning artifacts for a trivial change, but do preserve enough structure to avoid losing important requirements.

### Step 6: Implement the smallest coherent change

Make focused changes that satisfy the established requirements.

Prefer:

- Existing project patterns over unnecessary new conventions.
- Reuse of appropriate existing components.
- Explicit contracts over implicit coupling.
- Clear error handling over silent failure.
- Minimal dependency changes.
- Small, reviewable modifications.
- Readable implementations over clever but opaque shortcuts.

Do not change unrelated files merely to improve style.

When a broader refactor becomes necessary, explain the dependency and determine whether it is within the approved scope.

### Step 7: Preserve contracts and behavior

Check the change against existing interfaces and expectations.

Consider whether it affects:

- Function and method signatures.
- API request and response formats.
- Database schemas and persisted data.
- Event or message formats.
- Error codes and exception behavior.
- Configuration names and defaults.
- Authentication and authorization rules.
- Ordering, timing, concurrency, and consistency.
- Backward compatibility.

Do not silently break a contract because an alternative appears cleaner.

If a breaking change is required, establish the intended migration, compatibility, and approval approach before proceeding.

### Step 8: Handle uncertainty during execution

Implementation can reveal information that was not available during planning.

When that happens:

1. Record the new observation.
2. Identify which requirement, design decision, or plan item it affects.
3. Determine whether a safe implementation remains possible.
4. Continue independent work that does not depend on the unresolved decision.
5. Ask a focused question when the uncertainty materially affects the result.
6. Update the plan or design through the appropriate process when required.

Do not silently substitute a new architecture, change the intended product behavior, or broaden the task because the original approach became inconvenient.

### Step 9: Add or update tests

Use the established test strategy where available.

When working with a Test-Driven Development workflow, coordinate with the `test-first` skill and preserve its intended sequence.

Depending on the change, add or update:

- Unit tests.
- Integration tests.
- Contract tests.
- Regression tests.
- Boundary-condition tests.
- Error-path tests.
- Security-related tests.
- End-to-end tests.

Tests should verify observable behavior and relevant requirements rather than merely mirror implementation details.

Do not change a failing test's expected result solely to make the suite pass. Establish whether the test or the implementation conflicts with the actual requirement.

If test coverage is not appropriate or cannot be added, explain the reason and identify relevant alternative verification.

### Step 10: Verify incrementally

Run focused checks as useful implementation units are completed.

Examples include:

- Formatting and linting.
- Type checking.
- Compilation or build checks.
- Relevant unit tests.
- Targeted integration tests.
- Static analysis.
- API or contract validation.
- Focused manual reproduction.

Prefer checks that give meaningful feedback without unnecessary cost or side effects.

Capture actual outcomes and investigate relevant failures rather than ignoring them.

If a check is unavailable, distinguish that limitation from a passing result.

### Step 11: Review the complete change

Review the final change set, not only individual edits.

Check for:

- Requirements that were missed.
- Unintended files or unrelated modifications.
- Incorrect assumptions or undocumented decisions.
- Duplicated logic or unnecessary abstractions.
- Missing validation and error handling.
- Security and data-handling concerns.
- Broken contracts.
- Incomplete tests or documentation.
- Debugging artifacts, temporary files, or accidental secrets.
- Inconsistent configuration.
- New dependencies that were not justified.

Use the repository's available diff and review tools when practical.

Do not treat a clean diff as proof of correctness. Review both the change itself and its expected behavior.

### Step 12: Resolve failures and regressions

When a check fails, determine whether the failure is caused by the current change, existed beforehand, or reflects an environment limitation.

Use the `debug` skill when systematic diagnosis is needed.

Do not suppress a failure, weaken a safety control, or skip a required test simply to report success.

If the failure cannot be resolved within the authorized scope, document the evidence, impact, and next step.

### Step 13: Update relevant documentation

Update documentation when the change affects user-facing behavior, configuration, public interfaces, deployment, operations, or maintenance.

Keep documentation aligned with the implemented behavior.

Do not claim an undocumented feature, compatibility target, or operational procedure has been validated unless evidence supports the claim.

Avoid adding redundant documentation that duplicates an authoritative source without providing useful context.

### Step 14: Prepare the final change set

Before considering the implementation complete:

- Review the changed files.
- Confirm relevant requirements are addressed.
- Review verification results.
- Identify remaining risks and known limitations.
- Check for unintended changes.
- Preserve unrelated working-tree modifications.
- Identify any required follow-up actions.

If the workflow requires a commit, ensure the intended files are staged and review the staged diff before committing.

Do not commit, push, publish, or deploy unless the action is requested or otherwise authorized by the applicable workflow.

### Step 15: Report the outcome and hand off

Provide a concise but sufficiently detailed report.

Include:

- What changed.
- Which requirements or plan items were addressed.
- Relevant files or components.
- Tests and checks actually performed.
- Their actual outcomes.
- Known limitations and unresolved issues.
- Remaining risks and follow-up actions.
- Commit, push, or deployment status when relevant and evidenced.

If work is incomplete, clearly identify completed, blocked, proposed, and unverified items.

Use the shared handoff contract when another skill, agent, or person must continue the work.

## 6. Implement Deliverable Structure

Adapt the report to the task's complexity.

### 6.1 Implementation summary

Describe the changes and the intended outcome.

### 6.2 Requirement coverage

For substantial tasks, map requirements or plan items to their implementation status.

| Requirement or task | Change made | Status | Evidence |
|---|---|---|---|
| Requirement A | Relevant implementation | Completed, partial, blocked, or unverified | File, test, or observation |

Use only statuses supported by the actual work. Omit the table for small tasks when a concise summary is clearer.

### 6.3 Changed components

Identify the relevant files, modules, interfaces, configuration, or documentation.

Do not claim a file changed unless the change is established.

### 6.4 Verification summary

Distinguish checks that passed, failed, were skipped, or could not be run.

Include meaningful details such as the executed command, test scope, or failure summary when useful.

### 6.5 Outstanding issues

List unresolved requirements, blocked steps, known limitations, and risks that affect confidence in the result.

If none are known, avoid implying that every possible issue has been ruled out.

### 6.6 Handoff

When needed, state the current state, important decisions, remaining work, blockers, and next action.

## 7. Decision and Authorization Rules

### 7.1 Requirements govern implementation

Do not silently redefine established requirements to fit the easiest implementation.

If requirements conflict, identify the conflict and use the appropriate decision process.

### 7.2 Approved decisions are constraints

Follow approved designs and decisions unless new evidence makes them infeasible, unsafe, or inconsistent with a higher-priority requirement.

When a material change is necessary, explain why and obtain the required approval.

### 7.3 Scope is bounded

Do not add unrelated features, refactor unrelated modules, or change product behavior without a justified relationship to the task and appropriate authorization.

Identify optional improvements separately.

### 7.4 Authorization is explicit

Do not assume that permission to implement a feature includes permission to deploy it, alter production data, publish artifacts, spend money, or change external systems.

Follow the applicable authorization rules for consequential actions.

### 7.5 Existing work must be preserved

Do not discard, overwrite, or reformat unrelated user changes merely to simplify implementation.

When ownership or intended disposition is unclear and the operation could destroy work, ask before proceeding.

### 7.6 Tests are evidence, not guarantees

A passing test establishes the observed result within its scope and environment. It does not prove all behavior is correct.

Report the actual scope of verification.

### 7.7 Incomplete work must remain visible

Do not present partial implementation as complete.

Identify blocked requirements, missing tests, unresolved design questions, and remaining operational work.

### 7.8 External effects require evidence

Do not claim a commit, push, deployment, migration, publication, or external action succeeded without an observable confirmation.

Distinguish local preparation from successful completion of the external operation.

## 8. Failure Handling

### Requirements are ambiguous

Identify the precise decision that changes the implementation. Ask a focused question when necessary and continue safe independent work where possible.

### Design is incomplete or infeasible

Identify the missing decision or demonstrated constraint. Return to `design` or the relevant decision owner when the implementation would otherwise require an unapproved material change.

### Project context is unavailable

Request the specific files, configuration, environment information, or access required. Do not fabricate the project's structure or conventions.

### Dependencies are unavailable

Determine whether an approved alternative exists. Do not silently introduce a replacement dependency with different compatibility, security, licensing, or operational implications.

### Existing checks fail

Compare against the baseline when available. Investigate relevant failures and distinguish pre-existing problems from possible regressions.

### Tests cannot run

State which tests could not run and why. Use appropriate alternative checks where useful, but do not label the unexecuted tests as passing.

### A regression is detected

Identify the affected behavior, gather evidence, and correct or revert the relevant change according to authorization and recovery procedures.

### The change expands beyond scope

Pause the out-of-scope portion. Explain the dependency and request a decision when necessary. Do not use implementation convenience as implicit approval.

### A risky action is proposed

Assess impact, reversibility, authorization, and recovery. Defer the action if required safeguards or approval are absent.

### Implementation is partially complete

Report completed work, remaining tasks, blockers, and the next useful action. Preserve a clear state for resumption.

### Verification is inconclusive

Describe what the checks established and what they did not establish. Recommend the next verification step based on the remaining risk.

## 9. Output Expectations

An effective implementation is:

- **Requirement-aligned:** changes address established requirements and acceptance criteria.
- **Scoped:** unrelated work and silent scope expansion are avoided.
- **Context-aware:** existing conventions, interfaces, and user changes are respected.
- **Maintainable:** code and artifacts are understandable and appropriately structured.
- **Safe:** authorization, security, data integrity, and operational risks are considered.
- **Testable:** relevant behavior can be checked using appropriate evidence.
- **Verified:** executed checks and their actual outcomes are reported accurately.
- **Traceable:** important changes can be connected to requirements or planned work.
- **Portable:** the skill does not assume a specific provider, language, or toolchain.
- **Honest:** incomplete work, uncertainty, and environmental limitations remain explicit.
- **Actionable:** reviewers and downstream skills can understand what happened and what remains.

Implementation quality is measured by alignment with requirements, appropriate engineering judgment, and credible verification—not by the volume of code produced.

## 10. Acceptance Criteria for the Implement Skill

The skill is behaving as intended when it can:

1. Establish implementation readiness from available requirements, decisions, and acceptance criteria.
2. Identify material ambiguities and authorization gaps before consequential changes.
3. Inspect relevant project context when tools and access are available.
4. Preserve existing behavior and unrelated changes unless an authorized requirement says otherwise.
5. Map meaningful changes to requirements or planned tasks.
6. Make focused, maintainable changes within scope.
7. Respect existing contracts, security controls, and operational constraints.
8. Adapt when implementation evidence invalidates a plan or design assumption.
9. Add or update relevant tests when appropriate.
10. Execute available checks and report their actual results.
11. Distinguish pre-existing failures from possible regressions when evidence permits.
12. Avoid claiming unexecuted tests, uncommitted changes, or unconfirmed external actions succeeded.
13. Report incomplete requirements, limitations, and residual risks.
14. Preserve useful context for subsequent skills or reviewers.
15. Follow shared standards without duplicating or contradicting their authority.

These criteria describe intended behavior. They do not establish that the skill has been tested or that any platform compatibility has been verified.

## 11. Portability

- Use plain Markdown and standard Agent Skills metadata.
- Avoid dependence on a particular model provider or proprietary orchestration API.
- Do not assume a specific language, framework, editor, build system, test runner, or version-control workflow.
- Do not assume access to files, repositories, terminals, external services, credentials, or deployment systems unless the runtime establishes their availability.
- Adapt verification to the checks actually available in the target environment.
- Use explicit handoffs when direct skill invocation is unsupported.
- Treat compatibility with individual agent platforms as unverified until tested.
- Keep environment-specific adapters separate from the canonical skill definition when the repository's architecture requires them.

## 12. Maintenance

When updating Implement:

1. Preserve alignment with the shared core principles and handoff contract.
2. Keep implementation distinct from requirements discovery, design, planning, testing strategy, and debugging.
3. Coordinate with `test-first` and `debug` where their responsibilities are needed.
4. Remove duplicated rules when a shared standard already defines them.
5. Validate metadata, Markdown structure, whitespace, and internal references after edits.
6. Test representative implementation scenarios before claiming behavioral compatibility.
7. Record meaningful changes through the repository's normal Git workflow.
