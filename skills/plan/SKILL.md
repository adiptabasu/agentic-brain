---
name: plan
description: Sequence established requirements and technical designs into actionable implementation tasks.
---

# Plan

## 1. Purpose

Plan turns established requirements, accepted technical designs, and explicit constraints into a practical execution plan.

It answers:

- What work needs to be done?
- Why is each task necessary?
- What must happen first?
- Which tasks can proceed independently?
- What does completion mean for each task?
- What dependencies, risks, and uncertainties could affect execution?
- What decisions or approvals are required before work can proceed?

Plan is responsible for structuring and sequencing work. It does not silently redefine requirements, approve proposed designs, implement the solution, or claim that planned work has been completed.

The guiding principle is **Clarify, Don't Assume**. Make material uncertainty visible, ask focused questions when necessary, and continue safe planning when unresolved details do not prevent useful progress.

## 2. Core Responsibilities

### 2.1 Establish planning context

Identify the objective, expected outcomes, relevant requirements, accepted design decisions, constraints, and available resources.

Distinguish:

- Confirmed requirements from suggestions.
- Accepted decisions from proposed options.
- Known constraints from inferred constraints.
- Actual dependencies from convenient sequencing preferences.
- Verified facts from unverified statements.
- Explicit commitments from illustrative estimates.

Use available project context and artifacts when they are accessible. Do not claim to have inspected documents, repositories, tools, or external systems that were not actually available.

### 2.2 Assess readiness

Determine whether sufficient information exists to create a useful plan.

Identify:

- Missing requirements that materially affect task decomposition.
- Unapproved design choices that block dependent work.
- External dependencies and required access.
- Unresolved ownership or authorization.
- Unknowns that affect estimates, sequencing, or acceptance criteria.
- Decisions that can safely be deferred.

Do not block the entire plan because of a nonessential unknown. Mark affected tasks as conditional, identify the dependency, and plan independent work where useful.

### 2.3 Decompose work

Break the objective into tasks that have clear outcomes and can be understood independently.

Each task should, where applicable:

- Have a unique identifier.
- State an action and its intended outcome.
- Explain why it is necessary.
- Identify relevant requirements or design decisions.
- Define completion and verification criteria.
- List prerequisites and dependencies.
- Identify relevant risks or unresolved questions.

Prefer tasks small enough to execute and verify without requiring unrelated work to be completed first.

Avoid both extremes:

- Tasks so broad that their scope and completion cannot be assessed.
- Excessively granular tasks that create administrative overhead without improving execution.

### 2.4 Establish dependencies and sequencing

Identify relationships between tasks.

Distinguish:

- **Hard dependency:** a task cannot proceed until another task or decision is complete.
- **Soft dependency:** an order is recommended but not strictly required.
- **External dependency:** progress relies on a person, system, provider, approval, or resource outside the task's direct control.
- **Conditional dependency:** work proceeds only if a stated condition is satisfied.

Use these relationships to establish a sensible execution order.

Identify tasks that can run in parallel, but account for shared resources, integration points, conflicting changes, and coordination costs.

Do not invent dependency relationships merely to make a plan appear orderly.

### 2.5 Define completion criteria

Every meaningful task should have an observable definition of done.

Prefer criteria that can be evaluated objectively, such as:

- A specified artifact exists and meets agreed requirements.
- An interface contract is documented and accepted.
- A test passes under stated conditions.
- A migration is validated against an agreed checklist.
- A decision is explicitly recorded by an authorized decision-maker.
- A handoff contains the required context and outstanding questions.

Separate implementation completion from verification completion when they are different milestones.

Do not equate task completion with overall project success unless the agreed acceptance criteria support that conclusion.

### 2.6 Assess risks and uncertainty

Identify risks that could materially affect delivery, quality, security, reliability, cost, or scope.

For each significant risk, state:

- The risk or uncertainty.
- Its potential impact.
- The evidence or reasoning supporting it.
- A mitigation, fallback, or decision needed.
- The task or milestone affected.
- The person or role responsible, if known.

