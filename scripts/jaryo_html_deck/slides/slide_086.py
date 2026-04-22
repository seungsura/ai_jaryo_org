from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        86,
        title="재료 2 단일 진실원 만들기",
        shell="process-flow-shell",
        source_section="08",
        source_block="08-04",
        key_claim="prose는 source of truth",
        chapter_label="CHAPTER 08",
        notes_intent="prose를 기준 문장과 판단 기준으로 세운 과정",
        notes="source 08 lines 40-53",
        body={
            "steps": [
                {"index": "01", "title": "prose", "text": "블로그 글처럼 작성"},
                {"index": "02", "title": "논리 순서", "text": "주장 강도를 책임지고 확인"},
                {"index": "03", "title": "source of truth", "text": "HTML slide, PDF 구성 기준"},
                {"index": "04", "title": "사람이 개입", "text": "한국어 문체와 독자 경험"},
            ],
        },
    )
