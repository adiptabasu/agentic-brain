# Handoff Contract

**Version:** 1.0

## 1. Purpose

A handoff transfers relevant context and the next action between skills,
agents, or people.

This contract defines the logical interchange format. YAML is the reference
representation; an environment may use equivalent structured data or Markdown
when necessary.

## 2. Reference Example

```yaml
handoff_version: "1.0"
objective: "Implement the approved feature"
source_skill: "specify"
target_skill: "plan"
status: "ready"

context:
  summary: "Requirements have been clarified."
  constraints:
    - "Preserve existing API compatibility"

artifacts:
  - path: "docs/SPECIFICATION.md"
    status: "approved"

decisions:
  - id: "DEC-001"
    summary: "Use the agreed API contract"
    status: "approved"

unresolved_items: []
blockers: []
verification: []

next_action: "Create an ordered implementation plan"
```

This example is illustrative. Referenced files must not be assumed to exist or
be approved merely because they appear in an example.

## 3. Core Fields

- `handoff_version`: Version of this contract.
- `objective`: Purpose of the transferred work.
- `source_skill`: Originating skill, or an explicitly identified non-skill
  origin.
- `status`: State of the handoff.

When a next step is defined, include `target_skill` and `next_action`.
They may be omitted when no next step is assigned.

Other fields are optional but must be included when needed to preserve
material context, decisions, unresolved items, blockers, or verification.

## 4. Handoff Status Vocabulary

- `ready`: The assigned next task has the information and authorization it
  needs to begin. This does not mean the entire project is approved.
- `needs-input`: A clarification or decision is required.
- `blocked`: Progress depends on a blocker being resolved.
- `partial`: Useful work is complete, but completion criteria remain unmet.
- `completed`: The originating skill's completion criteria have been met.

Use `completed` only for the work represented by that handoff. It does not
imply that the overall project is complete.

## 5. Decision States

Each consequential decision should preserve, when applicable:

- `id`
- `question`
- `options`
- `selected_option`
- `rationale`
- `risks`
- `status`

Decision statuses:

- `proposed`
- `needs-approval`
- `approved`
- `deferred`
- `superseded`

Record the approving party or approval evidence when available.

A recommendation is not approval. Silence is not approval. A handoff does not
create approval.

## 6. Knowledge States

Use explicit labels for important context:

- `confirmed`
- `proposed`
- `assumed`
- `unknown`
- `verified`
- `unverified`

An authorized assumption must retain its scope and authorization context.

Do not convert a proposal or assumption into a confirmed fact when passing
work to another skill.

## 7. Unresolved Items and Blockers

An unresolved item should explain what is unknown and why it may matter.

A blocker should explain what must happen before dependent work can proceed.

Do not hide unresolved questions inside general prose if they affect the next
skill's behavior.

If an unresolved item is nonessential to the next step, work may continue
without resolving it, provided doing so is safe and the uncertainty remains
visible.

## 8. Receiving-Skill Obligations

The receiving skill must:

1. Read the handoff and check that it has the required context.
2. Preserve confirmed constraints and approved decisions.
3. Distinguish proposals and assumptions from approvals.
4. Ask for missing critical information before dependent work.
5. Report conflicts between the handoff and current evidence or instructions.
6. Check referenced artifacts when that is necessary and possible.
7. Avoid claiming verification succeeded without suitable evidence.

A handoff never grants new permissions by itself.

## 9. Fallback Representation

If structured data is unsupported, use Markdown with equivalent sections:

- Objective
- Source and target
- Status
- Confirmed context and constraints
- Decisions and approval states
- Artifacts
- Unresolved items
- Blockers
- Verification evidence
- Next action

The fallback must preserve the meaning of the contract, not merely its headings.
