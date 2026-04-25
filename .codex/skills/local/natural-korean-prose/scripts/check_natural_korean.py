#!/usr/bin/env python3
"""Lightweight candidate scanner for awkward Korean in Jaryo prose.

The scanner reports review candidates. It is intentionally conservative and
does not know context, so hits are prompts for human/editorial judgment.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


PATTERNS: list[tuple[str, str]] = [
    (r"장표", "Use 슬라이드 or 발표 자료."),
    (r"이 장에서|이 장은|이 장의|앞 장|다음 장", "Use 챕터 wording for presentation flow."),
    (r"측면에서", "Often a translationese frame; state the claim directly."),
    (r"라고 볼 수 있다", "Weak report ending; use a direct claim when evidence supports it."),
    (r"핵심은.{0,24}데 있다", "Methodology-translation rhythm; rewrite directly."),
    (r"강하게 호출", "English-like abstraction; use a natural Korean verb."),
    (r"상류|하류", "Imported process metaphor; check if 앞단/뒤쪽 is clearer."),
    (r"에 의해", "Passive translationese candidate."),
    (r"되어진|되어질|되어져", "Double passive candidate."),
    (r"수행된다|수행되었다|수행될", "Stiff passive verb candidate."),
    (r"기반으로 하여", "Stiff connector; shorten or use a real verb."),
]


def iter_markdown_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_dir():
            files.extend(sorted(path.rglob("*.md")))
        elif path.suffix == ".md":
            files.append(path)
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan Korean prose for translationese candidates.")
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--fail-on-hit", action="store_true")
    args = parser.parse_args()

    hits = 0
    for file_path in iter_markdown_files(args.paths):
        text = file_path.read_text(encoding="utf-8")
        for line_no, line in enumerate(text.splitlines(), start=1):
            for pattern, note in PATTERNS:
                if re.search(pattern, line):
                    hits += 1
                    print(f"{file_path}:{line_no}: {note}\n  {line.strip()}")
                    break

    return 1 if hits and args.fail_on_hit else 0


if __name__ == "__main__":
    raise SystemExit(main())
