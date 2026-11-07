# Manage resumable work sessions

Use the [`session` skill](../skills/session/SKILL.md) for feature development, debugging, or other software work likely to span multiple chats.

## Start or resume

> Start or resume a session for `<workstream>`. Check `sessions/README.md` first. Resume an active session or an existing closed scratch folder. If a paused session's scratch was terminated, read only its handoff and create today's dated folder from it. Record the goal and next action.

Scratch lives under `sessions/work/<session-id>/`. The tracked handoff lives at `sessions/handoffs/<workstream>.md`; the index points to both while scratch exists.

## Pause

> Close this session as paused. Update its rolling handoff and the session index with decisions, progress, changed files, checks, blockers, and next action. Keep the scratch folder.

A later chat can resume that closed folder. When ready to discard scratch, call terminate. The agent must ask explicit yes/no approval naming the exact folder. Terminating paused work keeps the handoff and index row; after termination, a later chat creates a fresh dated folder from that handoff.

## Complete and terminate

> Mark this workstream complete. Update only relevant source-of-truth files, mark its handoff complete, then prepare the session for termination.

After verifying durable project records, terminate the completed session. The agent must identify the exact scratch folder, obsolete handoff, and index row and ask for explicit yes/no approval before deletion. Cleanup removes only those session artifacts; project source files and other workstreams remain.

Never terminate an active session. Do not change README merely to log a session, create a generic TODO file, retain full chat transcripts, or delete a paused workstream's handoff.
