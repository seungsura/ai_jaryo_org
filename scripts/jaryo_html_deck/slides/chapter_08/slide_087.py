from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        87,
        title="생성과 검증을 같은 손에 쥐지 않았다",
        shell="split-compare-shell",
        source_section="08",
        source_block="08-07",
        key_claim="생성과 검증을 분리",
        chapter_label="CHAPTER 08",
        notes_intent="HTML generation 이후 기계적 검증과 사람 검토 분리",
        notes="source 08 lines 83-96; canonical Page 081",
        body={
            "variant": "validation-workflow",
            "left_label": "HTML generation",
            "right_label": "기계적 검증 + 사람 검토",
            "left_points": [
                "HTML generation",
                "생성자가 자기 결과를 스스로 통과시키게 두면",
                "그럴듯한 오류의 장기 생존",
            ],
            "right_points": [
                "기계적 검증",
                "사람 검토",
                "slide contract 점검",
                "한국어 문장 점검",
                "source와 주장 매핑 확인",
                "디자인 계약 위반 확인",
                "생성과 검증 분리",
            ],
            "arrow": True,
        },
    )
