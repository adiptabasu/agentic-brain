---
name: document
description: Create, update, and maintain accurate technical and operational documentation grounded in available evidence. Use for README files, setup guides, architecture descriptions, API references, runbooks, decision records, and documentation updates after implementation. Distinguish verified behavior from proposals and unknowns; do not invent implementation details or claim undocumented behavior is verified.
---

# Document — Evidence-Based Documentation

## 1. Purpose

Document creates and maintains useful, accurate, discoverable, and maintainable documentation for software, systems, workflows, and technical decisions.

Its central principle is:

**Document what is known, make uncertainty visible, and never let polished prose substitute for evidence.**

Documentation helps people and agents understand what a system does, why it exists, how to use it, how to operate it, and how to continue work without reconstructing all prior context.

Poor documentation can mislead as effectively as incorrect code. An outdated setup command, an invented API parameter, an unsupported architecture claim, or an undocumented operational risk can cause real failures.

Document therefore treats documentation as an evidence-based artifact rather than a place to fill gaps with plausible assumptions.

It must:

- Identify the intended audience and purpose.
- Establish the authoritative sources for documented claims.
- Distinguish confirmed behavior from proposals, assumptions, and unknowns.
- Prefer existing authoritative documentation over unnecessary duplication.
- Preserve meaningful decisions, constraints, and unresolved questions.
- Keep documentation proportionate to the system and its users.
- Verify the resulting documentation for accuracy, structure, and usability.
- State when the available evidence is insufficient to document a claim confidently.

Document does not guarantee that the underlying system is correct. It ensures that documentation accurately represents what the available evidence supports and makes material limitations visible.

## 2. Core Responsibilities

### 2.1 Understand the documentation need

Determine what the user or workflow needs the documentation to accomplish.

Examples include:

- Helping a new contributor install and run a project.
- Explaining a system's architecture and component responsibilities.
- Describing an API contract.
- Recording an approved technical decision.
- Providing a repeatable operational procedure.
- Explaining a feature to its intended users.
- Recording a change so future maintainers understand its impact.
- Creating handoff documentation for another person or agent.

Do not assume that every request requires a new standalone document. A targeted update to an existing README, API reference, or runbook may be more appropriate.

### 2.2 Identify the audience

Adapt the level of detail, terminology, and organization to the intended readers.

Possible audiences include:

- End users.
- Developers contributing to a codebase.
- System architects.
- Operators and support engineers.
- Security or compliance reviewers.
- Project stakeholders.
- Other AI agents continuing an existing workflow.

If the audience materially changes the content and cannot reasonably be inferred, ask a focused question.

When the audience is clear enough, proceed without unnecessary clarification.

### 2.3 Establish authoritative sources

Inspect the available sources relevant to the documentation request.

Depending on the task, these may include:

- Existing documentation.
- Source code and public interfaces.
- Configuration files.
- Build and dependency definitions.
- Tests and test fixtures.
- API schemas and specifications.
- Approved requirements and acceptance criteria.
- Architecture decision records.
- Migration scripts.
- Operational configuration and runbooks.
- Actual command output or runtime observations.
- Explicitly approved decisions and user-provided facts.

Evaluate each source according to its authority, relevance, and freshness.

Source code may establish an implementation detail, but it does not necessarily establish intended behavior. Tests may reveal observed behavior, but they may be incomplete or incorrect. Existing documentation may explain intent, but it may be stale.

When important sources disagree, preserve the conflict and resolve it where possible rather than silently selecting the most convenient version.

### 2.4 Produce useful documentation

Organize content around reader needs and practical tasks.

Use:

- Clear titles and section headings.
- A logical progression from context to action.
- Short, precise explanations.
- Concrete examples where they add value.
- Prerequisites before procedures.
- Expected outcomes after instructions.
- Warnings for material risks.
- Links to authoritative sources when available.
- Explicit limitations where relevant.

Avoid unnecessary verbosity, repeated explanations, unexplained jargon, and content that does not help the intended audience.

### 2.5 Maintain consistency

Keep terminology, naming, configuration descriptions, and cross-references consistent with authoritative sources.

When updating documentation, identify related pages or examples that may also become stale.

Do not automatically rewrite every related file. Make the changes needed to keep the documentation coherent and within the authorized scope.

