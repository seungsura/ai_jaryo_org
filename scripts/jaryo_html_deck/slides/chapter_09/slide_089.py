from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        89,
        title="우리가 다음에 해야 할 일",
        shell="section-divider-shell",
        source_section="09",
        source_block="09-00",
        key_claim="우리가 다음에 해야 할 일",
        chapter_label="CHAPTER 09",
        density="light",
        notes_intent="09장 chapter divider",
        notes="source 09 chapter entry",
        body={"keywords": []},
    )
