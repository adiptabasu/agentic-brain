# Canonical skills

This directory is the single editable source for Agentic Brain skills. Each skill lives in `skills/<name>/` and requires a `SKILL.md` with `name` and `description` front matter. Add optional `scripts/`, `references/`, `assets/`, or `agents/` resources only when the skill needs them.

Load only the skill selected for the task and the references it needs; this catalogue is not a request to read every skill.

## Current skills

- [initialize](initialize/SKILL.md) — check or prepare a selected agent host's project-level skill discovery folder.
- [write-document](write-document/SKILL.md) — draft or revise detailed software and operational documents, and compose clear commit messages from reviewed changes.
- [cheapaioutput](cheapaioutput/SKILL.md) — toggle concise wording for chat replies; use `write-document` for commit messages and local prose.
- [session](session/SKILL.md) — start, pause, resume, complete, and safely terminate multi-chat work sessions.
- [plan](plan/SKILL.md) — create persona-informed session plans and consolidate them into one session-local `PLAN.md` with `plan finish`.
- [define-testcases](define-testcases/SKILL.md) — map a completed plan to manual eval scenarios and applicable executable tests before implementation.
- [develop-to-green](develop-to-green/SKILL.md) — implement an approved plan and iterate until its evals and applicable unit tests pass.
- [create-scaffolding](create-scaffolding/SKILL.md) — create an evidence-based project scaffold and reusable template from a reference project.
- [project-destination](project-destination/SKILL.md) — collect and validate the exact project-folder path before scaffolding.
- [read-initialize-project](read-initialize-project/SKILL.md) — create or refresh a root-level project context guide while preserving manual notes.
- [start-support-issue](start-support-issue/SKILL.md) — start or resume a local support case with a durable, redacted issue record.
- [client-response](client-response/SKILL.md) — draft a copy-ready client message followed by a separate internal logic section.

Host-specific copies are generated in the directories listed under `adapters/` (currently Codex, Claude Code, Abacus AI Agent, and Cursor). The initialize workflow can add another host after verifying its current official project-skill documentation. Do not edit generated copies directly. After editing a canonical skill, synchronize it with `scripts/sync_skills.py` and recheck the result.

Use the [Skill Template](../standards/SKILL-TEMPLATE.md) when authoring another skill. Read [Initialize Agentic Brain for an agent](initialize/SKILL.md) when the canonical skill needs to be made available to a host.
