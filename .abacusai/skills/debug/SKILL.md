---
name: debug
description: Systematically investigate unexpected behavior, errors, and failures by reproducing symptoms, gathering evidence, testing competing hypotheses, isolating root causes, and verifying fixes. Use when software, workflows, tests, integrations, or systems behave differently from their established expectations.
---

# Debug

## 1. Purpose

Debug provides a systematic, evidence-driven process for investigating unexpected behavior and determining what causes it.

It helps establish the observed problem, gather relevant evidence, develop and test hypotheses, isolate the cause, validate a correction, and communicate the result with appropriate confidence.

Debug follows the principle **Clarify, Don't Assume**. A plausible explanation is not a confirmed root cause. A change that appears to work once is not automatically a verified fix.

Debug prioritizes reproducibility, controlled investigation, preservation of evidence, and minimal changes that address the established cause.

It does not silently redefine expected behavior, authorize risky operations, or claim that a defect is resolved without sufficient verification.

## 2. Core Responsibilities

### 2.1 Establish the symptom

Describe what is happening, what was expected to happen, and under what conditions the difference occurs.

Distinguish:

- The user's reported symptom from its possible cause.
- Observed behavior from inferred behavior.
- A reproducible failure from an intermittent or unconfirmed report.
- An established requirement from an assumption about intended behavior.
- A new regression from a pre-existing failure, when evidence allows.

Do not label behavior a defect until the expected behavior is sufficiently established.

### 2.2 Gather relevant evidence

Collect the smallest useful set of evidence needed to understand the failure.

Depending on the environment, this may include:

- Error messages and stack traces.
- Application, system, or service logs.
- Inputs, outputs, and relevant state.
- Reproduction steps.
- Recent code, configuration, data, or dependency changes.
- Runtime, platform, version, and environment information.
- Test results and build output.
- Network requests, responses, timing, or resource usage.
- Relevant architecture and interface contracts.

Use only sources and tools that are actually available. Do not claim to have inspected files, logs, environments, or external systems that were not accessible.

Protect credentials, tokens, personal information, and other sensitive data when collecting or sharing evidence.

### 2.3 Form competing hypotheses

Develop plausible explanations that are consistent with the observed evidence.

For each important hypothesis, identify:

- The evidence supporting it.
- Evidence that would weaken or disprove it.
- A test or observation that distinguishes it from alternatives.
- The expected result if it is correct.
- Any risks associated with testing it.

Keep hypotheses distinct from established facts. Avoid prematurely committing to the first explanation that seems reasonable.

### 2.4 Isolate the cause

Reduce the problem to the smallest useful reproduction or subsystem.

Use controlled comparisons, targeted tests, binary search over changes or inputs where appropriate, and systematic elimination of hypotheses.

Change one relevant variable at a time when practical. If an experiment changes multiple variables, account for the resulting uncertainty.

Distinguish the immediate trigger from the underlying cause and contributing conditions when the evidence supports those distinctions.

### 2.5 Develop and validate a correction

Prefer the smallest safe correction that addresses the established cause without introducing unrelated changes.

Consider:

- Whether the correction addresses the demonstrated failure mechanism.
- Whether it preserves existing contracts and requirements.
- Whether it introduces new edge cases or regressions.
- Whether a regression test should be added.
- Whether migration, rollout, rollback, or operational safeguards are necessary.

If the root cause remains uncertain, label the change as a candidate mitigation or provisional fix rather than presenting it as a confirmed resolution.

### 2.6 Verify and communicate

Reproduce the original scenario after the correction and run relevant regression checks.

Report:

- What was observed.
- What evidence was collected.
- Which hypotheses were tested.
- What cause was established, if any.
- What changed.
- Which verification steps were executed.
- Actual results and remaining limitations.
- Any risks or follow-up work.

Do not claim that a problem is fixed merely because the error disappeared temporarily or a single unrelated test passed.

## 3. When to Use Debug

Use Debug when:

- An application, service, or workflow behaves unexpectedly.
- A test or build fails.
- A regression appears after a change.
- An integration returns unexpected results.
- A production or development issue needs investigation.
- Performance, reliability, or resource behavior deviates from expectations.
- A proposed fix needs its causal explanation validated.
- A failure is intermittent, environment-specific, or difficult to reproduce.