Do not invent numerical probabilities, dates, costs, or confidence levels. If estimates are useful but evidence is limited, label them as estimates and state their basis or assumptions.

### 2.7 Prepare an execution handoff

Produce a plan that can be used by an implementer, another agent, or a human team without losing important context.

The handoff should explain:

- The objective and intended outcome.
- Relevant confirmed requirements and accepted design decisions.
- Task order and dependencies.
- Constraints and authorization boundaries.
- Completion and verification criteria.
- Risks, blockers, and unresolved questions.
- What should happen next.

Use the shared handoff contract and preserve the distinction between known facts, assumptions, proposals, and verified results.

## 3. When to Use Plan

Use Plan when:

- A feature, project, migration, or technical change needs an execution sequence.
- An accepted design needs to be broken into implementation tasks.
- Several people or agents need coordinated work.
- Dependencies, parallel work, milestones, or delivery risks need analysis.
- A task is too large or ambiguous to execute reliably as a single unit.
- An existing plan needs revision because requirements, constraints, or dependencies changed.

Do not use Plan as a substitute for:

- Requirements engineering when the intended outcome is not established.
- Technical design when architectural choices remain to be made.
- Implementation when the user requests execution rather than planning.
- Testing or independent verification when evidence of correctness is required.
- Authorization when a decision requires explicit approval.

These activities may be identified as dependencies or separate workstreams in a plan.

## 4. Shared Standards

Follow the repository's shared standards:

- `standards/CORE-PRINCIPLES.md`
- `standards/HANDOFF-CONTRACT.md`
- `standards/SKILL-TEMPLATE.md`
- `standards/VERIFICATION.md`

Treat those files as the canonical source for shared rules.

In particular:

1. Follow **Clarify, Don't Assume**.
2. Do not treat silence as approval.
3. Do not convert proposals into accepted decisions.
4. Distinguish confirmed, proposed, assumed, unknown, blocked, verified, and unverified information.
5. Preserve context across handoffs.
6. Do not claim that work, tests, approvals, or external actions occurred without evidence.
7. Continue safe, independent work when a nonessential question remains unresolved.
8. Ask focused questions when ambiguity materially affects scope, sequencing, safety, authorization, or correctness.

Do not duplicate entire shared standards inside this skill. Apply them to planning-specific decisions and artifacts.

## 5. Operating Procedure

### Step 1: Establish the objective

Restate the intended outcome in concrete terms.

Identify, where available:

- The problem being addressed.
- The expected deliverable or behavior.
- The intended users or stakeholders.
- The scope and explicit exclusions.
- The success criteria.
- The relevant deadline or milestone, if confirmed.

If the objective has multiple plausible interpretations that would produce materially different plans, ask a focused clarification question before committing to one interpretation.

Do not introduce a deadline merely because a plan normally contains one.

### Step 2: Gather inputs and evidence

Review the relevant requirements, accepted design, project notes, constraints, existing plans, and available artifacts.

Record the source of material decisions when practical.

Do not assume that a preceding skill ran, that its output exists, or that another skill can be invoked automatically. Use actual available context and artifacts.

If important inputs are missing, identify them and determine whether they block all planning or only particular tasks.

### Step 3: Assess readiness and open decisions

Create a concise list of:

- Confirmed inputs.
- Open questions.
- Required approvals.
- External dependencies.
- Known blockers.
- Decisions that can be deferred.

For each material unknown, explain which part of the plan it affects.

Ask questions when an unresolved detail would materially change the plan and cannot be safely represented as a conditional branch.

Otherwise, continue with explicit conditions and boundaries.

### Step 4: Define scope and workstreams

Translate the objective into major workstreams or outcomes.

For each workstream, identify:

- Its purpose.
- Its deliverables.
- Relevant requirements and design decisions.
- Dependencies on other workstreams.
- Its completion criteria.

Keep in-scope work separate from optional improvements and explicitly excluded work.

Do not silently expand the scope to include convenient but unrequested features.

### Step 5: Decompose work into tasks

Break each workstream into actionable tasks.

Use a stable identifier, such as `T1`, `T2`, or `API-01`, when the plan has multiple tasks or needs to be referenced later.

