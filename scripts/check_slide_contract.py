#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "docs/03-html/manifest.md"

SHELL_RULES = {
    "title-hero-shell": {
        "family": "title",
        "required": ["cover-main", "cover-rule", "title-placeholder", "footer"],
    },
    "agenda-list-shell": {
        "family": "agenda",
        "required": ["agenda-header", "agenda-list", "agenda-item", "footer"],
    },
    "section-divider-shell": {
        "family": "section",
        "required": ["section-main", "chapter-marker", "title-placeholder", "footer"],
    },
    "content-three-step-shell": {
        "family": "content",
        "required": [
            "top-band",
            "chapter-label",
            "title-placeholder",
            "top-band-rule",
            "body-area",
            "progression-board",
            "progress-step",
            "footer",
        ],
    },
    "content-three-card-shell": {
        "family": "content",
        "required": [
            "top-band",
            "chapter-label",
            "title-placeholder",
            "top-band-rule",
            "body-area",
            "role-shift-board",
            "role-shift-card",
            "footer",
        ],
    },
}


def parse_manifest(path: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    in_slide_registry = False

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line.startswith("| order | slide id |"):
            in_slide_registry = True
            continue
        if not in_slide_registry:
            continue
        if not line.startswith("|"):
            break
        normalized = line.replace("|", "").replace(" ", "").strip()
        if normalized and set(normalized) == {"-"}:
            continue

        parts = [part.strip() for part in line.strip("|").split("|")]
        if len(parts) != 10:
            continue

        rows.append(
            {
                "order": parts[0],
                "slide_id": parts[1].strip("`"),
                "title": parts[2],
                "family": parts[3].strip("`"),
                "density": parts[4].strip("`"),
                "shell": parts[5].strip("`"),
                "source_section": parts[6].strip("`"),
                "html_path": parts[7].strip("`"),
                "status": parts[8],
                "notes": parts[9],
            }
        )

    return rows


def extract_main_attrs(html: str) -> str | None:
    match = re.search(r"<main\b([^>]*)>", html, flags=re.IGNORECASE | re.DOTALL)
    return match.group(1) if match else None


def has_class(html: str, class_name: str) -> bool:
    pattern = rf'class="[^"]*\b{re.escape(class_name)}\b[^"]*"'
    return re.search(pattern, html) is not None


def footer_number(html: str) -> str | None:
    match = re.search(
        r'<span class="footer-right">\s*([^<]+?)\s*</span>', html, flags=re.IGNORECASE
    )
    return match.group(1).strip() if match else None


def footer_left(html: str) -> str | None:
    match = re.search(
        r'<span class="footer-left">\s*([^<]+?)\s*</span>', html, flags=re.IGNORECASE
    )
    return match.group(1).strip() if match else None


def body_class(html: str) -> str | None:
    match = re.search(r"<body\b[^>]*class=\"([^\"]+)\"", html, flags=re.IGNORECASE)
    return match.group(1) if match else None


def footer_mode(main_attrs: str) -> str:
    match = re.search(r'data-footer="([^"]+)"', main_attrs)
    return match.group(1).strip() if match else "default"


def main() -> int:
    rows = parse_manifest(MANIFEST_PATH)
    errors: list[str] = []
    warnings: list[str] = []

    if not rows:
        print(f"ERROR manifest slide registry not found: {MANIFEST_PATH}")
        return 1

    for row in rows:
        slide_id = row["slide_id"]
        shell = row["shell"]
        family = row["family"]
        density = row["density"]
        order = row["order"]
        html_path = ROOT / row["html_path"]

        if not html_path.exists():
            errors.append(f"{slide_id}: missing file {html_path}")
            continue

        html = html_path.read_text(encoding="utf-8")
        attrs = extract_main_attrs(html)
        if attrs is None:
            errors.append(f"{slide_id}: missing <main> root")
            continue

        if f'data-slide-id="{slide_id}"' not in attrs:
            errors.append(f"{slide_id}: main root missing data-slide-id=\"{slide_id}\"")
        if f'data-shell="{shell}"' not in attrs:
            errors.append(f"{slide_id}: main root missing data-shell=\"{shell}\"")
        if f"family-{family}" not in attrs:
            errors.append(f"{slide_id}: main root missing family-{family}")
        if f"density-{density}" not in attrs:
            errors.append(f"{slide_id}: main root missing density-{density}")

        if 'style="' in html:
            errors.append(f"{slide_id}: inline style attribute is not allowed")

        current_body_class = body_class(html)
        if current_body_class is None or "theme-" not in current_body_class:
            errors.append(f"{slide_id}: <body> must declare an active theme class")

        current_footer_mode = footer_mode(attrs)
        if current_footer_mode == "none":
            if "footer-exempt" not in row["notes"]:
                errors.append(
                    f"{slide_id}: data-footer=\"none\" requires 'footer-exempt' in manifest notes"
                )
            if has_class(html, "footer"):
                warnings.append(f"{slide_id}: footer-exempt slide still includes footer markup")
        else:
            current_footer_left = footer_left(html)
            if current_footer_left != "Harness 잘 사용하기":
                errors.append(
                    f"{slide_id}: footer-left must be 'Harness 잘 사용하기' (found: {current_footer_left!r})"
                )

            current_footer_number = footer_number(html)
            if current_footer_number != str(int(order)):
                errors.append(
                    f"{slide_id}: footer-right must match order {order} (found: {current_footer_number!r})"
                )

        shell_rule = SHELL_RULES.get(shell)
        if shell_rule is None:
            warnings.append(f"{slide_id}: unknown shell rule {shell}")
            continue

        if shell_rule["family"] != family:
            errors.append(
                f"{slide_id}: shell {shell} expects family {shell_rule['family']}, found {family}"
            )

        for class_name in shell_rule["required"]:
            if not has_class(html, class_name):
                errors.append(f"{slide_id}: shell {shell} requires class '{class_name}'")

        if shell == "content-three-step-shell":
            focus_count = len(re.findall(r'class="[^"]*\bprogress-step\b[^"]*\bis-focus\b', html))
            if focus_count != 1:
                errors.append(
                    f"{slide_id}: content-three-step-shell must have exactly one focused step"
                )

        if shell == "content-three-card-shell":
            focus_count = len(re.findall(r'class="[^"]*\brole-shift-card\b[^"]*\bis-focus\b', html))
            if focus_count != 1:
                warnings.append(
                    f"{slide_id}: content-three-card-shell should usually have exactly one focused card"
                )

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
