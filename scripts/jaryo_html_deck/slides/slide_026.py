from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        26,
        title="3막: 하네스의 시대",
        shell="process-flow-shell",
        source_section="02",
        source_block="02-09",
        key_claim="작업 환경 전체를 품기 시작한 코딩 도구",
        chapter_label="CHAPTER 02",
        notes_intent="Harness era minimal transition",
        notes="source markdown + user-requested S026 simplification",
        body={
            "variant": "harness-era-minimal",
            "claim": "코딩 도구는 이제 실행 환경을 품는다",
            "flow": [
                {"title": "자동완성·채팅"},
                {"title": "작업 환경 전체", "text": "파일 · 셸 · 테스트"},
                {"title": "Harness", "emphasis": True},
            ],
        },
    )
