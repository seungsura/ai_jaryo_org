from __future__ import annotations

from .config import SECTION_TARGETS
from .model import SlideSpec
from .slides import SLIDE_BUILDERS


def build_all_specs() -> list[SlideSpec]:
    specs = [build() for build in SLIDE_BUILDERS]
    assert len(specs) == sum(SECTION_TARGETS.values()), len(specs)
    for expected_order, spec in enumerate(specs, start=1):
        assert spec.order == expected_order, (expected_order, spec.slide_id)
    return specs
