#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "docs/03-html/manifest.md"


def parse_manifest(path: Path) -> list[str]:
    slide_ids: list[str] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    in_registry = False
    for raw_line in lines:
        line = raw_line.strip()
        if line.startswith("| order | slide id |"):
            in_registry = True
            continue
        if not in_registry:
            continue
        if not line.startswith("|"):
            break
        normalized = line.replace("|", "").replace(" ", "")
        if normalized and set(normalized) == {"-"}:
            continue
        parts = [part.strip().strip("`") for part in line.strip("|").split("|")]
        if len(parts) < 2:
            continue
        slide_ids.append(parts[1])
    return slide_ids


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print("ERROR usage: python3 scripts/check_deck_runtime.py docs/03-html/deck/index.html")
        return 1

    target = Path(argv[0]).resolve()
    if not target.exists():
        print(f"ERROR missing deck file: {target}")
        return 1

    slide_ids = parse_manifest(MANIFEST_PATH)
    html = target.read_text(encoding="utf-8")
    errors: list[str] = []

    if not slide_ids:
        errors.append(f"manifest slide registry not found: {MANIFEST_PATH}")

    wrappers = re.findall(r'class="deck-slide(?: active)?"', html)
    if len(wrappers) != len(slide_ids):
        errors.append(f"deck slide count mismatch: deck has {len(wrappers)}, manifest has {len(slide_ids)}")

    if 'class="deck"' not in html:
        errors.append('missing deck root class="deck"')

    required_snippets = [
        "function updateScale()",
        "function goTo(index)",
        "ArrowRight",
        "ArrowLeft",
        "touchstart",
        "touchend",
        "@media print",
        "--deck-scale",
    ]
    for snippet in required_snippets:
        if snippet not in html:
            errors.append(f"missing runtime snippet: {snippet}")

    forbidden = ["progress-bar", "fullscreen-btn", "slide-counter", "notes-panel"]
    for snippet in forbidden:
        if snippet in html:
            errors.append(f"deck includes forbidden UI chrome: {snippet}")

    active_count = len(re.findall(r'class="deck-slide active"', html))
    if active_count != 1:
        errors.append(f"deck must have exactly one active slide wrapper (found {active_count})")

    for slide_id in slide_ids:
        if f'data-slide-id="{slide_id}"' not in html:
            errors.append(f"missing slide id in deck: {slide_id}")

    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1

    print(f"OK deck runtime passed for {len(slide_ids)} slides")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
