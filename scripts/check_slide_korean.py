#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TARGET = ROOT / "docs/03-html/slides"
IGNORED_BASENAMES = {
    "README.md",
    "design.md",
    "manifest.md",
    "slide-outline.md",
    "layout-shell-reference.md",
}

POLITE_ENDING_RE = re.compile(r"(습니다|입니다|했습니다|되었습니다|하십시오|하세요|드립니다|합니다)(?:[.?!]|$)")
PROSE_ENDING_RE = re.compile(r"(이다|한다|된다|있다|없다|보인다|의미한다|설명한다)(?:[.?!]|$)")
REPORT_STYLE_RE = re.compile(r"(또한|따라서|그러나|한편|통하여|위하여|기반으로|관련하여)")
IGNORE_LINE_RE = re.compile(
    r"^(S\d+\.)|^(CHAPTER\s+\d+)$|^Harness 잘 사용하기$|^\d+$|^(<!DOCTYPE|<html|<head|<meta|<link|<main|</|class=|data-)"
)


def iter_targets(argv: list[str]) -> list[Path]:
    return [Path(arg).resolve() for arg in argv] if argv else [DEFAULT_TARGET]


def expand_files(target: Path) -> list[Path]:
    if target.is_dir():
        return sorted(
            path
            for path in target.rglob("*")
            if path.suffix.lower() in {".html", ".md", ".txt"}
            and path.name not in IGNORED_BASENAMES
        )
    return [target] if target.exists() else []


def strip_markup(line: str) -> str:
    line = re.sub(r"<[^>]+>", " ", line)
    line = re.sub(r"`[^`]+`", " ", line)
    line = re.sub(r"\[[^\]]+\]\([^)]+\)", " ", line)
    line = re.sub(r"[*_>#-]", " ", line)
    line = re.sub(r"\s+", " ", line)
    return line.strip()


def analyze_file(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    for line_no, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw_line.strip():
            continue
        if IGNORE_LINE_RE.search(raw_line.strip()):
            continue

        text = strip_markup(raw_line)
        if not text or IGNORE_LINE_RE.search(text):
            continue

        if POLITE_ENDING_RE.search(text):
            errors.append(f"{path}:{line_no} 공손체 ending 감지: {text}")

        if len(text) > 52:
            errors.append(f"{path}:{line_no} slide copy가 너무 김: {text}")
        elif len(text) > 38:
            warnings.append(f"{path}:{line_no} slide copy 길이 주의: {text}")

        if PROSE_ENDING_RE.search(text) and len(text) > 20:
            warnings.append(f"{path}:{line_no} prose-like 문장 ending 의심: {text}")

        if REPORT_STYLE_RE.search(text) and len(text) > 18:
            warnings.append(f"{path}:{line_no} 보고서형 연결어 의심: {text}")

    return errors, warnings


def main(argv: list[str]) -> int:
    targets = iter_targets(argv)
    files = sorted({path for target in targets for path in expand_files(target)})

    if not files:
        print("ERROR no analyzable slide or copy files found for Korean tone check")
        return 1

    errors: list[str] = []
    warnings: list[str] = []
    for path in files:
        file_errors, file_warnings = analyze_file(path)
        errors.extend(file_errors)
        warnings.extend(file_warnings)

    for warning in warnings:
        print(f"WARN {warning}")

    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1

    print(f"OK Korean tone check passed for {len(files)} files")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
