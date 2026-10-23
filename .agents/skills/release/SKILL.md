---
name: release
description: Prepare, assess, coordinate, and document software releases using explicit readiness criteria, evidence-based status, controlled authorization, artifact provenance, rollback planning, and post-release verification. Use when preparing a release candidate, evaluating release readiness, producing release notes, coordinating publication or deployment, or assessing release outcomes.
---

# Release Skill

## 1. Purpose

The Release skill coordinates the transition from a verified change or release candidate to a prepared, approved, published, and operationally assessed release.

Its purpose is to make release decisions deliberate, traceable, evidence-based, and appropriately authorized.

The skill helps an agent determine:

- What is intended to be released.
- Which version or release identifier applies.
- What changes are included and excluded.
- Whether the candidate satisfies the applicable release criteria.
- Which tests, reviews, builds, and verification activities have actually completed.
- Which blockers, risks, known limitations, and unresolved decisions remain.
- Whether required approvals have been obtained from the appropriate authority.
- Whether publication or deployment is permitted.
- Which artifacts and release records must be produced.
- How to assess the outcome and recover from a failed release.

The skill must never treat a successful build, a green test suite, a prepared changelog, or a completed release checklist as automatic authorization to publish or deploy.

A release may be technically ready but not approved. It may be approved but not yet published. It may be published but not yet verified. It may be deployed but experiencing operational problems.

These states must remain distinct.

### 1.1 Governing principle

**Clarify, Don't Assume.**

When release intent, scope, environment, versioning rules, approval authority, risk tolerance, or publication requirements are unclear, determine whether the uncertainty materially affects correctness, safety, authorization, or release integrity.

Ask a focused question when clarification is necessary.

Do not invent release policies, silently choose a production target, assume an approval has been granted, or report a release as complete without evidence.

### 1.2 Scope

This skill covers release preparation, readiness assessment, release coordination, release records, authorized release execution where supported, and post-release verification.

It may coordinate with other skills:

- `guide` for workflow navigation.
- `probe` for discovering assumptions and uncertainties.
- `specify` for requirements and acceptance criteria.
- `design` for architecture and technical decisions.
- `plan` for execution sequencing and dependencies.
- `test-first` for test-driven development practices.
- `implement` for implementing approved changes.
- `debug` for diagnosing release-blocking failures.
- `review` for independent change review.
- `verify` for evidence-based verification.
- `document` for documentation preparation.

These are coordination relationships. They do not imply that another skill can necessarily be invoked directly in the current environment.

If a required capability is unavailable, explain the limitation and provide a clear handoff.

### 1.3 Non-goals

This skill does not independently:

- Invent product requirements or release scope.
- Override security, compliance, or organizational policies.
- Grant deployment permissions.
- Approve its own high-risk actions.
- Bypass required human review or sign-off.
- Guarantee that a release is safe because checks passed.
- Guarantee rollback will succeed without a validated recovery mechanism.
- Fabricate version numbers, release dates, test results, artifact hashes, approvals, or deployment records.
- Claim to have published, deployed, signed, tagged, or verified an artifact without evidence.
- Treat a draft release note as proof of release completion.
- Replace incident management, change management, security review, or operational ownership where those processes are required.

## 2. Core Responsibilities

### 2.1 Establish release intent

Determine the requested outcome before making release decisions.

Identify, when applicable:

- Product, repository, service, package, or application.
- Requested release version or release identifier.
- Source branch, commit, or candidate.
- Intended release type.
- Target environment or distribution channel.
- Included changes and exclusions.
- Intended audience.
- Required release window.
- Required approvals.
- Required validation and evidence.
- Publication or deployment expectations.
- Rollback or recovery expectations.

Do not require every field for every release. Determine which details are material to the current task.

A request to draft release notes may not require deployment credentials or a production window. A request to deploy to production requires substantially more precise authorization and context.

### 2.2 Establish release identity

Maintain a clear relationship between the release and the source material from which it was produced.

Where supported, record:

- Release name and version.
- Repository or project identifier.
- Source commit.
- Source branch, when relevant.
- Build identifier.
- Artifact name and location.
- Artifact checksum or digest.
- Build environment or toolchain details, where required.
- Dependency or provenance records, where available.
- Release timestamp and responsible actor, when verified.

Use the project's established conventions.

Do not invent a commit hash, build identifier, checksum, signature, or provenance record.

If a required identity field cannot be verified, mark it as unknown or unavailable and determine whether that prevents release approval.

### 2.3 Evaluate readiness

Compare the candidate against explicit release criteria.

Assess relevant areas such as:

- Scope completeness.
- Acceptance criteria.
- Required tests.
- Independent review.
- Security and dependency checks.
- Build reproducibility or integrity requirements.
- Artifact availability.
- Documentation.
- Versioning and changelog accuracy.
- Migration compatibility.
- Configuration and secrets handling.
- Operational readiness.
- Monitoring and alerting.
- Rollback or recovery readiness.
- Required approvals.
- Known issues and residual risks.

Do not treat a generic checklist as a substitute for project-specific requirements.

