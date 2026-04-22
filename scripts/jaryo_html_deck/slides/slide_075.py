from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        75,
        title="Ralph Loop",
        shell="process-flow-shell",
        source_section="07",
        source_block="07-07",
        key_claim="PROMPT.md 하나를 루프의 중심에 둠",
        chapter_label="CHAPTER 07",
        notes_intent="PROMPT.md loop",
        notes="source lines 106-110, page 053 structure-only reference",
        body={
            "variant": "loop-map",
            "steps": [
                {"index": "01", "title": "PROMPT.md", "text": "규칙이 파일 한 장에 고정"},
                {"index": "02", "title": "Claude Code 실행", "text": "파일을 입력으로 사용"},
                {"index": "03", "title": "파일 수정과 검증", "text": "실행 결과를 다시 읽음"},
                {"index": "04", "title": "규칙 한 줄 추가", "text": "다음 루프에 자동 반영"},
            ],
            "thesis": "단순성은 예측 가능성",
        },
    )
