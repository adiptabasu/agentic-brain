# Inspect cloud resources safely

Use this when asking an agent to inspect a cloud account, project, region, or resource.

## Read or fetch data

Name the target and the information you need. State that access is read-only:

> Inspect [account/project/region/resource] to answer [question]. You may fetch or query data using operations known to be read-only. Do not create, update, delete, upload, deploy, start, stop, enable, disable, or otherwise change cloud state. Report evidence and uncertainty.

## Request a cloud change

Ask the agent to inspect and propose a specific change first. Review the operation, exact target, and scope. A direct instruction can authorize a clearly specified action; a broad request to investigate or fix a problem does not authorize an unspecified change.

If approval is needed, identify it explicitly:

> I authorize [specific operation] on [resource] in [account/project/region], limited to [scope]. Do not make any other changes. Stop and ask if the actual target or side effects differ.

The agent should perform only that change, then verify the result with read-only evidence and report what happened. Approval for one target or operation does not cover other resources or follow-up changes.
