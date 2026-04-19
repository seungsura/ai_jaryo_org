---
name: jaryo-slide-copy-ko
description: Generate and refine Korean slide copy and speaker notes for the Jaryo seminar using Gemini. Use when turning approved slide briefs into Korean titles, leads, body copy, or spoken notes with the fixed model `gemini-3.1-pro-preview`.
---

# Jaryo Slide Copy KO

## Overview

Use this skill for Korean slide wording after the planning layer is approved. Gemini handles the Korean drafting, while Codex preserves the workflow, contract, and review gates.

## Core Rules

- Use Gemini for all Korean drafting and revision in this layer.
- Fix the model name to `gemini-3.1-pro-preview`.
- Work from approved slide briefs, not from raw prose alone.
- Keep the wording faithful to the approved claim and supporting points.
- Treat the approved `reference shell` as fixed; wording should fit the shell rather than forcing shell drift later.
- Optimize for slide readability and spoken delivery, not prose fullness.
- When the active theme is `theme-minimal-light`, shorten wording further so bright minimal layouts do not expose copy density.
- Preserve must-keep English terms exactly when the brief requires them.
- Keep copy concise, non-polite, and presentation-oriented.
- Do not generate HTML in this layer.

## Workflow

1. Read the approved brief packet and the relevant source passages.
2. Prepare a Gemini prompt that includes:
   - slide purpose
   - one-sentence claim
   - supporting points
   - must-keep terms
   - do-not-say list
   - target family
   - approved reference shell
   - active theme and its density constraints
3. Call Gemini with `gemini -m gemini-3.1-pro-preview`.
4. Run `python3 scripts/check_slide_korean.py <copy-packet-or-html-path>` when a local text packet exists.
5. Return slide-by-slide Korean copy with any wording risks called out.
6. For speaker notes, keep the same model and adapt wording for spoken flow instead of slide scanability.

## Output Expectations

- Slide-ready Korean title / lead / body wording
- Explicit wording-risk notes when Gemini produces awkward or over-dense output
- Speaker notes that follow the same approved storyline without inventing claims

## When To Load References

- Read [references/gemini-invocation.md](references/gemini-invocation.md) when preparing or reviewing the Gemini invocation contract.
- Read [references/tone-rules.md](references/tone-rules.md) when judging whether wording feels presentation-ready or spoken-ready.

## Guardrails

- Do not let Gemini choose the slide structure; structure comes from the approved brief.
- Do not accept report-style Korean just because it is grammatical.
- Do not change must-keep terms unless the brief explicitly allows it.
- Do not allow model-name drift away from `gemini-3.1-pro-preview`.
