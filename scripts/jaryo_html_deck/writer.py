from __future__ import annotations

from pathlib import Path

from .config import SLIDES_ROOT

def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

def clean_generated_slides() -> None:
    SLIDES_ROOT.mkdir(parents=True, exist_ok=True)
    for path in SLIDES_ROOT.glob("slide-*.html"):
        path.unlink()
