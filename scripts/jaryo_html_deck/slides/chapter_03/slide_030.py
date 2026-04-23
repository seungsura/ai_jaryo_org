from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        30,
        title="Waterfall vs SDD",
        shell="split-compare-shell",
        source_section="03",
        source_block="03-04",
        key_claim="Waterfall은 순차적으로 진행되고, SDD는 스펙을 실행 기준으로 둔다",
        chapter_label="CHAPTER 03",
        notes_intent="Royce 1970과 spec-driven.md evidence로 Waterfall vs SDD 비교",
        notes="요구사항·설계·코딩·테스트 vs specification·plan·tasks",
        body={
            "variant": "waterfall-comparison",
            "left_label": "Waterfall",
            "right_label": "SDD",
            "rows": [
                {
                    "key": "개발 흐름",
                    "left": "요구사항 → 설계 → 코딩 → 테스트",
                    "right": "스펙이 primary artifact",
                },
                {
                    "key": "검증 시점",
                    "left": "테스트가 개발 후반에 실제 제약을 드러냄",
                    "right": "/speckit.specify\u200b → \u200b/speckit.plan\u200b → \u200b/speckit.tasks",
                },
                {
                    "key": "실행 산출물",
                    "left": "요구사항 또는 설계를 다시 고침",
                    "right": "spec · plan · tasks를 실행 산출물로 갱신",
                },
            ],
        },
    )
