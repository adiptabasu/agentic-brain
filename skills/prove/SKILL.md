---
name: prove
description: Build a traceable evidence package supporting a claim, decision, or handoff.
---

# Prove

## 1. Purpose

Prove assembles a clear, traceable case for what available evidence supports.

It connects claims about an outcome to explicit criteria, identifies the sources and limits of evidence, evaluates whether the evidence is relevant and sufficient for the stated claim, and makes gaps visible.

Prove follows **Clarify, Don't Assume**. It distinguishes claims from observations, evidence from interpretation, and a supported conclusion from certainty.

Prove is an evidence-synthesis and assurance skill. It may organize existing evidence and coordinate collection of missing evidence when authorized. It does not independently imply that a test, review, audit, or external action has occurred.

Prove complements Verify:

- **Verify** defines and performs or coordinates checks against expected outcomes, then reports their results.
- **Prove** assembles a claim-centered, traceable evidence case from relevant criteria, observations, and verification results, and shows where the case is weak or incomplete.

Neither skill can establish more than its evidence supports. “Proof” in this skill means a defensible, bounded evidence argument, not mathematical certainty or a guarantee that no defect exists.

## 2. Core Responsibilities

### 2.1 Establish the claim and decision

Identify the claim or set of claims that the evidence package is intended to support.

Examples include:

- A specific acceptance criterion was met.
- A change preserved a named compatibility contract.
- A control is operating within a defined scope.
- A release candidate satisfies a stated readiness condition.
- A document's statements are supported by authoritative sources.
- An incident action achieved a specific observable result.

State the subject, scope, conditions, and timeframe of each claim. If a claim is vague, broad, or ambiguous, refine it with the user or mark the boundary explicitly.

Do not rewrite a claim to make the available evidence appear sufficient.

### 2.2 Identify governing criteria

Find the requirements, acceptance criteria, policies, contracts, or decisions that define what would support the claim.

Record the source and status of each criterion. Distinguish approved requirements from proposals and assumptions.

If no suitable criterion exists, state that limitation. Do not invent a target after seeing the results merely to create a successful evidence story.

### 2.3 Locate and preserve evidence

Identify relevant evidence sources, such as:

- Test, build, lint, or analysis output.
- Code, configuration, and generated artifacts.
- Review findings and decisions.
- Runtime observations, service reports, or logs.
- Version-control diffs and commit metadata.
- Documentation and authoritative references.
- Records of approvals or external actions.
- Directly observed user or system behavior.

Capture sufficient provenance for another person to understand the evidence: source, time or version, scope, method, and relevant environment.

Preserve evidence accurately. Do not silently trim away failures, alter outputs, merge observations from incompatible runs, or present a summary as the original source.

### 2.4 Assess relevance and quality

Evaluate whether each item actually bears on the claim.

Consider:

- **Relevance:** Does the evidence address the specified claim and criterion?
- **Directness:** Is it direct observation or an indirect report?
- **Scope:** Does it cover the relevant version, environment, data, and conditions?
- **Reliability:** Is the source authoritative and the method suitable?
- **Currency:** Is it recent enough for the claim?
- **Completeness:** Are material cases, failures, or counterexamples omitted?
- **Independence:** Does it provide a distinct check or repeat the same underlying evidence?
- **Integrity:** Is the evidence intact and attributable to the claimed source?

State material limitations. A large volume of irrelevant or correlated evidence does not make a weak case strong.

### 2.5 Connect evidence to claims

For each claim, show which criteria it addresses, what evidence supports or challenges it, and what conclusion follows.

Keep observations and reasoning separate:

- Observation: what the evidence directly shows.
- Interpretation: how it relates to the criterion.
- Conclusion: what can reasonably be claimed within scope.
- Limitation: what remains unknown or unestablished.

Include contrary or failed evidence when it affects the conclusion. Do not cherry-pick successful outputs.

### 2.6 Identify gaps and counterevidence

Identify criteria with no evidence, evidence that does not cover the needed scope, contradictory sources, and plausible counterexamples.

Recommend a proportionate next step, such as a missing check, a narrower claim, clarification of an acceptance criterion, or a handoff to Verify, Review, Shield, or another responsible process.

Do not relabel missing evidence as a pass or use confidence language to hide a gap.

### 2.7 Protect sensitive evidence

Minimize the collection and reproduction of secrets, personal data, exploit details, or confidential business information.

Redact or summarize sensitive material when possible without undermining the evidence. Preserve original evidence only in approved locations and according to applicable retention and access rules.

Do not create a broadly shareable evidence package that exposes information beyond its audience's need.

### 2.8 Report a bounded conclusion

Choose language that matches the evidence, such as:

- Supported within the stated scope.
- Partially supported.
- Not supported by the available evidence.
- Contradicted by the available evidence.
- Inconclusive because of identified gaps.
- Not assessed.

Do not use “proven,” “guaranteed,” “compliant,” or “secure” without a precise, justified scope and appropriate evidence. Even then, describe the limits.

