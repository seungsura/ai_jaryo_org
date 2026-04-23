from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HTML_ROOT = ROOT / "docs/03-html"
OUTLINE_PATH = HTML_ROOT / "outline/slide-outline.md"
MANIFEST_PATH = HTML_ROOT / "manifest.md"
SLIDES_ROOT = HTML_ROOT / "slides"
DECK_ROOT = HTML_ROOT / "deck"
DECK_PATH = DECK_ROOT / "index.html"
SCRIPT_PATH = DECK_ROOT / "script.md"
DATA_PATH = HTML_ROOT / "data/slide-specs.json"
SHARED_ROOT = HTML_ROOT / "shared"
TOKENS_CSS = SHARED_ROOT / "tokens.css"
BASE_CSS = SHARED_ROOT / "slide-base.css"
ICON_ROOT = ROOT / "assets/icons"
TOOLCARD_ICON_ROOT = ICON_ROOT / "toolcards"

THEME = "theme-minimal-light"
FOOTER_LEFT = "Harness 잘 사용하기"
SOURCE_ROOT = ROOT / "docs/02-seminar/harness-rebuilt-md"

SECTION_TARGETS = {
    "00": 3,
    "01": 11,
    "02": 11,
    "03": 6,
    "04": 12,
    "05": 10,
    "06": 13,
    "07": 13,
    "08": 9,
    "09": 4,
}
