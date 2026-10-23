# Agentic Brain

A vendor-independent framework of composable agent skills for collaborative reasoning, software engineering, execution, and evidence-based verification.

## Guiding Principle

**Clarify, Don't Assume.**

Agentic Brain must establish shared understanding rather than silently guess the user's intent, requirements, constraints, or approval.

When uncertainty could materially affect the outcome, a skill must ask focused questions and resolve the uncertainty before proceeding. Nonessential unknowns may remain explicitly unresolved when work can safely continue without them.

## Goals

- Provide portable, independently useful, composable agent skills.
- Support explicit skill invocation and context-aware skill recommendations.
- Establish shared conventions for decisions, approvals, handoffs, and evidence.
- Adapt planning and project state to task complexity and risk.
- Make verification claims traceable to actual evidence.
- Support multiple agent environments without requiring proprietary APIs.
- Expand beyond software engineering over time.

## Initial Compatibility Targets

- Generic Agent Skills-compatible agents
- GitHub Copilot
- Cursor
- Claude Code
- Codex
- Abacus

Compatibility must be validated and reported per environment. Listing an environment as a target does not mean it has already been tested.

## Current Skills

| Skill | Responsibility |
|---|---|
| `guide` | Teach, orient, and recommend appropriate skills or workflows |
| `probe` | Clarify requirements, challenge assumptions, and resolve decisions |
| `test-first` | Drive development through a test-first workflow |
| `specify` | Turn agreed requirements into testable specifications |
| `design` | Evaluate architecture and consequential technical choices |
| `plan` | Organize implementation into ordered, actionable tasks |
| `debug` | Investigate failures and verify root-cause fixes |
| `implement` | Execute approved implementation work and verify behavior |
| `review` | Review correctness, maintainability, and regressions |
| `verify` | Verify outcomes against criteria and evidence |
| `document` | Create and maintain evidence-based documentation |
| `release` | Prepare and assess releases with explicit readiness and authorization |

This table lists the skills currently present in `skills/`. Their names and responsibilities may evolve as the framework is validated.

## Repository Layout

```text
agentic-brain/
├── skills/       # Canonical skill definitions and supporting resources
├── standards/    # Shared protocols and conventions
├── adapters/     # Environment-specific discovery and installation support
├── tests/
│   ├── structure/
│   ├── behavior/
│   └── compatibility/
└── docs/         # Architecture, usage, and contributor documentation
```

The canonical skill source should be maintained in one place. Adapters should support environment-specific installation and discovery without silently changing a skill's meaning.

## Core Standards

- [Core Principles](standards/CORE-PRINCIPLES.md)
- [Handoff Contract](standards/HANDOFF-CONTRACT.md)
- [Verification Standard](standards/VERIFICATION.md)
- [Skill Authoring Template](standards/SKILL-TEMPLATE.md)

## Project Status

Early development. The repository contains shared standards and an initial set of 12 skills. Compatibility, installation, and behavior across target environments still require validation.

No compatibility, installation, or behavioral claims should be made without corresponding validation evidence.

## Contributing

Contribution guidance, licensing, security reporting, and release procedures will be established before the project is considered ready for external contributions.

## License

Not yet selected. Do not assume that this project is licensed for reuse until a license has been explicitly chosen and added to the repository.
