from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        17,
        title="왜 Claude Code인가",
        shell="statement-editorial-shell",
        source_section="02",
        source_block="02-00",
        key_claim="Agent = Model + Harness",
        chapter_label="CHAPTER 02",
        notes_intent="Agent = Model + Harness thesis와 명사형 quote",
        notes="source markdown의 핵심 공식과 LangChain quote를 명사형으로 압축한다.",
        body={
            "variant": "thesis-harness",
            "statement": "Agent = Model + Harness",
            "quote": "모델이 아닌 것은 전부 하네스",
            "meaning": "힘이 센 말을 원하는 방향으로 몰고 멈추게 만드는 장비 전체",
            "mapping": [
                {"title": "무엇을 보는지", "text": "컨텍스트"},
                {"title": "무엇을 하게 할지", "text": "도구 · 권한"},
                {"title": "언제 멈출지", "text": "제약 · 검증"},
            ],
            "source": "LangChain · Vivek Trivedy",
        },
    )