### 2.6 Validate documentation

Check the resulting artifact for:

- Factual support.
- Completeness relative to the request.
- Clear and consistent terminology.
- Correct paths, links, commands, and references.
- Valid Markdown or the relevant document format.
- Correct code fences and formatting.
- Appropriate warnings and prerequisites.
- Internal consistency.
- Unresolved placeholders or unsupported claims.

Distinguish checks that were actually performed from checks that remain recommended.

### 2.7 Preserve maintainability

Documentation should remain useful as the system changes.

Prefer clear sources of truth, reusable references, and task-oriented instructions over duplicated content.

Where appropriate, recommend automated documentation checks, link validation, API schema generation, or documentation tests. Do not claim these checks exist unless their presence has been established.

## 3. When to Use Document

Use Document when creating, revising, reviewing for factual consistency, or organizing technical or operational documentation.

Typical situations include:

- Creating or improving a project README.
- Documenting installation, configuration, and local development.
- Explaining architecture, components, and data flows.
- Writing API usage instructions or reference material.
- Recording approved design decisions and their rationale.
- Documenting database schemas, migrations, or configuration options.
- Preparing deployment and troubleshooting runbooks.
- Updating documentation after implementation.
- Creating contributor guides and coding conventions.
- Preparing a handoff for a human or another agent.
- Identifying stale, contradictory, or unsupported documentation.
- Documenting limitations and known issues.

### 3.1 When not to use Document as the primary skill

Do not use Document as a substitute for:

- Discovering hidden assumptions: use Probe.
- Defining requirements and acceptance criteria: use Specify.
- Choosing system architecture: use Design.
- Sequencing implementation work: use Plan.
- Test-driven implementation: use Test-First.
- Diagnosing defects: use Debug.
- Making code or artifact changes beyond the documentation scope: use Implement.
- Independently assessing a code change: use Review.
- Establishing whether a claim is supported by evidence: use Verify.
- Navigating the overall workflow: use Guide.

These skills may provide authoritative inputs for documentation.

## 4. Shared Standards

### 4.1 Clarify, Don't Assume

Never silently transform an assumption, proposal, or unresolved question into a documented fact.

Distinguish among:

- **Confirmed:** Supported by an authoritative source or sufficient evidence.
- **Proposed:** Suggested but not approved or implemented.
- **Assumed:** Used provisionally, with its basis and impact stated.
- **Unknown:** Not established by the available evidence.
- **Blocked:** Cannot be established because of a specific dependency or limitation.
- **Verified:** Checked against the relevant source or behavior using adequate evidence.
- **Unverified:** Plausible or reported but not independently established.

Use only the labels necessary for the document. Do not burden ordinary prose with unnecessary status markers, but make material uncertainty explicit.

### 4.2 Evidence before claims

Claims about implementation, configuration, runtime behavior, supported versions, API contracts, and operational outcomes must be grounded in relevant evidence.

Do not invent:

- File paths.
- Configuration keys.
- Environment variables.
- API endpoints or request fields.
- Dependency versions.
- Commands or flags.
- Performance characteristics.
- Security guarantees.
- Deployment steps.
- Test results.
- Compatibility claims.
- Ownership or approval decisions.

If a detail cannot be confirmed, omit it, qualify it, or identify what is needed to establish it.

### 4.3 Preserve approval boundaries

Documenting a proposed decision does not approve it.

Do not represent an unapproved design, release, migration, policy, or operational procedure as authorized merely because it has been written down.

Keep proposals, decisions, and implementation status distinct.

### 4.4 Preserve context in handoffs

When documenting work for another person or agent, include enough context to continue safely.

Depending on the task, record:

- The goal and scope.
- Confirmed requirements.
- Relevant decisions and rationale.
- Current implementation state.
- Evidence already collected.
- Known limitations.
- Open questions and dependencies.
- Next steps and required approvals.

Do not force the recipient to reconstruct available context from scratch.

### 4.5 Avoid unsupported completion claims

Creating documentation does not establish that the documented procedure works.

For example, writing installation instructions does not prove that installation succeeds. Describing an API does not prove that the implementation matches the description.

State what was validated and what remains unverified.

### 4.6 Respect scope and confidentiality

Document only information appropriate for the intended audience and authorized destination.

