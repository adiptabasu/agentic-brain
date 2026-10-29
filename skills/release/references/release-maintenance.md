# Release skill maintenance reference

Read only when reviewing or maintaining this skill, not when preparing a release.

## 10. Acceptance Criteria

The Release skill's output is acceptable when all applicable criteria below are satisfied.

### 10.1 Intent and scope

- The requested release outcome is clear.
- The relevant candidate is identified or the ambiguity is explicitly reported.
- Included and excluded scope is accurate.
- Material uncertainties are resolved or documented.

### 10.2 Readiness and evidence

- Applicable release criteria are identified.
- Required checks are supported by evidence.
- Missing evidence is not represented as a pass.
- Failures and exceptions are accurately recorded.
- Evidence corresponds to the intended candidate.
- Material risks and blockers are visible.

### 10.3 Version and artifacts

- The version follows the applicable project convention.
- Release notes and changelog claims are evidence-based.
- Artifact identity is recorded where relevant.
- Provenance and integrity claims are supported.
- Artifact substitution is controlled and documented.

### 10.4 Authorization

- Required approval authority is identified.
- Approval is distinguished from readiness.
- Execution remains within the approved scope.
- External side effects are authorized.
- Required gates are not bypassed.
- Silence is not interpreted as approval.

### 10.5 Execution and recovery

- The release plan has appropriate prerequisites and sequencing.
- External actions are executed only when authorized and supported.
- Failures are handled without unsupported success claims.
- Recovery plans reflect actual technical constraints.
- Destructive or irreversible actions receive appropriate safeguards.
- Partial execution and uncertain outcomes are handled explicitly.

### 10.6 Post-release verification

- Publication or deployment is verified through appropriate evidence.
- Post-release checks are performed where required.
- Remaining uncertainty is stated.
- Operational issues are escalated according to policy.
- Completion is claimed only when applicable criteria are satisfied.

### 10.7 Communication and portability

- The report is clear and proportional.
- Blockers have actionable next steps.
- The handoff contains sufficient context.
- No sensitive information is unnecessarily exposed.
- Platform-specific dependencies are explicit.
- Unsupported compatibility or capability claims are avoided.

### 10.8 Failure conditions

The output must be considered unacceptable if it:

- Claims approval without evidence.
- Publishes or deploys without the required authorization.
- Misrepresents failed or missing checks.
- Uses an unverified candidate as though it were approved.
- Silently changes release scope or target.
- Claims successful rollback without evidence.
- Hides material risks or known issues.
- Treats a successful command as proof of complete system health.
- Claims release completion while mandatory criteria remain unmet.
- Violates governing security, privacy, compliance, or organizational rules.

## 11. Portability

### 11.1 Platform-neutral workflow

The core release process must remain usable across different repositories, CI systems, registries, cloud platforms, and deployment environments.

Keep the general workflow independent of a particular vendor's commands.

Where an implementation requires platform-specific functionality, isolate those details in the relevant adapter or environment-specific instructions.

### 11.2 Capability discovery

Before using a tool or external system, determine whether the current environment actually provides the required capability.

Possible capabilities include:

- Reading repository state.
- Inspecting commits and tags.
- Running tests.
- Reading CI results.
- Building artifacts.
- Inspecting artifact digests.
- Accessing a package registry.
- Creating a release record.
- Publishing a package.
- Deploying to an environment.
- Reading health checks and metrics.
- Initiating an authorized recovery.

Do not infer capability from the agent's product name or general reputation.

If the capability is unavailable, provide a handoff or manual procedure.

### 11.3 Adapter boundaries

Environment-specific adapters may define:

- Commands.
- Authentication mechanisms.
- API operations.
- Registry interactions.
- Deployment procedures.
- Evidence retrieval.
- Platform-specific approval controls.
- Platform-specific rollback operations.

Adapters must not redefine shared authorization, evidence, or status semantics without an explicit and reviewed change to the common standard.

### 11.4 Avoid vendor lock-in

Do not make a specific vendor mandatory unless the user's environment or project policy requires it.

Use portable concepts such as source revision, build result, artifact identity, approval record, deployment target, and health check.

Map these concepts to the selected platform only when the mapping is supported.

### 11.5 Compatibility claims

Do not claim that the skill has been validated on GitHub Copilot, Cursor, Claude Code, Codex, Abacus, or any other environment unless actual validation evidence exists.

A compatible format or design intent is not proof of runtime compatibility.

When testing portability, record the environment, version, tested behavior, and observed limitations.

### 11.6 Degraded operation

When a platform lacks an expected feature:

- Identify the missing capability.
- Determine whether a safe alternative exists.
- Preserve required authorization and evidence.
- Explain any reduction in confidence.
- Do not silently downgrade mandatory controls.

If no compliant alternative exists, stop at the relevant gate.

### 11.7 Human-operated steps

Some environments require a human to perform publication, approval, or deployment.

Provide an explicit handoff that identifies the action, target, prerequisites, expected result, and evidence to return.

Do not imply that a human step has occurred until its outcome is confirmed.

## 12. Maintenance

### 12.1 Review triggers

Review this skill when:

- Shared Agentic Brain standards change.
- The handoff contract changes.
- The skill template changes.
- Authorization rules change.
- A supported runtime changes its capabilities.
- Release tooling changes materially.
- A significant release failure reveals a gap.
- New security or compliance requirements apply.
- The workflow becomes unnecessarily complex or redundant.

### 12.2 Change discipline

When modifying this skill:

1. Identify the behavior or ambiguity being addressed.
2. Review related shared standards.
3. Determine whether the change affects other skills.
4. Preserve established safety and authorization boundaries.
5. Update examples and acceptance criteria where needed.
6. Validate the Markdown structure and metadata.
7. Review the diff for unintended changes.
8. Record the rationale for material behavioral changes.

Do not silently change a shared contract through a local wording adjustment.

### 12.3 Evidence-based maintenance

Treat real release incidents and observed workflow failures as evidence for improvement.

Separate observed causes from suspected causes.

Do not generalize a single incident into a universal rule without considering its context.

Prefer targeted improvements that reduce ambiguity, improve safety, or strengthen evidence quality.

### 12.4 Avoid uncontrolled expansion

Add new requirements when they address a real gap, a governing policy, or a material risk.

Do not duplicate entire procedures from other skills when a clear handoff is sufficient.

Keep the skill comprehensive enough to guide release work while preserving a clear division of responsibilities.

### 12.5 Final maintenance principle

The Release skill exists to make release outcomes trustworthy, not merely to make release operations faster.

A successful release workflow must preserve the distinction between what was planned, what was approved, what was executed, what was verified, and what remains unknown.
