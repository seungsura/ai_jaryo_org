#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "docs/03-html/manifest.md"

SHELL_RULES = {
    "title-hero-shell": ["cover-main", "cover-rule", "title-placeholder", "hero-points", "footer"],
    "agenda-list-shell": ["agenda-header", "agenda-list", "agenda-item", "footer"],
    "section-divider-shell": ["section-main", "chapter-marker", "title-placeholder", "section-keywords", "footer"],
    "statement-editorial-shell": ["statement-panel", "statement-tag", "statement-text", "statement-support", "footer"],
    "wide-bullets-shell": ["top-band", "body-area", "callout-card", "bullet-list", "footer"],
    "process-flow-shell": ["top-band", "process-track", "process-step", "footer"],
    "split-compare-shell": ["top-band", "compare-grid", "compare-col", "footer"],
    "evidence-table-shell": ["top-band", "table-wrap", "data-table", "footer"],
    "closing-shell": ["closing-main", "cover-rule", "title-placeholder", "closing-points", "footer"],
}


def parse_markdown_table(path: Path) -> list[dict[str, str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    in_registry = False
    headers: list[str] = []
    rows: list[dict[str, str]] = []

    for raw_line in lines:
        line = raw_line.strip()
        if line.startswith("| order | slide id |"):
            in_registry = True
            headers = [part.strip() for part in line.strip("|").split("|")]
            continue
        if not in_registry:
            continue
        if not line.startswith("|"):
            break
        normalized = line.replace("|", "").replace(" ", "")
        if normalized and set(normalized) == {"-"}:
            continue
        parts = [part.strip().strip("`") for part in line.strip("|").split("|")]
        if len(parts) != len(headers):
            continue
        rows.append(dict(zip(headers, parts, strict=True)))
    return rows


def extract_main_attrs(html: str) -> str | None:
    match = re.search(r"<main\b([^>]*)>", html, flags=re.IGNORECASE | re.DOTALL)
    return match.group(1) if match else None


def has_class(html: str, class_name: str) -> bool:
    pattern = rf'class="[^"]*\b{re.escape(class_name)}\b[^"]*"'
    return re.search(pattern, html) is not None


def footer_number(html: str) -> str | None:
    match = re.search(r'<span class="footer-right">\s*([^<]+?)\s*</span>', html)
    return match.group(1).strip() if match else None


def footer_left(html: str) -> str | None:
    match = re.search(r'<span class="footer-left">\s*([^<]+?)\s*</span>', html)
    return match.group(1).strip() if match else None


def body_class(html: str) -> str | None:
    match = re.search(r"<body\b[^>]*class=\"([^\"]+)\"", html)
    return match.group(1) if match else None


def main() -> int:
    rows = parse_markdown_table(MANIFEST_PATH)
    if not rows:
        print(f"ERROR manifest slide registry not found: {MANIFEST_PATH}")
        return 1

    errors: list[str] = []
    warnings: list[str] = []

    for row in rows:
        slide_id = row["slide id"]
        shell = row["shell"]
        layout = row["layout"]
        slide_type = row["slide type"]
        file_name = row["file"]
        path = ROOT / "docs/03-html/slides" / file_name

        if not path.exists():
            errors.append(f"{slide_id}: missing file {path}")
            continue

        html = path.read_text(encoding="utf-8")
        attrs = extract_main_attrs(html)
        if attrs is None:
            errors.append(f"{slide_id}: missing <main> root")
            continue

        if f'data-slide-id="{slide_id}"' not in attrs:
            errors.append(f"{slide_id}: main root missing data-slide-id")
        if f'data-shell="{shell}"' not in attrs:
            errors.append(f"{slide_id}: main root missing data-shell={shell}")
        if f"layout-{layout}" not in attrs:
            errors.append(f"{slide_id}: main root missing layout-{layout}")

        family_match = re.search(r"family-([a-z]+)", attrs)
        if not family_match:
            errors.append(f"{slide_id}: main root missing family-* class")
        if "density-" not in attrs:
            errors.append(f"{slide_id}: main root missing density-* class")
        if 'data-footer="default"' not in attrs:
            errors.append(f'{slide_id}: data-footer must be "default"')

        current_body_class = body_class(html)
        if current_body_class is None or "theme-minimal-light" not in current_body_class:
            errors.append(f"{slide_id}: <body> must declare theme-minimal-light")

        if 'style="' in html:
            errors.append(f"{slide_id}: inline style attribute is not allowed")

        if footer_left(html) != "Harness 잘 사용하기":
            errors.append(f"{slide_id}: footer-left must be 'Harness 잘 사용하기'")
        if footer_number(html) != row["order"]:
            errors.append(f"{slide_id}: footer-right must match order {row['order']}")

        required_classes = SHELL_RULES.get(shell)
        if required_classes is None:
            warnings.append(f"{slide_id}: unknown shell {shell}")
        else:
            for class_name in required_classes:
                if not has_class(html, class_name):
                    errors.append(f"{slide_id}: shell {shell} requires class '{class_name}'")

        if shell == "process-flow-shell":
            step_count = len(re.findall(r'class="[^"]*\bprocess-step\b[^"]*"', html))
            if step_count < 3:
                errors.append(f"{slide_id}: process-flow-shell requires at least three steps")

        if shell == "evidence-table-shell" and "<table class=\"data-table\">" not in html:
            errors.append(f"{slide_id}: evidence-table-shell requires a data table")

        if slide_type == "comparison":
            compare_count = len(re.findall(r'class="[^"]*\bcompare-col\b[^"]*"', html))
            if compare_count != 2:
                errors.append(f"{slide_id}: comparison slide must render two compare columns")

    for warning in warnings:
        print(f"WARN {warning}")

    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1

    print(f"OK slide contract passed for {len(rows)} slides")
    return 0


if __name__ == "__main__":
    sys.exit(main())