### 2.4 Coordinate controlled execution

When authorized and technically supported, coordinate the release process according to the approved plan.

Respect the distinction between:

1. Preparing.
2. Assessing readiness.
3. Obtaining approval.
4. Publishing or deploying.
5. Verifying the outcome.
6. Closing the release record.

Do not proceed from one state to another merely because the preceding state appears successful.

### 2.5 Maintain an auditable release record

Record material decisions, evidence, blockers, approvals, and execution outcomes.

The release record should make it possible for another person to understand:

- What was intended.
- What was actually included.
- What evidence was reviewed.
- Which decisions were made and by whom.
- Which actions were authorized.
- What actions actually occurred.
- What remains unverified.
- What happened after publication or deployment.

Avoid recording unnecessary secrets or sensitive data.

### 2.6 Report accurately

Use precise status language.

Distinguish among:

- Prepared.
- Readiness assessed.
- Ready for approval.
- Approved.
- Publication authorized.
- Published.
- Deployment initiated.
- Deployed.
- Post-release checks passed.
- Release complete.
- Failed.
- Rolled back.
- Partially recovered.

Use only statuses supported by available evidence.

## 3. When to Use This Skill

Use this skill when the user asks to:

- Prepare a software release.
- Assess whether a candidate is ready to ship.
- Establish or review release criteria.
- Prepare release notes or a changelog.
- Coordinate versioning and release metadata.
- Validate release artifacts and their provenance.
- Organize release approvals.
- Publish a package, create a release, or deploy an application.
- Prepare a rollback or recovery plan.
- Verify a release after publication or deployment.
- Investigate a failed release process.
- Create or improve a repeatable release procedure.

### 3.1 Do not use as the primary skill when

- The primary task is discovering the user's goal or selecting a workflow: use `guide`.
- The main problem is ambiguity or hidden assumptions: use `probe`.
- The primary work is defining requirements: use `specify`.
- The primary work is selecting architecture: use `design`.
- The task is sequencing implementation work before release preparation: use `plan`.
- The task is implementing the underlying feature: use `implement`.
- The task is diagnosing a technical failure: use `debug`.
- The task is independent assessment of code quality: use `review`.
- The task is collecting verification evidence without coordinating a release: use `verify`.
- The task is creating general documentation unrelated to a release: use `document`.

A release workflow may still need these skills. Select the primary skill based on the user's immediate goal and coordinate supporting work as needed.

### 3.2 Classify the requested action

Before proceeding, distinguish among the following requests:

**Informational request**

The user wants an explanation of release readiness, versioning, or release practices.

Respond with guidance. Do not modify external state.

**Preparation request**

The user wants a release checklist, release notes, a candidate assessment, or a rollback plan.

Prepare the requested materials and identify missing evidence. Do not publish or deploy unless separately authorized.

**Readiness assessment**

The user wants to know whether a candidate is ready.

Inspect the applicable criteria and available evidence. Return a status with blockers, risks, and limitations.

**Execution request**

The user wants an external action, such as creating a release, publishing a package, or deploying to an environment.

Confirm the target, scope, authorization, prerequisites, and permitted action boundaries before executing.

**Recovery request**

The user reports a failed or problematic release.

Prioritize impact assessment, preservation of evidence, containment, and authorized recovery. Do not blindly repeat the failed action.

## 4. Shared Standards

### 4.1 Clarify, Don't Assume

Never silently transform an assumption into an established release requirement.

Examples of material uncertainties include:

- Whether the target is staging or production.
- Whether the user wants a draft or an actual publication.
- Whether a version is fixed or may be proposed.
- Whether an approval is mandatory.
- Whether a release window is strict.
- Whether a database migration is backward-compatible.
- Whether the current artifact is the approved candidate.
- Whether rollback is supported.
- Whether a known issue is acceptable for this release.

When a decision materially changes risk, scope, authorization, or correctness, ask a focused question.

When an uncertainty is nonessential, document it and continue with safe, reversible preparation where possible.

### 4.2 Evidence before claims

A release claim must be supported by appropriate evidence.

Examples:

- A command exit code can support a claim that a particular command completed successfully.
- A package registry record can support a claim that a package is available at a particular version.
- A deployment system's confirmed result can support a claim that deployment completed.
- A health check can support a claim about the specific health check that ran.
- A release page can support a claim that a release record exists.
- A test report can support a claim about the tests represented in that report.

None of these automatically proves every other release property.

Do not infer production health from a successful package upload. Do not infer test success from the presence of a test configuration. Do not infer a deployment occurred from a prepared deployment command.

### 4.3 Preserve status distinctions

Keep separate records for:

- Planned actions.
- Proposed actions.
- Authorized actions.
- Attempted actions.
- Confirmed outcomes.
- Unverified outcomes.

A planned deployment is not an attempted deployment. An attempted deployment is not necessarily successful. A successful deployment command does not necessarily establish application health.

### 4.4 Preserve provenance

Do not silently substitute a different commit, artifact, environment, or version after approval.

If the candidate changes materially after review or approval, determine whether revalidation or renewed approval is required.

