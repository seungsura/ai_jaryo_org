from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        75,
        title="한 모델에만 기대지 않는다",
        shell="evidence-table-shell",
        source_section="07",
        source_block="07-09",
        key_claim="여러 모델의 응답을 합의, 불일치, 불확실로 나눔",
        chapter_label="CHAPTER 07",
        notes_intent="Claude/Codex/Gemini cross-check roles",
        notes="source lines 127-135, page 072 reference",
        body={
            "variant": "chapter-model-rail",
            "models": [
                {"index": "01", "title": "Claude", "text": "긴 맥락과 구현 루프 중심"},
                {"index": "02", "title": "Codex", "text": "코드 구조, 리팩터링, 코드 리뷰 및 검토"},
                {"index": "03", "title": "Gemini", "text": "UI, 가독성, 대안적 시각, 문서 피드백"},
            ],
            "rail": ["합의", "불일치", "불확실"],
            "conclusion": "합의하면 진행, 불일치하면 사람 검토, 불확실하면 추가 자료",
        },
    )
