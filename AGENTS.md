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

## HTML Slide Stage Policy

- For work under `docs/03-html/`, treat `docs/02-seminar/prose/` as the canonical content source.
- Before designing slides, read `docs/03-html/outline/slide-outline.md`, `docs/03-html/manifest.md`, and `docs/03-html/shared/design.md`.
- Treat `docs/03-html/manifest.md` as a live synchronization file: initialize it before slide production, then update it whenever slide ids, order, section mapping, or status change.
- Treat `docs/03-html/shared/design.md` as the design contract for tone, palette, typography, spacing, and slide grammar.
- Treat `slide-outline-planner` as the global outline governor for chapter order, slide allocation, slide family assignment, and chapter-batch gate criteria.
- Korean writing for slide planning, slide copy, and speaker notes must use `gemini -m gemini-3.1-pro-preview`.
- HTML/CSS generation under `docs/03-html/` is authored by Codex-based subagents, not Gemini.
- Keep HTML generation and HTML validation split across separate subagents.
- Use chapter-batch review gates before HTML generation and a final deck gate before PDF export or speaker notes.
- Use only approved visual assets; do not introduce new visual evidence or decorative imagery without explicit approval.

## Local Skills

- `.codex/skills/local/jaryo-doc-reconstruction/SKILL.md`
- `.codex/skills/local/jaryo-html-slide-design/SKILL.md`
- `.codex/skills/local/jaryo-slide-story-planning-ko/SKILL.md`
- `.codex/skills/local/jaryo-slide-copy-ko/SKILL.md`
- `.codex/skills/local/jaryo-slide-evaluation/SKILL.md`
- `.codex/skills/vendor/slides/SKILL.md`
- `.codex/skills/vendor/pdf/SKILL.md`

## Local Subagents

- `.codex/subagents/doc-editor-partner.yaml`
- `.codex/subagents/source-integrator.yaml`
- `.codex/subagents/source-curation-analyst.yaml`
- `.codex/subagents/seminar-writer-ko.yaml`
- `.codex/subagents/slide-outline-planner.yaml`
- `.codex/subagents/chapter-slide-pm-ko.yaml`
- `.codex/subagents/exception-slide-pm-ko.yaml`
- `.codex/subagents/korean-slide-copywriter-gemini.yaml`
- `.codex/subagents/storyline-auditor-ko.yaml`
- `.codex/subagents/korean-tone-auditor-ko.yaml`
- `.codex/subagents/html-slide-builder.yaml`
- `.codex/subagents/html-deck-consistency-auditor.yaml`
- `.codex/subagents/html-slide-designer.yaml`
- `.codex/subagents/pdf-export-reviewer.yaml`
- `.codex/subagents/speaker-notes-writer.yaml`

Use `.codex/subagents/README.md` for the intended order and `.codex/templates/subagent-task-template.md` for spawn prompts.
