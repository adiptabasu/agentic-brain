# Agentic Brain

A clean rebuild of Agentic Brain. Product scope, architecture, and project workflows will be established as this version develops.

The previous project version is preserved separately for reference.

## Get the project

Clone the repository with Git:

```sh
git clone https://github.com/adiptabasu/agentic-brain.git
cd agentic-brain
```

Or download and extract the latest `main` branch ZIP (without Git history):

```sh
curl -L https://github.com/adiptabasu/agentic-brain/archive/refs/heads/main.zip -o agentic-brain.zip
unzip agentic-brain.zip
cd agentic-brain-main
```

## Initialize for an AI host

Copy this prompt into your AI coding agent and replace `<AI HOST>` with the exact product, such as `Codex`, `Claude Code`, `Abacus AI Agent`, or `Cursor`:

> Read `skills/initialize/SKILL.md` and follow it. Initialize this project for `<AI HOST>`. Check the canonical `skills/` tree, report missing or differing copies, and copy only missing files for the selected host. If the host is not listed in `adapters/`, research its current official documentation and follow the initialize skill's process for adding support. Preserve conflicts and unrelated files, recheck afterward, and report whether skill discovery was verified in the host UI. Do not initialize other hosts.

## Skills

Canonical skill sources live in [`skills/`](skills/README.md). The [`initialize` skill](skills/initialize/SKILL.md) checks or prepares host-specific discovery folders using documented adapters. Current adapters support Codex, Claude Code, Abacus AI Agent, and Cursor. The [`write-document` skill](skills/write-document/SKILL.md) drafts or revises local software and operational documents and composes commit messages from reviewed changes, with relevant persona viewpoints when useful. The [`cheapaioutput` skill](skills/cheapaioutput/SKILL.md) shapes concise chat replies only. Use `write-document` or the appropriate implementation skill for local file content. Use canonical sources as the only editable copy and regenerate host copies when they change.

## Personas

Personas provide focused viewpoints for software development work; they do not grant permissions or replace repeatable skills. The initial profiles cover requirements analysis, software architecture, security architecture, implementation, independent review and test strategy, technical writing and knowledge curation, SRE, and DevOps. See the [persona catalogue](personas/README.md).

## Main operating rules

- Follow [AGENTS.md](AGENTS.md) and the applicable project standards. Ask when material details are unclear, honor approval and trust boundaries, and report only verified outcomes.

See [Core Principles](standards/CORE-PRINCIPLES.md), [Cloud Access Rules](standards/CLOUD-PLATFORM-ACCESS.md), [Local Change Approval Rules](standards/LOCAL-CHANGE-APPROVAL.md), [Version Control Approval Rules](standards/VERSION-CONTROL-APPROVAL.md), and the [Verification Standard](standards/VERIFICATION.md). The [operating rules guide](how-to-use/01-operating-rules.md) gives copy-ready prompts. Manual behavior checks are listed in [evaluations](evaluations/README.md).

For a quick setup walkthrough, see [Initialize skills for an agent](how-to-use/03-initialize-an-agent.md).