Do not expose credentials, tokens, private keys, personal data, or sensitive operational details unnecessarily.

Do not broaden a documentation request into unauthorized implementation changes or external publication.

## 5. Operating Procedure

### Step 1: Establish the requested outcome

Identify the artifact, purpose, audience, and intended level of detail.

Determine whether the task is to:

- Create a new document.
- Update an existing document.
- Reorganize a documentation set.
- Reconcile contradictory information.
- Audit documentation for accuracy.
- Generate reference material from authoritative sources.
- Prepare a handoff or operational guide.

If the user explicitly specifies the file, format, or scope, follow that instruction unless a material conflict requires clarification.

### Step 2: Locate existing documentation

Inspect the available documentation before creating new content.

Look for:

- The project's main README.
- Existing guides and references.
- Relevant documentation directories.
- Templates and shared standards.
- Existing terminology and conventions.
- Links to authoritative specifications.
- Existing pages that already cover the requested topic.

Prefer updating the established source of truth when appropriate.

Avoid creating duplicate pages that may diverge over time. If duplication is necessary for audience or delivery reasons, establish clear links or ownership where practical.

Do not assume repository access or file availability unless the runtime establishes it.

### Step 3: Define scope and structure

Choose a structure that supports the intended reader's task.

For example:

**README**
- Project purpose.
- Main capabilities.
- Prerequisites.
- Installation and setup.
- Basic usage.
- Configuration.
- Testing.
- Contribution guidance.
- License information, when confirmed.

**Architecture document**
- System context.
- Component responsibilities.
- Interfaces and data flows.
- Key constraints.
- Important decisions and trade-offs.
- Failure modes and operational considerations.
- Open questions.

**API reference**
- Supported endpoints or operations.
- Authentication requirements, when established.
- Request and response schemas.
- Error behavior.
- Examples.
- Versioning and compatibility notes.

**Runbook**
- Purpose and scope.
- Prerequisites and permissions.
- Preconditions and safety checks.
- Step-by-step procedure.
- Expected observations.
- Failure handling and escalation.
- Rollback or recovery guidance, if authorized and established.

These are adaptable examples, not mandatory templates. Include only sections relevant to the actual request.

### Step 4: Build a source-of-truth map

For each material claim, identify its supporting source.

A lightweight working map may look like this:

| Documentation claim | Preferred evidence | Status |
|---|---|---|
| Project uses a specific runtime | Build files or authoritative setup documentation | Confirmed / Unknown |
| An endpoint accepts a field | API schema or implementation and tests | Confirmed / Unverified |
| A deployment step is supported | Approved operational procedure | Confirmed / Blocked |
| A design choice was approved | Explicit decision record or approval | Confirmed / Proposed |
| A command succeeds | Actual command result in the relevant environment | Verified / Unverified |

Adapt the table to the task. The purpose is traceability, not bureaucracy.

### Step 5: Resolve ambiguity before documenting material claims

Check whether the sources establish:

- Intended versus current behavior.
- Supported versus experimental functionality.
- Approved versus proposed design choices.
- Required versus optional configuration.
- Local development versus production procedures.
- Mandatory versus recommended steps.
- Known limitations versus untested behavior.

If a distinction materially changes the instructions, resolve it using authoritative evidence or ask a focused question.

When the uncertainty is nonessential, proceed with the supported content and clearly isolate the unresolved point.

### Step 6: Draft around reader tasks

Write for the reader's practical objective.

For task-oriented instructions:

1. State the goal.
2. List prerequisites.
3. Provide the steps in execution order.
4. Show relevant examples.
5. Describe the expected result.
6. Explain common failures and recovery paths when known.
7. Identify limitations and next steps.

For explanatory material, introduce context before detail, define specialized terms, and explain important relationships.

For decision records, distinguish the problem, considered options, approved decision, rationale, consequences, and unresolved questions.

Do not force every document into the same structure.

### Step 7: Handle examples carefully

Examples should be useful, realistic, and consistent with the documented contract.

Before including a command or code sample, establish that its syntax is supported by the relevant tool or source.

Before including sample output, distinguish illustrative output from output actually observed.

Label illustrative examples clearly when they could otherwise be mistaken for real results.

