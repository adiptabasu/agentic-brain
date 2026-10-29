# Optional verification report format

Read when a detailed verification report or matrix is needed; scale the structure to the task.

## 6. Verification Deliverable Structure

Use the following structure for meaningful verification work. Scale it down for simple checks.

### 6.1 Summary

State the overall result in plain language.

Examples:

- "Verified within the stated scope: the targeted regression test and relevant build passed."
- "Partially verified: syntax and unit tests passed, but integration behavior remains unchecked."
- "Verification failed: the acceptance criterion for API response compatibility was not met."
- "Verification is blocked: the required staging environment is unavailable."

### 6.2 Scope

Identify what was examined.

Include relevant details when available:

- Repository and commit.
- Artifact or file.
- Service or component.
- Environment.
- Version or release identifier.
- Acceptance criteria covered.

Do not invent identifiers when the environment does not provide them.

### 6.3 Results matrix

| Criterion | Status | Evidence | Limitation or next action |
|---|---|---|---|
| Specific acceptance criterion | Verified / Failed / Blocked / Inconclusive / Not checked | Actual observed result | Relevant caveat or next step |

Every material criterion should have an explicit status.

### 6.4 Checks performed

List the meaningful checks actually performed.

For each check, include the command, test name, query, observation, or other identifier when available, along with its result.

Distinguish checks that were run from checks that were only recommended.

### 6.5 Findings and limitations

Describe material failures, unresolved contradictions, missing evidence, environmental constraints, and unverified areas.

Prioritize items that affect safety, correctness, release readiness, or the user's stated goal.

### 6.6 Conclusion

State exactly what can and cannot be claimed.

Avoid broad statements such as "everything works" unless the scope is explicitly defined and the evidence adequately supports the statement.

### 6.7 Recommended next action

Identify the next useful step, responsible skill or operator, and any required authorization.

If no further action is required within the requested scope, say so without implying broader validation.