Debug can be used for software, infrastructure, data pipelines, agent workflows, and other technical systems, provided the available evidence and investigation methods fit the problem.

Do not use Debug as a substitute for:

- Requirements definition when expected behavior is unclear.
- Technical design when the real task is to choose an architecture.
- Test planning when the primary need is to define expected behavior.
- Authorization when an investigation requires a restricted or risky action.
- Independent verification when the work requires a separate review or assurance process.

These activities may be required before, during, or after debugging.

## 4. Shared Standards

Follow the repository's shared standards:

- `standards/CORE-PRINCIPLES.md`
- `standards/HANDOFF-CONTRACT.md`
- `standards/SKILL-TEMPLATE.md`
- `standards/VERIFICATION.md`

Apply the shared principles:

1. Follow **Clarify, Don't Assume**.
2. Do not treat silence as approval.
3. Distinguish confirmed facts, hypotheses, assumptions, proposed changes, and verified results.
4. Preserve context and evidence across handoffs.
5. Do not claim a command, test, experiment, or external action occurred without evidence.
6. Make material uncertainty and environmental limitations visible.
7. Continue safe, independent investigation when a nonessential unknown remains unresolved.
8. Ask focused questions when ambiguity materially affects diagnosis, safety, authorization, or correctness.

Shared standards remain the canonical source for general rules. This skill defines their application to investigation and root-cause analysis.

## 5. Operating Procedure

### Step 1: Define the problem

Establish:

- The observed symptom.
- Expected behavior and its source.
- When the problem occurs.
- Who or what is affected.
- Frequency and reproducibility.
- Recent relevant changes.
- Impact and urgency, when known.

Separate the problem statement from explanations about why it occurs.

If the expected behavior is ambiguous, identify the competing interpretations and clarify material differences before using one as the basis for diagnosis.

### Step 2: Assess risk and preserve the current state

Before investigation, determine whether the problem affects production systems, sensitive data, availability, security, or irreversible operations.

Where appropriate:

- Preserve relevant logs and timestamps.
- Capture error messages and reproduction details.
- Record relevant versions and configuration.
- Preserve a known failing input or test case.
- Avoid destructive experiments.
- Avoid exposing secrets in diagnostic output.
- Obtain required authorization before restricted actions.

Do not modify the environment merely to make investigation easier if doing so could destroy evidence or worsen the incident.

For urgent incidents, prioritize safe containment and recovery according to the applicable incident process. Root-cause investigation may continue after immediate impact is controlled.

### Step 3: Reproduce the failure

Attempt to reproduce the symptom under controlled conditions.

Record:

- Preconditions.
- Exact input or triggering action.
- Relevant environment and versions.
- Steps to reproduce.
- Expected result.
- Actual result.
- Whether the failure is consistent.

Use the smallest reproduction that preserves the failure.

If reproduction is not possible, document the attempts and available evidence. Do not invent reproduction steps or claim reproducibility without evidence.

### Step 4: Establish a baseline

Determine whether the behavior is new, intermittent, environment-specific, or already present.

Compare against relevant evidence such as:

- A known-good version.
- Earlier test results.
- A different environment.
- A working input or request.
- A related successful execution.
- Recent deployment or configuration changes.

Control for differences between comparison cases.

Do not attribute the failure to a recent change solely because the timing appears correlated.

### Step 5: Gather and organize evidence

Collect relevant evidence before making speculative corrections.

For each observation, record its source and what it establishes.

Useful distinctions include:

- **Observed:** directly visible in logs, output, tests, or reproduced behavior.
- **Inferred:** a conclusion drawn from observations.
- **Hypothesized:** a possible explanation that has not been established.
- **Unknown:** information needed but not currently available.

Check whether logs are complete, timestamps align, the relevant environment is represented, and the evidence corresponds to the failing execution.

Absence of an error message is not proof that the relevant operation succeeded.

### Step 6: Map the failure path

Trace the relevant flow from trigger to observable result.

Depending on the system, examine:

- Inputs and validation.
- State transitions.
- Component or service boundaries.
- Data transformations.
- Calls to external dependencies.
- Error propagation and exception handling.
- Configuration and environment differences.
- Timing, concurrency, and lifecycle behavior.

Focus on the path that can explain the symptom. Do not investigate unrelated components without a reason.

### Step 7: Form and prioritize hypotheses

Develop a manageable set of plausible explanations.

Prioritize them using evidence, explanatory power, testability, and the cost or risk of investigation.

For each hypothesis, ask:

- What would have to be true for this explanation to hold?
- Which existing observations support it?
- What observation would contradict it?
- What is the smallest safe experiment that distinguishes it?
- Could multiple causes produce the same symptom?

Do not manufacture numerical confidence scores. If qualitative confidence is useful, explain the evidence supporting it.

### Step 8: Design a discriminating experiment

Choose a test that distinguishes competing explanations rather than merely repeating the symptom.

A useful experiment has:

- A clear hypothesis.
- A controlled change or observation.
- An expected result if the hypothesis is correct.
- An alternative interpretation if the result differs.
- A way to avoid or account for confounding variables.
- Appropriate safety and rollback precautions.

Prefer reversible, low-risk experiments.

If the experiment cannot distinguish competing explanations, refine it before treating its result as decisive.

### Step 9: Run the experiment and interpret results

Execute the test only when the necessary tools, access, and authorization are available.

Record what actually happened.

For each result:

1. Compare the observation with the predicted result.
2. Determine which hypotheses gained or lost support.
3. Identify alternative explanations for the outcome.
4. Update the investigation rather than forcing the result to fit the original theory.
5. Choose the next experiment based on the new evidence.

A failed experiment may still be useful if it eliminates a hypothesis or reveals an environmental limitation.

Do not claim an experiment was executed when it was only proposed.

### Step 10: Isolate the root cause

Use the accumulated evidence to determine which explanation best accounts for the failure.

When possible, establish a causal connection by demonstrating that:

- The suspected condition is present.
- It can produce the observed symptom.
- Correcting or controlling it changes the outcome.
- The result is repeatable under relevant conditions.
- Competing explanations have been reasonably considered.

Distinguish:

- **Trigger:** the event or input that activates the failure.
- **Immediate cause:** the mechanism directly producing the symptom.
- **Underlying cause:** the condition that allows the mechanism to occur.
- **Contributing factor:** another condition that increases likelihood or impact.

Use these labels only when the evidence supports them. Some investigations will establish only a likely cause, not a complete causal chain.

### Step 11: Select the correction or mitigation

Choose a correction proportionate to the established cause and the problem's impact.

Consider whether the appropriate response is:

- A code change.
- A configuration correction.
- A data repair.
- A dependency or interface correction.
- A change to validation or error handling.
- A rollback or containment measure.
- Improved observability.
- An operational or process change.
- Further investigation because the cause remains unresolved.

Distinguish a mitigation that reduces symptoms from a fix that addresses the cause.

Do not introduce unrelated refactoring or expand scope without justification and authorization.

### Step 12: Verify the correction

After applying an authorized correction, verify the original failure scenario.

Where appropriate:

1. Re-run the minimal reproduction.
2. Confirm the expected behavior.
3. Run a regression test.
4. Execute relevant unit, integration, contract, or system tests.
5. Check relevant logs and state.
6. Assess side effects and compatibility.
7. Verify recovery or rollback behavior when required.

Record actual commands, results, and limitations when available.

A single successful run may be insufficient for intermittent, concurrent, or timing-sensitive defects. Choose repeated or broader verification when justified by the risk.

If verification cannot be completed, state what remains unverified.

### Step 13: Assess regressions and residual risk

Determine whether the correction could introduce new problems or leave part of the original failure unresolved.

Consider:

- Related code paths.
- Boundary conditions.
- Error handling.
- Concurrency and retries.
- Data consistency.
- Performance and resource use.
- Security and authorization.
- Compatibility with existing interfaces.
- Deployment and rollback requirements.

Add regression coverage when practical and appropriate.

Do not claim that all regressions have been ruled out merely because selected tests pass.

### Step 14: Document and hand off