Use placeholders only when their purpose is explicit. For example, `<YOUR_API_TOKEN>` is a user-supplied placeholder convention, not a real credential. Never include invented credentials or values that resemble valid secrets.

Avoid copying sensitive production data into examples.

### Step 8: Preserve decision history

When documenting decisions, record the distinction between:

- The problem being addressed.
- Constraints and requirements.
- Options considered.
- The decision that was actually approved.
- The person or authority responsible, when known.
- The rationale and trade-offs.
- Consequences and follow-up actions.
- Conditions that could trigger reconsideration.

Do not infer approval from silence, participation, or the absence of objections.

If the decision is still pending, label it as a proposal or open decision.

### Step 9: Update related references selectively

After drafting, identify references that the change could invalidate.

Examples include:

- README instructions pointing to renamed files.
- Architecture diagrams describing changed components.
- API examples affected by contract changes.
- Setup instructions affected by dependency changes.
- Runbooks affected by altered operational procedures.
- Navigation links to moved documentation.

Update the relevant references within scope.

If a related update is outside the authorized scope, identify it as a follow-up rather than silently expanding the change.

### Step 10: Validate factual accuracy

Compare each material claim against its supporting source.

Check:

- Names, paths, commands, flags, and configuration keys.
- API parameters and response fields.
- Version numbers and compatibility statements.
- Requirements and approved decisions.
- Procedure ordering and prerequisites.
- Warnings and safety boundaries.
- Links and cross-references.
- Claims about tests, builds, deployment, or runtime behavior.

Where possible, verify procedural claims by executing safe checks in the relevant environment. If execution is unavailable or unauthorized, state that the procedure was not executed.

### Step 11: Validate structure and usability

Inspect the artifact for:

- Correct metadata and frontmatter when required.
- Valid Markdown or target format.
- Correct headings and hierarchy.
- Properly closed code fences.
- Readable tables and lists.
- Consistent terminology.
- Working links when link checking is available.
- Appropriate file names and locations.
- Accidental duplicate content.
- Unresolved placeholders.
- Trailing whitespace and unintended blank lines.

Use automated checks when available and proportionate. Do not claim that a link checker, Markdown parser, or other validator ran unless its execution and result are known.

### Step 12: Review completeness

Compare the document with the original request.

Ask:

- Can the intended audience understand the purpose?
- Are the required tasks or topics covered?
- Are prerequisites and constraints visible?
- Are instructions sufficiently specific to follow?
- Are expected outcomes clear?
- Are relevant risks and limitations disclosed?
- Are important unknowns identified?
- Are next steps clear where the task cannot be completed?
- Is the content free of unnecessary repetition?

Do not confuse a long document with a complete one.

### Step 13: Report the documentation outcome

Summarize:

- What was created or updated.
- Which files or sections changed, when known.
- Which authoritative sources informed the content.
- Which checks were actually performed.
- What remains unverified or unresolved.
- Any follow-up documentation work required.

Do not claim that files were changed, links were checked, commands were executed, or documentation was published unless the relevant action was actually confirmed.

## 6. Documentation Deliverable Structure

Choose the deliverable structure based on the artifact type and audience.

### 6.1 General document

A useful default structure is:

1. **Title** — Identifies the subject.
2. **Purpose** — Explains why the document exists.
3. **Scope** — Establishes what is and is not covered.
4. **Context** — Provides necessary background.
5. **Main content** — Explains the relevant concepts, instructions, or decisions.
6. **Constraints and limitations** — Makes important boundaries explicit.
7. **References** — Points to authoritative related material.
8. **Next steps** — Identifies actions that remain, when relevant.

Not every document needs all eight sections.

### 6.2 README

A README should quickly answer:

- What is this project?
- Who is it for?
- What does it do?
- What prerequisites are needed?
- How can someone get started?
- How is it used or configured?
- How can it be tested or developed?
- Where can readers find further information?
- What license applies, if one has been confirmed?

Prioritize the first successful user journey. Put detailed reference material in dedicated documents when that improves readability.

Do not invent a license, project maturity level, compatibility guarantee, or feature claim.

### 6.3 Architecture documentation

Describe the system at the level needed to understand its structure and important trade-offs.

Depending on the system, include:

