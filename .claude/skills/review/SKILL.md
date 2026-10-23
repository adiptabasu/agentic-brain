---
name: review
description: Independently evaluate code, configuration, documentation, and other technical changes against requirements, correctness, maintainability, security, compatibility, and available verification evidence. Use when reviewing a proposed or completed change before acceptance, merge, release, or handoff.
---

# Review

## 1. Purpose

Review provides a systematic, evidence-based assessment of proposed or completed changes.

It examines whether a change satisfies its intended requirements, introduces defects or regressions, respects project conventions, and presents acceptable security, maintainability, compatibility, and operational risks.

Review prioritizes actionable findings over stylistic preference. It identifies concrete problems, explains their impact, and provides sufficient evidence for another person to reproduce or evaluate each important finding.

Review follows the principle **Clarify, Don't Assume**. It must not silently invent requirements, assume tests passed, infer correctness from a successful build, or treat the absence of visible defects as proof that a change is defect-free.

Review is an assessment activity, not an automatic authorization to merge, deploy, publish, or otherwise accept a change.

## 2. Core Responsibilities

### 2.1 Establish review scope

Determine what is being reviewed, why the review is needed, and which criteria govern acceptance.

Relevant context may include:

- The proposed change or diff.
- Requirements and acceptance criteria.
- Approved technical design decisions.
- Related implementation plans.
- Existing interfaces and project conventions.
- Security and operational constraints.
- Applicable testing and release policies.
- Known limitations and previously identified risks.

Distinguish explicit requirements from inferred expectations and optional improvements.

If a material acceptance criterion is unclear, identify the ambiguity and seek clarification where it affects the correctness of the verdict.

### 2.2 Inspect the actual changes

Examine the available change set rather than relying solely on a summary written by its author.

Where possible, inspect:

- Added, modified, and deleted files.
- Relevant surrounding code.
- Public interfaces and contracts.
- Configuration and dependency changes.
- Tests and their assertions.
- Documentation affected by the change.
- Relevant existing behavior and conventions.
- Evidence associated with the implementation.

Check the scope of the diff and identify unrelated modifications when they matter.

Do not claim to have inspected files, executed commands, or accessed repository history unless the environment provides evidence that those actions occurred.

### 2.3 Identify actionable defects

Look for problems that could materially affect behavior, correctness, security, reliability, maintainability, or the stated requirements.

Examples include:

- Incorrect logic or edge-case handling.
- Broken interface contracts.
- Missing validation.
- Incorrect error handling.
- Data loss or corruption risks.
- Authentication or authorization weaknesses.
- Resource leaks or concurrency problems.
- Incompatible configuration or dependency changes.
- Inadequate regression coverage for a material behavior change.
- Documentation that contradicts the implementation.

Prioritize concrete defects over speculative scenarios or personal preferences.

### 2.4 Evaluate evidence

Support findings with the smallest relevant piece of evidence available.

Explain the conditions under which a problem occurs and why the behavior matters.

Distinguish:

- Directly observed defects.
- Findings derived from code inspection.
- Plausible risks that need further verification.
- Questions about unclear requirements.
- Optional improvements.

Do not present an unverified possibility as a confirmed defect.

### 2.5 Assess verification quality

Examine what the available tests and checks actually establish.

Consider whether tests:

- Cover the relevant behavior.
- Exercise important boundaries and failure paths.
- Assert meaningful outcomes.
- Detect the suspected regression.
- Depend on hidden state or unstable conditions.
- Could pass despite the reported defect.

A passing test suite is useful evidence, but does not guarantee correctness. An absent test is not automatically a defect if equivalent assurance is appropriate and established.

Do not claim that checks passed merely because a report says they should have passed. Distinguish reported results from results independently observed during the review.

### 2.6 Communicate findings clearly

For each substantive finding, provide:

- A concise explanation of the problem.
- The affected file, component, or behavior.
- The conditions required to reproduce it.
- The expected impact.
- Supporting evidence.
- A practical direction for correction.

Use severity levels consistently and explain the basis for high-impact findings.

Avoid vague statements such as "this code could be better" without identifying a meaningful problem or actionable improvement.

### 2.7 Provide a calibrated assessment

Summarize the review outcome according to the evidence and acceptance rules.

Possible outcomes include:

- **Changes required:** one or more material findings remain unresolved.
- **Conditionally acceptable:** no blocking issue is established, but specified checks, clarifications, or conditions remain.
- **No material findings identified:** the reviewed scope revealed no actionable material issue, subject to stated limitations.
- **Unable to assess:** missing context, access, or evidence prevents a meaningful conclusion.

