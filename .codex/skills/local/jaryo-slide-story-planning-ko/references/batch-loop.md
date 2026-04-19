# Chapter Batch Loop

Use chapter batches as the default planning unit.

## Default Loop

1. `slide-outline-planner`
   - locks chapter order, batch boundaries, slide allocation, and family distribution
2. `chapter-slide-pm-ko`
   - writes briefs for ordinary slides in one batch
3. `exception-slide-pm-ko`
   - handles special slides when needed
4. hand off approved briefs to Korean slide copy generation

## Batch Boundaries

- Prefer one chapter or one stable theme per batch.
- A batch should be small enough that storyline review can judge it as one sequence.
- If a chapter contains many special slide types, split the batch before copy generation rather than after HTML.

## Exception Slide Rule

Route a slide to exception planning when:

- it is the cover
- it is the agenda
- it is a section divider
- it is a synthesis slide
- it is a comparison slide whose structure is the main message

Do not treat every visually different slide as an exception. The exception decision is about structural role, not just appearance.
