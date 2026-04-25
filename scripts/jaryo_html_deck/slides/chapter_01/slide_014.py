from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        14,
        title="그래도 기초가 중요하다",
        shell="statement-editorial-shell",
        source_section="01",
        source_block="01-06",
        key_claim="AI 코딩은 에이전트가 일할 환경을 설계하고 검증하는 영역",
        chapter_label="CHAPTER 01",
        density="light",
        notes_intent="reference layout 기반 quote and summary cards",
        notes="source markdown의 기본기와 시스템 이해 문단",
        body={
            "variant": "summary-cards",
            "quote": "AI가 더 많이 해줄수록 기초 지식을 가진 사람의 경쟁력 상승",
            "cards": [
                {
                    "eyebrow": "변하는 것",
                    "title": "직접 코드를 타이핑하는 비중",
                    "lines": ["줄어든 것은 타이핑의 비중"],
                },
                {
                    "eyebrow": "변하지 않는 것",
                    "title": "시스템을 이해하는 능력",
                    "lines": ["안전성 · 유지보수성 · 기존 시스템 적합성", "인증과 권한 · 동시성 · 데이터베이스 스키마 · 캐싱"],
                },
            ],
        },
    )