Summarize the investigation in a form appropriate to the issue.

Include:

- Problem statement and impact.
- Expected and observed behavior.
- Reproduction steps or the reason reproduction was unavailable.
- Relevant evidence.
- Hypotheses tested and their results.
- Established or likely cause.
- Correction or mitigation.
- Verification performed and outcomes.
- Remaining uncertainty, risks, and follow-up actions.

If another person or agent must continue, provide the context needed to resume without repeating unnecessary work.

Follow the shared handoff contract.

## 6. Debug Deliverable Structure

Adapt the level of detail to the severity and complexity of the issue.

### 6.1 Problem statement

Describe the symptom, expected behavior, scope, impact, and reproducibility.

### 6.2 Environment and reproduction

Record relevant versions, preconditions, inputs, steps, and observed results when available.

### 6.3 Evidence log

Use a concise table when it helps separate observations from interpretation.

| Field | Meaning |
|---|---|
| Evidence | Observation, output, or artifact |
| Source | Where it came from |
| Observation time | When it was collected, if relevant |
| Interpretation | What it supports or contradicts |
| Limitations | Missing context or reliability concerns |

### 6.4 Hypothesis register

For significant hypotheses, record:

| Field | Meaning |
|---|---|
| Hypothesis | Proposed explanation |
| Supporting evidence | Observations consistent with it |
| Contradicting evidence | Observations that weaken it |
| Discriminating test | Experiment that could distinguish it |
| Result | Actual outcome, if tested |
| Status | Open, weakened, rejected, likely, or confirmed where justified |

Avoid maintaining a large list of speculative causes without useful tests.

### 6.5 Root-cause assessment

State the established cause or best-supported explanation, the causal evidence, and the remaining uncertainty.

If the cause is unknown, say so explicitly.

### 6.6 Correction and verification

Describe the correction or mitigation and the verification performed.

Distinguish proposed actions from completed actions and observed results.

### 6.7 Follow-up

List outstanding risks, prevention measures, monitoring, regression coverage, and further investigation where relevant.

### 6.8 Handoff

Provide the current status, key evidence, decisions, blockers, and next action.

## 7. Decision and Authorization Rules

### 7.1 A hypothesis is not a finding

Do not present a plausible explanation as the root cause without sufficient supporting evidence.

Use calibrated language such as:

- Possible cause.
- Evidence supports this explanation.
- Likely cause.
- Cause confirmed under the tested conditions.

Choose the strongest wording the evidence justifies.

### 7.2 Correlation is not causation

A failure occurring after a deployment or configuration change does not, by itself, prove that change caused the problem.

Use controlled comparisons, reproduction, or other evidence to establish a stronger causal link.

### 7.3 A workaround is not necessarily a fix

State whether a change contains the impact, bypasses the failure, or addresses the underlying cause.

Do not label a workaround a root-cause correction without evidence.

### 7.4 Preserve evidence and authorization boundaries

Do not delete logs, alter production data, disable security controls, expose secrets, or execute destructive experiments without appropriate authorization and safeguards.

If an investigation requires a restricted action, identify the decision and access needed.

### 7.5 Do not hide contradictory evidence

Record observations that challenge the leading hypothesis.

Reassess the explanation when new evidence contradicts it rather than selectively reporting only supportive results.

### 7.6 Separate diagnosis from approval

A technical finding does not automatically authorize a deployment, rollback, data repair, or other consequential operation.

Follow the relevant approval and operational processes.

### 7.7 Be explicit about incomplete investigations

If reproduction, diagnosis, or verification is incomplete, report the exact limitation and the next useful step.

Do not imply resolution because the investigation has stopped.

## 8. Failure Handling

### Failure cannot be reproduced

Collect available evidence, identify differences between failing and successful conditions, and seek a minimal reproduction.

Treat the cause as unresolved until sufficient evidence exists.

### Evidence is incomplete

Identify the missing evidence, why it matters, and how to obtain it safely.

Avoid filling gaps with unsupported assumptions.

### Multiple hypotheses remain plausible

Design a test that distinguishes them, or explain why the available environment cannot do so.

Report the uncertainty rather than selecting an arbitrary cause.

