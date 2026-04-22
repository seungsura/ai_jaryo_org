from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        67,
        title="멀티 모델과 멀티 에이전트",
        shell="evidence-table-shell",
        source_section="06",
        source_block="06-12",
        key_claim="여러 모델 교차 사용은 독립 평가자 풀에 가까움",
        chapter_label="CHAPTER 06",
        notes_intent="멀티 모델 distinction과 Claude/Codex/Gemini 역할",
        notes="source lines 179-183",
        body={
            "variant": "evidence-cards",
            "cards": [
                {"value": "Claude", "label": "구현 계획", "text": "긴 맥락과 구현 루프 중심"},
                {"value": "Codex", "label": "구조 검토", "text": "코드 구조·리팩터링·코드 리뷰"},
                {"value": "Gemini", "label": "가독성 피드백", "text": "UI·문서·대안적 시각"},
            ],
            "question": "합의 · 불일치 · 불확실 분리",
        },
    )
