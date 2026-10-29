# Skill Template

Use this as a checklist, not a requirement to create every section. Keep the skill body as short as the workflow permits. Put detailed reference material in supporting files and instruct the agent to read a file only when its scenario applies. The host synchronizer copies these supporting files with SKILL.md.

## Required in every skill

### Metadata

Use Agent Skills YAML frontmatter with a directory-matching name and a short description that states the task and trigger. Avoid generic trigger phrases that cause unrelated activation.

### Purpose and boundaries

State the outcome, when to use the skill, and the most important adjacent workflows it does not own.

### Workflow

Give the smallest sequence of decisions and actions needed for the common case. Ask only when uncertainty materially changes scope, correctness, safety, or authorization. Do not turn every possible edge case into a mandatory step.

### Completion and reporting

Define the result the user should receive and require honest reporting of evidence, unknowns, limitations, and next steps.

### Safety and shared contracts

Follow standards/CORE-PRINCIPLES.md. Refer to standards/VERIFICATION.md when making outcome claims and standards/HANDOFF-CONTRACT.md when transferring work. Repeat only skill-specific rules; do not copy shared policies wholesale.

## Optional sections

Add a section only when it changes behavior in a meaningful scenario:

- Required or optional inputs and artifacts.
- Durable state or privacy requirements.
- High-impact decisions and authorization boundaries.
- Failure recovery for realistic, important failure modes.
- Specialized output structures.
- Examples that clarify an ambiguous trigger or boundary.
- Platform-specific adapters or portability limits.
- Maintenance and compatibility notes for skill maintainers.

Keep rare or lengthy cases in supporting reference files. The main SKILL.md should tell the agent which reference to consult and when; it should not ask the agent to load all references for every invocation.

## Review before publishing

- Is the description concise and accurately scoped?
- Does each instruction affect a decision or outcome?
- Are shared standards referenced instead of duplicated?
- Are references loaded only when relevant and copied by the repository’s host sync process?
- Are claims about tools, hosts, and verification evidence-supported?
- Are appropriate manual evaluations and repository indexes current?

Remove unused placeholders and irrelevant sections before publishing. Never claim an evaluation passed unless it was run and reviewed.
