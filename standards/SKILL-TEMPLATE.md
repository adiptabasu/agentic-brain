# Skill Template

Create each canonical skill under `skills/<name>/SKILL.md`.

```markdown
---
name: skill-name
description: Explain the task this skill performs and when it should be selected.
---

# Skill title

State the purpose and relevant boundaries.

## Workflow

Describe only the steps that improve the outcome for this task.

## Completion

State the expected output and what must be reported as incomplete or unverified.
```

Keep the description concise and discriminating. Add `scripts/`, `references/`, `assets/`, or `agents/` only when needed. See the [Skill Creator](https://learn.chatgpt.com/docs/build-skills) guidance for the current Codex skill format.
