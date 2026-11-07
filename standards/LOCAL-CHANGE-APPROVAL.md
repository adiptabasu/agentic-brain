# Local Change Approval Rules

These rules apply to changes on the user's machine or in the local project, including filesystem operations, installed software, and global configuration.

## Routine edits

Make focused, reversible edits that are clearly within the user's request. Preserve unrelated work and inspect the affected files before changing them.

## Destructive or broad changes

Before bulk deletion, overwriting substantial existing work, resetting or cleaning a working tree, changing global machine settings, or performing another difficult-to-reverse local operation, present an explicit yes/no prompt. State:

- The exact files, data, settings, or other targets affected.
- What will be removed, replaced, or changed.
- The scope and material consequences, including whether a backup exists when relevant.

Proceed only after an affirmative answer to that specific prompt. A general goal such as “clean this up” is not enough to authorize an unspecified destructive operation. Stop and ask again if the actual scope or effect differs from what was approved.

Do not treat a backup as a substitute for approval. Do not delete, overwrite, or reset unrelated user changes.
