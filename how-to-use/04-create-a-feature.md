# Create a feature in an existing codebase

Use this when you want to add behavior to a project that already exists. First make sure the agent has the correct repository open; see [how to provide a codebase](02-provide-a-codebase.md).

## 1. Describe the feature and ask for clarification

Invoke `probe` or say:

> Read the repository instructions and inspect the relevant code. Use probe to clarify this feature request: [describe desired outcome]. Ask about decisions that could change the behavior, user experience, compatibility, or risk. Do not edit files yet.

Answer questions about expected behavior, edge cases, constraints, and what should remain unchanged. If something is a preference rather than a requirement, label it as such.

## 2. Agree on requirements and design

Ask `specify`:

> Use specify to turn the agreed feature into testable requirements and acceptance criteria. Include important edge cases and non-goals. Keep unconfirmed behavior as an open question rather than filling it in.

Review and approve the specification. If the feature affects architecture, interfaces, stored data, compatibility, or security, ask `design` to compare options:

> Use design to propose an implementation approach for the approved requirements. Explain the affected components, interfaces, trade-offs, risks, and any migration or compatibility concerns. Wait for my decision on consequential choices.

## 3. Plan the change

Ask `plan` for an execution outline:

> Use plan to break this feature into focused tasks. Include dependencies, test coverage, completion criteria, and any decisions that still need approval. Preserve existing behavior outside the approved scope.

For a small feature, a short plan may be enough. Confirm any meaningful design decisions before implementation.

## 4. Develop test-first

Start with `test-first`:

> Use test-first for the approved acceptance criteria. Inspect the existing test conventions, add or identify a focused test for the first behavior, and show what should fail before the implementation. Do not change unrelated tests or behavior.

Then implement the approved slice:

> Use implement to make the smallest change that satisfies the failing criterion. Run the relevant checks and report exactly what ran and the result. Stop before expanding the scope.

Review the result and repeat for the next slice only after the current behavior and tests are understood.

## 5. Review and verify

Ask for an independent code review:

> Use review to inspect the diff against the approved requirements. Look for defects, regressions, missing tests, maintainability concerns, and compatibility issues. Report findings; don't make edits during the review.

Then ask `verify`:

> Use verify to map every acceptance criterion to actual evidence. Report test commands and results, plus anything blocked, failed, inconclusive, or unchecked. Do not make a broader success claim than the evidence supports.

Ask `document` to update relevant user or developer docs if the feature changes documented behavior. Creating a feature does not by itself authorize a commit, push, or deployment.
