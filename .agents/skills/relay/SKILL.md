---
name: relay
description: Prepare, validate, and transfer concise context between people, agents, or workflow stages using explicit objectives, decisions, artifacts, blockers, evidence, and next actions. Use when work must continue across a handoff without losing intent or inventing approval.
---

# Relay

## 1. Purpose

Relay prepares and supports clear transfers of work between people, agents, teams, or workflow stages.

It preserves the context a receiver needs to continue safely: the objective, current status, constraints, decisions and their approval states, artifacts, unresolved items, blockers, verification evidence, and next action.

Relay follows **Clarify, Don't Assume**. It distinguishes confirmed facts from proposals, authorized assumptions, unknowns, and unverified claims. It treats a handoff as a transfer of context, never as a grant of permission or proof of completion.

The shared Handoff Contract is canonical. Relay helps produce and assess a handoff that conforms to it; it does not replace the source skill's work, make the receiver's decisions, or silently alter the user's intent.

## 2. Core Responsibilities

### 2.1 Establish why the handoff is needed

Identify:

- The objective or work being transferred.
- The source and intended receiver.
- Why responsibility or context is changing.
- The current state of the work.
- What the receiver is expected to do next.
- Any limits on what can be shared or acted upon.

If the receiver or next action is unknown, state that explicitly instead of inventing one.

### 2.2 Preserve the objective and confirmed context

Summarize the user's intended outcome, relevant requirements, constraints, and prior decisions accurately.

Keep the handoff concise, but do not omit information that could materially change the receiver's action.

Distinguish:

- Confirmed facts and requirements.
- Approved decisions and who or what approved them.
- Proposals and recommendations.
- Authorized assumptions and their scope.
- Unknown or conflicting information.
- Evidence-supported and unverified results.

Do not convert a suggestion into an instruction or a tentative decision into an approval.

### 2.3 Represent status accurately

Use the status vocabulary and meanings in the Handoff Contract.

Select a status that applies to the transferred work, not the overall project by implication. In particular:

- ready means the assigned next task has the context and authorization it needs to begin.
- needs-input means clarification or a decision is required.
- blocked means a concrete dependency prevents progress.
- partial means useful work is complete but criteria remain unmet.
- completed applies only to the work represented by that handoff.

A handoff marked ready is not blanket approval for consequential action.

### 2.4 Reference artifacts and evidence accurately

For each material artifact, state its path or identifier and its actual status, such as proposed, created, modified, approved, or verified.

Confirm that references are available when access allows. If access is unavailable, label the reference as unconfirmed.

Summarize verification evidence with the relevant check, result, and limitation. A plan to run a check is not a result. A report from another party is not independently observed unless it was checked.

Do not include secrets or unnecessary personal information. Follow applicable access and retention requirements.

### 2.5 Make unresolved items and blockers actionable

For each unresolved item, explain what is unknown and why it matters.

For each blocker, identify what must happen, who or what it depends on when known, and which work is affected.

Separate nonessential unknowns from blockers. The receiver may proceed with independent work when it is safe and authorized.

### 2.6 Define the next action

State the smallest useful next action clearly.

When there is a target skill or role, name it only if that capability is available or clearly identified as a requested recipient. Do not claim a skill was invoked merely because it is named in a handoff.

Clarify any required input, decision, permission, or evidence before the next action can begin.

### 2.7 Preserve provenance and context

Include the source of important requirements, approvals, and evidence where practical.

Record dates, versions, commits, environments, or other identifiers when they are necessary to avoid ambiguity.

Do not overstate memory or persistence. A handoff only preserves information actually included or linked and accessible to the receiver.

### 2.8 Check that the handoff is usable

Before sending or presenting a handoff, check that the receiver can answer:

- What outcome is expected?
- What is known and approved?
- What remains uncertain or blocked?
- What artifacts should be inspected?
- What evidence supports reported results?
- What action should happen next?
- What authorization boundaries apply?

If those questions cannot be answered, improve the handoff or label the missing context.

## 3. When to Use Relay

Use Relay when:

- Work moves between skills, agents, teams, or people.
- A task pauses and must resume later without reconstructing context.
- A change needs a structured transfer to an implementer, reviewer, verifier, or decision-maker.
- A blocked task needs a precise request to the person or system that can unblock it.
- A project needs a concise status transfer with evidence and outstanding decisions.
- The receiver needs to know what is approved and what still requires approval.

