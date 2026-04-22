from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        51,
        title="현실에서 보이는 증상들",
        shell="statement-editorial-shell",
        source_section="05",
        source_block="05-05",
        key_claim="작은 오류가 누적되면 증상으로 드러난다",
        chapter_label="CHAPTER 05",
        notes_intent="실전 증상 3종을 source-backed 카드로 압축",
        notes="source markdown의 AI Slop, Doom Loop, Shadow Agent 문단",
        body={
            "variant": "failure-card-grid",
            "cards": [
                {
                    "title": "AI Slop",
                    "lines": [
                        "산출물 조잡화",
                    ],
                },
                {
                    "title": "Doom Loop",
                    "lines": [
                        "같은 실수 반복",
                    ],
                },
                {
                    "title": "Shadow Agent",
                    "lines": [
                        "작업 이유와 기준 상실",
                    ],
                },
            ],
            "synthesis": "모델 이상이 아니라 구조 문제",
        },
    )
