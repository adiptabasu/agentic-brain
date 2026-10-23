---
name: design
description: Develop and evaluate technical designs and architectures from established requirements. Use when a solution needs component boundaries, interfaces, data flows, technology trade-offs, architecture decisions, reliability or security considerations, or a technical design handoff before implementation.
---

# Design — Technical Design and Architecture

## 1. Purpose

Design transforms established requirements into a coherent technical approach.

It determines how a solution could satisfy its requirements by defining architectural structure, component responsibilities, interfaces, data flows, technology choices, operational considerations, and important trade-offs.

Design follows the Agentic Brain principle:

**Clarify, Don't Assume.**

A design must preserve the established requirements and constraints. It must distinguish evidence from assumptions, recommendations from decisions, and proposed validation from completed verification.

Design is responsible for evaluating how to solve the problem, not silently changing what the user asked to achieve.

## 2. Core Responsibilities

Design is responsible for:

1. Understanding the requirements, acceptance criteria, constraints, and dependencies.
2. Identifying the technical concerns that materially affect the solution.
3. Developing plausible architectural or implementation alternatives.
4. Evaluating alternatives against relevant requirements and quality attributes.
5. Defining component boundaries, responsibilities, interfaces, and dependencies.
6. Describing important data flows, state transitions, and interactions.
7. Evaluating security, privacy, reliability, performance, scalability, and maintainability where relevant.
8. Identifying technical risks, failure modes, and unresolved decisions.
9. Recording significant design decisions and their rationale.
10. Defining validation activities for important technical assumptions.
11. Producing a design artifact suitable for downstream planning, implementation, and testing.
12. Preserving traceability from requirements to design elements.

Design is not responsible for inventing requirements, implementing the solution, or claiming that a proposed architecture has been validated without supporting evidence.

## 3. When to Use Design

Use Design when:

- Requirements are sufficiently understood to evaluate technical approaches.
- A feature requires decisions about architecture or component responsibilities.
- Multiple implementation approaches have meaningful trade-offs.
- System boundaries, interfaces, data flows, or integration contracts need definition.
- Reliability, security, performance, scalability, or maintainability concerns affect the approach.
- A significant technology or dependency choice must be evaluated.
- An existing design needs review or revision.
- Implementation teams need an agreed technical direction and a clear record of outstanding decisions.

Do not create a heavyweight architecture document for a small, routine change that requires no meaningful design decision.

If critical requirements are ambiguous, return to `probe` or `specify` before treating the design as settled.

## 4. Shared Standards

Design MUST follow these shared Agentic Brain standards:

- `standards/CORE-PRINCIPLES.md`
- `standards/HANDOFF-CONTRACT.md`
- `standards/VERIFICATION.md`

Use `standards/SKILL-TEMPLATE.md` as the shared skill-structure reference where applicable.

These documents establish common principles and handoff expectations. Design must not redefine or contradict them.

## 5. Operating Procedure

### Step 1: Establish the design context

Review the available requirements, specifications, acceptance criteria, constraints, and relevant existing-system information.

Establish, where applicable:

- Problem and intended outcome.
- Functional and non-functional requirements.
- Existing architecture and integration boundaries.
- Technology and platform constraints.
- Operational environment.
- Security and privacy requirements.
- Deployment and maintenance expectations.
- Budget, schedule, or resource constraints.
- Decisions already made and decisions still open.

Use available context rather than asking for information that is already established.

Do not assume that a suggested technology, existing pattern, or prior design remains mandatory unless its status is clear.

### Step 2: Assess design readiness

Determine whether the information is sufficient to make useful technical decisions.

Check whether:

- The important requirements are understood.
- Material constraints are identified.
- Relevant external dependencies are known or explicitly uncertain.
- Quality attributes have usable targets where necessary.
- Critical authorization and ownership boundaries are clear.
- Acceptance criteria provide a basis for evaluating the proposed approach.

If a missing detail could materially change the architecture, investigate it or request clarification.

If uncertainty is noncritical, continue with an explicit assumption and identify its consequences.

Design readiness does not require every detail to be settled. It requires enough information to make the decisions currently under consideration responsibly.

### Step 3: Identify architectural drivers

Select the requirements and constraints that most strongly influence the design.

Potential drivers include:

- Correctness and data integrity.
- Security and privacy.
- Performance and latency.
- Availability and fault tolerance.
- Scale and workload characteristics.
- Deployment and operational simplicity.
- Compatibility and interoperability.
- Maintainability and extensibility.
- Cost and resource consumption.
- Regulatory or organizational constraints.
- Reversibility and migration risk.

Prioritize drivers based on the actual problem. Do not treat every quality attribute as equally important by default.

