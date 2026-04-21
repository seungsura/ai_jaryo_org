from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .config import FOOTER_LEFT

SHELL_TO_FAMILY = {
    "title-hero-shell": "title",
    "agenda-list-shell": "agenda",
    "section-divider-shell": "section",
    "statement-editorial-shell": "content",
    "process-flow-shell": "content",
    "split-compare-shell": "comparison",
    "evidence-table-shell": "content",
}

SHELL_TO_LAYOUT = {
    "title-hero-shell": "centered",
    "agenda-list-shell": "wide",
    "section-divider-shell": "centered",
    "statement-editorial-shell": "editorial",
    "process-flow-shell": "wide",
    "split-compare-shell": "split",
    "evidence-table-shell": "wide",
}

SHELL_TO_TYPE = {
    "title-hero-shell": "title",
    "agenda-list-shell": "agenda",
    "section-divider-shell": "section",
    "statement-editorial-shell": "statement",
    "process-flow-shell": "process",
    "split-compare-shell": "comparison",
    "evidence-table-shell": "table",
}


@dataclass
class SlideSpec:
    order: int
    slide_id: str
    file_name: str
    title: str
    slide_type: str
    layout: str
    shell: str
    family: str
    density: str
    source_section: str
    source_block: str
    key_claim: str
    notes_intent: str
    notes_status: str
    status: str
    chapter_label: str
    notes: str
    lead: str = ""
    footer_left: str = FOOTER_LEFT
    body: dict[str, Any] = field(default_factory=dict)


def make_slide(
    order: int,
    *,
    title: str,
    shell: str,
    source_section: str,
    source_block: str,
    key_claim: str,
    chapter_label: str,
    lead: str = "",
    density: str = "medium",
    notes_intent: str = "",
    notes: str = "",
    body: dict[str, Any] | None = None,
) -> SlideSpec:
    return SlideSpec(
        order=order,
        slide_id=f"S{order:03d}",
        file_name=f"slide-{order:03d}.html",
        title=title,
        slide_type=SHELL_TO_TYPE[shell],
        layout=SHELL_TO_LAYOUT[shell],
        shell=shell,
        family=SHELL_TO_FAMILY[shell],
        density=density,
        source_section=source_section,
        source_block=source_block,
        key_claim=key_claim,
        notes_intent=notes_intent or key_claim,
        notes_status="ready",
        status="built",
        chapter_label=chapter_label,
        notes=notes or key_claim,
        lead=lead,
        body=body or {},
    )
