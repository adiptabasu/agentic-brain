# Write or update technical documentation

Use this when a code, configuration, API, or operational change needs accurate documentation, or when existing docs may no longer match the implementation.

Open the repo and identify the audience and target document. Then invoke `document`:

> Read `skills/document/SKILL.md` and follow it. Update [document/path or requested doc type] for [change or system]. The audience is [users / developers / operators]. Inspect the relevant source code, config, tests, and current docs first. Ground claims in those sources, distinguish implemented behavior from proposals or unknowns, and do not change code.

For a README, you can ask:

> Document how to [install / configure / run / troubleshoot] this project. Use commands and settings verified in the repository. Identify anything that cannot be confirmed instead of inventing it.

For a behavior change, provide the accepted requirements and implementation evidence. Ask the agent to flag conflicts between the docs and code rather than silently deciding which is correct.

## Review and validate

Review the result for intended audience, completeness, commands, links, and any unsupported claims. Ask:

> Show which sources support the important instructions. Check internal links and commands where possible. Tell me exactly what you validated, what you did not run, and which details remain unknown.

Writing instructions does not prove that they work; run setup or operational commands only when safe and authorized. Do not publish documentation externally unless that action is separately requested.
