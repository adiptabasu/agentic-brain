# Optional release deliverable structures

Read when the user requests a detailed readiness report, release plan, release notes, release record, recovery report, or evidence package.

## 6. Deliverable Structure

Choose the smallest deliverable that adequately serves the request.

### 6.1 Release readiness report

A readiness report should contain:

1. Release identity.
2. Intended outcome.
3. Candidate and source revision.
4. Scope summary.
5. Applicable release criteria.
6. Evidence reviewed.
7. Readiness matrix.
8. Blockers.
9. Known issues and residual risks.
10. Approval status.
11. Recommended next action.
12. Evidence limitations.

A compact report may omit empty sections, but it must not omit material blockers or approval requirements.

### 6.2 Release plan

A release plan should contain:

1. Objective and scope.
2. Candidate identity.
3. Preconditions.
4. Ordered execution steps.
5. Responsible roles.
6. Approval gates.
7. Expected results.
8. Evidence capture.
9. Failure handling.
10. Rollback or recovery.
11. Post-release checks.
12. Completion criteria.

Clearly label unapproved steps and proposed decisions.

### 6.3 Release notes

A release note should contain the applicable elements:

- Product and version.
- Release date, if confirmed.
- Summary.
- New functionality.
- Changes and fixes.
- Breaking changes.
- Deprecations or removals.
- Security information suitable for the audience.
- Upgrade or migration instructions.
- Known issues.
- Compatibility information.
- Required user action.
- Relevant references.

Do not invent dates, versions, fixes, or compatibility claims.

If an item is not verified, omit it or label it appropriately.

### 6.4 Release record

A release record should capture:

- Release identifier.
- Candidate revision.
- Artifact identity.
- Scope.
- Readiness decision.
- Required approvals.
- Execution record.
- Publication or deployment result.
- Verification evidence.
- Known limitations.
- Recovery actions, if any.
- Final status.
- Follow-up actions.

Keep the record proportionate to the release's risk and the project's audit requirements.

### 6.5 Recovery report

A recovery report should include:

- Observed failure.
- Evidence and time of observation, where known.
- Known or suspected impact.
- Immediate containment.
- Recovery decision and authority.
- Actions attempted.
- Confirmed outcomes.
- Remaining risk.
- Current system or publication status.
- Required follow-up.

Separate observed facts from hypotheses.

### 6.6 Evidence references

Prefer references to authoritative records over unsupported narrative claims.

Where available, include:

- CI run identifiers.
- Test report references.
- Review records.
- Source commit identifiers.
- Artifact digests.
- Registry locations.
- Deployment identifiers.
- Health-check results.
- Approval records.
- Monitoring or incident records.

Do not expose credentials or confidential data in evidence references.
