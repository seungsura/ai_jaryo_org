# Project Subagents

These subagents are project-local. They are defined for this repository only and assume the local skills under `.codex/skills/`.

## Prose And Document Agents

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

## HTML Slide Agents

HTML slide work is a separate subagent system. The main session acts only as HTML orchestrator: it records/loads rules, dispatches subagents, inspects their outputs, and issues the next task. It does not skip PM or reviewer review.

- `html-slide-pm.yaml`
  - Planning and gate agent.
  - Use before any builder work to create the source-backed task packet, editable-file list, visual-reference obligations, QA checks, and reviewer acceptance criteria.
- `html-slide-builder.yaml`
  - Implementation agent.
  - Use only after PM scope is ready. Actual HTML editing goes through `scripts/jaryo_html_deck/slides/chapter_XX/slide_YYY.py`; generated `docs/03-html/slides/slide-XXX.html` is an artifact for inspection.
- `html-slide-qa.yaml`
  - Verification agent.
  - Use after builder work to run the required static checks, runtime checks, screenshot checks, and PDF smoke checks for the assigned scope.
- `html-slide-reviewer.yaml`
  - Final review agent.
  - Use after QA. The orchestrator waits for reviewer output and does not accept or close HTML work without it.

## Prose Standard Order

1. Run `source-curation-analyst` first when the current source set, provenance, or approved external materials need to be organized.
2. Run `source-integrator` when new markdown or text materials must be merged into the current structure.
3. Run `seminar-writer-ko` or `doc-editor-partner` to produce and refine the canonical Korean prose under `docs/02-seminar/prose/`. Use `docs/00-process/seminar-refinement-plan.md` as the per-file loop contract and keep `docs/00-process/seminar-refinement-manifest.md` synchronized.
4. Continue editorial review and source integration loops until the prose docs are stable enough for the user's next task.

## HTML Orchestration Order

1. The orchestrator confirms the HTML task scope and writes any new user feedback into `docs/03-html/shared/slide-quality-rules.md` before implementation.
2. Dispatch `html-slide-pm` and wait for its task packet. Do not send builder work before PM scope, required inputs, and acceptance criteria are clear.
3. Dispatch `html-slide-builder` with the PM packet. Builder edits `scripts/jaryo_html_deck/slides/chapter_XX/slide_YYY.py`; generated slide HTML is regenerated/inspected as an artifact, not hand-edited as source.
4. Dispatch `html-slide-qa` with builder notes and generated artifacts. QA reports pass/fail evidence and any missing checks.
5. Dispatch `html-slide-reviewer` with the PM packet, builder notes, QA evidence, source markdown, visual references, and relevant artifacts. The orchestrator waits for reviewer output and does not skip this gate.
6. The orchestrator either closes the task from reviewer acceptance or issues a narrow follow-up task through the same PM -> builder -> QA -> reviewer chain.

## Project Skill Paths

- Local custom skill:
  - `/Users/seungsu/Desktop/project/jaryo/.codex/skills/local/jaryo-doc-reconstruction/SKILL.md`
  - `/Users/seungsu/Desktop/project/jaryo/.codex/skills/local/natural-korean-prose/SKILL.md`
- Local vendor skills:
  - `/Users/seungsu/Desktop/project/jaryo/.codex/skills/vendor/pdf/SKILL.md`

## Prompt Template

Use `.codex/templates/subagent-task-template.md` as the wrapper prompt. Each agent YAML already contains a `default_prompt` that can be inserted into that template.

## HTML Work Gate

For any HTML-related task, every spawned subagent must read the following before planning, editing, QA, or review:

- `AGENTS.md`
- `.codex/subagents/README.md`
- `.codex/templates/subagent-task-template.md`
- `docs/03-html/shared/slide-quality-rules.md`
- `docs/03-html/shared/decision-log.md`
- `.codex/skills/local/natural-korean-prose/SKILL.md`
- target source markdown
- required visual reference pages approved for the task
- relevant `scripts/jaryo_html_deck/slides/chapter_XX/slide_YYY.py`
- relevant generated `docs/03-html/slides/slide-XXX.html`
- relevant `docs/03-html/outline/slide-outline.md` entries
- relevant `docs/03-html/manifest.md` rows

HTML-related scope includes `docs/03-html/` outline, manifest, generated slides, deck HTML, shared CSS/tokens, screenshot QA, and PDF export QA.

All Codex CLI, Gemini CLI, and project-local subagent prompts for Jaryo docs/slide work must keep `.codex/skills/local/natural-korean-prose/SKILL.md` applied. Korean outputs, slide copy review, QA findings, and user-facing questions should preserve technical English terms while removing translationese and stiff report-style Korean.

Latest user feedback must be written to `docs/03-html/shared/slide-quality-rules.md` before implementation, then verified through the relevant static checks and visual/PDF smoke checks. Missing `docs/03-html/shared/decision-log.md` or missing visual reference pages are blocking input gaps for HTML subagents unless the orchestrator explicitly narrows the task to docs-only system maintenance.

## Pipeline Intent

These subagents are scoped to the Jaryo repository only.

- Source curation and prose writing keep `docs/01-sources/` and `docs/02-seminar/prose/` as the canonical planning layer.
- Canonical prose refinement follows a fixed per-document loop: reference shell lock -> prose pass -> editorial review packet -> manifest sync -> next pass.
