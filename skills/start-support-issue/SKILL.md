---
name: start-support-issue
description: Start or resume a local support case folder and maintain its durable issue record. Use when the user invokes an issue ID to begin or continue an investigation.
---

# Start or resume a support issue

Use this conversational skill to create or resume a local support case that can continue across chats. Keep one concise `issue-record.md` per issue and preserve existing information.

## Perspectives

- Use the Requirements Analyst viewpoint to capture the reported symptom, impact, and unanswered questions without turning guesses into facts.
- Use the Site Reliability Engineer viewpoint to organize evidence, investigation state, actions, and next steps for a resumable diagnosis.

## Start and resume

1. **Collect required inputs.** Confirm the issue ID. Ask for the issues root path on every invocation, including when resuming. Do not reuse a previously supplied root unless the user supplies it again.
2. **Validate the issue ID and paths.** Treat the issue ID as one child-folder name. Reject absolute paths, separators, `.`/`..`, and traversal attempts; ask for the correct ID instead of rewriting it. Confirm the root is a directory or can be created at the user-supplied path, and ensure the issue folder remains within that root. Stop if a path is a file or a symlink would escape the root.
3. **Create or resume.** Use `<issues-root>/<issue-id>/issue-record.md`. For a new issue, create the folder and record with local state `open`. If the folder already exists, resume it without replacing the record or other files. If the record exists, read it and preserve its current state, facts, findings, and manual notes; add only relevant new details. If the folder exists without a record, create the record without altering other contents. If the existing record is malformed or contains a material conflict, stop and ask before changing it.
4. **Maintain the record.** Use stable headings for issue ID, state, summary/impact, observed facts, hypotheses, client questions and answers, log paths and evidence, findings, actions tried, and next steps. Leave unknown fields marked unknown or pending. Use only relevant, redacted excerpts and metadata; never save complete raw logs, credentials, secrets, or a full chat transcript. Record a client question or answer as a concise summary.
5. **Keep the local lifecycle accurate.** Use the agreed local states `open`, `investigating`, `awaiting-client`, `RCA-proposed`, `RCA-agreed`, and `closed`. Change state only when the corresponding event occurs; do not imply RCA agreement or closure without the required discussion and explicit user approval. This skill does not update an external tracker.

## Ongoing interaction

Keep the record current as the user supplies facts, evidence, client replies, actions, or decisions. Clearly label observations, hypotheses, and confirmed conclusions. When the investigation pauses, leave the current state and next steps in the record. On resume, ask for the root path again, review the record, summarize the current state briefly, and continue from its next step rather than starting over.

## Completion

Complete each invocation when the issue folder and record are created or safely resumed, the current state and next steps are recorded, and any missing information needed for progress has been asked for. Report the folder path and any blocker. Do not send messages, modify external trackers, or store unredacted logs or secrets.
