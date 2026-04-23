from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        88,
        title="이 발표가 증거",
        shell="process-flow-shell",
        source_section="08",
        source_block="08-08",
        key_claim="원하는 것을 글로 작성 → 규칙을 문서로 작성 → 결과를 사람이 검증",
        chapter_label="CHAPTER 08",
        notes_intent="제작 과정 자체가 Harness 방식으로 만들어진 사례",
        notes="source 08 lines 102-121; canonical Page 081-082",
        body={
            "variant": "proof-formula",
            "steps": [
                {"index": "01", "title": "원하는 것을", "text": "글로 작성"},
                {"index": "02", "title": "규칙을", "text": "문서로 작성"},
                {"index": "03", "title": "결과를", "text": "사람이 검증"},
            ],
        },
    )