Use the project's actual approval vocabulary when established. Do not invent a formal approval state or imply that a review verdict grants merge or release authorization.

## 3. When to Use Review

Use Review when:

- A feature or bug fix is ready for examination.
- A pull request or proposed patch needs feedback.
- A configuration or dependency change may affect system behavior.
- A refactor needs regression and contract review.
- A security-sensitive change requires focused scrutiny.
- Tests or documentation need assessment against requirements.
- A change must be evaluated before acceptance or handoff.
- A previous review's findings need reassessment after revisions.

Review can be used on a small diff or a larger change set. The depth of the review should reflect the change's complexity, impact, and risk.

Do not use Review as a substitute for:

- Requirements definition when expected behavior is unknown.
- Design work when the architecture itself needs to be selected.
- Systematic debugging when the cause of a failure needs investigation.
- Executed tests when runtime behavior must be established.
- Formal security assessment, compliance certification, or independent audit when those processes are required.

Review may recommend or coordinate these activities when the evidence warrants them.

## 4. Shared Standards

Follow the repository's shared standards:

- `standards/CORE-PRINCIPLES.md`
- `standards/HANDOFF-CONTRACT.md`
- `standards/SKILL-TEMPLATE.md`
- `standards/VERIFICATION.md`

Apply the shared principles:

1. Follow **Clarify, Don't Assume**.
2. Do not silently convert assumptions into requirements or decisions.
3. Distinguish facts, hypotheses, concerns, proposed changes, and verified results.
4. Preserve context and evidence across handoffs.
5. Do not claim an action or verification step occurred without evidence.
6. Make uncertainty and limitations visible.
7. Continue safe, independent analysis when nonessential information remains unresolved.
8. Ask focused questions when ambiguity materially affects correctness, scope, security, or acceptance.

Shared standards remain the canonical source for general rules. This skill describes how to apply them during review.

## 5. Operating Procedure

### Step 1: Establish review context

Identify:

- The change being reviewed.
- Its purpose and intended behavior.
- Relevant requirements and acceptance criteria.
- Approved design decisions.
- The expected review depth.
- Applicable security and compatibility constraints.
- Any explicit exclusions.
- The required acceptance or approval process.

If the change's purpose is unclear, establish enough context to avoid judging it against an invented goal.

### Step 2: Confirm available evidence

Determine which artifacts and tools are actually available.

Inspect the change set, relevant files, test evidence, and project context as appropriate.

Identify missing material evidence, such as an unavailable base revision, absent requirements, or unreported test results.

Do not imply that the review is comprehensive if important parts of the change are inaccessible.

### Step 3: Establish the baseline and scope

Determine which changes belong to the review.

Where available, compare against the correct base revision and examine relevant surrounding behavior.

Separate:

- Changes introduced by the proposal.
- Existing behavior that the proposal depends on.
- Pre-existing defects.
- Unrelated working-tree modifications.
- Generated files and other artifacts that need special interpretation.

Do not attribute a pre-existing problem to the proposed change without evidence that the change introduced or materially worsened it.

### Step 4: Map changes to requirements

For each material requirement or acceptance criterion, identify the relevant implementation and evidence.

Ask:

- Is the requirement addressed?
- Does the implementation preserve the intended behavior?
- Are important edge cases covered?
- Does the change conflict with another requirement?
- Is there evidence for the claimed outcome?
- Are any requirements left partially implemented?

For larger changes, use a lightweight coverage table. For a small change, a concise mental or written checklist may be sufficient.

### Step 5: Review correctness and logic

Inspect the behavior that the change introduces or modifies.

Consider:

- Boundary conditions.
- Empty, missing, malformed, or unexpected inputs.
- Nullability and type assumptions.
- State transitions and invariants.
- Ordering and duplication.
- Numeric precision and overflow.
- Time zones and temporal boundaries.
- Error propagation.
- Retry and idempotency behavior.
- Resource lifetime.
- Concurrency and shared state.
- Data consistency and transaction boundaries.

Only investigate dimensions relevant to the actual change. Avoid generic checklists that generate unsupported findings.

### Step 6: Review interfaces and compatibility

Check whether the change preserves the relevant contracts.

Depending on the system, consider:

