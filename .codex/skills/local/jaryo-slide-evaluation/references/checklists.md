# Gate Checklists

## Storyline Gate

- Do titles alone form a sensible sequence?
- Are chapter transitions explicit enough?
- Is any slide duplicating another slide's claim?
- Is there a narrative jump that the audience would feel?
- Does each slide stay inside its approved shell role instead of drifting into another pattern?

## Korean Tone Gate

- Does the copy sound like slide language rather than report prose?
- Is the Korean awkward, overly translated, or dense?
- Does each slide keep one purpose?
- Are must-keep terms preserved without making the slide unreadable?
- Did `scripts/check_slide_korean.py` return any hard errors?

## HTML Deck Consistency Gate

- Do slide families look like members of one deck system?
- Are footer, chapter marker, and title-band rules consistent?
- Do exception slides still feel part of the same deck?
- Does the deck rhythm avoid random visual drift?
- Does each slide declare the same shell id that outline and manifest expect?

## HTML Render Gate

- Is there any overflow or clipping?
- Do no-wrap titles actually stay on one line?
- Are chapter markers and footers positioned correctly?
- Are there browser-rendering defects that block review or export?
- Did `scripts/check_slide_contract.py` fail on structure or manifest sync?
