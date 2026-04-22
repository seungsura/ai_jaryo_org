from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        54,
        title="결정 제어와 확률 제어를 분리하라",
        shell="split-compare-shell",
        source_section="05",
        source_block="05-08",
        key_claim="기계가 확인할 것은 기계에게, 유연한 판단은 AI에게",
        chapter_label="CHAPTER 05",
        notes_intent="결정론적 제어와 확률적 제어의 분리",
        notes="source markdown의 deterministic / probabilistic control 구분",
        body={
            "variant": "control-gate-board",
            "claim_parts": [
                "기계가 확인할 것은 기계에게",
                "AI는 판단과 생성에 집중",
            ],
            "left_title": "결정론적 제어",
            "right_title": "확률적 제어",
            "left_items": [
                "린트",
                "타입 체크",
                "테스트",
                "포맷",
                "위험 명령 차단",
                "파일 권한",
                "승인 게이트",
            ],
            "right_items": [
                "설계 대안 제안",
                "코드 리뷰 의견",
                "아키텍처 판단",
                "요약",
                "우선순위 평가",
            ],
        },
    )
