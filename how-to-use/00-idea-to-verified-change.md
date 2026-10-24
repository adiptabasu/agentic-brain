# From an idea to a verified change

Use this walkthrough when you have a software problem or feature idea and want to move from an unclear request to a change with evidence that it works. The workflow is composable: skip steps that do not matter for your task, but do not skip decisions or checks that materially affect correctness or risk.

## 1. Start with Guide

Invoke `guide`, or say:

> Use the guide skill. I want to [describe the goal or problem]. Help me choose the right workflow. Ask about important uncertainties, constraints, and approval boundaries before recommending next steps.

If shortcuts are unavailable, say: “Read `skills/guide/SKILL.md` and follow it.”

## 2. Clarify and agree on the requirements

If the request is unclear, have `probe` ask focused questions:

> Use probe to identify assumptions and missing decisions that could change the solution. Ask one focused question at a time. Summarize confirmed requirements, unresolved items, and what you need me to decide.

When the request is clear enough, have `specify` produce acceptance criteria:

> Use specify to turn the confirmed request into testable requirements and acceptance criteria. Separate requirements from proposals and open questions. Do not add behavior I did not request.

Review the result. Correct it before approving. The specification is not approved just because the agent wrote it.

## 3. Design and plan when the work needs them

For changes with meaningful architectural or interface choices:

> Use design to compare the reasonable approaches for these requirements. Explain trade-offs, risks, and compatibility effects. Recommend one option, but wait for my decision before treating it as approved.

After agreeing on requirements and any needed design, ask `plan`:

> Use plan to break this approved scope into ordered tasks. Include dependencies, completion criteria, verification, risks, and any decisions or approvals still needed. Keep the plan proportional to the change.

Small, clear changes may not need separate design or planning documents. Ask Guide to route to a smaller workflow when appropriate.

## 4. Implement with the right workflow

For a behavior change or bug fix, you can use `test-first`:

> Use test-first to define the expected behavior and an appropriate test before implementation. Show me the test and expected result. Then implement only the approved behavior.

When implementation is ready:

> Use implement to make the approved change. Follow the project conventions, preserve unrelated work, and run only the relevant authorized checks. Report files changed and actual check results.

## 5. Review and verify

For consequential changes, ask for a separate review:

> Use review to inspect this change against the approved requirements. Look for correctness issues, regressions, maintainability concerns, and missing coverage. Report findings with file and line references; do not edit anything during the review.

Use `shield` when security or safety risks matter:

> Use shield to assess the relevant trust boundaries, plausible threats, existing controls, and proportionate mitigations for this change.

Then use `verify` to check the outcome:

> Use verify to map each acceptance criterion to evidence. Run or inspect only checks that are safe and authorized. Distinguish passed, failed, blocked, inconclusive, and unchecked criteria. Do not claim the change works beyond the evidence.

Use `prove` if you need a traceable evidence package for a decision, handoff, or audit:

> Use prove to connect the important claims about this change to requirements and evidence. Show gaps, limits, and any claims the evidence cannot support.

## 6. Document, release, or hand off if needed

Use `document` to update relevant user or maintainer instructions from evidence. Use `release` only when preparing a real release, with the required readiness and authorization checks. Use `relay` when another person or agent must continue the work.

Do not treat a plan, review, verification, or handoff as permission to commit, push, deploy, or publish. Ask for and follow the required authorization for each consequential action.

## The short version

**Guide → Probe (if unclear) → Specify → Design (if needed) → Plan (if useful) → Test-First → Implement → Review / Shield (as relevant) → Verify → Prove, Document, Release, or Relay (as needed).** The user confirms requirements and consequential decisions along the way; evidence determines what can be claimed at the end.
