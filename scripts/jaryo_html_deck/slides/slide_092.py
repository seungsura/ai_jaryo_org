from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        92,
        title="시작하며: FOMO 와 피로",
        shell="statement-editorial-shell",
        source_section="09",
        source_block="09-01",
        key_claim="더 많은 정보를 읽는 일이 아니라 직접 써 보는 일",
        chapter_label="CHAPTER 09",
        notes_intent="FOMO와 피로를 직접 써 보기로 연결",
        notes="source 09 lines 1-7; canonical Page 084",
        body={
            "variant": "summary-cards",
            "quote": "\"지식이 쌓이는 속도보다 감가상각되는 속도가 더 빠르다. 나도 지쳤다.\"",
            "cards": [
                {
                    "eyebrow": "Simon Willison, 2025",
                    "title": "최전선의 피로",
                    "lines": ["AI FoMO", "무엇을 남기고 무엇을 버릴지"],
                },
                {
                    "eyebrow": "FOMO-AI • 2025",
                    "title": "뒤처지는 두려움",
                    "lines": ["뒤처질까 두려움", "좋은 도구를 못 쓸까", "남들만 이득 볼까", "직접 써 보는 일"],
                },
            ],
        },
    )