The release must identify what was actually published or deployed, not merely what was originally intended.

### 4.5 Respect least privilege

Use only the access and capabilities required for the authorized release action.

Do not expose credentials, copy secrets into release notes, weaken security checks to obtain a green result, or bypass access controls.

If required access is missing, report the blocker. Do not invent a workaround that violates policy.

### 4.6 Preserve user control

Preparing a release does not grant permission to publish it.

A general request to prepare a release must not be interpreted as permission to deploy to production.

Follow any established authorization policy and explicit user instructions. Where policy requires an approval gate, stop at that gate until the required authorization is confirmed.

### 4.7 Portability

Use the project's existing release tooling where available.

Do not assume a particular CI provider, package registry, hosting platform, container runtime, cloud provider, source-control host, or deployment system.

When a platform-specific command is necessary, identify the platform dependency and keep the general release procedure separate from its implementation details.

### 4.8 Shared handoff contract

When another skill or human must continue the workflow, communicate:

- Objective.
- Current release candidate.
- Relevant source revision.
- Confirmed facts.
- Assumptions and unknowns.
- Readiness status.
- Completed actions and their evidence.
- Outstanding blockers and risks.
- Required decision or approval.
- Next safe action.
- Actions that must not occur without authorization.

Do not imply that another skill or agent has performed work unless there is evidence that it did.

## 5. Operating Procedure

Follow these phases in order where applicable. Adapt the depth to the risk and scope of the release.

Do not force a heavyweight release ceremony onto a low-risk documentation-only change. Do not simplify a high-impact production release merely because the user wants speed.

### Phase 1: Establish the objective

Determine what the user means by releasing.

Clarify the expected deliverable:

- Release plan.
- Readiness report.
- Release notes.
- Version and changelog update.
- Release artifact.
- Published release.
- Deployment.
- Post-release report.
- Recovery plan.

Identify the relevant project and source of truth.

If the request could mean either preparing materials or performing an external action, resolve that distinction before the external action.

### Phase 2: Identify the candidate

Determine which code, configuration, package, or content is intended for release.

Inspect available evidence such as:

- Repository state.
- Branch and commit.
- Changes included since the previous release.
- Existing tags or version metadata.
- Build records.
- Artifact metadata.
- Existing release records.
- Relevant approvals.
- Applicable release documentation.

Do not assume the current working directory, branch, or most recent commit represents the approved candidate.

If multiple candidates exist, identify the ambiguity and ask which one is intended when the difference matters.

### Phase 3: Establish release policy

Discover the rules that apply to this release.

Check available sources for:

- Versioning policy.
- Branch protection and merge requirements.
- Required reviewers.
- CI/CD requirements.
- Security or compliance requirements.
- Release windows.
- Change-management approval.
- Artifact-signing requirements.
- Publication permissions.
- Deployment restrictions.
- Rollback expectations.
- Required post-release monitoring.

Use the project's documented policy or the relevant authoritative owner.

Do not invent a policy when none is available. Propose a policy separately from describing existing policy.

If the absence of a policy materially affects a high-risk decision, identify the gap and request the required decision.

### Phase 4: Define scope

Create a clear statement of what the release includes.

Where relevant, identify:

- Features.
- Bug fixes.
- Security fixes.
- Dependency changes.
- Configuration changes.
- Database migrations.
- Infrastructure changes.
- Documentation changes.
- Breaking changes.
- Deprecations.
- Excluded changes.
- Known issues.

Compare the intended scope against the candidate's actual changes.

Do not assume that every merged change belongs in the release. Do not assume that a change mentioned in release notes exists in the candidate.

When scope is uncertain, separate confirmed inclusions from proposed inclusions.

### Phase 5: Determine version and release type

Use the project's established versioning convention.

Possible conventions include semantic versioning, date-based versions, calendar versioning, application build numbers, or ecosystem-specific package versions.

Do not impose one convention universally.

If semantic versioning is used, assess whether the changes indicate:

- A patch release.
- A minor release.
- A major release.

Treat the assessment as a proposal until the applicable project policy and compatibility implications are established.

Consider:

- Public API changes.
- Breaking behavior.
- Deprecations.
- Dependency compatibility.
- Data-format changes.
- Migration requirements.
- Prerelease identifiers.
- Supported-version policy.

If the versioning convention is unknown, ask whether an existing convention can be identified before inventing a version.

### Phase 6: Build a readiness matrix

Compare each applicable requirement against available evidence.

Use statuses such as:

- **PASS:** Required evidence supports completion.
- **FAIL:** Evidence demonstrates that a requirement is not satisfied.
- **BLOCKED:** A prerequisite or required decision prevents completion.
- **UNKNOWN:** Evidence is insufficient.
- **NOT APPLICABLE:** The requirement does not apply, with a rationale where necessary.

A missing test report is not proof that tests failed. It is also not proof that tests passed.

Do not mark a requirement as passed because no failure has been reported.

Assess at least the following areas where relevant:

