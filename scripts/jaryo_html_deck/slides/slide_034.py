from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        34,
        title="프롬프트를 넘어서",
        shell="section-divider-shell",
        source_section="04",
        source_block="04-00",
        key_claim="Prompt, Context, Harness",
        chapter_label="CHAPTER 04",
        notes_intent="04장 진입을 알리는 section divider",
        notes="프롬프트와 컨텍스트를 포함하는 하네스 구조로 진입",
        body={"keywords": ["Prompt", "Context", "Harness"]},
    )
