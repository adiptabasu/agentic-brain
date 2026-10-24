# Clarify a request before deciding

Use this when a request could mean several things, requirements conflict, or a missing detail could lead to the wrong work.

Invoke `probe` or say:

> Read `skills/probe/SKILL.md` and follow it. Help clarify this request: [paste request]. Identify the uncertainties or assumptions that could materially change the result. Ask one focused question at a time, explain the relevant trade-offs when useful, and do not make a plan or change files until we agree on the requirements.

Answer each question; “not sure” is a valid answer. The agent should distinguish requirements from preferences and unresolved items. If it makes an assumption, say:

> You are treating [assumption] as settled. I have not confirmed that. Please mark it as unknown and explain whether work can proceed safely without deciding it.

When the requirements are clear, ask for a recap:

> Summarize the confirmed requirements, constraints, decisions, open questions, and what is explicitly out of scope. I will correct this before you continue.

If you approve the recap, move to `specify` for testable acceptance criteria, or ask `guide` for the next skill. Do not use Probe to keep asking about details that will not affect the result.
