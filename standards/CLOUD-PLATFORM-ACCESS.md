# Cloud Platform Access Rules

These rules apply to cloud consoles, APIs, CLIs, SDKs, infrastructure tools, and cloud-hosted services.

## Read-only access

When the user requests inspection, read-only operations that are known not to change remote state are allowed. Examples include `get`, `fetch`, `list`, `describe`, status, metrics, and log queries. Confirm the operation's effects when they are unclear; do not infer that a read-like name guarantees read-only behavior.

## State-changing access

Do not run an operation that can create, update, edit, delete, upload, publish, deploy, start, stop, enable, disable, restart, scale, migrate, change permissions, execute remote jobs, or otherwise mutate cloud state until the user explicitly approves the specific operation.

Before acting, ask a yes/no question that names:

- The exact operation and intended change.
- The account, project, region, and resource, as applicable.
- The permitted scope and known material side effects.

Proceed only after an affirmative answer to that prompt. Approval covers only the named operation and target. Stop and ask again if execution reveals a materially different target, scope, side effect, or risk. A request to inspect, diagnose, recommend, or broadly “fix” something does not authorize an unspecified change.

Treat indirect changes as state changes too, including triggering workflows, applying infrastructure code, submitting jobs, and using tools whose read-like request has write side effects. If the effects or target are unclear, do not run the operation; clarify first.

After an authorized change, verify the result with read-only evidence when available and report what changed, what was observed, and what remains unknown.
