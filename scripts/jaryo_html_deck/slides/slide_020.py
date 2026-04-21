from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide

def build() -> SlideSpec:
    return make_slide(
        20,
        title="네 가지 에이전틱 패턴",
        shell="evidence-table-shell",
        source_section="02",
        source_block="02-04",
        key_claim="모델 바깥 구조가 성능을 좌우",
        chapter_label="CHAPTER 02",
        notes_intent="Andrew Ng 4 agentic patterns",
        notes="source markdown의 Andrew Ng 네 가지 패턴과 02-v02 asset",
        body={
            "variant": "agentic-native",
            "cards": [
                {"title": "Reflection", "text": "자기 결과 검토와 수정", "effect": "자기 수정 루프", "example": ["Generate", "Critique", "Revise"]},
                {"title": "Tool Use", "text": "검색·계산·실행 도구 호출", "effect": "바깥 세계 연결", "example": ["Model", "Search/API", "Result"]},
                {"title": "Planning", "text": "큰 목표의 단계 분해", "effect": "긴 작업 추진", "example": ["Goal", "Plan", "Steps"]},
                {"title": "Multi-Agent Collaboration", "text": "역할 분리와 협업", "effect": "생성과 검증 분리", "example": ["Writer", "Reviewer", "Merge"]},
            ],
            "thesis": "모델 바깥 구조가 성능을 좌우",
        },
    )
