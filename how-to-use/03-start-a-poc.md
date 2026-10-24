# Start a proof of concept from scratch

Use this when you have an idea to explore and want to validate it through a small working prototype. Decide whether the POC is throwaway or may become a product foundation; that affects stack and structure choices.

## 1. Explain the idea and constraints

Start with `probe` or `guide`:

> Use probe to help me define a proof of concept for [idea]. Ask about the user or problem, the smallest outcome that would prove or disprove the idea, constraints, deadline, skills, budget, and where it needs to run. Do not choose a technology stack or write code yet.

Clarify your goal and what result would count as success. If this is only to test feasibility, say so; avoid letting a POC silently grow into a complete product.

## 2. Compare stack options before choosing

Once the goal and constraints are clear, ask `design`:

> Use design to recommend a practical stack for this POC. Compare a small number of viable options against my requirements, experience, deployment target, cost, ecosystem, and the possibility that the prototype may or may not be kept. Check current official documentation where version or support details matter. Explain trade-offs and what remains unknown. Recommend a stack, but wait for me to choose.

If you are learning a particular technology, say so; otherwise the agent should not assume that using the newest or most complex stack is a goal. Review the recommendation and decide:

> I choose [stack]. Use [specific versions or services if agreed]. Keep the POC limited to [scope]. Do not add production infrastructure or optional features unless I approve them.

If none of the options fit, ask for another comparison or change your constraints before proceeding.

## 3. Define the first vertical slice

Ask `specify` to write a minimal, testable specification:

> Use specify to define the smallest end-to-end POC behavior that will test the core idea. Include acceptance criteria, explicit non-goals, and what result would count as a useful validation. Keep proposed features separate from the agreed scope.

Approve or correct the acceptance criteria. Then use `plan`:

> Use plan to break the approved POC into small, ordered slices. Start with a runnable skeleton and the smallest end-to-end behavior. For each slice, define a completion check and identify any unresolved dependency. Keep setup proportional to the POC.

## 4. Develop incrementally

For each slice, use `test-first` when behavior can be expressed as a useful test, then `implement`:

> Work only on the first approved slice. Define and run its relevant check, implement the smallest change, and report the actual result. Don't begin later slices until I review this one.

Review each result. If the slice disproves an assumption, use `probe` or `design` to reconsider the decision before continuing. Keep a short record of what was learned and what the next experiment should test.

## 5. Decide what the POC proved

At the agreed stopping point, use `verify`:

> Use verify to check the POC acceptance criteria against evidence from the implementation and checks. State what the POC demonstrated, what it did not establish, and any failed or inconclusive criteria. Do not describe it as production-ready unless that was separately assessed.

Then decide whether to discard it, run another experiment, or plan a production-quality implementation. If keeping it, ask for a review of security, reliability, and maintainability gaps before treating it as a foundation. Git initialization, commits, pushes, or deployment are separate actions that require their own authorization.
