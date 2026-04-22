from __future__ import annotations

from jaryo_html_deck.model import SlideSpec, make_slide


def build() -> SlideSpec:
    return make_slide(
        69,
        title="시작하며: 두 가지 막다른 길",
        shell="split-compare-shell",
        source_section="07",
        source_block="07-01",
        key_claim="출발점은 원리를 시스템이 대신 강제하게 만드는 일",
        chapter_label="CHAPTER 07",
        notes_intent="두 dead-end split comparison",
        notes="source lines 3-9, page 070 reference",
        body={
            "left_label": "모든 것을 직접 세팅",
            "left_points": ["명령어를 매번 손으로 조합", "검증 루프를 기억에 의존", "세션마다 비슷한 지시를 다시 입력"],
            "right_label": "원리 없이 Skills·플러그인·프리셋",
            "right_points": ["이상 동작이 나오면 원인을 읽지 못함", "시간이 지나면 팀에 블랙박스만 남음", "원리가 아니라 도구만 축적"],
            "opinion": "어떤 원리를 시스템이 대신 강제하게 만들 것인가",
        },
    )
