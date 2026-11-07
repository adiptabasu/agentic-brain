---
name: initialize
description: Prepare or troubleshoot canonical project skills for a named agent host using its verified project-level format.
---

# Initialize skills for an agent

Use when the user asks to prepare, sync, or troubleshoot Agentic Brain skills for a host. Canonical sources live in `skills/`; adapters map them to host discovery formats. Initialization copies existing skills; it does not author new skill content.

## Workflow

1. Identify the exact product. Ask if the host is unclear. Initialize only the selected host(s); do not sync every adapter unless asked.
2. Use the adapter in `adapters/README.md` if present. For a new host, verify project support, discovery path, manifest, supporting-file layout, and invocation in current official docs. Do not rely on third-party guidance or infer compatibility. Adapt the sync helper only from verified requirements, then update the adapter catalogue, relevant guide, evaluation, and indexes. If official docs are unclear, explain the gap and ask before writing host files.
3. Inspect canonical skills and the selected target. Preserve unrelated files. Run `python3 scripts/sync_skills.py --host <host>` to report missing, differing, or extra files; check mode is read-only.
4. If initialization is requested, use `--write` to copy missing files only. Preserve extras. Never overwrite a differing copy without explicit approval for the exact files and `--force`.
5. Recheck. Report the host, files copied or conflicted, invocation method, and whether UI discovery was observed. Do not claim UI discovery without observing it.

See [adapter documentation](../../adapters/README.md) for host paths and the process for adding hosts. Follow project approval and verification standards. Do not change global settings, install extensions, commit, push, publish, or deploy as part of initialization.
