from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        49,
        title="컨텍스트가 길수록 항상 좋은 것은 아니다",
        shell="split-compare-shell",
        source_section="05",
        source_block="05-03",
        key_claim="신호 대 잡음비가 핵심이다",
        chapter_label="CHAPTER 05",
        notes_intent="길어진 컨텍스트의 잡음 문제",
        notes="컨텍스트는 길이보다 신호 대 잡음비",
        body={
            "variant": "context-signal-stack",
            "claim": "지금 판단에 필요한 신호만 남기는 것이 능력",
            "equation": "관련 정보가 있음 ≠ 제때, 제 위치, 올바른 기준",
            "noise": [
                "오래된 가정",
                "실패한 도구 결과",
                "폐기된 계획",
                "불필요한 파일",
            ],
            "operating": "신호 대 잡음비",
        },
    )
