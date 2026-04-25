---
name: natural-korean-prose
description: Use when writing, revising, or reviewing Korean prose and slide copy in this repository, especially to remove translationese, stiff AI-generated Korean, bureaucratic phrasing, unnatural English-to-Korean word order, or awkward seminar narration while preserving technical precision.
---

# Natural Korean Prose

## Purpose

Use this skill whenever Korean wording quality matters. The goal is not "simpler Korean" in the abstract. The goal is Korean that sounds written in Korean first: natural word order, clear subject-verb relationships, living verbs, precise technical terms, and a rhythm that fits the Jaryo seminar voice.

For `docs/02-seminar/prose/`, the default voice is spoken Korean that the presenter can actually say aloud, with the density of a technical blog essay. Do not turn it into a public notice, product manual, bland summary, or loose chat transcript.

## Source Basis

This skill adapts stable principles from Korean public-language guidance, especially the Ministry of Culture, Sports and Tourism and National Institute of Korean Language guide `쉬운 공공언어 쓰기`: write from the reader's position, choose familiar words where precision allows, make sentences clear, keep sentence elements in agreement, avoid unnecessary passive/causative and translationese, and check ambiguity.

Those principles are adapted here for technical seminar prose. Public-document politeness and bureaucratic neutrality are not imported.

## Workflow

1. Preserve the claim, source boundary, and technical precision before changing style.
2. Decide the surface:
   - prose: spoken, presentation-ready technical essay; natural when read aloud.
   - slide copy: compressed phrase or noun phrase, source-backed, scan-friendly.
   - conversation: natural Korean explanation without editorial jargon.
3. Run the translationese pass:
   - replace English word order with Korean word order.
   - prefer active verbs when the actor matters.
   - reduce noun piles and `A의 B의 C` chains.
   - remove unnecessary `~에 의해`, `~을 통해서`, `~의 측면에서`, `~라고 볼 수 있다`.
   - split a sentence when one sentence carries two claims.
4. Run the seminar voice pass:
   - keep strong claims when they are source-backed.
   - remove report-style connectors and padded summaries.
   - avoid meme tone, empty hype, and decorative literary phrasing.
5. Run the local scanner when useful:

```bash
python3 .codex/skills/local/natural-korean-prose/scripts/check_natural_korean.py docs/02-seminar/prose
```

Use scanner hits as review candidates, not automatic failures. Context decides.

## When To Load References

- Read [references/translationese-checklist.md](references/translationese-checklist.md) before a Korean prose quality pass, broad chapter rewrite, or slide-copy review.
- Use the checklist table when explaining why a sentence feels awkward.

## Hard Rules For Jaryo

- `장표` is not used in prose or spoken script. Use `슬라이드` or `발표 자료`.
- In presentation prose, use `이 챕터에서`, `앞 챕터`, `다음 챕터` instead of chapter-flow wording that sounds like a report.
- Keep English for product names, APIs, commands, paths, protocols, method names, and technical terms whose Korean translation would reduce precision.
- Do not replace every English term with a pure Korean word. Natural Korean in this project means Korean syntax around precise technical vocabulary.
- Prose may become spoken and presentation-ready; slide copy keeps the existing rule: compressed Korean phrases, noun phrases, and source-backed visible text rather than full spoken sentences.
