from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide

from jaryo_html_deck.content import (
    CODE_C_POINT,
    CODE_JAVA_POINT,
)


def build() -> SlideSpec:
    return make_slide(
        7,
        title="C → Java",
        shell="split-compare-shell",
        source_section="01",
        source_block="01-01",
        key_claim="수동 메모리 관리에서 GC로",
        chapter_label="CHAPTER 01",
        notes_intent="source code block 기반 세 번째 전환 사례",
        notes="source markdown의 C와 Java 코드 블록",
        body={
            "left_label": "C",
            "left_code": CODE_C_POINT,
            "right_label": "Java",
            "right_code": CODE_JAVA_POINT,
            "opinion": "메모리를 직접 관리하지 않으면 진짜 개발자가 아니다!",
            "arrow": True,
        },
    )
