---
name: project-destination
description: Collect and validate the exact project-folder path before scaffolding. Use when a new project needs a destination and the user has not yet supplied a usable path.
---

# Project destination

Use this one-shot skill to obtain a usable path for the project folder and hand that exact path to `create-scaffolding`. This skill does not create or change folders.

## Perspectives

- Use the Requirements Analyst viewpoint to confirm the requested destination and resolve missing path details without inventing them.
- Use the Implementation Engineer viewpoint to check that the path can be handed to the scaffolding workflow as a project root.

## Workflow

1. **Get the path.** If the user has not supplied a destination, ask for the exact project-folder path. Do not choose a location or append a project-name directory on the user's behalf.
2. **Validate read-only.** Preserve the supplied path, including spaces and its original spelling. Check that it is a usable path for a folder. An existing regular file is not a usable project folder; ask for a corrected path. An existing directory, including a non-empty one, is a candidate destination; do not inspect its contents. Do not create, rename, or modify folders or files, inspect the reference project, generate a blueprint, or copy a template in this skill. If the path cannot be interpreted or validated in the current context, ask a focused question instead of guessing.
3. **Hand off the exact path.** Pass the unchanged path as the project folder root to `create-scaffolding` when that workflow is requested and available. That skill decides whether the directory can be used or must be left unchanged for review. If scaffolding was not requested or is unavailable, return the validated path and wait for the next step. Report a validation blocker and ask for the missing or corrected path.
