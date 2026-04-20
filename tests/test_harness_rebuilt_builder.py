from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILD_SCRIPT = ROOT / "scripts/build_harness_rebuilt_html_deck.py"
SOURCE_ROOT = ROOT / "docs/02-seminar/harness-rebuilt-md"


def run_builder(output_root: Path, *extra_args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            "python3",
            str(BUILD_SCRIPT),
            "--source-root",
            str(SOURCE_ROOT),
            "--output-root",
            str(output_root),
            *extra_args,
        ],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )


class HarnessRebuiltBuilderTest(unittest.TestCase):
    def test_builder_generates_expected_artifacts_and_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            output_root = Path(tmpdir) / "docs/03-html/harness-rebuilt"
            run_builder(output_root)

            outline_path = output_root / "outline/slide-outline.md"
            manifest_path = output_root / "manifest.md"
            briefs_path = output_root / "briefs/chapter-01.md"
            copy_path = output_root / "copy/chapter-01.md"
            specs_path = output_root / "data/slide-specs.json"
            review_path = output_root / "data/chapter-review-metadata.json"
            deck_path = output_root / "deck/index.html"

            for path in [
                outline_path,
                manifest_path,
                briefs_path,
                copy_path,
                specs_path,
                review_path,
                deck_path,
                output_root / "shared/tokens.css",
                output_root / "shared/slide-base.css",
                output_root / "shared/deck.css",
            ]:
                self.assertTrue(path.exists(), path)

            specs = json.loads(specs_path.read_text(encoding="utf-8"))
            chapter_meta = json.loads(review_path.read_text(encoding="utf-8"))

            self.assertGreater(len(specs), 100)
            self.assertEqual(specs[0]["slide_kind"], "cover")
            self.assertEqual(specs[0]["shell"], "cover-title-shell")

            chapter_transitions = [spec for spec in specs if spec["slide_kind"] == "chapter-transition"]
            self.assertEqual(len(chapter_transitions), 9)
            self.assertEqual(
                {spec["shell"] for spec in specs},
                {
                    "cover-title-shell",
                    "chapter-transition-shell",
                    "content-essay-shell",
                    "content-card-shell",
                    "content-emphasis-shell",
                },
            )

            self.assertIn("01", chapter_meta)
            self.assertIn("chapter_01_special_decomposition", chapter_meta["01"]["special_rules"])
            chapter_01_opening = next(row for row in chapter_meta["01"]["section_coverage"] if row["block_id"] == "01-01")
            self.assertEqual(chapter_01_opening["slide_count"], 5)
            self.assertTrue(
                any("page-003.jpg" in asset for asset in chapter_meta["01"]["footnote_assets"]),
                chapter_meta["01"]["footnote_assets"],
            )

            cover_html = (output_root / "slides" / specs[0]["file_name"]).read_text(encoding="utf-8")
            self.assertIn('class="theme-minimal-light"', cover_html)
            self.assertIn('data-shell="cover-title-shell"', cover_html)
            self.assertIn('class="cover-title"', cover_html)
            self.assertIn('class="cover-subtitle"', cover_html)
            self.assertIn('class="cover-author"', cover_html)
            self.assertNotIn("cover-kicker", cover_html)
            self.assertNotIn("cover-points", cover_html)
            self.assertIn(">게임플랫폼 1팀 라승수<", cover_html)

            transition_html = (
                output_root / "slides" / chapter_transitions[0]["file_name"]
            ).read_text(encoding="utf-8")
            self.assertIn('class="transition-title"', transition_html)
            self.assertNotIn("chapter-summary", transition_html)
            self.assertNotIn("chapter-keywords", transition_html)

    def test_builder_keeps_each_source_block_within_one_to_five_slides(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            output_root = Path(tmpdir) / "docs/03-html/harness-rebuilt"
            run_builder(output_root)

            chapter_meta = json.loads(
                (output_root / "data/chapter-review-metadata.json").read_text(encoding="utf-8")
            )

            coverage_rows = []
            for meta in chapter_meta.values():
                coverage_rows.extend(meta["section_coverage"])

            self.assertTrue(coverage_rows)
            for row in coverage_rows:
                self.assertGreaterEqual(row["slide_count"], 1, row)
                self.assertLessEqual(row["slide_count"], 5, row)

    def test_builder_supports_incremental_builds_through_selected_chapter(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            output_root = Path(tmpdir) / "docs/03-html/harness-rebuilt"
            run_builder(output_root, "--through-chapter", "01")

            specs = json.loads((output_root / "data/slide-specs.json").read_text(encoding="utf-8"))
            review_meta = json.loads((output_root / "data/chapter-review-metadata.json").read_text(encoding="utf-8"))
            manifest = (output_root / "manifest.md").read_text(encoding="utf-8")

            self.assertEqual(sorted(review_meta.keys()), ["00", "01"])
            self.assertEqual(sorted({spec["chapter_id"] for spec in specs}), ["00", "01"])
            self.assertEqual(len([spec for spec in specs if spec["slide_kind"] == "chapter-transition"]), 1)
            self.assertIn("chapter-01.md", manifest)
            self.assertNotIn("chapter-02.md", manifest)
            self.assertFalse((output_root / "briefs/chapter-02.md").exists())
            self.assertFalse((output_root / "copy/chapter-02.md").exists())


if __name__ == "__main__":
    unittest.main()
