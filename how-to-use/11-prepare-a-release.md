# Assess and prepare a release

Use this when deciding whether a software version is ready to publish or deploy. A release assessment does not itself authorize publication or deployment.

## Request a readiness assessment

Identify the candidate version or commit, target environment, intended release date, and relevant requirements. Then invoke `release`:

> Read `skills/release/SKILL.md` and follow it. Assess readiness for [version/commit] to [target]. Inspect available requirements, change list, verification evidence, dependencies, artifact provenance, operational risks, and rollback options. First report what is ready, blocked, failed, or unknown. Do not publish or deploy anything.

If there are required checks or approvers, name them. Do not assume a passing unit test is sufficient evidence for the full release.

## Resolve gaps and prepare release materials

Ask for an actionable readiness list:

> Map each release criterion to the evidence available and the missing check or approval. Identify risky changes, compatibility or migration concerns, monitoring and rollback needs, and who must decide any unresolved item. Do not invent approval or completion evidence.

After gaps are resolved, request release notes based on the actual changes:

> Draft release notes for [version] from the verified changes. Separate user-visible changes, fixes, known limitations, and migration instructions. Flag anything that cannot be confirmed.

## Authorize publication separately

Review the final artifact, destination, version, and rollback plan. If you intend the agent to publish or deploy, explicitly state the action and target:

> I authorize publishing [specific artifact/version] to [destination]. Confirm the exact action and any remaining risk before proceeding. Do not deploy to another environment or publish additional artifacts.

Afterward, use `verify` to establish what actually happened. Distinguish a request being accepted from the release being live and healthy. For a release decision or audit, use `prove` to assemble traceable readiness evidence.