Where targets or priorities are missing and materially affect the choice, identify the decision needed.

### Step 4: Develop alternatives

Consider plausible alternatives when the choice has meaningful consequences.

For each alternative, determine:

- How it satisfies the requirements.
- Its principal benefits and drawbacks.
- Relevant implementation and operational complexity.
- Security and reliability implications.
- Performance and scalability characteristics.
- Cost and resource implications.
- Dependencies and compatibility concerns.
- Failure modes and recovery behavior.
- Migration or adoption risks.
- Long-term maintenance implications.
- Reversibility of the decision.

Include a baseline or simpler option where appropriate.

Avoid generating numerous alternatives that do not represent meaningful choices. A single approach may be sufficient when constraints clearly determine the solution.

Do not invent benchmarks, prices, measurements, or product capabilities to justify a preferred option.

### Step 5: Evaluate and recommend

Compare the alternatives using criteria derived from the established requirements and priorities.

A comparison may use a table:

| Criterion | Alternative A | Alternative B | Evidence or uncertainty |
|---|---|---|---|
| Requirement fit | Assessment | Assessment | Supporting facts and gaps |
| Complexity | Assessment | Assessment | Implementation and operational implications |
| Reliability | Assessment | Assessment | Failure behavior and evidence |
| Performance | Assessment | Assessment | Measurements, estimates, or unknowns |
| Cost | Assessment | Assessment | Known costs and assumptions |
| Reversibility | Assessment | Assessment | Migration or replacement implications |

Include only relevant criteria.

Explain why the recommended approach best fits the problem.

Distinguish measured evidence from qualitative judgment, estimates, and assumptions.

If the recommendation depends on a user's unresolved priority, explain the dependency rather than silently choosing a preference.

A recommendation may be provided without treating it as approved.

### Step 6: Define the architecture

Describe the proposed solution at the level needed for the intended implementation.

Where relevant, define:

- System boundaries and external actors.
- Components and their responsibilities.
- Interfaces and contracts.
- Data ownership and persistence.
- Data flows and transformations.
- Important state transitions.
- Synchronous and asynchronous interactions.
- External integrations.
- Authentication and authorization boundaries.
- Error propagation and recovery.
- Observability and operational responsibilities.
- Deployment boundaries and infrastructure dependencies.

Use diagrams, tables, structured descriptions, or concise prose where they improve understanding.

For each important component, explain its purpose and the boundaries of its responsibility.

Avoid unnecessary detail that belongs in implementation code or a lower-level design.

### Step 7: Design interfaces and contracts

For material interfaces, define the expected interaction between components.

Specify, where applicable:

- Purpose and responsibility.
- Inputs and outputs.
- Data schemas or formats.
- Preconditions and postconditions.
- Validation rules.
- Error conditions and failure responses.
- Authentication and authorization requirements.
- Idempotency and retry behavior.
- Timeout and resource limits.
- Versioning and compatibility expectations.
- Ownership and lifecycle.

Do not invent external API behavior or undocumented contracts. Verify available documentation when accessible, or explicitly mark the contract as provisional.

If a contract depends on an unresolved requirement, record that dependency.

### Step 8: Evaluate failure behavior and resilience

Identify realistic failure scenarios that could affect correctness or operation.

Consider, where applicable:

- Invalid or unexpected input.
- Partial failures across components.
- Network interruptions and timeouts.
- Dependency unavailability.
- Duplicate requests or repeated events.
- Concurrent updates and race conditions.
- Resource exhaustion.
- Data corruption or inconsistency.
- Authentication and authorization failures.
- Deployment and migration failures.
- Recovery, retry, rollback, and reconciliation.

For each significant scenario, describe the expected behavior and recovery approach.

Do not prescribe retries, caching, replication, or other resilience mechanisms without considering their consequences. For example, retries may duplicate non-idempotent operations, and caching may introduce stale data.

### Step 9: Evaluate security and privacy

Apply security and privacy considerations proportionately to the system's risks.

Consider:

- Trust boundaries.
- Identity and access control.
- Least privilege.
- Input validation and output handling.
- Secrets and credential management.
- Sensitive data collection and retention.
- Data in transit and at rest.
- Auditability and logging.
- Abuse cases and threat scenarios.
- Dependency and supply-chain risks.
- Secure failure behavior.

Identify important threats and proposed mitigations.

Distinguish a proposed security control from a control that has actually been implemented or independently assessed.

Do not claim that an architecture is secure merely because security considerations are documented.

### Step 10: Record design decisions

Document consequential decisions in a decision record or equivalent section.

For each important decision, record:

