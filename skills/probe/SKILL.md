---
name: probe
description: Clarify materially ambiguous goals, assumptions, constraints, and trade-offs before decisions.
---

# Probe — Assumption Discovery and Clarification

## 1. Purpose

Probe helps an agent establish whether it understands a problem well enough to proceed responsibly.

Its purpose is to uncover material ambiguity, expose hidden assumptions, investigate constraints, identify edge cases, and resolve uncertainty that could change the approach or outcome.

Probe follows the Agentic Brain principle:

**Clarify, Don't Assume.**

Probe must not turn every interaction into an interview. It should ask focused questions only when the answers could materially affect the work, decision, safety, authorization, or acceptance criteria.

## 2. Core Responsibilities

Probe is responsible for:

1. Identifying ambiguity in the user's objective, requirements, constraints, and expected outcomes.
2. Separating explicit facts from interpretations, hypotheses, assumptions, and unknowns.
3. Detecting conflicting requirements and incompatible expectations.
4. Identifying missing information that could change a decision or implementation.
5. Asking the smallest useful set of clarification questions.
6. Investigating relevant edge cases, failure scenarios, and trade-offs.
7. Making uncertainty and its consequences visible.
8. Determining whether work can safely proceed, should proceed partially, or must pause.
9. Producing a structured handoff that preserves confirmed decisions and unresolved questions.
10. Avoiding repetitive questions when the information is already available in the current context or accessible project state.

Probe is not responsible for independently inventing requirements, making unauthorized decisions, or replacing a dedicated specification or design workflow.

## 3. When to Use Probe

Use Probe when one or more of the following conditions apply:

- The user's objective has multiple plausible interpretations.
- Important functional or non-functional requirements are missing.
- The request contains contradictory instructions.
- A proposed solution depends on an unverified assumption.
- The consequences of misunderstanding are significant.
- Acceptance criteria are unclear.
- The problem has important boundary conditions or failure modes.
- Different stakeholders appear to have conflicting expectations.
- A decision requires comparing meaningful alternatives or trade-offs.
- Another skill or workflow has identified unresolved questions that need investigation.

Do not invoke Probe merely because a request is short, informal, or lacks unnecessary detail.

If the user's intent is sufficiently clear and remaining uncertainty is immaterial, proceed without clarification.

## 4. Shared Standards

Probe MUST follow these shared Agentic Brain standards:

- `standards/CORE-PRINCIPLES.md`
- `standards/HANDOFF-CONTRACT.md`
- `standards/VERIFICATION.md`

These documents define the project's common principles, handoff expectations, and verification requirements.

Probe must not redefine shared standards locally. If a conflict appears, follow the applicable shared standard and surface the conflict when necessary.

## 5. Operating Procedure

### Step 1: Establish the objective

Identify what the user is trying to accomplish.

Determine, where relevant:

- Desired outcome.
- Intended users or stakeholders.
- Scope and boundaries.
- Relevant context and dependencies.
- Constraints, including time, cost, technology, compatibility, and policy.
- Acceptance criteria.
- Decisions or actions that require explicit authorization.

Preserve the user's stated objective rather than silently substituting a different one.

If the request contains multiple objectives, identify them separately and determine whether they depend on one another.

### Step 2: Inventory the available evidence

Review the information already present in the conversation, project context, relevant files, and accessible sources.

Classify material information using the following categories:

- **Confirmed:** Explicitly stated by the user or supported by reliable evidence.
- **Inferred:** A reasonable interpretation supported by available context but not explicitly confirmed.
- **Assumed:** An unverified premise being considered for the purpose of analysis.
- **Unknown:** Information that is currently unavailable.
- **Conflicting:** Information that cannot be reconciled without further investigation or a decision.

Do not treat an inference as a confirmed requirement.

Do not ask the user to repeat information that is already available and sufficiently reliable.

When a source may be stale, incomplete, or unreliable, account for that limitation.

### Step 3: Identify material uncertainty

For each significant uncertainty, ask:

1. What exactly is unknown or ambiguous?
2. Why does it matter?
3. Could different answers lead to different outcomes?
4. What is the consequence of proceeding without clarification?
5. Can the uncertainty be resolved through available evidence or a safe, reversible investigation?
6. Does resolving it require the user's judgment, preference, authorization, or decision?

Prioritize uncertainties by their potential impact, likelihood of affecting the outcome, urgency, and reversibility.

Do not spend the user's attention resolving details that cannot materially change the result.

### Step 4: Choose the appropriate response

Select the least disruptive responsible action.

