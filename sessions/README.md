# Work sessions

- `work/<session-id>/` contains temporary scratch and is ignored by Git. Use IDs like `YYYY-MM-DD-<workstream>`; add a suffix if needed.
- `handoffs/<workstream>.md` is the single tracked checkpoint for paused or completed work. Update it in place; do not keep transcripts or duplicate history.
- This index tracks active, paused, and completed work awaiting termination. After terminating paused work, keep its row and handoff but clear the session folder. After completed work is terminated, remove its row and obsolete handoff.
- Working and finished plans stay in the ignored session folder; `plan finish` consolidates the plan in place. Session termination removes the plan with scratch.

| Workstream | Status | Updated | Session folder | Handoff |
|---|---|---|---|---|
| _No sessions_ |  |  |  |  |

Start with the [session skill](../skills/session/SKILL.md). A new chat should read this index and only the relevant handoff.
