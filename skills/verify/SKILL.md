---
name: verify
description: Check outcomes against explicit criteria and report observed results, failures, and unknowns.
---

# Verify — Evidence-Based Outcome Verification

## 1. Purpose

Verify establishes whether an intended outcome has actually been achieved by comparing explicit expectations against observable evidence.

Its central rule is:

**An attempted action is not a verified outcome. A claim is not evidence.**

An agent may write code, run a command, invoke a tool, update a configuration, or request a deployment without achieving the intended result. Verify determines what the available evidence supports, what remains uncertain, and what should happen next.

Verify exists to prevent unsupported statements such as:

- "The tests pass" when tests were not run or their results are unavailable.
- "The issue is fixed" when the relevant failure condition has not been retested.
- "The file was updated" when the write operation was not confirmed.
- "The deployment succeeded" when only a deployment request was submitted.
- "The change is compatible" when compatibility has not been evaluated.
- "Everything is working" when only one narrow scenario was checked.

Verification must be proportionate to the risk and scope of the claim. It should establish meaningful confidence without inventing evidence, repeating dangerous actions, or expanding the task unnecessarily.

Verify does not guarantee absolute correctness. It reports what was checked, how it was checked, what the evidence demonstrates, and what remains outside the verification scope.

## 2. Core Responsibilities

### 2.1 Define the expected outcome

Identify the specific result that must be established.

Use available requirements, acceptance criteria, specifications, approved decisions, test expectations, and explicit user instructions.

An expectation should be observable whenever possible.

Examples:

- A specified API request returns the documented response.
- A regression test reproduces the original defect before the fix and passes afterward.
- A configuration file contains the approved setting.
- A build command completes successfully.
- A generated artifact exists at the intended location and can be read.
- A deployment service reports the intended release as healthy.
- A database migration completes and the expected schema change is present.

Do not replace a missing acceptance criterion with an invented one.

If the expected outcome is ambiguous and the ambiguity materially affects verification, ask a focused question or report the limitation. Continue with clearly defined checks that remain valid.

### 2.2 Identify the evidence required

Choose evidence that directly supports the claim.

Depending on the task, evidence may include:

- Command output and exit status.
- Test results and test reports.
- Build or compilation output.
- Relevant source files or generated artifacts.
- File existence, contents, metadata, or checksums.
- API responses and service health checks.
- Database query results.
- Deployment status and runtime observations.
- Logs, traces, and monitoring measurements.
- Reproduction steps and observed behavior.
- Version-control status, diffs, and commit history.
- Explicit confirmation from an authorized external system.

Prefer direct, current, relevant evidence over indirect statements.

A tool invocation is evidence that an action was attempted. It is not automatically evidence that the intended effect occurred.

### 2.3 Execute or coordinate appropriate checks

Perform checks only when the necessary tools, access, permissions, and context are available.

Use the least disruptive method that provides adequate evidence.

When verification requires another skill or a specialized capability, hand off the defined verification task with its expectations, constraints, and current evidence.

Do not claim to have run a command, inspected a file, accessed a service, or observed a result unless that activity actually occurred and the result is available.

If the environment does not permit direct verification, provide the exact checks a capable operator or agent should perform.

### 2.4 Evaluate evidence against expectations

For every material acceptance criterion, determine whether the evidence supports the expected outcome.

Distinguish among:

- **Verified:** Sufficient evidence supports the specified claim within the stated scope.
- **Failed:** Evidence demonstrates that the criterion was not satisfied.
- **Blocked:** A required check could not be completed because of a concrete dependency, permission, environmental limitation, or other obstacle.
- **Inconclusive:** Available evidence is insufficient or contradictory.
- **Not checked:** The criterion was not evaluated.

Do not collapse these states into a binary success/failure label when doing so would hide important uncertainty.

### 2.5 Report the verification boundary

State what was checked and what was not.

A passing unit test does not establish that an entire application works in production. A successful build does not prove functional correctness. A healthy service does not establish that every user workflow is correct.

Keep conclusions within the scope of the evidence.

