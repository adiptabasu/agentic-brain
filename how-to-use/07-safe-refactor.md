# Refactor code without changing behavior

Use this when you want to improve structure, readability, or maintainability without intentionally changing what the software does.

Open the correct repository and ask `refine`:

> Read `skills/refine/SKILL.md` and follow it. I want to improve [area or concern] while preserving the existing behavior and contracts. Inspect relevant code, public interfaces, tests, and current Git changes. First describe the current behavior and propose a focused refactor with the checks that can detect regressions. Do not edit files yet.

If there is a specific reason, such as duplication or difficult testing, explain it. Do not prescribe a rewrite when a smaller structural change could help.

Review the proposal. Clarify whether any interface, output, error behavior, or data format must remain stable. Then authorize the bounded change:

> I approve the focused refactor of [scope]. Preserve [specific contracts]. Change no product behavior. Use the existing tests and add only focused regression checks if needed. Stop if you find the change requires new behavior.

After implementation, use `verify`:

> Compare the result with the stated behavior and contracts. Run relevant tests and checks and report actual results. Identify what could not be verified; do not call the refactor behavior-preserving based only on visual similarity.

Use `review` if you want an independent look at the diff. A refactor should remain separate from feature work unless you explicitly agree to combine them.
