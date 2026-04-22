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
        notes_intent="Andrew Ng four patterns native quadrant",
        notes="source markdown의 Andrew Ng 네 가지 패턴과 approved 05 asset 구조",
        body={
            "variant": "agentic-native",
            "cards": [
                {"title": "Reflection", "text": "한 번 낸 답을 다시 보고 고침", "effect": "자기 수정 루프", "example": ["Generate", "Critique", "Revise"]},
                {"title": "Tool Use", "text": "검색·계산·실행을 바깥 도구에 맡김", "effect": "모델 바깥 세계 연결", "example": ["Model", "Search/API", "Result"]},
                {"title": "Planning", "text": "목표를 단계로 쪼갬", "effect": "긴 작업 추진", "example": ["Goal", "Plan", "Steps"]},
                {"title": "Multi-Agent Collaboration", "text": "역할을 나눠 다른 관점으로 봄", "effect": "생성과 검증 분리", "example": ["Writer", "Reviewer", "Merge"]},
            ],
            "thesis": "모델 바깥 구조가 성능을 좌우",
        },
    )
