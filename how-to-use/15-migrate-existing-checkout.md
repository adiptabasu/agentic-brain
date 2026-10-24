# Migrate an older checkout to generated host folders

Use this when your existing Agentic Brain checkout contains tracked `.agents/`, `.claude/`, or `.abacusai/` skill copies. The current setup keeps canonical skills in `skills/`; host-specific copies are generated locally by initialization and ignored by Git.

## 1. Check and preserve local work before pulling

Before updating, inspect the current repo and branch. Ask the agent:

> Read `skills/initialize/SKILL.md` and follow it. This is an older Agentic Brain checkout. Inspect the Git status and compare any local changes in `.agents/`, `.claude/`, or `.abacusai/` against the canonical files under `skills/`. Do not discard, overwrite, reset, or pull anything yet. Tell me whether I have custom changes that need to be preserved.

If you customized a host copy, decide whether that customization belongs in the canonical source. Preserve it in the appropriate `skills/<name>/SKILL.md` or another deliberate file before updating. Do not treat generated copies as independent sources of truth. Back up or commit any unrelated local work using your normal Git policy.

If the working tree is not clean or Git reports that local changes would be overwritten, stop and resolve how to preserve those changes first. Do not use a hard reset or force operation as a shortcut.

## 2. Pull the repository update

Once your local work is safely preserved, update the same branch from its configured remote:

> My local work is preserved and the intended branch is [branch]. Update this checkout from its configured remote. Do not change the remote, switch branches, or discard local changes. Stop and show me any conflict.

The update removes the old tracked host copies from a clean checkout. It should retain your canonical files in `skills/`. Confirm the branch and status afterward. If a merge conflict occurs, preserve the conflict and review it rather than forcing a resolution.

## 3. Recreate only the host copies you use

Run the `initialize` skill and identify the exact application, not just the model. Ask it to check the selected host first:

> Use `skills/initialize/SKILL.md` to set up [Codex / Claude Code / Abacus AI Agent] for this repository. Verify the current official discovery path and invocation. Run `python3 scripts/sync_skills.py --host [codex|claude|abacus]` in check mode and show the missing or differing copies. Do not write or overwrite files yet.

Missing copies are expected after this migration. Review the target path and approve generation for the host you selected:

> I approve creating missing skill copies for [host] in its project folder from the canonical `skills/` files. Do not overwrite differing copies; report conflicts. Do not change global settings or perform Git actions.

After approving one host, the initializer can then run the matching command:

```sh
python3 scripts/sync_skills.py --host codex --write
python3 scripts/sync_skills.py --host claude --write
python3 scripts/sync_skills.py --host abacus --write
```

Run only the command for the host you selected.

Use `--host all` only if you want all supported host copies on this machine. Differing files remain conflicts unless you review and specifically approve an overwrite with `--force`. The sync script never deletes files.

## 4. Check the new setup

Ask the agent to run the selected host's sync check again and explain the result. The generated folders are ignored by Git, so local setup does not add those copies back to the repository. Confirm shortcuts in the actual agent UI; files on disk alone do not prove that they are discoverable.

For a new clone, skip the migration and go directly to [agent initialization](13-initialize-an-agent.md). For the repository's general policy, see the [README setup section](../README.md).
