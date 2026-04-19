---
name: jaryo-doc-reconstruction
description: Reconstruct and iteratively refine long-form source documents for the Jaryo project from local markdown and user-supplied text materials. Use when turning page-based OCR markdown into coherent prose docs under `docs/02-seminar/prose/`, improving draft quality through user dialogue, absorbing newly collected documents into `docs/01-sources/`, mapping source fragments to target sections, or tracking missing content without consulting JPG/PDF assets unless the user explicitly changes that rule.
---

# Jaryo Doc Reconstruction

## Overview

Rebuild source-quality documentation from the markdown files in this repository and improve it through repeated review conversations with the user. Treat local markdown and user-supplied text materials as the authoritative source unless the user explicitly permits visual assets.

## Core Rules

- Read local `*.md` files first and treat them as the source of truth.
- Accept additional user-supplied markdown, notes, transcripts, or text summaries as new source material after mapping them into the existing structure.
- Do not inspect `assets/`, JPG, PNG, or PDF files unless the user explicitly changes the source policy.
- Rewrite OCR-like fragments into coherent prose, but do not invent facts that are missing from the markdown.
- Record ambiguity, missing evidence, or conflicting phrasing in `docs/01-sources/intake/open-questions.md` instead of guessing.
- Prefer section-scoped files under `docs/02-seminar/prose/` over one giant document unless the user explicitly wants a monolith.
- Keep future slide regeneration in mind: preserve section boundaries, strong headings, and claims that can later collapse back into slides.
- Follow the repository seminar voice policy: prose should read like a dense technical blog essay, not a report or translated methodology memo.
- Avoid translationese and dead explanatory phrasing when a sharper Korean sentence is available.
- After each meaningful draft or revision pass, prepare focused follow-up questions for the user instead of silently making speculative editorial decisions.

## Workflow

1. Inventory the available markdown sources and identify repeated section titles, themes, and overlaps.
2. Build or confirm a target documentation tree before drafting prose. Use [references/structure.md](references/structure.md) for the default layout.
3. Map page ranges, source fragments, or newly collected materials to target sections.
4. Draft or revise one section at a time in prose form.
5. Cross-check terminology and claims across related markdown files before finalizing a section.
6. After each pass, return a short editorial review packet: what changed, what still feels weak, and what specific questions should be asked to the user next.
7. Promote all unresolved issues to `docs/01-sources/intake/open-questions.md` using the output contract in [references/output-contract.md](references/output-contract.md).

## Output Expectations

- Produce readable narrative prose, not slide bullets.
- Preserve the original argument order when it is recoverable from the markdown.
- Distinguish recovered facts from editorial smoothing.
- Surface missing content early so the user can fill the gap collaboratively.
- Ask at most 1 to 3 high-value follow-up questions when user input would materially improve the document.
- When new source material appears, explain exactly which section it strengthens, changes, or contradicts.

## When To Load References

- Read [references/structure.md](references/structure.md) when deciding the pipeline file tree or section splits.
- Read [references/output-contract.md](references/output-contract.md) when preparing section maps, draft outputs, or open-question logs.
- Read [references/collaboration-loop.md](references/collaboration-loop.md) when improving draft quality through user dialogue or integrating newly collected materials.
- Read [references/tone-rules.md](references/tone-rules.md) when prose starts drifting into report-style or translated-Korean phrasing.

## Example Triggers

- "프로젝트 md 파일을 기준으로 원문 문서를 복원해줘"
- "슬라이드 전사본을 줄글 문서로 다시 써줘"
- "docs 파이프라인 구조를 먼저 잡고 섹션별로 정리하자"
- "jpg/pdf는 보지 말고 markdown만으로 정리해줘"
- "문서를 정리한 뒤 나와 대화하면서 퀄리티를 올려줘"
- "새로 수집한 자료를 기존 문서에 어디에 녹일지 먼저 판단해줘"
