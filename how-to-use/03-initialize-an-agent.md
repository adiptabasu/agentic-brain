# Initialize skills for an agent

Canonical skill sources live under `skills/<name>/SKILL.md`. A host adapter maps them to the selected agent's project-level discovery folder. Current adapters are Codex (`.agents/skills/`), Claude Code (`.claude/skills/`), Abacus AI Agent (`.abacusai/skills/`), and Cursor (`.cursor/skills/`).

## Initialize for Codex

If the `initialize` skill is already available, invoke it and name the host:

> Initialize this project for Codex. Check the canonical `skills/` tree, report missing or differing copies, and copy missing files into `.agents/skills/`. Do not overwrite conflicts. Recheck afterward and tell me whether UI discovery was actually verified.

If the skill is not yet available in the host, use the canonical file directly:

> Read `skills/initialize/SKILL.md` and follow it. Initialize this project for Codex, using only the documented Codex adapter.

The helper checks by default and creates missing copies only with `--write`:

```sh
python3 scripts/sync_skills.py --host codex
python3 scripts/sync_skills.py --host codex --write
```

Different existing copies are reported as conflicts; the helper does not overwrite them unless `--force` is used. Review each conflicting file and obtain explicit approval before replacing it. The helper never deletes extra files.

## Initialize for another supported host

Replace `codex` with the chosen adapter ID:

```sh
python3 scripts/sync_skills.py --host claude-code
python3 scripts/sync_skills.py --host abacusai
python3 scripts/sync_skills.py --host cursor
```

For example, to initialize Claude Code, first check and then populate only its project folder:

> Read `skills/initialize/SKILL.md` and follow it. Initialize this project for Claude Code. Check `.claude/skills/`, report conflicts, copy only missing files, and recheck. Do not initialize other hosts.

Claude.ai custom skills use a separate account upload flow and are not part of these filesystem adapters. Do not treat Claude Code's `.claude/skills/` directory as a Claude.ai upload.

## Add another agent host

Name the exact application and extension, not just the model or vendor. If it is outside the four current adapters, check online for that exact product's current official documentation. Confirm project-level skill support, discovery path, manifest format and required fields, supporting-file conventions, and invocation method.

If the documented format uses the canonical `SKILL.md` layout, add a verified adapter in `adapters/`. If it uses a different manifest or file layout, extend the sync helper to generate the required host files from canonical sources and document that mapping. Update the adapter catalogue, evaluation case, and relevant indexes. Keep canonical sources in `skills/`. If official documentation does not clearly establish the format, describe the uncertainty and ask before writing host-specific files. Initialize only the requested host, preserve existing user files, and do not claim host UI discovery without observing it.
