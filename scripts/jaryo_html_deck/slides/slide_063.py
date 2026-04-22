from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        63,
        title="5. Agent Teams: 양방향 대화가 가능한 팀을 만든다",
        shell="process-flow-shell",
        source_section="06",
        source_block="06-08",
        key_claim="Agent Teams는 함께 토론하고 합의하는 구조",
        chapter_label="CHAPTER 06",
        notes_intent="team graph reference를 role cards로 재구성",
        notes="source lines 112-124, page 067 structure reference",
        body={
            "variant": "chapter-team-graph",
            "nodes": [
                {"title": "Researcher", "text": "외부 문서와 사례"},
                {"title": "Architect", "text": "설계 대안"},
                {"title": "Reviewer", "text": "위험과 누락"},
                {"title": "Coordinator", "text": "논의를 수렴"},
                {"title": "Editor", "text": "최종 품질"},
            ],
            "side_cards": [
                {"title": "양방향 대화", "text": "여러 독립 세션이 서로 대화하며 수렴"},
                {"title": "복수 관점", "text": "연구, 전략 문서, 대규모 아키텍처 검토, 제품 기획"},
            ],
            "conclusion": "보통 3명 안팎에서는 이득, 너무 커지면 AI 회의만 길어질 수 있음",
        },
    )
