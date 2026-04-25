#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from html import unescape
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
TRANSLATIONESE_RE = re.compile(
    r"(상류|하류|강하게\s*호출|의\s*측면에서|라고\s*볼\s*수\s*있다|라\s*볼\s*수\s*있다|핵심은\s*.{0,20}\s*데\s*있다)"
)
AWKWARD_VERB_RE = re.compile(r"(수행하|제공하|처리하|활용하)(?:는|고|며|면|다|기|게|도록|지|자|라|여|해)")
AWKWARD_SLIDE_COPY_RE = re.compile(r"(passage\s*검색|retriever\s*품질|컨텍스트로\s*주입)")
SOURCE_META_PREFIXES = ("Sources:",)
DIRECT_QUOTE_EXCEPTIONS = {
    "모델이 아닌 것은 전부 하네스입니다.",
    "하네스 시대에는 잘 쓰는 것 못지않게 안 바꾸는 것도 능력입니다.",
    "WHAT/WHY와 HOW를 분리하고, 모호한 부분은 [NEEDS CLARIFICATION]에서 멈춘다.",
    "테스트를 먼저 쓰고, 통과하는 코드를 나중에 쓴다. AI 시대에는 인간이 테스트, AI가 구현.",
    "AI는 \"동작하는 것 같은\" 코드를 자신 있게 만듦. 테스트 없으면 맞는지 틀린지 확인 불가.",
    "테스트 수정 금지 규칙 필수. 테스트 코드 임의 수정 금지 · assert 조건 약화 · 실패 확인 전 구현 금지.",
    "\"지식이 쌓이는 속도보다 감가상각되는 속도가 더 빠르다. 나도 지쳤다.\"",
}
IGNORE_LINE_RE = re.compile(
    r"^(S\d+\.)|^(CHAPTER\s+\d+)$|^Harness 잘 사용하기$|^\d+$|^(<!DOCTYPE|<html|<head|<meta|<link|<main|</|class=|data-)"
)


def iter_targets(argv: list[str]) -> list[Path]:
    return [Path(arg).resolve() for arg in argv] if argv else [DEFAULT_TARGET]


def expand_files(target: Path) -> list[Path]:
    if target.is_dir():
        if target.resolve() == DEFAULT_TARGET.resolve():
            return sorted(
                path
                for path in target.glob("slide-*.html")
                if path.is_file()
            )
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
    return unescape(line.strip())


def iter_text_segments(raw_line: str) -> list[str]:
    html_split = re.sub(r"<[^>]+>", "\n", raw_line)
    segments: list[str] = []
    for part in html_split.splitlines():
        text = strip_markup(part)
        if text:
            segments.append(text)
    return segments


def analyze_file(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    for line_no, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw_line.strip():
            continue

        for text in iter_text_segments(raw_line):
            if IGNORE_LINE_RE.search(text):
                continue
            if text.startswith(SOURCE_META_PREFIXES):
                continue
            if text in DIRECT_QUOTE_EXCEPTIONS:
                continue
            if "/speckit." in text:
                continue

            if POLITE_ENDING_RE.search(text):
                errors.append(f"{path}:{line_no} 공손체 ending 감지: {text}")

            if TRANSLATIONESE_RE.search(text):
                errors.append(f"{path}:{line_no} 번역체/어색한 한국어 표현 감지: {text}")

            if AWKWARD_SLIDE_COPY_RE.search(text):
                errors.append(f"{path}:{line_no} slide-specific 어색한 번역투 감지: {text}")

            if len(text) > 52:
                errors.append(f"{path}:{line_no} slide copy가 너무 김: {text}")
            elif len(text) > 38:
                warnings.append(f"{path}:{line_no} slide copy 길이 주의: {text}")

            if PROSE_ENDING_RE.search(text) and len(text) > 20:
                warnings.append(f"{path}:{line_no} prose-like 문장 ending 의심: {text}")

            if REPORT_STYLE_RE.search(text) and len(text) > 18:
                warnings.append(f"{path}:{line_no} 보고서형 연결어 의심: {text}")

            if AWKWARD_VERB_RE.search(text) and len(text) > 14:
                warnings.append(f"{path}:{line_no} 어색한 서술 동사 의심: {text}")

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
