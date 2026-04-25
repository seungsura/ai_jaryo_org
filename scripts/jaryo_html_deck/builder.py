from __future__ import annotations

import json
from dataclasses import asdict

from .config import DATA_PATH, DECK_PATH, MANIFEST_PATH, OUTLINE_PATH, SCRIPT_PATH, SLIDES_ROOT
from .documents import render_manifest, render_outline, render_script
from .registry import build_all_specs
from .renderers import render_deck, render_slide_file
from .writer import clean_generated_slides, write


def main() -> None:
    specs = build_all_specs()
    clean_generated_slides()

    for spec in specs:
        write(SLIDES_ROOT / spec.file_name, render_slide_file(spec))

    write(OUTLINE_PATH, render_outline(specs))
    write(MANIFEST_PATH, render_manifest(specs))
    write(SCRIPT_PATH, render_script(specs))
    write(DECK_PATH, render_deck(specs))
    write(DATA_PATH, json.dumps([asdict(spec) for spec in specs], ensure_ascii=False, indent=2) + "\n")
