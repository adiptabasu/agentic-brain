# Migrate code between codebases in small, verified chunks

Use this guide when moving an application, service, feature, or other code from one codebase to another. It is designed for larger migrations where copying everything at once would make regressions difficult to isolate. The source and target may use different structures, frameworks, or conventions.

The core loop is: understand both codebases, agree on a migration map, migrate one bounded chunk, test and review it, get confirmation, and only then start the next chunk.

## 1. Identify the source, target, and outcome

Open or point the agent to both codebases. State which is the source of behavior and which is the destination. Include the relevant branches or revisions, the intended outcome, and any constraints such as supported platforms, deadlines, or compatibility requirements.

Start with this prompt:

> I want to migrate [system / feature / capability] from source codebase [path or repository and revision] into target codebase [path or repository and revision]. The intended outcome is [what users or callers should be able to do]. First inspect both codebases and their project instructions. Do not edit files, install dependencies, run migrations, or perform Git operations. Ask me about anything that is unclear, then report the existing behavior, target conventions, tests, constraints, and questions that need answers.

Do not assume that the source layout or implementation should be copied as-is. The target codebase may already provide equivalent behavior or a better-fitting design.

## 2. Agree on a migration map

Ask for a read-only comparison before implementation:

> Compare the source behavior and contracts with the target codebase. Identify what already exists in the target, what is missing, dependencies between parts, data or configuration changes, compatibility risks, and relevant tests. Propose a migration map that divides the work into small, independently reviewable chunks. For each chunk, state its scope, prerequisites, expected behavior, acceptance criteria, and checks. Order the chunks by dependency. Do not edit files.

Review the map with the agent. Adjust chunk boundaries until each chunk is small enough to understand and validate on its own. A chunk might be a single endpoint with its tests, a data model plus a safe compatibility layer, or one vertical user-visible capability. Avoid arbitrary file-count boundaries when files participate in one behavior.

Agree explicitly on:

- Which repository is allowed to change, and which paths are in scope.
- Whether the source must remain unchanged and available during the migration.
- The order and acceptance criteria for the chunks.
- Required behavior parity versus intentional behavior changes.
- How data, configuration, secrets, APIs, and deployment are handled, where applicable.
- Which test, build, integration, or manual checks provide adequate evidence.
- Who confirms a chunk before work proceeds to the next one.

Do not start implementation until the migration map and the first chunk are clear.

## 3. Establish a baseline

Before changing the target, record its current status and run the checks that are practical for the affected area. This helps distinguish pre-existing failures from migration regressions. Inspect existing local changes and preserve them. Do not overwrite unrelated work.

Ask the agent:

> Before implementing chunk 1, inspect the target working tree and relevant tests. Run the agreed baseline checks for the affected area without changing files. Report the exact commands and results, including any existing failures or checks that cannot run, then wait.

Agree how to handle any baseline failure before proceeding. Do not claim a migration caused or fixed a failure without evidence.

## 4. Migrate one chunk at a time

For each chunk, restate its scope and acceptance criteria. Authorize that chunk only. For example:

> Proceed with chunk [number and name] from the agreed migration map. Change only [target repository and paths] to meet these acceptance criteria: [criteria]. Preserve existing target conventions and unrelated changes. Add or update focused tests. Do not start another chunk, change the source codebase, or commit or push. When finished, show the changed files, explain the implementation, and report the exact checks run and their results. Stop for my review.

Review the diff and evidence. If checks fail or behavior is uncertain, keep the work on that chunk: diagnose, make a focused correction, and rerun the relevant checks. If the chunk reveals a new dependency or changes the migration plan, update the map and agree on the revised scope before continuing.

Only after reviewing and accepting the chunk, say:

> I have reviewed and accept chunk [number and name]. Do not change it further. We can proceed to the next agreed chunk: [number and name]. First confirm its scope and acceptance criteria, then wait for my approval to implement it.

This confirmation gate matters on large migrations: a passing check is evidence for the check that ran, not automatic approval to continue or proof that every behavior is correct.

## 5. Validate the integrated migration

After all chunks are accepted, review the complete change across chunk boundaries. Check interactions, shared contracts, data and configuration transitions, compatibility, security-sensitive paths, and operational behavior that applies to this migration. Run the agreed broader test suite and integration checks. Compare the final behavior with the migration map and identify anything deferred or unverified.

Prompt:

> Review the completed migration against the agreed migration map and acceptance criteria. Inspect the full diff and interactions between chunks. Run the agreed final checks and report exact evidence, failures, unverified behavior, deferred work, and any rollout or rollback concerns. Do not commit, push, deploy, or delete source code.

Do not remove or decommission the source implementation or data until that action is separately agreed and the target is verified for the intended use.

## 6. Handle Git and rollout separately

Once the migration is reviewed, decide how to record it in Git. Specify the repository, branch, commit scope, and whether a push is wanted. Keep commits aligned to the accepted chunks when useful, and use descriptive messages. Do not combine unrelated work. Deployment, production data changes, cutover, and source decommissioning are separate actions that need their own plan and authorization.

Example prompt:

> The integrated migration has been reviewed. Prepare a commit for the accepted target-codebase changes only, using the message `[commit message]`. Show me the staged file list and staged diff before committing. Do not push or deploy.

## If an existing migration is already underway

If work has already started, first inspect both codebases, the target working tree, recent changes, and available test evidence without editing. Reconstruct which migration-map chunks appear complete, partially complete, or untouched. Do not infer acceptance from a commit or passing test alone. Present the current state and ask which chunk the user wants reviewed or resumed.
