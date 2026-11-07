# Choose and combine personas

Personas provide role-focused viewpoints. They do not grant permissions or replace repeatable skills. See the [persona catalogue](../personas/README.md) for each profile and its boundaries.

## Use one focused viewpoint

Name the persona and the question you want it to address:

> Use the Software Architect persona to compare two designs for this API. Use the confirmed requirements in `docs/requirements.md`, identify tradeoffs, and mark any unresolved decisions. Do not edit code.

## Combine viewpoints when needed

For cross-cutting work, state each perspective and what it should contribute:

> Review this authentication change from the Security Architect and Code Reviewer and Test Strategist perspectives. The security review should identify trust boundaries and abuse cases; the reviewer should examine the diff for defects and missing tests. Report disagreements and uncertainty separately. Do not make edits.

Use only the viewpoints that help answer the task. If recommendations conflict, describe the tradeoff and ask for a decision rather than silently choosing one.

## Personas and skills

Personas shape the perspective used to reason about a task. Skills, when added, will define repeatable procedures such as clarifying requirements, implementing a change, or verifying results. A persona does not imply that a skill has run, and neither grants approval for state-changing actions.
