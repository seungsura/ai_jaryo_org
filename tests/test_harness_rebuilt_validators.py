from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "docs/02-seminar/harness-rebuilt-md"
BUILD_SCRIPT = ROOT / "scripts/build_harness_rebuilt_html_deck.py"
SHELL_CHECK = ROOT / "scripts/check_harness_rebuilt_shell_contract.py"
STYLE_CHECK = ROOT / "scripts/check_harness_rebuilt_style_rules.py"
SECTION_CHECK = ROOT / "scripts/check_harness_rebuilt_section_coverage.py"
DECK_CHECK = ROOT / "scripts/check_harness_rebuilt_deck_runtime.py"
EXPORT_SCRIPT = ROOT / "scripts/export_harness_rebuilt_pdf.py"


def run(cmd: list[str], *, expect_ok: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        cmd,
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if expect_ok and result.returncode != 0:
        raise AssertionError(f"command failed: {' '.join(cmd)}\nstdout={result.stdout}\nstderr={result.stderr}")
    return result


class HarnessRebuiltValidatorTest(unittest.TestCase):
    def build_fixture(self, tmpdir: str, *extra_args: str) -> Path:
        output_root = Path(tmpdir) / "docs/03-html/harness-rebuilt"
        run(
            [
                "python3",
                str(BUILD_SCRIPT),
                "--source-root",
                str(SOURCE_ROOT),
                "--output-root",
                str(output_root),
                *extra_args,
            ]
        )
        return output_root

    def test_generated_output_passes_all_validators(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            output_root = self.build_fixture(tmpdir)

            run(["python3", str(SHELL_CHECK), str(output_root)])
            run(["python3", str(STYLE_CHECK), str(output_root)])
            run(["python3", str(SECTION_CHECK), str(output_root)])
            run(["python3", str(DECK_CHECK), str(output_root / "deck/index.html")])

    def test_style_validator_rejects_broken_icon_cluster(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            output_root = self.build_fixture(tmpdir)
            specs = json.loads((output_root / "data/slide-specs.json").read_text(encoding="utf-8"))
            icon_slide = specs[0]
            slide_path = output_root / "slides" / icon_slide["file_name"]
            html = slide_path.read_text(encoding="utf-8")
            slide_path.write_text(
                html.replace("OpenCode</span>", "OpenCode Missing</span>", 1),
                encoding="utf-8",
            )

            result = run(["python3", str(STYLE_CHECK), str(output_root)], expect_ok=False)

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("icon cluster", result.stdout)

    def test_shell_validator_rejects_cover_with_extra_copy(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            output_root = self.build_fixture(tmpdir)
            specs = json.loads((output_root / "data/slide-specs.json").read_text(encoding="utf-8"))
            cover_slide = specs[0]
            slide_path = output_root / "slides" / cover_slide["file_name"]
            html = slide_path.read_text(encoding="utf-8")
            slide_path.write_text(
                html.replace("</section>", '<p class="content-body">불필요한 설명</p></section>', 1),
                encoding="utf-8",
            )

            result = run(["python3", str(SHELL_CHECK), str(output_root)], expect_ok=False)

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("cover-title-shell", result.stdout)

    def test_validators_accept_partial_build_scope(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            output_root = self.build_fixture(tmpdir, "--through-chapter", "01")

            run(["python3", str(SHELL_CHECK), str(output_root)])
            run(["python3", str(STYLE_CHECK), str(output_root)])
            run(["python3", str(SECTION_CHECK), str(output_root)])
            run(["python3", str(DECK_CHECK), str(output_root / "deck/index.html")])

    def test_pdf_export_reports_missing_runtime_clearly(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            output_root = self.build_fixture(tmpdir)
            pdf_path = Path(tmpdir) / "output/pdf/harness-rebuilt.pdf"

            result = run(
                [
                    "python3",
                    str(EXPORT_SCRIPT),
                    "--deck",
                    str(output_root / "deck/index.html"),
                    "--output",
                    str(pdf_path),
                    "--browser-command",
                    "/definitely/missing/browser",
                ],
                expect_ok=False,
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("No supported browser runtime", result.stdout)
            self.assertFalse(pdf_path.exists())


if __name__ == "__main__":
    unittest.main()
