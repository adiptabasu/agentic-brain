# Skill Host Adapters

Each `*.json` file defines one verified host adapter for `scripts/sync_skills.py`. An adapter records the host ID, project-level discovery directory, official documentation URL, and invocation guidance.

## Implemented adapters

| Agent host | Adapter | Project discovery directory |
|---|---|---|
| [Codex](https://learn.chatgpt.com/docs/build-skills) | [codex](codex.json) | `.agents/skills/` |
| [Claude Code](https://code.claude.com/docs/en/skills) | [claude-code](claude-code.json) | `.claude/skills/` |
| [Abacus AI Agent](https://api.abacus.ai/help/abacusai-desktop/skills) | [abacusai](abacusai.json) | `.abacusai/skills/` |
| [Cursor](https://cursor.com/docs/skills) | [cursor](cursor.json) | `.cursor/skills/` |

The `claude-code` adapter is for Claude Code. Claude.ai custom skills use an account-level upload flow, not a project-local discovery directory, so they are outside this sync helper.

## Supporting another host

The four adapters above are the currently implemented hosts, not a limit. When asked to initialize a different host, research that exact product's current official documentation online. Verify project-level skill support, its discovery directory, manifest filename and required fields, supporting-file layout, and invocation method. Distinguish products from the same vendor when they use different discovery mechanisms. Do not infer compatibility from a model name, third-party guidance, or another host's conventions.

If the documented format uses the canonical `SKILL.md` layout, add an adapter JSON with the verified discovery directory, official documentation URL, and invocation guidance. If its manifest or file layout differs, update the sync helper to emit the host's required files from canonical sources, and document the mapping and limitations. Add a manual evaluation case for the host and update the relevant indexes and how-to. If official sources do not establish the format clearly, report the gap and ask before writing host-specific files. Add support only for the host the user requested; do not initialize every adapter by default.
