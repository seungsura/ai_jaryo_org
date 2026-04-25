from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        82,
        title="이 발표를 만든 방법",
        shell="process-flow-shell",
        source_section="08",
        source_block="08-02",
        key_claim="source → prose → outline → html → pdf",
        chapter_label="CHAPTER 08",
        notes_intent="source에서 pdf까지 이어지는 제작 pipeline",
        notes="source 08 lines 5-30; canonical Page 077",
        body={
            "variant": "source-pipeline",
            "steps": [
                {"index": "01", "title": "source", "text": "PDF, HTML, 외부 링크, 로컬 마크다운 자료"},
                {"index": "02", "title": "prose", "text": "발표와 글의 기준 문장"},
                {"index": "03", "title": "outline", "text": "slide 단위와 장 구조"},
                {"index": "04", "title": "html", "text": "Spec, Harness, Skills"},
                {"index": "05", "title": "pdf", "text": "markdown, html, 규칙 문서"},
            ],
        },
    )
