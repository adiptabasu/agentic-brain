---
name: specify
description: Turn clarified intent into structured, testable requirements and acceptance criteria.
---

# Specify — Requirements and Specification Engineering

## 1. Purpose

Specify transforms an understood problem into an explicit, consistent, testable specification.

It establishes what a solution must accomplish, which constraints it must respect, how success will be evaluated, and which decisions remain unresolved.

Specify follows the Agentic Brain principle:

**Clarify, Don't Assume.**

A specification must preserve the user's intent. It must not silently invent requirements, turn proposals into commitments, or hide uncertainty behind confident language.

Specify describes the required outcome and observable behavior. It does not prescribe technical architecture or implementation details unless those are explicit requirements or necessary constraints.

## 2. Core Responsibilities

Specify is responsible for:

1. Capturing the objective, context, intended users, and desired outcomes.
2. Defining scope, exclusions, boundaries, and assumptions.
3. Converting confirmed needs into clear functional requirements.
4. Identifying relevant non-functional requirements and quality attributes.
5. Recording business rules, constraints, dependencies, and integrations.
6. Defining observable and testable acceptance criteria.
7. Maintaining traceability between user needs, requirements, and acceptance criteria.
8. Identifying ambiguity, inconsistency, duplication, and missing requirements.
9. Distinguishing confirmed decisions from proposals and unresolved questions.
10. Producing a specification suitable for downstream workflows.
11. Recording risks and limitations that materially affect interpretation or delivery.
12. Keeping the specification proportionate to the size and complexity of the problem.

Specify is not responsible for independently choosing an architecture, creating a detailed implementation plan, or claiming that requirements have been implemented or tested.

## 3. When to Use Specify

Use Specify when:

- A clarified objective needs to become a formal set of requirements.
- A feature or system needs explicit functional behavior.
- Acceptance criteria are missing or too vague to validate.
- Multiple stakeholders or components depend on a shared definition of scope.
- Requirements must be handed off to design, planning, implementation, or testing.
- Existing requirements need review for completeness, consistency, or testability.
- Changes to requirements need impact analysis and traceability.
- A project needs a baseline against which proposed changes can be evaluated.

Do not create a heavyweight specification for a trivial task that can be completed safely from the existing request.

If material uncertainty prevents an accurate specification, use `probe` or ask focused clarification questions before finalizing the affected requirements.

## 4. Shared Standards

Specify MUST follow these shared Agentic Brain standards:

- `standards/CORE-PRINCIPLES.md`
- `standards/HANDOFF-CONTRACT.md`
- `standards/VERIFICATION.md`

Use `standards/SKILL-TEMPLATE.md` as the shared skill-structure reference where applicable.

These documents define common principles and workflow expectations. Specify must not redefine or contradict them.

## 5. Operating Procedure

### Step 1: Establish the specification context

Identify, where applicable:

- Problem or opportunity being addressed.
- Desired outcome and business or user value.
- Intended users and relevant stakeholders.
- Existing system or operational context.
- Scope of the requested specification.
- Constraints and dependencies.
- Known decisions and unresolved issues.
- Intended consumers of the specification.

Use available conversation and project context rather than asking the user to repeat established information.

If the intended outcome itself remains materially ambiguous, clarify it before treating the specification as settled.

### Step 2: Capture scope and boundaries

Record what the solution is expected to cover.

Distinguish:

- **In scope:** Capabilities and outcomes included in the current effort.
- **Out of scope:** Explicit exclusions or work intentionally deferred.
- **Constraints:** Conditions the solution must respect.
- **Dependencies:** External systems, decisions, resources, or prerequisites.
- **Future considerations:** Potential improvements not committed to the current scope.

Do not interpret an omission as an explicit exclusion.

Do not expand scope merely because an adjacent capability seems useful.

When a proposed addition changes cost, risk, schedule, compatibility, or intended behavior materially, identify it as a proposal and seek direction when necessary.

### Step 3: Inventory and classify requirements

Record requirements using meaningful identifiers and explicit status.

Use the following classifications as appropriate:

