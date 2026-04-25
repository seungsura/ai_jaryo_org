from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        43,
        title="하네스는 환경 그 자체다",
        shell="process-flow-shell",
        source_section="04",
        source_block="04-11",
        key_claim="필요한 파일, 필요한 도구, 필요한 규칙",
        chapter_label="CHAPTER 04",
        notes_intent="chapter 04 closing statement",
        notes="Harness Builder는 에이전트가 쓸 수 있는 환경을 만드는 사람",
        body={
            "steps": [
                {"index": "01", "title": "필요한 파일", "text": "상태와 근거를 세션 밖에 남김"},
                {"index": "02", "title": "필요한 도구", "text": "에이전트가 실제 일을 할 수 있게 연결"},
                {"index": "03", "title": "필요한 규칙", "text": "권한, 검증, 중단 지점을 고정"},
            ],
            "thesis": "Harness Builder는 에이전트가 쓸 수 있는 환경을 만드는 사람",
        },
    )
