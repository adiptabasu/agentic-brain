# Optional documentation deliverable structures

Read only when the requested document needs a specialized structure such as an API reference, architecture description, runbook, decision record, or handoff.

## 6. Documentation Deliverable Structure

Choose the deliverable structure based on the artifact type and audience.

### 6.1 General document

A useful default structure is:

1. **Title** — Identifies the subject.
2. **Purpose** — Explains why the document exists.
3. **Scope** — Establishes what is and is not covered.
4. **Context** — Provides necessary background.
5. **Main content** — Explains the relevant concepts, instructions, or decisions.
6. **Constraints and limitations** — Makes important boundaries explicit.
7. **References** — Points to authoritative related material.
8. **Next steps** — Identifies actions that remain, when relevant.

Not every document needs all eight sections.

### 6.2 README

A README should quickly answer:

- What is this project?
- Who is it for?
- What does it do?
- What prerequisites are needed?
- How can someone get started?
- How is it used or configured?
- How can it be tested or developed?
- Where can readers find further information?
- What license applies, if one has been confirmed?

Prioritize the first successful user journey. Put detailed reference material in dedicated documents when that improves readability.

Do not invent a license, project maturity level, compatibility guarantee, or feature claim.

### 6.3 Architecture documentation

Describe the system at the level needed to understand its structure and important trade-offs.

Depending on the system, include:

- System boundaries.
- Components and responsibilities.
- Interfaces and dependencies.
- Data flows.
- Trust boundaries and security considerations.
- Failure modes.
- Scaling or performance constraints when supported by evidence.
- Approved decisions and rejected alternatives.
- Known limitations and unresolved design questions.

Distinguish actual architecture from intended or proposed architecture.

### 6.4 API documentation

Document only established interfaces.

Include relevant information such as:

- Operation or endpoint.
- Supported method and parameters.
- Request and response formats.
- Authentication and authorization behavior.
- Error responses.
- Validation rules.
- Examples.
- Versioning and deprecation information.

Prefer generated references or authoritative schemas where available.

If implementation and specification disagree, report the discrepancy. Do not silently document one as if the conflict does not exist.

### 6.5 Operational runbook

Operational documentation must be especially careful about risk.

Include:

- Intended purpose.
- Preconditions and required permissions.
- Environmental assumptions.
- Safe inspection steps.
- Execution steps.
- Expected observations.
- Failure handling.
- Escalation criteria.
- Recovery or rollback instructions when established.
- Explicit warnings about destructive or irreversible actions.

Do not invent rollback commands or recommend production changes without an adequate basis and appropriate authorization.

### 6.6 Decision record

A decision record should make it possible for a future reader to understand both the choice and its context.

Record:

- Decision title and date, when known.
- Status: proposed, accepted, rejected, superseded, or another clearly defined state.
- Context and constraints.
- Considered options.
- Decision and rationale.
- Consequences and trade-offs.
- Related decisions.
- Open questions or review triggers.

Use only statuses supported by the actual decision process.

### 6.7 Agent handoff document

When the goal is to continue work across agents or sessions, preserve operationally relevant context.

Include:

- Goal and current scope.
- Confirmed requirements.
- Decisions and rationale.
- Relevant artifacts and their locations.
- Work completed and evidence collected.
- Failures, limitations, and unresolved questions.
- Dependencies and blockers.
- Next recommended actions.
- Required permissions or approvals.

Separate observed state from proposed next steps. A handoff must not imply that a suggested action has already been performed.
