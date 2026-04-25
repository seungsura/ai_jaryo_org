from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        15,
        title="왜 Claude Code인가",
        shell="section-divider-shell",
        source_section="02",
        source_block="02-00",
        key_claim="AI 코딩 도구 흐름의 대표 사례",
        chapter_label="CHAPTER 02",
        density="light",
        notes_intent="02장 진입과 제품 리뷰가 아닌 흐름 분석 고정",
        notes="Claude Code를 특정 제품 리뷰가 아니라 하네스 흐름의 대표 사례로 둔다.",
        body={"keywords": []},
    )
