---
name: initialize
description: Prepare or troubleshoot this project's canonical skills for a named agent host, using its verified project-level discovery format.
---

# Initialize Agentic Brain skills for an agent

Use this skill when the user asks to initialize, prepare, sync, or troubleshoot Agentic Brain skills for a specific agent host.

## Scope and structure

- Canonical, editable skill sources live in `skills/<name>/SKILL.md` with their supporting files.
- A host adapter maps a named agent product to its documented project-level skill format and discovery directory. Current adapters are Codex, Claude Code, Abacus AI Agent, and Cursor; see `adapters/`.
- Generated copies are created only for the selected host. Do not edit them independently or change global agent settings.
- Initialization makes existing canonical skills discoverable; it does not invent or author new skill content.

## Workflow

1. Identify the exact agent host and product. If the user did not name one, ask. A model name alone does not identify a host; distinguish products with different discovery behavior. In particular, `claude-code` means Claude Code, not Claude.ai.
2. Read the repository instructions and `adapters/README.md`. If an adapter exists, use it. If the host is unsupported, research its current official documentation online before proceeding. Verify that the exact product supports project-level skills, the discovery path, manifest format and required fields, supporting-file conventions, and invocation method. Do not rely on third-party posts or infer paths from another product.
3. If official documentation confirms a compatible project-level format, add a host-specific adapter under `adapters/` with the verified path, documentation URL, and invocation guidance. If its manifest or file layout differs from the canonical `SKILL.md` structure, update `scripts/sync_skills.py` to translate or emit the required format without changing canonical sources. Document any limits. Update the adapter catalogue, relevant how-to, evaluation case, and indexes as needed. If documentation is missing or ambiguous, explain what could not be verified and ask before creating host files.
4. Inspect `skills/` and the selected discovery directory. Preserve unrelated files and user changes. Confirm each canonical skill has one `SKILL.md` and any supporting resources are inside its skill folder.
5. Run the sync helper in check mode: `python3 scripts/sync_skills.py --host <host>`. Report missing files and conflicts before writing. Check mode is read-only.
6. If the user clearly requested initialization for the named host, run the sync helper in write mode to create the discovery folder and copy missing canonical files. This does not overwrite differing files or delete extras. If a differing copy needs replacement, identify the exact files and ask for explicit yes/no approval before forcing an overwrite.
7. Re-run check mode and report the host, created or conflicting files, and observed result. Explain the host's invocation method from its adapter documentation. Do not claim that the skill picker or implicit invocation works unless that was observed in the host UI.

Do not initialize all adapters unless the user specifically asks for all. Do not install extensions, change global settings, initialize Git, commit, push, publish, or deploy as part of this workflow.

## Completion

Report which host was selected, which canonical skills were synchronized, any conflicts or skipped files, check results, and whether UI discovery was actually verified. Keep those outcomes distinct.