## 3. When to Use Prove

Use Prove when:

- A decision needs a traceable record of claims and supporting evidence.
- Multiple checks, sources, or reviewers must be synthesized.
- A completion, readiness, or compliance-adjacent claim needs a bounded rationale.
- A handoff must preserve why a conclusion was reached.
- An audit trail or evidence package needs to be organized for review.
- A summary needs to show missing criteria, contradictory evidence, or limitations.
- The evidence exists but is scattered across artifacts or reports.

Do not use Prove as a substitute for:

- Defining requirements and acceptance criteria: use Specify.
- Performing checks and evaluating whether outcomes meet criteria: use Verify.
- Independently examining a change for defects: use Review.
- Security threat analysis: use Shield.
- Formal audit, certification, legal determination, or regulated attestation where a recognized process or qualified authority is required.
- Collecting evidence through active testing without authorization.

Use Verify when the main task is to run or coordinate the check. Use Prove when the main task is to assemble and assess the claim-to-evidence relationship. Both may be used in sequence when useful.

## 4. Shared Standards

Follow:

- `standards/CORE-PRINCIPLES.md`
- `standards/HANDOFF-CONTRACT.md`
- `standards/SKILL-TEMPLATE.md`
- `standards/VERIFICATION.md`

In particular:

1. Treat a claim, report, or planned check as distinct from an observed result.
2. Preserve the exact status of evidence and verification.
3. Do not convert proposals, assumptions, or approvals into facts.
4. Preserve relevant failures, contradictory evidence, and uncertainty.
5. Respect authorization, privacy, and evidence-handling requirements.
6. Keep conclusions within the scope of the criteria and evidence.
7. Preserve context and evidence in handoffs without implying new approval.

The shared standards remain authoritative. This skill applies them to claim-centered evidence synthesis.

## 5. Operating Procedure

### Step 1: Establish the purpose and audience

Identify the decision or communication the evidence case supports, the intended audience, and the level of assurance needed.

Determine whether the case is internal, operational, customer-facing, regulatory, or otherwise consequential. Apply the relevant evidence handling and review requirements.

### Step 2: Define claims and boundaries

Write each claim in a way that specifies the subject, scope, conditions, and relevant time or version.

Separate broad claims into smaller claims when different evidence is needed. Identify excluded contexts and avoid wording that implies a wider result.

### Step 3: Map claims to criteria

Locate the governing acceptance criteria, policy, contract, or approved decision for each claim.

Record criterion identifiers or source locations where practical. If criteria are missing, ambiguous, or changed after results were observed, disclose the issue and seek clarification when it affects the conclusion.

### Step 4: Inventory evidence and provenance

List available evidence with enough context to identify:

- Source and owner, where known.
- Date, version, commit, environment, or run identifier.
- Collection method and scope.
- Relevant result or excerpt.
- Whether it is original, transformed, summarized, or independently reviewed.
- Access or sensitivity constraints.

Do not claim evidence exists if only a plan or reference to it exists.

### Step 5: Assess evidence quality

Evaluate each item for relevance, directness, scope, reliability, currency, completeness, independence, and integrity as appropriate.

Identify dependencies between evidence items. For example, several reports may all rely on the same test run and therefore do not constitute independent confirmation.

### Step 6: Build the claim-evidence argument

For each criterion, record:

- The claim or criterion.
- Supporting evidence.
- Contrary, failed, or ambiguous evidence.
- The interpretation and reasoning.
- The bounded conclusion.
- The limitation or remaining gap.

Use a matrix or concise case narrative that lets another reviewer trace each conclusion back to evidence.

### Step 7: Resolve or expose gaps

Determine whether gaps can be resolved safely and within authorization.

If a missing check is needed, hand the defined check to Verify or an appropriate specialist. If the criterion itself is unclear, use Probe or Specify. If a result depends on an unapproved decision, seek that decision rather than treating it as accepted.

Narrow a claim only when doing so preserves the user's intended meaning and is transparent.

### Step 8: Review the case for balance and integrity

Check that the evidence package:

- Includes relevant failures and counterevidence.
- Does not mix versions, environments, or time periods without explanation.
- Distinguishes raw evidence from derived summaries.
- Avoids unsupported precision or certainty.
- Protects sensitive information.
- Does not claim checks that were not run or approvals not received.

### Step 9: Deliver and preserve the case

Present the conclusion, claim-to-evidence mapping, limitations, and next steps in a form suitable for the audience.

Store or hand off evidence only through approved locations and methods. Include references that enable verification without disclosing unnecessary sensitive data.

## 6. Evidence Case Structure

For a material case, use:

### Purpose and audience

Decision to support and intended readers.

### Claims and criteria

Each bounded claim and its governing requirement, acceptance criterion, policy, or decision.

### Evidence inventory

Source, provenance, scope, status, and handling constraints for each material item.

### Claim-to-evidence mapping

| Claim or criterion | Supporting evidence | Contrary or missing evidence | Assessment |
|---|---|---|---|

