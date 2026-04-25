from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        55,
        title="하나의 에이전트 = 하나의 역할",
        shell="process-flow-shell",
        source_section="06",
        source_block="06-02",
        key_claim="멀티 에이전트의 본질은 병렬화가 아니라 분해",
        chapter_label="CHAPTER 06",
        notes_intent="다섯 패턴과 Planner/Generator/Evaluator 원칙 연결",
        notes="source lines 15-24, page 064 layout reference",
        body={
            "variant": "chapter-pattern-row",
            "cards": [
                {"index": "01", "title": "Sub-Agent", "text": "중간 작업을 격리하는 기본형", "detail": "단일 심부름", "nodes": ["Main", "Sub"]},
                {"index": "02", "title": "Orchestrator", "text": "계획자 하나가 여러 실행자를 배치", "detail": "1:N 위임", "nodes": ["Plan", "Exec", "Exec"]},
                {"index": "03", "title": "Parallel", "text": "같은 목표를 평면으로 벌림", "detail": "독립 lane", "nodes": ["A", "shared repo", "B"]},
                {"index": "04", "title": "GAN-Style", "text": "생성과 평가를 분리", "detail": "루브릭으로 평가", "nodes": ["Gen", "Eval"]},
                {"index": "05", "title": "Agent Teams", "text": "양방향 대화와 합의", "detail": "그래프 구조", "nodes": ["R", "C", "E"]},
            ],
            "thesis": "메인 컨텍스트에 무엇을 남기고, 무엇을 밖으로 밀어낼 것인가",
            "source_label": "Planner / Generator / Evaluator: 생성과 평가를 같은 손에 쥐지 않음",
        },
    )
