# Manual skill evaluations

These cases help reviewers check whether important skills activate for suitable requests, stay out of unrelated requests, and follow their core behavior. They are manual evaluation prompts, not automated tests; no runner or CI enforcement is currently provided.

## Running a case

1. Use a clean, isolated copy of the repository and an agent host where the skill is available.
2. Run a positive trigger and confirm the intended skill is selected or followed. Run a negative trigger and confirm the skill is not inappropriately selected; an appropriate alternative may be suggested.
3. Run the behavioral scenario with the skill available. Compare the response and any generated artifacts with every pass criterion in the case.
4. Record the skill revision, host/runtime, prompt, observed outcome, and any limitations in the change review. Do not report a case as passed unless it was actually run and reviewed.

Use synthetic or redacted inputs. Behavioral cases may authorize file creation inside the isolated evaluation copy; do not point them at real incident data or production systems.

When a covered skill changes, update its case if the expected behavior or routing has changed. Add cases for other skills when their risk or expected behavior makes manual evaluation useful. These cases are examples of important behaviors, not proof that a skill works in every host or situation.

## Current coverage
- [Analyze Logs](cases/analyze-logs.json)
- [Create Document](cases/create-document.json)
- [Debug](cases/debug.json)
- [Document](cases/document.json)
- [Guide](cases/guide.json)
- [Initialize](cases/initialize.json)
- [Release](cases/release.json)
- [Repository integration](cases/repository-integration.json)
- [Shield](cases/shield.json)
- [Verify](cases/verify.json)
- [Writing](cases/writing.json)