### 2.6 Recommend the next action

When verification identifies a failure, uncertainty, or blocker, recommend a proportionate next step.

Examples include:

- Run a missing test.
- Reproduce the original failure.
- Inspect contradictory evidence.
- Obtain required access.
- Ask for a missing acceptance criterion.
- Return a specific finding to Debug or Implement.
- Request explicit authorization before a consequential action.
- Report the limitation when additional checks are unsafe or unavailable.

Do not automatically repeat a failed or consequential operation without assessing its risks.

## 3. When to Use Verify

Use Verify when an agent must establish whether a claimed result is supported by evidence.

Typical situations include:

- After implementation or bug fixes.
- After running tests, builds, or static analysis.
- After modifying configuration or infrastructure.
- After creating, editing, or converting files.
- After executing database operations or migrations.
- After making API requests or changing external systems.
- After requesting a deployment or release.
- Before reporting completion to a user.
- Before handing work to another agent or workflow stage.
- When evidence from multiple sources conflicts.
- When a previous agent reports success without sufficient supporting details.

Verify can be used independently for a narrow check or as a final verification stage in a larger workflow.

### 3.1 When not to use Verify as the primary skill

Do not use Verify as a replacement for:

- Requirements discovery and ambiguity resolution: use Probe.
- Formal requirements specification: use Specify.
- Technical architecture and trade-off analysis: use Design.
- Sequencing work and identifying dependencies: use Plan.
- Test-driven implementation workflow: use Test-First.
- Diagnosing the root cause of a defect: use Debug.
- Implementing code or modifying an artifact: use Implement.
- Independent assessment of code quality and design risks: use Review.
- General workflow navigation: use Guide.

These skills may provide evidence that Verify subsequently evaluates.

## 4. Shared Standards

### 4.1 Clarify, Don't Assume

Never silently convert an expectation into an observed result.

Keep distinct:

- What was requested.
- What was expected.
- What action was attempted.
- What was actually observed.
- What conclusion the evidence supports.
- What remains unknown.

If a material expectation is unclear, resolve it before issuing a definitive verdict.

### 4.2 Evidence before claims

Every material verification conclusion must be traceable to relevant evidence.

Identify the source and, when available, the command, test, artifact, response, timestamp, version, or observation that supports the conclusion.

Do not fabricate evidence, results, identifiers, logs, file contents, or test outcomes.

### 4.3 Preserve authorization boundaries

Verification permission does not automatically authorize remediation or other consequential actions.

Do not assume permission to:

- Modify production systems.
- Deploy or roll back releases.
- Delete or overwrite data.
- Run destructive migrations.
- Change permissions or security controls.
- Spend money or create external commitments.
- Send communications on behalf of a user.
- Repeat an operation that may create duplicate or irreversible effects.

Check existing authorization and applicable safeguards before taking action.

### 4.4 Continue safe independent work

A blocked check should not unnecessarily stop unrelated, safe verification work.

Record the blocker, complete independent checks where useful, and report what remains unresolved.

### 4.5 Preserve context during handoffs

When handing work to another skill or agent, include:

- The claim or outcome being verified.
- Relevant acceptance criteria.
- Evidence already collected.
- Checks already attempted.
- Failures, contradictions, and blockers.
- Remaining checks.
- Constraints and authorization boundaries.

Do not force the next agent to reconstruct context that is already available.

### 4.6 Evidence-based completion

Never report a task as fully verified when material acceptance criteria remain failed, blocked, inconclusive, or unchecked.

A task may be complete within an explicitly limited scope even when broader verification is unavailable, but that limitation must be stated clearly.

## 5. Operating Procedure

### Step 1: Establish the verification target

Identify the exact claim or outcome to establish.

Examples:

- "Verify that the regression is fixed."
- "Verify that the generated report is readable."
- "Verify that the build succeeds."
- "Verify that the deployment is healthy."
- "Verify that the implementation satisfies the agreed acceptance criteria."

Avoid vague targets such as "check everything" unless the scope has been explicitly defined.

