from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        69,
        title="Plan-Critic-Build",
        shell="process-flow-shell",
        source_section="07",
        source_block="07-03",
        key_claim="합의된 뒤에만 실행",
        chapter_label="CHAPTER 07",
        notes_intent="Plan/Critic/Build와 Explore/Plan/Code/Commit 연결",
        notes="source lines 36-49",
        body={
            "variant": "chapter-staged-flow",
            "primary": ["Plan", "Critic", "Build"],
            "secondary": ["Explore", "Plan", "Code", "Commit"],
            "conclusion": "success criteria",
        },
    )
