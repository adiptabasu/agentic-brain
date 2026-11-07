# Verification Standard

## Purpose

Verification establishes what evidence supports a result. Performing an action and observing its success message do not by themselves prove that the intended outcome meets its requirements.

## Core rules

1. Make claims only when supported by relevant observed evidence.
2. Distinguish attempted actions from successful outcomes.
3. Do not say tests, builds, reviews, or evaluations passed unless they were run and their results reviewed.
4. Report partial results and material limitations; do not generalize beyond what was checked.
5. Use checks appropriate to the change and its risk. Do not add or run unrelated tests.

## Verification states

- `not-started`: no check has been attempted.
- `in-progress`: a check is underway.
- `passed`: the defined check succeeded and its evidence was reviewed.
- `failed`: the check ran and did not meet its criteria.
- `blocked`: a dependency or restriction prevented the check.
- `inconclusive`: evidence does not establish success or failure.
- `not-applicable`: the check does not apply, with a brief reason.

## Plan and evidence

For material changes, identify the relevant requirement, the check, and the evidence needed. Evidence may include command output and exit codes, inspected file contents or diffs, or observed application behavior. Keep evidence specific and do not expose secrets.

If a check fails, report the failure and evidence accurately. Do not claim a root cause without evidence. After a fix, rerun the relevant check and report the result; a later pass does not erase a relevant earlier failure.

## Reporting

State what was changed, what checks were actually performed, their results, and what remains unchecked or uncertain. If an implementation is complete but verification is incomplete, say so. A task is verified only when its material acceptance criteria have appropriate supporting evidence.
