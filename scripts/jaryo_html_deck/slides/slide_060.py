from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        60,
        title="2. Orchestrator: 계획자 하나가 여러 실행자를 배치한다",
        shell="process-flow-shell",
        source_section="06",
        source_block="06-05",
        key_claim="Orchestrator는 1:N 위임 구조",
        chapter_label="CHAPTER 06",
        notes_intent="source numbered flow를 1:N chain으로 구현",
        notes="source lines 63-76, page 064/066 fan-out reference",
        body={
            "variant": "chapter-fanout",
            "planner": "Planner",
            "planner_text": "목표 해석 · 하위 작업 분해 · 실행자 배정",
            "workers": [
                {"title": "Exec", "text": "하위 작업"},
                {"title": "Exec", "text": "하위 작업"},
                {"title": "Exec", "text": "하위 작업"},
            ],
            "path": ["결과 수집", "전체 통합", "재작업 지시"],
            "conclusion": "품질은 분해의 품질과 수렴 지점의 품질",
        },
    )
