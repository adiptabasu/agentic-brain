---
name: client-response
description: Draft a copy-ready response to a client using the active support issue record. Use when the user provides a client's question or needs to request specific diagnostic information.
---

# Client response

Use this conversational skill to prepare a client-facing draft and keep the related issue record current. Never send the message. Every response has two clearly separated sections so the user can copy the client text without including internal reasoning.

## Perspectives

- Use the Requirements Analyst viewpoint to identify what the client asked, what is known, and what information is still needed.
- Use the Technical Writer and Knowledge Curator viewpoint to make the client wording clear, focused, and easy to act on.

## Workflow

1. **Identify the issue context.** Read the active `issue-record.md` and the client's question. If the issue ID or record location is missing, ask for it or for the minimum facts needed to draft; do not invent an issue or assume access to a previous chat's files.
2. **Separate facts from gaps.** Use only confirmed issue facts. Identify unsupported claims, unresolved hypotheses, and the precise information needed to answer safely. If the record conflicts with the client's question or lacks material context, ask the user before drafting a definitive answer.
3. **Draft the client section first.** Output exactly this marked section first:

   `CLIENT MESSAGE — COPY/PASTE`

   Write the message in client-friendly plain text, ready to copy. Answer directly when the evidence supports an answer. When more information is needed, ask a focused set of questions with the specific data or steps requested (for example: time with timezone, request/correlation ID, affected endpoint or region, reproduction steps, or relevant redacted logs). Do not request secrets or credentials.
4. **Add internal logic separately.** Below the client message, output:

   `INTERNAL LOGIC — NOT FOR CLIENT`

   Briefly explain the confirmed facts used, assumptions or uncertainty, evidence gaps, and why requested details help. Keep this section clearly outside the copy-ready client message. Never put internal hypotheses, raw log excerpts, credentials, or private implementation notes in the client section.
5. **Update the issue record.** Record a concise summary of the client's question and the draft or information request. Do not store a full chat transcript. If the draft asks the client for information, set the local state to `awaiting-client`; do not mark the message as sent. Preserve existing facts, notes, and state when no transition is warranted. If the record cannot be safely updated, explain the blocker and provide the draft only if the known facts are sufficient.
6. **Pause or resume.** After providing the draft, wait for the user's direction or the client's reply. On a later reply, re-read the issue record, incorporate the new information as a concise note, and prepare the next draft. Continue until the user ends the response task or another support skill should take over.

## Boundaries

- Do not send email, chat, or other messages to clients.
- Do not state a hypothesis as the root cause or promise a resolution that the record does not support.
- Do not perform log analysis or close the issue; route those requests to `analyze-logs` or `agree-rca-close-issue`.
- Keep the client message and internal logic in separate, explicitly marked sections on every invocation.

## Completion

Complete an invocation when the two sections are present in the required order, the client draft is grounded and copy-ready, and the issue record reflects the concise interaction and correct local state. If material facts are missing, ask a focused question in the internal section or obtain the context needed to draft; never guess.
