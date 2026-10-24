# Point Agentic Brain at a codebase or repository

Before asking for code work, make it clear which repository and state the agent should inspect. Opening the project in the agent's workspace is usually the most direct way to provide local files.

## If the repository is local

Open the repository root in the agent application. Then say:

> The repository for this task is the currently open workspace at [absolute path, if needed]. Work only in this repository. First read its `AGENTS.md`, README, and relevant project instructions; inspect the Git branch and working-tree status. Then inspect only files relevant to [task]. Do not edit anything until you summarize what you found and confirm the intended scope.

If there are multiple folders or nested repositories, identify the exact root and subproject. For example:

> Use `/path/to/monorepo/packages/api` as the target subproject, but check the repository root instructions and status at `/path/to/monorepo` first.

Do not assume that a path mentioned in a chat is accessible to the agent. If it cannot read the files, ask it to say what access is missing rather than guessing or searching unrelated locations.

## If you have a repository URL

Provide the URL and context:

> The repository is [URL]. I want help with [task]. The relevant branch or commit is [branch/commit, if known]. Can you access this repository in the current environment? If not, tell me the simplest way to open it here. Do not clone it, change remotes, or modify files until I confirm the workspace and scope.

If you already cloned it, open that local checkout and provide its path. A URL alone does not prove the current agent has repository access. Do not provide credentials or tokens in a prompt; use the host's approved authentication mechanism.

## Give enough task context

Include what you want changed, what should remain unchanged, constraints, and any expected behavior or error. For example:

> In this repo, the export endpoint returns duplicate rows for [case]. Please inspect the endpoint and relevant tests, then explain the likely cause and propose a focused fix. Preserve other behavior. Do not implement until I approve the plan.

If you want analysis only, say so:

> This is read-only inspection. Do not edit, stage, commit, or push anything.

## Continue into a workflow

After the agent confirms the correct repository and scope, ask `guide` to choose an appropriate workflow, or invoke a skill directly. For feature work, see [create a feature](04-create-a-feature.md); for new prototypes, see [start a POC](03-start-a-poc.md).
