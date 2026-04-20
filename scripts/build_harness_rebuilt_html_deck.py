#!/usr/bin/env python3
from __future__ import annotations

import sys

from harness_rebuilt_pipeline import build_pipeline, parse_cli


def main(argv: list[str]) -> int:
    args = parse_cli(argv)
    specs, _ = build_pipeline(
        args.source_root.resolve(),
        args.output_root.resolve(),
        through_chapter=args.through_chapter,
        chapters_arg=args.chapters,
    )
    print(f"OK built harness-rebuilt deck with {len(specs)} slides at {args.output_root.resolve()}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