For each task, specify as appropriate:

- ID and title.
- Intended outcome.
- Scope and relevant context.
- Prerequisites.
- Dependencies.
- Completion criteria.
- Verification method.
- Risk or unresolved decision.
- Owner or role, if known.

A task should have a clear result and an understandable boundary. If it contains several independently deliverable outcomes, consider splitting it.

Do not force every task into an identical level of detail when the work naturally requires different granularity.

### Step 6: Map dependencies

Construct a dependency relationship for each task that has prerequisites.

Check for:

- Missing prerequisites.
- Circular dependencies.
- Decisions that must precede implementation.
- Shared resources that prevent simultaneous work.
- Integration work that depends on multiple components.
- External services or approvals that could delay progress.

If dependencies form a cycle, do not hide it. Explain the conflict and propose a way to resolve it.

Distinguish genuine blockers from preferred ordering.

### Step 7: Sequence and identify parallel work

Choose an execution order that respects hard dependencies and reduces unnecessary rework.

Where useful, group work into phases such as:

1. Discovery and decisions.
2. Foundations and interfaces.
3. Core implementation.
4. Integration.
5. Verification.
6. Release and follow-up.

These are examples, not mandatory phases.

Identify tasks that can proceed independently. State any coordination requirements or shared-resource constraints.

Prefer early resolution of high-impact uncertainty when doing so reduces downstream rework. Do not delay independent, low-risk work without a reason.

### Step 8: Define milestones and checkpoints

Identify meaningful points where progress can be assessed or a decision is needed.

For each milestone, specify:

- Expected outcome.
- Required preceding tasks.
- Acceptance or review criteria.
- Decisions or approvals required.
- Conditions for proceeding.

Use dates only when they are supplied, agreed, or derived transparently from an explicit planning basis.

If dates or durations are unknown, use relative ordering or leave the schedule unresolved rather than inventing precision.

### Step 9: Assess effort and resources

Estimate effort only when it is useful and the available evidence supports a reasonable estimate.

Distinguish effort from elapsed time. Account for dependencies, reviews, integration, testing, and external waiting time when relevant.

State:

- The unit used, such as person-hours or person-days.
- Whether the estimate is preliminary or validated.
- The assumptions and exclusions.
- Important uncertainty.
- Known capacity or resource constraints.

If reliable estimation is not possible, state what information would improve it. A qualitative size estimate may be used if its scale is defined.

Do not assign owners, staffing levels, budgets, or commitments without evidence or authorization.

### Step 10: Plan for risks and failure

Consider risks arising from technical complexity, external dependencies, security, data handling, migration, integration, deployment, operational readiness, and unclear ownership.

For material risks, define a mitigation, fallback, decision point, or contingency task.

Identify what would cause work to stop, be reconsidered, or require escalation.

Include rollback, recovery, or release safeguards when relevant to the objective.

Do not add elaborate risk procedures to trivial work when they provide no meaningful benefit.

### Step 11: Define verification and acceptance

For each important deliverable, identify how completion will be demonstrated.

Specify, where relevant:

- Expected tests or reviews.
- Required test environments or data.
- Acceptance criteria.
- Evidence to retain.
- Responsible reviewer, if known.
- What happens if verification fails.

Distinguish planned verification from verification already performed.

If a test environment, tool, or data source is unavailable, record the limitation and its impact.

Do not mark a task as verified merely because a verification step has been included in the plan.

### Step 12: Validate plan consistency

Before handing off the plan, check that:

- Every in-scope outcome maps to one or more tasks.
- Each task contributes to an identified outcome.
- Material tasks have clear completion criteria.
- Hard dependencies are represented.
- The dependency graph contains no unexplained cycles.
- Parallel work does not rely on conflicting assumptions.
- Required decisions and approvals are visible.
- Risks and blockers are addressed or explicitly accepted by an authorized party.
- Dates, estimates, owners, and commitments are evidence-based.
- Verification is planned at the appropriate level.
- No proposed decision is presented as approved.
- The plan does not silently change requirements or design decisions.

Report material gaps rather than concealing them behind a polished presentation.