Do not use Relay as a substitute for:

- Performing the originating skill's work.
- Defining requirements or making the user's decision.
- Granting authorization or approving a release.
- Verifying a claimed outcome.
- Independently reviewing the quality of the work.
- Storing information in a system that the runtime does not provide.

Relay may prepare content for another channel or system when authorized and available. It must not send messages or modify external records without the required user authorization and tool permission.

## 4. Shared Standards

Follow:

- standards/CORE-PRINCIPLES.md
- standards/HANDOFF-CONTRACT.md
- standards/SKILL-TEMPLATE.md
- standards/VERIFICATION.md

The Handoff Contract is the authoritative specification for fields, statuses, decision states, knowledge states, and fallback representation.

Apply the shared rules:

1. Preserve the user's intent and explicit constraints.
2. Keep proposals, assumptions, approvals, and verified facts distinct.
3. Do not infer consent from silence or from a handoff status.
4. Preserve material unresolved items and blockers.
5. Do not claim evidence, artifacts, or actions exist without confirmation.
6. Include only context needed for safe and effective continuation.
7. Protect sensitive information and follow authorization boundaries.

If a local workflow requires a different transport format, preserve the contract's meaning.

## 5. Operating Procedure

### Step 1: Identify source, receiver, and objective

Determine who or what is handing off work, who should receive it, and what outcome the transferred work serves.

If the handoff is only a draft, label it as a draft. If the receiver is not established, do not invent a person, skill invocation, or destination.

### Step 2: Gather the current state

Use available conversation context, artifacts, and observed results to establish what has happened.

Record the current status and what remains. Distinguish completed work from work that is merely planned, requested, or reported by another source.

Do not access unavailable systems or imply that referenced artifacts were inspected.

### Step 3: Preserve requirements, decisions, and constraints

Include only the context relevant to the next step, while retaining material boundaries.

For each consequential decision, include its status and approval evidence when available. Clearly label proposals, assumptions, deferred decisions, and superseded decisions.

### Step 4: Inventory artifacts and evidence

List relevant artifacts and their actual status. Include paths, versions, or identifiers as appropriate.

Summarize checks performed and evidence observed. Include failures, limitations, and contradictory results that affect continuation.

Avoid pasting large amounts of source data when a stable, accessible reference is sufficient.

### Step 5: Identify unresolved items and blockers

Separate questions that require a response from unknowns that do not prevent the next safe step.

For each blocker, specify the dependency and affected work. Do not label ordinary follow-up as a blocker unless progress actually depends on it.

### Step 6: Select contract status and next action

Use the Handoff Contract's vocabulary and apply it to the transferred task.

Include target_skill and next_action when assigning a next step. Verify that the next step has the required context and authorization before describing the handoff as ready.

If a decision or permission is missing, use needs-input or blocked as appropriate and state the precise request.

### Step 7: Minimize and protect information

Remove unrelated details and unnecessary sensitive data. Keep enough evidence and provenance for the receiver to validate important claims.

Use approved storage and transfer channels. Do not place credentials, tokens, or private user data in an ordinary handoff.

### Step 8: Validate the handoff

Check required core fields, vocabulary, references, approval states, and next action against the Handoff Contract.

Check internal consistency: status must match blockers and unresolved items; artifact status must match observed state; claims must match evidence.

### Step 9: Deliver or prepare the handoff

If the user asks only for a draft, present the handoff without transmitting it.

If transmission or an external record update is requested, verify that the action is authorized and supported by available tools. Report the actual result and any delivery limitation.

## 6. Handoff Deliverable Structure

Use the YAML reference representation in standards/HANDOFF-CONTRACT.md where supported. Otherwise, provide Markdown with equivalent meaning.

A handoff should include, as applicable:

- Handoff version.
- Objective.
- Source and target skill, role, or person.
- Status.
- Context summary and constraints.
- Artifacts and their status.
- Decisions and approval states.
- Unresolved items.
- Blockers.
- Verification evidence.
- Next action.

For concise work, omit optional fields only when doing so does not lose material context. Use the fallback headings in the shared contract when YAML is unavailable.

Do not leave template placeholders or illustrative sample values in a delivered handoff.

## 7. Decision and Authorization Rules

### 7.1 Formatting and summarization

Relay may choose a clear, concise format that preserves the contract's meaning and the user's intent.

It may omit irrelevant details but must not omit material constraints, approvals, blockers, failures, or evidence limitations.

