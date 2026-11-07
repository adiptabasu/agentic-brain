# Version Control Approval Rules

Before creating a commit or pushing to a remote, ask the user an explicit yes/no question describing the exact operation.

- Before asking to commit, stage only the intended files and review the complete staged diff. Confirm it contains no unrelated or unintended changes. If the staged contents change after review or approval, review again and ask for approval again.
- After reviewing the complete staged diff, use the [write-document skill](../skills/write-document/SKILL.md) to compose the commit message from the changes actually staged. The message must be informative at a glance: use a specific subject that describes the change and affected area, and a body that explains the important details and rationale. Avoid generic messages such as “updates” or “fix stuff.” Include the proposed full message in the approval prompt.
- In the commit approval prompt, identify the staged change set and proposed commit message.
- Before a push, identify the remote, branch, and commits that will be sent.
- Wait for an affirmative answer to that specific prompt. A general request to finish work, silence, or approval of another operation does not count.
- Treat commit and push as separate approvals. Approval to commit does not authorize a push, and approval to push does not authorize additional commits or unrelated changes.
- If the scope changes after approval, stop and ask again with an updated prompt.

Example commit message:

```text
feat(auth): refresh expired sessions automatically

Refresh access tokens when a valid refresh token is available, avoiding
unnecessary sign-outs. Add coverage for refresh success and expiration.
```

Example approval prompt:

> I staged and reviewed 3 files: `src/auth/session.ts`, `src/auth/session.test.ts`, and `README.md`. The diff adds automatic session refresh and covers the expired-token case. Create commit `feat(auth): refresh expired sessions automatically` with the body shown above on `main`? Please answer yes or no.

For a push, ask separately:

> Push commit `abc1234` from `main` to `origin/main`? Please answer yes or no.
