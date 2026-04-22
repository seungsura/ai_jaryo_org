from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        18,
        title="Chain-of-Thought",
        shell="process-flow-shell",
        source_section="02",
        source_block="02-03",
        key_claim="중간 추론 단계를 쓰게 한다",
        chapter_label="CHAPTER 02",
        notes_intent="Chain-of-Thought native example diagram",
        notes="source markdown의 Chain-of-Thought row와 approved 02-chain-of-thought asset 구조",
        body={
            "variant": "cot-native",
            "claim": "중간 추론 단계를 쓰게 한다",
            "meaning": "답만 내던 모델을 reasoning path가 있는 모델처럼 다루기 시작",
            "steps": [
                {"title": "문제", "text": "5개 + 2캔 × 3개"},
                {"title": "중간 추론", "text": "2캔 × 3개 = 6개"},
                {"title": "답", "text": "5개 + 6개 = 11개"},
            ],
        },
    )
