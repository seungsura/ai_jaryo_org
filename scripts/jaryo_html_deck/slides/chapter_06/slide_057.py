from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        57,
        title="Advisor 전략: 작은 실행자, 큰 자문",
        shell="evidence-table-shell",
        source_section="06",
        source_block="06-04",
        key_claim="막히는 순간에만 상위 판단을 빌림",
        chapter_label="CHAPTER 06",
        notes_intent="executor와 advisor의 결정 책임 분리",
        notes="source lines 55-59, page 065 high-contrast split reference",
        body={
            "variant": "chapter-split-panels",
            "cards": [
                {"title": "executor", "text": "규모가 작은 저렴한 모델이 실제 일을 계속 맡음", "evidence": "메인 실행자는 그대로 유지"},
                {"title": "advisor", "text": "막히는 순간에만 더 상위 모델에게 판단을 빌림", "evidence": "다음 계획 · 방향 수정 · 여기서 멈춰라"},
            ],
            "conclusion": "복잡한 아키텍처 분기, 막힌 디버깅, 위험한 계획 수정에 필요한 일시적 판단",
        },
    )
