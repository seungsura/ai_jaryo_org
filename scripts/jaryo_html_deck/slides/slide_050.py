from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        50,
        title="대표 실패 패턴 네 가지",
        shell="statement-editorial-shell",
        source_section="05",
        source_block="05-04",
        key_claim="기억과 잡음과 규칙이 하나의 컨텍스트 안에서 썩고 있다",
        chapter_label="CHAPTER 05",
        notes_intent="컨텍스트 실패 모드 네 가지 정리",
        notes="Drew Breunig 실패 모드와 source transcription facts",
        body={
            "variant": "failure-card-grid",
            "cards": [
                {
                    "title": "POISONING",
                    "lines": [
                        "오래된 가정 / 잘못된 메모 / 판단 오염",
                    ],
                },
                {
                    "title": "DISTRACTION",
                    "lines": [
                        "정보 과잉 / 핵심 신호 매몰",
                    ],
                },
                {
                    "title": "CONFUSION",
                    "lines": [
                        "과거 결정과 현재 결정 / 최신 기준 혼선",
                    ],
                },
                {
                    "title": "CLASH",
                    "lines": [
                        "서로 다른 지시와 기준 / 한 컨텍스트 안의 충돌",
                    ],
                },
            ],
            "synthesis": "기억과 잡음과 규칙이 한 컨텍스트 안에서 썩음",
        },
    )
