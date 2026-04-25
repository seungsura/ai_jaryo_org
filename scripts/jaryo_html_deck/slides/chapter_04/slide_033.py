from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        33,
        title="Prompt, Context, Harness",
        shell="evidence-table-shell",
        source_section="04",
        source_block="04-01",
        key_claim="Prompt ⊂ Context ⊂ Harness",
        chapter_label="CHAPTER 04",
        notes_intent="source page 36/37 의미를 한 장의 hierarchy로 압축",
        notes="프롬프트, 컨텍스트, 하네스의 포함 관계",
        body={
            "headers": ["층위", "핵심 질문", "초점"],
            "rows": [
                ["Prompt", "무엇을/어떻게 말할 것인가", "명령의 품질 / 단일 프롬프트 / 정적"],
                ["Context", "무엇을/어떻게 보여줄 것인가", "정보의 품질 / 입력 파이프라인 / 동적"],
                ["Harness", "무엇을/어떻게 통제할 것인가", "시스템의 안정성 / 실행 환경 전체"],
            ],
            "question": "Prompt ⊂ Context ⊂ Harness",
        },
    )
