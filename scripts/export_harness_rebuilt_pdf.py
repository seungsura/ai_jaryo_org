#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

from harness_rebuilt_pipeline import DEFAULT_OUTPUT_ROOT, DEFAULT_PDF_OUTPUT


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--deck", type=Path, default=DEFAULT_OUTPUT_ROOT / "deck/index.html")
    parser.add_argument("--output", type=Path, default=DEFAULT_PDF_OUTPUT)
    parser.add_argument("--browser-command", default=None)
    return parser.parse_args(argv)


def detect_browser(command_override: str | None) -> tuple[str | None, list[str]]:
    searched: list[str] = []
    if command_override:
        searched.append(command_override)
        override_path = Path(command_override)
        if override_path.exists():
            return str(override_path), searched
        resolved = shutil.which(command_override)
        if resolved:
            return resolved, searched
        return None, searched

    for candidate in [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "chromium",
        "chromium-browser",
        "google-chrome",
        "google-chrome-stable",
        "microsoft-edge",
        "msedge",
    ]:
        searched.append(candidate)
        resolved = shutil.which(candidate)
        if resolved:
            return resolved, searched
    return None, searched


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    deck_path = args.deck.resolve()
    if not deck_path.exists():
        print(f"ERROR missing deck file: {deck_path}")
        return 1

    browser, searched = detect_browser(args.browser_command)
    if browser is None:
        print("ERROR No supported browser runtime found for PDF export.")
        print("searched:", ", ".join(searched))
        return 1

    args.output.parent.mkdir(parents=True, exist_ok=True)
    command = [
        browser,
        "--headless",
        "--disable-gpu",
        "--no-first-run",
        "--no-default-browser-check",
        "--allow-file-access-from-files",
        f"--print-to-pdf={args.output.resolve()}",
        deck_path.as_uri(),
    ]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        print("ERROR PDF export failed.")
        print(result.stdout.strip())
        print(result.stderr.strip())
        return 1
    if not args.output.exists():
        print("ERROR PDF export command completed but no PDF file was created.")
        return 1

    print(f"OK exported PDF to {args.output.resolve()}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
