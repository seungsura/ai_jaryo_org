from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        28,
        title="AI 시대의 개발 방법론",
        shell="section-divider-shell",
        source_section="03",
        source_block="03-00",
        key_claim="TDD·SDD·Spec-first 재부상",
        chapter_label="CHAPTER 03",
        notes_intent="03장 진입을 알리는 section divider",
        notes="AI 시대의 개발 방법론 장 진입",
        body={"keywords": []},
    )
