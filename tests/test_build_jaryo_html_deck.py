from __future__ import annotations

import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILD_SCRIPT = ROOT / "scripts/build_jaryo_html_deck.py"
MANIFEST_PATH = ROOT / "docs/03-html/manifest.md"
OUTLINE_PATH = ROOT / "docs/03-html/outline/slide-outline.md"
DECK_PATH = ROOT / "docs/03-html/deck/index.html"
SCRIPT_PATH = ROOT / "docs/03-html/deck/script.md"
SLIDES_DIR = ROOT / "docs/03-html/slides"


def run_builder() -> None:
    subprocess.run(
        ["python3", str(BUILD_SCRIPT)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )


def manifest_rows() -> list[str]:
    rows: list[str] = []
    in_registry = False
    for raw_line in MANIFEST_PATH.read_text(encoding="utf-8").splitlines():
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
        rows.append(line)
    return rows


class BuildJaryoHtmlDeckTest(unittest.TestCase):
    def test_builder_generates_132_slide_registry(self) -> None:
        run_builder()

        rows = manifest_rows()
        self.assertEqual(len(rows), 132)
        self.assertIn("`S001`", rows[0])
        self.assertIn("`S132`", rows[-1])

    def test_builder_uses_three_digit_slide_files(self) -> None:
        run_builder()

        slide_files = sorted(SLIDES_DIR.glob("slide-*.html"))
        self.assertEqual(len(slide_files), 132)
        self.assertEqual(slide_files[0].name, "slide-001.html")
        self.assertEqual(slide_files[-1].name, "slide-132.html")

    def test_builder_writes_outline_deck_and_script(self) -> None:
        run_builder()

        outline = OUTLINE_PATH.read_text(encoding="utf-8")
        deck = DECK_PATH.read_text(encoding="utf-8")

        self.assertIn("### S001.", outline)
        self.assertIn("### S132.", outline)
        self.assertTrue(SCRIPT_PATH.exists())
        self.assertIn('data-slide-id="S001"', deck)
        self.assertIn('data-slide-id="S132"', deck)
        self.assertIn("function goTo(index)", deck)


if __name__ == "__main__":
    unittest.main()
