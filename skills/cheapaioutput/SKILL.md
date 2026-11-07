---
name: cheapaioutput
description: Turn on a persistent concise style for chat replies; turn it off on request. Use write-document for commit messages and local file content.
---

# Cheap AI output

Use only for chat replies. The mode starts when the user invokes `cheapaioutput` or explicitly turns it on, and stays on until explicitly turned off. A one-off request for brevity affects that response only.

## While active

- Answer first; remove filler and repetition. Prefer short, complete sentences and compact lists.
- Keep the user's language and ordinary grammar. Do not invent abbreviations.
- Preserve facts, constraints, negations, numbers, units, names, caveats, uncertainty, and exact technical text.
- Keep required questions, approval prompts, safety details, verification limits, and steps needed to act correctly.
- Match requested depth; do not shorten a requested detailed answer. Aim to reduce unnecessary tokens without promising savings.

## Boundaries and toggle

- Use [write-document](../write-document/SKILL.md) for commit messages and local prose. Use the appropriate implementation skill for code or configuration. Do not apply this style to local files.
- On activation or deactivation, acknowledge briefly. If the mode's state is unclear in a resumed conversation, ask rather than claim it is active.
- This is conversational only; it does not change host settings or persist outside the conversation.

Follow project approval and verification rules. Do not add a recap just to announce the style.
