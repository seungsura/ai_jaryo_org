from __future__ import annotations

from importlib import import_module
from pathlib import Path
from typing import Callable

from jaryo_html_deck.model import SlideSpec


def _load_builders() -> list[Callable[[], SlideSpec]]:
    module_name = __name__
    package_dir = Path(__file__).resolve().parent
    builders: list[Callable[[], SlideSpec]] = []
    for slide_path in sorted(package_dir.glob("slide_*.py")):
        module = import_module(f"{module_name}.{slide_path.stem}")
        build = getattr(module, "build", None)
        if not callable(build):
            raise TypeError(f"{module.__name__} must define callable build()")
        builders.append(build)
    return builders


SLIDE_BUILDERS = _load_builders()

__all__ = ["SLIDE_BUILDERS"]
