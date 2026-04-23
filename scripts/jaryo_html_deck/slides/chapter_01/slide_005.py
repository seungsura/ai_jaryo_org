from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide

from jaryo_html_deck.content import (
    CODE_ASSEMBLY_MOV,
    CODE_MACHINE,
)


def build() -> SlideSpec:
    return make_slide(
        5,
        title="기계어 → 어셈블리",
        shell="split-compare-shell",
        source_section="01",
        source_block="01-01",
        key_claim="이진 코드 직접 작성 부담의 감소",
        chapter_label="CHAPTER 01",
        notes_intent="source code block 기반 첫 전환 사례",
        notes="source markdown의 기계어와 어셈블리 코드 블록",
        body={
            "left_label": "기계어",
            "left_code": CODE_MACHINE,
            "right_label": "어셈블리",
            "right_code": CODE_ASSEMBLY_MOV,
            "opinion": "컴파일러가 만든 코드가 사람보다 효율적일 리 없다!",
            "arrow": True,
        },
    )
