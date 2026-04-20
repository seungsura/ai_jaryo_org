#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

from harness_rebuilt_pipeline import FOOTER_LABEL, SHELL_CONTRACTS, load_specs


FORBIDDEN_BY_SHELL = {
    "cover-title-shell": {"content-body", "card-grid", "card-item", "emphasis-line", "transition-title"},
    "chapter-transition-shell": {"cover-subtitle", "cover-author", "content-body", "card-grid", "card-item", "emphasis-line"},
}


def has_class(html: str, class_name: str) -> bool:
    for attr in re.findall(r'class="([^"]+)"', html):
        if class_name in attr.split():
            return True
    return False


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print("ERROR usage: python3 scripts/check_harness_rebuilt_shell_contract.py <output-root>")
        return 1

    output_root = Path(argv[0]).resolve()
    specs = load_specs(output_root)
    errors: list[str] = []

    for spec in specs:
        slide_path = output_root / "slides" / spec["file_name"]
        if not slide_path.exists():
            errors.append(f"{spec['slide_id']}: missing slide file {slide_path}")
            continue
        html = slide_path.read_text(encoding="utf-8")
        main_match = re.search(r"<main\b([^>]*)>", html)
        if not main_match:
            errors.append(f"{spec['slide_id']}: missing <main> root")
            continue
        attrs = main_match.group(1)
        for attr_name, expected in [
            ("data-slide-id", spec["slide_id"]),
            ("data-shell", spec["shell"]),
            ("data-slide-kind", spec["slide_kind"]),
            ("data-chapter", spec["chapter_id"]),
            ("data-source-block", spec["source_block"]),
        ]:
            if f'{attr_name}="{expected}"' not in attrs:
                errors.append(f"{spec['slide_id']}: main root missing {attr_name}={expected}")
        if 'data-footer="default"' not in attrs:
            errors.append(f"{spec['slide_id']}: data-footer must be default")
        for required_class in [f"family-{spec['family']}", f"layout-{spec['layout']}", f"density-{spec['density']}"]:
            if required_class not in attrs:
                errors.append(f"{spec['slide_id']}: main root missing class {required_class}")
        if 'style="' in html:
            errors.append(f"{spec['slide_id']}: inline style attribute is not allowed")
        if FOOTER_LABEL not in html:
            errors.append(f"{spec['slide_id']}: footer label mismatch")
        if f'<span class="footer-right">{spec["order"]}</span>' not in html:
            errors.append(f"{spec['slide_id']}: footer order mismatch")

        for class_name in SHELL_CONTRACTS[spec["shell"]]:
            if not has_class(html, class_name):
                errors.append(f"{spec['slide_id']}: shell {spec['shell']} requires class {class_name}")

        for forbidden_class in FORBIDDEN_BY_SHELL.get(spec["shell"], set()):
            if has_class(html, forbidden_class):
                errors.append(f"{spec['slide_id']}: shell {spec['shell']} forbids class {forbidden_class}")

    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1

    print(f"OK shell contract passed for {len(specs)} slides")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