### 7.2 Decision status

Relay may record a decision's status based on explicit evidence. It must not decide for the user or receiver whether a proposal is approved, a risk is accepted, or work is complete.

When approval evidence is missing, mark the status as proposed, needs-approval, unknown, or otherwise appropriate under the shared contract.

### 7.3 External transmission

Creating a draft does not require external transmission. Sending a message, creating an external record, sharing a file, or assigning work requires user authorization and appropriate tool access.

A request to prepare a handoff is not automatically authorization to transmit it.

### 7.4 New or expanded work

A handoff cannot enlarge the original scope or authorize the receiver to take actions the user did not authorize.

If the next action entails consequential work beyond existing authorization, identify that requirement in the handoff.

### 7.5 Conflict handling

If current instructions conflict with prior context, preserve the conflict and identify which decision is needed. Do not silently resolve it in the handoff.

## 8. Failure Handling

### 8.1 Missing receiver or next action

Prepare a draft that identifies the missing destination or decision. Do not mark it ready if a specific receiver or action is necessary to begin.

### 8.2 Context is incomplete

State which facts, requirements, or artifacts are missing and how they affect continuation. Include independent work that can safely proceed, if any.

### 8.3 Artifact reference cannot be confirmed

Label the artifact reference as unverified or unavailable. Do not imply the receiver can access it.

### 8.4 Approval state is unclear

Mark the decision as proposed or needing approval and state who must decide if known. Do not infer approval from an earlier discussion, silence, or a status label.

### 8.5 Handoff is too large

Prioritize the objective, constraints, decisions, blockers, evidence, and next action. Move supplementary context to accessible references when appropriate, and check that the receiver can access them.

### 8.6 Handoff contains sensitive information

Redact or replace sensitive content with a safe reference where possible. If the information is necessary, use an approved restricted channel and audience.

### 8.7 Delivery fails or is unavailable

Report that the handoff was prepared but not delivered. Provide the prepared content or a safe alternative when appropriate. Do not claim delivery from an attempted send.

### 8.8 Status and context disagree

Resolve the inconsistency using observed evidence. If it cannot be resolved, use a less conclusive status and explain the discrepancy.

## 9. Output Expectations

A Relay output should be:

- Concise but sufficient for the receiver to continue.
- Accurate about current status and artifact availability.
- Explicit about decisions and approval states.
- Traceable to relevant requirements and evidence.
- Clear about blockers, unresolved items, and next action.
- Safe for its intended audience.
- Honest about whether it was drafted, delivered, or acknowledged.

Do not claim that a receiver read or accepted a handoff without evidence. Delivery, acknowledgment, and completion are separate states.

## 10. Acceptance Criteria

Relay is complete when:

1. The objective and transferred scope are clear.
2. Material requirements, constraints, and decisions are preserved accurately.
3. Knowledge and approval states are represented correctly.
4. Artifacts and evidence have accurate status and usable references.
5. Unresolved items and blockers are actionable.
6. The status and next action conform to the Handoff Contract.
7. Sensitive information and authorization boundaries are respected.
8. The receiver can identify what to do next without relying on invented context.
9. Any transmission outcome is reported accurately.

If a receiver cannot proceed safely because required context or approval is missing, report the handoff as needing input or blocked rather than ready.

## 11. Portability

Relay does not depend on a specific messaging service, task tracker, orchestration runtime, or agent platform.

Environments differ in support for structured data, persistence, direct skill invocation, and message delivery. Use an available representation that preserves the Handoff Contract and clearly state transport limitations.

Do not claim persistent memory, delivery, acknowledgment, or direct invocation unless the environment provides evidence for it.

Adapters may add platform-specific metadata but must preserve objective, status, decisions, constraints, evidence, blockers, and next action.

## 12. Maintenance

Update this skill when the Handoff Contract or handoff lifecycle changes materially.

When maintaining it:

- Keep field and status definitions aligned with the shared contract.
- Preserve the distinction among draft, delivered, acknowledged, and completed.
- Keep user authorization boundaries explicit.
- Avoid duplicating contract content where a direct reference is sufficient.
- Ensure examples contain no unresolved placeholders or implied approvals.
- Record material limitations and compatibility evidence where the repository provides a place for them.
- Ensure metadata name remains relay and matches the directory.

Relay exists to make transitions reliable. A useful handoff carries enough verified context to continue while keeping uncertainty, authority, and responsibility visible.