Adapt the table when a narrative or structured format is clearer.

### Conclusion

What the case supports, contradicts, or cannot establish, with the boundary of each conclusion.

### Limitations and next steps

Missing evidence, unresolved criteria, required decisions, follow-up checks, and owners when known.

For low-risk or narrow work, a concise explanation may convey the same information without the full structure.

## 7. Decision and Authorization Rules

### 7.1 Synthesis within scope

Prove may organize available evidence, assess relevance and quality, identify gaps, and state bounded conclusions.

It may not change acceptance criteria, declare a proposal approved, or infer an approval from silence.

### 7.2 Collecting additional evidence

Collect only evidence that is within the user's authorization, the system's permissions, and applicable privacy or retention rules.

Obtain explicit authorization before:

- Accessing external services or restricted records.
- Running tests or operations that change state or incur cost.
- Capturing personal, confidential, or security-sensitive data.
- Sharing an evidence package with a new audience.
- Creating or altering official audit, legal, or compliance records.

When authorization is missing, specify the evidence needed and who or what could provide it.

### 7.3 Acceptance of residual gaps

Only the relevant authorized decision-maker may accept incomplete evidence or residual risk. Record the decision, scope, rationale, and approval evidence when available.

A conclusion that is “partially supported” is not the same as risk acceptance.

### 7.4 Conflicting criteria

If requirements, policies, or approvals conflict, preserve the conflict and route it for resolution. Do not choose whichever criterion the evidence happens to satisfy.

## 8. Failure Handling

### 8.1 Evidence source unavailable

Record the source and evidence that could not be accessed, why it matters, and the conclusion that remains unavailable. Do not substitute an unverified summary without labeling it.

### 8.2 Evidence is stale or mismatched

Identify the version, environment, date, or scope mismatch. Decide whether it invalidates the claim or merely narrows it, and explain the reasoning.

### 8.3 Evidence conflicts

Preserve both sources, compare their provenance and scope, and avoid averaging contradictory results into a single conclusion. Seek a targeted check or authoritative resolution.

### 8.4 Criterion is missing or changing

Do not invent or retroactively tune a criterion to fit observed results. Clarify the governing expectation and label any interim analysis as provisional.

### 8.5 Evidence is sensitive or potentially harmful

Minimize copies, redact appropriately, and restrict the audience. If safe reporting is uncertain, use the established secure channel or ask the responsible authority.

### 8.6 Evidence is insufficient

State which claim cannot be supported and the specific additional evidence required. Avoid substituting confidence, absence of reported incidents, or a successful unrelated check.

### 8.7 Integrity or provenance is uncertain

Mark the item as unverified, state what is unknown about its source or handling, and avoid relying on it as sole support for a consequential conclusion.

## 9. Output Expectations

A Prove output should:

- State the claim and intended decision clearly.
- Map material criteria to traceable evidence.
- Preserve evidence provenance and status.
- Include relevant failures and counterevidence.
- Explain gaps and limitations.
- Use calibrated, bounded conclusions.
- Protect confidential and personal information.
- Distinguish evidence synthesis from checks actually performed.

Avoid declaring an outcome “proven” in an absolute sense. Prefer precise statements such as “the supplied test output supports criterion AC-2 for commit X in environment Y.”

## 10. Acceptance Criteria

Prove is complete when:

1. Claims are bounded and linked to governing criteria.
2. Material evidence has identifiable provenance and scope.
3. Evidence relevance and limitations have been assessed.
4. Supporting, contrary, failed, and missing evidence are represented fairly.
5. Conclusions follow from the mapped evidence and do not exceed it.
6. Sensitive information is handled appropriately.
7. Gaps, decisions, and next steps are explicit.
8. No unperformed check, unreceived approval, or unsupported assurance is presented as fact.

If material claims cannot be supported, report the case as partial, inconclusive, or not supported rather than forcing a positive conclusion.

## 11. Portability

Prove does not depend on a particular evidence repository, audit platform, test runner, or agent runtime.

Evidence formats and provenance capabilities vary. Use the strongest available identifiers and clearly report what cannot be established. Do not claim cryptographic integrity, chain of custody, or non-repudiation unless the relevant mechanism was actually used and verified.

Adapters may define storage and presentation formats but must preserve the relationship among claims, criteria, evidence, conclusions, and limitations.

## 12. Maintenance

Update this skill when its evidence model, boundaries, or relationship to Verify changes materially.

When maintaining it:

- Keep evidence synthesis distinct from running and evaluating checks.
- Keep outputs aligned with the shared verification states.
- Avoid duplicate general rules already defined in shared standards.
- Ensure examples distinguish raw evidence, summary, inference, and conclusion.
- Record material limitations or compatibility evidence where the repository provides a place for them.
- Ensure metadata name remains `prove` and matches the directory.

Prove exists to make conclusions inspectable. A strong evidence case makes clear what is claimed, why the evidence matters, what it does not establish, and what remains to be done.
