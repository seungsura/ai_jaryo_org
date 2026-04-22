from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        52,
        title="Context Rot: 길어진 기억은 조용히 썩는다",
        shell="statement-editorial-shell",
        source_section="05",
        source_block="05-06",
        key_claim="길이보다 신호 대 잡음비가 중요하다",
        chapter_label="CHAPTER 05",
        notes_intent="Context Rot의 길이 문제와 외부 아티팩트 전환",
        notes="source markdown의 Context Rot 설명과 아티팩트 보존 문단",
        body={
            "variant": "context-rot-native",
            "claim": "길이 문제가 아니라 흐려지는 의도와 제약",
            "left_title": "대화창 안의 상태",
            "left_items": [
                "초반 규칙 약화",
                "가정의 사실화",
                "오래된 도구 결과 잔존",
            ],
            "center_title": "끊을 타이밍",
            "center_items": [
                "현재 결론",
                "다음 행동",
            ],
            "right_title": "바깥의 아티팩트",
            "right_items": [
                "파일",
                "이슈",
                "진행 기록",
                "테스트 결과",
                "Git 이력",
            ],
        },
    )
