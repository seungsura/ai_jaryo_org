from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        33,
        title="SDD + TDD가 Harness로 이어지는 이유",
        shell="statement-editorial-shell",
        source_section="03",
        source_block="03-05",
        key_claim="이 시스템이 곧 하네스 엔지니어링",
        chapter_label="CHAPTER 03",
        notes_intent="03장에서 04장 Harness 구조로 넘어가는 bridge",
        notes="스펙과 테스트 루프를 사람이 매번 손으로 굴리지 않도록 시스템화",
        body={
            "variant": "spec-tdd-bridge",
            "subheading": "SDD + TDD가 Harness로 이어지는 이유",
            "synthesis": "이 시스템이 곧 하네스 엔지니어링",
            "cards": [
                {
                    "title": "Spec",
                    "items": [
                        "스펙 템플릿",
                        "계획 문서",
                    ],
                },
                {
                    "title": "TDD",
                    "items": [
                        "TDD 루프",
                        "Skills",
                        "Hooks",
                    ],
                },
            ],
        },
    )