1. Release scope.
2. Acceptance criteria.
3. Test execution.
4. Independent review.
5. Security checks.
6. Dependency and license checks.
7. Build success.
8. Artifact integrity.
9. Version and changelog accuracy.
10. Documentation readiness.
11. Configuration and secrets handling.
12. Database or data migration readiness.
13. Compatibility.
14. Deployment prerequisites.
15. Monitoring and alerting.
16. Rollback or recovery.
17. Approval requirements.
18. Publication permissions.
19. Operational ownership.
20. Post-release verification.

Tailor the matrix to the actual release.

### Phase 7: Verify quality evidence

Review evidence from the appropriate verification process.

Determine:

- Which checks were required.
- Which checks actually ran.
- Which candidate they tested.
- Whether the results are current.
- Whether any checks were skipped.
- Whether failures were resolved.
- Whether exceptions were approved.
- Whether the evidence is trustworthy and relevant.

Prefer direct, reproducible evidence over informal statements.

A green result for an earlier commit does not establish that the current candidate passed the same checks.

A successful local test run does not automatically establish that the CI pipeline or production environment is healthy.

Where verification belongs to another workflow, request the required evidence through a handoff rather than fabricating or duplicating it.

### Phase 8: Validate artifact provenance

Determine how the release artifact relates to the reviewed source.

Where relevant, confirm:

- Source revision.
- Build identity.
- Artifact identity.
- Artifact checksum or digest.
- Signing or attestation status.
- Dependency provenance.
- Build environment.
- Registry or distribution destination.
- Whether the artifact is the same artifact that was verified.

Do not claim that an artifact is signed, reproducible, or provenance-verified unless the corresponding evidence is available.

If a new build is created after verification, determine whether the new artifact needs additional validation.

### Phase 9: Prepare changelog and release notes

Collect change information from reliable project records.

Potential sources include:

- Merged pull requests.
- Commit history.
- Issue references.
- Approved change records.
- Feature documentation.
- Deprecation notices.
- Migration documentation.
- Verified security advisories.

Do not derive user-facing promises from commit messages alone when their meaning is ambiguous.

Organize notes according to the project's convention. Useful categories include:

- Added.
- Changed.
- Fixed.
- Deprecated.
- Removed.
- Security.
- Known issues.
- Upgrade instructions.

Include only changes supported by evidence.

For each material change, determine whether readers need:

- User impact.
- Compatibility implications.
- Configuration changes.
- Migration instructions.
- Required actions.
- Workarounds.
- Known limitations.

Do not expose sensitive vulnerability details in a public release note if disclosure is restricted by the relevant security process.

If release notes cannot be finalized because the change scope is unclear, identify the unresolved items instead of guessing.

### Phase 10: Assess operational readiness

For releases that affect a running system, evaluate operational concerns.

Consider:

- Target environment.
- Deployment strategy.
- Capacity and dependencies.
- Configuration readiness.
- Secrets and credential handling.
- Database migrations.
- Backward compatibility.
- Health checks.
- Metrics and alerts.
- Logs and diagnostics.
- Support ownership.
- Expected user impact.
- Maintenance window.
- Communication plan.
- Rollback feasibility.

Determine whether the release can be deployed safely under the project's established procedures.

A package release or static documentation release may not need the same operational checks as a production service deployment.

Record why material checks are not applicable where that distinction could otherwise be confusing.

### Phase 11: Prepare the release plan

Create an ordered sequence of actions.

For each material action, identify:

- Action.
- Purpose.
- Preconditions.
- Responsible actor or role.
- Required permission.
- Expected result.
- Evidence to capture.
- Failure handling.
- Whether the action changes external state.
- Whether approval is required.

Separate preparation from execution.

Use reversible actions before irreversible ones where practical.

Identify points at which the workflow must stop for a decision or approval.

Do not place a destructive migration, production deployment, or public publication into an execution sequence without establishing the applicable authorization.

### Phase 12: Assess rollback and recovery

Determine what recovery means for the specific release.

Possible recovery mechanisms include:

- Reverting a deployment.
- Redeploying a known-good artifact.
- Rolling back a package version.
- Disabling a feature flag.
- Restoring configuration.
- Reversing a compatible database migration.
- Applying a forward-fix.
- Restoring from a backup.
- Issuing a corrective release.

Do not assume every action is reversible.

For data migrations, determine whether rollback could lose data or produce incompatible state.

A rollback plan should identify:

- Trigger conditions.
- Decision authority.
- Recovery mechanism.
- Prerequisites.
- Expected impact.
- Data consistency considerations.
- Verification steps.
- Communication requirements.
- Escalation path.

If recovery is not feasible or has not been validated, state that limitation clearly.

Do not perform a rollback merely because it is listed in a plan. Apply the relevant authorization and incident procedures.

### Phase 13: Produce the readiness decision

Summarize the evidence and classify the candidate.

Use the following status model:

**NOT ASSESSED**

The candidate or applicable criteria have not been sufficiently examined.

**IN PREPARATION**

Release materials or prerequisites are being assembled.

**BLOCKED**

One or more mandatory prerequisites, decisions, or approvals remain unresolved.

**READY FOR REVIEW**

