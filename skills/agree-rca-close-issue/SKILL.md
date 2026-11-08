---
name: agree-rca-close-issue
description: Discuss and document a support RCA, then close the local issue only after the user explicitly approves it. Use for RCA review, agreement, and closeout files.
---

# Agree RCA and close issue

Use this iterative skill to discuss an evidence-based root cause analysis (RCA) with the user and prepare local issue closure. Agreement must be explicit in chat before the issue can be closed.

## Perspectives

- Use the Site Reliability Engineer viewpoint to distinguish causal evidence from correlation and identify remaining uncertainty.
- Use the Code Reviewer and Test Strategist viewpoint to check each material claim against evidence and preserve traceability.
- Use the Technical Writer and Knowledge Curator viewpoint to produce clear client, technical, and handoff-ready text for distinct audiences.

## Workflow

1. **Load the issue context.** Read the active `issue-record.md`. If its path or issue ID is missing, ask for them rather than assuming a location. Confirm the local state and identify the proposed RCA, impact, timeline, resolution, preventive actions, and evidence references.
2. **Review the RCA with the user.** Separate observed facts, hypotheses, root cause, contributing factors, and unknowns. Check each material causal claim against the recorded evidence IDs and source details. If evidence is insufficient or conflicts, explain the gap and revise or leave the RCA proposed; do not present a guess as fact.
3. **Seek explicit approval.** Present the complete proposed RCA and ask whether the user approves it for closure. Treat uncertainty, “looks plausible,” requests for review, or silence as no approval. Keep state `RCA-proposed` and create no closeout files until the user clearly approves the specific RCA and authorizes closure in chat.
4. **Record agreement.** After explicit approval, record the approved RCA, evidence IDs, approval, and any remaining uncertainty in `issue-record.md`, and transition locally through `RCA-agreed`. Do not update an external tracker or send messages.
5. **Prepare three plain-text files in the issue folder.** Create or update exactly these closeout files:
   - `client-email.txt` — a client-friendly summary of the issue, impact, resolution, and next steps. Exclude internal-only analysis and raw evidence.
   - `technical-rca.txt` — impact, timeline, root cause, contributing factors, resolution, preventive actions, and evidence IDs for material claims.
   - `technical-rca-evidence.txt` — one entry per evidence ID with the source log filename, line number(s), timestamp(s), and a short relevant snippet. Do not paste complete logs or secrets.

   Use plain text with readable headings and paragraphs; do not use Markdown code fences or create alternate timestamped filenames. Verify all three files exist and match the agreed RCA before changing state to `closed`. If file creation or verification fails, leave the issue not closed and report what remains.
6. **Handle reopening and revisions.** If a closed issue is explicitly reopened, update its local state to `investigating` while evidence is reviewed and `RCA-proposed` when a revision is ready. Discuss the revised RCA and obtain explicit approval for that revision before changing the closeout documents. Update the same three filenames in place and add a revision note to `issue-record.md`; do not create timestamped copies. Keep the issue open until the revised artifacts are checked.

## Interaction lifecycle

The skill remains in `RCA-proposed` while the user reviews or requests changes. Pause with the current proposal and evidence in the issue record when the user needs time or more information. Resume by rereading the record and continuing the discussion. The closure lifecycle ends only after explicit approval, verified local files, and the `closed` state, or after a safe stop with the specific evidence gap reported.

## Boundaries

- Never infer approval or close an issue based on ambiguous agreement.
- Never send the client email or update an external tracker.
- Do not invent evidence, timestamps, snippets, impact, or remediation claims.
- Keep client-facing content free of internal-only analysis and raw evidence.
- Store only relevant redacted evidence in the issue record and closeout files.

## Completion

Complete closure only when the user explicitly approves the specific RCA, `issue-record.md` records the decision, and all three verified `.txt` files are current and consistent with it. If approval or evidence is missing, keep the issue unclosed and state what is needed next.
