# Release failure handling

Read only when a release blocker, failed check, publication/deployment issue, recovery need, or other listed failure occurs.

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
