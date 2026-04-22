from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        25,
        title="컨텍스트 시대의 벽",
        shell="process-flow-shell",
        source_section="02",
        source_block="02-08",
        key_claim="좋은 입력만으로는 루프 통제 불가",
        chapter_label="CHAPTER 02",
        notes_intent="컨텍스트 시대의 한계와 에이전트 루프",
        notes="source markdown의 gather context to repeat loop",
        body={
            "variant": "loop-map",
            "steps": [
                {"index": "01", "title": "gather context", "text": "컨텍스트 수집"},
                {"index": "02", "title": "take action", "text": "파일 수정과 명령 실행"},
                {"index": "03", "title": "verify", "text": "테스트 · 린트 · 로그"},
                {"index": "04", "title": "repeat", "text": "실패 후 재수정"},
            ],
            "thesis": "하네스는 네 지점 각각에 개입",
        },
    )