- **Confirmed:** Explicitly established by the user or an authorized source.
- **Proposed:** Suggested but not yet accepted.
- **Assumed:** A provisional premise that has not been verified.
- **Unresolved:** Requires additional information or a decision.
- **Deferred:** Intentionally postponed with its status and rationale documented.
- **Rejected:** Explicitly declined or ruled out, with rationale where useful.

Do not assign a status that implies approval without supporting evidence.

Keep requirements distinct from design choices, implementation tasks, risks, and open questions.

When a requirement is derived from a source, preserve enough source context to trace its origin.

### Step 4: Write functional requirements

Describe what the solution must do in terms of observable behavior.

Where relevant, specify:

- Trigger or initiating condition.
- Actor or system component involved.
- Preconditions.
- Expected behavior.
- Inputs and outputs.
- State changes.
- Business rules.
- Error and recovery behavior.
- Permissions and authorization.
- Relevant edge cases.

Use precise, unambiguous language.

Prefer a unique identifier and a clear statement of required behavior for each independently verifiable requirement.

Avoid combining unrelated behaviors into a single requirement when they need separate acceptance criteria.

Avoid vague terms such as "fast," "easy," "robust," or "user-friendly" unless they are defined by measurable or observable conditions.

Do not prescribe a specific implementation when multiple implementations could satisfy the requirement and no technical constraint requires one.

### Step 5: Define non-functional requirements

Identify relevant quality attributes based on the problem and its risks.

Potential categories include:

- Performance and latency.
- Scalability and capacity.
- Availability and reliability.
- Security and access control.
- Privacy and data handling.
- Accessibility and usability.
- Maintainability and observability.
- Compatibility and portability.
- Data integrity and recovery.
- Regulatory or organizational compliance.

Do not mechanically include every category in every specification.

For each applicable requirement, record a measurable target or observable condition where feasible.

If the target is unknown, identify the missing decision rather than inventing a number.

Distinguish a verified external or organizational constraint from a recommendation that still requires approval.

### Step 6: Define acceptance criteria

Acceptance criteria must make it possible to determine whether a requirement has been satisfied.

Prefer criteria that specify:

- Preconditions or initial state.
- Action, event, or input.
- Expected observable outcome.
- Relevant boundary conditions.
- Expected failure behavior when applicable.

Use scenario-based formats, tables, examples, or structured test conditions when they improve clarity.

Acceptance criteria must be:

- Clear enough to interpret consistently.
- Relevant to the requirement.
- Observable or objectively assessable.
- Specific enough to support validation.
- Consistent with approved scope and constraints.

Do not claim that acceptance criteria have passed merely because they have been written.

Keep three concepts distinct:

1. **Acceptance criterion:** The condition that must be satisfied.
2. **Verification method:** How satisfaction will be assessed.
3. **Verification result:** Evidence of the actual outcome, if testing or inspection has occurred.

If an acceptance criterion cannot yet be made testable, explain what information is needed.

### Step 7: Check completeness and consistency

Review the specification for material gaps.

Consider:

- Every confirmed objective has relevant requirements.
- Every in-scope capability has defined expected behavior.
- Important inputs, outputs, and state transitions are addressed.
- Error paths and boundary conditions are covered where relevant.
- Non-functional requirements reflect actual project needs.
- Constraints and dependencies are explicit.
- Requirements do not contradict one another.
- Scope and exclusions are understandable.
- Acceptance criteria cover the intended behavior.
- Unresolved decisions are visible.
- Terminology is consistent.
- Requirements do not imply unauthorized work.
- No requirement is supported only by an unstated assumption.

Use judgment proportional to the risk and complexity of the solution. Completeness does not require documenting every imaginable scenario.

### Step 8: Establish traceability

Where the complexity justifies it, link requirements to their origin and validation criteria.

A traceability record may contain:

| Field | Purpose |
|---|---|
| Requirement ID | Stable identifier for reference |
| Source | User request, stakeholder, policy, or other evidence |
| Requirement | Required behavior or condition |
| Status | Confirmed, proposed, assumed, unresolved, deferred, or rejected |
| Priority | Relative importance, if established |
| Acceptance criteria | Conditions that demonstrate satisfaction |
| Dependencies | Related requirements or external prerequisites |
| Verification method | Intended validation approach |
| Change impact | Downstream items affected by changes |

