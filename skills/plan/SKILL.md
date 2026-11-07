---
name: plan
description: Create actionable software work plans in a session and consolidate planning material into one session-local document when the user says “plan finish.”
---

# Plan software work

Use for multi-step feature, architecture, migration, debugging, or operational work that benefits from an actionable plan. Keep the plan only in the active session. Session termination deletes the plan with the ignored scratch folder.

## Create or update a session plan

1. Clarify the goal, scope, constraints, and success conditions when they are materially unclear. Use the Requirements Analyst viewpoint to resolve requirement questions; distinguish confirmed facts, proposals, and open questions.
2. Work in the active workstream's session folder. If no session exists, use [session](../session/SKILL.md) to start or resume one. Keep a single working document at `sessions/work/<session-id>/PLAN.md`.
3. Apply at least one relevant persona viewpoint. Use [Software Architect](../../personas/software-architect.md) by default for software design and implementation plans. Add only relevant specialists, such as Requirements Analyst, Security Architect, SRE, DevOps Engineer, Implementation Engineer, or Code Reviewer and Test Strategist. Persona profiles provide viewpoints; they are not separate agents or approval.
4. Use [write-document](../write-document/SKILL.md) for `sessions/work/<session-id>/PLAN.md`. Keep one plan file from the start and update it in place. Include the goal and scope, ordered deliverables or steps, dependencies, decisions and open questions, risks, and acceptance or verification criteria. Keep steps actionable and proportionate; do not invent estimates, owners, deadlines, or requirements.

## `plan finish`

Treat the user's `plan finish` request as authorization to consolidate the plan in the active session; it does not authorize implementing the plan or making the plan a tracked project document.

1. Review the current `PLAN.md` and only the relevant planning material in the active session. Resolve contradictions where evidence allows; retain unresolved items as open questions.
2. Consolidate relevant planning material into the single `PLAN.md` in the active session folder. Keep persona viewpoints, scope, ordered actions, dependencies, risks, decisions/open questions, and acceptance or verification criteria; distinguish agreed items from proposals.
3. Mark `PLAN.md` status as `ready` and record the next action in session state. A pause may carry a concise summary into the durable handoff, but keep the plan itself only in session scratch.
4. Do not create a plan under another project directory or delete intermediate material as part of `plan finish`. Session termination removes `PLAN.md` along with the ignored scratch folder. Do not begin execution unless the user separately asks.

See the [planning guide](../../how-to-use/06-create-and-finish-a-plan.md). Follow project clarification, local change approval, and verification rules.
