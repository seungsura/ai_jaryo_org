from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        13,
        title="개발자의 새로운 역할",
        shell="process-flow-shell",
        source_section="01",
        source_block="01-05",
        key_claim="환경 설계와 결과 판단",
        chapter_label="CHAPTER 01",
        notes_intent="reference layout 기반 evolution and analogy blocks",
        notes="source markdown의 개발자 역할 bullet list",
        body={
            "variant": "evolution-analogies",
            "flow": [
                "코드를 잘 짜는 능력",
                "문서를 잘 쓰는 능력",
                "컨텍스트를 설계하는 능력",
            ],
            "analogies": [
                {
                    "title": "건축가",
                    "lines": [
                        "벽돌 쌓기 대신 설계도 작성",
                        "정확한 설계도 → 튼튼한 건물",
                    ],
                },
                {
                    "title": "오케스트라 지휘자",
                    "lines": [
                        "직접 연주 대신 전체 조율",
                        "CLAUDE.md = 총보",
                    ],
                },
            ],
        },
    )
