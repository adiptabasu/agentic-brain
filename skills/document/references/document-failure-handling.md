# Documentation failure handling

Read only when source access, conflicting information, unsupported examples, links, formatting, scope, or sensitive information creates a material problem.

## 8. Failure Handling

### 8.1 Missing files or source access

If a required file or source is unavailable:

1. Identify what is missing.
2. Search only the available, authorized sources.
3. Complete independent documentation work where possible.
4. Mark unsupported claims as unknown or omit them.
5. Request the specific source or access needed.

Do not fabricate file contents or pretend to have inspected unavailable artifacts.

### 8.2 Contradictory documentation

If two documents disagree:

1. Identify the conflicting statements and locations.
2. Determine whether one is explicitly designated as authoritative.
3. Compare them with implementation or approved decisions when available.
4. Update the appropriate source only when the correct interpretation is established.
5. Link related documents where useful.
6. Record unresolved conflicts as follow-up work.

Do not resolve contradictions based solely on which wording sounds more plausible.

### 8.3 Unsupported examples or commands

If an example cannot be validated:

- Look for an authoritative command reference, schema, or existing working example.
- Correct it if sufficient evidence is available.
- Label it as illustrative if it is not an actual observed result.
- Omit it when presenting it would likely mislead the reader.
- State the limitation if the example is essential to the requested documentation.

Never invent successful output to make a guide appear complete.

### 8.4 Broken links or missing references

When a link fails or its destination is unavailable:

- Confirm the intended destination if possible.
- Correct it only when the replacement is established.
- Remove or flag obsolete references when appropriate.
- Avoid replacing an unavailable internal reference with an unrelated public page.
- Report links that could not be checked.

A failed network request alone does not prove that a destination no longer exists.

### 8.5 Ambiguous audience or purpose

If different interpretations would produce substantially different documents, ask a focused question.

Otherwise, choose a reasonable, low-risk structure, make material scope boundaries clear, and proceed.

Do not turn every stylistic preference into a blocking question.

### 8.6 Scope expansion

If the documentation review uncovers additional work:

1. Separate required corrections from optional improvements.
2. Complete authorized, relevant corrections.
3. Record unrelated issues as recommendations.
4. Ask before making consequential or out-of-scope changes.
5. Keep the final summary clear about what was and was not changed.

### 8.7 Formatting or validation failure

If a document parser, linter, link checker, or other validator reports an issue:

- Inspect the actual failure.
- Determine whether it affects validity, readability, or factual correctness.
- Fix issues within scope.
- Rerun the relevant check when available.
- Report unresolved failures honestly.

If the validation tool is unavailable, do not claim validation succeeded.

### 8.8 Sensitive information discovered during documentation

If source material contains secrets or sensitive information:

- Avoid copying the sensitive value into documentation.
- Redact it from examples and excerpts.
- Prefer placeholders or references to an approved secret-management mechanism.
- Report material exposure through the appropriate channel.
- Do not publish the sensitive value as part of a documentation fix.

### 8.9 Interrupted work

If documentation work is interrupted:

- Preserve the last confirmed state.
- Identify completed and incomplete sections.
- Record unresolved source questions.
- Avoid reporting a draft as complete if material sections remain unfinished.
- Provide a concise handoff so work can resume safely.