- Decision identifier, if useful.
- Context and problem.
- Relevant requirements and constraints.
- Alternatives considered.
- Selected option or recommendation.
- Rationale and trade-offs.
- Consequences and dependencies.
- Evidence and assumptions.
- Decision status.
- Revisit conditions, if appropriate.

Use explicit statuses such as:

- **Proposed:** Recommended but not yet accepted.
- **Accepted:** Approved by the appropriate decision-maker.
- **Rejected:** Considered and declined.
- **Superseded:** Replaced by a later decision.
- **Unresolved:** Requires more evidence or a decision.

Only use a status supported by the available evidence and authorization.

Record significant decisions without requiring a formal decision record for every minor implementation detail.

### Step 11: Validate important assumptions

Identify assumptions whose failure could invalidate the design or create significant risk.

For each material assumption, determine:

- What is assumed.
- Why it matters.
- What evidence would confirm or reject it.
- How the evidence could be obtained.
- Whether the validation is reversible and safe.
- What design changes may be needed if the assumption is false.

Prefer inexpensive, focused validation when it can resolve a high-impact uncertainty.

Potential validation methods include:

- Documentation review.
- Prototype or proof of concept.
- Benchmark or load test.
- Compatibility test.
- Threat analysis.
- Integration experiment.
- Data migration rehearsal.
- Failure-injection exercise.

A proposed validation method is not a completed test. Record actual results only when evidence is available.

### Step 12: Assess trade-offs, risks, and reversibility

Identify the costs and consequences of the proposed design.

Consider:

- Complexity introduced.
- Operational burden.
- Long-term maintenance.
- Lock-in and replacement cost.
- Migration difficulty.
- Failure impact.
- Performance and capacity limits.
- Security and privacy exposure.
- Dependence on external services.
- Cost of reversing a decision.

Prefer simpler, reversible decisions when they satisfy the requirements and avoid unnecessary commitment.

Do not optimize for hypothetical future needs at the expense of established requirements without explaining the trade-off.

### Step 13: Prepare the design handoff

Produce a design artifact that downstream workflows can use without reconstructing the original reasoning.

Include, as applicable:

- Design objective and scope.
- Relevant requirements and architectural drivers.
- Proposed architecture and component responsibilities.
- Interfaces and data flows.
- Alternatives considered and rationale.
- Security, reliability, and operational considerations.
- Important risks and assumptions.
- Decision status and required approvals.
- Validation plan and actual evidence, if available.
- Open questions and dependencies.
- Recommended next workflow.

Use `plan` when the design is sufficiently established and work needs sequencing.

Use `test-first` when the expected behavior and relevant design contracts are ready to guide test creation.

Return to `probe` or `specify` if unresolved requirements prevent responsible design decisions.

Use `guide` when the next workflow is unclear.

Use `relay` when a context-preserving handoff is needed and that skill is available.

These are intended workflow relationships, not proof that every referenced skill is installed or invocable in the current runtime.

If a destination skill is unavailable, provide an explicit handoff rather than claiming it was invoked.

## 6. Design Deliverable Structure

Adapt the level of detail to the complexity and risk of the system.

A substantial design document may contain:

### 1. Overview

- Problem and design objective.
- Scope and boundaries.
- Relevant stakeholders and constraints.

### 2. Requirements and Architectural Drivers

- Relevant functional requirements.
- Important quality attributes.
- Key constraints and dependencies.
- Requirement references.

### 3. Alternatives and Recommendation

- Viable approaches.
- Comparison criteria.
- Benefits, drawbacks, and trade-offs.
- Recommended approach and rationale.

### 4. Proposed Architecture

- System context.
- Components and responsibilities.
- Interfaces and contracts.
- Data flows and state transitions.
- External dependencies.

### 5. Cross-Cutting Concerns

- Security and privacy.
- Reliability and recovery.
- Performance and scalability.
- Observability and operations.
- Deployment and compatibility.

### 6. Decisions

- Accepted decisions.
- Proposed decisions awaiting approval.
- Rejected alternatives.
- Unresolved choices.

### 7. Risks and Validation

- Material technical risks.
- Assumptions requiring validation.
- Validation methods and evidence.
- Limitations and conditions for revisiting the design.

### 8. Handoff

- Implementation and planning considerations.
- Relevant acceptance criteria.
- Open dependencies and approvals.
- Recommended next steps.

For small changes, use only the sections needed to communicate the design clearly.

## 7. Decision and Authorization Rules

Design MUST follow these rules:

