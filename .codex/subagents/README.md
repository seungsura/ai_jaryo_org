# Project Subagents

These subagents are project-local. They are defined for this repository only and assume the local skills under `.codex/skills/`.

## Available Agents

- `doc-editor-partner.yaml`
  - Primary collaborative agent.
  - Use to organize docs, improve prose, ask the user focused questions, and iterate quality upward.
- `source-integrator.yaml`
  - Intake and merge agent.
  - Use when new markdown/text materials arrive and must be mapped into the current docs before editing.
- `deck-architect.yaml`
  - Presentation regeneration agent.
  - Use later, after the prose docs are approved, to design a slide-ready outline or editable deck plan.
- `source-curation-analyst.yaml`
  - Provenance-first source intake agent.
  - Use to inventory current local materials, classify approved external materials, and expose citation or asset gaps before writing.
- `seminar-writer-ko.yaml`
  - Final Korean prose agent.
  - Use to turn approved sources into the canonical seminar text under `docs/02-seminar/prose/`.
- `slide-outline-planner.yaml`
  - Planning gate for presentation work.
  - Use to compress approved docs into a slide outline that can be reviewed before any HTML design starts.
- `html-slide-designer.yaml`
  - HTML slide production agent.
  - Use after outline approval to generate or refine `slide-XX.html` style presentation files and verify browser rendering.
- `pdf-export-reviewer.yaml`
  - Final export QA agent.
  - Use to review HTML-to-PDF conversion quality and block delivery when visual defects remain.
- `speaker-notes-writer.yaml`
  - Presentation script agent.
  - Use after the deck stabilizes to create Korean speaker notes, transitions, and delivery cues.

## Standard Order

1. Run `source-curation-analyst` first when the current source set, provenance, or approved external materials need to be organized.
2. Run `source-integrator` when new markdown or text materials must be merged into the current structure.
3. Run `seminar-writer-ko` or `doc-editor-partner` to produce and refine the canonical Korean prose under `docs/02-seminar/prose/`.
4. Run `slide-outline-planner` after the prose docs become the accepted source of truth.
5. Run `html-slide-designer` only after the outline is approved.
6. Run `pdf-export-reviewer` after HTML slides exist and before delivery.
7. Run `speaker-notes-writer` after the deck order and core copy have stabilized.
8. Keep `deck-architect` as a higher-level fallback when a broad deck plan is needed before splitting work across the more specific presentation agents.

## Project Skill Paths

- Local custom skill:
  - `/Users/seungsu/Desktop/project/jaryo/.codex/skills/local/jaryo-doc-reconstruction/SKILL.md`
- Local vendor skills:
  - `/Users/seungsu/Desktop/project/jaryo/.codex/skills/vendor/slides/SKILL.md`
  - `/Users/seungsu/Desktop/project/jaryo/.codex/skills/vendor/pdf/SKILL.md`

## Prompt Template

Use `.codex/templates/subagent-task-template.md` as the wrapper prompt. Each agent YAML already contains a `default_prompt` that can be inserted into that template.

## Pipeline Intent

These subagents are scoped to the Jaryo repository only.

- Source curation and prose writing keep `docs/01-sources/` and `docs/02-seminar/prose/` as the canonical planning layer.
- Presentation work follows the seminar's own documented staging: `PLAN -> DESIGN -> EXPORT`, which maps to outline approval, HTML slide production, and PDF export review.
- Speaker notes come last and must stay faithful to the approved docs and deck instead of inventing new framing.
