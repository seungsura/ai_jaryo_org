#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print("ERROR usage: python3 scripts/check_harness_rebuilt_deck_runtime.py <deck-index.html>")
        return 1

    deck_path = Path(argv[0]).resolve()
    if not deck_path.exists():
        print(f"ERROR missing deck file: {deck_path}")
        return 1

    output_root = deck_path.parents[1]
    specs_path = output_root / "data/slide-specs.json"
    specs = json.loads(specs_path.read_text(encoding="utf-8"))
    html = deck_path.read_text(encoding="utf-8")
    errors: list[str] = []

    wrappers = re.findall(r'class="deck-slide(?: active)?"', html)
    if len(wrappers) != len(specs):
        errors.append(f"deck slide count mismatch: deck has {len(wrappers)}, specs has {len(specs)}")
    if 'class="deck"' not in html:
        errors.append('missing deck root class="deck"')
    if html.count('class="deck-slide active"') != 1:
        errors.append("deck must contain exactly one active slide")
    if '<body class="theme-minimal-light">' not in html:
        errors.append("deck body must declare theme-minimal-light")

    required = [
        "function updateScale()",
        "function goTo(index)",
        "ArrowRight",
        "ArrowLeft",
        "touchstart",
        "touchend",
        "@media print",
        "--deck-scale",
    ]
    for snippet in required:
        if snippet not in html:
            errors.append(f"missing runtime snippet: {snippet}")

    forbidden = [
        "deck-status",
        "fullscreen",
        'class="notes-panel"',
        "speaker-notes-panel",
    ]
    for snippet in forbidden:
        if snippet in html:
            errors.append(f"forbidden runtime chrome detected: {snippet}")

    for spec in specs:
        if f'data-slide-id="{spec["slide_id"]}"' not in html:
            errors.append(f"missing slide in deck: {spec['slide_id']}")

    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1

    print(f"OK deck runtime passed for {len(specs)} slides")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