If the target includes multiple outcomes, break it into individually assessable criteria.

### Step 2: Recover authoritative expectations

Gather the strongest available source of expected behavior.

Use the following order as a guide, subject to the actual task's authority structure:

1. Explicit user instructions and approved decisions.
2. Approved acceptance criteria or requirements.
3. Relevant specifications and contracts.
4. Applicable repository standards and documented invariants.
5. Existing tests and established behavior.
6. Reasonable diagnostic checks that do not invent new requirements.

Existing implementation behavior is not automatically the correct specification. Existing tests may be incomplete or incorrect. Treat each source according to its authority and relevance.

If two authoritative sources conflict, do not silently choose one. Report the conflict and seek clarification when it affects the verdict.

### Step 3: Build a verification matrix

Map each material criterion to a check and an expected observation.

Example:

| Criterion | Verification method | Expected evidence |
|---|---|---|
| Regression is fixed | Run a focused regression test | Test passes and exercises the defect |
| Project compiles | Run the documented build command | Successful exit status |
| API contract is preserved | Run relevant contract tests | Expected status and response structure |
| Artifact is valid | Inspect or parse the generated artifact | Successful validation |
| Deployment is healthy | Inspect deployment status and health checks | Intended release is healthy |

Adapt the matrix to the task. Do not require every category when it is irrelevant.

For small tasks, a concise checklist is sufficient.

### Step 4: Inspect the available environment

Determine which relevant evidence sources are actually accessible.

Establish, as applicable:

- Current project or artifact location.
- Relevant branch, commit, or version.
- Available test and build commands.
- Tool permissions and execution limitations.
- Environment or configuration dependencies.
- Whether the evidence reflects the latest intended change.
- Whether an external operation is safe and authorized.

Do not assume that a tool exists, a command is supported, a service is reachable, or a file is present.

If the environment cannot be inspected directly, record the limitation rather than guessing.

### Step 5: Select proportionate checks

Choose checks based on the acceptance criteria, risk, change scope, and available evidence.

A useful progression is:

1. **Basic integrity:** Confirm that the relevant artifact or change exists and is readable.
2. **Structural validation:** Check syntax, formatting, schema, or expected structure.
3. **Focused behavior:** Exercise the directly affected behavior.
4. **Regression coverage:** Check that the original defect or failure no longer occurs.
5. **Broader integration:** Validate interactions with relevant components.
6. **System-level behavior:** Check end-to-end or runtime behavior when required.
7. **Operational outcome:** Confirm external effects such as deployment health when explicitly in scope.

Not every task requires every level.

Use the narrowest checks that adequately establish the required outcome, adding broader checks when the risk or acceptance criteria justify them.

### Step 6: Execute checks safely

Before running a check:

- Confirm that the command or action matches the intended environment.
- Identify destructive, costly, externally visible, or irreversible effects.
- Check whether the operation is safe to repeat.
- Confirm required permissions and approvals.
- Prefer read-only inspection when it is sufficient.
- Use isolated or disposable environments for destructive tests when appropriate.

Run only authorized checks.

Capture actual results, including failures, exit codes, and relevant output when available. Do not suppress a material error merely to produce a cleaner result.

If a check cannot be run, mark it as blocked, inconclusive, or not checked according to the reason.

### Step 7: Assess result quality

Determine whether each check actually tests the criterion it is intended to establish.

Consider:

- Does the test exercise the changed code or relevant behavior?
- Does the evidence come from the correct commit, artifact, environment, or version?
- Did the check complete successfully, or did only the command launch?
- Were tests skipped, filtered, mocked, or disabled?
- Did a test pass because the relevant assertion was never reached?
- Is the observed result consistent with independent evidence?
- Is the evidence sufficiently recent for the claim?
- Are important environmental conditions missing?
- Could a cached result or stale artifact explain the outcome?
- Does the check prove the full claim or only a narrower property?

A green status indicator is not sufficient when the underlying check is irrelevant, incomplete, or stale.

### Step 8: Evaluate each criterion