1. **Requirements remain authoritative:** Do not silently alter established requirements to fit a preferred design.
2. **Recommendations are not approvals:** Do not present a proposed architecture as an accepted decision without evidence of authorization.
3. **No invented constraints:** Do not fabricate technology restrictions, stakeholder preferences, external capabilities, or operational requirements.
4. **Evidence before certainty:** Distinguish facts, measurements, estimates, assumptions, and hypotheses.
5. **Proportionality:** Choose the simplest design that responsibly satisfies the requirements.
6. **Explicit trade-offs:** Make material costs, risks, and limitations visible.
7. **Security by design:** Consider applicable trust boundaries and security implications before implementation.
8. **Failure awareness:** Address realistic failure modes when they materially affect the solution.
9. **Traceability:** Link consequential design choices to relevant requirements and constraints where practical.
10. **No false verification:** A proposed architecture, diagram, prototype plan, or review checklist is not evidence of successful validation.
11. **Preserve scope:** Do not expand the solution or authorize consequential actions without the required decision.
12. **Reversibility:** Consider the cost and consequences of reversing major decisions.
13. **Honest uncertainty:** Mark important unknowns and explain their potential effect on the design.
14. **Explicit handoffs:** Preserve the context and decision status needed by downstream workflows.

## 8. Failure Handling

### Requirements are incomplete

Identify the requirements that materially affect the design. Return to clarification or specification rather than inventing missing behavior.

### No alternative clearly dominates

Explain the trade-offs and identify the priority or evidence that would determine the choice. Recommend an option only when the available information supports doing so.

### Technical evidence is unavailable

State what could not be verified, the limitations of the assessment, and what evidence would reduce uncertainty.

### External integration is undocumented

Mark the interface assumptions as provisional and identify the documentation or integration test needed before relying on them.

### Security concerns remain unresolved

Describe the threat, potential impact, and required mitigation or review. Do not represent the design as security-approved.

### A critical assumption fails validation

Explain which parts of the design are affected, reassess the alternatives, and update the recommendation or decision record as appropriate.

### Stakeholders disagree

Separate technical facts from preferences, priorities, and authorization decisions. Provide the relevant trade-offs and seek a decision from the appropriate authority.

### Scope expands during design

Distinguish the original scope from the proposed addition. Explain the implications and seek direction when the change affects commitments or authorization.

### A downstream skill is unavailable

Provide a context-preserving handoff and identify the intended next action. Do not fabricate skill invocation or execution results.

## 9. Output Expectations

Adapt the response to the user's needs and the system's complexity.

For a small change, a short design summary with key decisions and risks may be sufficient.

For a larger system, provide a structured design document with diagrams, comparison tables, decision records, and explicit validation activities where useful.

Every substantive design deliverable should communicate:

- What is being designed and why.
- Which requirements and constraints drive the design.
- How the major components interact.
- Which alternatives were considered.
- Why the proposed approach is recommended.
- Which decisions are accepted versus proposed.
- What remains uncertain.
- What risks and failure modes matter.
- How important assumptions will be validated.
- What downstream work can proceed.

Do not confuse design completeness with implementation completion or verified system behavior.

## 10. Acceptance Criteria for the Design Skill

A Design execution is successful when applicable criteria are satisfied:

- The design accurately reflects established requirements.
- Material constraints and architectural drivers are identified.
- The proposed architecture has clear boundaries and responsibilities.
- Important interfaces and data flows are described.
- Relevant alternatives and trade-offs have been considered.
- Material security, reliability, and operational concerns are addressed.
- Significant risks and assumptions are visible.
- Consequential decisions have clear status and rationale.
- Important assumptions have suitable validation plans.
- Requirements and design choices are traceable where appropriate.
- The design is proportionate to the problem.
- The handoff identifies relevant downstream work and dependencies.
- No unsupported claims of approval, implementation, compatibility, or verification are made.

These criteria assess the quality of the design process. They do not establish that the proposed architecture has been implemented or proven correct.

## 11. Portability

Design must remain useful across different AI agents and execution environments.

- Use plain Markdown and standard Agent Skills metadata.
- Avoid dependence on a particular model provider or proprietary orchestration API.
- Do not assume that other skills can be invoked automatically.
- Do not assume that files, external sources, diagrams, tools, or test environments are available unless the runtime establishes their availability.
- Use explicit handoffs when direct skill invocation is unsupported.
- Keep design reasoning independent of a particular programming language or application framework unless the requirements constrain that choice.
- Treat compatibility with individual agent platforms as unverified until tested.

## 12. Maintenance

When updating Design:

1. Preserve alignment with the shared core principles and handoff contract.
2. Keep technical design distinct from requirements definition, execution planning, implementation, and verification.
3. Prefer clear, evidence-based decisions over unnecessary architectural complexity.
4. Remove duplicated rules when a shared standard already defines them.
5. Validate metadata, Markdown structure, whitespace, and internal references after edits.
6. Test representative design scenarios before claiming behavioral compatibility.
7. Record meaningful changes through the repository's normal Git workflow.
