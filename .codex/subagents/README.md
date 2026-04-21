# Project Subagents

These subagents are project-local. They are defined for this repository only and assume the local skills under `.codex/skills/`.

## Available Agents

- `doc-editor-partner.yaml`
  - Primary collaborative agent.
  - Use to organize docs, improve prose, ask the user focused questions, and iterate quality upward.
- `source-integrator.yaml`
  - Intake and merge agent.
  - Use when new markdown/text materials arrive and must be mapped into the current docs before editing.
- `source-curation-analyst.yaml`
  - Provenance-first source intake agent.
  - Use to inventory current local materials, classify approved external materials, and expose citation or asset gaps before writing.
- `seminar-writer-ko.yaml`
  - Final Korean prose agent.
  - Use to turn approved sources into the canonical seminar text under `docs/02-seminar/prose/`.

## Standard Order

1. Run `source-curation-analyst` first when the current source set, provenance, or approved external materials need to be organized.
2. Run `source-integrator` when new markdown or text materials must be merged into the current structure.
3. Run `seminar-writer-ko` or `doc-editor-partner` to produce and refine the canonical Korean prose under `docs/02-seminar/prose/`. Use `docs/00-process/seminar-refinement-plan.md` as the per-file loop contract and keep `docs/00-process/seminar-refinement-manifest.md` synchronized.
4. Continue editorial review and source integration loops until the prose docs are stable enough for the user's next task.

## Project Skill Paths

- Local custom skill:
  - `/Users/seungsu/Desktop/project/jaryo/.codex/skills/local/jaryo-doc-reconstruction/SKILL.md`
- Local vendor skills:
  - `/Users/seungsu/Desktop/project/jaryo/.codex/skills/vendor/pdf/SKILL.md`

## Prompt Template

Use `.codex/templates/subagent-task-template.md` as the wrapper prompt. Each agent YAML already contains a `default_prompt` that can be inserted into that template.

## HTML Work Gate

For any HTML-related task, every spawned subagent must read `AGENTS.md` and `docs/03-html/shared/slide-quality-rules.md` before planning or editing. HTML-related scope includes `docs/03-html/` outline, manifest, generated slides, deck HTML, shared CSS/tokens, screenshot QA, and PDF export QA.

Latest user feedback must be written to `docs/03-html/shared/slide-quality-rules.md` before implementation, then verified through the relevant static checks and visual/PDF smoke checks.

## Pipeline Intent

These subagents are scoped to the Jaryo repository only.

- Source curation and prose writing keep `docs/01-sources/` and `docs/02-seminar/prose/` as the canonical planning layer.
- Canonical prose refinement follows a fixed per-document loop: reference shell lock -> prose pass -> editorial review packet -> manifest sync -> next pass.
