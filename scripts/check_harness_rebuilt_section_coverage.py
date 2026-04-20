#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

from harness_rebuilt_pipeline import load_review_meta


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print("ERROR usage: python3 scripts/check_harness_rebuilt_section_coverage.py <output-root>")
        return 1

    output_root = Path(argv[0]).resolve()
    review_meta = load_review_meta(output_root)
    errors: list[str] = []
    checked = 0

    for chapter_id, meta in sorted(review_meta.items()):
        if chapter_id != "00" and not meta.get("transition_slide_id"):
            errors.append(f"{chapter_id}: missing chapter transition slide")
        for row in meta["section_coverage"]:
            checked += 1
            count = row["slide_count"]
            if count < 1 or count > 5:
                errors.append(f"{chapter_id}:{row['block_id']} coverage must be 1-5 slides (found {count})")

    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1

    print(f"OK section coverage passed for {checked} source blocks")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