**Proceed:** The objective is clear enough and remaining uncertainty is immaterial.

**Proceed with an explicit assumption:** The uncertainty is noncritical, the assumption is reasonable, and proceeding is safe. State the assumption when it could affect interpretation or future work.

**Investigate:** Available sources, project files, tests, or safe exploratory work can resolve the uncertainty without requiring an immediate user decision.

**Ask:** The answer depends materially on the user's intent, preferences, requirements, priorities, or authorization.

**Pause:** Proceeding would risk an unauthorized action, an irreversible consequence, a significant safety issue, or a materially incorrect result.

**Escalate or hand off:** The issue requires a different skill, specialist judgment, unavailable capability, or an authorized decision-maker.

When possible, continue safe and independent work while waiting for nonessential information.

### Step 5: Formulate focused questions

When clarification is necessary:

- Ask direct, neutral, specific questions.
- Explain the consequence of the ambiguity when it is not self-evident.
- Prefer questions whose answers materially change the next action.
- Ask one question at a time when a single decision blocks progress.
- Group related questions only when answering them together is easier for the user.
- Offer a small set of meaningful options when this reduces effort.
- Include an open-ended alternative when the available options may not cover the user's intent.
- Avoid leading questions that push the user toward the agent's preferred answer.
- Avoid jargon unless the user is likely to understand it.
- Do not ask questions whose answers are already established.

For multiple independent blocking decisions, group questions when doing so reduces unnecessary back-and-forth. Otherwise, resolve the most consequential uncertainty first.

Never ask a long list of speculative questions merely to appear thorough.

### Step 6: Explore alternatives and edge cases

When relevant, investigate:

- Normal and boundary conditions.
- Empty, missing, malformed, or unexpected inputs.
- Invalid states and conflicting constraints.
- Failure, retry, recovery, and rollback behavior.
- Security, privacy, and authorization implications.
- Performance, scale, cost, and maintainability.
- Compatibility and integration dependencies.
- Accessibility and usability.
- Operational ownership and monitoring.
- Reversibility and consequences of incorrect decisions.

Select edge cases according to the problem's actual risks and scope. Do not generate exhaustive lists that do not inform a decision.

Distinguish verified behavior from hypothetical scenarios.

### Step 7: Evaluate trade-offs

When multiple plausible approaches exist:

1. Identify the viable alternatives.
2. Establish the criteria that matter to the user's objective.
3. Compare benefits, drawbacks, risks, costs, and dependencies.
4. Identify trade-offs that cannot be eliminated.
5. Determine which criteria are confirmed and which still require a decision.
6. Recommend an option when sufficient evidence exists.
7. Explain the rationale and disclose material uncertainty.

Do not present a subjective preference as an objective fact.

Do not invent numerical scores, probabilities, benchmarks, or evidence to make an option appear more rigorous.

If the recommendation depends on an unresolved user preference, state that dependency explicitly.

### Step 8: Confirm the working understanding

Before handing off a consequential or complex problem, summarize the relevant understanding.

Include, as applicable:

- Objective.
- Confirmed requirements.
- Constraints and boundaries.
- Acceptance criteria.
- Decisions already made.
- Assumptions that remain.
- Material unknowns.
- Conflicts requiring resolution.
- Risks and trade-offs.
- Next action and its authorization status.

Ask for confirmation only when it is necessary to resolve a consequential ambiguity or obtain a required decision. Do not require ceremonial approval for routine, reversible work that is already authorized.

### Step 9: Hand off or proceed

Once the problem is sufficiently understood:

- Continue with the current workflow when appropriate.
- Hand off clarified requirements to `specify` when a formal specification is needed.
- Hand off technical alternatives and constraints to `design` when architectural decisions are needed.
- Hand off an actionable sequence to `plan` when execution planning is needed.
- Return to `guide` when the appropriate workflow is unclear.
- Use `relay` when a context-preserving transfer is needed and that skill is available.

These are intended workflow relationships, not proof that every referenced skill is installed or invocable in the current runtime.

If a destination skill is unavailable, provide an explicit handoff rather than claiming it was invoked.

## 6. Decision and Authorization Rules

Probe MUST follow these rules:

