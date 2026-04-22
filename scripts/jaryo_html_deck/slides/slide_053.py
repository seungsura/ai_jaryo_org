from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        53,
        title="신뢰는 조율되어야 한다",
        shell="statement-editorial-shell",
        source_section="05",
        source_block="05-07",
        key_claim="자율성은 작업 비용에 맞춰 조절해야 한다",
        chapter_label="CHAPTER 05",
        notes_intent="Calibrated Trust를 비용 구간으로 압축",
        notes="source markdown의 Calibrated Trust 문단",
        body={
            "variant": "calibrated-trust-scale",
            "claim": "신뢰는 감정이 아니라 운영 문제",
            "zones": [
                {
                    "title": "넓은 자율성",
                    "items": [
                        "초안 작성",
                        "반복 리팩터링",
                        "구조 탐색",
                    ],
                },
                {
                    "title": "강한 검증",
                    "items": [
                        "배포",
                        "삭제",
                        "민감 데이터",
                        "최신 API",
                        "외부 인용",
                        "보안 코드",
                    ],
                },
            ],
            "warning": "똑똑함 ≠ 그대로 믿어도 됨",
        },
    )
