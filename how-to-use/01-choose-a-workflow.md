# Choose where to start

Use this when you have a task but are unsure which Agentic Brain skill fits. The Guide skill should choose a proportionate route, not automatically send every request through every skill.

Invoke `guide` or say:

> Read `skills/guide/SKILL.md` and follow it. I want to [goal]. I am unsure where to start. Ask about any detail that could change the recommended approach, then suggest the smallest useful workflow and the next skill. Tell me what can proceed now and what needs a decision or approval.

Examples:

- “I have a failing test, but I don't know whether the bug is in our code or setup. What should I do next?”
- “I want to simplify a module without changing behavior. Which skill should lead?”
- “I need to prepare a production release. Help me route the work and identify what needs approval.”

If you already know what you want, invoke the relevant skill directly. You do not need to use Guide as a mandatory gate. If the recommendation feels too broad, say:

> That seems heavier than this task needs. Recommend a smaller route that still covers the important risks and completion checks.
