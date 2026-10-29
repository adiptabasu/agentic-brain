# Verification failure handling

Read only when a check fails, is blocked or interrupted, produces inconsistent results, or causes an unexpected effect.

## 8. Failure Handling

### 8.1 Missing tools or access

If a required tool, environment, account, permission, or artifact is unavailable:

1. Identify the exact missing dependency.
2. Complete independent checks that remain useful and safe.
3. State which criteria are affected.
4. Specify what access or evidence is needed.
5. Mark the affected criteria appropriately.

Do not imply that an unavailable check passed.

### 8.2 Command failure

When a command fails:

1. Preserve the actual error and exit status when available.
2. Determine whether the failure is relevant to the criterion.
3. Distinguish an infrastructure or setup failure from a product failure when evidence supports that distinction.
4. Avoid repeated execution without understanding the possible effects.
5. Recommend diagnosis or remediation when appropriate.

A test runner that cannot start does not establish that the code is correct or incorrect. It establishes that the intended test result is unavailable until the execution problem is resolved.

### 8.3 Flaky or nondeterministic checks

If results vary across repeated runs:

1. Record the differing outcomes.
2. Check whether the environment, data, timing, or dependencies changed.
3. Avoid selecting only the passing run.
4. Determine whether the acceptance criterion requires deterministic behavior.
5. Report the instability and its effect on the verdict.

Repeated retries can help diagnose nondeterminism but do not erase earlier failures.

### 8.4 Contradictory evidence

When sources disagree:

1. Identify each observation and its source.
2. Confirm that the sources refer to the same version, environment, and behavior.
3. Investigate plausible scope or timing differences.
4. Seek additional independent evidence if safe and useful.
5. Preserve unresolved contradictions in the final report.

Do not silently prefer the source that supports the desired conclusion.

### 8.5 Incomplete or ambiguous requirements

If a criterion lacks an observable definition:

1. State the ambiguity.
2. Determine whether an authoritative specification resolves it.
3. Ask a focused question when the ambiguity materially changes the verdict.
4. Perform only checks that do not depend on the unresolved interpretation.
5. Mark the remaining criterion inconclusive or blocked as appropriate.

Do not invent a new acceptance threshold simply to finish the verification.

### 8.6 Unexpected side effects

If verification triggers an unexpected consequential effect:

1. Stop further actions that could worsen the situation.
2. Preserve relevant evidence.
3. Assess immediate risk within available information.
4. Follow applicable incident and authorization procedures.
5. Escalate to the appropriate operator when necessary.
6. Do not attempt an unapproved rollback or cleanup.

Report the side effect honestly, including what is known and unknown.

### 8.7 Partial results

When some checks succeed and others fail or cannot run:

- Preserve the individual statuses.
- Identify the exact scope that is verified.
- Avoid an unqualified overall success statement.
- Explain which missing checks matter to the requested outcome.
- Recommend the next action that most efficiently resolves the uncertainty.

### 8.8 Interrupted verification

If execution is interrupted, a tool times out, or the environment becomes unavailable:

- Record the last confirmed state.
- Distinguish completed checks from interrupted checks.
- Do not infer the result of an unfinished operation.
- Determine whether rerunning it is safe.
- Resume only when sufficient context and authorization remain available.
