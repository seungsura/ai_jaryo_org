from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        7,
        title="재료 4 규칙 세우기",
        shell="evidence-table-shell",
        source_section="08",
        source_block="08-06",
        key_claim="design contract를 먼저 고정",
        chapter_label="CHAPTER 08",
        notes_intent="design contract와 validation contract를 한 장에 압축",
        notes="source 08 lines 69-96; canonical Page 079",
        body={
            "variant": "rule-contract",
            "headers": ["design contract", "validation"],
            "rows": [
                ["톤과 분위기", "slide contract 점검"],
                ["색상 팔레트", "한국어 문장 점검"],
                ["타이포그래피", "deck-level consistency 확인"],
                ["여백과 레이아웃 규칙", "source와 주장 매핑 확인"],
                ["금지해야 할 표현과 과한 장식", "디자인 계약 위반 확인"],
            ],
            "question": "사용 도구: MS의 슬라이드 디자인 규칙 · Google Stitch의 Design.md · Kuneosu/make-slide",
        },
    )
