# Set up Agentic Brain in an agent host

Use this after opening or cloning Agentic Brain when you want its canonical skills available as host-specific shortcuts. Host and model are separate choices; for example, Claude Code and Claude.ai are different environments.

## Identify the host

If `initialize` is available, invoke it. Otherwise say:

> Read `skills/initialize/SKILL.md` and follow it for this repository. I use [exact agent application and extension, if applicable]. My model is [model, if relevant]. Check the host's current official skill-discovery instructions and inspect this repo's canonical skills and existing copies. Report missing or differing files and the invocation method. Do not write files or change global settings yet.

If all you know is “VS Code,” tell the agent which assistant or extension you use. If the host is not one of the implemented adapters, the initializer should verify documentation and propose what is needed rather than inventing a folder.

## Review and approve the project setup

For Codex, Claude Code, and Abacus AI Agent, the repo documents project folders and provides `scripts/sync_skills.py`. Ask for a read-only check first:

> Run the synchronization helper in check mode for [codex / claude / abacus]. Show which copies are missing or differ from `skills/`. Do not use `--write` or `--force` yet.

Review the destination and any conflicts. If you approve adding missing copies, say:

> I approve writing missing canonical skills to [host project folder] in this repository. Do not overwrite differing files; report conflicts. Do not change global settings, initialize Git, commit, or push.

Use `--force` only after reviewing and agreeing to the exact differing files it would replace. The sync helper does not delete files.

## Verify actual discovery

After approved synchronization, ask:

> Recheck that the selected host copies match the canonical skills. Tell me what the files establish and what remains to check in the host UI. Do not claim shortcut discovery unless it is visible in the actual host.

Follow the host's current refresh or restart instructions if needed, then check its skill picker or command menu. If shortcuts are unavailable, you can still ask the agent to read a canonical file such as `skills/probe/SKILL.md` and follow it. File synchronization alone does not prove UI availability.
