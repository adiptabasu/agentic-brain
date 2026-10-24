# Investigate and fix a bug

Use this when software, a test, integration, or workflow behaves differently from what you expect. Start with evidence; do not jump straight to a speculative fix.

## Describe and reproduce the symptom

Open the relevant repo as described in [provide a codebase](02-provide-a-codebase.md). Then invoke `debug`:

> Read `skills/debug/SKILL.md` and follow it. The observed problem is [symptom]. I expected [expected result] but got [actual result]. It occurs when [steps or conditions]. Relevant error/output: [small redacted excerpt]. First inspect the relevant files and existing Git changes, then help reproduce it. Do not edit files yet.

Include the environment and exact steps when they affect the result. Do not paste secrets or unrelated logs.

## Investigate before changing code

The Debug workflow should collect evidence, form competing hypotheses, and test them to isolate a cause. If the issue cannot yet be reproduced, ask:

> What evidence is missing to distinguish the leading hypotheses? Suggest the smallest safe diagnostic check. Do not claim a root cause until evidence supports it.

When the likely cause is established, ask for the minimal fix and regression check:

> Summarize the evidence for the root cause, the proposed smallest fix, possible side effects, and the test that would demonstrate the fix. Wait for my approval before implementing.

## Fix and verify

After you approve, route the change through `test-first` or `implement` as appropriate. Then use `verify`:

> Verify the original reproduction now behaves as expected and run the relevant regression checks. Report the actual command results and any untested cases. Do not claim the issue is fixed beyond those results.

If the evidence points to configuration, a service, or an external dependency rather than code, report the next responsible action instead of making unrelated changes.
