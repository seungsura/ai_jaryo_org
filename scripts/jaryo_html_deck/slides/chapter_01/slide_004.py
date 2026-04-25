from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        4,
        title="코딩은 사라지는가",
        shell="section-divider-shell",
        source_section="01",
        source_block="01-00",
        key_claim="개발의 추상화 수준 상승",
        chapter_label="CHAPTER 01",
        density="light",
        notes_intent="01장의 질문을 챕터 단위로 고정",
        notes="코딩이 사라지는가보다 개발자가 직접 붙들 일이 어디로 이동하는가를 묻는다.",
        body={"keywords": []},
    )
