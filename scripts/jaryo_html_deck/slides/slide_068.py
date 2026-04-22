from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        68,
        title="결론: 더 많은 AI가 아니라 더 좁은 역할의 AI 여럿",
        shell="evidence-table-shell",
        source_section="06",
        source_block="06-13",
        key_claim="더 좁은 역할의 AI 여럿을, 더 명확한 경계 안에서 일하게 한다",
        chapter_label="CHAPTER 06",
        notes_intent="chapter 06 closing lines",
        notes="source lines 187-189",
        body={
            "variant": "chapter-principle-grid",
            "cards": [
                {"index": "01", "title": "메인 컨텍스트", "text": "판단에 필요한 신호만 남김"},
                {"index": "02", "title": "판단 책임", "text": "계획·실행·리뷰를 나눔"},
                {"index": "03", "title": "검증 관점", "text": "생성 결과를 다른 기준으로 판정"},
            ],
            "conclusion": "더 좁은 역할의 AI 여럿을, 더 명확한 경계 안에서 일하게 한다",
        },
    )
