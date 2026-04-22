from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide

def build() -> SlideSpec:
    return make_slide(
        19,
        title="ReAct / Tree-of-Thought",
        shell="process-flow-shell",
        source_section="02",
        source_block="02-03",
        key_claim="행동 루프와 경로 탐색",
        chapter_label="CHAPTER 02",
        notes_intent="ReAct / Tree-of-Thought native diagrams",
        notes="source markdown의 ReAct, Tree-of-Thought rows와 approved assets 구조",
        body={
            "variant": "pattern-pair",
            "patterns": [
                {
                    "index": "02",
                    "title": "ReAct",
                    "text": "추론과 행동을 번갈아 수행",
                    "kind": "react",
                    "meaning": "검색과 도구 호출이 루프 안으로 진입",
                    "nodes": ["Reason", "Act", "Observe"],
                },
                {
                    "index": "03",
                    "title": "Tree-of-Thought",
                    "text": "여러 추론 경로를 동시에 탐색",
                    "kind": "tot",
                    "meaning": "하나의 답이 아니라 후보 경로를 비교",
                    "nodes": ["경로 A", "경로 B", "경로 C"],
                },
            ],
        },
    )