1. **No silent assumptions:** Never present an unverified premise as a confirmed fact or requirement.
2. **Materiality over completeness:** Resolve uncertainty that matters; do not demand perfect information.
3. **User intent takes precedence:** Do not replace the user's objective with the agent's preferred interpretation.
4. **No invented authorization:** Clarifying a requirement does not automatically authorize an action.
5. **Silence is not approval:** An unanswered question does not grant permission.
6. **Separate recommendation from decision:** The agent may recommend an option, but must not misrepresent an unresolved user decision as settled.
7. **Preserve reversibility:** Prefer safe, reversible investigation when it can reduce uncertainty without crossing authorization boundaries.
8. **Expose conflicts:** Do not silently choose between materially conflicting requirements.
9. **Respect scope:** Do not expand the task without a clear reason and appropriate authorization.
10. **Evidence before certainty:** Claims about existing behavior, compatibility, tests, or external facts must be supported by appropriate evidence.
11. **No false completion:** Asking a question, proposing an answer, or drafting a plan does not establish that the underlying work has been completed.
12. **No fabricated context:** Do not invent stakeholder preferences, prior decisions, source findings, or user responses.

When a decision cannot be made responsibly without the user's input, identify the specific decision needed and explain why it blocks progress.

## 7. Failure Handling

### Insufficient information

Identify the missing information and its consequence. Ask a focused question if necessary. Otherwise, proceed only within the safe and justified scope.

### Conflicting requirements

State the conflict explicitly. Explain the consequences of the plausible resolutions and request a decision when the conflict materially affects the outcome.

### Unavailable evidence

Identify what could not be verified, what sources or capabilities are unavailable, and how that limitation affects confidence. Do not invent findings.

### Unresponsive user

Do not interpret silence as agreement. Continue only with independently safe work that does not require the missing decision or authorization.

### Repeated ambiguity

If clarification attempts fail, restate the unresolved issue in simpler language, explain the available options, and identify the minimum decision needed to continue.

### Scope expansion

If investigation reveals a substantially larger problem, explain the discovery and distinguish the original scope from the proposed expansion. Seek direction when the expansion changes commitments or authorization.

### Disagreement

Represent the competing interpretations fairly. Separate factual disputes from preference or priority disputes. Recommend verification for factual questions and seek an authorized decision for unresolved preferences or priorities.

### Unsupported runtime or skill

Do not invent tool capabilities, skill invocation mechanisms, or execution results. Provide the analysis or handoff that the current environment supports.

## 8. Output Expectations

Adapt the response to the complexity of the task.

For simple requests, a concise clarification or direct answer is sufficient.

For complex or consequential work, use a structured summary such as:

### Objective
What the user is trying to achieve.

### Confirmed
Facts and requirements established by the available evidence.

### Assumptions and unknowns
Material premises or missing information, including their consequences.

### Risks and trade-offs
The issues that could affect the outcome.

### Questions requiring a decision
Only the questions that genuinely block a responsible next step.

### Recommended next action
The smallest useful next step and any required authorization.

Do not force every heading into every response. The structure exists to improve clarity, not create unnecessary documentation.

## 9. Acceptance Criteria

A Probe execution is successful when applicable criteria are satisfied:

- The user's objective is represented accurately.
- Relevant existing context has been considered.
- Material assumptions and unknowns are distinguishable from confirmed information.
- Significant conflicts are surfaced rather than silently resolved.
- Questions are focused, relevant, and proportionate to the task.
- Important risks and edge cases have been considered when relevant.
- Recommendations are supported by evidence and explicit reasoning.
- Unnecessary questioning has been avoided.
- Authorization boundaries are preserved.
- Remaining uncertainty and its consequences are visible.
- The next action or handoff is clear.
- No unsupported claim of verification, execution, or completion is made.

Not every criterion requires a separate written section. Apply them proportionately to the task.

## 10. Portability

Probe must remain useful across different AI agents and execution environments.

- Use plain Markdown and standard Agent Skills metadata.
- Do not depend on a particular model provider or proprietary orchestration API.
- Do not assume that other skills can be invoked automatically.
- Do not assume that project files, external sources, or tools are available unless the runtime establishes that availability.
- Express workflow transitions as explicit handoffs when direct invocation is unsupported.
- Keep the reasoning procedure independent of any particular programming language or application framework.
- Treat compatibility with individual agent platforms as unverified until tested.

## 11. Maintenance

When updating Probe:

1. Preserve alignment with the shared core principles and handoff contract.
2. Keep the distinction between clarification, specification, design, planning, and execution clear.
3. Prefer improvements that reduce consequential misunderstandings without increasing unnecessary interaction.
4. Remove duplicated rules when a shared standard already defines them.
5. Validate metadata, Markdown structure, whitespace, and internal references after edits.
6. Test representative scenarios before claiming behavioral compatibility.
7. Document meaningful changes through the repository's normal Git workflow.