### Step 13: Prepare the handoff

Present the plan in a form suited to its scale.

A small change may need only a short checklist. A larger initiative may need workstreams, task tables, milestones, dependencies, risk registers, and decision logs.

Include:

- Objective and scope.
- Confirmed inputs and accepted decisions.
- Task sequence and dependencies.
- Completion and verification criteria.
- Risks, blockers, and open decisions.
- Recommended next action.
- Relevant assumptions and limitations.

Use the shared handoff contract when the plan is passed to another skill, agent, or person.

### Step 14: Adapt when circumstances change

When requirements, accepted decisions, resources, or dependencies change:

1. Identify the change and its source.
2. Determine which tasks, dependencies, estimates, and milestones are affected.
3. Reassess the plan's readiness and validity.
4. Identify new decisions or approvals required.
5. Update affected work rather than rewriting unrelated sections unnecessarily.
6. Explain significant changes and their consequences.
7. Preserve the distinction between previous and current decisions.

Do not treat an outdated plan as authoritative after material inputs have changed.

## 6. Plan Deliverable Structure

Adapt the output to the scale and complexity of the work. Do not require every section for a small task.

### 6.1 Objective and scope

Describe the intended outcome, deliverables, inclusions, and exclusions.

### 6.2 Inputs and decisions

Summarize confirmed requirements, accepted design decisions, constraints, open questions, and required approvals.

### 6.3 Work breakdown

Represent workstreams and tasks in a concise list or table.

Recommended task fields:

| Field | Meaning |
|---|---|
| ID | Stable task reference |
| Task | Action and intended outcome |
| Prerequisites | Conditions required before starting |
| Dependencies | Tasks or decisions that must precede this work |
| Completion criteria | Observable definition of done |
| Verification | How completion will be demonstrated |
| Status | Planned, ready, in progress, blocked, completed, or verified, as supported by evidence |
| Notes | Relevant risks, conditions, or unresolved questions |

Omit columns that add no value for the specific plan.

### 6.4 Execution sequence

Explain the intended order, parallelizable tasks, hard dependencies, and key integration points.

### 6.5 Milestones

Describe significant outcomes and the conditions required to reach them.

### 6.6 Risks and blockers

List material risks, their impact, mitigations, dependencies, and escalation conditions.

### 6.7 Estimates and resources

Include effort, schedule, ownership, or resource information only to the extent justified by available evidence.

### 6.8 Acceptance and verification

Explain the overall completion conditions and the evidence needed to demonstrate them.

### 6.9 Handoff and next action

Identify the next actionable task, required inputs, unresolved decisions, and intended recipient or role when known.

## 7. Decision and Authorization Rules

### 7.1 A plan is not approval

A recommended sequence, task breakdown, estimate, milestone, or technical choice does not become an authorized commitment merely because it appears in the plan.

Keep recommendations distinct from decisions made by an authorized person or process.

### 7.2 Preserve established requirements

Do not reinterpret a requirement merely to make planning easier.

If a requirement conflicts with a constraint, design decision, or other requirement, expose the conflict and request clarification or an authorized decision.

### 7.3 Do not invent ownership or commitments

Do not assign a named owner, commit a team to a deadline, approve expenditure, or promise delivery without the necessary evidence and authorization.

When ownership is unknown, identify the role or decision needed without inventing a person.

### 7.4 Handle uncertainty explicitly

Use conditional tasks, alternative paths, decision gates, and explicit assumptions where appropriate.

An assumption must not silently become a confirmed requirement.

If an assumption requires acceptance before work proceeds, mark the affected task as blocked or conditional until the decision is made.

### 7.5 Respect safety and authorization boundaries

Include necessary review, security, privacy, and approval steps when relevant.

Do not plan around bypassing required controls or treating an unapproved action as authorized.

### 7.6 Continue safe independent work

When one workstream is blocked, identify other work that can proceed without relying on the unresolved issue.

Do not use this principle to justify work that could cause irreversible consequences, violate constraints, or make an unapproved decision on the user's behalf.

## 8. Failure Handling

### Insufficient requirements

