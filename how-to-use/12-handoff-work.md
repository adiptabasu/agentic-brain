# Hand work to another person or agent

Use this when work will continue in another chat, agent, team, or person and you do not want decisions or open questions to be lost.

Invoke `relay` or say:

> Read `skills/relay/SKILL.md` and follow it. Prepare a handoff for [person, team, or next skill/agent] about [objective]. Use the shared handoff contract. Include confirmed context and constraints, decisions and approval status, relevant artifact paths and status, blockers, unresolved questions, verification evidence, and one concrete next action. Do not claim the recipient has access to files or systems unless that is confirmed.

Review the handoff. Correct stale status, missing decisions, or any proposal mislabeled as approved. Make sure the paths are relevant to the recipient and the next action is within its authority.

Before sending, ask for a destination-appropriate version:

> Produce a concise handoff I can paste into [new chat / issue / email / task]. Keep unresolved items and required approvals explicit. Do not include secrets or unnecessary personal data.

A handoff transfers context; it does not grant approval, create access, or prove that its referenced artifacts are available. The receiving agent should check critical references before acting and ask about any missing dependency that affects the next step.
