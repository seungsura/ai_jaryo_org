from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        79,
        title="결론: 실전 워크플로우의 중심은 운영 구조다",
        shell="evidence-table-shell",
        source_section="07",
        source_block="07-13",
        key_claim="검증과 흔적 위에 다음 판단을 올리는 운영 구조",
        chapter_label="CHAPTER 07",
        notes_intent="chapter 07 closing lines",
        notes="source lines 186-188, page 068/063 closing structure reference",
        body={
            "variant": "chapter-principle-grid",
            "cards": [
                {"index": "01", "title": "원리를 명령어로 고정", "text": "계획과 실행을 분리"},
                {"index": "02", "title": "결정론적 게이트", "text": "무엇을 어디서 검증할 것인가"},
                {"index": "03", "title": "상태와 기준의 흔적", "text": "외부 아티팩트에 남김"},
            ],
            "conclusion": "무엇을 어디서 검증하고, 어떤 흔적 위에 다음 판단을 올릴 것인가",
        },
    )