### Experiments produce conflicting results

Check for uncontrolled variables, environment differences, timing, shared state, and unreliable measurements.

Preserve the conflicting observations and update the investigation.

### Root cause remains unknown

Report what has been established, what has been ruled out, what remains plausible, and the next high-value investigation step.

A useful partial diagnosis is preferable to a fabricated definitive answer.

### Correction fails to resolve the problem

Reproduce the failure after the correction, reassess the causal theory, and investigate whether the correction was incomplete or the original hypothesis was wrong.

Do not repeatedly apply variations of the same fix without new evidence.

### Regression appears

Determine whether the correction introduced the regression, exposed an existing issue, or coincided with another change.

Use evidence to establish the relationship and follow appropriate rollback or mitigation procedures.

### Environment or access is unavailable

Identify which investigative or verification steps cannot be performed.

Provide a bounded analysis based on available evidence without claiming execution or confirmation.

### Investigation has operational risk

Stop or defer the risky experiment until appropriate authorization, isolation, backup, and recovery measures are established.

Prioritize safe containment when impact is ongoing.

## 9. Output Expectations

A useful Debug result is:

- **Reproducible:** the failure is characterized by concrete observations where possible.
- **Evidence-driven:** conclusions follow from available evidence.
- **Hypothesis-aware:** alternatives are tested rather than ignored.
- **Causally grounded:** root-cause claims reflect the strength of the evidence.
- **Minimal:** changes address the established problem without unnecessary scope expansion.
- **Regression-conscious:** relevant neighboring behavior is considered.
- **Verifiable:** the original failure and correction are tested appropriately.
- **Safe:** investigation respects authorization, data protection, and operational risk.
- **Portable:** the method is independent of a particular language or vendor platform.
- **Honest:** uncertainty, incomplete diagnosis, and unexecuted verification remain explicit.
- **Actionable:** another person can understand the evidence and continue the work.

The objective is not to produce a confident-sounding explanation quickly. It is to reduce uncertainty and establish the best-supported causal explanation with the least unnecessary risk.

## 10. Acceptance Criteria for the Debug Skill

The skill is behaving as intended when it can:

1. Separate symptoms from hypotheses and established causes.
2. Identify the source of expected behavior before treating an observation as a defect.
3. Establish a reproducible failure when practical.
4. Gather relevant evidence without claiming access it does not have.
5. Develop competing hypotheses with discriminating tests.
6. Account for confounding variables and contradictory observations.
7. Distinguish triggers, immediate causes, underlying causes, and contributing factors when supported.
8. Recommend a minimal, appropriately authorized correction or mitigation.
9. Verify the original failure after a correction when execution is available.
10. Report test outcomes and environmental limitations accurately.
11. Preserve operational safety, sensitive information, and evidence.
12. Avoid treating correlation, a workaround, or a single successful run as definitive proof.
13. Provide a useful handoff when diagnosis or verification remains incomplete.
14. Follow shared standards without silently changing their meaning.
15. Adapt investigation methods to different technical systems and environments.

These criteria describe intended behavior. They do not establish that the skill has been tested or that any platform compatibility has been verified.

## 11. Portability

- Use plain Markdown and standard Agent Skills metadata.
- Avoid dependence on a particular model provider or proprietary orchestration API.
- Do not assume that a particular programming language, logging system, debugger, or test framework is available.
- Do not assume access to source code, runtime environments, production logs, credentials, or external services unless the runtime establishes their availability.
- Use explicit handoffs when direct skill invocation is unsupported.
- Treat compatibility with individual agent platforms as unverified until tested.
- Prefer investigation methods that can be adapted to the system's available evidence and tools.

## 12. Maintenance

When updating Debug:

1. Preserve alignment with the shared core principles and handoff contract.
2. Keep diagnosis distinct from requirements definition, implementation, and independent verification.
3. Prefer discriminating experiments over speculative or uncontrolled changes.
4. Remove duplicated rules when a shared standard already defines them.
5. Validate metadata, Markdown structure, whitespace, and internal references after edits.
6. Test representative debugging scenarios before claiming behavioral compatibility.
7. Record meaningful changes through the repository's normal Git workflow.
