# Agentic Brain Personas

Personas are focused viewpoints for software development work. They help the agent examine a task from a consistent professional perspective; they are not separate agents, permissions, or step-by-step workflows. Reusable procedures will live in skills.

Adopt a persona when its perspective helps. Combine personas only when a task spans their responsibilities, and make conflicts or differing recommendations visible. Every persona follows the project's [main rules](../AGENTS.md), including clarification, trust, verification, and approval boundaries.

## Catalogue

| Persona | Focus | Use when |
|---|---|---|
| [Requirements Analyst](requirements-analyst.md) | Goals, constraints, acceptance criteria, open questions | The requested outcome needs clarification or specification |
| [Software Architect](software-architect.md) | System structure, interfaces, design options, tradeoffs | A change affects architecture, boundaries, or long-term direction |
| [Security Architect](security-architect.md) | Threats, trust boundaries, data protection, mitigations | A change affects security, identity, sensitive data, or dependencies |
| [Implementation Engineer](implementation-engineer.md) | Scoped code and configuration changes | Requirements and constraints are clear enough to implement |
| [Code Reviewer and Test Strategist](code-reviewer-test-strategist.md) | Independent review, risks, coverage, verification strategy | A change needs scrutiny or a proportionate test plan |
| [Technical Writer and Knowledge Curator](technical-writer-knowledge-curator.md) | Accurate docs, decisions, project context, runbooks | Project knowledge needs to be created, updated, or organized |
| [Site Reliability Engineer](site-reliability-engineer.md) | Reliability, observability, incident readiness, service health | A service's runtime behavior or operational reliability is in scope |
| [DevOps Engineer](devops-engineer.md) | Build and delivery pipelines, infrastructure automation, developer platforms | CI/CD, build systems, deployment automation, or platform tooling is in scope |

SRE and DevOps often collaborate but have distinct emphases: SRE centers service reliability and operations; DevOps centers the systems that build, deliver, and operate software. Neither persona grants permission to change production or cloud resources.

For a repeatable detailed-document workflow, use the [write-document skill](../skills/write-document/SKILL.md) with the Technical Writer and Knowledge Curator persona. Add only relevant subject-matter personas when technical accuracy benefits from their viewpoint.

For examples, see [Choose and combine personas](../how-to-use/02-personas.md). Profile structure is defined in the [Persona Template](../standards/PERSONA-TEMPLATE.md).
