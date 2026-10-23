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
| `analyze-logs` | Analyze log timelines, performance symptoms, outages, and timezones |
| `refine` | Improve software structure while preserving established behavior |
| `implement` | Execute approved implementation work and verify behavior |
| `review` | Review correctness, maintainability, and regressions |
| `shield` | Assess security and safety risks and recommend mitigations |
| `verify` | Verify outcomes against criteria and evidence |
| `prove` | Assemble traceable evidence for claims and conclusions |
| `relay` | Prepare context-preserving handoffs between people and workflows |
| `document` | Create and maintain evidence-based documentation |
| `release` | Prepare and assess releases with explicit readiness and authorization |
| `initialize` | Prepare Agentic Brain's repository skills for a supported agent environment |

This table lists the skills currently present in `skills/`. Their names and responsibilities may evolve as the framework is validated.

## Repository Layout

```text
agentic-brain/
├── skills/       # Canonical skill definitions and supporting resources
├── .agents/      # Codex-discoverable skill copies, generated from skills/
├── .claude/      # Claude Code skill copies, generated from skills/
├── .abacusai/    # Abacus AI Agent skill copies, generated from skills/
├── scripts/      # Skill synchronization helpers
├── standards/    # Shared protocols and conventions
├── adapters/     # Environment-specific discovery and installation support
├── tests/
│   ├── structure/
│   ├── behavior/
│   └── compatibility/
└── docs/         # Architecture, usage, and contributor documentation
```

The canonical skill source should be maintained in one place. Adapters should support environment-specific installation and discovery without silently changing a skill's meaning.

## Agent setup and skill shortcuts

Agentic Brain keeps canonical skills in `skills/`. `scripts/sync_skills.py` copies them into the selected agent's project discovery folder so they appear in that agent's skill picker.

| Agent | Project skill folder | Explicit invocation |
|---|---|---|
| Codex | `.agents/skills/` | Type `$` to select a skill, or use `/skills` |
| Claude Code | `.claude/skills/` | Type `/skill-name` |
| Abacus AI Agent | `.abacusai/skills/` | Type `/skill-name`; `/skills` lists and manages skills |

The `initialize` skill explains setup and troubleshooting for these adapters.

To check or populate a host's copies, use its name with the sync helper:

```sh
python3 scripts/sync_skills.py --host codex --write
python3 scripts/sync_skills.py --host claude --write
python3 scripts/sync_skills.py --host abacus --write
```

Use `--host all` to populate all three. Without `--write`, the script only checks the copies. It reports differing files and does not overwrite them unless `--force` is supplied. It never deletes files. Start a new session after adding skills; Codex detects changes automatically, and can be restarted if updated skills do not appear.

The copies under `.agents/skills/`, `.claude/skills/`, and `.abacusai/skills/` are generated outputs. Make changes under `skills/`, then synchronize them.

## Core Standards

- [Core Principles](standards/CORE-PRINCIPLES.md)
- [Handoff Contract](standards/HANDOFF-CONTRACT.md)
- [Verification Standard](standards/VERIFICATION.md)
- [Skill Authoring Template](standards/SKILL-TEMPLATE.md)

## Project Status

Early development. The repository contains shared standards and 18 canonical skills. Project skill folders and sync support are implemented for Codex, Claude Code, and Abacus AI Agent; UI behavior has not been validated in each host. Other compatibility targets still require validation.

No compatibility, installation, or behavioral claims should be made without corresponding validation evidence.

## Contributing

Contribution guidance, licensing, security reporting, and release procedures will be established before the project is considered ready for external contributions.

## Host documentation

- [Codex skills](https://learn.chatgpt.com/docs/build-skills)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Abacus AI Agent skills](https://abacus.ai/help/abacusai-desktop/agents-and-skills)

## License

Not yet selected. Do not assume that this project is licensed for reuse until a license has been explicitly chosen and added to the repository.
