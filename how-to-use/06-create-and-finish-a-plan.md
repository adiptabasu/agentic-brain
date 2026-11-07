# Create and finish a plan

Use the [`plan` skill](../skills/plan/SKILL.md) for multi-step software work. It keeps a working plan in the active work session and uses relevant persona viewpoints.

## Create or update the session plan

> Plan `<workstream>`. Use the Software Architect viewpoint and any other relevant personas. Keep the working plan at `sessions/work/<session-id>/PLAN.md`. Clarify material open questions and do not implement the plan.

The Software Architect is the default viewpoint for software design and implementation plans. Add relevant perspectives such as Requirements Analyst, Security Architect, SRE, DevOps Engineer, Implementation Engineer, or Code Reviewer and Test Strategist; do not load unrelated personas.

## Publish the consolidated plan

> `plan finish` for `<workstream>`. Consolidate all relevant planning material into the session's `PLAN.md`, mark the plan ready, record the next action in session state, and stop without executing the plan.

`plan finish` consolidates in the same session-local file; it does not publish a tracked project document. The plan remains untracked until session termination removes the scratch folder. A finished plan does not authorize implementation, deployment, or other planned actions.