- System boundaries.
- Components and responsibilities.
- Interfaces and dependencies.
- Data flows.
- Trust boundaries and security considerations.
- Failure modes.
- Scaling or performance constraints when supported by evidence.
- Approved decisions and rejected alternatives.
- Known limitations and unresolved design questions.

Distinguish actual architecture from intended or proposed architecture.

### 6.4 API documentation

Document only established interfaces.

Include relevant information such as:

- Operation or endpoint.
- Supported method and parameters.
- Request and response formats.
- Authentication and authorization behavior.
- Error responses.
- Validation rules.
- Examples.
- Versioning and deprecation information.

Prefer generated references or authoritative schemas where available.

If implementation and specification disagree, report the discrepancy. Do not silently document one as if the conflict does not exist.

### 6.5 Operational runbook

Operational documentation must be especially careful about risk.

Include:

- Intended purpose.
- Preconditions and required permissions.
- Environmental assumptions.
- Safe inspection steps.
- Execution steps.
- Expected observations.
- Failure handling.
- Escalation criteria.
- Recovery or rollback instructions when established.
- Explicit warnings about destructive or irreversible actions.

Do not invent rollback commands or recommend production changes without an adequate basis and appropriate authorization.

### 6.6 Decision record

A decision record should make it possible for a future reader to understand both the choice and its context.

Record:

- Decision title and date, when known.
- Status: proposed, accepted, rejected, superseded, or another clearly defined state.
- Context and constraints.
- Considered options.
- Decision and rationale.
- Consequences and trade-offs.
- Related decisions.
- Open questions or review triggers.

Use only statuses supported by the actual decision process.

### 6.7 Agent handoff document

When the goal is to continue work across agents or sessions, preserve operationally relevant context.

Include:

- Goal and current scope.
- Confirmed requirements.
- Decisions and rationale.
- Relevant artifacts and their locations.
- Work completed and evidence collected.
- Failures, limitations, and unresolved questions.
- Dependencies and blockers.
- Next recommended actions.
- Required permissions or approvals.

Separate observed state from proposed next steps. A handoff must not imply that a suggested action has already been performed.

## 7. Decision and Authorization Rules

### 7.1 Existing documentation versus a new document

Prefer the existing authoritative location when the request concerns an established topic.

Create a new document when it serves a distinct audience, purpose, lifecycle, or navigational need.

If multiple sources already cover the topic, identify the canonical source and use links rather than copying large amounts of content without a maintenance plan.

### 7.2 Incomplete information

When evidence is missing:

- Document the supported information.
- Mark material unknowns.
- Ask for clarification when a missing fact materially affects correctness.
- Avoid filling gaps with invented defaults.
- Identify the source or access needed to resolve the gap.

Do not block the entire document because one nonessential detail is unavailable.

### 7.3 Conflicting sources

When sources conflict:

1. Identify the conflicting claims.
2. Assess the authority and freshness of each source.
3. Inspect additional evidence where available.
4. Seek clarification or an explicit decision when needed.
5. Record the unresolved discrepancy if it cannot be settled.

Do not silently rewrite requirements or implementation to make the documentation internally consistent.

### 7.4 Proposed versus approved content

Use explicit status labels for material decisions.

A suggestion in a discussion, an agent recommendation, or a draft document does not establish approval.

If the approval status cannot be determined, state that it is unknown.

### 7.5 Documentation changes versus implementation changes

Keep documentation work separate from unrelated code changes.

If documentation reveals a probable implementation defect:

- Describe the discrepancy.
- Identify the supporting evidence.
- Recommend the appropriate implementation or debugging workflow.
- Avoid silently changing application behavior unless that work is explicitly within scope and authorized.

Likewise, do not change documented requirements merely to match an implementation that may be wrong.

### 7.6 Generated documentation

When documentation can be generated from schemas, source annotations, or other canonical data:

- Identify the authoritative input.
- Prefer repeatable generation over manual duplication where appropriate.
- Avoid editing generated output if the change belongs in its source.
- Confirm that the generation process is available before claiming the output is current.
- Record limitations of the generation method.

Do not assume generated content is accurate merely because it was generated automatically.

### 7.7 Publication and external effects

Writing a document locally is different from publishing it or communicating it externally.

Do not assume permission to publish, send, merge, or distribute documentation merely because the content is ready.

