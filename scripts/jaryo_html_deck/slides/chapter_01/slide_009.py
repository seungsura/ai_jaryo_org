from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide

from jaryo_html_deck.content import (
    PROMPT_AI_REFACTOR,
)


def build() -> SlideSpec:
    return make_slide(
        9,
        title="AI 개발",
        shell="statement-editorial-shell",
        source_section="01",
        source_block="01-01",
        key_claim="개발의 추상화 수준 상승",
        chapter_label="CHAPTER 01",
        notes_intent="source prompt와 quote 기반 AI 개발 사례",
        notes="source markdown의 AI 개발 prompt와 quote",
        body={
            "variant": "prompt-only",
            "prompt": PROMPT_AI_REFACTOR,
        },
    )