Assign one of the five statuses:

**Verified**
- The check ran or the required evidence was otherwise obtained.
- The evidence is relevant and sufficiently reliable.
- The expected result was observed.
- No known contradiction undermines the conclusion within the stated scope.

**Failed**
- Evidence directly demonstrates that the criterion was not met.

**Blocked**
- A necessary check could not proceed because of a specific external dependency, missing permission, unavailable environment, or other concrete obstacle.

**Inconclusive**
- Evidence is incomplete, contradictory, ambiguous, or insufficient to distinguish success from failure.

**Not checked**
- No meaningful verification was attempted for the criterion.

Do not use "verified" to mean merely "likely correct."

### Step 9: Investigate contradictions

When evidence conflicts, preserve the conflicting observations and investigate their scope.

For example:

- A local test passes, but the integration test fails.
- The build succeeds for one commit, while the current branch contains additional changes.
- A deployment request succeeds, but the health check fails.
- A file exists, but its contents do not match the expected output.
- A dashboard reports healthy status, but recent logs show a relevant error.

Check whether the evidence differs by version, time, environment, configuration, or test coverage.

Do not discard negative evidence simply because another source reports success.

If the contradiction cannot be resolved safely, mark the relevant criterion inconclusive and explain why.

### Step 10: Decide whether further verification is warranted

Additional checks are warranted when they materially reduce uncertainty about an important claim.

Consider:

- Severity of a possible failure.
- Likelihood and impact of an undetected regression.
- Importance of the acceptance criterion.
- Reliability of current evidence.
- Cost and risk of further checks.
- Whether the remaining uncertainty affects the completion decision.

Stop when the required scope has adequate evidence or when further checking is blocked, unsafe, unauthorized, or disproportionate.

Do not endlessly repeat passing checks without a reason. Do not continue merely to accumulate evidence that does not materially improve the conclusion.

### Step 11: Remediate or hand off when needed

When a criterion fails, determine whether the next step is within Verify's authorized scope.

If further implementation or diagnosis is needed, hand off to the relevant skill:

- Debug for root-cause investigation.
- Implement for a code or artifact change.
- Test-First for a test-driven development workflow.
- Review for independent assessment of a change.
- Probe or Specify when the expected behavior itself is unclear.

Include the failing criterion, observed evidence, reproduction details, and any constraints.

After remediation, verify the relevant criteria again. A proposed fix is not a verified fix.

### Step 12: Report the final result

Produce a concise but auditable summary that states:

- Overall verification status.
- Scope and version or artifact examined, when known.
- Criteria checked and their statuses.
- Checks actually performed.
- Key supporting evidence.
- Failures, blockers, and contradictions.
- Limitations and unchecked areas.
- Recommended next actions.

The overall status must not hide a material failure or unresolved blocker.

## 6. Verification Deliverable Structure

For simple checks, report the result, scope, evidence, and limitations briefly. Read references/verify-report-format.md when a detailed report or criteria matrix is useful.

## 7. Decision and Authorization Rules

### 7.1 Overall status

Choose the overall status according to the most consequential unresolved criterion.

**Verified within scope**
- All required material criteria are verified.
- No material contradiction remains unresolved.
- The scope and limitations are stated.

**Partially verified**
- Some material criteria are verified, but others remain blocked, inconclusive, or unchecked.
- The verified portion is clearly identified.

**Failed**
- One or more required criteria have evidence demonstrating failure.
- A passing check elsewhere does not override the failed criterion.

**Blocked**
- Required verification cannot meaningfully proceed because of a material external dependency or authorization constraint.
- Report any useful checks completed independently.

**Inconclusive**
- The available evidence cannot support a defensible overall conclusion, and the uncertainty cannot currently be resolved.

Use the label that best communicates the current state. If a result contains both a confirmed failure and a blocker, report both explicitly rather than obscuring the failure behind the blocker.

### 7.2 No unsupported completion claims

Do not say that a task is complete merely because:

- A command was submitted.
- An agent reported success.
- A file-editing tool returned without an obvious error.
- A test process started.
- A deployment was requested.
- A commit was created.
- A dashboard displayed a general success indicator.
- A checklist was completed without inspecting the underlying evidence.

Confirm the specific outcome when the claim requires it.

### 7.3 No implied authorization

Verification does not grant permission to change the system being verified.

If a check reveals a problem, do not automatically deploy a fix, alter production data, change access controls, or perform a rollback unless that action is already explicitly authorized and safe under the applicable constraints.

### 7.4 External effects require stronger evidence

For consequential external actions, distinguish among:

1. Requested.
2. Accepted by the tool or service.
3. Executed.
4. Observed in the target system.
5. Confirmed to have achieved the intended outcome.

These are separate states.

For example, an HTTP request returning success may confirm that the request was accepted, but it may not prove that an asynchronous job completed or that the intended downstream effect occurred.

Choose the verification depth required by the claim and risk.

### 7.5 Evidence freshness and scope

Evidence must correspond to the relevant version, environment, and time.

Do not use a previous commit's passing tests to claim that the current untested commit passes.

Do not use development-environment observations to claim production health.

If the evidence is stale or its provenance is unclear, report that limitation and obtain fresh evidence when appropriate.

### 7.6 Security and sensitive information

Avoid exposing credentials, tokens, personal data, private keys, or other secrets in verification reports.

When logs contain sensitive material, summarize the relevant observation and redact the sensitive portions.

Do not disable security controls or weaken safeguards merely to make a verification check pass.

### 7.7 Confidence is not proof

Confidence can help communicate uncertainty, but a numerical confidence score must not replace evidence or a clear status.

Do not invent percentages or precision that the verification method cannot justify.

## 8. Failure Handling

Preserve actual outcomes and distinguish failed, blocked, inconclusive, and unchecked criteria. Read references/verify-failure-handling.md for the matching failure path.

## 9. Output Expectations

### 9.1 Be precise

Prefer:

- "The unit test `test_invalid_input` passed in the observed run."
- "The build command exited successfully."
- "The file exists, but its contents have not been validated."
- "The deployment request was accepted; runtime health is not yet confirmed."
- "The integration check is blocked by unavailable staging credentials."

Avoid:

- "Everything is fine."
- "It definitely works."
- "The issue is fixed" without a relevant retest.
- "All tests passed" when only a subset ran.
- "Deployment complete" when only a request was submitted.

### 9.2 Keep evidence actionable

Include enough detail for another person or agent to reproduce or audit important conclusions.

Where available, provide:

- Command or test identifier.
- Relevant output or exit status.
- Artifact or version identifier.
- Environment and timing.
- Acceptance criterion.
- Failure location or reproduction steps.

Do not dump large logs when a focused excerpt or summary is sufficient.

### 9.3 Separate observations from interpretations

Use explicit language:

- **Observed:** What the evidence directly shows.
- **Interpretation:** What the observation means for the criterion.
- **Limitation:** What the evidence does not establish.
- **Next action:** What should happen next.

This separation is particularly important when evidence is indirect or incomplete.

### 9.4 Match detail to risk

A small, reversible documentation change may need only a concise integrity check.

A security-sensitive change, production deployment, migration, or other high-impact operation requires stronger and more explicit evidence.

Do not apply a heavyweight verification process indiscriminately, but never reduce verification below what the claim and risk reasonably require.

### 9.5 Respect user communication preferences

Use the format requested by the user when compatible with clarity and safety.

If a user requests a short completion summary, keep it short while retaining material failures and limitations.

Do not conceal uncertainty merely to make a report more reassuring.

## 10. Skill maintenance criteria

This maintenance-only checklist is in references/verify-maintenance.md; it is not an acceptance-criteria template for the user’s work.

## 11. Portability

Use available tools and evidence without assuming a platform. For skill-adapter guidance, see references/verify-maintenance.md only when maintaining this skill.

## 12. Maintenance

Skill-maintenance guidance is in references/verify-maintenance.md and is not needed for routine verification.
