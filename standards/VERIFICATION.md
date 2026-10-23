# Verification Standard

**Version:** 1.0

## 1. Purpose

Verification establishes whether a result satisfies its stated requirements.

Agentic Brain distinguishes between performing an action, observing its result, and proving that the result meets the required criteria.

No skill may claim successful verification without appropriate evidence.

## 2. Core Rules

1. **Evidence before claims.** Claims about tests, commands, file changes, deployments, and other actions must be supported by observed evidence.
2. **Attempted does not mean successful.** Running a command does not establish that it passed.
3. **Partial success remains partial.** Passing some checks does not establish that all requirements are satisfied.
4. **Report limitations.** If verification cannot be performed, state why.
5. **Preserve uncertainty.** Missing evidence must not be replaced by confidence or inference.
6. **Verify the relevant outcome.** A successful tool call is not necessarily proof that the intended result occurred.
7. **Respect authorization.** Verification must not bypass permissions, safeguards, or approval requirements.

## 3. Verification States

Use these states when reporting material results:

- `not-started`: Verification has not been attempted.
- `in-progress`: Verification is underway.
- `passed`: The defined check succeeded, supported by evidence.
- `failed`: The defined check ran and did not meet its criteria.
- `blocked`: Verification could not proceed because of a dependency or restriction.
- `not-applicable`: The check does not apply, with a brief rationale.
- `inconclusive`: Available evidence does not establish success or failure.

Do not use `passed` when the check did not run or when its result is ambiguous.

## 4. Verification Plan

Before consequential work, identify applicable checks in proportion to the risk and complexity of the task.

A verification plan should define, when relevant:

- Requirement or behavior being checked.
- Check or test to perform.
- Expected result.
- Required environment or dependencies.
- Evidence needed to determine the outcome.

Clarify acceptance criteria when ambiguity could materially change the result.

For low-risk, reversible work, use a lightweight plan. For high-impact work, use more rigorous and independent checks.

## 5. Evidence Requirements

Evidence should be specific enough for another person or agent to understand what was checked and what happened.

Examples include:

- Test output and exit codes.
- Build or lint results.
- Relevant command output.
- File contents or diffs.
- API responses or observable application behavior.
- Deployment or operational status from an authoritative source.
- Review findings linked to specific requirements.

Record relevant context when necessary, including the command, environment, scope, and limitations.

Do not expose secrets, credentials, private tokens, or unnecessary personal information in evidence.

A claim should not exceed what its evidence supports. For example, a successful build does not prove that every feature works correctly.

## 6. Requirements-to-Evidence Mapping

For work with multiple acceptance criteria, map each important criterion to a check and its result.

| Criterion | Check | Result | Evidence |
|---|---|---|---|
| Required behavior works | Relevant test | `passed` | Test output or report |
| Existing behavior remains intact | Regression test | `not-started` | None yet |
| Documentation is accurate | Content review | `in-progress` | Review findings |

This table is illustrative. Actual checks must reflect the task.

Do not mark the overall task fully verified while material acceptance criteria remain failed, blocked, inconclusive, or unchecked.

## 7. Failure Handling

When a check fails:

1. Report the failure accurately.
2. Preserve the relevant error or evidence.
3. Determine whether the failure is caused by the implementation, environment, test, or an unknown factor.
4. Avoid unsupported root-cause claims.
5. Fix the issue only within the authorized scope.
6. Rerun the relevant check after a change.
7. Report any remaining failures or limitations.

A later successful check does not erase the historical failure if that history is relevant to understanding the work.

## 8. Independent Review

Use an independent verification method when the risk justifies it.

Examples include:

- Reviewing a diff after tests pass.
- Checking generated files rather than trusting a success message.
- Testing boundary cases in addition to ordinary cases.
- Comparing observed behavior with explicit acceptance criteria.
- Reviewing security-sensitive changes separately from functional correctness.

Independent review is not mandatory for every trivial task. Its use should be proportionate to risk.

## 9. Final Verification Report

For consequential work, report:

- **Outcome:** What was completed.
- **Checks performed:** What was actually tested or inspected.
- **Results:** The state of each relevant check.
- **Evidence:** The observable results supporting the claims.
- **Limitations:** What was not checked or could not be established.
- **Remaining work:** Outstanding failures, blockers, or acceptance criteria.

Clearly distinguish completed work from verified work.

## 10. Handoffs

When handing work to another skill or agent:

- Include material verification states and evidence.
- Identify failed or incomplete checks.
- Preserve relevant environmental constraints.
- State what the receiving skill must verify next.
- Never convert an unverified claim into a verified fact.

Use the shared Handoff Contract for the transfer of context, decisions, blockers, and next actions.

## 11. Completion Rule

A task may be described as completed only when its agreed completion criteria have been met.

If implementation is complete but verification remains outstanding, report that distinction explicitly.

If a requirement cannot be verified, identify it as unresolved rather than silently treating it as satisfied.
