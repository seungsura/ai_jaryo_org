from __future__ import annotations

from importlib import import_module
from typing import Callable

from jaryo_html_deck.model import SlideSpec

CHAPTER_PACKAGES = [
    "chapter_00",
    "chapter_01",
    "chapter_02",
    "chapter_03",
    "chapter_04",
    "chapter_05",
    "chapter_06",
    "chapter_07",
    "chapter_08",
    "chapter_09",
]


def _load_all_builders() -> list[Callable[[], SlideSpec]]:
    builders: list[Callable[[], SlideSpec]] = []
    base = __name__
    for chapter_package in CHAPTER_PACKAGES:
        module = import_module(f"{base}.{chapter_package}")
        chapter_builders = getattr(module, "SLIDE_BUILDERS", None)
        if not isinstance(chapter_builders, list):
            raise TypeError(f"{module.__name__}.SLIDE_BUILDERS must be a list")
        builders.extend(chapter_builders)
    return builders


SLIDE_BUILDERS = _load_all_builders()

__all__ = ["SLIDE_BUILDERS"]