Follow the user's explicit instructions and the applicable authorization process.

### 7.8 Completion claims

A documentation task can be complete within its defined scope even if broader implementation behavior remains unverified.

However, clearly distinguish:

- Documentation written.
- Documentation structurally validated.
- Claims checked against sources.
- Procedures actually executed.
- Links actually checked.
- Changes committed or published.

Each statement must be supported by its own evidence.

## 8. Failure Handling

### 8.1 Missing files or source access

If a required file or source is unavailable:

1. Identify what is missing.
2. Search only the available, authorized sources.
3. Complete independent documentation work where possible.
4. Mark unsupported claims as unknown or omit them.
5. Request the specific source or access needed.

Do not fabricate file contents or pretend to have inspected unavailable artifacts.

### 8.2 Contradictory documentation

If two documents disagree:

1. Identify the conflicting statements and locations.
2. Determine whether one is explicitly designated as authoritative.
3. Compare them with implementation or approved decisions when available.
4. Update the appropriate source only when the correct interpretation is established.
5. Link related documents where useful.
6. Record unresolved conflicts as follow-up work.

Do not resolve contradictions based solely on which wording sounds more plausible.

### 8.3 Unsupported examples or commands

If an example cannot be validated:

- Look for an authoritative command reference, schema, or existing working example.
- Correct it if sufficient evidence is available.
- Label it as illustrative if it is not an actual observed result.
- Omit it when presenting it would likely mislead the reader.
- State the limitation if the example is essential to the requested documentation.

Never invent successful output to make a guide appear complete.

### 8.4 Broken links or missing references

When a link fails or its destination is unavailable:

- Confirm the intended destination if possible.
- Correct it only when the replacement is established.
- Remove or flag obsolete references when appropriate.
- Avoid replacing an unavailable internal reference with an unrelated public page.
- Report links that could not be checked.

A failed network request alone does not prove that a destination no longer exists.

### 8.5 Ambiguous audience or purpose

If different interpretations would produce substantially different documents, ask a focused question.

Otherwise, choose a reasonable, low-risk structure, make material scope boundaries clear, and proceed.

Do not turn every stylistic preference into a blocking question.

### 8.6 Scope expansion

If the documentation review uncovers additional work:

1. Separate required corrections from optional improvements.
2. Complete authorized, relevant corrections.
3. Record unrelated issues as recommendations.
4. Ask before making consequential or out-of-scope changes.
5. Keep the final summary clear about what was and was not changed.

### 8.7 Formatting or validation failure

If a document parser, linter, link checker, or other validator reports an issue:

- Inspect the actual failure.
- Determine whether it affects validity, readability, or factual correctness.
- Fix issues within scope.
- Rerun the relevant check when available.
- Report unresolved failures honestly.

If the validation tool is unavailable, do not claim validation succeeded.

### 8.8 Sensitive information discovered during documentation

If source material contains secrets or sensitive information:

- Avoid copying the sensitive value into documentation.
- Redact it from examples and excerpts.
- Prefer placeholders or references to an approved secret-management mechanism.
- Report material exposure through the appropriate channel.
- Do not publish the sensitive value as part of a documentation fix.

### 8.9 Interrupted work

If documentation work is interrupted:

- Preserve the last confirmed state.
- Identify completed and incomplete sections.
- Record unresolved source questions.
- Avoid reporting a draft as complete if material sections remain unfinished.
- Provide a concise handoff so work can resume safely.

## 9. Output Expectations

### 9.1 Be useful before being exhaustive

Prioritize the information that enables the intended reader to succeed.

A practical setup guide is often more useful than a lengthy overview with no runnable path. An architecture document should explain meaningful boundaries and trade-offs rather than merely enumerate files.

Add detail when it improves understanding, safety, reproducibility, or maintainability.

### 9.2 Use precise language

Prefer:

- "The configuration file defines `SERVICE_PORT`."
- "The README documents the local startup command."
- "The test suite covers the documented error case."
- "The procedure has not been executed in the target environment."
- "The design is proposed and has not been approved."
- "The runtime behavior remains unverified."

Avoid unsupported statements such as:

- "The service is production-ready."
- "This configuration is secure."
- "All supported environments work."
- "The deployment procedure is guaranteed to succeed."
- "The decision was approved" when approval is unknown.

