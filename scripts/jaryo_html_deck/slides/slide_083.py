from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        83,
        title="이 글과 발표가 만들어진 과정",
        shell="statement-editorial-shell",
        source_section="08",
        source_block="08-01",
        key_claim="코드 한 줄, PPT 한 장도 직접 만들지 않았습니다",
        chapter_label="CHAPTER 08",
        notes_intent="코드/PPT 직접 제작이 아니라 하네스 설계였다는 증거 진입",
        notes="source 08 lines 1-3; canonical Page 076",
        body={
            "variant": "chapter-proof-memory",
            "hook": "기억하시나요",
            "main": ["이 발표를", "코드 한 줄 없이 만든 방법"],
            "proof": "한 것은 하나 - 하네스 설계",
            "kicker": "지금부터 그 증거",
        },
    )
