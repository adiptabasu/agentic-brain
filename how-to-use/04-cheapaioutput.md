# Use cheapaioutput

`cheapaioutput` reduces filler and unnecessary words in chat replies while keeping meaning, technical accuracy, and required safeguards. It is a persistent mode that stays on until explicitly turned off.

Turn it on explicitly:

> Turn on `cheapaioutput` and keep it active until I turn it off.

Turn it off explicitly:

> Turn off `cheapaioutput` and return to normal output.

A one-off request such as “keep this answer brief” affects only that response. While the mode is active, it does not omit important facts, negatives, caveats, uncertainty, code, commands, approval prompts, or requested detail. It aims to reduce tokens but does not promise a specific saving.

For commit messages, use only the `write-document` skill to draft from the reviewed staged diff. Do not use `cheapaioutput` for commit messages.

Do not use `cheapaioutput` to write or shorten content saved in local files. Use the [write-document skill](../skills/write-document/SKILL.md) for local prose and documents, and the appropriate implementation skill for code or configuration. Keep those artifacts complete to the request even when chat mode is on.

The skill takes design inspiration from the [Caveman skill](https://github.com/JuliusBrussee/caveman/blob/main/skills/caveman/SKILL.md), especially its answer-first, filler-free style and preservation of technical details. This project uses its own wording and does not adopt a caveman voice.
