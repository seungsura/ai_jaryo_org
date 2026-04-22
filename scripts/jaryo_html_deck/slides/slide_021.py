from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        21,
        title="네 가지 에이전틱 패턴",
        shell="evidence-table-shell",
        source_section="02",
        source_block="02-04",
        key_claim="모델 바깥 구조가 성능을 좌우",
        chapter_label="CHAPTER 02",
        notes_intent="Andrew Ng four patterns node-only native quadrant",
        notes="source markdown의 Andrew Ng 네 가지 패턴과 approved 05 asset 구조, diagram 내부 text 제거",
        body={
            "variant": "agentic-native",
            "cards": [
                {"kind": "reflection", "title": "Reflection", "text": "자기 결과를 비판하고 반복 개선", "effect": "자기 수정 루프"},
                {"kind": "tool-use", "title": "Tool Use", "text": "외부 도구로 정보 수집과 실행", "effect": "모델 바깥 세계 연결"},
                {"kind": "planning", "title": "Planning", "text": "목표를 실행 순서로 나눠 추진", "effect": "긴 작업 추진"},
                {"kind": "multi-agent", "title": "Multi-Agent Collaboration", "text": "전문 역할로 나눠 복잡한 작업 수행", "effect": "생성과 검증 분리"},
            ],
            "thesis": "모델 바깥 구조가 성능을 좌우",
        },
    )
