from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        22,
        title="프롬프트 시대의 벽",
        shell="statement-editorial-shell",
        source_section="02",
        source_block="02-05",
        key_claim="모델은 보지 못한 것을 알 수 없음",
        chapter_label="CHAPTER 02",
        notes_intent="프롬프트 시대의 한계",
        notes="source markdown의 Blind Prompting 문단",
        body={
            "variant": "blind-prompting",
            "statement": "모델은 보지 못한 것을 알 수 없음",
            "cards": [
                {"title": "관련 파일 부재", "text": "기존 유틸리티 인식 불가"},
                {"title": "기존 설계 부재", "text": "설계 결정 활용 불가"},
                {"title": "팀 컨벤션 부재", "text": "내부 규칙 활용 불가"},
            ],
            "thesis": "문제는 지시문이 아니라 모델이 소비하는 정보",
        },
    )
