# Document skill maintenance reference

Read only when adapting or maintaining this skill, not when writing project documentation.

## 11. Portability

- Use plain Markdown and standard Agent Skills metadata unless the repository defines a different convention.
- Adapt to the available documentation format, tooling, and repository structure.
- Do not assume a particular language, framework, operating system, documentation generator, hosting provider, or CI platform.
- Do not assume access to source code, project files, external links, or connected systems unless the runtime establishes their availability.
- Use existing project conventions when supported by evidence.
- Keep environment-specific instructions separate from generic concepts when both are needed.
- Use explicit handoffs when source inspection, implementation, or external publication requires another capability.
- Treat compatibility with individual agent platforms as unverified until tested.

## 12. Maintenance

When updating Document:

1. Preserve alignment with the shared core principles and handoff contract.
2. Keep documentation claims grounded in authoritative sources.
3. Maintain a clear distinction between verified facts, intended behavior, proposals, and unknowns.
4. Prefer updating canonical sources over creating unnecessary duplicates.
5. Validate links, metadata, formatting, commands, and internal references when tools are available.
6. Test procedural instructions when safe, authorized, and relevant.
7. Reassess related documentation when interfaces, configuration, architecture, or operational procedures change.
8. Remove stale content and duplicated rules when their authoritative source already defines them.
9. Avoid including sensitive information in examples or operational instructions.
10. Record meaningful changes through the repository's normal Git workflow.
