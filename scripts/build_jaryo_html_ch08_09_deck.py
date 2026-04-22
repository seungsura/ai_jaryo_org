#!/usr/bin/env python3
from __future__ import annotations

import html
import json
from dataclasses import asdict
from pathlib import Path

from jaryo_html_deck.config import HTML_ROOT, THEME
from jaryo_html_deck.renderers import render_deck, render_slide_markup
from jaryo_html_deck.slides.chapter_08_09 import SLIDE_BUILDERS
from jaryo_html_deck.writer import write


CHAPTER_KEY = "chapter-08-09"
SLIDES_ROOT = HTML_ROOT / "slides" / CHAPTER_KEY
DECK_PATH = HTML_ROOT / "deck" / f"{CHAPTER_KEY}.html"
DATA_PATH = HTML_ROOT / "data" / f"{CHAPTER_KEY}-slide-specs.json"
LOCAL_IDS = [
    ("CH08-00", "ch08-00.html"),
    ("CH08-01", "ch08-01.html"),
    ("CH08-02", "ch08-02.html"),
    ("CH08-03", "ch08-03.html"),
    ("CH08-04", "ch08-04.html"),
    ("CH08-05", "ch08-05.html"),
    ("CH08-06", "ch08-06.html"),
    ("CH08-07", "ch08-07.html"),
    ("CH08-08", "ch08-08.html"),
    ("CH09-00", "ch09-00.html"),
    ("CH09-01", "ch09-01.html"),
    ("CH09-02", "ch09-02.html"),
    ("CH09-03", "ch09-03.html"),
]


def render_chapter_slide_file(spec) -> str:
    return "\n".join(
        [
            "<!DOCTYPE html>",
            '<html lang="ko">',
            "<head>",
            '<meta charset="UTF-8">',
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
            f"<title>{html.escape(spec.title)}</title>",
            '<link rel="icon" href="data:,">',
            '<link rel="stylesheet" href="../../shared/tokens.css">',
            '<link rel="stylesheet" href="../../shared/slide-base.css">',
            "</head>",
            f'<body class="{THEME}">',
            render_slide_markup(spec),
            "</body>",
            "</html>",
            "",
        ]
    )


def build_specs():
    specs = [build() for build in SLIDE_BUILDERS]
    for expected_order, spec in enumerate(specs, start=1):
        assert spec.order == expected_order, (expected_order, spec.slide_id)
    assert len(specs) == len(LOCAL_IDS), len(specs)
    for spec, (slide_id, file_name) in zip(specs, LOCAL_IDS, strict=True):
        spec.slide_id = slide_id
        spec.file_name = file_name
    return specs


def main() -> None:
    specs = build_specs()
    SLIDES_ROOT.mkdir(parents=True, exist_ok=True)
    for path in SLIDES_ROOT.glob("*.html"):
        path.unlink()

    for spec in specs:
        write(SLIDES_ROOT / spec.file_name, render_chapter_slide_file(spec))

    write(DECK_PATH, render_deck(specs))
    write(DATA_PATH, json.dumps([asdict(spec) for spec in specs], ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