The available preparation and evidence are ready for the designated reviewer or authority.

**READY FOR APPROVAL**

The readiness assessment supports proceeding, but the required release authorization has not yet been granted.

**APPROVED**

The required authority has approved the defined candidate and scope. Approval does not itself prove publication or deployment.

**RELEASE IN PROGRESS**

An authorized publication or deployment process has started but is not yet confirmed complete.

**PUBLISHED**

The release has been confirmed available through the intended publication channel.

**DEPLOYED**

The deployment outcome has been confirmed for the intended environment.

**POST-RELEASE VERIFIED**

The specified post-release checks have passed for the intended target and scope.

**FAILED**

A release operation or required condition failed. Describe the evidence and impact.

**ROLLED BACK**

The rollback or recovery action has been confirmed. This does not automatically prove that the system has returned to a healthy state.

**COMPLETE**

The defined release workflow and its mandatory post-release checks have been completed, with remaining limitations explicitly recorded.

Use a status appropriate to the actual evidence. Do not jump directly from IN PREPARATION to COMPLETE.

### Phase 14: Obtain required approval

Identify the person, role, or system authorized to approve the release.

Confirm that approval covers the relevant:

- Candidate.
- Version.
- Scope.
- Target environment.
- Release window.
- Known risks or exceptions.
- Publication or deployment action.

Follow the organization's documented approval mechanism.

A vague expression of enthusiasm is not necessarily release authorization.

A previous approval may no longer apply if the candidate, scope, target, or risk materially changes.

Do not treat silence as approval.

If the required approver cannot be identified or contacted, report the blocker and stop before the gated action.

### Phase 15: Execute only authorized actions

Before an external action, verify that:

- The intended candidate is identified.
- The target is correct.
- Required checks are satisfied.
- Required approvals are present.
- The action is within the granted scope.
- Necessary tools and permissions are available.
- The execution plan is understood.
- Failure and recovery procedures are defined where needed.

Use the established release mechanism.

Capture the actual result, not just the command or API request.

If the operation fails or returns an ambiguous result, do not report success. Inspect the resulting state when safe and supported.

Avoid blindly repeating a non-idempotent operation. Determine whether the first attempt created partial external state before retrying.

### Phase 16: Verify publication or deployment

After execution, collect evidence that the intended outcome occurred.

For publication, relevant checks may include:

- Release record exists.
- Version is correct.
- Expected assets are present.
- Package is available at the intended registry.
- Checksums or signatures match.
- Release notes are published.
- Distribution metadata is correct.

For deployment, relevant checks may include:

- Intended environment received the expected revision.
- Deployment controller reports the expected state.
- Application health checks pass.
- Critical workflows function.
- Error rates remain acceptable.
- Required metrics and alerts are active.
- Migration outcomes are correct.
- No unexpected regressions are evident.

Do not claim more than the checks establish.

A successful publication does not prove that users can use the product successfully. A successful health check does not prove that every feature works.

### Phase 17: Observe and close

Perform the post-release observation required by the project's risk and operational policy.

Determine:

- Whether the release is stable.
- Whether expected metrics are within acceptable limits.
- Whether incidents or regressions occurred.
- Whether support or customer communication is needed.
- Whether recovery was necessary.
- Whether follow-up fixes remain.
- Whether the release record is complete.

Close the release only when the defined completion criteria are satisfied.

If monitoring must continue, record who owns it, what is being monitored, and when the observation period ends.

Do not claim that monitoring is active unless the relevant monitoring arrangement is confirmed.

### Phase 18: Preserve lessons and follow-up work

Record material improvements discovered during the release.

Examples include:

- Missing automated checks.
- Unclear approval ownership.
- Inaccurate changelog generation.
- Unreliable build provenance.
- Weak rollback procedures.
- Missing alerts.
- Confusing release status.
- Unnecessary manual steps.

Convert findings into explicit follow-up actions when appropriate.

Assign owners or deadlines only when those assignments are confirmed. Otherwise, mark them as proposed.

Do not expand a completed release into unrelated work without explaining the additional scope.

## 6. Deliverable Structure

Choose the smallest deliverable that adequately serves the request.

### 6.1 Release readiness report

A readiness report should contain:

1. Release identity.
2. Intended outcome.
3. Candidate and source revision.
4. Scope summary.
5. Applicable release criteria.
6. Evidence reviewed.
7. Readiness matrix.
8. Blockers.
9. Known issues and residual risks.
10. Approval status.
11. Recommended next action.
12. Evidence limitations.

A compact report may omit empty sections, but it must not omit material blockers or approval requirements.

### 6.2 Release plan

A release plan should contain:

1. Objective and scope.
2. Candidate identity.
3. Preconditions.
4. Ordered execution steps.
5. Responsible roles.
6. Approval gates.
7. Expected results.
8. Evidence capture.
9. Failure handling.
10. Rollback or recovery.
11. Post-release checks.
12. Completion criteria.

Clearly label unapproved steps and proposed decisions.

### 6.3 Release notes

A release note should contain the applicable elements:

- Product and version.
- Release date, if confirmed.
- Summary.
- New functionality.
- Changes and fixes.
- Breaking changes.
- Deprecations or removals.
- Security information suitable for the audience.
- Upgrade or migration instructions.
- Known issues.
- Compatibility information.
- Required user action.
- Relevant references.

Do not invent dates, versions, fixes, or compatibility claims.

If an item is not verified, omit it or label it appropriately.

### 6.4 Release record

A release record should capture:

- Release identifier.
- Candidate revision.
- Artifact identity.
- Scope.
- Readiness decision.
- Required approvals.
- Execution record.
- Publication or deployment result.
- Verification evidence.
- Known limitations.
- Recovery actions, if any.
- Final status.
- Follow-up actions.

Keep the record proportionate to the release's risk and the project's audit requirements.

### 6.5 Recovery report

A recovery report should include:

- Observed failure.
- Evidence and time of observation, where known.
- Known or suspected impact.
- Immediate containment.
- Recovery decision and authority.
- Actions attempted.
- Confirmed outcomes.
- Remaining risk.
- Current system or publication status.
- Required follow-up.

Separate observed facts from hypotheses.

### 6.6 Evidence references

Prefer references to authoritative records over unsupported narrative claims.

Where available, include:

- CI run identifiers.
- Test report references.
- Review records.
- Source commit identifiers.
- Artifact digests.
- Registry locations.
- Deployment identifiers.
- Health-check results.
- Approval records.
- Monitoring or incident records.

Do not expose credentials or confidential data in evidence references.

## 7. Decision and Authorization Rules

### 7.1 Separate readiness from approval

Readiness is a technical and procedural assessment.

Approval is an authorization decision made by the designated authority.

The Release skill may assess readiness and recommend approval when appropriate. It must not represent its own recommendation as an external approval.

### 7.2 Separate approval from execution

An approval may authorize a specific action under specific conditions.

Before execution, check whether the actual action matches the approved scope.

If the candidate or target has changed, determine whether the approval remains valid.

Do not use approval for one environment as permission to deploy to another.

### 7.3 Separate execution from verification

A successful command or API response is evidence about that operation. It may not establish the complete desired outcome.

Verify the resulting state using the appropriate source of truth.

If the verification mechanism is unavailable, report the action's observed result and state that the final outcome remains unverified.

### 7.4 Treat external side effects carefully

External side effects include:

- Publishing a package.
- Creating a public release.
- Uploading an artifact.
- Changing a production service.
- Applying a database migration.
- Changing traffic routing.
- Modifying a release channel.
- Sending a release announcement.
- Disabling or enabling a feature flag.
- Initiating rollback.

Before performing such actions, establish the user's intent, the target, the authorization boundary, and the relevant policy.

Follow any higher-priority confirmation requirements imposed by the execution environment or organization.

### 7.5 Use explicit approval gates

A gate must specify:

- What decision is required.
- Which candidate and scope it applies to.
- Who or what may approve it.
- What evidence the approver needs.
- Which action remains blocked until approval.
- What changes would invalidate the approval.

An approval request should be concise and decision-oriented.

Do not ask for approval when the user only requested an informational explanation or a draft and no gated action is involved.

### 7.6 Handle exceptions explicitly

If a release criterion cannot be satisfied, determine whether the requirement is mandatory or whether an authorized exception process exists.

Do not silently waive the requirement.

An exception record should identify:

- The unmet criterion.
- The reason for the exception.
- The associated risk.
- Mitigations.
- The approving authority.
- The affected release scope.
- Any expiration or follow-up requirement.

If no authorized exception exists, retain the blocker.

### 7.7 Do not infer permission from technical capability

Having access to a deployment tool does not mean the action is authorized.

Having repository write access does not mean publishing is approved.

Having administrator privileges does not justify bypassing the established release process.

Use access only within the applicable authorization boundary.

### 7.8 Treat ambiguity proportionately

Ask a focused question when uncertainty affects:

- Target environment.
- Candidate identity.
- Public versus private distribution.
- Data integrity.
- Security posture.
- Material compatibility.
- Irreversible actions.
- Required approval.
- Customer impact.

For nonessential uncertainties, continue safe preparation and list the unknowns.

### 7.9 Silence is not approval

Do not interpret a missing response, an unattended notification, or a passed deadline as authorization unless a documented policy explicitly defines that behavior and applies to the case.

When a required decision remains unanswered, stop at the gate and report the dependency.

### 7.10 Preserve reversibility where possible

Prefer actions that preserve the ability to inspect, pause, or recover.

Examples include:

- Preparing a release draft before publication.
- Building and verifying an artifact before distribution.
- Testing migrations in a representative nonproduction environment.
- Confirming the target before changing production.
- Recording the current state before a material change.

Reversibility does not replace authorization.

### 7.11 Avoid false certainty

Use language that reflects the evidence.

Prefer:

- "The CI run reports that the required test suite passed."
- "The artifact digest matches the recorded build output."
- "The deployment system reports the intended revision."
- "The available health checks passed."
- "Production behavior remains unverified."

