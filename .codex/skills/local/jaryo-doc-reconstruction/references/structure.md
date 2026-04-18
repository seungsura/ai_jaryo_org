# Default Docs Structure

Use this layout unless the user asks for a different split:

```text
docs/
  README.md
  01-sources/
    registry.md
    local-canonical/
    local-supplemental/
    approved-external/
    intake/
      source-inbox.md
      open-questions.md
    maps/
      seminar-claims-and-sources.md
      prompt-context-harness-to-seminar.md
  02-seminar/
    prose/
      00-overview.md
      01-where-coding-is-going.md
      02-why-claude-code.md
      03-ai-era-methodology.md
      04-harness-and-context-engineering.md
      05-limitations-and-failure-patterns.md
      06-multi-agent-patterns.md
      07-practical-workflow-and-tooling.md
      08-how-this-presentation-was-made.md
      09-what-we-should-do-next.md
      90-appendix-references.md
```

## Source Mapping Guidance

- `docs/01-sources/local-canonical/claude-code-seminar-kakao.md` is the main source for the seminar narrative and section order.
- `docs/01-sources/local-supplemental/prompt-context-harness-1-15.md` is a supporting source that deepens the harness-related sections and can become `docs/01-sources/maps/prompt-context-harness-to-seminar.md`.
- Preserve the main seminar section boundaries first, then merge supporting material into the most relevant section or reference file.

## Splitting Rule

- Split by section when the source already has stable section boundaries or when different sections will need separate review cycles.
- Keep a single master index in `docs/README.md`.
- Avoid page-by-page files.
- Avoid a single monolithic file unless the user explicitly wants print-style delivery first.