Do not invent priorities or sources.

Use identifiers consistently and avoid unnecessary traceability overhead for small tasks.

### Step 9: Record risks and unresolved decisions

List only issues that materially affect the specification or its downstream use.

For each important issue, record:

- What remains uncertain or could go wrong.
- Why it matters.
- Which requirements or decisions are affected.
- What evidence or decision would resolve it.
- Whether work can safely continue in the meantime.

Distinguish an unresolved requirement from a risk that an otherwise understood requirement may not be satisfied.

When a decision requires the user's preference, authority, or commitment, do not silently choose on their behalf.

### Step 10: Review changes and their impact

When an existing specification changes:

1. Identify the requirement or decision being changed.
2. Record the reason and source of the change when known.
3. Determine which acceptance criteria are affected.
4. Identify dependent requirements, components, tests, and downstream work.
5. Surface newly introduced conflicts, risks, or scope changes.
6. Preserve previously confirmed decisions unless they are explicitly revised.
7. Update the specification and its traceability records.
8. Identify any additional approval or validation required.

Do not imply that a downstream artifact has been updated unless that work has actually been completed and verified.

### Step 11: Prepare the handoff

Produce a specification that the next workflow can consume without reconstructing the original conversation.

Select the appropriate level of detail for the intended consumer.

- Hand off to `probe` when material ambiguity or conflicting requirements remain.
- Hand off to `design` when the requirements are sufficiently clear and technical alternatives must be evaluated.
- Hand off to `plan` when the scope and outcomes are established and execution needs sequencing.
- Hand off to `test-first` when testable behavior is ready to guide test design and development.
- Return to `guide` when the next workflow is unclear.
- Use `relay` when a context-preserving transfer is needed and that skill is available.

These are intended workflow relationships, not proof that every referenced skill is installed or invocable in the current runtime.

If a destination skill is unavailable, provide an explicit handoff instead of claiming it was invoked.

## 6. Specification Structure

Adapt the structure to the task. A substantial specification may contain the following sections.

### 1. Overview

- Problem statement.
- Objectives and expected outcomes.
- Intended users or stakeholders.
- Background and context.

### 2. Scope

- In-scope capabilities.
- Out-of-scope items.
- Boundaries and exclusions.
- Future considerations.

### 3. Requirements

- Functional requirements with identifiers.
- Applicable non-functional requirements.
- Business rules.
- Constraints and dependencies.

### 4. Acceptance Criteria

- Criteria linked to individual requirements.
- Important success and failure scenarios.
- Boundary conditions.
- Intended verification methods.

### 5. Data and Integrations

- Relevant inputs and outputs.
- Data ownership and lifecycle.
- External dependencies and integration expectations.
- Data protection and retention requirements, where applicable.

Include only what is relevant and sufficiently understood.

### 6. Risks and Open Decisions

- Material risks.
- Unresolved questions.
- Assumptions requiring validation.
- Decisions requiring authorization.

### 7. Traceability and Change History

- Requirement sources.
- Requirement-to-acceptance-criteria mapping.
- Relevant dependencies.
- Material changes and their rationale.

### 8. Handoff

- Recommended next workflow.
- Required inputs for downstream work.
- Known limitations.
- Conditions that must be resolved before specific work can proceed.

For small tasks, a concise specification containing only the necessary sections is preferable to a heavyweight document.

## 7. Decision and Authorization Rules

Specify MUST follow these rules:

1. **Preserve intent:** Requirements must reflect the user's established objective.
2. **No invented requirements:** Do not turn suggestions or assumptions into confirmed commitments.
3. **No silent scope expansion:** Clearly distinguish the agreed scope from optional enhancements.
4. **Explicit status:** Keep confirmed, proposed, assumed, unresolved, deferred, and rejected items distinguishable.
5. **Testability:** Define observable acceptance criteria wherever feasible.
6. **No false verification:** Writing a criterion is not evidence that it has passed.
7. **Separate requirement from implementation:** Describe the required outcome without unnecessarily prescribing how to implement it.
8. **Expose conflicts:** Surface materially incompatible requirements instead of silently prioritizing one.
9. **Preserve authorization:** A specification does not grant permission to execute consequential actions.
10. **Evidence-based traceability:** Do not invent requirement sources, stakeholder decisions, priorities, or test results.
11. **Proportionate detail:** Use the minimum structure that preserves the information needed for reliable downstream work.
12. **Explicit uncertainty:** Identify requirements whose correctness depends on unresolved assumptions or decisions.
13. **Controlled changes:** Evaluate the impact of changes on scope, acceptance criteria, dependencies, and downstream work.
14. **Honest handoff:** Do not claim that a downstream skill, artifact, or workflow was executed unless the runtime and available evidence support that claim.

