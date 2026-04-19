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
- `slide-outline-planner.yaml`
  - Global outline governor.
  - Use to lock chapter order, slide allocation, slide family selection, exception-slide placement, and chapter-batch gate rules before any slide build starts.
- `chapter-slide-pm-ko.yaml`
  - Chapter planning agent.
  - Use to turn one approved chapter or theme into a batch of slide briefs.
- `exception-slide-pm-ko.yaml`
  - Exception-slide planning agent.
  - Use for cover, agenda, section divider, synthesis, comparison, or other structural exception slides.
- `korean-slide-copywriter-gpt.yaml`
  - GPT-driven Korean slide copy agent.
  - Use to compress approved slide briefs into presentation-ready Korean title/lead/body copy with the fixed model `gpt-5.4`.
- `storyline-auditor-ko.yaml`
  - Storyline gate agent.
  - Use to review title flow, chapter transitions, duplicate claims, and narrative jumps before HTML work proceeds.
- `korean-tone-auditor-ko.yaml`
  - Korean tone gate agent.
  - Use to review spoken-slide readability, awkward Korean phrasing, translationese, and report-like density before HTML work proceeds.
- `html-slide-builder.yaml`
  - Codex HTML authoring agent.
  - Use to build `slide-XX.html` files and shared HTML/CSS from approved outline, brief, and copy.
- `html-deck-consistency-auditor.yaml`
  - Deck-level HTML consistency agent.
  - Use to review family rhythm, footer/title-band/chapter-marker consistency, and overall deck coherence across built HTML files.
- `html-slide-designer.yaml`
  - HTML slide validation agent.
  - Use after Codex has generated `slide-XX.html` files to verify slide-level render quality, overflow, clipping, and exact contract adherence.
- `pdf-export-reviewer.yaml`
  - Final export QA agent.
  - Use to review HTML-to-PDF conversion quality and block delivery when visual defects remain.
- `speaker-notes-writer.yaml`
  - Presentation script agent.
  - Use after the deck stabilizes to create Korean speaker notes, transitions, and delivery cues with GPT.

## Standard Order

1. Run `source-curation-analyst` first when the current source set, provenance, or approved external materials need to be organized.
2. Run `source-integrator` when new markdown or text materials must be merged into the current structure.
3. Run `seminar-writer-ko` or `doc-editor-partner` to produce and refine the canonical Korean prose under `docs/02-seminar/prose/`.
4. Run `slide-outline-planner` after the prose docs become the accepted source of truth. Do not let chapter PM work start before this gate passes.
5. Run `chapter-slide-pm-ko` per chapter or theme batch, and add `exception-slide-pm-ko` when cover, agenda, section divider, synthesis, or comparison slides need special handling.
6. Require an approved `reference shell` per slide before Korean copy or HTML work starts.
7. Run `korean-slide-copywriter-gpt` with the fixed model `gpt-5.4` after the slide brief batch is approved.
8. Run `storyline-auditor-ko` and `korean-tone-auditor-ko` in parallel. Only proceed to HTML generation if both return `PASS`.
9. Run `html-slide-builder` to author HTML/CSS, then run `python3 scripts/check_slide_contract.py` and `python3 scripts/check_slide_korean.py docs/03-html/slides`.
10. Run `html-deck-consistency-auditor` and `html-slide-designer` in parallel. Only proceed if both return `PASS`.
11. Repeat steps 5 through 10 per chapter batch until the full deck exists.
12. Re-run `storyline-auditor-ko`, `korean-tone-auditor-ko`, `html-deck-consistency-auditor`, and `html-slide-designer` over the whole deck as the final deck gate.
13. Run `pdf-export-reviewer` after the final deck gate passes.
14. Run `speaker-notes-writer` after deck order and core copy are frozen.

## Project Skill Paths

- Local custom skill:
  - `/Users/seungsu/Desktop/project/jaryo/.codex/skills/local/jaryo-doc-reconstruction/SKILL.md`
  - `/Users/seungsu/Desktop/project/jaryo/.codex/skills/local/jaryo-html-slide-design/SKILL.md`
  - `/Users/seungsu/Desktop/project/jaryo/.codex/skills/local/jaryo-slide-story-planning-ko/SKILL.md`
  - `/Users/seungsu/Desktop/project/jaryo/.codex/skills/local/jaryo-slide-copy-ko/SKILL.md`
  - `/Users/seungsu/Desktop/project/jaryo/.codex/skills/local/jaryo-slide-evaluation/SKILL.md`
- Local vendor skills:
  - `/Users/seungsu/Desktop/project/jaryo/.codex/skills/vendor/slides/SKILL.md`
  - `/Users/seungsu/Desktop/project/jaryo/.codex/skills/vendor/pdf/SKILL.md`

## Prompt Template

Use `.codex/templates/subagent-task-template.md` as the wrapper prompt. Each agent YAML already contains a `default_prompt` that can be inserted into that template.

## Pipeline Intent

These subagents are scoped to the Jaryo repository only.

- Source curation and prose writing keep `docs/01-sources/` and `docs/02-seminar/prose/` as the canonical planning layer.
- Presentation work follows a gated loop:
  - `global outline gate -> chapter PM -> reference shell lock -> GPT Korean copy -> pre-HTML gate -> Codex HTML build -> automated checks -> post-HTML gate -> final deck gate -> PDF -> speaker notes`
- `slide-outline.md` and `manifest.md` only hold approved outcomes, not working drafts of briefs or gate findings.
- GPT is used for slide-related Korean writing only, with the fixed model `gpt-5.4`.
- Codex is used for HTML generation, deck consistency review, and render validation.
- Speaker notes come last and must stay faithful to the approved docs and deck instead of inventing new framing.
