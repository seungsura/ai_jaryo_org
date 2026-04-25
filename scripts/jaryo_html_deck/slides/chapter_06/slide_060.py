from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        60,
        title="4. GAN-Style: 생성자와 평가자를 분리한다",
        shell="process-flow-shell",
        source_section="06",
        source_block="06-07",
        key_claim="생성과 평가는 같은 손에 묶지 않음",
        chapter_label="CHAPTER 06",
        notes_intent="Planner/Generator/Evaluator loop",
        notes="source lines 96-108, page 064 feedback-loop reference",
        body={
            "variant": "chapter-feedback-loop",
            "roles": [
                {"index": "Planner", "title": "제품 스펙과 작업 범위", "text": "사용자 요청 확장"},
                {"index": "Generator", "title": "기능 또는 스프린트", "text": "한 번에 하나씩 구현"},
                {"index": "Evaluator", "title": "테스트·브라우저·루브릭·리뷰", "text": "별도 관점으로 평가"},
            ],
            "feedback": "구체적인 피드백을 다시 Generator에게 돌려보냄",
            "conclusion": "생성과 평가는 같은 손에 묶지 않음",
        },
    )
