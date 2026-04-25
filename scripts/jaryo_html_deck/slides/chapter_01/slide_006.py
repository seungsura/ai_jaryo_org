from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide

from jaryo_html_deck.content import (
    CODE_ASSEMBLY_HELLO,
    CODE_C_HELLO,
)


def build() -> SlideSpec:
    return make_slide(
        6,
        title="어셈블리 → C/Pascal",
        shell="split-compare-shell",
        source_section="01",
        source_block="01-01",
        key_claim="어셈블리 표현량에서 C 함수 표현으로",
        chapter_label="CHAPTER 01",
        notes_intent="source code block 기반 두 번째 전환 사례",
        notes="source markdown의 어셈블리와 C 코드 블록",
        body={
            "left_label": "어셈블리",
            "left_code": CODE_ASSEMBLY_HELLO,
            "right_label": "C/Pascal",
            "right_code": CODE_C_HELLO,
            "opinion": "진짜 프로그래머는 파스칼 같은 걸 쓰지 않는다!",
            "arrow": True,
        },
    )