Explain which outcomes or task boundaries remain unclear. Ask focused questions or produce a conditional outline that does not pretend the missing information is settled.

### Missing or conflicting design decisions

Identify the affected tasks and the decision needed. Do not invent an architecture or silently choose between incompatible options.

### Circular or contradictory dependencies

Show the conflicting relationships and explain what must change to restore a workable sequence.

### Unavailable resources or external dependencies

Identify the dependency, its current evidence-based status, and the work blocked by it. Do not claim to have contacted a provider, obtained access, or secured approval unless that occurred.

### Unreliable estimates

State why the estimate is uncertain and what information would improve it. Avoid false precision.

### Scope expansion

Separate the new request from the established scope. Explain its impact on tasks, dependencies, risks, and acceptance criteria before incorporating it as an approved change.

### Changed requirements or constraints

Reassess affected work and record the consequences. Preserve valid unaffected tasks where possible.

### Verification unavailable

Specify the verification that remains outstanding and its impact on completion confidence. Do not label the result verified.

### Missing ownership or authorization

Identify the responsible role or approval needed. Do not manufacture a commitment to fill the gap.

## 9. Output Expectations

A useful plan is:

- **Outcome-oriented:** every meaningful task contributes to an intended result.
- **Actionable:** tasks specify what needs to happen and how completion is recognized.
- **Dependency-aware:** prerequisites, blockers, and parallel work are explicit.
- **Proportionate:** detail matches the complexity and risk of the work.
- **Evidence-based:** estimates, ownership, dates, and status are supported or clearly qualified.
- **Adaptable:** changes can be incorporated without losing the reasoning behind the plan.
- **Verifiable:** completion criteria describe observable evidence.
- **Portable:** the plan does not depend on a specific agent platform or orchestration API.
- **Honest:** unknowns, limitations, unverified claims, and required approvals remain visible.
- **Context-preserving:** another person or agent can understand the objective and continue the work.

Do not optimize for the appearance of certainty. Optimize for a plan that people can execute, evaluate, and revise responsibly.

## 10. Acceptance Criteria for the Plan Skill

The skill is behaving as intended when it can:

1. Turn sufficiently clear requirements and accepted designs into actionable tasks.
2. Identify missing inputs that materially affect the plan.
3. Continue safe independent planning despite nonessential unknowns.
4. Distinguish hard, soft, external, and conditional dependencies.
5. Identify parallel work without ignoring coordination constraints.
6. Define observable completion and verification criteria.
7. Expose circular dependencies, contradictions, and unresolved decisions.
8. Avoid inventing owners, deadlines, budgets, estimates, approvals, or commitments.
9. Separate planning from requirements definition, design, implementation, and verification.
10. Adapt the level of detail to the scope and risk of the work.
11. Preserve context, assumptions, decisions, and limitations in handoffs.
12. Follow the repository's shared standards without silently changing their meaning.
13. Avoid claiming that planned work has been executed or verified.
14. Produce a useful result across supported agent environments without assuming automatic skill invocation.

These criteria define intended behavior. They do not establish that compatibility or performance has been tested.

## 11. Portability

- Use plain Markdown and standard Agent Skills metadata.
- Avoid dependence on a particular model provider or proprietary orchestration API.
- Do not assume that other skills can be invoked automatically.
- Do not assume access to project files, task trackers, calendars, dependency graph tools, or execution environments unless the runtime establishes their availability.
- Use explicit handoffs when direct skill invocation is unsupported.
- Keep task decomposition independent of a particular project-management tool unless the user specifies one.
- Treat compatibility with individual agent platforms as unverified until tested.

## 12. Maintenance

When updating Plan:

1. Preserve alignment with the shared core principles and handoff contract.
2. Keep planning distinct from requirements definition, technical design, implementation, and verification.
3. Prefer actionable tasks and meaningful dependencies over administrative overhead.
4. Remove duplicated rules when a shared standard already defines them.
5. Validate metadata, Markdown structure, whitespace, and internal references after edits.
6. Test representative planning scenarios before claiming behavioral compatibility.
7. Record meaningful changes through the repository's normal Git workflow.
