from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        23,
        title="컨텍스트만으로는 부족하다",
        shell="process-flow-shell",
        source_section="02",
        source_block="02-08",
        key_claim="좋은 입력만으로는 루프 통제 불가",
        chapter_label="CHAPTER 02",
        notes_intent="컨텍스트 시대의 벽을 통제 관점으로 재구성",
        notes="source heading + risk list + control question 4개를 context-wall 구조로 압축",
        body={
            "variant": "context-wall",
            "claim": "좋은 입력만으로는 루프를 통제할 수 없다",
            "risks": [
                "도구 호출 실패",
                "테스트 오해",
                "비용 폭주",
                "위험 명령",
                "보안 경계",
                "목표 망각",
            ],
            "source": "어떤 정보를 넣어야 하나",
            "controls": [
                "무엇을 하게 할 것인가",
                "무엇을 못 하게 막을 것인가",
                "어디서 멈출 것인가",
                "어떻게 검증할 것인가",
            ],
        },
    )