- Public method and API signatures.
- Request and response formats.
- Database schemas and migrations.
- Event and message contracts.
- Configuration keys and defaults.
- Error codes and exception behavior.
- Serialization and deserialization.
- Dependency versions.
- Backward and forward compatibility.
- Deployment ordering and mixed-version operation.

If a breaking change is intentional, evaluate it against the approved migration and compatibility plan rather than treating every breaking change as inherently incorrect.

### Step 7: Review security and privacy

Assess security concerns that are relevant to the changed code or configuration.

Potential areas include:

- Authentication and authorization.
- Input validation and injection.
- Secret handling.
- Sensitive data exposure.
- Unsafe deserialization.
- File and path access.
- Insecure defaults.
- Cryptographic misuse.
- Dependency and supply-chain risk.
- Logging of sensitive information.
- Trust boundaries between components.
- Abuse of privileges or external integrations.

Distinguish a concrete vulnerability from a concern that requires further assessment.

Do not expose credentials or reproduce sensitive values unnecessarily in review comments.

A code review is not automatically a complete security audit. State when specialized analysis is needed.

### Step 8: Review reliability and operational behavior

When relevant, examine:

- Timeouts and cancellation.
- Retry behavior and duplicate side effects.
- Failure recovery.
- Resource exhaustion.
- Logging and observability.
- Health checks and readiness.
- Configuration drift.
- Rollback and migration safety.
- Availability and performance.
- Partial failure across service boundaries.

Prioritize issues supported by the implementation and expected operating conditions.

Do not speculate about production impact without explaining the conditions under which that impact could occur.

### Step 9: Evaluate tests

Inspect tests that are relevant to the change.

Determine whether they establish the expected behavior or leave important failure modes undetected.

Consider:

- Whether assertions would fail if the defect existed.
- Whether tests verify outcomes rather than implementation details alone.
- Whether important boundaries and error cases are represented.
- Whether tests are deterministic.
- Whether mocks or fixtures conceal the relevant behavior.
- Whether a regression test should accompany a defect correction.
- Whether integration behavior requires checks beyond unit tests.

If execution is available and appropriate, run targeted checks according to the task's authorization and risk.

Record the exact scope of execution and actual outcomes.

If execution is unavailable, review the test code and reported evidence without claiming independent execution.

### Step 10: Examine maintainability and design fit

Assess whether the change fits the project's established architecture and conventions.

Consider:

- Separation of responsibilities.
- Naming and clarity.
- Duplication.
- Unnecessary complexity.
- Coupling and cohesion.
- Appropriate abstractions.
- Error handling consistency.
- Extensibility where required.
- Documentation of non-obvious behavior.
- Unnecessary dependencies or configuration.

Distinguish material maintainability problems from stylistic preferences.

A different implementation is not a defect merely because the reviewer would have written it differently.

### Step 11: Validate candidate findings

Before reporting a finding, test its reasoning against the available evidence.

Ask:

1. Is the relevant behavior actually present in the reviewed change?
2. Is the finding supported by a requirement, contract, invariant, or concrete risk?
3. Under what conditions does the issue occur?
4. What is the realistic impact?
5. Could an existing guard, caller constraint, or test already prevent it?
6. Is the issue newly introduced or materially worsened?
7. Is the proposed severity proportionate?
8. Can the finding be made more precise?

When practical, use a targeted test, minimal reproduction, or direct inspection to validate uncertain findings.

If validation cannot establish the concern, lower its confidence or report it as a question rather than a confirmed defect.

### Step 12: Prioritize findings

Prioritize issues by their realistic impact, likelihood, affected scope, and applicable project policy.

Use an established project severity scale when available.

Otherwise, use the following guidance:

- **Critical:** a severe, credible failure such as broad compromise, catastrophic data loss, or a major system-wide outage under realistic conditions.
- **High:** a serious defect or vulnerability that materially affects core behavior, important data, security, or availability.
- **Medium:** a meaningful correctness, reliability, compatibility, or maintainability issue with a bounded but material impact.
- **Low:** a minor defect or limited improvement with low expected impact.
- **Informational:** useful context or a non-blocking suggestion that is not a defect.

Do not inflate severity to make a finding more likely to be addressed.

If severity depends on an unknown operational condition, state that dependency.

### Step 13: Write actionable findings

For each finding, include:

- **Severity:** according to the established scale.
- **Location:** the smallest useful file and line range or component reference available.
- **Problem:** the specific behavior or condition.
- **Impact:** what can go wrong and under which conditions.
- **Evidence:** the relevant code, test, observation, or contract.
- **Recommendation:** a practical direction for correction.