## 8. Failure Handling

### Ambiguous objectives

Return to clarification. Identify the minimum information required to establish the intended outcome.

### Conflicting requirements

Record the conflict and its implications. Request an authorized decision when the conflict cannot be resolved from established priorities or evidence.

### Missing measurable targets

Identify the quality attribute or expected outcome and ask for a target when it materially affects correctness. Do not invent thresholds.

### Unavailable source information

Mark the affected requirements as unresolved or provisional. Explain how the missing evidence limits the specification.

### Unverifiable acceptance criteria

Explain why the criterion cannot currently be assessed and propose a more observable formulation if doing so preserves the user's intent. Mark the criterion as proposed until accepted when necessary.

### Scope changes

Identify the change, its consequences, and affected requirements. Seek direction when the change alters commitments, authorization, or material constraints.

### Excessive complexity

Break the specification into logical sections or independently manageable areas while preserving cross-references and dependencies.

### Downstream skill unavailable

Provide a clear handoff artifact and identify the intended next action. Do not fabricate invocation or execution results.

## 9. Output Expectations

Use the output format best suited to the user's goal and the complexity of the work.

For simple requests, a concise list of requirements and acceptance criteria may be sufficient.

For larger tasks, provide a structured specification with identifiers and explicit status.

Every substantive specification should make it possible to determine:

- What outcome is required.
- What is included and excluded.
- Which requirements are established and which remain provisional.
- How satisfaction will be assessed.
- Which constraints and dependencies matter.
- Which material decisions remain open.
- What downstream work can begin.

Keep recommendations, proposed requirements, and confirmed commitments distinguishable.

Avoid unnecessary repetition, excessive ceremony, and unsupported certainty.

## 10. Acceptance Criteria for the Specify Skill

A Specify execution is successful when applicable criteria are satisfied:

- The objective and intended outcome are represented accurately.
- Scope and exclusions are clear enough for the intended work.
- Requirements are identifiable and sufficiently unambiguous.
- Relevant functional and non-functional requirements are addressed.
- Material constraints and dependencies are documented.
- Acceptance criteria are observable and testable wherever feasible.
- Requirement statuses reflect the available evidence.
- Important sources and dependencies are traceable where appropriate.
- Material conflicts and unresolved decisions are visible.
- The specification avoids unnecessary implementation prescriptions.
- The level of detail is proportionate to the problem.
- The handoff identifies appropriate downstream work.
- No unsupported claims of approval, implementation, or verification are made.

These criteria evaluate the quality of the specification process. They do not establish that a proposed solution has been implemented successfully.

## 11. Portability

Specify must remain useful across different AI agents and execution environments.

- Use plain Markdown and standard Agent Skills metadata.
- Avoid dependence on a particular model provider or proprietary orchestration API.
- Do not assume that other skills can be invoked automatically.
- Do not assume that files, external sources, tools, or stakeholder records are available unless the runtime establishes their availability.
- Use explicit handoffs when direct skill invocation is unsupported.
- Keep requirements engineering independent of any particular programming language or application framework.
- Treat compatibility with individual agent platforms as unverified until tested.

## 12. Maintenance

When updating Specify:

1. Preserve alignment with the shared core principles and handoff contract.
2. Keep requirements engineering distinct from clarification, design, planning, implementation, and testing.
3. Prefer precise, testable requirements over unnecessary documentation.
4. Remove duplicated rules when a shared standard already defines them.
5. Validate metadata, Markdown structure, whitespace, and internal references after edits.
6. Test representative requirements scenarios before claiming behavioral compatibility.
7. Record meaningful changes through the repository's normal Git workflow.
