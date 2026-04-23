from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        28,
        title="SDD",
        shell="process-flow-shell",
        source_section="03",
        source_block="03-02",
        key_claim="스펙이 진실의 원천",
        chapter_label="CHAPTER 03",
        lead="Spec-Driven Development",
        notes_intent="GitHub Spec Kit의 세 단계와 멈춤 장치",
        notes="요구사항, 계획, 태스크를 파일로 고정하는 흐름",
        body={
            "variant": "spec-kit-workflow",
            "steps": [
                {
                    "index": "SPECIFY",
                    "title": "/speckit.specify",
                    "text": "WHAT / WHY 분리",
                    "items": [
                        "[NEEDS CLARIFICATION]",
                    ],
                },
                {
                    "index": "PLAN",
                    "title": "/speckit.plan",
                    "text": "HOW 제안",
                    "items": [
                        "Constitution Check",
                    ],
                },
                {
                    "index": "TASKS",
                    "title": "/speckit.tasks",
                    "text": "태스크 분해",
                    "items": [
                        "병렬 가능 작업 [P] 마킹",
                    ],
                },
            ],
            "principle_title": "강제되는 원칙",
            "principle": "WHAT/WHY와 HOW를 분리하고, 모호한 부분은 [NEEDS CLARIFICATION]에서 멈춘다.",
            "outcome_title": "핵심",
            "outcome": "모든 산출물이 파일로 저장되고 커밋되고 계속 참조된다.",
            "source": {
                "icon_label": "GitHub Copilot icon",
                "text": "GitHub spec-kit",
            },
        },
    )
