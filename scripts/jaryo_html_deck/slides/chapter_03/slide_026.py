from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        26,
        title="AI 시대의 개발 방법론",
        shell="section-divider-shell",
        source_section="03",
        source_block="03-00",
        key_claim="TDD·SDD·Spec-first 재부상",
        chapter_label="CHAPTER 03",
        notes_intent="03장 진입을 source heading 키워드와 함께 고정",
        notes="03장 source heading의 핵심 축(SDD/TDD/Waterfall)만 keyword rail로 노출",
        body={"keywords": ["SDD", "TDD", "Waterfall"]},
    )
