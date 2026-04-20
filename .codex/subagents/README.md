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
- `slide-style-reference-analyst.yaml`
  - HTML track setup agent.
  - Use to lock visual references, chrome rules, and shell constraints before outline planning.
- `slide-outline-planner.yaml`
  - Slide map agent.
  - Use to compress source markdown into a chapter-by-chapter outline with transition slides.
- `slide-copy-compressor.yaml`
  - Copy density agent.
  - Use to shorten outline text into production slide copy while preserving the argument.
- `slide-html-builder.yaml`
  - HTML build agent.
  - Use to turn approved outline and copy into slide HTML under the harness-rebuilt track.
- `slide-contract-reviewer.yaml`
  - Contract gate agent.
  - Use to return PASS, REVISE, or BLOCK against the slide contract.
- `slide-render-reviewer.yaml`
  - Render gate agent.
  - Use to check the rendered deck for visual drift and spacing regressions.
- `chapter-committer.yaml`
  - Chapter freeze agent.
  - Use to lock an approved chapter before deck export.
- `deck-pdf-exporter.yaml`
  - Final delivery agent.
  - Use to export the approved deck to PDF after all chapter gates pass.

## Standard Order

1. Run `source-curation-analyst` first when the current source set, provenance, or approved external materials need to be organized.
2. Run `source-integrator` when new markdown or text materials must be merged into the current structure.
3. Run `seminar-writer-ko` or `doc-editor-partner` to produce and refine the canonical Korean prose under `docs/02-seminar/prose/`. Use `docs/00-process/seminar-refinement-plan.md` as the per-file loop contract and keep `docs/00-process/seminar-refinement-manifest.md` synchronized.
4. Continue editorial review and source integration loops until the prose docs are stable enough for the user's next task.

## Harness-Rebuilt HTML Order

1. Run `slide-style-reference-analyst` to lock the visual contract and shell set.
2. Run `slide-outline-planner` to map source markdown into chapter and slide order.
3. Run `slide-copy-compressor` to reduce outline text into slide copy.
4. Run `slide-html-builder` to produce the HTML slides from approved copy.
5. Run `slide-contract-reviewer` before any render work.
6. Run `slide-render-reviewer` on rendered output.
7. Run `chapter-committer` to freeze a chapter after both reviews pass.
8. Run `deck-pdf-exporter` only after the final chapter has been committed.

## Project Skill Paths

- Local custom skill:
  - `/Users/seungsu/Desktop/project/jaryo/.codex/skills/local/jaryo-doc-reconstruction/SKILL.md`
- Local vendor skills:
  - `/Users/seungsu/Desktop/project/jaryo/.codex/skills/vendor/pdf/SKILL.md`

## Prompt Template

Use `.codex/templates/subagent-task-template.md` as the wrapper prompt. Each agent YAML already contains a `default_prompt` that can be inserted into that template.

## Pipeline Intent

These subagents are scoped to the Jaryo repository only.

- Source curation and prose writing keep `docs/01-sources/` and `docs/02-seminar/prose/` as the canonical planning layer.
- Canonical prose refinement follows a fixed per-document loop: reference shell lock -> prose pass -> editorial review packet -> manifest sync -> next pass.
