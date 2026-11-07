---
name: session
description: Start, resume, pause, complete, or terminate multi-chat development work using dated scratch folders and concise durable handoffs.
---

# Manage a work session

Use for feature development, debugging, or other software work likely to span chats or days. Keep scratch artifacts local under `sessions/work/`; preserve only the latest handoff per workstream.

## Start or resume

1. Confirm the workstream and goal when unclear. Use a stable lowercase workstream slug.
2. Check `sessions/README.md`. For an active workstream, resume its listed session or close it before creating another. For a paused workstream, read only its handoff; do not load other workstreams.
3. Resume an existing closed scratch folder in place. If it was terminated, create `sessions/work/YYYY-MM-DD-<workstream>/SESSION.md` from `sessions/SESSION-TEMPLATE.md`; add a numeric suffix if the ID exists. Seed it from the handoff and update the index.
4. Keep temporary plans, notes, logs, and generated files in that ignored folder. Save real project changes at their normal paths.

Use the [plan skill](../plan/SKILL.md) for session-local planning. `plan finish` consolidates the plan in the session's `PLAN.md`; a handoff may carry a concise summary and next action, but the plan itself remains untracked and is deleted with scratch at termination.

## Close or complete

- **Pause:** Use [write-document](../write-document/SKILL.md) to update `sessions/handoffs/<workstream>.md` in place with status, decisions, progress, changed files, checks, blockers, and next actions. Mark the scratch session `closed`; update the index. Preserve both handoff and scratch folder.
- **Complete:** First update only relevant source-of-truth project files. Do not edit README merely to record the session, create a generic TODO list, or leave completed items open. Mark the handoff and session `complete`; keep the index row and scratch folder until termination.
- Do not store full chat transcripts. Keep one rolling handoff per workstream, sufficient to resume in a later chat.

## Terminate

1. Do not terminate an `active` session. Close or complete it first. Verify the session state and matching handoff; for completed work, confirm durable project records are updated.
2. Before deleting anything, ask an explicit yes/no question naming each exact target and its effect.
3. For paused work, delete only its `sessions/work/<session-id>/` folder. Retain the handoff and index row, and clear the session-folder entry. A later chat creates a fresh dated folder from the handoff.
4. For completed work, delete only its scratch folder and obsolete handoff, then remove its index row. Preserve all project source files and other workstreams.

Follow [Local Change Approval Rules](../../standards/LOCAL-CHANGE-APPROVAL.md). Use the [session guide](../../how-to-use/05-work-sessions.md) and [handoff template](../../sessions/SESSION-TEMPLATE.md). Never commit, push, or publish as part of session management.
