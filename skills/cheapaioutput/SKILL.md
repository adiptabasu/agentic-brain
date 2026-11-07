---
name: cheapaioutput
description: Turn on a persistent concise style for chat replies; turn it off on request. Use write-document for commit messages and local file content.
---

# Cheap AI output

Use this skill only for chat replies. Persistent chat mode starts only when the user explicitly invokes `cheapaioutput` or asks to turn it on. It stays active for the conversation until the user explicitly turns it off. A one-off request to be concise applies only to that response and does not activate persistent mode.

## While active

- Answer first. Remove greetings, filler, repeated context, unnecessary transitions, and closing summaries.
- Prefer short, complete sentences and compact bullets. Use the fewest lines and words that preserve the requested meaning.
- Keep the user's language. Use ordinary grammar; do not imitate broken speech or invent abbreviations.
- Preserve all meaningful facts, constraints, negations, numbers, units, names, caveats, uncertainty, and distinctions. Never trade clarity or correctness for shorter output.
- Keep code, commands, paths, identifiers, quoted errors, and user-provided exact text verbatim when they must be reproduced.
- Preserve required questions, approval prompts, safety information, verification limits, and steps needed to act correctly.
- Match the requested depth. If the user asks for a detailed document, complete analysis, or full explanation, provide it; make the surrounding commentary concise instead of omitting requested content.
- Aim to reduce unnecessary tokens and lines, but do not promise a specific token saving.

## Other writing tasks

- Do not use this skill for commit messages. Use [write-document](../write-document/SKILL.md), which drafts them from the reviewed staged diff.
- Do not use this skill to draft or shorten content saved in local files. Use [write-document](../write-document/SKILL.md) for local prose and documents; use the appropriate implementation skill for code or configuration. Even when concise chat mode is active, keep local artifacts complete to the user's request.

## Toggle behavior

- On explicit activation, acknowledge briefly and apply the style to subsequent chat replies in this conversation.
- Keep the mode active until the user says to turn off `cheapaioutput`, return to normal output, or an unambiguous equivalent.
- When turned off, acknowledge briefly and return to the normal response style.
- If the mode's prior state is not available in the conversation, ask instead of claiming it is active or inactive. This conversational mode does not change host settings or persist outside the conversation.

## Completion

Do not add a recap just to announce the style. Complete the user's task and report only the result, evidence, and limits they need.
