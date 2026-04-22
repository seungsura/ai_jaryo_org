from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        46,
        title="이렇게 하면 망한다",
        shell="section-divider-shell",
        source_section="05",
        source_block="05-00",
        key_claim="한계와 실패 패턴",
        chapter_label="CHAPTER 05",
        notes_intent="chapter 05 opener",
        notes="05장 진입을 알리는 opener",
        body={"keywords": []},
    )