Use concise language and avoid repeating the same root issue in multiple findings.

Prefer one well-supported finding for a single underlying problem over several overlapping comments.

When a line-number reference is available, ensure it points to the relevant changed lines where possible. Do not invent line numbers.

### Step 14: Reassess after revisions

When an updated change set is available, inspect the new diff and reassess relevant findings.

Determine whether each earlier finding was:

- Addressed with sufficient evidence.
- Partially addressed.
- Still present.
- Made irrelevant by a justified change in scope.
- Unable to verify.

Do not mark a finding resolved merely because the author says it was fixed. Inspect the revision or relevant verification evidence when available.

Check for regressions introduced by the correction.

### Step 15: Produce the review assessment

Summarize:

- Review scope.
- Material findings, ordered by severity.
- Relevant positive evidence or coverage.
- Checks performed and their actual results.
- Unresolved questions or risks.
- The assessment outcome and its limitations.

If no material findings are identified, state that result without implying that every possible defect has been ruled out.

Do not automatically modify the reviewed code unless implementation work is explicitly part of the authorized task.

## 6. Review Deliverable Structure

Adapt the output to the size and risk of the change.

### 6.1 Review summary

Provide a concise statement of the review scope, assessment, and principal concerns.

### 6.2 Findings

Use a structured format for each actionable finding.

**[Severity] Short, specific title**

- **Location:** file, line range, or component.
- **Issue:** the behavior or condition that creates the problem.
- **Impact:** the concrete consequence under stated conditions.
- **Evidence:** the observation, code path, contract, or test supporting the finding.
- **Recommendation:** a practical correction or investigation step.

Order findings by severity and practical importance, not by file order alone.

### 6.3 Requirements coverage

For substantial changes, use a table such as:

| Requirement | Evidence reviewed | Assessment |
|---|---|---|
| Requirement A | Relevant code or test | Satisfied, partial, unclear, or not satisfied |

Do not mark a requirement satisfied solely because a related file exists.

### 6.4 Verification record

Separate:

- Checks independently executed during the review.
- Results reported by others.
- Static inspection and reasoning.
- Checks that were not run.
- Checks that failed or could not be completed.

Include useful details about scope and limitations.

### 6.5 Questions and risks

List unresolved questions that materially affect the assessment.

Distinguish these from confirmed defects and optional improvements.

### 6.6 Overall assessment

Use the project's established decision vocabulary where available. Otherwise, choose an outcome consistent with the evidence:

- Changes required.
- Conditionally acceptable.
- No material findings identified.
- Unable to assess.

State any conditions or limitations clearly.

## 7. Decision and Authorization Rules

### 7.1 Evidence takes precedence over confidence

Do not convert an intuitive concern into a confirmed finding without adequate support.

State the evidence and reasoning that justify each material conclusion.

### 7.2 Requirements and contracts govern correctness

Judge behavior against established requirements, approved decisions, and relevant contracts.

When these are unclear or contradictory, identify the ambiguity rather than silently choosing a preferred interpretation.

### 7.3 Review findings must be actionable

A finding should identify a meaningful problem, its impact, and a practical next step.

Do not block acceptance solely because of subjective preferences that have no material connection to project requirements or quality standards.

### 7.4 Absence of findings is not proof of perfection

A review can only support conclusions about the scope, evidence, and methods used.

Do not describe a change as defect-free, fully secure, or universally correct based on a limited review.

### 7.5 Passing tests do not override a demonstrated defect

A test suite may omit a relevant condition or assert the wrong behavior.

When direct evidence demonstrates a defect, explain why the existing test evidence does not resolve it.

### 7.6 A concern is not automatically a blocker

Use severity and acceptance policy consistently. Explain when a risk warrants a blocking decision and when it is a follow-up concern.

### 7.7 Review does not grant authorization

A favorable assessment does not itself authorize merging, deployment, publication, data migration, or external actions.

Follow the established approval process.

### 7.8 Preserve independent judgment

Do not approve a change simply because its author, another agent, or a previous review declared it correct.

Use the actual change and available evidence to form the assessment.

### 7.9 Do not conceal uncertainty

If context, access, or execution evidence is missing, state the limitation and adjust the assessment accordingly.

## 8. Failure Handling

### Requirements are unclear

Identify the specific ambiguity and request clarification when it materially affects correctness or acceptance.

Continue reviewing aspects that can be evaluated independently.

### Diff or source files are unavailable

