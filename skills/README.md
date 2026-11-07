# Canonical skills

This directory is the single editable source for Agentic Brain skills. Each skill lives in `skills/<name>/` and requires a `SKILL.md` with `name` and `description` front matter. Add optional `scripts/`, `references/`, `assets/`, or `agents/` resources only when the skill needs them.

## Current skills

- [initialize](initialize/SKILL.md) — check or prepare a selected agent host's project-level skill discovery folder.
- [write-document](write-document/SKILL.md) — draft or revise detailed software and operational documents, and compose clear commit messages from reviewed changes.
- [cheapaioutput](cheapaioutput/SKILL.md) — toggle concise wording for chat replies; use `write-document` for commit messages and local prose.

Host-specific copies are generated in the directories listed under `adapters/` (currently Codex, Claude Code, Abacus AI Agent, and Cursor). The initialize workflow can add another host after verifying its current official project-skill documentation. Do not edit generated copies directly. After editing a canonical skill, synchronize it with `scripts/sync_skills.py` and recheck the result.

Use the [Skill Template](../standards/SKILL-TEMPLATE.md) when authoring another skill. Read [Initialize Agentic Brain for an agent](initialize/SKILL.md) when the canonical skill needs to be made available to a host.