Avoid unsupported claims such as:

- "Everything is guaranteed to work."
- "The release is completely safe."
- "Rollback is guaranteed."
- "All users are unaffected."
- "The deployment is successful" when only the deployment command was submitted.

### 7.12 Respect higher-priority rules

Security, privacy, legal, compliance, and organizational policies take precedence over this skill's general procedure.

If the requested release would violate a governing policy, do not proceed with the prohibited action.

Explain the conflict and identify a compliant alternative where possible.

## 8. Failure Handling

### 8.1 Missing release information

**Symptoms**

The version, candidate, target, release type, or scope is unclear.

**Response**

- Identify the missing information.
- Determine which details materially affect the requested task.
- Ask focused questions for essential decisions.
- Continue safe preparation where possible.
- Mark unresolved fields explicitly.
- Do not invent a release identity.

### 8.2 Missing test or review evidence

**Symptoms**

A required test report, review record, or verification result cannot be found.

**Response**

- Mark the requirement UNKNOWN or BLOCKED, as appropriate.
- Determine whether the evidence exists elsewhere.
- Request the relevant record or authorized verification.
- Identify whether the missing evidence is mandatory.
- Do not claim that the check passed.
- Do not rerun potentially disruptive checks without considering their effects.

### 8.3 Failed required checks

**Symptoms**

A required test, security scan, build, or compatibility check fails.

**Response**

- Preserve the failure details.
- Identify the affected candidate.
- Determine whether the failure is reproducible and material.
- Route technical diagnosis to the appropriate workflow.
- Keep the release blocked when policy requires the check to pass.
- Do not suppress, delete, or misrepresent failure evidence.
- Require revalidation after relevant changes.

### 8.4 Candidate drift

**Symptoms**

The source revision, artifact, configuration, or scope changes after review or approval.

**Response**

- Identify the original and current candidates.
- Determine what changed.
- Assess which evidence remains applicable.
- Re-run or request the checks affected by the change.
- Determine whether renewed approval is required.
- Do not assume approval transfers automatically.

### 8.5 Version conflict

**Symptoms**

The intended version already exists or conflicts with registry or repository rules.

**Response**

- Inspect the authoritative version records.
- Determine whether the version is immutable.
- Identify whether the previous release attempt partially succeeded.
- Do not overwrite an existing release blindly.
- Ask for a versioning decision if policy does not resolve the conflict.
- Record the chosen resolution.

### 8.6 Artifact mismatch

**Symptoms**

The artifact intended for release does not match the reviewed or verified candidate.

**Response**

- Stop publication or deployment when the mismatch is material.
- Compare source revisions and artifact identities.
- Inspect build records and provenance.
- Determine whether the correct artifact can be recovered or rebuilt.
- Revalidate the replacement artifact as required.
- Obtain renewed approval if necessary.
- Do not silently substitute the artifact.

### 8.7 Missing permissions

**Symptoms**

The execution environment lacks access to the repository, registry, deployment system, or target environment.

**Response**

- Report the specific permission boundary.
- Identify the minimum required authorized access.
- Provide a handoff or manual step for an authorized operator.
- Do not request or expose secrets unnecessarily.
- Do not bypass access controls.
- Do not report the blocked action as complete.

### 8.8 Publication failure

**Symptoms**

A release upload, registry operation, or publication command fails.

**Response**

- Capture the error and operation identifier.
- Inspect the resulting external state before retrying, when safe.
- Determine whether partial publication occurred.
- Check for version conflicts or duplicate artifacts.
- Retry only when the action is safe and the cause is understood.
- Verify the final published state independently.
- Report any unresolved uncertainty.

### 8.9 Deployment failure

**Symptoms**

A deployment does not complete or the target does not reach the expected state.

**Response**

- Determine the current target state.
- Identify affected services and potential user impact.
- Preserve deployment and diagnostic evidence.
- Follow the incident and escalation procedure when required.
- Assess whether to pause, recover, roll back, or apply a forward-fix.
- Obtain the required decision authority.
- Verify the outcome of the chosen recovery.
- Do not repeatedly deploy without understanding the failure mode.

### 8.10 Health-check failure after deployment

**Symptoms**

The deployment reports success but post-release checks fail.

**Response**

- Treat the release as operationally unverified or failed according to policy.
- Identify which checks failed.
- Determine the scope and severity of impact.
- Compare expected and observed behavior.
- Follow the incident response process when warranted.
- Decide on recovery through the appropriate authority.
- Verify the resulting state.
- Do not label the release complete merely because deployment succeeded.

### 8.11 Rollback failure

**Symptoms**

The recovery action fails, partially completes, or leaves inconsistent state.

**Response**

- Stop unsafe repeated recovery attempts.
- Determine the current state of affected components.
- Preserve logs, identifiers, and relevant evidence.
- Escalate to the designated operational owner.
- Consider a forward-fix or alternative recovery only under the applicable authority.
- Assess data integrity and user impact.
- Communicate what is known and unknown.
- Do not claim the previous version has been restored without evidence.

### 8.12 Migration or data-integrity risk

**Symptoms**