State what could not be inspected and request the relevant change set or access. Do not produce findings that depend on unseen code.

### Base revision is uncertain

Identify the comparison limitation. Avoid claims about newly introduced defects until the relevant baseline is established.

### Test results are missing

Review available test code and implementation evidence. Clearly state that execution results were unavailable rather than assuming the suite passed.

### A suspected defect cannot be reproduced

Explain the suspected failure path and its supporting evidence. Lower confidence or report the issue as a question if the causal claim remains uncertain.

### Findings conflict with project conventions

Check the relevant standards and contracts. Distinguish a deliberate, justified exception from an actual inconsistency.

### Security impact is uncertain

Describe the trust boundary, plausible abuse path, and missing evidence. Recommend specialized assessment when the potential impact warrants it.

### Findings disagree with another reviewer

Compare the evidence, assumptions, requirements, and severity rationale. Resolve disagreements through explicit reasoning rather than deference to authority.

### A revision addresses only part of a finding

Report the remaining issue precisely and explain what is still unverified or incorrect.

### Review scope is too large

Prioritize high-risk components and identify the portions examined and omitted. Do not imply full coverage when the review was partial.

### No material finding is identified

Report that no material findings were identified within the reviewed scope. Mention important verification gaps or limitations without inventing problems to populate the report.

## 9. Output Expectations

A useful Review result is:

- **Independent:** conclusions follow from the actual change and evidence.
- **Requirement-aligned:** findings are grounded in requirements, contracts, or concrete risks.
- **Actionable:** each material finding explains the issue, impact, and next step.
- **Prioritized:** serious issues are distinguished from minor concerns.
- **Evidence-based:** confirmed defects, plausible risks, and questions are clearly separated.
- **Scoped:** review coverage and limitations are explicit.
- **Constructive:** recommendations address the problem without unnecessary redesign.
- **Security-conscious:** sensitive information and authorization boundaries are respected.
- **Non-destructive:** the reviewer does not silently alter the reviewed change.
- **Portable:** the process does not depend on a specific model provider or development platform.
- **Honest:** tests, checks, and findings are not overstated.
- **Useful for decisions:** the assessment helps the appropriate decision-maker understand remaining risks.

The objective is not to maximize the number of comments. It is to identify meaningful issues with enough evidence and precision to support a sound decision.

## 10. Acceptance Criteria for the Review Skill

The skill is behaving as intended when it can:

1. Establish review scope and acceptance criteria.
2. Inspect available changes rather than relying solely on a summary.
3. Distinguish new defects from pre-existing problems where evidence permits.
4. Evaluate correctness, edge cases, interfaces, and relevant non-functional risks.
5. Assess security and privacy concerns proportionately.
6. Evaluate whether tests provide meaningful evidence for changed behavior.
7. Distinguish confirmed findings from unverified concerns and preferences.
8. Produce concise, actionable, appropriately prioritized findings.
9. Avoid unsupported claims about files, test results, or external actions.
10. Reassess findings against revised changes when evidence is available.
11. Report no-finding outcomes without implying exhaustive proof of correctness.
12. Respect the project's authorization and approval process.
13. Preserve context for implementation, debugging, or follow-up work.
14. Adapt the review depth to the scope and risk of the change.
15. Follow shared standards without duplicating or contradicting their authority.

These criteria describe intended behavior. They do not establish that the skill has been tested or that compatibility with individual platforms has been verified.

## 11. Portability

- Use plain Markdown and standard Agent Skills metadata.
- Avoid dependence on a particular model provider or proprietary orchestration API.
- Do not assume a specific language, framework, editor, test runner, repository host, or review interface.
- Do not assume access to source files, diffs, history, test results, or external systems unless the runtime establishes their availability.
- Adapt finding locations and evidence formats to the available environment.
- Use explicit handoffs when direct skill invocation is unsupported.
- Treat compatibility with individual agent platforms as unverified until tested.
- Keep environment-specific adapters separate from the canonical skill definition when required by the repository architecture.

## 12. Maintenance

When updating Review:

1. Preserve alignment with the shared core principles and handoff contract.
2. Keep independent review distinct from implementation, testing execution, debugging, and approval.
3. Maintain consistent distinctions between findings, questions, risks, and suggestions.
4. Remove duplicated rules when a shared standard already defines them.
5. Validate metadata, Markdown structure, whitespace, and internal references after edits.
6. Test representative review scenarios before claiming behavioral compatibility.
7. Record meaningful changes through the repository's normal Git workflow.
