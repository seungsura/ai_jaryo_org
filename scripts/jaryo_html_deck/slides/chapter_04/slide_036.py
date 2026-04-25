from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        36,
        title="하네스의 책임",
        shell="process-flow-shell",
        source_section="04",
        source_block="04-04",
        key_claim="다섯 개 기능 블록",
        chapter_label="CHAPTER 04",
        notes_intent="5 responsibility cards와 설계 순서 rail",
        notes="운영 관점에서 보는 하네스의 책임",
        body={
            "steps": [
                {"index": "01", "title": "Guardrails", "text": "위험한 행동과 권한 경계"},
                {"index": "02", "title": "Specification", "text": "작업 범위와 기준선"},
                {"index": "03", "title": "Verification", "text": "결정론적 결과 검증"},
                {"index": "04", "title": "State Management", "text": "파일, Git 이력, 진행 기록"},
                {"index": "05", "title": "Observability", "text": "실행 로그, trace, checkpoint"},
            ],
        },
    )
