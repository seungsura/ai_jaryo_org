from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        23,
        title="컨텍스트만으로는 부족하다",
        shell="split-compare-shell",
        source_section="02",
        source_block="02-08",
        key_claim="잘못된 방향으로 전력질주",
        chapter_label="CHAPTER 02",
        notes_intent="page 35 loop diagram reuse + larger right-side failure cards + plus sign",
        notes="좌측 mini loop, 가운데 plus, 우측 상단 실패 카드 4개, 하단 one-line emphasis 유지",
        body={
            "variant": "context-loop-injection",
            "steps": [
                {"index": "01", "title": "gather context"},
                {"index": "02", "title": "take action"},
                {"index": "03", "title": "verify work"},
                {"index": "04", "title": "repeat"},
            ],
            "issues": [
                "도구 호출 실패",
                "목표 망각",
                "테스트 오해",
                "보안 경계",
            ],
            "opinion": "잘못된 방향으로 전력질주",
        },
    )
