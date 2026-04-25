from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        18,
        title="CoT / ReAct / ToT",
        shell="process-flow-shell",
        source_section="02",
        source_block="02-03",
        key_claim="세 추론 패턴의 구조 차이",
        chapter_label="CHAPTER 02",
        notes_intent="CoT / ReAct / ToT native three-card comparison",
        notes="source markdown의 CoT, ReAct, ToT row와 approved page-064 layout 구조",
        body={
            "variant": "cot-triad",
            "cards": [
                {
                    "title": "Chain-of-Thought",
                    "acronym": "CoT",
                    "meaning": "중간 추론 단계",
                    "kind": "cot",
                },
                {
                    "title": "ReAct",
                    "acronym": "Reason + Act",
                    "meaning": "추론과 행동 반복",
                    "kind": "react",
                },
                {
                    "title": "Tree-of-Thought",
                    "acronym": "ToT",
                    "meaning": "여러 추론 경로",
                    "kind": "tot",
                },
            ],
        },
    )
