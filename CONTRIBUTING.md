# Contributing to Agentic Brain

Thanks for helping improve Agentic Brain. This repository is in early development; please keep proposals focused and make behavior claims traceable to evidence.

## Propose a change

For a new skill or a substantial behavior change, first compare the proposal with the skill list in `README.md` and relevant directories under `skills/`. Explain the gap and why an existing skill should not be extended instead. Raise a focused issue or discussion before investing in a large change.

For skill work, read `AGENTS.md` and `standards/SKILL-TEMPLATE.md`. Keep canonical skill content in `skills/<name>/SKILL.md`, use a kebab-case directory name matching the frontmatter `name`, and describe when the skill should be used. Prefer a small, focused change over adding overlapping skills or duplicating shared rules.

## Prepare a change

- Preserve the repository's principles in `standards/CORE-PRINCIPLES.md` and verification expectations in `standards/VERIFICATION.md`.
- Update relevant manual evaluation cases under `evaluations/cases/` when changing one of the covered skills. For a new or high-impact skill, consider adding trigger examples and a behavioral scenario before treating it as validated.
- Run checks relevant to the change. At minimum, inspect the full diff and run `git diff --check`; report the commands actually run and their results. The evaluation cases are manual examples; this repository currently has no automated runner or CI enforcement.
- Do not include secrets, private logs, or unrelated formatting changes. Redact sensitive data in examples and reports.

## Open a pull request or issue

Explain the user problem, the affected skills or files, the intended behavior, and any alternatives considered. Include relevant evaluation prompts and observed results for skill behavior changes. State what you checked, what you could not check, and any known limitations. For a problem report, include a sanitized prompt, the expected and actual behavior, and the agent host or environment when relevant.

Do not post credentials, private logs, or exploitable security details in a public issue. Contact the repository maintainer privately for sensitive reports until a dedicated security reporting process is published.

## License for contributions

By submitting a contribution for inclusion in this repository, you agree that the contribution is provided under the repository's [MIT License](LICENSE). Submit only material you authored or are authorized to contribute.
