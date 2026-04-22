from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        6,
        title="재료 3- slides-grab, Skill 경계로 박힌 분리",
        shell="process-flow-shell",
        source_section="08",
        source_block="08-05",
        key_claim="단계 사이에 사용자 승인을 물리적으로 강제",
        chapter_label="CHAPTER 08",
        notes_intent="outline, manifest, slides-grab의 단계 분리와 승인 관문",
        notes="source 08 lines 55-67, 83-96; canonical Page 080",
        body={
            "variant": "gate-diagram",
            "steps": [
                {"index": "PLAN", "title": "slide-outline.md", "text": "승인된 아웃라인"},
                {"index": "DESIGN", "title": "slide-XX.html", "text": "사용자 승인까지 반복"},
                {"index": "EXPORT", "title": "PDF 변환", "text": "산출물 검증"},
            ],
        },
    )
