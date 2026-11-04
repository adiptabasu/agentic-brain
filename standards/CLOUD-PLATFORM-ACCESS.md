# Cloud Platform Access Boundary

This standard applies whenever an agent uses a cloud provider console, API, CLI, SDK, infrastructure tool, or cloud-hosted service to access a user's account or resources.

## Default access

- Read-only retrieval is allowed when it is within the user's request: fetch/get/list/describe/status/metrics/log queries that are known not to change remote state.
- Do not create, update, delete, upload, deploy, publish, start, stop, enable, disable, restart, scale, migrate, execute remote jobs, change permissions, or otherwise mutate cloud resources without explicit authorization for that action and scope.
- Treat indirect changes as changes too. This includes invoking a workflow, applying infrastructure code, submitting a job, triggering a deployment, or using a tool whose read-like request has write side effects.
- If an operation's effect is unclear, do not run it. Check authoritative tool documentation or ask the user.

## Authorization for a change

A direct user instruction can authorize a change when it clearly identifies the requested operation and target. Before acting, ensure the target account/project/region/resource and the permitted scope are unambiguous. If they are not, ask a focused question. Do not infer authorization from a request to inspect, diagnose, recommend, prepare, or fix an unspecified problem.

After authorization:

1. Perform only the approved operation on the approved target and scope.
2. Stop if execution reveals a materially different target, side effect, cost, risk, or scope; explain it and get approval before proceeding.
3. Verify the result with read-only evidence when available, and report what changed, what was observed, and what remains unknown.

Authorization for one resource, operation, account, environment, or time does not authorize additional changes. A plan, tool availability, prior access, or successful read does not grant write permission.
