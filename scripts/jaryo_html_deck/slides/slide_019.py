from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide

def build() -> SlideSpec:
    return make_slide(
        19,
        title="프롬프트 패턴의 확장",
        shell="process-flow-shell",
        source_section="02",
        source_block="02-03",
        key_claim="프롬프트가 모델에게 추가로 맡긴 일",
        chapter_label="CHAPTER 02",
        notes_intent="CoT/ReAct/ToT/Self-Refine/Reflexion diagram",
        notes="source markdown의 prompt pattern table과 02-v01 assets",
        body={
            "variant": "pattern-diagram",
            "patterns": [
                {
                    "index": "01",
                    "title": "Chain-of-Thought",
                    "text": "중간 추론 단계",
                    "kind": "cot",
                    "example": {
                        "label": "테니스공 산술",
                        "problem": "5개 + 2캔 × 3개",
                        "step": "2캔 × 3개 = 6개",
                        "answer": "5개 + 6개 = 11개",
                    },
                },
                {
                    "index": "02",
                    "title": "ReAct",
                    "text": "추론과 행동 교대",
                    "kind": "react",
                    "example": {
                        "label": "WebShop 검색",
                        "start": "WebShop",
                        "action": "Search",
                        "observation": "Observe",
                    },
                },
                {
                    "index": "03",
                    "title": "Tree-of-Thought",
                    "text": "여러 추론 경로",
                    "kind": "tot",
                    "example": {
                        "label": "Game of 24",
                        "root": "Game of 24",
                        "branches": [
                            {"text": "4 × 6"},
                            {"text": "8 + 16", "class": "selected"},
                            {"text": "backtrack"},
                        ],
                    },
                },
                {
                    "index": "04",
                    "title": "Self-Refine",
                    "text": "자기 출력 개선",
                    "kind": "refine",
                    "example": {
                        "label": "code feedback",
                        "draft": "초안 코드",
                        "feedback": "code feedback",
                        "refined": "개선 코드",
                    },
                },
                {
                    "index": "05",
                    "title": "Reflexion",
                    "text": "피드백 루프",
                    "kind": "reflexion",
                    "example": {
                        "label": "reflection memory",
                        "trial": "실패 로그",
                        "memory": "reflection memory",
                        "retry": "재시도",
                    },
                },
            ],
        },
    )
