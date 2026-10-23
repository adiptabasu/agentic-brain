# Skill Template

**Template version:** 1.0

> Replace the placeholders and remove guidance that does not belong in the finished skill. Do not leave unresolved placeholders in a released skill.

## 1. Skill Metadata

- **Name:** `<skill-name>`
- **Version:** `0.1.0`
- **Purpose:** `<one-sentence purpose>`
- **Status:** `draft`
- **Owner or maintainer:** `<person or team, if known>`

The skill name must match its directory name and follow the repository's naming conventions.

Use only metadata supported by the target agent environment. Keep additional project metadata in documentation or manifests when necessary.

## 2. Purpose and Boundaries

### Purpose

Explain the specific problem this skill solves and the outcome it is intended to produce.

### In scope

- `<responsibility>`
- `<responsibility>`

### Out of scope

- `<explicit exclusion>`
- `<explicit exclusion>`

### Non-goals

Describe outcomes that must not be inferred from this skill's invocation.

## 3. Invocation

### When to use

Describe explicit requests, conditions, or workflow states that justify invoking the skill.

### When not to use

Identify cases better handled by another skill or where invocation would be premature or inappropriate.

### Required inputs

List information required to begin safely and effectively.

### Optional inputs

List information that improves results but is not essential.

### Invocation rules

- Do not infer authorization from invocation alone.
- Do not assume that a recommendation is an approved decision.
- Ask focused questions when missing information could materially change the outcome.
- Leave nonessential unknowns unresolved when safe progress is possible.

## 4. Shared Principles

The skill must comply with:

- `standards/CORE-PRINCIPLES.md`
- `standards/HANDOFF-CONTRACT.md`, when transferring work
- `standards/VERIFICATION.md`, when making or verifying outcome claims

If a platform cannot access repository-relative files at runtime, its adapter or packaging process must provide the relevant rules without silently changing their meaning.

## 5. Operating Procedure

Define an ordered workflow appropriate to this skill.

1. **Understand:** Establish the objective, context, constraints, and expected outcome.
2. **Check readiness:** Identify missing critical information, authorization, dependencies, and blockers.
3. **Clarify:** Ask focused questions when uncertainty materially affects correctness, safety, scope, or approval.
4. **Act:** Perform only work within the authorized scope.
5. **Evaluate:** Compare the result against explicit criteria.
6. **Verify:** Gather evidence proportionate to the task's risk.
7. **Report or hand off:** State the outcome, unresolved items, evidence, and next action.

Replace this generic sequence with a specialized procedure where appropriate. Do not retain irrelevant steps merely for uniformity.

## 6. Decision Rules

Document the decisions this skill may make independently and those requiring clarification or approval.

| Decision category | Expected behavior |
|---|---|
| Reversible, low-impact implementation detail within scope | Use reasonable judgment; disclose material choices |
| Ambiguity that could materially change the result | Ask a focused question |
| Consequential or irreversible action | Obtain required authorization before acting |
| Conflict with an approved requirement | Surface the conflict; do not silently override the requirement |
| Missing nonessential information | Continue safely if possible and preserve the uncertainty |
| Missing critical information | Pause dependent work and request clarification |

Adapt this table to the skill's actual responsibilities and risk profile.

## 7. Inputs, Outputs, and Artifacts

### Inputs

Describe expected input formats, sources, assumptions, and validation.

### Outputs

Specify the deliverables, expected structure, and acceptance criteria.

### Artifact handling

- Do not claim to have created or modified an artifact without evidence.
- Do not claim that an artifact exists merely because it was planned or referenced.
- Preserve user-provided work unless changes are within the authorized scope.
- Identify proposed, generated, modified, and verified artifacts distinctly.

## 8. State and Continuity

Define what information must survive between invocations.

When relevant, preserve:

- Objective and current status.
- Confirmed requirements and constraints.
- Approved and proposed decisions, distinguished clearly.
- Authorized assumptions and their scope.
- Artifacts and their actual status.
- Verification results and supporting evidence.
- Unresolved questions and blockers.
- Next action and required authorization.

Do not invent state or imply persistent memory when the runtime does not provide it.

## 9. Failure Modes and Recovery

List likely failure modes and the appropriate response.

For each significant failure, specify:

- Observable symptom.
- Potential impact.
- Safe diagnostic action.
- Recovery options.
- Conditions requiring escalation or user input.

Do not present an unverified explanation as the established root cause.

## 10. Verification and Acceptance

Define objective completion criteria for this skill.

For each important criterion, specify an appropriate check and the evidence required.

Use `standards/VERIFICATION.md` for verification states and reporting expectations.

A skill must not report full completion when material acceptance criteria remain unmet or unverified.

## 11. Handoff

When another skill, agent, or person must continue the work, use `standards/HANDOFF-CONTRACT.md`.

Include the relevant objective, constraints, decisions, artifacts, unresolved items, blockers, verification evidence, and next action.

A handoff does not grant permissions or create approval.

If no handoff is necessary, state the final outcome directly.

## 12. Examples

### Appropriate use

Provide a realistic example showing when and how this skill should be used.

### Clarification example

Show how the skill responds when a critical ambiguity prevents safe or correct progress.

### Boundary example

Show a case where the skill must decline to make an unsupported assumption, exceed its authorization, or claim unverified success.

Keep examples consistent with the skill's actual capabilities.

## 13. Portability

Separate the skill's behavior from platform-specific details.

Document any dependencies on:

- Invocation syntax.
- Filesystem layout.
- Available tools.
- Permissions and approval mechanisms.
- Context or memory persistence.
- Handoff transport.
- Verification capabilities.

Do not claim compatibility with an agent or platform until it has been tested and the evidence recorded.

## 14. Maintenance

Record:

- Version and change history.
- Known limitations.
- Compatibility test status.
- Outstanding issues.
- Migration notes for breaking changes.

Update this section when the skill's behavior or contract changes materially.
