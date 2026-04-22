from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        94,
        title="내일부터",
        shell="statement-editorial-shell",
        source_section="09",
        source_block="09-03",
        key_claim="글로 먼저 · 직접 써보기 · 도구",
        chapter_label="CHAPTER 09",
        notes_intent="Page 086 actions and source line",
        notes="source 09 lines 35-43; canonical Page 086",
        body={
            "variant": "tomorrow-actions",
            "actions": [
                {"title": "글로 먼저", "text": "CLAUDE.md 1페이지 작성, 또는 반복 업무 1개를 글로 명세"},
                {"title": "직접 써보기", "text": "터미널 열고 Claude Code 3~4창 - 토큰을 일부러라도 소비"},
                {"title": "도구", "text": "Oh My Claude Code 설치 - 원리의 자동화"},
            ],
            "quote": "\"토큰을 많이 쓰는 사람이 가장 경쟁력 있는 개발자\" - 박종천",
        },
    )
