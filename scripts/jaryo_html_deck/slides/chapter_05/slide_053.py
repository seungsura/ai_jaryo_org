from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        53,
        title="더 긴 컨텍스트보다 더 좋은 게이트",
        shell="statement-editorial-shell",
        source_section="05",
        source_block="05-09",
        key_claim="더 긴 컨텍스트보다 더 좋은 게이트",
        chapter_label="CHAPTER 05",
        notes_intent="05장 결론을 source-backed gate principle로 마무리",
        notes="source markdown의 conclusion block",
        body={
            "variant": "closing-gate",
            "claim": "누적되는 루프에는 통제 구조가 필요",
            "supports": [
                {
                    "title": "조용히 커지는 것",
                    "text": "작은 오류는 조용히 커짐",
                },
                {
                    "title": "앞쪽 게이트",
                    "text": "기계가 확인할 것은 앞쪽 게이트로",
                },
                {
                    "title": "AI의 자리",
                    "text": "AI는 판단과 생성에 집중",
                },
            ],
        },
    )
