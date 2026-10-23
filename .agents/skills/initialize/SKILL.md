---
name: initialize
description: Prepare Agentic Brain skills for a supported AI agent and diagnose missing skill shortcuts. Use when onboarding this repository to an agent or when its skill commands do not appear.
---

# Initialize Agentic Brain for an agent

**Version:** 0.1.0
**Status:** Draft

## Purpose

Make the repository's canonical skills available through the selected agent's documented project-skill discovery mechanism.

## Boundaries

- Canonical skill sources live in `skills/<name>/SKILL.md`.
- Implemented project adapters are Codex (`.agents/skills/`), Claude Code (`.claude/skills/`), and Abacus AI Agent (`.abacusai/skills/`), synchronized by `scripts/sync_skills.py`.
- Claude.ai custom skill uploads and other Claude surfaces are separate from Claude Code project skills. Do not treat a filesystem copy as an upload to those services.
- Other agent hosts require a verified adapter and current official documentation before files or settings are added.
- Do not change global agent configuration, install extensions, delete files, initialize Git, commit, or push as part of initialization unless separately authorized.

## Workflow

1. Confirm the target agent application when it is not already clear. A model name alone does not identify the host; distinguish Claude Code from Claude.ai and Abacus AI Agent from other Abacus products.
2. Inspect the repository instructions, README, canonical `skills/` tree, and any existing host-specific files. Preserve unrelated work.
3. Verify the selected host's current official skill-discovery path and invocation method:
   - Codex: `.agents/skills/`; use `$` or `/skills`.
   - Claude Code: `.claude/skills/`; use `/skill-name`.
   - Abacus AI Agent: `.abacusai/skills/`; use `/skill-name` or `/skills`.
4. Run `python3 scripts/sync_skills.py --host <codex|claude|abacus>` in check mode. Report missing and differing copies before writing. Review differing files; do not use `--force` without agreement to replace them.
5. After the user authorizes populating the selected discovery folder, run `python3 scripts/sync_skills.py --host <host> --write`. Recheck with the script in check mode. Use `--host all` only when the user wants all three copies populated.
6. Explain how to invoke the skills in the selected host. Do not claim that shortcuts are visible in the UI unless that was observed. Start a new session after adding skills; restart Codex if it does not show updated skills.
7. For a host without an implemented adapter, report what its official documentation confirms and propose the smallest adapter change before modifying files.

## Completion

Report the host, files created or updated, check results, and whether the host UI was actually verified. Distinguish repository setup from verified autocomplete behavior.
