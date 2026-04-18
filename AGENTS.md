# Jaryo Agent Guide

## Scope

This repository uses project-local skills and subagent specs under `.codex/`. Keep the setup local to this repository and prefer those local artifacts over global skills when the task is about document reconstruction or later presentation regeneration.

## Default Source Policy

- Treat local markdown files as the only authoritative source for reconstruction work.
- Do not inspect `assets/`, JPG, PNG, or PDF files unless the user explicitly changes that rule.
- When content is missing, record it in `docs/01-sources/intake/open-questions.md` instead of guessing.
- Ask focused follow-up questions to the user after meaningful editorial passes instead of silently guessing.

## Documentation Language Policy

- Write new and revised documentation in Korean by default.
- Keep English for terms, technical vocabulary, product names, service names, library or framework names, API names, commands, paths, protocols, and other expressions where translation would reduce precision.
- When readability benefits from explanation, add a short Korean explanation without replacing the canonical English term.

## Local Skills

- `.codex/skills/local/jaryo-doc-reconstruction/SKILL.md`
- `.codex/skills/vendor/slides/SKILL.md`
- `.codex/skills/vendor/pdf/SKILL.md`

## Local Subagents

- `.codex/subagents/doc-editor-partner.yaml`
- `.codex/subagents/source-integrator.yaml`
- `.codex/subagents/deck-architect.yaml`
- `.codex/subagents/source-curation-analyst.yaml`
- `.codex/subagents/seminar-writer-ko.yaml`
- `.codex/subagents/slide-outline-planner.yaml`
- `.codex/subagents/html-slide-designer.yaml`
- `.codex/subagents/pdf-export-reviewer.yaml`
- `.codex/subagents/speaker-notes-writer.yaml`

Use `.codex/subagents/README.md` for the intended order and `.codex/templates/subagent-task-template.md` for spawn prompts.
