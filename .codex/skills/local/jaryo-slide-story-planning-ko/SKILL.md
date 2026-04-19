---
name: jaryo-slide-story-planning-ko
description: Plan the Jaryo seminar deck at the outline, chapter-batch, and exception-slide levels before any Korean slide copy or HTML generation starts. Use when governing chapter order, assigning slide families, writing internal slide briefs, defining batch gates, or deciding what one slide should claim and omit.
---

# Jaryo Slide Story Planning KO

## Overview

Use this skill to turn approved seminar prose into governed slide briefs. This is the planning layer that sits between prose and slide wording. It decides what a slide is for, what it must claim, what it must omit, and which layout family it belongs to.

## Core Rules

- Treat `docs/02-seminar/prose/` as the canonical content source.
- Read `docs/03-html/outline/slide-outline.md`, `docs/03-html/manifest.md`, and `docs/03-html/shared/design.md` before planning.
- Use chapter batches as the default planning unit.
- Use one slide goal, one claim, and one layout family per slide.
- Assign one approved `reference shell` per slide during planning.
- Keep exception slides explicit: cover, agenda, section divider, synthesis, comparison, and other structural exceptions should be called out instead of being hidden inside normal content planning.
- Do not write final Korean slide copy in this stage.
- Do not write HTML in this stage.
- Keep internal planning artifacts in agent output or templates, and write only approved outcomes back into `slide-outline.md` and `manifest.md`.

## Workflow

1. Confirm the governed deck structure from `slide-outline-planner`.
2. Read the source prose for the target chapter batch.
3. Decide the slide count and slide order inside the batch.
4. For each slide, assign:
   - slide purpose
   - one-sentence claim
   - supporting points
   - must-keep terms
   - do-not-say items
   - recommended layout family
   - approved reference shell
   - evidence requirement
   - speaker intent
5. Mark slides that need exception handling and route them to the exception-slide workflow.
6. Return a clean handoff packet for Korean slide copy generation.

## Output Expectations

- A chapter-batch slide brief packet
- Clear separation between ordinary slides and exception slides
- Family assignment, reference shell, and evidence requirement for every slide
- Enough detail that Korean copy generation does not need to make structural decisions

## When To Load References

- Read [references/brief-contract.md](references/brief-contract.md) when writing slide briefs or chapter-batch packets.
- Read [references/batch-loop.md](references/batch-loop.md) when deciding gate boundaries, fan-out/fan-in flow, or exception-slide handling.

## Guardrails

- Do not invent claims that are not supported by the prose.
- Do not let one slide carry multiple unrelated objectives.
- Do not assign a slide family after the fact; choose it during planning.
- Do not leave shell selection implicit; every slide must name one approved shell before HTML work starts.
- Do not merge exception slides into ordinary chapter content just because they are nearby in order.
