# Verify skill maintenance reference

Read only when reviewing or maintaining this skill, not during ordinary outcome verification.

## 10. Acceptance Criteria for the Verify Skill

The Verify skill is itself suitable for use only when it satisfies the following checks.

### 10.1 Scope and role

- Clearly distinguishes verification from review, implementation, debugging, and approval.
- Defines an observable verification target.
- Requires conclusions to be tied to relevant evidence.
- Supports both direct execution and explicit handoffs.

### 10.2 Status accuracy

- Defines Verified, Failed, Blocked, Inconclusive, and Not checked.
- Prevents an attempted action from being treated as a confirmed outcome.
- Requires material failures and uncertainty to remain visible.
- Prevents a narrow passing check from supporting an unjustifiably broad claim.

### 10.3 Safety and authorization

- Addresses destructive and externally consequential checks.
- Does not treat verification permission as permission to remediate.
- Requires appropriate authorization for consequential actions.
- Provides a safe response to unexpected side effects.

### 10.4 Evidence quality

- Addresses relevance, provenance, freshness, scope, and contradictory results.
- Distinguishes actual execution from recommended checks.
- Accounts for flaky tests, timeouts, and unavailable environments.
- Requires explicit limitations in the final report.

### 10.5 Portability

- Uses generic concepts that apply across languages, frameworks, tools, and platforms.
- Does not require a particular test runner or hosting service.
- Allows environment-specific commands and evidence formats.
- Avoids unsupported claims about platform compatibility.

### 10.6 Deliverables

- Provides a reusable verification matrix.
- Defines a clear reporting structure.
- Includes actionable failure-handling procedures.
- Supports concise reports for simple tasks and detailed reports for consequential ones.

## 11. Portability

- Use plain Markdown and standard Agent Skills metadata.
- Avoid dependence on a specific model provider or proprietary orchestration API.
- Do not assume a particular language, framework, editor, operating system, test runner, repository host, CI platform, or deployment service.
- Do not assume that files, logs, command output, external systems, or connected tools are accessible unless the runtime establishes their availability.
- Adapt verification methods to the actual environment.
- Use explicit handoffs when direct skill invocation is unsupported.
- Treat compatibility with individual agent platforms as unverified until tested.
- Keep environment-specific adapters separate from the canonical skill definition when required by the repository architecture.

## 12. Maintenance

When updating Verify:

1. Preserve alignment with the shared core principles and handoff contract.
2. Keep evidence evaluation distinct from implementation, debugging, independent review, and authorization.
3. Maintain consistent definitions for verification statuses.
4. Remove duplicated rules when a shared standard already defines them.
5. Validate metadata, Markdown structure, whitespace, and internal references after edits.
6. Test representative scenarios, including success, failure, blocked checks, contradictory evidence, and interrupted execution.
7. Confirm that examples do not imply unavailable tools or unsupported results.
8. Record meaningful changes through the repository's normal Git workflow.