### 9.3 Make instructions reproducible

When documenting a procedure, provide enough detail for the intended reader to follow it.

Include relevant prerequisites, command context, required inputs, expected results, and failure guidance.

Do not expose secrets or assume that one environment's paths and configuration apply everywhere.

### 9.4 Keep references maintainable

Prefer stable links and canonical sources.

Avoid unnecessary duplicated specifications, repeated command lists, or copied tables that must be updated independently.

When duplication is unavoidable, make the relationship between the documents clear.

### 9.5 Match detail to risk

A small explanatory note needs less procedural detail than a production migration guide.

Operational, security-sensitive, or destructive procedures require explicit prerequisites, authorization boundaries, expected observations, and failure handling.

Do not bury important warnings in optional notes or distant sections.

### 9.6 Respect the requested format

Use the requested output format and location when known.

If the format cannot represent a required element adequately, explain the limitation and offer an appropriate alternative rather than silently omitting critical information.

### 9.7 Report work honestly

In the completion summary, distinguish:

- What was authored or changed.
- What evidence was consulted.
- What validation was performed.
- What was not checked.
- What remains unresolved.

Do not claim that documentation is current merely because it was just edited.

## 10. Acceptance Criteria for the Document Skill

### 10.1 Purpose and audience

- Identifies the documentation goal and intended audience.
- Selects a structure appropriate to the artifact.
- Reuses authoritative documentation when practical.
- Avoids unnecessary duplication.

### 10.2 Factual accuracy

- Grounds material claims in available sources.
- Distinguishes implementation behavior from intended behavior.
- Separates approved decisions from proposals.
- Makes important unknowns and conflicts visible.
- Avoids invented commands, configuration, APIs, versions, and outcomes.

### 10.3 Usability

- Uses clear headings and consistent terminology.
- Provides actionable instructions where appropriate.
- Includes prerequisites and expected outcomes for procedures.
- Makes limitations and risks visible.
- Provides relevant references and next steps.

### 10.4 Maintainability

- Identifies canonical sources of truth.
- Updates relevant cross-references within scope.
- Avoids needless repetition.
- Recommends automation where it materially improves consistency.
- Distinguishes generated output from its authoritative source.

### 10.5 Validation

- Checks factual support and internal consistency.
- Validates structure and formatting when possible.
- Distinguishes performed checks from recommended checks.
- Does not claim successful validation without evidence.
- Reports unresolved issues.

### 10.6 Safety and authorization

- Avoids exposing secrets or sensitive data.
- Does not treat documentation as approval.
- Does not silently expand into consequential implementation or publication.
- Makes operational risks and authorization requirements explicit.

### 10.7 Portability

- Uses standard Markdown and plain-language documentation principles where appropriate.
- Avoids unnecessary dependence on a specific documentation platform.
- Allows project-specific conventions when they are established.
- Does not claim compatibility with untested systems or tools.

## 11. Portability

- Use plain Markdown and standard Agent Skills metadata unless the repository defines a different convention.
- Adapt to the available documentation format, tooling, and repository structure.
- Do not assume a particular language, framework, operating system, documentation generator, hosting provider, or CI platform.
- Do not assume access to source code, project files, external links, or connected systems unless the runtime establishes their availability.
- Use existing project conventions when supported by evidence.
- Keep environment-specific instructions separate from generic concepts when both are needed.
- Use explicit handoffs when source inspection, implementation, or external publication requires another capability.
- Treat compatibility with individual agent platforms as unverified until tested.

## 12. Maintenance

When updating Document:

1. Preserve alignment with the shared core principles and handoff contract.
2. Keep documentation claims grounded in authoritative sources.
3. Maintain a clear distinction between verified facts, intended behavior, proposals, and unknowns.
4. Prefer updating canonical sources over creating unnecessary duplicates.
5. Validate links, metadata, formatting, commands, and internal references when tools are available.
6. Test procedural instructions when safe, authorized, and relevant.
7. Reassess related documentation when interfaces, configuration, architecture, or operational procedures change.
8. Remove stale content and duplicated rules when their authoritative source already defines them.
9. Avoid including sensitive information in examples or operational instructions.
10. Record meaningful changes through the repository's normal Git workflow.
