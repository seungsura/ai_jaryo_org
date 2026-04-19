---
name: jaryo-html-slide-design
description: Design and refine HTML presentation slides for the Jaryo seminar from approved outline files. Use when turning `docs/02-seminar/prose/` into `docs/03-html/slides/slide-XX.html`, enforcing `docs/03-html/shared/design.md`, keeping `docs/03-html/manifest.md` synchronized, and validating browser rendering before export.
---

# Jaryo HTML Slide Design

## Overview

HTML/CSS code generation for this project is authored by Codex from approved outline, slide briefs, and approved Korean copy. This skill governs both HTML build discipline and post-build validation handoff.

## Core Rules

- Read `docs/03-html/shared/design.md` before any HTML generation or validation.
- Read `docs/03-html/shared/layout-shell-reference.md` before any HTML generation or validation.
- Read `docs/03-html/shared/minimal-light-adaptation.md` when the active theme is `theme-minimal-light`.
- Read [references/presentation-archetypes.md](references/presentation-archetypes.md) before selecting a slide structure.
- Read `docs/03-html/manifest.md` before slide work and update it whenever slide ids, ordering, section mapping, layout family, or implementation status change.
- Read `docs/03-html/outline/slide-outline.md` before design work. Do not bypass outline approval.
- Treat `docs/02-seminar/prose/` as the canonical content source for claims and wording.
- Treat approved slide briefs and approved Korean slide copy as required intermediates before HTML generation.
- Use only approved assets, citations, and visual evidence.
- Keep slide copy aligned with the design contract: Korean by default, short, direct, non-polite, scan-friendly, non-report-like, and free of translationese.
- Choose a named `layout family` before writing HTML.
- Choose an approved `reference shell` before writing HTML.
- Choose a `density` band before writing HTML.
- Build slides around placeholder roles, not around decorative wrappers.
- HTML/CSS generation is performed by Codex, not the Korean-writing model.
- Active deck palette is `theme-slate` unless the user explicitly asks for a study variant.
- Verify generated HTML slides in a real browser whenever layout quality matters.

## Workflow

1. Confirm the approved prose source, approved outline path, approved slide brief packet, approved Korean copy packet, and active design contract.
2. Read `docs/03-html/shared/design.md`, `docs/03-html/shared/layout-shell-reference.md`, `docs/03-html/shared/minimal-light-adaptation.md`, `docs/03-html/shared/tokens.css`, and `docs/03-html/manifest.md`.
3. Identify the slide intent first: `title`, `agenda`, `section`, `content`, `comparison`, `visual`, or `conclusion`.
4. Map that intent to one named layout family, one approved reference shell, and one density band in `docs/03-html/outline/slide-outline.md` and `docs/03-html/manifest.md`.
5. Define the placeholder plan: `title`, `lead`, `body`, `media`, `caption`, `footer-left`, `footer-right`.
6. Build or revise shared CSS / slide HTML with Codex while staying inside the approved family system.
7. Run `python3 scripts/check_slide_contract.py` and `python3 scripts/check_slide_korean.py docs/03-html/slides` after structural edits, then validate visually in the browser and note any overflow, overlap, density, hierarchy, title-wrap, chapter-label, or footer-consistency defects.
8. Update `docs/03-html/manifest.md` so the deck state remains auditable.
9. Hand off the exact post-HTML gate scope to deck-consistency and render validators.

## Output Expectations

- Codex-authored slide HTML that follows the approved outline, slide brief, Korean copy, layout family, density, reference shell, and design contract
- Shared tokens and reusable layout styling kept in `docs/03-html/shared/`
- Updated `docs/03-html/manifest.md`
- A short render verification note, automated check result, and post-HTML gate handoff when the change affects layout or export readiness

## Required Inputs

- `docs/03-html/outline/slide-outline.md`
- `docs/03-html/manifest.md`
- `docs/03-html/shared/design.md`
- `docs/03-html/shared/layout-shell-reference.md`
- `docs/03-html/shared/minimal-light-adaptation.md`
- `references/presentation-archetypes.md`
- `docs/02-seminar/prose/*.md`
- approved slide brief packet
- approved Korean slide copy packet

## Guardrails

- Do not treat HTML as the source of truth for content.
- Do not add a new layout family for a single slide if an existing family can express the content.
- Do not bypass the approved shell catalog with one-off wrappers or unnamed patterns.
- Do not leave the manifest stale after slide edits.
- Do not use decorative gradients, browser chrome, dashboard cards, pills, helper labels, or English UI copy unless the outline explicitly requires them as content.
- Do not write one-off compositions outside the shared layout family system.
- Do not generate HTML before the slide brief and Korean copy gates pass.
- Do not rewrite approved Korean copy into flatter report-style wording while fitting it into HTML.
- Do not let translationese sneak into visible Korean labels, headings, or body text.
- Do not use polite Korean endings in slide copy.
- Do not ship without browser-based render verification.
