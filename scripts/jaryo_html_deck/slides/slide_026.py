from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        26,
        title="Agent = Model + Harness",
        shell="statement-editorial-shell",
        source_section="02",
        source_block="02-10",
        key_claim="하네스가 결정하는 네 지점",
        chapter_label="CHAPTER 02",
        notes_intent="02-v05 decision points",
        notes="source markdown의 하네스가 결정하는 것",
        body={
            "variant": "harness-layered",
            "statement": "Agent = Model + Harness",
            "decisions": [
                {"title": "무엇을 보는지", "text": "컨텍스트"},
                {"title": "무엇을 할 수 있는지", "text": "도구 · 권한"},
                {"title": "언제 멈추는지", "text": "검증 · 중단 조건"},
                {"title": "잘못되었을 때", "text": "오류 시나리오와 재시도"},
            ],
        },
    )
