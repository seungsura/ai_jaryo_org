from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        37,
        title="에이전트 루프: 하네스의 심장",
        shell="process-flow-shell",
        source_section="04",
        source_block="04-03",
        key_claim="거의 모든 에이전트가 반복하는 4단계.",
        chapter_label="CHAPTER 04",
        notes_intent="gather context, take action, verify work, repeat loop",
        notes="거의 모든 코딩 에이전트가 반복하는 네 단계",
        body={
            "variant": "loop-map",
            "steps": [
                {"index": "01", "title": "gather context", "text": "무엇을 안 보여줄지 설계"},
                {"index": "02", "title": "take action", "text": "되돌릴 수 있는 액션부터 허용"},
                {"index": "03", "title": "verify work", "text": "테스트, 린트, 리뷰"},
                {"index": "04", "title": "repeat", "text": "현재 결론과 다음 행동만 남김"},
            ],
            "thesis": "거의 모든 에이전트가 반복하는 4단계.",
        },
    )
