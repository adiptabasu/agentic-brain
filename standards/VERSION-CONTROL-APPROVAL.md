# Version Control Approval Rules

Before creating a commit or pushing to a remote, ask the user an explicit yes/no question describing the exact operation.

- Before a commit, identify the files or change set and the proposed commit message.
- Before a push, identify the remote, branch, and commits that will be sent.
- Wait for an affirmative answer to that specific prompt. A general request to finish work, silence, or approval of another operation does not count.
- Treat commit and push as separate approvals. Approval to commit does not authorize a push, and approval to push does not authorize additional commits or unrelated changes.
- If the scope changes after approval, stop and ask again with an updated prompt.

Example:

> Commit the current scaffold and rule updates on branch `main` with message “docs: define project operating rules”? Please answer yes or no.

For a push, ask separately:

> Push commit `abc1234` from `main` to `origin/main`? Please answer yes or no.
