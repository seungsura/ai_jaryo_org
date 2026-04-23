from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide

from jaryo_html_deck.content import (
    CODE_JAVA_HELLO,
    CODE_PYTHON_HELLO,
)


def build() -> SlideSpec:
    return make_slide(
        8,
        title="Java → Python",
        shell="split-compare-shell",
        source_section="01",
        source_block="01-01",
        key_claim="같은 출력과 더 짧은 표현",
        chapter_label="CHAPTER 01",
        notes_intent="source code block 기반 네 번째 전환 사례",
        notes="source markdown의 Java와 Python 코드 블록",
        body={
            "left_label": "Java",
            "left_code": CODE_JAVA_HELLO,
            "right_label": "Python",
            "right_code": CODE_PYTHON_HELLO,
            "opinion": "장난감 언어로 무슨 개발을 하냐!",
            "arrow": True,
        },
    )
