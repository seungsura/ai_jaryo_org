from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        1,
        title="이 글과 발표가 만들어진 과정",
        shell="section-divider-shell",
        source_section="08",
        source_block="08-00",
        key_claim="이 글과 발표가 만들어진 과정",
        chapter_label="CHAPTER 08",
        density="light",
        notes_intent="08장 chapter divider",
        notes="Page 076-077 and source 08 chapter entry",
        body={"keywords": []},
    )
