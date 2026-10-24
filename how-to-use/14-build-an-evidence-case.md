# Assemble evidence for an important claim

Use this when a decision, review, audit, or handoff needs a traceable case connecting a claim to requirements and evidence. `prove` organizes evidence; it does not make weak evidence stronger or replace `verify`.

State the claim and intended decision, then invoke `prove`:

> Read `skills/prove/SKILL.md` and follow it. Assess this claim: [claim]. It will support [decision, handoff, or review]. Use these criteria: [requirements or decision criteria]. Inspect only these sources or artifacts: [paths, reports, test results, versions]. Build an evidence map that shows what supports each part, what contradicts it, and what remains unknown. Do not infer approval or claim more than the sources establish.

For a release claim, for example:

> Claim: release candidate [version] satisfies the agreed readiness criteria. Use the criteria in [path] and the verification report at [path]. Check which criteria have direct evidence, identify stale or missing evidence, and state what must be checked before approval.

Review the evidence map. Confirm that references point to the correct versions and that each source actually supports the linked claim. Ask:

> Separate direct observations from interpretations. For each gap, say what evidence would close it and who or what must provide it. Keep contradictory evidence visible.

Use `verify` when you need to run or assess checks against acceptance criteria. Use `review` for an independent assessment of a code change. The evidence package can inform a decision, but it does not itself approve the decision or authorize release, deployment, or publication.