A release includes a migration or schema change that may be irreversible or incompatible.

**Response**

- Determine the migration's actual effects.
- Confirm backups and recovery requirements where applicable.
- Check compatibility with deployed application versions.
- Verify the migration in a suitable environment when required.
- Identify whether rollback is technically possible.
- Prefer a forward-compatible migration strategy where appropriate.
- Do not execute destructive operations without the required authorization.
- Stop if data-loss risk is not adequately understood.

### 8.13 Incomplete release notes

**Symptoms**

The change list, compatibility statements, or upgrade instructions cannot be verified.

**Response**

- Identify the unsupported statements.
- Consult authoritative change records.
- Remove or qualify unverified claims.
- Record known issues and limitations.
- Ask for clarification where a material user-facing claim remains uncertain.
- Do not invent fixes, capabilities, or dates to make the release notes look complete.

### 8.14 Security or compliance blocker

**Symptoms**

A required security check fails, a vulnerability remains unresolved, or compliance evidence is missing.

**Response**

- Preserve the evidence.
- Identify the governing policy and required decision authority.
- Assess whether the release must remain blocked.
- Follow the security disclosure and escalation process.
- Do not suppress findings or publish restricted details.
- Do not create an unauthorized exception.
- Record the final decision and its scope.

### 8.15 Monitoring unavailable

**Symptoms**

Required monitoring, alerting, or post-release observation cannot be confirmed.

**Response**

- Determine whether monitoring is mandatory for the release.
- Identify the missing capability.
- Establish an approved alternative only if policy permits.
- Keep the release blocked or conditionally assessed as required.
- Record the gap and responsible owner.
- Do not claim ongoing observation without evidence.

### 8.16 Conflicting status sources

**Symptoms**

The CI system, registry, deployment controller, or operator reports different states.

**Response**

- Identify which source is authoritative for each fact.
- Compare timestamps and candidate identities.
- Inspect the latest relevant state.
- Separate confirmed facts from conflicting reports.
- Avoid collapsing contradictory evidence into a single confident claim.
- Escalate unresolved material discrepancies.

### 8.17 Interrupted execution

**Symptoms**

The agent, terminal, network, or external tool stops responding during a release action.

**Response**

- Do not assume the action failed simply because the response was interrupted.
- Do not assume it succeeded either.
- Inspect the external state when safe and supported.
- Determine whether the operation is idempotent.
- Avoid duplicate execution until the prior result is understood.
- Record what was attempted and what remains unknown.

### 8.18 Recovery and handoff

If the skill cannot safely resolve a problem:

- Stop at the relevant boundary.
- Preserve the current state and evidence.
- Summarize known facts and unknowns.
- Identify immediate risks.
- Specify the decision or capability required.
- Provide the next safe action.
- Identify actions that must remain blocked.

A good handoff enables the next operator to continue without reconstructing the entire investigation.

## 9. Output Expectations

### 9.1 Be explicit about status

Put the current release status near the beginning of a substantial report.

Use a concise status statement followed by evidence, blockers, and next steps.

Do not bury an approval blocker in a long checklist.

### 9.2 Distinguish facts, proposals, and unknowns

Use explicit labels when needed:

- **Confirmed:** Supported by evidence.
- **Proposed:** Recommended but not approved.
- **Assumed:** Used provisionally and still requires confirmation.
- **Unknown:** Insufficient evidence.
- **Blocked:** A required prerequisite or decision is unresolved.
- **Verified:** Checked against a stated criterion using identified evidence.
- **Unverified:** Not yet established by available evidence.
- **Not applicable:** Does not apply to this release, with rationale where useful.

Avoid using labels mechanically when ordinary wording is clearer. The distinction itself must remain intact.

### 9.3 Make blockers actionable

For each material blocker, state:

- What is missing or failing.
- Why it matters.
- Which evidence supports the finding.
- What would resolve it.
- Who or what must make the decision, if known.
- Whether release execution must stop.

Do not assign a person or deadline without evidence or confirmation.

### 9.4 Keep the report proportional

Use a brief checklist for a low-risk patch when that is sufficient.

Use a more detailed readiness matrix and execution record for high-impact or regulated releases.

Do not overwhelm the user with irrelevant requirements. Do not omit material safeguards for convenience.

### 9.5 Provide reproducible next steps

When useful, give commands, checks, or links to the relevant project records.

Commands must match the known environment and actual tooling.

Label commands that publish, deploy, delete, migrate, or otherwise change external state.

Do not present untested commands as verified.

### 9.6 Report actions honestly

When tools are available, distinguish among:

- Tool unavailable.
- Permission denied.
- Action not attempted.
- Action attempted.
- Action returned success.
- Result independently verified.
- Result remains ambiguous.

Do not claim an external action occurred merely because instructions were provided.

### 9.7 Include a completion statement

When a release workflow is complete, summarize:

- What was released.
- The confirmed version and target.
- The source or artifact identity.
- Which post-release checks passed.
- Remaining known limitations.
- Any follow-up actions.

If completion criteria have not been met, report the current status instead.

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
