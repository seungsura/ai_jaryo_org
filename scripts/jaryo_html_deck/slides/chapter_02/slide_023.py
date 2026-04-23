from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        23,
        title="컨텍스트만으로는 부족하다",
        shell="split-compare-shell",
        source_section="02",
        source_block="02-08",
        key_claim="멈춤 기준과 검증 경로를 먼저 설계해야 한다",
        chapter_label="CHAPTER 02",
        notes_intent="page 37 diagram rhythm + right-side failure cards + injection arrows",
        notes="좌측 loop panel, 중간 잘못된 응답 주입 화살표, 우측 상단 실패 카드 4개, 하단 one-line emphasis 유지",
        body={
            "variant": "context-loop-injection",
            "loop_label": "루프",
            "issues": [
                "도구 호출 실패",
                "목표 망각",
                "테스트 오해",
                "보안 경계",
            ],
            "rail_label": "잘못된 응답 주입",
            "opinion": "멈춤 기준과 검증 경로를 먼저 설계해야 한다",
        },
    )
