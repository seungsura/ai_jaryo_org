#!/usr/bin/env python3
from __future__ import annotations

import html as html_lib
import re
import sys
from pathlib import Path

from harness_rebuilt_pipeline import ICON_CLUSTER_ITEMS, POLITE_ENDING_RE, REPORT_STYLE_RE, load_specs


TEXT_RE = re.compile(r">([^<>]+)<")
STYLE_SCRIPT_RE = re.compile(r"<style\b.*?</style>|<script\b.*?</script>", re.IGNORECASE | re.DOTALL)


def strip_tags(html: str) -> list[str]:
    html = STYLE_SCRIPT_RE.sub("", html)
    return [
        re.sub(r"\s+", " ", html_lib.unescape(part)).strip()
        for part in TEXT_RE.findall(html)
        if part.strip()
    ]


def class_count(html: str, class_name: str) -> int:
    count = 0
    for attr in re.findall(r'class="([^"]+)"', html):
        count += attr.split().count(class_name)
    return count


def extract_icon_labels(html: str) -> list[str]:
    return re.findall(r'<span class="icon-cluster-label">([^<]+)</span>', html)


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print("ERROR usage: python3 scripts/check_harness_rebuilt_style_rules.py <output-root>")
        return 1

    output_root = Path(argv[0]).resolve()
    specs = load_specs(output_root)
    errors: list[str] = []
    warnings: list[str] = []
    expected_icon_labels = [label for _, label in ICON_CLUSTER_ITEMS]

    for spec in specs:
        html_path = output_root / "slides" / spec["file_name"]
        html = html_path.read_text(encoding="utf-8")
        visible_lines = strip_tags(html)

        if '<body class="theme-minimal-light">' not in html:
            errors.append(f"{spec['slide_id']}: body must declare theme-minimal-light")

        labels = extract_icon_labels(html)
        if labels != expected_icon_labels:
            errors.append(f"{spec['slide_id']}: icon cluster labels must be {', '.join(expected_icon_labels)}")
        if class_count(html, "icon-cluster-item") != 3:
            errors.append(f"{spec['slide_id']}: icon cluster must contain exactly 3 items")
        if class_count(html, "icon-cluster-glyph") != 3:
            errors.append(f"{spec['slide_id']}: icon cluster must contain exactly 3 glyphs")

        for line in visible_lines:
            if line in expected_icon_labels or line == "Harness 잘 사용하기":
                continue
            if POLITE_ENDING_RE.search(line):
                errors.append(f"{spec['slide_id']}: polite ending detected: {line}")
            if len(line) > 90:
                errors.append(f"{spec['slide_id']}: copy too long: {line}")
            elif len(line) > 62:
                warnings.append(f"{spec['slide_id']}: copy length warning: {line}")
            if REPORT_STYLE_RE.search(line) and len(line) > 20:
                warnings.append(f"{spec['slide_id']}: report-style connector warning: {line}")

        if spec["shell"] == "content-card-shell":
            cards = class_count(html, "card-item")
            if not 2 <= cards <= 3:
                errors.append(f"{spec['slide_id']}: content-card-shell requires 2-3 card-item blocks")

        if spec["shell"] == "content-emphasis-shell" and class_count(html, "emphasis-line") != 1:
            errors.append(f"{spec['slide_id']}: content-emphasis-shell requires one emphasis-line")

    for warning in warnings:
        print(f"WARN {warning}")

    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1

    print(f"OK style rules passed for {len(specs)} slides")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
